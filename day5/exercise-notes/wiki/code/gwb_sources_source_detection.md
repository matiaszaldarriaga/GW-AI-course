# `gwb_sources/source_detection.py`

Detectability of a single bright source versus its angular power spectrum — the
computational backbone of paper-v2 Sec. V. Added 2026-06-23 and remediated
2026-08-11. Unit-tested in `tests/test_source_detection.py` (8 tests); all
numbers reproduced by `paper_v2/scripts/verify_source_vs_cl.py` and the
deterministic detection sidecar.

## Purpose

Turns the claims of [[../sources/pta_point_source_multipole]] into tested code:
the coherent source-SNR coefficients $\alpha_{\rm ps},\alpha_L$ from the real PTA
antenna response, the coherent-scan-vs-Poisson-$C_\ell$ detection thresholds,
and the Neyman–Pearson equivalence of the coherent and covariance single-source
tests.

## Public API (exported from `gwb_sources`)

| Function | Returns | Notes |
|---|---|---|
| `real_sph_design(theta, phi, lmax, include_monopole)` | `(Y, keys)` | real orthonormal SH design matrix; orthonormal under HEALPix quadrature |
| `alpha_ps_analytic()` | dict | closed form: $\langle\gamma_s^2\rangle=1/18$, $\langle\Gamma_0^2\rangle=1/108$, `alpha_ps2`$=5$ |
| `pair_alpha_coefficients(n_pulsars, lmax, source_dir, seed, nside)` | `{alpha_ps2, alpha_L2}` | identity-metric (white-noise) pair templates from `z_plus`/`z_cross` |
| `rho_scan_req(K, pfa, p_det)` | float | $\Phi^{-1}(1-p_{\rm fa}/K)+\Phi^{-1}(p_{\rm det})$ |
| `rho_cl_req(K, pfa, p_det)` | float | exact non-central $\chi^2_K$ threshold inversion |
| `detection_penalty_table(L_values, pfa, p_det)` | rows | $(L,K,\rho_{\rm scan},\rho_{C_\ell},{\rm ratio})$ — `tab:detection` |
| `required_p1(rho0, alpha, K, pfa, p_det)` | `(p1_scan, p1_cl)` | $p_1=\rho_{\rm req}/(\alpha\rho_0)$ |
| `monte_carlo_required_rho(L, ...)` | `(K, rho_scan, rho_cl)` | honest max-over-sky scan vs $\lVert x\rVert^2$ |
| `single_template_equivalence(rho, pfa, ...)` | `(pd_coh, pd_cov)` | NP monotone equivalence demo (equal $P_{\rm det}$) |

## Key algorithms / formulas

- **alpha from templates.** Builds pair templates $\Gamma_0$ (HD, = sky-average
  of the pair response), $\gamma_s$ (point source), and
  $\Gamma_{\ell m}=\int Y_{\ell m}\gamma\,d\Omega$ over a HEALPix grid; the
  noise-dominated (equal-noise white) limit makes the pair inner product the
  plain pair average. $\alpha_L^2=(P_\perp T_L,P_\perp T_L)/(\Gamma_0,\Gamma_0)$.
  Backlink [[../formulas#source-detection]].
- **Detection thresholds.** Scan = max over $\sim K$ Gaussian beams; $C_\ell$
  statistic $\lVert x\rVert^2\sim\chi^2_K(\rho^2)$. See
  [[../sources/pta_point_source_multipole]].
- **NP equivalence.** Coherent $s\sim\chi^2_1(\rho^2)$; covariance profiled LR
  $T_\star=\max(s-1-\ln s,0)$ monotone in $s$ ⇒ identical $P_{\rm det}$.

## Known gotchas

- `z_plus`/`z_cross` have a removable $0/0$ at the source antipode; the module
  uses `np.nan_to_num` on a fine grid (the singularity is integrable).
- `pair_alpha_coefficients` is the **identity-metric** (white-noise-dominated)
  limit. The paper's `s_L` benchmark instead puts the background *in* the
  covariance (the $1+(N_p-1)/48$ factor); the two agree only asymptotically
  ($\alpha_{\rm ps}^2=\sum s_L\to5$). Quote $\sqrt5$ as the large-array ideal.
- $\alpha_L$ depends on the random array and source direction; figures average
  over several configurations.

## Consumers

- `paper_v2/scripts/fig_source_snr_vs_resolution.py` → `source_snr_vs_resolution.pdf`
- `paper_v2/scripts/fig_cl_vs_scan_penalty.py` → figure plus
  `paper_v2/data/detection_penalty_mc.json`
- `paper_v2/scripts/verify_source_vs_cl.py` → full numerical report
- `tests/test_source_detection.py`

## 2026-08-11 deterministic threshold calibration

`monte_carlo_required_rho` now creates fixed common null/signal variates once,
uses a deterministic bisection of the resulting empirical power curve, and
reports standard errors from eight batch inversions. It no longer draws fresh
random numbers inside a root objective. The $L=1$ scan and norm statistics are
the same statistic and are enforced as bitwise-identical in code and tests.

For the production calibration the scan/$C_\ell$ threshold ratios are
$1.0000\pm0$ ($L=1$), $1.0831\pm0.0048$ ($L=2$),
$1.1384\pm0.0051$ ($L=3$), and $1.2072\pm0.0038$ ($L=4$). These are numerical
calibrations of the accepted equal-noise benchmark; they do not change the
$\alpha_{\rm ps}^2=5$ or $\rho_{\rm ps}=\sqrt5\,p_1\rho_0$ interpretation.
