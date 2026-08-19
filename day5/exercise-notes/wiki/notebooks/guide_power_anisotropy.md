# Notebook: `guide_power_anisotropy`

## Purpose

Interactive walkthrough of $C_\ell/C_0$ (source-power sky convention) computed
from Monte Carlo realizations of the SMBHB GWB. Covers HEALPix power-map
construction, monopole statistics, normalized angular power spectra, the effect
of excluding the top-$N$ brightest sources, $N_{\rm eff}$ scaling, scatter
plots, and frequency dependence of the dipole and quadrupole.

## Sections

| # | Title |
|---|-------|
| 1 | Introduction — SH decomposition, $C_\ell$, motivation for $C_\ell/C_0$ |
| 2 | Computation setup — parameter table loaded from results file |
| 3 | Power-map construction — Poisson sampling, multinomial sky placement, $h^2_s$ deposition, `healpy.anafast` |
| 4 | Power maps (Mollweide) — interactive realization slider, three frequency panels |
| 5 | Source strain distributions — survival functions, brightest-to-rest ratio |
| 6 | Pixel strain distributions — single-realization histogram, max/mean ratio across realizations |
| 7 | Monopole $C_0$ — PDF at selected frequency; $C_0$ vs frequency with 95% band, all vs excl. top 20 |
| 8 | Normalized $C_\ell/C_0$ — mean + overlay of individual realizations |
| 9 | Exclusion effect — mean spectrum before/after removing top-$N$ sources ($N \in \{1,5,10,20\}$) |
| 10 | $C_\ell/C_0$ error bars — median + 95% band at three frequencies |
| 10b | $C_\ell/C_0$ PDF — distribution across realizations at fixed $\ell$, all vs excluded |
| 10c | Scatter plots — $C_\ell/C_0$ vs $C_1/C_0$; $C_1/C_0$ vs $h^2_{\rm bright}/h^2_{\rm tot}$ |
| 10d | $N_{\rm eff}$ scaling — $N_{\rm eff}$ vs frequency; $C_\ell/C_0$ vs $1/N_{\rm eff}$ scatter |
| 10e | Joint $(p_1, C_1/C_0)$ density + conditional $P(p_1\mid C_1/C_0)$ — **own model dropdown** (ε=0.20/0.38/0.66) + frequency/slice-width sliders. E1 joint hexbin with the $C_1/C_0=p_1^2$ line; E2 conditional PDF+CDF at $C_1/C_0\in\{0.05,0.1,0.2,0.5\}$; E3 median $p_1$ vs $C_1/C_0$ at the three Table I frequencies vs the $\sqrt{C_1/C_0}$ envelope |
| 10f | **Analytic $P(p_1\mid C_1/C_0)$ and $P(N_{\rm eff}\mid C_1/C_0)$** — **own** model dropdown + frequency/slice-width sliders (light prep: $Q$ from the monopole, no power-maps read). F1: Bayesian inverse of the paper's forward laws, $\eta=\sum_{a\ge2}p_a^2$ marginalized by **importance sampling** (red, matches MC ~1–2%), vs mean-$\eta$ plug-in (orange, ≈red) vs flat-prior closed form (blue) vs $\sqrt{x}$ anchor. F2: $N_{\rm eff}=1/(p_1^2+\eta)$ conditional, peaking at $1/(C_1/C_0)$ — a handful of sources |
| 11 | $C_\ell/C_0$ vs frequency — dipole and quadrupole mean/median bands, all vs excl. top 20 |
| Summary | Eight key findings listed |

## Key findings

1. Power maps are dominated by individual bright sources at all frequencies.
   At the lowest frequency the brightest source carries $\sim$15% of total power;
   at higher frequencies a single source can carry 40–50%.
2. $C_0$ fluctuates significantly across realizations (Poisson variance in total
   source count). Excluding the top sources reduces both amplitude and variance.
3. $C_\ell/C_0$ is approximately flat in $\ell$, with a level set by $1/N_{\rm eff}$
   rather than the raw source count.
4. Removing brightest sources reduces $C_\ell/C_0$; the effect is strongest at
   high frequencies where fewer sources contribute — confirming the anisotropy
   is driven by the loudest individual binaries.
5. $C_\ell/C_0$ increases with frequency, tracking the decrease in $N_{\rm eff}$.
6. **A large $C_1/C_0$ requires a single dominant source** (§10e). Conditioning on
   the realized dipole, $p_1$ concentrates just below $\sqrt{C_1/C_0}$ (the
   single-source envelope, since realized $C_1/C_0 \gtrsim p_1^2$). At the
   NANOGrav "limit" $C_1/C_0=0.2$ the brightest source carries a median
   $\sim$40% of the power; at $C_1/C_0=0.5$ it dominates ($p_1>0.5$) in
   $\sim$90% of realizations. corr$(\log p_1,\log C_1/C_0)\approx0.85$. High
   dipole is never produced by many comparable sources adding up — this is the
   conditional evidence Fig. 5 (marginal CDF + mean-fraction) does not show.
