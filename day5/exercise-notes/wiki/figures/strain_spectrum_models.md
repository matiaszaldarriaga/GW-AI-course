# Figure: Strain spectrum for three epsilon models

**File:** `paper_v2/figures/strain_spectrum_models.pdf`
**Ingested:** 2026-04-13
**Updated:** 2026-08-11 (schema-v2 common-run totals)

## What it shows

**Revised 2026-06-22** to the **raw** spectrum $h_c^2(f)$ (no renormalization,
no frequency rescaling). This is possible now that all three models are
calibrated to the *same* mean amplitude $\sqrt{\langle h_c^2\rangle} =
2.5\times10^{-15}$ at $f = 1\,{\rm yr}^{-1}$ (per-model $\phi_\sigma$; see
[[concepts/SMBH_population_model]], [[reproducibility]]). Because the mean
spectrum is $\langle h_c^2\rangle\propto f^{-4/3}$ for every model, the three
**mean** curves (thin solid) coincide — their overlap is a direct visual
**check that the $\phi_\sigma$ calibration is consistent** (they pass through a
star at $(1\,{\rm yr}^{-1},(2.5\times10^{-15})^2)$). The **realization median**
(thick dashed) falls below by a model-dependent amount.

Median/mean ratios (matched normalization): $\varepsilon=0.20$:
$0.984\to0.664$; $\varepsilon=0.38$: $0.921\to0.412$; $\varepsilon=0.66$:
$0.458\to0.052$ (lowest frequency $\to f=1.03$/yr). A large mean--median split is the
signature of a heavy-tailed, rare-bright-source population; a measured spectrum
that tracks the mean across the band disfavors the high-$\varepsilon$ models.
(The earlier 2026-06-19 version divided each model by its own mean and
multiplied by $(f/f_*)^{4/3}$ to flatten the means; that step is unnecessary
now that the means are matched by construction.)

## Caption (from paper)

> Raw characteristic-strain spectrum $h_c^2(f)$ for three models, all normalized
> to the same mean amplitude $\sqrt{\langle h_c^2\rangle} = 2.5\times10^{-15}$
> at $f = 1\,{\rm yr}^{-1}$ (star). The three mean curves (thin solid) coincide;
> their overlap is a check that the per-model $\phi_\sigma$ calibration is
> consistent. The median (thick dashed) falls below by an amount growing with
> $\varepsilon$ and frequency [...] even at the lowest frequency the
> $\varepsilon = 0.66$ median is already only $0.46$ of the mean.

## Generator

`paper_v2/scripts/fig_strain_spectrum_models.py` (schema-v2 consumer).
Run: `conda run -n gw_pta python paper_v2/scripts/fig_strain_spectrum_models.py`.
(Originally drawn ad hoc from `notebooks/guide_model_comparison.py` Sec. 2,
which is still cited via `\fromnotebook` in `astrophysical_model.tex`.)

## Inputs

- `new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps020.npz`
  — `fmean_per_year`, `h2c_vs_f` (analytic mean), `total_power_Q` (10,000 x
  frequencies) for $\varepsilon = 0.20$.
- The matching schema-v2 `eps038` product for
  $\varepsilon = 0.38$.
- The matching schema-v2 `eps066` product for
  $\varepsilon = 0.66$.

These are bitwise compact derivatives of the common schema-v2 power runs.

## Concepts illustrated

- [[concepts/SMBH_population_model]] — the $\varepsilon$ scatter
  controls the high-mass tail; larger scatter produces louder and
  more variable backgrounds.
- [[concepts/brightest_source_fraction]] — the mean--median
  divergence is a direct proxy for the dominance of rare, bright
  sources and hence for the brightest-source fraction $p$.
- [[concepts/N_eff]] — when the median falls below the mean, a
  small effective number of sources dominates; $N_{\rm eff}$ is
  correspondingly low for large $\varepsilon$.
- [[concepts/shot_noise]] — the mean--median gap is a manifestation
  of shot noise from heavy-tailed Poisson sampling of the source
  population.

## Paper sections using this figure

- `paper_v2/sections/astrophysical_model.tex`, subsection "Mean versus
  median" (`\label{fig:strain_spectrum}`).

## Related pages

- `wiki/figures/mass_function_kernel.md` — preceding figure in the
  same section; shows the mass function and power kernel whose shape
  determines the strain spectrum.
- `wiki/figures/c1c0_neff_vs_freq.md` — following figure; shows
  $C_1/C_0$ and $N_{\rm eff}$ vs frequency, the anisotropy
  consequences of the same three models.

---

```json
{"slug": "strain_spectrum_models", "concepts": ["SMBH_population_model", "brightest_source_fraction", "N_eff", "shot_noise"], "generator": "paper_v2/scripts/fig_strain_spectrum_models.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps*.npz"], "paper_uses": ["paper_v2/sections/astrophysical_model.tex, fig:strain_spectrum"]}
```
