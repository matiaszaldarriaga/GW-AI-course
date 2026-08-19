# Sampled-Property Full-Moment Monte Carlo

**Location:** `new_montecarlos_codex/`
**Status:** schema-v2 production complete; all end-to-end product checks pass
**Production date:** 2026-08-11

## Purpose

The paper's legacy Monte Carlos assign every source in one `(f,M)` bin the same
representative power. The sidecar instead samples redshift, mass ratio, and
inclination for each tracked source while retaining the legacy Poisson counts
and the exact conditional-mean identity

$$
E[h_s^2\mid f,M] = h_{s,\mathrm{legacy}}^2(f,M).
$$

Thus the mean spectrum and its $2.5\times10^{-15}$ calibration at 1/yr are
unchanged; only source-level scatter is added. The maximum numerical mismatch
of the mean source-power grids is about $6.5\times10^{-16}$ relative.

## Production artifacts and rollback

- `sampled_population_analysis_eps{020,038,066}.npz`: 10,000 realizations,
  44 frequencies, top-20 source ledger.
- `sampled_power_anisotropy_eps{020,038,066}.npz`: 10,000 realizations,
  44 frequencies, `nside=8`, top-100 ledger, `cls_all`, and map cubes.
- `sampled_c1c0_distribution_eps066.npz`: 10,000-realization sampled 3D-walk
  cache for the Fig. 4 replacement.

The 2026-07 products remain immutable under
`new_montecarlos_codex/results/` (11 NPZ files, 10,666,893,206 bytes; hashes in
`wiki/reviews/paper_v2_rerun_baseline_manifest.json`). Corrected products live
alongside them under `new_montecarlos_codex/results_full_moment_v2/`; both
directories are ignored and retained. See [[../reproducibility]] for commands.

## 2026-08-11 defect and resolution

The later code audit identified a production defect in the 2026-07 sidecar:
the faint-source angular second moment used $nE[w]^2$ rather than
$nE[w^2]=n(E[w]^2+\mathrm{Var}[w])$, and downstream quantities labeled
all-source omitted the unresolved remainder. Schema v2 fixes the data model:

1. Every realization/frequency stores total $Q$, full $S_2$, $Q^2/S_2$, the
   complete brightest-source ledger and explicit $(Q,S_2)$ remainder.
2. The brightest 500 marked-Poisson events are sampled in order, making the
   stored top-100/top-20 ledgers complete rather than threshold-conservative.
3. The direct dipole uses individual directions plus unresolved random-walk
   covariance $S_{2,\rm bulk}/3$; direct $C_0,C_1$ are authoritative.
4. Positive Gamma/Dirichlet maps conserve realized $Q$ and support
   $\ell\ge2$; no clipped Gaussian or mean-filled dipole is used.
5. A schema/version gate makes old incomplete products a clear error for
   corrected consumers. Population and Figure-4 products are bitwise
   derivatives of the common power run, with no additional random draws.

The older integration work remains relevant as historical context:

1. **Missing Fig. 4 replacement:**
   `generate_sampled_c1c0_distribution.py` implements the same standalone 3D
   random walk used by the paper, now with sampled source powers. The writer
   candidate is `figures/new/c1c0_distribution_3d_walk.pdf`. This is distinct
   from the HEALPix `anafast` diagnostic named `c1c0_distribution.pdf` in the
   comparison report.
2. **Mechanical result switch:** the exact old-to-new basename map and affected
   scripts are in `reports/writer_handoff.md`.
3. **Inline numbers and tables:** the handoff contains all strain ratios,
   Fig. 5 dominance fractions, and Fig. 4 caption statistics.
   `tables/new_conditional_stats_latex.txt` and
   `tables/new_percentiles_latex.txt` contain LaTeX-ready Tables I--III,
   including the uncertainty columns absent from the first previews.
4. **Threshold convergence:** `run_threshold_sweep.py` holds the configuration
   fixed across thresholds 100/500/2000/5000. Threshold 500 is conservative;
   most medians are within about 6% of threshold 5000. The largest discrepancy
   is epsilon 0.20 at 0.085/yr: median 9% low, 95th percentile 17% low.

