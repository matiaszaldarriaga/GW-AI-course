# Toy models for prior sensitivity of A_gw in PTA covariance fits

**Source:** `references/pta_toy_models_prior_sensitivity.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

The note constructs a minimal Gaussian toy model for the PTA covariance problem to isolate how the choice of prior on per-pulsar nuisance variances $v_i = \tau_i^2$ distorts the marginalized posterior for $c \equiv A_\mathrm{gw}^2$. The covariance model is $\Sigma(c, \mathbf{v}) = c R_\rho + \mathrm{diag}(v_1, \ldots, v_{N_p})$, where $R_\rho$ is an equicorrelated proxy for the HD matrix. In the large-$N_f$ ridge limit, the diagonals of the sample covariance $S$ pin each $v_i \approx S_{ii} - c$, and the marginalized posterior reduces to a product of nuisance prior densities evaluated along that ridge. Because this product multiplies over all $N_p$ pulsars, the prior sensitivity grows with array size. Log-flat priors on $v_i$ or $\tau_i$ are especially dangerous: the ridge factor $(u_i - c)^{-1}$ per pulsar produces a non-integrable edge at $c \to u_\mathrm{min}$ unless a hard lower cutoff is imposed, and that cutoff then controls the answer. A hierarchical exponential-Gamma prior cures this by replacing the per-pulsar product with a function of the collective sum $\sum_i (u_i - c)$, removing the boundary pile-up and reducing sensitivity to the shape of the per-pulsar prior.

## Key equations and claims

- **Toy covariance model** (Section 1):
  $\Sigma(c, \mathbf{v}) = c R_\rho + \mathrm{diag}(v_1, \ldots, v_{N_p})$,
  $R_\rho = (1-\rho)I + \rho\, \mathbf{1}\mathbf{1}^T$.
  Diagonals of $S$ constrain $c + v_i$; off-diagonals are the only channel that isolates $c$.

- **Exact Wishart likelihood** (Section 2):
  $p(S \mid c, \mathbf{v}) \propto |\Sigma|^{-N_f/2} \exp[-\tfrac{N_f}{2}\,\mathrm{Tr}(\Sigma^{-1} S)]$,
  with $|\Sigma|$ and $\Sigma^{-1}$ evaluated analytically via the matrix determinant lemma and Woodbury identity.

- **Large-$N_f$ ridge posterior** (Section 3):
  $p(c \mid S) \propto p(c)\, L_\mathrm{off}(c) \prod_{i=1}^{N_p} \pi_v(u_i - c)\, \mathbf{1}_{0 \le c \le u_\mathrm{min}}$,
  where $u_i \equiv S_{ii}$ and $L_\mathrm{off}(c)$ is the off-diagonal likelihood factor.

- **Ridge factors by prior choice** (Section 3, Table):

  | Prior | Ridge factor |
  |---|---|
  | flat in $v_i$ | 1 |
  | flat in $\tau_i$ | $\prod_i (u_i - c)^{-1/2}$ |
  | log-flat in $v_i$ or $\tau_i$ | $\prod_i (u_i - c)^{-1}$ (non-integrable at boundary) |

- **Equal-diagonal scaling with $N_p$** (Section 4):
  For $u_i \approx u$, the ridge factor is $(u-c)^{-N_p/2}$ (flat in $\tau$) or $(u-c)^{-N_p}$ (log-flat); for one shared nuisance variance the exponents are $-1/2$ or $-1$ regardless of $N_p$.

- **Hierarchical conjugate toy** (Section 5):
  $v_i \mid \lambda \sim \mathrm{Exp}(\lambda)$, $\lambda \sim \mathrm{Gamma}(a,b)$;
  marginalizing $\lambda$ gives $\pi(\mathbf{v}) \propto (b + \sum_i v_i)^{-(a+N_p)}$,
  so the ridge factor becomes $[b + \sum_i (u_i - c)]^{-(a+N_p)}$, which is finite at $c \to u_\mathrm{min}$ for $b > 0$.

- **Posterior mean shift** (Section 4, table): for $N_p = 8$ and the toy off-diagonal Gaussian, the mean of $c$ shifts from $\approx 0.250$ (flat in $v$) to $\approx 0.286$ (flat in $\tau$) to $\approx 0.327$ (log-flat in $v$), while the hierarchical prior gives $\approx 0.270$.

## Concepts touched

- `prior_sensitivity`
- `coherent_vs_incoherent` (background: diagonals vs cross-correlations as the distinction between the two channels)
- `shot_noise` (tangentially: the same weak-signal ridge geometry that makes individual sources hard to separate from noise is what makes the diagonal channel prior-sensitive)
- `matched_filter_vs_power` (off-diagonal vs diagonal channel maps loosely onto coherent vs power-based information)

## Current paper citations

(None yet.)

## Potential additional uses

- **Section on incoherent search limitations**: the ridge geometry plus nuisance-prior sensitivity is an independent reason why covariance-based searches are prior-dependent even for the isotropic-amplitude problem, reinforcing the hierarchy coherent > incoherent.
- **Appendix on systematic effects**: if the paper discusses why simple covariance searches can be biased, this note provides a clean analytic argument with explicit posterior formulae.
- **Referee response**: if a referee asks why log-flat RN priors affect the GW amplitude posterior, this note has a self-contained pedagogical answer with quantitative examples.

## Relations to other sources

- `references/pedagogical_note_coherent_vs_quadratic_pta_self_contained_v2.md`: the present note explicitly builds on it (Section 9). That note develops the coherent-vs-quadratic hierarchy; the present note adds the nuisance-prior layer on top of the quadratic channel.
- `references/PTA_summary_statistics (8).pdf`: Section 9 also references this; it provides the Gaussianized PTA framework (coherent Earth term + Gaussian pulsar term + noise) that the toy model approximates.

## Caveats / open questions

- The equicorrelated proxy $R_\rho$ replaces the actual HD overlap reduction function. The note acknowledges this and suggests replacing it with the true HD matrix in a follow-up numerical study (Section 7). It is not known whether the scaling with $N_p$ survives quantitatively under realistic HD correlations.
- The note explicitly flags that the exponential-Gamma hierarchical toy is not a prior recommendation for PTA analyses; more realistic choices (half-$t$, log-normal on $\tau$) are listed in Section 5.3 but not analyzed.
- The figures referenced (volume_factor_vs_c.png, posterior_comparison_vs_c.png) are described in the text but the image files are not present in the repository. The numerical claims in the tables are stated without a runnable script; they should be treated as pedagogical estimates rather than verified results until reproduced.
- The note does not connect explicitly to the $p$-scaling of KL divergences that is central to the paper. The connection (prior sensitivity degrades covariance-based searches, reinforcing the KL hierarchy) is an inference, not a claim made in the note itself.
