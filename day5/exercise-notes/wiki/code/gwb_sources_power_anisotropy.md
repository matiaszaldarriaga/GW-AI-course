# `gwb_sources.power_anisotropy`

**Source:** `gwb_sources/power_anisotropy.py`
**Type:** Python module
**Ingested:** 2026-04-13

## Purpose

Computes the source-power-sky angular power spectra $C_\ell^{(P)}$ from
Monte Carlo realizations of discrete SMBHB populations. Each realization
is a HEALPix power map $P(\hat n) = \sum_a h_{s,a}^2\,\delta^{(2)}(\hat n,
\hat n_a)$; this module calls `healpy.anafast` to decompose it into
$C_\ell$ and aggregates those spectra across many realizations. The
module also supports post-hoc exclusion of the brightest sources using
a stored per-realization ledger, enabling studies of how the spectrum
changes with the brightest-source fraction $p$.

**Convention note:** all $C_\ell$ here are $C_\ell^{(P)}$ (source-power
sky). They are **not** the pulsar-map spectra $C_\ell^{(b)}$; see
[[../concepts/Cl_over_C0]] and [[../conventions]] for the transfer
function connecting the two.

## Public API

| Function | Inputs | Output | Notes |
|---|---|---|---|
| `compute_power_cls(realizations, exclude_top_n=None, exclude_above_flux=None)` | list of realization dicts; optional exclusion params | `ndarray (Nrel, Nfreq, lmax+1)` | Main entry point |
| `compute_power_statistics(cls, percentiles=None)` | `(Nrel, Nfreq, lmax+1)` array | dict of mean/median/std/percentiles | Aggregates over realizations axis |
| `save_power_results(filepath, cls, statistics=None)` | path, cls array, optional stats dict | `.npz` on disk | Saves raw + optional summary |
| `load_power_results(filepath)` | path | dict matching `save_power_results` schema | Restores exactly what was saved |

`_apply_exclusion` is private; callers should not rely on it.

## Key formulas implemented

For legacy realizations, `hp.anafast` computes

$$C_\ell = \frac{1}{2\ell+1}\sum_m |a_{\ell m}|^2, \qquad
  a_{\ell m} = \int P(\hat n)\,Y_{\ell m}^*(\hat n)\,d\hat n$$

applied to the pixelized map. Schema-v2 realizations replace its $\ell=0,1$
entries by the direct formulas documented below and retain the transform for
$\ell\ge2$. `lmax` is set to `3*nside - 1` (healpy default). The resulting
$C_\ell$ are in units of $(\text{strain}^2)^2 /
\text{sr}$ (i.e. $h_s^4$); ratios $C_\ell/C_0$ are dimensionless and
match the canonical formula in [[../concepts/Cl_over_C0]]:

$$\frac{C_\ell}{C_0} = \sum_{a,b} p_a p_b\, P_\ell(\hat n_a \cdot \hat n_b).$$

Exclusion applies by subtracting the flagged sources' $h_s^2$
contributions pixel-by-pixel from the map before calling `anafast`. The
`brightest` ledger (keyed by frequency bin) stores `h2s` sorted
descending and the corresponding HEALPix pixel indices, making the two
exclusion modes (`exclude_top_n`, `exclude_above_flux`) commutable with
OR logic.

## Known gotchas

- **Exclusion is OR, not AND.** If both `exclude_top_n` and
  `exclude_above_flux` are set, a source is excluded if it satisfies
  either condition, not both.
- **`exclude_top_n` uses ledger rank.** Schema-v2 records the guaranteed
  completeness rank and raises if an exclusion exceeds it. Historical
  products lack that guarantee and are not corrected-analysis inputs.
- **`lmax` tied to `nside`.** Downstream consumers that request a fixed
  $\ell_{\max}$ (e.g. $\ell=6$ to match NANOGrav 15yr) must slice the
  returned array; it is not configurable in the call.
- **Absolute $C_\ell$ values are not normalized.** The array holds raw
  `anafast` output, not $C_\ell/C_0$. Consumers must divide by
  `cls[:,:,0]` to obtain the paper's primary observable.

## Consumers

- `scripts/` batch scripts that call `compute_power_cls` and store
  results under `results/*.npz`.
- Marimo notebooks that plot $C_\ell/C_0$ distributions vs. $p$ (see
  `wiki/notebooks/` once ingested).
- `tests/generate_reference_data.py` — generates reference `.npz` files
  for regression tests.

## Related pages

[[../concepts/Cl_over_C0]], [[../concepts/brightest_source_fraction]],
[[../concepts/shot_noise]], [[../concepts/transfer_function]],
[[../concepts/N_eff]], [[../conventions]]

## 2026-08-11 full-moment remediation

Schema-v2 realizations now carry authoritative direct monopole and dipole
moments. `compute_power_cls` keeps `healpy.anafast` for $\ell\ge2$, but replaces
the first two entries by

$$
C_0={4\pi\over N_{\rm pix}^2}Q^2,
\qquad
C_1={4\pi\over N_{\rm pix}^2}|\mathbf D|^2,
\qquad
{C_1\over C_0}={|\mathbf D|^2\over Q^2}.
$$

The $N_{\rm pix}^{-2}$ factor is required because each stored map value is
power integrated over a pixel rather than intensity per steradian. Top-source
exclusions subtract the same complete ledger entries from both the map and the
direct $(Q,\mathbf D)$ moments; requesting a rank beyond the guaranteed ledger
completeness now fails explicitly. Tests independently fix the absolute
normalization and the direct-dipole ratio.
