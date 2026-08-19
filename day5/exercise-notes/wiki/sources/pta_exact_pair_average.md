# Exact pair-average denominator and block weights for the noise-dominated benchmark

**Source:** `references/pta_covariance_exact_pair_average_note.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives the exact noise-dominated benchmark for the PTA anisotropy Fisher matrix
from first principles, without using the shortcut $\xi(\gamma)^2$ formula (which is explicitly
discarded). Every object is defined and every numerical result is reproducible.
The three outputs used by the paper are: (1) the exact isotropic-background Fisher
normalization $\Sigma_{\rm bg}^2$ with its $1/48$ Hellings-Downs integral; (2) the closed
exact form of the diagonal terms $D_L$ and the pair-average integral defining $O_L$;
and (3) tabulated numerical values of $s_L(N_p=67, 0)$ for $L=1,\dots,6$,
confirmed by Monte Carlo pair-averaging at sub-percent level for all tested $N_p$.

## Key equations and claims

**Isotropic Fisher normalization** (Sec. 4):
$$\langle F_A \rangle = \frac{N_p}{2\sigma_n^4}\!\left(1+\frac{N_p-1}{48}\right), \qquad \Sigma_{\rm bg}^2 = A^2\langle F_A\rangle.$$
The $1/48$ is the exact Legendre integral $\tfrac{1}{2}\int_{-1}^{1}\chi(\mu)^2\,d\mu = 1/48$
where $\chi(\mu)$ is the Hellings-Downs cross-curve.

**Block-weight formula** (Sec. 5 and 12):
$$s_L(N_p,0) = \frac{2L+1}{4\pi}\,\frac{D_L+(N_p-1)O_L}{1+(N_p-1)/48}.$$

**Exact diagonal terms** (Sec. 6, from Legendre expansion of $(3/4)(1+x)^2$):
$$D_1 = \pi, \qquad D_2 = \frac{\pi}{25}, \qquad D_{L\ge3} = 0.$$

**Off-diagonal pair-average** (Sec. 7):
$$O_L = \frac{1}{2}\int_{-1}^{1}d\mu\; g_L(\mu), \qquad g_L(\mu) = \frac{1}{2L+1}\sum_{M}|\kappa_{LM}(\mu)|^2,$$
where $\kappa_{LM}(\mu)$ are the sky-integral harmonic coefficients of the exact kernel
$K^{\rm tot}_\mu$ in the computational pair frame.

**Per-$L$ SNR formula** (Sec. 5):
$${\rm SNR}_L^2 = \Sigma_{\rm bg}^2\,s_L(N_p,0)\,\frac{C_L^{(P)}}{C_0^{(P)}}.$$

**Tabulated $O_L$ values** (Sec. 9, Gauss-Legendre quadrature $N_\mu=80$, $N_u=120$, $N_\phi=240$):

| $L$ | $O_L$ |
|---:|---:|
| 1 | 0.03776126 |
| 2 | 0.07890934 |
| 3 | 0.03597465 |
| 4 | 0.01846204 |
| 5 | 0.00968570 |
| 6 | 0.00538049 |

**Tabulated $s_L(67,0)$ values** (Sec. 12):

| $L$ | $s_L$ |
|---:|---:|
| 1 | 0.5663 |
| 2 | 0.8936 |
| 3 | 0.5569 |
| 4 | 0.3674 |
| 5 | 0.2356 |
| 6 | 0.1547 |

**Monte Carlo check** (Secs. 10–11): ensemble mean of $\widehat O_L$ over 20,000 random
isotropic arrays agrees with exact quadrature at $\le 0.2\%$ for $N_p \ge 10$.
The $1/48$ denominator is separately confirmed. Per-array scatter is large at small $N_p$
(especially $L=1$); the agreement is for ensemble means, not single realizations.

## Concepts touched

- `s_L_block_weights`
- `fisher_hierarchy`
- `transfer_function`
- `Cl_over_C0`
- `coherent_vs_incoherent`
- `shot_noise`

## Current paper citations

(None yet.)

## Potential additional uses

- **`numerical_estimates` section**: fill in the exact $s_L$ table and the $1/48$ origin
  of $\Sigma_{\rm bg}^2$; these are the numbers the section needs.
- **Fisher vs KL discussion**: cite as the source of the per-block SNR formula when
  explaining that ${\rm SNR}_L^2 \propto \Sigma_{\rm bg}^2 \cdot s_L \cdot C_L/C_0$.
- **Methods / benchmark section**: cite as authority for the uniform-array pair-average
  benchmark replacing any earlier $\xi(\gamma)^2$ shortcut.
- **Supplemental material**: the Monte Carlo validation tables and quadrature parameters
  could be cited to justify numerical reproducibility.

## Relations to other sources

- `wiki/conventions.md` already quotes the $s_L$ table and the $1/48$ formula as
  canonical (see Block weights section); this note is the primary source for those entries.
- The $D_{L\ge3}=0$ result is consistent with the transfer-function coefficients
  $\tau_L$ in `wiki/conventions.md` ($\tau_{L\ge3}=0$), confirming the diagonal
  contribution has the same angular support as the HD response.
- The per-$L$ SNR formula connects directly to the KL-divergence hierarchy discussed
  in `CLAUDE.md`: $D_{C_\ell} \propto \Sigma_{\rm bg}^2 \cdot s_L \cdot (C_L/C_0)$,
  and the $p^4$ scaling of the $C_\ell$-only strategy follows from $C_L/C_0 \propto p^2$.

## Caveats / open questions

- The note does not provide a closed analytic formula for $O_L$ at large $L$; the
  asymptotic decay is only numerical.
- The note explicitly disclaims the earlier $\xi(\gamma)^2$ shortcut formula but does
  not state where it appeared or why it is wrong; that provenance should be tracked.
- The Monte Carlo check tests only the pair-average formula, not the sky quadrature
  independently; the sky integral is validated only by internal quadrature convergence.
- No closed-form expression is derived for $g_L(\mu)$; it is treated as a purely
  numerical object. A future derivation in terms of Wigner $d$-matrices could
  provide a useful cross-check.
