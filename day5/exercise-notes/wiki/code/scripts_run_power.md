# `scripts/run_power_anisotropy.py`

**Source:** `scripts/run_power_anisotropy.py`
**Type:** batch script (CLI, not importable)
**Ingested:** 2026-04-13

## Purpose

Generates the primary Monte Carlo dataset for the power-anisotropy analysis.
For a given M-sigma scatter parameter `--eps`, it draws 10 000 SMBHB
population realizations, pixelizes each into a HEALPix power map
(nside = 8), computes $C_\ell^{(P)}$ spectra at four source-exclusion
levels, and saves everything to `results/power_anisotropy_eps<NNN>.npz`.
The trio `eps020.npz`, `eps038.npz`, `eps066.npz` covers the low, mid,
and fiducial scatter cases compared side-by-side in
`notebooks/guide_model_comparison.py`.

## CLI

```
python scripts/run_power_anisotropy.py [--eps EPS]
```

| Argument | Default | Meaning |
|---|---|---|
| `--eps` | 0.66 | M-sigma intrinsic scatter $\varepsilon$ (dex) |

The output filename is constructed as `power_anisotropy_eps{int(eps*100):03d}.npz`
so `--eps 0.20` → `eps020`, `--eps 0.38` → `eps038`, `--eps 0.66` → `eps066`.

## Pipeline stages

1. **Population model** — calls `gwb_sources.population.luminosity_function`
   with `make_params(eps=eps)` to obtain the expected number of binaries
   per (z, M, q, f) cell and the per-cell $h_s^2$ (strain-squared) weight.
   Frequency grid spans $[1/16.03\text{ yr},\, 9\times10^{-8}\text{ Hz}]$
   with bins of width $1/T_{\rm obs}$; the mean frequency per bin is
   computed using a $f^{-7/3}$-weighted average (44 bins, Nfreq = 44).

2. **Realizations** — calls `gwb_sources.sources.generate_realizations`
   with `Nrel=10000`, `nside=8`, `N_brightest=100`, `seed=42`.
   Each realization returns a `(Nfreq, npix=768)` power map and a per-frequency
   ledger of the 100 brightest source $h_s^2$ values.

3. **Power maps** — stacks realization power maps into
   `power_maps (10000, 44, 768)` and the brightest ledger into
   `brightest_h2s (10000, 44, 100)`.

4. **Cls — no exclusion** — calls `compute_power_cls(realizations)` via
   `gwb_sources.power_anisotropy` to produce `cls_all (10000, 44, 24)`.
   `lmax = 3*nside - 1 = 23`, so index `[..., ell]` holds $C_\ell^{(P)}$.

5. **Cls — exclusion sweeps** — repeats for `exclude_top_n in [1, 5, 10, 20]`,
   saving `cls_excl_N (10000, 44, 24)` for each `N`.

6. **Statistics** — calls `compute_power_statistics` for each Cls array,
   saving `mean`, `median`, and `pct` (percentiles 2.5, 25, 50, 75, 97.5)
   at shapes `(44, 24)` and `(5, 44, 24)` respectively.

## Population parameters (fixed across eps runs)

| Parameter | Value | Meaning |
|---|---|---|
| `sigma` | 160 | velocity dispersion normalization |
| `phi_sigma` | 2.611e-2 | M-sigma amplitude |
| `a_sigma`, `b_sigma` | 0.41, 2.59 | M-sigma power-law exponents |
| `a_ms`, `b_ms` | 8.32, 5.64 | mass-scaling parameters |
| `B` | 0.5 | binary fraction |
| `Zs` | 0.33 | redshift scaling |
| `C` | -1 | spectral index |
| z grid | logspace(-2, log10(20), 20) | 19 redshift bins |
| M grid | linspace(6, 14, 400) log10(Msun) | 399 mass bins |
| q grid | logspace(-1, 0, 20) | 19 mass-ratio bins |

See `[[../concepts/SMBH_population_model]]` for the astrophysical context.

## Key algorithms / formulas

`make_params` computes the per-bin mean frequency via a $f^{-7/3}$-weighted
average:
$$\langle f \rangle_i = \frac{\int_{f_i}^{f_{i+1}} f \cdot f^{-7/3}\,df}
  {\int_{f_i}^{f_{i+1}} f^{-7/3}\,df}.$$

`healpy.anafast` is used internally by `compute_power_cls` to decompose
each power map into $C_\ell^{(P)}$ via
$$C_\ell = \frac{1}{2\ell+1}\sum_m |a_{\ell m}|^2.$$

