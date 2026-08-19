# Notebook: Population and Spectra

**Source:** `notebooks/guide_population_and_spectra.py`
**Rendered:** `results/guide_population_and_spectra.html`
**Type:** Marimo notebook
**Ingested:** 2026-04-13

## Purpose

Pedagogical walkthrough of the SMBHB population pipeline, from the galaxy
velocity dispersion function through to Monte Carlo realizations of the GW
strain spectrum. Establishes that the low-frequency GWB is dominated by a
handful of loud sources (the Poisson regime), motivating the paper's central
claim that $C_\ell$-based searches are suboptimal.

## Sections / outline

1. **Introduction** — PTA basics; pipeline overview (population model → strain PDF → Monte Carlo realizations).
2. **Parameters** — Grid dimensions and model parameters read from the results file (redshift 19 bins, mass 399 bins, 44 frequency bins, 19 mass-ratio bins; $\epsilon=0.66$, $\phi_\sigma=0.02611$, $\alpha_\sigma=0.41$, $\beta_\sigma=2.59$, $\alpha_{M\sigma}=8.32$, $\beta_{M\sigma}=5.64$, $B=0.5$, $Z_s=0.33$, $C=-1$).
3. **Velocity Dispersion Function and Mass Function** — Equations for $dn/d\sigma$ (modified Schechter form) and the convolved SMBH mass function; interactive sliders for $\alpha_\sigma$, $\beta_\sigma$, $\epsilon$.
4. **Luminosity Function** — $N(f,M)$ and $h^2_s(f,M)$ heatmaps; mean strain spectrum $h_c^2(f)$ vs $f^{-4/3}$ reference.
5. **Strain PDF** — Characteristic-function / FFT method for the compound-Poisson flux PDF $P(S)$; resolved / faint / bright source decomposition controlled by $N_c$; interactive frequency-bin slider.
6. **Source Realizations** — 10 000 Monte Carlo draws; total strain, brightest-source strain, total-without-brightest, total-without-brightest-20; interactive overlay slider; 95% percentile error-bar summary plot.
7. **Summary** — Key takeaways; pointer to `power_anisotropy.py` for sky structure.

## Key findings / figures

- The mean spectrum follows $h_c^2 \propto f^{-4/3}$ (shown by log-log overlay).
- $N_c$ drops from ~7 at the lowest frequency bin to $\ll 1$ by the third bin, confirming the Poisson regime sets in immediately above $f_{\min} \approx 0.085\,\text{yr}^{-1}$.
- Removing the single brightest source substantially reduces total strain at low frequencies; the brightest-to-rest ratio $h^2_{\rm brightest}/h^2_{\rm rest}$ is $>1$ there (shown in log-scale histogram).
- The 95% percentile summary (final figure) shows that the median total spectrum is dominated by a small number of sources whose contribution is highly variable across realizations — quantitative motivation for $p$ as the key parameter.

**Figures produced (inline, not saved to disk):**
- Log-log VDF and SMBH mass function (static + interactive).
- $N(f,M)$ and $h^2_s(f,M)$ heatmaps + $h_c^2(f)$ vs $f^{-4/3}$.
- Source distribution $dN/d\ln x$, strain PDF $P(S)$, per frequency bin (interactive).
- Strain spectrum realizations overlay (interactive count).
- Single-realization decomposition: total, w/o brightest, w/o brightest-20, brightest scatter.
- Cumulative strain distributions and brightest-to-rest ratio histogram (interactive).
- 95% percentile error-bar summary over all 44 frequency bins.

## Inputs

- `results/population_analysis_eps066.npz` — all pre-computed population
  quantities (VDF, mass function, $N_\text{bin}$, $h^2_s$, PDF grids,
  Monte Carlo realizations; 10 000 draws, seed 42).
- `gwb_sources.population.vdisp_func` — VDF evaluator (used for interactive slider).
- `gwb_sources.population.MFSMBH_vdisp` — SMBH mass function evaluator (interactive slider).

## Outputs

No files written to disk; all figures are rendered inline in the Marimo UI.

## Concepts touched

- [[concepts/SMBH_population_model]] — VDF, M-$\sigma$ relation, merger rate parameterization.
- [[concepts/brightest_source_fraction]] — $p = h^2_{\rm brightest}/h^2_{\rm tot}$; Poisson vs Gaussian regime.
- [[concepts/N_eff]] — Effective source count $N_{\rm eff} = 1/\sum_a p_a^2$; implicit in the $N_c$ transition.
- [[concepts/shot_noise]] — Compound-Poisson FFT PDF is the formal underpinning of shot-noise statistics.
- [[concepts/coherent_vs_incoherent]] — Brightest-source decomposition motivates why individual source fitting outperforms covariance-based methods.

## Paper cross-references

No `\fromnotebook{notebooks/guide_population_and_spectra}` citations found in
`paper/` at time of ingestion. The notebook serves as background motivation;
the Poisson-regime result is cited conceptually in the introduction and
Section II.

## Related pages

- `wiki/notebooks/` — sibling notebook pages (none yet ingested).
- `wiki/concepts/SMBH_population_model.md` — canonical definition of the population model used here.
- `wiki/concepts/brightest_source_fraction.md` — definition of $p$; the $N_c$ plot here is a direct illustration.
- `wiki/results/population_analysis_eps066.md` — full array inventory for the input file (not yet written).