7. **The conditional is reproduced analytically** (§10f, F1). $P(p_1\mid C_1/C_0)$
   is the Bayesian inverse of the paper's one-source+Gaussian forward law
   (noncentral Maxwell, `distribution_c1c0.tex` Eq. 1src_gauss): $P(p_1\mid x)
   \propto \pi(p_1)\,p_1^{-1}e^{-3p_1^2/2\eta}\sinh(3p_1\sqrt{x}/\eta)$. The
   background $\eta=\sum_{a\ge2}p_a^2$ is marginalized **properly** over
   $P(\eta\mid p_1)$ by importance-sampling the realizations with weights
   $f(x\mid p_{1,j},\eta_j)$ (this also folds in the prior $\pi(p_1)$). It
   matches the MC median to $\sim$1–2% at all four reference $C_1/C_0$ and both
   extreme frequencies; the $\eta$-spread barely shifts the centre (mean-$\eta$
   plug-in ≈ marginalized), and the flat-prior mode is $\sqrt{x}-\eta/(3\sqrt{x})$.
8. **A high dipole means a handful of sources** (§10f, F2). With $N_{\rm eff}=
   1/\sum_a p_a^2=1/(p_1^2+\eta)$ and $\langle C_1/C_0\rangle=1/N_{\rm eff}$,
   conditioning gives $N_{\rm eff}\approx 1/(C_1/C_0)$: median $\sim$2 at
   $C_1/C_0=0.5$, $\sim$5 at the NANOGrav "limit" 0.2, $\sim$10 at 0.1 (capped
   at high frequency where few sources exist). The analytic ($\eta$-marginalized)
   $P(N_{\rm eff}\mid C_1/C_0)$ tracks the MC. §10f reads only `cls_all` +
   `brightest_h2s` (total power $Q=\sqrt{C_0}\,N_{\rm pix}/\sqrt{4\pi}$,
   verified to ~0.04% vs the pixel sum), so model switching is fast. As of
   2026-06-19 §10e uses this **same** monopole-based $Q$ (it no longer reads
   `power_maps`), so $p_1$ is defined identically in §10e and §10f.

## Inputs

| File | Description |
|------|-------------|
| `results/power_anisotropy_eps066.npz` | Default: pre-computed power maps and $C_\ell$ (10 000 realizations, nside=8, $\ell_{\rm max}=23$, 44 frequency bins, excl. levels 1/5/10/20, top-100 brightest ledger) |
| `results/power_anisotropy_eps{020,038,066}.npz` | §10e only: the model dropdown loads whichever of the three is selected |

The `.npz` arrays consumed directly:

- `power_maps` — shape (10000, 44, 768), linear $h^2_s$ per pixel (summed over the sources that landed there); §10e uses its pixel sum as the total power $\sum_a h^2_{s,a}$
- `cls_all` — shape (10000, 44, 24), $C_\ell$ for $\ell=0\ldots23$
- `cls_excl_{1,5,10,20}` — same shape, after source removal
- `brightest_h2s` — shape (10000, 44, 100), top-100 source powers; §10e uses `[:,:,0]` (the brightest) for $p_1 = h^2_{\rm brightest}/\sum_{\rm pix}P_i$; §10f also uses `[:,:,1:]` for $\eta=\sum_{a\ge2}p_a^2$ (the inversion's background variance)
- `fmean_per_year` — shape (44,), frequency axis (~0.085–2.8/yr)

## Outputs

No files written; all figures are inline interactive plots. The whole notebook
is exported to `results/guide_power_anisotropy.html` via
`marimo export html` (untracked; see [[reproducibility]]).

## Concepts touched

- [[concepts/Cl_over_C0]] — central ratio computed throughout
- [[concepts/N_eff]] — $N_{\rm eff} \equiv (\sum h^2)^2/\sum h^4$; scatter plot tests $C_\ell/C_0 \approx 1/N_{\rm eff}$
- [[concepts/brightest_source_fraction]] — $p = h^2_{\rm bright}/h^2_{\rm tot}$ plotted vs $C_1/C_0$
- [[concepts/dipole_distribution]] — PDF and scatter of $C_1/C_0$ across realizations
- [[concepts/coherent_vs_incoherent]] — context for why $C_\ell/C_0$ scales as $p^2$
- [[concepts/SMBH_population_model]] — Poisson + multinomial sampling procedure (Sec. 3)
- [[concepts/shot_noise]] — $C_\ell/C_0 \approx 1/N_{\rm eff}$ is the shot-noise floor

## Paper cross-references

- Angular power spectrum definition and $C_\ell/C_0$ exact formula:
  `angular_power_spectrum.tex` (`eq:cl_exact`, `eq:cl_c0_exact`, `eq:mean_cl`)
- Dominance of brightest sources and $p^2$ scaling: `three_strategies.tex`
- $N_{\rm eff}$ definition: `angular_power_spectrum.tex`

## Related pages

- [[../concepts/Cl_over_C0]]
- [[../concepts/N_eff]]
- [[../concepts/brightest_source_fraction]]
- [[../results/power_anisotropy_eps066]] (ingest pending)

---

```json
{"slug": "guide_power_anisotropy", "concepts": ["Cl_over_C0", "N_eff", "brightest_source_fraction", "dipole_distribution", "coherent_vs_incoherent", "SMBH_population_model", "shot_noise"], "inputs": ["results/power_anisotropy_eps020.npz", "results/power_anisotropy_eps038.npz", "results/power_anisotropy_eps066.npz"], "outputs": ["results/guide_power_anisotropy.html"], "paper_refs": ["angular_power_spectrum.tex", "distribution_c1c0.tex", "three_strategies.tex"]}
```
