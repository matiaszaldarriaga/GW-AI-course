# `scripts/run_population_analysis.py`

**Source:** `scripts/run_population_analysis.py`
**Type:** batch script
**Ingested:** 2026-04-13

## Purpose

Runs all heavy computation for the SMBHB population and GW-strain-spectra
analysis. For a given M-sigma scatter parameter ε, the script:

1. Builds the redshift, mass, frequency, and mass-ratio grids.
2. Evaluates intermediate population quantities: velocity-dispersion
   function and SMBHB mass function on those grids.
3. Calls `luminosity_function` to get per-bin source counts and strain
   squared (background + brightest source).
4. Calls `pdf_all_frequencies` to compute strain PDFs at all 44 frequency
   bins and at 6 representative frequencies in full resolution.
5. Runs 10 000 Monte Carlo realizations via `run_realizations` (seed = 42),
   tracking the total strain, the brightest source, and the top-20
   brightest sources per realization per frequency.

All results are saved to a single `.npz` file tagged by the ε value
(e.g. `population_analysis_eps066.npz`).

The script is the source of truth for [[concepts/SMBH_population_model]]
and feeds the [[concepts/brightest_source_fraction]] statistics used
throughout the paper.

## CLI

```
python scripts/run_population_analysis.py [--eps FLOAT]
```

| flag | default | description |
|---|---|---|
| `--eps` | `0.66` | M-sigma scatter parameter ε (dimensionless). Controls the width of the SMBHB mass function. |

Canonical values used in the paper: `0.20`, `0.38`, `0.66`.

## Dependencies

`gwb_sources` modules imported:

- `gwb_sources.population`: `luminosity_function`, `vdisp_func`,
  `MFSMBH_vdisp`, `M_sigma`
- `gwb_sources.strain_stats`: `pdf_all_frequencies`
- `gwb_sources.sources`: `run_realizations`

External: `numpy`, `astropy.units`.

Fixed population parameters (see `make_params`):

| symbol | value | meaning |
|---|---|---|
| σ | 160 km/s | fiducial velocity dispersion |
| φ_σ | 2.611e-2 | velocity-dispersion function normalization |
| a_σ, b_σ | 0.41, 2.59 | velocity-dispersion function power-law indices |
| a_ms, b_ms | 8.32, 5.64 | M-sigma relation coefficients |
| B | 0.5 | merger-rate bias |
| Z_s | 0.33 | merger redshift scale |
| C | −1 | merger-rate redshift power |

Grids: 19 redshift bins (z ∈ [0.01, 20]), 399 mass bins (log M/M☉ ∈ [6, 14]),
44 frequency bins (f_min = 1/(16.03 yr)), 19 mass-ratio bins.

## Outputs

- [[results/population_analysis_eps020]] — ε = 0.20
- [[results/population_analysis_eps038]] — ε = 0.38
- [[results/population_analysis_eps066]] — ε = 0.66

Each file is ~2.3 GB on disk, dominated by the 6 × 4 per-frequency strain
PDF arrays of shape (16 777 216,).

## Consumers

- `notebooks/guide_population_and_spectra.py` — primary interactive
  visualization of all outputs.
- `notebooks/guide_model_comparison.py` — cross-ε comparison of population
  statistics and brightest-source fractions.

## Reproduce

**Environment:** `gw_pta` conda env (see [[../environment]]).

**Canonical invocations** (produces all three eps files for this project):

```bash
conda run -n gw_pta python scripts/run_population_analysis.py --eps 0.20
conda run -n gw_pta python scripts/run_population_analysis.py --eps 0.38
conda run -n gw_pta python scripts/run_population_analysis.py --eps 0.66
```

**CLI arguments:**

| Arg | Default | Type | Meaning |
|---|---|---|---|
| `--eps` | `0.66` | float | M-sigma intrinsic scatter ε (dex); controls width of SMBHB mass function |

**Outputs:**

| File | Size | Description |
|---|---|---|
| `results/population_analysis_eps020.npz` | 2.3 GB | Full population analysis for ε=0.20 |
| `results/population_analysis_eps038.npz` | 2.3 GB | Full population analysis for ε=0.38 |
| `results/population_analysis_eps066.npz` | 2.3 GB | Full population analysis for ε=0.66 |

**Wall time:** ~2 minutes per run on a typical workstation (dominated by `pdf_all_frequencies` at ~45 s and 10 000 realizations at ~48 s; `luminosity_function` takes ~6 s).

**Consumer notebooks:** [[../notebooks/guide_population_and_spectra]], [[../notebooks/guide_model_comparison]]

## Related pages

- [[concepts/SMBH_population_model]]
- [[concepts/brightest_source_fraction]]
- [[concepts/coherent_vs_incoherent]]
- [[code/gwb_sources_population]]
- [[code/gwb_sources_strain_stats]]
- [[code/gwb_sources_sources]]
