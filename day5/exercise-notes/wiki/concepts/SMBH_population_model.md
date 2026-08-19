# SMBH population model

The astrophysical input that produces source realizations for the GW
background. Different choices of mass function and scatter determine
$p_1$, $N_{\rm eff}$, and the full distribution of $C_1/C_0$.

## Framework

Start from an observed stellar/kinematic tracer of galaxies and convert
to SMBH masses:

1. **Velocity-dispersion route** (Sato-Polito + Zaldarriaga + Quataert,
   arxiv 2312.06756): start with the galaxy velocity dispersion
   function (VDF), convert to SMBH masses via the $M$–$\sigma$ relation
   with log-normal scatter $\varepsilon$ (in dex).

2. **Stellar-mass route** (Liepold + Ma, arxiv 2407.14595): start
   directly from the galaxy stellar mass function (GSMF) and apply the
   $M_{\rm BH}$–$M_\ast$ relation. A revised high-mass tail from the
   MASSIVE survey shifts the resulting BHMF upward.

Integrate over mass ratio and redshift to get the GWB luminosity
function $\bar N(f,M)\,h_s^2(f,M)$. The total characteristic strain
and its anisotropy are built from this.

## The scatter parameter $\varepsilon$

Log-normal scatter around the $M$–$\sigma$ relation. Governs the
high-mass tail of the BHMF.

- $\varepsilon$ larger → more ultra-massive SMBHs per galaxy-sigma bin
  → louder, more anisotropic background.
- Closed-form scatter boost (Sato-Polito + Zaldarriaga + Quataert,
  their Eq. after MF_scatter):
  $$\rho_{\rm BH} = \rho_{\rm BH,0}\,\exp\!\bigl(\tfrac12\,\varepsilon^2\ln^2 10\bigr),$$
  $$h_c^2 = h_{c,0}^2\,\exp\!\bigl(\tfrac{25}{18}\varepsilon^2\ln^2 10\bigr).$$

## Three scenarios used in this project

| $\varepsilon$ | $\log_{10}(M_{\rm peak}/M_\odot)$ | Comment |
|---:|---:|---|
| 0.20 | 9.2 | Low-scatter; narrow mass function |
| 0.38 | 9.5 | Fiducial (SPZ 2025dist nominal value) |
| 0.66 | 10.6 | High-scatter; heavy-tailed |

## The distribution, not just the mean

Two papers in the source tree make this precise:

- [[../sources/arxiv_2406_17010]] (SPZ 2025dist, **the direct precursor
  to this project**) introduces the **characteristic-function method**
  to get the full pdf of $h_c^2$:
  $$\hat P(\omega) = \exp\!\left[\int dh_s^2\,
  \frac{dN}{dh_s^2}\,(e^{i\omega h_s^2}-1)\right].$$
  The result is universally a **Gaussian core** (many faint sources) plus
  a **power-law tail** (rare bright sources, shape = luminosity function).
  This is the foundation for the brightest-source-dominated picture.

- [[../sources/arxiv_2407_06270]] (Lamb + Taylor) gives moment scalings
  across frequency bins. The variance-to-mean ratio is lambda-independent
  (decouples from binary hardening physics), making it a clean
  Poissonian-finite-N diagnostic.

## Mean vs median strain

Project's own Monte Carlo result (from
`notebooks/guide_model_comparison.py`, documented in `astrophysical_model.tex:70`):

- $\varepsilon=0.66$: median $h_c^2$ is $\sim 57\%$ of the analytic mean at the lowest frequency.
- $\varepsilon=0.20$: median is $\sim 99\%$ of mean.

Physical interpretation: high-scatter models have enough rare-bright-source
realizations that the ensemble mean is far above the typical draw. This is
**the most informative near-term observable** (per `discussion.tex`), and
it does not require any anisotropy measurement.

**Caveat:** the precise 57% value is a project-computed number from our
Monte Carlo, not a quoted result from SPZ 2025dist. See `notebooks/guide_model_comparison.py` for the source.

## The "missing big black holes" tension

[[../sources/arxiv_2312_06756]] (SPZQ) argues that reproducing the
observed NANOGrav amplitude requires $M_{\rm peak}^{\rm GW} \sim 3\times
10^{10}\,M_\odot$, about $10\times$ heavier than EM surveys directly
confirm. Implications:

- Either there is a population of ultra-massive SMBHs missed by current
  EM surveys, or the nominal $M$–$\sigma$ relation at high mass needs
  revision.
