# Notebook: Interactive GW Background Explorer

**Source:** `notebooks/guide_interactive.py`
**Rendered:** `results/guide_interactive.html`
**Type:** Marimo notebook
**Ingested:** 2026-04-13

## Purpose

Interactive walkthrough that generates Monte Carlo realizations of the SMBHB
GWB on-the-fly — directly in the browser — using sliders for all population
parameters. The notebook demonstrates how the mass-function scatter $\varepsilon$,
VDF slope $\alpha_\sigma$, VDF cutoff $\beta_\sigma$, and redshift-evolution
parameter $B$ jointly control $p_1$, $N_{\rm eff}$, and $C_1/C_0$. It also
benchmarks four semi-analytic approximations to the $C_1/C_0$ distribution.
The ~0.5 s wall time for 1 K realizations is achieved via the CDF-based
source-placement trick described below.

## Sections / outline

1. **Definitions** — Source weights $q_a = h^2_s$, normalized fractions
   $p_a = q_a / \sum_b q_b$, brightest fraction $p_1 = \max_a p_a$,
   $N_{\rm eff} = 1/\sum_a p_a^2$, dipole identity
   $C_1/C_0 = |\mathbf{S}|^2 = |\sum_a p_a \hat{n}_a|^2$.
2. **Parameters** — Sliders: $\varepsilon \in [0.15, 0.80]$ (default 0.66),
   $\alpha_\sigma \in [0.2, 0.8]$ (default 0.41), $\beta_\sigma \in [1.5, 4.0]$
   (default 2.59), $B \in [-1, 2]$ (default 0.5), $N_{\rm realizations}$
   (500–10 000, default 1 000).  Fixed: $\phi_\sigma = 2.611\times10^{-2}$,
   $\alpha_{M\sigma}=8.32$, $\beta_{M\sigma}=5.64$, $Z_s=0.33$, $C=-1$.
3. **Mass Function and Power Kernel** — SMBH mass function $dn/d\log_{10}M$;
   normalized power kernel $\mathcal{K}(\log_{10}M)$ (area = 1, frequency-independent
   after normalization); $M_{\rm peak}$ marked.
4. **Realizations** — Prose description of the CDF-based algorithm (see Method
   section below).
5. **Strain Spectrum** — $h_c^2(f)$: analytic mean, realization mean, median,
   and up to 50 individual overlays (slider). Brightest fraction $p_1$ vs
   frequency with 95% credible band.
6. **Dipole Anisotropy and $N_{\rm eff}$** — $C_1/C_0$ and $N_{\rm eff}$ vs
   frequency with mean, median, and 95% credible bands.
7. **Distribution of $C_1/C_0$ at selected frequency** — Histogram plus four
   semi-analytic approximations: (1) $\delta(u - p_1^2)$; (2) uniform on
   $[(p_1-p_2)^2, (p_1+p_2)^2]$ (2-source, random angle); (3) 1-source +
   Gaussian (noncentral Maxwell, variance $\eta = \sum_{a \geq 2} p_a^2$);
   (4) 2-source + Gaussian ($p_1,p_2$ explicit, variance
   $\eta_2 = \sum_{a \geq 3} p_a^2$). Linear and log-$y$ panels side by side.
8. **Summary Statistics** — Markdown table: mean $C_1/C_0$, median, 95th
   percentile, $\langle N_{\rm eff}\rangle$, $\langle p_1\rangle$ at five
   representative frequency bins.

## Method: CDF-based source-placement trick

This is the core performance innovation enabling ~0.5 s for 1 K realizations.

Per frequency bin $j$, sources are divided into **rare** (top $N_{\rm rare} \approx 100$
brightest by $h^2_s$) and **bulk** (all remaining).

**Pre-computation (once per parameter set):**
- Sort mass bins by $h^2_s$ descending.
- Build a cumulative-$N$ axis $c_k = \sum_{i=1}^k \bar{N}_{(i)}$ over the
  sorted rare bins.
- Store the sorted $h^2_s$ values $\{h^2_{s,(i)}\}$ for interpolation.
- Record $\bar{N}_{\rm rare} = c_{N_{\rm rare}}$, bulk mean
  $\mu_{\rm bulk} = \sum_{i>N_{\rm rare}} \bar{N}_i h^2_{s,i}$, and bulk
  variance proxy $\sigma^2_{\rm bulk} = \sum_{i>N_{\rm rare}} \bar{N}_i (h^2_{s,i})^2$.

**Per realization:**
1. Draw total rare count: $N_d \sim {\rm Poisson}(\bar{N}_{\rm rare})$, capped
   at $N_{\rm max}=200$.
2. Draw $N_{\rm max}$ uniform variates $u \sim U[0, \bar{N}_{\rm rare}]$ per
   frequency; look up $h^2_s(u)$ by linear interpolation on the pre-computed
   $(c_k, h^2_{s,(k)})$ table.  Entries beyond index $N_d$ are zeroed.
3. Bulk rare sources add a deterministic contribution $\mu_{\rm bulk}$ to
   $h^2_{\rm tot}$ and a Gaussian contribution (variance $\sigma^2_{\rm bulk}/3$
   per component) to each Cartesian component of $\mathbf{S}$.
