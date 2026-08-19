# Figure: Brightest-source concentration

**File:** `paper_v2/figures/p1_distributions.pdf`
**Generator:** `paper_v2/scripts/fig_p1_distributions.py`
**Updated:** 2026-08-11 (schema-v2 full moments)

## What it shows

For the three calibrated $M$--$\sigma$ scatter models and three representative
frequency bins, the left panel shows the distribution of the complete-ledger
brightest-source fraction $p_1=w_1/Q$. The right panel shows the fraction of
the direction-averaged anisotropy moment carried by that source,

$$
{p_1^2\over\sum_a p_a^2}={w_1^2\over S_2}.
$$

The denominator is the full schema-v2 $S_2$, including the explicit faint
remainder. It is not a sum over the stored top 20 or top 100 sources.
The corrected median fractions at $f=0.085/0.278/1.029\,{\rm yr}^{-1}$ are
**0.401/0.499/0.614**, **0.503/0.585/0.677**, and
**0.650/0.708/0.771** for $\varepsilon=0.20/0.38/0.66$, respectively.

## Inputs and reproduce

The generator reads
`new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps{020,038,066}.npz`.
Those compact products are bitwise derivatives of their common 10,000-
realization power runs.

```bash
conda run --no-capture-output -n gw_pta python \
  paper_v2/scripts/fig_p1_distributions.py
```

## Concepts and paper use

- [[../concepts/brightest_source_fraction]] — complete individual-source
  ledger and $p_1$.
- [[../concepts/N_eff]] — full $S_2/Q^2=1/N_{\rm eff}$ denominator.
- [[../concepts/dipole_distribution]] — the direction-averaged scale about
  which the realized direct dipole fluctuates.
- `paper_v2/sections/dipole_source.tex`, `fig:p1_distributions`.

---

```json
{"slug": "p1_distributions", "concepts": ["brightest_source_fraction", "N_eff", "dipole_distribution"], "generator": "paper_v2/scripts/fig_p1_distributions.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps*.npz"], "paper_uses": ["paper_v2/sections/dipole_source.tex, fig:p1_distributions"]}
```
