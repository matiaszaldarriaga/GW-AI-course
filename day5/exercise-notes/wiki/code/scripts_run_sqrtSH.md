# `scripts/run_sqrtSH_realizations.py`

**Source:** `scripts/run_sqrtSH_realizations.py`
**Type:** Batch script
**Ingested:** 2026-04-13
**Key commits:** `461b99a` (initial), `926ec5f` (parameterize `--nside`, lmax convergence study)

## Purpose

Generates Monte Carlo realizations of the square-root spherical harmonic (sqrt-SH)
GW power sky following the NANOGrav 15yr anisotropy analysis (2306.16221). Each
realization draws $b_{LM}$ from NANOGrav's uniform prior, constructs the positive
power map $P(\hat\Omega) = [\sum_{LM} b_{LM} Y_{LM}]^2$, and records the resulting
angular power spectrum $C_\ell$ and its ratio $C_\ell/C_0$. The accumulated
statistics across $N_{\rm rel}$ realizations characterize the prior distribution
on $C_\ell/C_0$ — the central quantity for the project's argument that the
NANOGrav anisotropy upper limits are prior-driven.

## CLI

```
python scripts/run_sqrtSH_realizations.py [--nside NSIDE]
```

| Argument | Default | Effect |
|---|---|---|
| `--nside` | 8 | HEALPix resolution; sets `lmax = 3*nside - 1` |

`Nrel = 10000`, `seed = 42` are hardcoded. The older `lmax3`/`lmax6` files
were produced by a separate version of the script that exposed `lmax_blm`
directly; those runs used `nside=32` and `nside=8` respectively (see result pages).

## Algorithm

1. Fix $b_{00} = 1$ (breaks scale and parity degeneracy).
2. For $L = 1, \ldots, L_{\max}^b$: draw $b_{L0} \sim U[-50, 50]$; for
   $M > 0$ draw amplitude $|b_{LM}| \sim U[0, 50]$ and phase
   $\phi \sim U[0, 2\pi]$, set $b_{LM} = |b_{LM}| e^{i\phi}$.
3. Convert $b_{LM}$ alm array to HEALPix pixel space via `healpy.alm2map`.
4. Square the field: $P = f^2$.
5. Compute $C_\ell$ of $P$ via `healpy.anafast` up to `lmax = 3*nside - 1`.
6. After all realizations: compute per-multipole statistics of $C_\ell/C_0$
   (mean, median, 2.5th, 25th, 75th, 97.5th percentiles) and save to npz.

**Convention note:** `lmax` is $\ell_{\max}^a$ (the anafast truncation) and
also sizes the $b_{LM}$ alm array in the default path, so $L_{\max}^b = $ `lmax`
there. The `lmax_blm` runs decouple the two: `lmax3` uses $L_{\max}^b = 3$
at `nside=32`, `lmax6` uses $L_{\max}^b = 6$ at `nside=8`.

## Outputs

| File | `nside` | `lmax` ($\ell_{\max}^a$) | `lmax_blm` | `Nrel` | Description |
|---|---|---|---|---|---|
| `sqrtSH_realizations.npz` | 8 | 23 | — | 10 000 | Original default run |
| `sqrtSH_realizations_nside8.npz` | 8 | 23 | — | 10 000 | Same as above (named run) |
| `sqrtSH_realizations_nside16.npz` | 16 | 47 | — | 10 000 | Higher-res convergence check |
| `sqrtSH_realizations_nside32.npz` | 32 | 95 | — | 10 000 | Higher-res convergence check |
| `sqrtSH_realizations_lmax3.npz` | 32 | 6 | 3 | 50 000 | NANOGrav-faithful: $L_{\max}^b = 3$ |
| `sqrtSH_realizations_lmax6.npz` | 8 | 23 | 6 | 10 000 | Double-truncation: $L_{\max}^b = 6$ |

## Reproduce

**Environment:** `gw_pta` conda env (see [[../environment]]).

**Canonical invocation** (default nside=8, produces the primary result file):

```bash
conda run -n gw_pta python scripts/run_sqrtSH_realizations.py --nside 8
```

**Additional runs** (convergence study):

```bash
conda run -n gw_pta python scripts/run_sqrtSH_realizations.py --nside 16
conda run -n gw_pta python scripts/run_sqrtSH_realizations.py --nside 32
```

