# `gwb_sources.strain_stats`

**Source:** `gwb_sources/strain_stats.py`
**Type:** Python module
**Ingested:** 2026-04-13

## Purpose

Computes the probability distribution function (PDF) of the total GW strain flux
$S \equiv h_c^2$ at a given frequency, summed over an entire Poisson-sampled
source population. This is the analytical/FFT-based counterpart to the Monte Carlo
realization approach in `gwb_sources.sources`. The central output is $P(S)$, from
which mean and median strain can be extracted and compared — the mean-vs-median
observable identified in `discussion.tex` as the most informative near-term
diagnostic. See [[concepts/SMBH_population_model]].

The implementation follows the characteristic-function method of SPZ 2025dist
(arxiv 2406.17010): the PDF is computed via inverse FFT of
$\exp\!\bigl[\int dh_s^2\,(dN/dh_s^2)(e^{i\omega h_s^2}-1)\bigr]$,
with bright and faint source contributions handled separately to maintain numerical
accuracy across the dynamic range of the luminosity function.

## Public API

| Function | Inputs | Returns |
|---|---|---|
| `create_S(dNdx_in, x, dx, ...)` | luminosity function arrays, grid size params | strain grid `S`, interpolated `dNdS`, step `dS`, mean source count `Nbar`, mean flux `Sbar` |
| `faint_contribution(x, dNdx_in, xmin, xmax, ...)` | luminosity function, grid bounds | `mean_faint`, `sigma2_faint`, `sigma_faint` |
| `bright_contribution(x, dNdx_in, xmax, ...)` | luminosity function, upper grid bound | `Nbar_bright`, `xbar_bright` |
| `compute_p(dNdS, dS, mean_faint, sigma2_faint, Nbar_bright, ...)` | gridded `dNdS`, faint/bright stats | `p` — the PDF array $P(S)$ on the strain grid |
| `pdf_all_frequencies(lum_fct, fmean, ...)` | luminosity function dict, frequency array | dict of all intermediate and final arrays for every frequency bin |

All functions accept an optional `Nc_scale` multiplier (scales $dN/dx$ globally, e.g. to vary number density) and a `verb` flag for diagnostic printing.

## Key statistics

- **Mean flux** `xbar` = $\int (dN/dx)\,x\,dx$ — analytic mean of $h_c^2$.
- **PDF** `p` — full probability distribution $P(S)$ from which median, percentiles,
  and any moment can be extracted by the caller.
- **Faint-source Gaussian approximation** — sources below the FFT grid floor
  (`xmin = S[1]`) are replaced by a Gaussian with mean `mean_faint` and variance
  `sigma2_faint`; contributes a phase term $e^{-\sigma^2\omega^2/2 - i\mu\omega}$ to
  the characteristic function.
- **Bright-source correction** — sources above the grid ceiling (`xmax = S[-1]`) are
  rare enough that only their Poisson suppression factor $e^{-N_{\rm bright}}$ is
  applied; their flux is tracked separately as `xbar_bright`.
- The interpolated log-spaced version `pinter` on 500 points is stored for plotting.

## Consumers

- `gwb_sources/__init__.py` re-exports `pdf_all_frequencies` as part of the public API.
- `notebooks/guide_model_comparison.py` uses the resulting PDF to compute and compare
  median vs mean $h_c^2$ across $\varepsilon$ scenarios (the 57% figure quoted in
  [[concepts/SMBH_population_model]]).
- Scripts in `scripts/` that produce `.npz` results for figure generation may call
  `pdf_all_frequencies` directly.

## Related pages

- [[concepts/SMBH_population_model]] — population scenarios and mean-vs-median interpretation
- [[concepts/brightest_source_fraction]] — $p_1$ and $N_{\rm eff}$ emerge from the same $dN/dx$
- [[concepts/shot_noise]] — the Gaussian-core + power-law-tail structure this PDF exhibits
- [[code/gwb_sources_init]] — package-level re-export
- [[code/gwb_sources_sources]] — Monte Carlo realization approach (complementary method)
