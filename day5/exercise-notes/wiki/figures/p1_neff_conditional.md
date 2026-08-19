# Figure: source content of a large dipole

**File:** `paper_v2/figures/p1_neff_conditional.pdf`
**Created:** 2026-06-19 (Section IV, `fig:p1_neff_conditional`)

> **Full-moment update (2026-08-11).** The conditioning variable is the direct
> $x=|\mathbf D|^2/Q^2$. The displayed $p_1$ comes from the complete individual
> ledger, while $N_{\rm eff}=Q^2/S_2$ includes the unresolved all-source second
> moment. The plotted inverse relation is therefore an empirical conditional
> result, not an algebraic inversion of $E[x\mid\{p_a\}]$.

> **Palette exception (2026-08-12, decision GS-09).** Color in this figure
> encodes **frequency**, not the $M$--$\sigma$ scatter $\varepsilon$. Every
> other model-resolved figure keeps the project convention
> (`_paperstyle.EPS_COLORS`), but this panel shows a single
> $\varepsilon = 0.66$ model, so the convention carried no information here
> and cost legibility: all six curves came out the same green, which is what
> GS-P flagged. The palette (`FREQ_COLORS`) is local to
> `fig_p1_neff_conditional.py` and chosen away from `EPS_COLORS`; line style
> still encodes frequency too, so the panel survives grayscale, and shade
> still separates Monte Carlo from the analytic reweighting. The caption says
> so. Recorded as an exception in [[conventions]] so it is not read as drift.

## What it shows

Two-panel (`figure*`, full width) figure for the most anisotropic model
($\varepsilon = 0.66$), at the three Table II / Fig. 4 frequencies
($f \approx 0.085,\,0.28,\,1.0$ /yr), conditioned on $C_1/C_0 > 0.2$ (the
NANOGrav 95% value):

- **Left:** distribution of the brightest-source fraction $p_1$. Peaks at
  $p_1 \sim 0.5$–$0.6$ with a tail to 1.
- **Right:** distribution of the effective number of sources
  $N_{\rm eff} = 1/\sum_a p_a^2$ (log axis). Peaks at $N_{\rm eff}\sim 2$–$3$.

Solid = Monte Carlo; dashed = the prediction of Eq. `eq:p1_given_x`, obtained by
**importance-reweighting** each Monte-Carlo realization by its exceedance
probability $S(0.2\mid p_1,\eta) = P(C_1/C_0 > 0.2\mid p_1,\eta)$ (the survival
function of the one-source + Gaussian, i.e. noncentral $\chi^2_3$, forward law).
Only the forward law $S$ is analytic; the priors $\pi(p_1)$, $P(\eta\mid p_1)$
are supplied by the Monte Carlo itself. The two agree, and the conditional
distributions are nearly model- and frequency-independent (the universality of
[[source_content_estimators]]). Message: a dipole above the current "limit"
requires the brightest source to carry $\sim 60\%$ of the power, with only
$\sim 3$ effective sources. This is figure 7 in the paper (after the new
estimator figure was inserted as Fig. 6).

For the corrected $\varepsilon=0.66$ lowest-frequency selection, 1,796 of
10,000 realizations exceed 0.2 and give
$\langle p_1\rangle=0.605\pm0.18$,
$\langle N_{\rm eff}\rangle=3.20\pm1.8$, and
$\langle\eta\rangle=0.0146$. Across all valid Table-II cells at this threshold,
the means span $p_1=0.58$--0.62 and $N_{\rm eff}=3.1$--3.4.

## Generator

`paper_v2/scripts/fig_p1_neff_conditional.py` (updated 2026-08-11).
Run: `conda run -n gw_pta python paper_v2/scripts/fig_p1_neff_conditional.py`.
Uses `scipy.stats.ncx2` for the exceedance weights.

## Inputs

- `new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps066.npz`
  — direct $C_1/C_0$, $Q$, $S_2$, complete-ledger $p_1$, and frequency grid.

## Concepts illustrated

- [[concepts/brightest_source_fraction]] — $\langle p_1\mid x\rangle\simeq\sqrt{x}$.
- [[concepts/N_eff]] — $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$.
- [[concepts/dipole_distribution]] — Bayesian inverse of the forward laws.

## Paper sections using this figure

- `paper_v2/sections/dipole_source.tex`, subsection "The source content of a
  given dipole" (`fig:p1_neff_conditional`, alongside Table `tab:conditional`).

## Related pages

- [[../notebooks/guide_power_anisotropy]] §10e–10f — interactive version (the
  joint density, conditional $P(p_1\mid C_1/C_0)$ and $P(N_{\rm eff}\mid C_1/C_0)$).
- [[c1c0_distribution]] — the forward-law figure (Fig. 4) this complements.

---

```json
{"slug": "p1_neff_conditional", "concepts": ["brightest_source_fraction", "N_eff", "dipole_distribution"], "generator": "paper_v2/scripts/fig_p1_neff_conditional.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps066.npz"], "paper_uses": ["paper_v2/sections/dipole_source.tex, fig:p1_neff_conditional"]}
```
