# Block weights $s_L$

The per-multipole response weights that enter the signal-to-noise
formula for covariance-based anisotropy searches. Tabulated numerical
values plus the exact derivation.

## Definition

$$s_L(N_p,\beta) \equiv \frac{2L+1}{4\pi}\,r_L(N_p,\beta),\qquad
\beta = A/\sigma_n^2,$$
with
$$r_L = \bar F_L / \langle F_A\rangle.$$

$\bar F_L$ is the block-averaged anisotropy Fisher; $\langle F_A\rangle$
is the isotropic-amplitude Fisher. The role of $s_L$ is captured by:

$$\mathrm{SNR}_L^2 = \Sigma_{\rm bg}^2 \, s_L(N_p,\beta)\,
\frac{C_L^{(P)}}{C_0^{(P)}}.$$

## Finite-$N_p$ formula (noise-dominated benchmark, $\beta\to 0$)

$$s_L(N_p,0) = \frac{2L+1}{4\pi}\,\frac{D_L + (N_p-1)O_L}{1+(N_p-1)/48}.$$

Exact components:

- **Diagonal:** $D_1=\pi,\;D_2=\pi/25,\;D_{L\ge 3}=0$. Closed form.
- **Off-diagonal:** $O_L = \tfrac12\int_{-1}^1 g_L(\mu)\,d\mu$, where $g_L(\mu)$ is the pair-frame multipole power. Numerically computed.
- **Denominator:** $1/48 = \tfrac12\int_{-1}^1 \chi(\mu)^2\,d\mu$, closed form from the HD curve.

$\Sigma_{\rm bg}^2$ formula: see [[../conventions|conventions]].

## Numerical values

Exact quadrature values (Monte Carlo-validated at percent level across
$N_p \in \{10,20,50,100\}$):

| $L$ | $O_L$ |
|---:|---:|
| 1 | 0.03776 |
| 2 | 0.07891 |
| 3 | 0.03597 |
| 4 | 0.01846 |
| 5 | 0.00969 |
| 6 | 0.00538 |

For $N_p = 67$:

| $L$ | $s_L$ |
|---:|---:|
| 1 | 0.5663 |
| 2 | 0.8936 |
| 3 | 0.5569 |
| 4 | 0.3674 |
| 5 | 0.2356 |
| 6 | 0.1547 |

**Non-obvious fact:** $s_2 > s_1$ at this $N_p$. The quadrupole is
pair-dominated almost immediately (crossover at $N_p\sim 2.6$), while
the dipole is still strongly helped by the diagonal contribution
(crossover at $N_p\sim 84$).

## Asymptotic (observed, not proved)

$O_L \propto L^{-3}$ and $s_L \propto L^{-2}$ for $L\gtrsim 3$ and
large $N_p$.

## Role in the hierarchy

- Full incoherent Fisher: $F_{pp}^{\rm full}=\Sigma_{\rm bg}^2\sum_L s_L$.
- $C_L$-only Fisher: $F_{pp}^{(C_L)} = 2p^2\Sigma_{\rm bg}^4\sum_L s_L^2/(2L+1)$.
- Dipole fraction captured: $s_1/\sum_L s_L \approx 0.43$ at $N_p=67$ up to $L=6$.

## Source pages

- [[../sources/pta_exact_pair_average]] — canonical derivation, numerical values, Monte Carlo validation.
- [[../sources/pta_noise_dominated_limit]] — companion note with Fisher normalizations.
- [[../sources/pta_1src_vs_cls_toy]] — block-weight formalism toy model.
- [[../sources/pta_1src_vs_CL]], [[../sources/pn_coh_vs_incoh_fisher]] — usage in the $C_L$-only Fisher.

## Paper uses

- `three_strategies.tex` — $F_{pp}^{\rm full}$ and $F_{pp}^{(C_L)}$ formulas.
- `numerical_estimates.tex` — **TODO**: explicit $s_L$ table.

## Related concepts

[[fisher_hierarchy]], [[Cl_over_C0]], [[transfer_function]].