## Pre-fix headline values (comparison baseline)

- Median realized/mean strain power at epsilon 0.66, 0.085/yr: **0.455**
  (paper currently says 55%; writer suggestion 46%).
- At 1.029/yr the ratios for epsilon 0.20/0.38/0.66 are
  **0.672 / 0.413 / 0.051**.
- For epsilon 0.66 the median brightest share
  $p_1^2/\sum_a p_a^2$ at 0.085/0.278/1.029 per yr is
  **0.660 / 0.714 / 0.770**.
- Sampled 3D-walk Fig. 4 at 0.085/yr has median
  $C_1/C_0=0.0494$ and median $N_{\rm eff}=18.98$.
  The current caption's "peak near 0.04" is actually the legacy median; the
  writer should say "median near 0.05," not "peak."

## Corrected approximation contract

`individual_threshold=500` is now the number of explicitly sampled global
order statistics per frequency, not an incomplete bin-selection threshold.
The top-100 ledger is guaranteed complete and the compact top-20 product is
its bitwise prefix. The unresolved population contributes positive realized
$Q$, full $S_2$, count, upper bound, and random-walk covariance.

For the direct walk, the unresolved vector has zero mean and component
variance $S_{2,\rm bulk}/3$. Its $p_1$, $p_2$, $\eta$, and $\eta_2$ overlays
use the same complete ledger plus explicit full-moment remainder.

## Corrected headline values

At $f=0.085\,{\rm yr}^{-1}$ the corrected median
$N_{\rm eff}$ and direct $C_1/C_0$ are, respectively:

- $\varepsilon=0.20$: **1167.04**, **0.000779**;
- $\varepsilon=0.38$: **181.62**, **0.005058**;
- $\varepsilon=0.66$: **18.94**, **0.050472**.

The corresponding probabilities of $C_1/C_0>0.2$ are
**0.0011 / 0.0183 / 0.1796**. The model ordering is unchanged at every
representative frequency. For $\varepsilon=0.66$, the median fraction
$p_1^2/(S_2/Q^2)$ is **0.650 / 0.708 / 0.771** at
$f=0.085/0.278/1.029\,{\rm yr}^{-1}$. At the lowest frequency the brightest
source's $h_0$ 95th percentiles are
**$3.49/6.57/11.7\times10^{-15}$** across the three models.

The largest headline correction is the low-frequency, low-scatter
$N_{\rm eff}$ value, **1810.61 $\rightarrow$ 1167.04**. Its dipole moves from
0.000530 to 0.000779: large in relative terms but still below $10^{-3}$ and
far from every paper-relevant anisotropy threshold. All qualitative model
orderings, exceedance regimes, and brightest-source detectability statements
remain unchanged. Complete old/new percentiles and hashes are in
`wiki/reviews/paper_v2_full_moment_rerun_comparison.html`; the schema and
identity inventory is in
`wiki/reviews/paper_v2_full_moment_validation.json`.

## Writer entry point

The checked paper-v2 registries under `paper_v2/structure/` are the current
per-artifact map. Corrected publication consumers use only strict schema-v2
products; the old writer handoff is retained as baseline history.

## Verification

```bash
conda run -n gw_pta pytest tests/test_new_montecarlos_codex.py
conda run -n gw_pta python new_montecarlos_codex/generate_sampled_c1c0_distribution.py
conda run -n gw_pta python new_montecarlos_codex/run_threshold_sweep.py
conda run -n gw_pta python new_montecarlos_codex/generate_writer_handoff.py
```

After the full-moment implementation, the complete suite passes **37/37**;
the production product validator separately checks all ledger, moment,
dipole, map-normalization, schema, and bitwise common-run identities.

## Related pages

- [[../figures/c1c0_distribution]]
- [[../concepts/brightest_source_fraction]]
- [[../concepts/N_eff]]
- [[../reproducibility]]