**CLI arguments:**

| Arg | Default | Type | Meaning |
|---|---|---|---|
| `--nside` | `8` | int | HEALPix resolution; sets `lmax = 3*nside - 1` and sizes both the b_LM expansion and the anafast truncation |

`Nrel = 10000` and `seed = 42` are hardcoded.

**Outputs:**

| File | Size | Description |
|---|---|---|
| `results/sqrtSH_realizations_nside8.npz` | 2.2 MB | Default run: nside=8, lmax=23, 10 000 realizations |
| `results/sqrtSH_realizations_nside16.npz` | 4.9 MB | Convergence check: nside=16, lmax=47 |
| `results/sqrtSH_realizations_nside32.npz` | 12 MB | Convergence check: nside=32, lmax=95 |

**Wall time:** ~12 seconds for `--nside 8` (1.2 ms per realization × 10 000). `--nside 32` is slower due to larger alm arrays and pixel maps; expect ~5–10 minutes.

**Consumer notebooks:** [[../notebooks/guide_sqrtSH_model]]

## Key findings

- The 97.5th-percentile $C_1/C_0$ under the NANOGrav prior ($L_{\max}^b = 3$)
  is 0.23, falling to 0.010 when $L_{\max}^b = 23$ (nside=8) and 0.0007 when
  $L_{\max}^b = 95$ (nside=32). This demonstrates the strong convergence: as
  more modes are available to carry power, $C_\ell/C_0$ at low $\ell$ is
  suppressed by orders of magnitude. The upper limit is prior-driven and
  non-convergent.
- The mean $C_1/C_0 = 0.0795$ at $L_{\max}^b = 3$ (NANOGrav) vs. $0.0002$
  at $L_{\max}^b = 95$. The prior peaks at an anisotropy level that has no
  astrophysical justification.

## Known gotchas

- **`sqrtSH_realizations.npz` and `sqrtSH_realizations_nside8.npz` share
  all parameters** (same seed, nside, lmax, Nrel) but were produced at
  different times; verify arrays agree before treating as identical.
- **`lmax_blm` scalar is absent** from the nside-parameterized npz files;
  only the `lmax3`/`lmax6` runs record it.
- **`example_maps` is zeroed** (`shape=(0,0)`) in the `lmax3` and `lmax6`
  files; pixel maps were not saved for those runs.

## Consumers

- `notebooks/guide_sqrtSH_model.py` — primary analysis notebook; plots
  $C_\ell/C_0$ prior distributions and convergence across `nside`/`lmax_blm`.
- Paper section `nanograv_prior.tex` — cites the $L_{\max}^b = 3$ statistics
  as evidence the NANOGrav upper limits are prior-driven.

## Related pages

[[../concepts/sqrt_SH_basis]], [[../concepts/Cl_over_C0]],
[[../concepts/prior_sensitivity]], [[../conventions]]

## 2026-08-11 analytic low-moment sequence

The registered high-$\ell_{\max}^b$ sensitivity values no longer come from an
under-resolved squared HEALPix field. The script now supports a paired sequence
that draws one nested set of $b_{LM}$ coefficients and evaluates $C_0$ and
$C_1$ analytically from harmonic recurrences:

```bash
conda run --no-capture-output -n gw_pta python \
  scripts/run_sqrtSH_realizations.py \
  --analytic-sequence 3,6,23,47,95 --nrel 10000 --batch-size 256 \
  --suffix _convergence
```

The output is
`results/sqrtSH_full_moment_v2/sqrtSH_low_moments_convergence.npz` (schema 2).
Independent high-margin pixel transforms use $N_{\rm side}=16,32,64,128,256$
and give absolute $C_1/C_0$ shifts of
$2.47\times10^{-5}$, $1.43\times10^{-6}$, $2.33\times10^{-7}$,
$5.48\times10^{-8}$, and $7.52\times10^{-9}$. The paired 95th percentiles are
$0.20243$, $0.085894$, $0.0087566$, $0.0022178$, and $0.0005640$ for
$\ell_{\max}^b=3,6,23,47,95$, respectively. Runtime was 4.0 s inside the
sampler (5.81 s wall including environment startup).
