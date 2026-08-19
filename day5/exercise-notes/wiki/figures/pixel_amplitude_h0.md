# Figure: Brightest individual-source amplitude vs the NANOGrav CW limit

**File:** `paper_v2/figures/pixel_amplitude_h0.pdf`
**Ingested:** 2026-06-22
**Updated:** 2026-08-12 (real frequency-dependent sky-averaged limit curve;
decision MZ-11)

## What it shows

A three-panel full-width figure (paper Fig. 8), one panel per $\varepsilon$
model, modeled on Fig. 6 ("fig:limits") of the Goncharov et al. joint
resolved+unresolved search ([[sources/joint_search_resolved_unresolved]]). The
quantity is the brightest individual source in the complete schema-v2 ledger,
converted from its stored characteristic-strain-squared to strain amplitude

$$h_0 = \sqrt{h_s^2/(f\,T_{\rm obs})}, \qquad T_{\rm obs} = 16.03\,{\rm yr},$$

scattered against GW frequency. Solid median and dotted 95th-percentile curves
use all 10,000 realizations; only the dots use a fixed 400-realization subset.
The conversion uses the exact relation $h_s^2 = h_0^2\,(f/\Delta f)$ between the
per-source characteristic strain (which already carries the $f/\Delta f$ factor)
and the inclination/polarization-averaged CW amplitude $h_0$, from
[[sources/arxiv_2406_17010]] (Eqs. tildehs2, h0). No blended pixel is labeled
as an individual source.

## The plotted limit (changed 2026-08-12)

The dashed black curve is the **sky average over the 192 pixels** of
`UL_skies` in `paper_v2/data/15yr_cw_3d_limits_v4.npz`, the public data release
of the NANOGrav 15-yr individual-source search (Agazie et al. 2023, ApJL 951
L50, [arXiv:2306.16222], `NANOGrav:2023individual`) — the analysis behind the
cyan binned line of Goncharov et al. Fig. 6. It is drawn at the geometric bin
centres $\sqrt{F_{\rm edges}[i]F_{\rm edges}[i+1]}$ over the file's own support
and is never extrapolated. Provenance, SHA-256 and fetch command:
[[reproducibility]].

Before this change the figure carried only the single verified best point,
$h_0 = 8\times10^{-15}$ near 6 nHz, drawn as a star, and the caption spent five
lines asserting the frequency dependence in words. The curve replaces both.

Read off the file, the sky-averaged limit runs

| $f$ | sky-averaged 95% UL on $h_0$ |
|---|---|
| 1.08 nHz (0.034 yr$^{-1}$, first bin centre) | $5.2\times10^{-14}$ |
| 2.72 nHz ($\approx$ lowest paper frequency) | $1.30\times10^{-14}$ |
| 5.89 nHz | $7.4\times10^{-15}$ |
| 8.01 nHz (deepest bin) | $6.4\times10^{-15}$ |
| 27.5 nHz (0.868 yr$^{-1}$, last bin centre) | $1.00\times10^{-14}$ |

### Two things the caption must keep saying

1. **It is sky-averaged, not a position-independent bound.** At the lowest
   paper frequency the per-pixel limit spans $5.2\times10^{-15}$ to
   $2.7\times10^{-14}$ about a sky mean of $1.30\times10^{-14}$ — a factor of
   five across the sky.
2. **It is not the published curve, and the reason is now established (2026-08-12).**
   The sky average of this file is $7.4\times10^{-15}$ at 5.9 nHz while
   Ref. `NANOGrav:2023individual` quotes $8\times10^{-15}$ at 6 nHz. That is
   **not a discrepancy: they are two different estimators, and the paper says
   so.** Its Sec. IV.1: *"the sky-averaging is not done uniformly on the sky,
   but rather through the posterior samples, which in practice results in the
   all-sky limit being biased high. In this example $\sim$73% of the sky gives
   a lower upper limit than the all-sky value."* The published number is the
   **sky-marginalized** limit — the 95th percentile of the pooled $h_0$
   posterior samples, with the source position a free MCMC parameter. This
   file is the **fixed-sky** limit as a function of position, released
   separately *"to allow follow-up studies to use the full search results"*.
   The published $8\times10^{-15}$ is retained in Table II
   (`tab:source_ratio`), where it is quoted as a published number, and the
   plotted curve is never described as the published curve.

### The published all-sky limit, reproduced (2026-08-12)

No external party was needed. The same repository ships the posterior samples
(`data/15yr_quickCW_UL.h5`, 90 MB) and the estimator
(`UL_analysis.ipynb`: bin the samples in frequency, take the 95th percentile
of $h_0$ in each bin, no sky weighting). Applying it reproduces the headline
number:

| | |
|---|---|
| most sensitive bin | 11 (5.4506–6.3590 nHz, geometric centre **5.887 nHz**) |
| reproduced all-sky 95% UL there | **8.227e-15** |
| published | $8\times10^{-15}$ at "our most sensitive frequency of 6 nHz" |
| uniform pixel mean of `UL_skies[11]` (what this figure plots) | 7.367e-15 |
| ratio all-sky / pixel-mean | 1.117 (all-sky weaker, as the paper predicts) |
| sky fraction with a deeper limit than the all-sky value | 69.8% (paper: "$\sim$73%") |

Two independent consistency checks passed: the reproduced curve's minimum
falls in the bin the paper calls its most sensitive, and `F_edges` in this npz
is bit-identical to the first 23 edges of the 37-bin ladder used in
`UL_analysis.ipynb` (max relative difference exactly 0.0).