4. Compute $p_a$, $p_1$, $p_2$, $\sum p_a^2$, $\eta$, $\eta_2$ from the
   rare sources; add bulk correction to $\sum p_a^2$.
5. Draw isotropic unit vectors for each rare source; sum $\mathbf{S}$; add
   bulk Gaussian noise; compute $C_1/C_0 = |\mathbf{S}|^2$.

The vectorized NumPy implementation processes all realizations and all
frequency bins simultaneously with a single `np.interp` call per frequency,
making the entire loop $O(N_{\rm rel} \cdot N_{\rm freq} \cdot N_{\rm max})$
with very small constant.

## Key findings / figures

- The power kernel $\mathcal{K}(\log_{10}M)$ is frequency-independent after
  normalization, confirming that $\bar{N} \propto f^{-8/3}$ and
  $h^2_s \propto f^{-4/3}$ cancel in the ratio.
- At the lowest frequency bin ($f \approx 0.062\,{\rm yr}^{-1}$), the summary
  table (Sec. 8) provides the paper's quoted values: median
  $p_1 \approx 0.15$, mean $p_1 \approx 0.22$, $\langle N_{\rm eff}\rangle \approx 25$,
  $\langle C_1/C_0\rangle \approx 0.04$.
- The 2-source + Gaussian approximation (Approx 4) most closely tracks the
  full 3D walk histogram at low frequencies where $p_1$ and $p_2$ are
  individually resolvable.

**Figures produced (inline, not saved to disk):**
- SMBH mass function + normalized power kernel (Sec. 3).
- Strain spectrum overlay + $p_1$ vs frequency (Sec. 5).
- $C_1/C_0$ and $N_{\rm eff}$ vs frequency with credible bands (Sec. 6).
- $C_1/C_0$ histogram with four approximations, linear and log scale (Sec. 7).

## Inputs

- `gwb_sources.population.luminosity_function` — returns `N_bin[Nfreq, Nmass]`
  and `h2s[Nfreq, Nmass]`; called once per slider change.
- `gwb_sources.population.MFSMBH_vdisp` — SMBH mass function (mass-function panel).
- `gwb_sources.population.vdisp_func`, `gaussian`, `M_sigma` — imported but
  used internally by `luminosity_function`.

## Outputs

No files written to disk; all figures and the summary table are rendered inline
in the Marimo UI.

## Concepts touched

- [[concepts/SMBH_population_model]] — VDF, M-$\sigma$ relation, merger-rate parameterization controlled by sliders.
- [[concepts/brightest_source_fraction]] — $p_1$ computed and plotted vs frequency; central observable.
- [[concepts/N_eff]] — $N_{\rm eff} = 1/\sum p_a^2$ computed per realization and plotted.
- [[concepts/dipole_distribution]] — Full $C_1/C_0$ distribution and four analytic approximations benchmarked.
- [[concepts/Cl_over_C0]] — $C_1/C_0 = |\mathbf{S}|^2$ computed from the 3D walk.
- [[concepts/shot_noise]] — CDF interpolation method handles the Poisson (shot-noise) regime explicitly.
- [[concepts/coherent_vs_incoherent]] — $p_1$ and $N_{\rm eff}$ trends motivate the paper's hierarchy of strategies.

## Paper cross-references

- `paper/sections/astrophysical_model.tex:50` — `\fromnotebook{notebooks/guide_interactive.py, Sec. 3}` (mass function and power kernel figure).
- `paper/sections/astrophysical_model.tex:65` — `\fromnotebook{notebooks/guide_interactive.py, Sec. 4}` (realizations and CDF method).
- `paper/sections/numerical_estimates.tex:34` — `\fromnotebook{notebooks/guide_interactive.py, Sec. 8}` (summary statistics table; $p_1$, $N_{\rm eff}$, $\langle C_1/C_0\rangle$ at lowest frequency).

## Related pages

- `wiki/notebooks/guide_population_and_spectra.md` — companion notebook; loads pre-computed `.npz` instead of recomputing; provides the FFT-based strain PDF.
- `wiki/concepts/brightest_source_fraction.md` — definition of $p$.
- `wiki/concepts/N_eff.md` — definition of $N_{\rm eff}$.
- `wiki/concepts/dipole_distribution.md` — analytic approximations benchmarked here.

---

## JSON report

```json
{
  "slug": "guide_interactive",
  "concepts": [
    "SMBH_population_model",
    "brightest_source_fraction",
    "N_eff",
    "dipole_distribution",
    "Cl_over_C0",
    "shot_noise",
    "coherent_vs_incoherent"
  ],
  "inputs": [
    "gwb_sources.population.luminosity_function",
    "gwb_sources.population.MFSMBH_vdisp",
    "gwb_sources.population.vdisp_func"
  ],
  "outputs": [],
  "paper_refs": [
    "astrophysical_model.tex:50",
    "astrophysical_model.tex:65",
    "numerical_estimates.tex:34"
  ],
  "method_notes": "CDF-based source placement: pre-compute sorted cumulative-N vs h2s curve per frequency bin; Poisson-draw total rare count; uniform variates mapped to h2s via linear interpolation; bulk contributes deterministic mean plus Gaussian noise to S vector. Enables ~0.5s for 1K realizations."
}
```
