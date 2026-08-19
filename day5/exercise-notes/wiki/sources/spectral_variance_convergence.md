# Why the spectral variance of $h_c^2$ does not converge for heavy-tailed populations

**Source:** `references/spectral_variance_convergence_note.md`
**Type:** internal analysis note
**Ingested:** 2026-04-14

## Summary

The exact Poisson variance of the total realized strain,
$\text{Var}[h_{\rm tot}^2] = \sum_k \bar N_k h_{s,k}^4$, is mathematically
correct and verified against Monte Carlo in a 3-bin toy (ratio 0.9997 with
$10^6$ draws). For heavy-tailed SMBHB populations ($\varepsilon = 0.66$),
however, 99.86% of this variance comes from mass bins with expected counts
$\bar N_k < 10^{-7}$ — sources that essentially never fire. The SPZ
characteristic-function PDF grid ($x_{\max} = 3.5 \times 10^5$ in
rescaled units, $2^{24}$ points at $\delta x = 0.021$) does not extend
far enough to capture those bins' $x^2$ contribution, so the PDF-derived
second moment underestimates the Poisson variance by $\sim 1000\times$,
and a naive Monte Carlo (10K realizations) is off by $\sim 5000\times$.
The mean and all robust quantiles (median, percentile bands) converge
fine because they weight by $h_s^2$, not $h_s^4$, and the bulk of the
distribution determines them. As a result the frequency-scatter /
coefficient-of-variation figure was dropped from the paper.

## Key findings

- **Poisson formula verified:** $\text{Var}[h_{\rm tot}^2] = \sum_k \bar N_k h_{s,k}^4$
  matches MC at the $<0.03\%$ level in a controlled toy model.
- **Variance budget ($\varepsilon = 0.66$, lowest frequency):**
  - SPZ grid range: 0.14% of total variance
  - Beyond-grid bright tail: 99.86% of total variance ($\bar N \sim 10^{-7}$)
- **Mean convergence ($\varepsilon = 0.66$):** theory $2.283\times 10^{-28}$,
  MC $2.294\times 10^{-28}$ (ratio 1.005).
- **Variance convergence failure ($\varepsilon = 0.66$):** Poisson formula
  $2.28\times 10^{-50}$; SPZ PDF integral $2.71\times 10^{-53}$ ($\times 0.001$);
  MC (10K) $4.40\times 10^{-54}$ ($\times 0.0002$).
- **Mild-tail comparison ($\varepsilon = 0.20$):** grid captures 94.3% of
  variance; theory, PDF, and MC all agree.
- **Root cause:** the variance weights by $h_s^4$ (second power of the
  single-source strain), which amplifies the extreme tail far more than the
  mean's $h_s^2$ weighting. Extending the grid to $x_{\max} \sim 10^6$
  would require incompatible combinations of grid extent and $\delta x$.
- **Robust statistics unaffected:** the SPZ PDF correctly captures median,
  5th/95th percentiles, and the full PDF shape; median/mean ratio from PDF
  (0.594) and MC (0.568) agree well.
- **Lamb & Taylor (2024) formula** $\text{Var}[\Omega_{\rm GW}]/
  \langle\Omega_{\rm GW}\rangle^2 \approx 1/N_c$ is a correct Poisson
  identity but is not a practically measurable quantity when the mass
  function extends to very high masses — same convergence failure applies.

## Concepts touched

- [[concepts/SMBH_population_model]] — SPZ characteristic-function PDF,
  luminosity function exponent $\varepsilon$, bin occupancy $\bar N_k$
- [[concepts/N_eff]] — inverse participation ratio; convergent first-moment
  quantity, unlike the variance
- [[concepts/brightest_source_fraction]] — $p = h_{s,\max}^2 / h_{\rm tot}^2$;
  convergent; not affected by this issue
- [[concepts/shot_noise]] — the Poisson variance formula is the exact
  shot-noise result; the note explains why it is numerically inaccessible
  for heavy tails
- [[concepts/coherent_vs_incoherent]] — paper's main results ($p$,
  $N_{\rm eff}$, $C_1/C_0$, KL hierarchy) are all first-moment quantities
  and are not affected

## Current paper citations

(None — internal note.)

## Relevance to the project

This note documents and closes a dead end: the coefficient of variation
$\text{cv}[h_c^2(f)]$ cannot be reliably estimated from the SPZ PDF or
from feasible Monte Carlo runs for the astrophysically motivated
$\varepsilon = 0.66$ model. The decision to drop the frequency-scatter
figure is justified here. All paper figures that remain (mean, median,
percentile bands from the SPZ PDF) are unaffected.

## Relations to other sources

- `sources/arxiv_2406_17010.md` — SPZ characteristic-function method;
  Fig. 3 of that paper shows the power-law PDF tail that the note
  references; the grid truncation issue is not discussed there.
- `sources/pn_C1_over_C0.md` — $\mathbb{E}[C_1/C_0] = \sum p_a^2$ is a
  first-moment quantity and converges in the same regime where the variance
  does not.
- `sources/pta_1src_vs_CL.md` — Fisher information on $p$ involves
  $\sum s_L$ (first moments of block response), also convergent.

## Caveats / open questions

- A grid with $x_{\max} \sim 10^6$ and fine enough $\delta x$ could
  capture the variance for $\varepsilon = 0.66$, but would require
  $\sim 5\times 10^7$ points; not attempted.
- The note does not evaluate whether the variance becomes accessible for
  population models with $\varepsilon$ between 0.20 and 0.66; a
  transition $\varepsilon$ is not computed.
- The Lamb & Taylor (2024) formula is cited but not fully verified against
  an independent derivation in this project.