The all-sky curve is weaker than the pixel mean in **every** bin (ratio 1.03
to 1.53), so plotting it instead would only widen the margin in Sec. IV C:
max(95th pct / limit) would move 0.290 → 0.255, 0.504 → 0.429, 0.898 → 0.764
for $\varepsilon = 0.20/0.38/0.66$. It has one drawback: at bin 22
(32.09 nHz $= 1.013\,{\rm yr}^{-1}$) the all-sky limit spikes to
$1.4\times10^{-12}$, the annual timing-model hole — a fit artifact sitting
exactly at the right-hand edge of this figure. The released sky map stops at
29.7 nHz, just short of it.

**Open choice, not an open question** (see `todo.md`): which of the two
curves Fig. 8 should show. Decision MZ-11 option A specified this one (the
sky average of the public file); MZ's own words in the annotation pointed at
the cyan line of Ref. `Goncharov:2026joint` Fig. 6, which is the all-sky
limit. Both are defensible and the paper's conclusion holds under either.

## The comparison, and the scientific statement it changed

Over the support of the public grid, no model reaches the limit at any
frequency. Computed by `fig_pixel_amplitude.py` and written to
`paper_v2/data/cw_limit_comparison.json`:

| $\varepsilon$ | max(95th pct / limit) | at $f$ | max(median / limit) | at $f$ |
|---|---|---|---|---|
| 0.20 | 0.290 | 0.215 yr$^{-1}$ | 0.114 | 0.085 yr$^{-1}$ |
| 0.38 | 0.504 | 0.085 yr$^{-1}$ | 0.185 | 0.085 yr$^{-1}$ |
| 0.66 | 0.898 | 0.085 yr$^{-1}$ | 0.245 | 0.085 yr$^{-1}$ |

Against the single best point the draft had said the heaviest-tailed model
"only marginally" clears the limit, and hedged in four places ("except in the
tail of the most heavy-tailed model"). Against the real curve the statement is
simpler and stronger: **every model stays below the sky-averaged limit at every
frequency**, closest at the lowest frequency of the $\varepsilon = 0.66$ model
where the 95th percentile reaches 90% of it. All four hedges were removed on
2026-08-12; see the `log.md` entry of that date.

At $f=0.085\,{\rm yr}^{-1}$ the underlying medians are
$1.48/2.42/3.19\times10^{-15}$ and the 95th percentiles are
$3.49/6.57/11.7\times10^{-15}$ for $\varepsilon=0.20/0.38/0.66$.

## Generator

`paper_v2/scripts/fig_pixel_amplitude.py` (updated 2026-08-12; imports the
shared style module `paper_v2/scripts/_paperstyle.py` via `apply_style()`,
`figsize_2col`, and the `EPS_MODELS` color/label map).
Run: `conda run -n gw_pta python paper_v2/scripts/fig_pixel_amplitude.py`.
Reads `brightest_source_power` from each compact full-moment population
product, converts all 10,000 values per frequency to
$h_0 = \sqrt{h_s^2/(f\,T_{\rm obs})}$ with `TOBS_YR = 16.03`, and selects 400
indices only for scatter. It is the sole writer of the sidecar
`paper_v2/data/cw_limit_comparison.json`, which
`paper_v2/scripts/compute_paper_numbers.py` reads to register the
`cw_limit_*` and `h0_over_cwlimit_*` number keys.

## Inputs

- `new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps{020,038,066}.npz`
  — complete-ledger `brightest_source_power`, `fmean_per_year`, and `h2c_vs_f`
  with matched-normalization $\phi_\sigma$.
- `paper_v2/data/15yr_cw_3d_limits_v4.npz` — tracked external grid; see
  [[reproducibility]] for source, SHA-256 and fetch command.

## Concepts illustrated

- [[concepts/brightest_source_fraction]] — the absolute brightest-source
  strain $h_0$ and the ratio $R$ (`eq:R_ratio`).
- [[concepts/SMBH_population_model]] — the $h_s^2\leftrightarrow h_0$ relation
  and the matched amplitude normalization.

## Caveats / citation

- The reference figure is Fig. 6 of Goncharov et al. 2026, on
  **arXiv:2606.18241**, keyed `@misc{Goncharov:2026joint}` (the companion joint
  resolved+unresolved search; [[sources/joint_search_resolved_unresolved]]).
- The limit grid traces to the NANOGrav 15-yr individual-source
  (continuous-wave) search, **arXiv:2306.16222** (Agazie et al. 2023, ApJL 951
  L50), keyed `@article{NANOGrav:2023individual}`. (Not to be confused with
  2306.16221, the separate GWB-anisotropy paper.)

History of the plotted constraint: flat $h_0 = 10^{-14}$ until 2026-06-24;
the verified deepest point $8\times10^{-15}$ near 6 nHz with a star from
2026-06-24; the sky-averaged frequency-dependent curve from the public grid
since 2026-08-12.

## Paper sections using this figure

- `paper_v2/sections/dipole_source.tex`, subsection "The brightest source in
  absolute terms" (`\label{fig:pixel_amplitude}`); figure 8 in the paper.
  Companion to Table II (`tab:source_ratio`).

## Related pages

- [[figures/source_content_estimators]] — the relative ($p_1$, $N_{\rm eff}$)
  view of the same realizations.

---

```json
{"slug": "pixel_amplitude_h0", "concepts": ["brightest_source_fraction", "SMBH_population_model"], "generator": "paper_v2/scripts/fig_pixel_amplitude.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps*.npz", "paper_v2/data/15yr_cw_3d_limits_v4.npz"], "paper_uses": ["paper_v2/sections/dipole_source.tex, fig:pixel_amplitude"], "cites": ["NANOGrav:2023individual (2306.16222, sky-averaged 95% UL grid)", "Goncharov:2026joint (2606.18241, reference figure)"]}
```