- Liepold + Ma ([[../sources/arxiv_2407_14595]]) argues the tension
  mostly disappears if one uses the revised stellar-mass function
  instead: their GSMF-based BHMF is consistent with current PTA
  amplitudes with $M_{\rm BH}\sim 1$–$3\times 10^9\,M_\odot$ dominating,
  not ultra-massive objects. Different approach, same observational
  constraint.

This dichotomy — low-scatter / $\sim 10^9 M_\odot$-dominated vs
high-scatter / $\sim 10^{10}M_\odot$-dominated — is **exactly what the
project's $\varepsilon$-scan probes**. The choice controls $p_1$ and
$N_{\rm eff}$ and therefore all anisotropy observables.

## Frequency structure

From the spectrum (Sato-Polito + Kamionkowski,
[[../sources/arxiv_2305_05690]]), the GW-driven inspiral limit gives
$C_\ell/C_0 \propto 1/[1+(f/f_\ast)^{-11/3}]$: flat at high frequency
(source-limited) and suppressed at low frequency (more sources contribute,
$N_{\rm eff}$ larger).

## Source pages (arxiv)

- [[../sources/arxiv_2312_06756]] — population model: VDF + $M$–$\sigma$ scatter, missing-BH argument. **Cited in `introduction.tex:10`, `astrophysical_model.tex:7, 22`.**
- [[../sources/arxiv_2406_17010]] — **the precursor** to this project. Characteristic-function method, Gaussian-core + tail. **Cited in `astrophysical_model.tex:25`, `discussion.tex:25`.**
- [[../sources/arxiv_2407_14595]] — alternative stellar-mass-based BHMF. **Cited in `introduction.tex:10`.**
- [[../sources/arxiv_2305_05690]] — C_l spectrum from SMBHB populations. **Cited in `introduction.tex:17`.**
- [[../sources/arxiv_2407_06270]] — spectral variance moments. **Cited in `discussion.tex:25`.**
- [[../sources/arxiv_2608_09929]] — Lin, Lidz & Ma 2026b: Monte Carlo realizations of LM24 (Liepold & Ma) and SZQ; quantifies $z_{\rm min}\in[0.005,0.2]$ (median insensitive, mean $h_c^4$ sensitive), $M_{\rm BH,max}=10^{10.5}M_\odot$, and a mass-independent stellar-hardening residence time ($f_b=5$ nHz, $\kappa=10/3$) that suppresses $h_c^2\propto f^2$ below the bend. Their LM24 is *not* renormalized to a fixed GWB amplitude, unlike our three $\varepsilon$ models — see the comparison table in that page before quoting either against the other.
- [[../sources/joint_search_resolved_unresolved]] — Goncharov et al. 2026: recasts $(N_{\rm c},h_{\rm c})\leftrightarrow(\rho_{\rm BH},M_{\rm peak})$ via the saddle-point log-normal strain number-count; quasi-invariant $\mu(x)=N_{\rm c}^{-1}\,dN/d\log x$; proposes $N_{\rm c}$ ($N_{\rm c}\ge1000$ Gaussian null) as the SMBHB-origin detection statistic on NG15.

## Paper uses

- `astrophysical_model.tex` — the entire section.
- `distribution_c1c0.tex` — realizations drawn from this model.
- `discussion.tex` — heavy-tailed distribution as key observational diagnostic; "missing BHs" argument.
- `introduction.tex` — population model as motivation for the anisotropy discussion.

## Implementation

Python package modules:
- [[../code/gwb_sources_population]] — VDF, $M$–$\sigma$, BHMF, $h_c^2$ per bin
- [[../code/gwb_sources_sources]] — Poisson realization generator with single-RNG invariant
- [[../code/gwb_sources_strain_stats]] — FFT characteristic-function PDF of $h_c^2$ (SPZ 2025dist method)

Notebooks:
- [[../notebooks/guide_population_and_spectra]] — population walkthrough
- [[../notebooks/guide_model_comparison]] — 3-$\varepsilon$ scan; verifies 57% median/mean at $\varepsilon=0.66$
- [[../notebooks/guide_interactive]] — CDF-based fast realizations

Batch scripts:
- [[../code/scripts_run_population]] → [[../results/population_analysis_eps020]], [[../results/population_analysis_eps038]], [[../results/population_analysis_eps066]]

## Related concepts

[[N_eff]], [[brightest_source_fraction]], [[shot_noise]],
[[dipole_distribution]].
