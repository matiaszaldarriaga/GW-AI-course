# Figure: the C_l penalty relative to a coherent scan is modest

**File:** `paper_v2/figures/cl_vs_scan_penalty.pdf` (Sec. VI, `fig:cl_penalty`).
**Generator:** `paper_v2/scripts/fig_cl_vs_scan_penalty.py` (fixed/common
Monte Carlo variates; numeric sidecar
`paper_v2/data/detection_penalty_mc.json`). **Updated 2026-08-11.**

The deterministic rerun gives scan/$C_\ell$ ratios
$1.0000\pm0$, $1.0831\pm0.0048$, $1.1384\pm0.0051$, and
$1.2072\pm0.0038$ at $L=1,2,3,4$. Equality at $L=1$ is exact; error bars are
batch standard errors from the same common-variate threshold inversions used
for the registered numbers.

## Caption (expanded)

Two panels.

**Left:** the source amplitude required to detect via the one-parameter Poisson
$C_\ell$ statistic, relative to an unknown-direction coherent scan, versus
angular resolution $L$ ($K_L=L(L+2)$ modes). Squares: analytic non-central-$\chi^2$
thresholds (the $K_{\rm eff}=K_L$ approximation), ratio
$1.13,1.16,1.21,1.27,1.33,1.38$ for $L=1\ldots6$. Circles: honest
maximum-over-sky Monte Carlo, $1.00,1.07,1.15$ for $L=1,2,3$ — at $L=1$ the scan
max equals $\sqrt{C_1}$, so the two searches are literally the same test. The
analytic curve over-states the low-$L$ penalty because it treats the $K_L$ beams
as independent.

**Right:** the brightest-source fraction $p_1$ needed for a $50\%$ detection at
false alarm $0.05$, versus the background SNR $\rho_0$, for the scan and the
Poisson $C_\ell$ at resolution $L\le2$. The shaded band marks $p_1\sim0.6$ — the
fraction a dipole at the NANOGrav $95\%$ "limit" would require
([[../concepts/brightest_source_fraction]], Sec. IV). For $\rho_0\simeq20$ a
source with $p_1\gtrsim0.09$ is detectable; the $C_\ell$ penalty is $\sim15\%$.

## Concepts illustrated

- [[../sources/pta_point_source_multipole]] — the detection comparison.
- [[../concepts/fisher_hierarchy]] — modest **detection** penalty vs. the large
  **estimation** ($\sigma_p$) penalty; the figure is the detection side.
- [[../concepts/matched_filter_vs_power]] — scan (linear) vs $C_\ell$ (quadratic).

## Inputs / reproduce

- Inputs: none (uses `detection_penalty_table`, `monte_carlo_required_rho`,
  `required_p1`).
- `conda run -n gw_pta python paper_v2/scripts/fig_cl_vs_scan_penalty.py`

## Used in

- `paper_v2/sections/source_detection.tex`, Sec. V (`fig:cl_penalty`).
