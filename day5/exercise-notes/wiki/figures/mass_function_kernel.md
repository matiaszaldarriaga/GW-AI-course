# Figure: Mass function and power kernel

**File:** `paper_v2/figures/mass_function_kernel.pdf`
**Ingested:** 2026-04-13

## What it shows

A two-panel figure. Left panel: the SMBH mass function $dn/d\log_{10}M$
for three values of the $M$--$\sigma$ scatter $\varepsilon$ (0.20, 0.38,
0.66). Higher scatter pushes the distribution toward more massive
binaries, populating the high-mass tail. Right panel: the normalized
power kernel $\mathcal{K}(\log_{10}M) = \bar{N}(M)\cdot h_s^2(M)/h_c^2$,
which integrates to 1 and shows which mass bin contributes most to the
total GW power. Each panel shows dotted vertical lines marking
$M_{\rm peak}$, the mass at which the kernel peaks. As $\varepsilon$
increases, $M_{\rm peak}$ shifts from $10^{9.2}\,M_\odot$ to
$10^{9.5}\,M_\odot$ to $10^{10.6}\,M_\odot$.

## Caption (from paper)

> Left: the SMBH mass function $dn/d\log_{10}M$ for three values
> of the $M$--$\sigma$ scatter $\varepsilon$. Higher scatter populates the
> high-mass tail. Right: the normalized power kernel
> $\mathcal{K}(\log_{10}M)$ whose integral is 1, showing which masses
> contribute most to the total GW power. The dotted lines mark $M_{\rm peak}$.

## Generator

**paper_v2 (2026-07-14):** `paper_v2/scripts/fig_mass_function_kernel.py`
(standalone, under `_paperstyle`; run
`conda run -n <env> python paper_v2/scripts/fig_mass_function_kernel.py`,
~1 min). Two changes relative to the legacy notebook export: (i) colors
now follow the canonical `EPS_COLORS` map ($\varepsilon = 0.66$ = green;
the old export used red), no in-plot titles, serif fonts; (ii) the left
panel now draws each model's mass function at its **calibrated**
$\phi_\sigma$ (the normalization matched to $h_c = 2.5\times10^{-15}$,
multipliers ~13/6/0.7), so the low-scatter curves sit above the
fiducial abundance; pass `--fiducial` to reproduce the legacy panel
where all three models share $\phi_\sigma = 2.611\times10^{-2}$.

**Legacy (`paper/`):** `notebooks/guide_interactive.py`, Section 3
(no savefig call; the old PDF was an unregenerable notebook export).

## Inputs

- `gwb_sources/` population model module (Sato-Polito & Zaldarriaga
  model): provides $\bar{N}(f,M)$ and $h_s^2(f,M)$.
- Velocity dispersion function and $M$--$\sigma$ relation with
  log-normal scatter $\varepsilon$; no external `.npz` results file
  identified for this figure.

## Concepts illustrated

- [[concepts/SMBH_population_model]] — the Sato-Polito & Zaldarriaga
  model, $M$--$\sigma$ relation, log-normal scatter $\varepsilon$, and
  the role of the high-mass tail.
- [[concepts/brightest_source_fraction]] — $M_{\rm peak}$ sets the
  typical mass of the loudest sources; higher $\varepsilon$ drives
  $p \equiv p_1$ upward by concentrating power in fewer, heavier
  binaries.
- [[concepts/N_eff]] — $N_{\rm eff}$ is suppressed when the power
  kernel is sharply peaked (fewer effective sources), as shown for
  large $\varepsilon$.

## Paper sections using this figure

- `paper_v2/sections/astrophysical_model.tex`, Section "The power kernel"
  (`\label{fig:mass_kernel}`).

## Related pages

- `wiki/figures/strain_spectrum_models.md` — next figure in the same
  section, showing $h_c^2(f)$ for the same three $\varepsilon$ values.
- `wiki/figures/c1c0_neff_vs_freq.md` — shows $C_1/C_0$ and $N_{\rm eff}$
  vs frequency, the downstream consequence of the mass-function shape.

---

```json
{"slug": "mass_function_kernel", "concepts": ["SMBH_population_model", "brightest_source_fraction", "N_eff"], "generator": "paper_v2/scripts/fig_mass_function_kernel.py", "inputs": ["gwb_sources population model (Sato-Polito & Zaldarriaga)"], "paper_uses": ["paper_v2/sections/astrophysical_model.tex, fig:mass_kernel"]}
```
