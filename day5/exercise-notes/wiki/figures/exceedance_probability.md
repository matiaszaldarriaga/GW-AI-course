# Figure: Exceedance probability of C_1/C_0

**File:** `paper_v2/figures/exceedance_probability.pdf`
**Ingested:** 2026-04-13

> **Full-moment update (2026-08-11).** Every exceedance curve is recomputed
> from schema-v2 direct $C_1/C_0=|\mathbf D|^2/Q^2$ at all 10,000
> realizations. The unresolved population contributes its full random-walk
> covariance; the curves do not use a mean-filled HEALPix dipole.

## What it shows

A three-panel figure (one panel per astrophysical model: $\varepsilon = 0.20$,
$0.38$, $0.66$). Each panel plots $P(C_1/C_0 > \text{threshold})$ on a log
scale versus GW frequency $f$ [1/yr] for four thresholds: 0.01 (dotted),
0.10 (solid), 0.20 (dashed, red — the NANOGrav 95% "upper limit"), and 0.50
(dash-dot). The key message is that even for the most anisotropic model
($\varepsilon = 0.66$) the probability of exceeding the NANOGrav threshold is
only $17.96\%$ at the lowest frequency; for $\varepsilon = 0.20$ it is
$0.11\%$ there. The probability rises toward high frequency as the number of
sources falls. The NANOGrav "constraint" is therefore uninformative
for the astrophysically expected signal.

## Caption (from paper)

> Probability that $C_1/C_0$ exceeds a given threshold as a function of GW
> frequency, for three astrophysical models. The $C_1/C_0 > 0.2$ line (red
> dashed) corresponds to the NANOGrav 95\% ``upper limit,'' which is simply the
> prior (see text). Even for the most anisotropic model ($\varepsilon = 0.66$),
> this threshold is exceeded in only $\sim 18\%$ of realizations at the lowest
> frequency. The probability rises at high frequency (where fewer sources
> contribute), but this is also where PTA sensitivity is weakest.

## Generator

`paper_v2/scripts/fig_exceedance_probability.py`

The script loads three results files, computes the empirical exceedance
fraction $P(C_1/C_0 > \text{thresh}) = \langle \mathbf{1}[C_1/C_0 >
\text{thresh}] \rangle_{\rm realizations}$ at each frequency bin, and saves
the figure to `paper_v2/figures/exceedance_probability.pdf`.

## Inputs

- `new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps020.npz`
  — `fmean_per_year` and direct `c1c0_direct` for
  $\varepsilon = 0.20$.
- The matching `eps038` product — same structure for
  $\varepsilon = 0.38$.
- The matching `eps066` product — same structure for
  $\varepsilon = 0.66$.

## Concepts illustrated

- [[concepts/Cl_over_C0]] — the ratio $C_1/C_0$ is the primary statistic;
  the figure shows its full exceedance distribution rather than a point
  estimate.
- [[concepts/SMBH_population_model]] — the three $\varepsilon$ panels span
  the plausible range of $M$--$\sigma$ scatter, which controls how
  concentrated GW power is in the brightest sources.
- [[concepts/brightest_source_fraction]] — larger $\varepsilon$ means higher
  $p$, driving $C_1/C_0 \sim p^2$ upward and shifting the exceedance curves.
- [[concepts/prior_sensitivity]] — the NANOGrav 0.2 threshold is the 95th
  percentile of the $b_{LM}$ prior with $\ell_{\rm max}^b = 3$; the figure
  makes visible that the posterior never pushes above this threshold in a
  meaningful fraction of realizations.
- [[concepts/sqrt_SH_basis]] — the truncation at $\ell_{\rm max}^b = 3$ sets
  the prior on $C_1/C_0$, directly determining how "easy" the NANOGrav limit
  is to satisfy (i.e., almost always).
- [[concepts/shot_noise]] — exceedance probability rises at high frequency
  because fewer sources contribute per bin, increasing sample variance.

## Paper sections using this figure

- `paper_v2/sections/nanograv_prior.tex`, Section "The prior determines the
  constraint" (`\label{fig:exceedance}`).

## Related pages

- `wiki/figures/mass_function_kernel.md` — shows the $\varepsilon$-dependent
  mass functions whose power-concentration drives the $C_1/C_0$ distributions
  plotted here.

---

```json
{"slug": "exceedance_probability", "concepts": ["Cl_over_C0", "SMBH_population_model", "brightest_source_fraction", "prior_sensitivity", "sqrt_SH_basis", "shot_noise"], "generator": "paper_v2/scripts/fig_exceedance_probability.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps*.npz"], "paper_uses": ["paper_v2/sections/nanograv_prior.tex, fig:exceedance"]}
```
