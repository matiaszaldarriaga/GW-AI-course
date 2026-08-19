# Figure: Simple estimators of source content (universality)

**File:** `paper_v2/figures/source_content_estimators.pdf`
**Ingested:** 2026-06-22
**Updated:** 2026-08-11 (direct full-moment estimators)

> All pooled points now use direct $x=|\mathbf D|^2/Q^2$,
> complete-ledger $p_1$, and $N_{\rm eff}=Q^2/S_2$ including the faint
> remainder. "Universal" here can only mean approximately model- and
> frequency-independent over the three calibrated models and tested grid.

## What it shows

A two-panel single-column figure (paper Fig. 6) testing the simple closed-form
estimators of source content against the Monte Carlo. Within each
$\varepsilon$ model, every realization at every frequency is pooled with
`ravel()` over the full `(Nreal, Nfreq)` grid; the three models remain separate
colored point sets so their agreement can be tested. The points are binned by
measured $C_1/C_0=x$; each point is the conditional mean (with $1\sigma$ scatter) of the
brightest-source fraction $p_1$ (left) and the effective number of sources
$N_{\rm eff} = 1/\sum_a p_a^2$ (right) in that $x$ bin.

The overlaid black curves are the back-of-envelope estimates
$\langle p_1\mid x\rangle \simeq \sqrt{x}$ (`eq:p1_given_x_simple`) and
$\langle N_{\rm eff}\mid x\rangle \simeq 1/x$ (`eq:neff_given_x`). Across the
plotted $0.05\le x<0.9$ bins, the corrected products give
$\langle p_1\mid x\rangle/\sqrt{x}=0.81$--$0.98$ and
$x\langle N_{\rm eff}\mid x\rangle=0.85$--$1.28$. The model-to-model spread in
$\langle p_1\mid x\rangle$ is at most 0.028; the $N_{\rm eff}$ spread is largest
in the lowest dipole bin (4.93) and falls below 0.37 for $x\ge0.17$.
Thus “universal” is shorthand for approximate model- and
frequency-independence over this tested family, not an exact identity.

## Generator

`paper_v2/scripts/fig_source_content_estimators.py` (updated 2026-08-11;
imports the shared style module `paper_v2/scripts/_paperstyle.py` via
`apply_style()`, `figsize_2col`, and the `EPS_MODELS` color/label map).
Run: `conda run -n gw_pta python paper_v2/scripts/fig_source_content_estimators.py`.
$p_1$, $\eta$, $N_{\rm eff}$, and $x$ are defined exactly as in Table I from
the direct schema-v2 moments. The loader `ravel()`s over
the full `(Nreal, Nfreq)` grid separately for each model before binning by $x$.

## Inputs

- `new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps{020,038,066}.npz`
  — direct `c1c0_direct`, `brightest_source_fraction`, `neff_full`, and full
  $Q,S_2$ arrays from the common production runs.

## Concepts illustrated

- [[concepts/brightest_source_fraction]] — $\langle p_1\mid x\rangle\simeq\sqrt{x}$
  and the model-independence of the inverse problem.
- [[concepts/N_eff]] — $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$.
- [[concepts/dipole_distribution]] — the forward law that makes the inverse
  universal.

## Paper sections using this figure

- `paper_v2/sections/dipole_source.tex`, subsection "The source content of a
  given dipole" (`\label{fig:source_content_simple}`); figure 6 in the paper.

## Related pages

- [[figures/p1_neff_conditional]] — the full conditional distributions behind
  these means (for $\varepsilon=0.66$, conditioned on $C_1/C_0>0.2$).
- [[figures/c1c0_neff_vs_freq]] — the same ledger $N_{\rm eff}$ vs frequency.

---

```json
{"slug": "source_content_estimators", "concepts": ["brightest_source_fraction", "N_eff", "dipole_distribution"], "generator": "paper_v2/scripts/fig_source_content_estimators.py", "inputs": ["new_montecarlos_codex/results_full_moment_v2/sampled_population_analysis_eps*.npz"], "paper_uses": ["paper_v2/sections/dipole_source.tex, fig:source_content_simple"]}
```
