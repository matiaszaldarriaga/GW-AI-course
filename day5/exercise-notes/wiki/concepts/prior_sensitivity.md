# Prior sensitivity

How much does the marginalized posterior for the GW background
amplitude depend on the choice of prior on per-pulsar nuisance
variances? The answer: it depends on whether the priors are independent
per pulsar or pooled in a hierarchical model.

## Setup

Covariance model in one bin:
$$\Sigma(c, \mathbf v) = c\,R_\rho + \mathrm{diag}(v_1,\ldots, v_{N_p}),$$
with $c = A_{\rm GW}^2$ and $v_i$ per-pulsar nuisance variances.

## Ridge posterior

In the large-$N_f$ (many Fourier bins) limit, after the diagonals
constrain the residuals $u_i - c \approx v_i$:

$$p(c\mid S) \propto p(c)\, L_{\rm off}(c)\, \prod_{i=1}^{N_p} \pi_v(u_i - c).$$

The **product over pulsars** is the critical feature. A small bias per
pulsar multiplies into a large total bias with $N_p$ growing.

## Effect of common priors

| Nuisance prior | Ridge factor $\prod \pi_v(u_i - c)$ | Behavior |
|---|---|---|
| Flat in $v_i$ | 1 | Neutral |
| Flat in $\tau_i$ (SD) | $\prod (u_i-c)^{-1/2}$ | Tilts posterior toward larger $c$ |
| Log-flat in $v_i$ or $\tau_i$ | $\prod (u_i-c)^{-1}$ | Non-integrable at boundary; pathological without a hard lower cutoff $v_{\min}>0$ |
| Hierarchical (Gamma-Exp) | $[b + \sum_i (u_i-c)]^{-(a+N_p)}$ | Depends on collective variance sum; finite at boundary |

## Cure

Replace per-pulsar independent priors with a hierarchical model tying
$v_i$ to a common population scale. The posterior then depends on a
**collective** quantity $\sum_i (u_i - c)$ rather than a **product** of
per-pulsar factors. Much smaller dependence on prior choice.

## Relation to the KL hierarchy

Not directly part of the hierarchy argument — this note studies
**prior-volume** effects in incoherent searches, not the scaling of
detection strength with $p$. But it reinforces the same moral:
incoherent searches are subtle and easily biased; coherent searches
avoid most of these issues because they don't marginalize over a
random field.

## Source pages

- [[../sources/pta_prior_sensitivity]] — canonical note (toy models, numerical posteriors).
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — uses the same Schur-complement profiling to define $F^{\rm prof}_{\eta\eta} = F_{\eta\eta} - F_{\eta\lambda}F_{\lambda\lambda}^{-1}F_{\lambda\eta}$, the nuisance-marginalized Fisher for HD shape detection.
- [[../sources/pta_curn_hd_cross_only]] — the one-sided CURN prior $A_{\rm C} \ge 0$ generates a boundary factor $\log\Phi((\hat P-B)/\sigma_P)$ in the marginal HD posterior, a distinct prior-sensitivity mechanism (nuisance-direction hard boundary) from the per-pulsar noise-prior effects above.

## Paper uses

- Not currently cited. Could inform discussion of why NANOGrav
  posteriors depend on prior choices, but outside the paper's core
  argument.

## Related concepts

[[coherent_vs_incoherent]], [[shot_noise]], [[matched_filter_vs_power]].