Consumers divide `cls_all[:,:,ell]` by `cls_all[:,:,0]` to obtain
$C_\ell/C_0$; see `[[../concepts/Cl_over_C0]]`.

## Outputs

| File | Generating command |
|---|---|
| `results/power_anisotropy_eps020.npz` | `--eps 0.20` |
| `results/power_anisotropy_eps038.npz` | `--eps 0.38` |
| `results/power_anisotropy_eps066.npz` | `--eps 0.66` |

Pointer pages: `[[../results/power_anisotropy_eps020]]`,
`[[../results/power_anisotropy_eps038]]`,
`[[../results/power_anisotropy_eps066]]`.

## Reproduce

**Environment:** `gw_pta` conda env (see [[../environment]]).

**Canonical invocations** (produces all three eps files for this project):

```bash
conda run -n gw_pta python scripts/run_power_anisotropy.py --eps 0.20
conda run -n gw_pta python scripts/run_power_anisotropy.py --eps 0.38
conda run -n gw_pta python scripts/run_power_anisotropy.py --eps 0.66
```

**CLI arguments:**

| Arg | Default | Type | Meaning |
|---|---|---|---|
| `--eps` | `0.66` | float | M-sigma intrinsic scatter ε (dex); controls SMBHB population model |

**Outputs:**

| File | Size | Description |
|---|---|---|
| `results/power_anisotropy_eps020.npz` | 3.2 GB | Power anisotropy analysis for ε=0.20 |
| `results/power_anisotropy_eps038.npz` | 3.2 GB | Power anisotropy analysis for ε=0.38 |
| `results/power_anisotropy_eps066.npz` | 3.2 GB | Power anisotropy analysis for ε=0.66 |

**Wall time:** ~60 minutes per run on a typical workstation. Dominated by `generate_realizations` (10 000 realizations × nside=8, ~37 min extrapolated) and five passes of `compute_power_cls` (no exclusion + four exclusion levels, ~22 min total extrapolated). `luminosity_function` takes ~6 s.

**Consumer notebooks:** [[../notebooks/guide_power_anisotropy]], [[../notebooks/guide_model_comparison]]

## Known gotchas

- **`exclude_top_n` uses ledger rank, not full-population rank.** Only the
  top-100 brightest sources per frequency are stored; exclusion cannot reach
  beyond the ledger. See `[[../code/gwb_sources_power_anisotropy]]`.
- **Absolute $C_\ell$ are raw `anafast` output.** Not normalized by $C_0$.
  Consumers must divide by index 0.
- **lmax = 23 exceeds NANOGrav 15yr reach ($\ell_{\max} = 6$).** Consumers
  that compare to NANOGrav must slice `[..., :7]`.

## Related pages

`[[../concepts/Cl_over_C0]]`, `[[../concepts/brightest_source_fraction]]`,
`[[../concepts/SMBH_population_model]]`, `[[../concepts/shot_noise]]`,
`[[../code/gwb_sources_power_anisotropy]]`, `[[../code/gwb_sources_population]]`,
`[[../code/gwb_sources_sources]]`, `[[../conventions]]`

## 2026-08-11 schema-v2 production path

The paper-v2 remediation uses
`new_montecarlos_codex/run_new_power_anisotropy.py`, not the historical script
documented above. Corrected products are written alongside the preserved old
files under `new_montecarlos_codex/results_full_moment_v2/`:

```bash
conda run --no-capture-output -n gw_pta python \
  new_montecarlos_codex/run_new_power_anisotropy.py \
  --eps 0.20 --nrel 10000 --nside 8 --n-brightest 100 --seed 42 \
  --individual-threshold 500 --tail-grid-size 4096
```

Run the same command for $\varepsilon=0.38,0.66$. The marked-Poisson
order-statistic sampler draws the brightest 500 events explicitly, stores a
complete descending top-100 identity ledger, and represents the unresolved
population by explicit positive compound-Poisson $Q$, full $S_2$, and dipole
covariance. Positive Gamma/Dirichlet maps conserve each realized total and are
used only for $\ell\ge2$; direct $Q$ and $\mathbf D$ define $C_0$ and $C_1$.
Schema-v2 metadata makes an old product a hard error for corrected consumers.

After each common power run, the compact population product is derived without
additional random draws:

```bash
conda run --no-capture-output -n gw_pta python \
  new_montecarlos_codex/run_new_population_analysis.py \
  --eps 0.20 --nrel 10000 --n-top 20 --seed 42 \
  --individual-threshold 500 \
  --from-power new_montecarlos_codex/results_full_moment_v2/sampled_power_anisotropy_eps020.npz
```
