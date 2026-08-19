# `gwb_sources.sources`

**Source:** `gwb_sources/sources.py`
**Type:** Python module
**Ingested:** 2026-04-13

## Purpose

Generates Monte Carlo realizations of the SMBHB source population. Given a
luminosity function (binned over frequency and mass), it Poisson-samples source
counts per bin, assigns isotropic sky positions and Gaussian polarization
amplitudes, accumulates HEALPix power maps, and builds a per-realization ledger
of the brightest sources. The ledger enables post-hoc exclusion of loud sources
without re-running the realization. Outputs feed directly into
[[concepts/brightest_source_fraction]] and [[concepts/shot_noise]] estimates.

## Public API

| Function | Signature | Returns |
|---|---|---|
| `sample_sources` | `(lum_fct, rng=None)` | `N_bin_real` shape `(n_freq, n_mass)` — Poisson draw of counts |
| `expand_sources` | `(N_bin_real, h2s, rng=None)` | dict keyed by freq index; each entry has `theta_s, phi_s, hp_real, hp_imag, hc_real, hc_imag, h2s` |
| `gen_random_sources` | `(Nsources, rng=None)` | list `[hp_real, hp_imag, hc_real, hc_imag, theta_s, phi_s]` — unit-variance, isotropic |
| `compute_total_strain` | `(N_bin_real, strain_bins)` | `(n_freq,)` — sum over mass bins |
| `find_brightest_source_strain` | `(N_bin_real, strain_bins)` | `(n_freq,)` — strain of highest-strain occupied bin |
| `count_sources_brighter_than_strain` | `(N_bin_real, strain_bins, threshold_strains)` | `(n_freq,)` — count above per-freq threshold |
| `brightest_n_sources` | `(N_bin_real, strain_bins, N)` | `(brightest_strains, total_lower_strain)` — top-N strains plus residual |
| `run_realizations` | `(lum_fct, Nrel, count_threshold_ratio=10, N=5, seed=None)` | dict of arrays shape `(Nrel, Nfreq[, N])` — strain statistics only, no sky maps |
| `generate_realizations` | `(lum_fct, Nrel, nside, N_brightest=100, individual_threshold=1000, seed=None)` | list of dicts with `N_bin_real`, `power_maps`, `brightest` — full HEALPix output |

`run_realizations` is a lightweight loop (no sky maps) used for strain statistics.
`generate_realizations` is the primary realization engine used by notebooks and
scripts that need `C_ell^(P)`.

Sky positions are drawn isotropically: `theta = arccos(2*U - 1)`,
`phi = 2*pi*U`. Polarization amplitudes are i.i.d. N(0, 1/2) for each of
`hp_real, hp_imag, hc_real, hc_imag`.

## Known gotchas

### Single-RNG-per-realization fix (critical)

`generate_realizations` creates one `rng` per realization from a
`SeedSequence`-spawned child seed:

```python
ss = np.random.SeedSequence(seed)
real_seeds = ss.spawn(Nrel)
for i in range(Nrel):
    rng = np.random.default_rng(real_seeds[i])
    ...
```

All draws for that realization — Poisson counts, pixel assignments for
individual bins, and multinomial draws for bulk bins — use this single `rng` in
a fixed order. Consequently the pixel recorded in the ledger is *the same draw*
that was added to `power_maps`, not an independent sample. Without this fix the
map and ledger could be inconsistent, invalidating any exclusion study that
removes the `N_brightest` sources from the map using ledger pixels.

### Individual vs. bulk bin split

Bins are sorted by expected count ascending (rarest = highest h2s first).
Bins whose cumulative expected count is <= `individual_threshold` (default 1000)
are "individual": every sampled source gets its own `rng.integers` pixel draw
tracked in the ledger. The remaining high-count bins are "bulk": distributed via
`rng.multinomial` for efficiency. The split is pre-computed once before the
realization loop. Only individual-bin sources appear in the `brightest` ledger;
bulk bins contribute to `power_maps` but not to the ledger.

### `find_brightest_source_strain` corner case

Uses `argmax` on a reversed mask to find the *rightmost* occupied bin (assumed
to be the highest-strain bin because `strain_bins` is ordered ascending in the
mass axis). This is correct only if mass bins are sorted by strain. Verify that
`lum_fct['h2s']` is monotone in the mass axis before using this function.

### `run_realizations` uses a flat `np.random.default_rng(seed)` loop

Unlike `generate_realizations`, `run_realizations` advances a single shared
`rng` across all realizations sequentially. Reproducibility is exact for fixed
`Nrel`, but adding a new realization changes all subsequent ones. For production
MC use `generate_realizations` with `SeedSequence.spawn`.

## Consumers

- `scripts/` batch scripts that call `generate_realizations` and save `.npz`
  results for C_ell analysis.
- Marimo notebooks (`guide_*.py`) that plot [[concepts/brightest_source_fraction]]
  distributions and [[concepts/shot_noise]] scaling.
- Any exclusion study that removes bright sources from the map and re-computes
  `C_ell^(P)` relies on the ledger–map consistency guarantee described above.

## Related pages

- [[code/gwb_sources_init]] — package exports
- [[concepts/brightest_source_fraction]] — p = q_max / sum q_a
- [[concepts/shot_noise]] — variance from Poisson sampling
- [[concepts/SMBH_population_model]] — luminosity function input
- [[concepts/coherent_vs_incoherent]] — why p matters for detection scaling
