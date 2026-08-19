# Transfer function source-power sky → pulsar-power map

The exact Legendre kernel that relates the source-power sky
$P(\hat\Omega)$ (what NANOGrav analyzes) to the incoherent
pulsar-power map $b(\hat p)$. Closed-form and terminates at $L=2$.

## Statement

The response kernel is
$$T(x) = \left(\frac{1+x}{4}\right)^2
= \frac{1}{12} + \frac{1}{8}P_1(x) + \frac{1}{24}P_2(x),$$
with $x = \hat p\cdot\hat\Omega$.

In harmonic space:
$$b_{LM} = \tau_L\,p_{LM},$$
with
$$\tau_0 = \tfrac{\pi}{3},\quad \tau_1 = \tfrac{\pi}{6},\quad
\tau_2 = \tfrac{\pi}{30},\quad \tau_{L\ge 3} = 0.$$

## Consequences for power spectra

$$\frac{C_L^{(b)}}{C_0^{(b)}} = \left(\frac{\tau_L}{\tau_0}\right)^{\!2}
\frac{C_L^{(P)}}{C_0^{(P)}},$$

which for a single bright source plus isotropic remainder gives:

$$\frac{C_1^{(b)}}{C_0^{(b)}} = \frac{p^2}{4}, \qquad
\frac{C_2^{(b)}}{C_0^{(b)}} = \frac{p^2}{100}, \qquad
\frac{C_{L\ge 3}^{(b)}}{C_0^{(b)}} = 0.$$

## One-source = dipole after compression

At the $\ell=1$ level, the source-power sky for one bright source plus
isotropic background projects to
$P^{(\ell=1)}(\hat\Omega) = \tfrac{1}{4\pi}[1 + 3p\,\hat n\cdot\hat\Omega]$
— a dipole sky. So **once restricted to $\ell=1$, a one-source model
and a dipole model are the same object**. After profiling over an
unknown source direction, the statistic becomes
$T_{\max}=|\mathbf x|^2$ — dipole power.

## Role in the argument

This transfer function is why:
- The dipole intuition works for the **pulsar-power map** $b(\hat p)$.
- The full source-power sky spectrum $C_\ell^{(P)}$ has structure at all $\ell$.
- Compressing the full covariance to the $|z|^2$ diagonal loses no info above $\ell=2$.
- Compressing the full covariance to the $C_L$ blocks is lossy for every $L$ (different issue — see [[fisher_hierarchy]]).

## Source pages

- [[../sources/pn_1src_vs_dipole_cov]] — canonical derivation with all exact $\tau_L$ values.
- [[../sources/pn_coh_vs_quadratic]] — Sec. 9 derives the same result in incoherent-dipole language.
- [[../sources/pta_exact_pair_average]], [[../sources/pta_1src_vs_cls_toy]] — diagonal terms $D_L$ come from $K^{\rm tot}_{aa}$ Legendre expansion, same structure.

## Paper uses

- Not explicitly named in the current paper text. Could strengthen
  the narrative around why $C_\ell$-based approaches look intuitive.
  **TODO:** consider adding in `nanograv_prior.tex` or
  `discussion.tex`.

## Related concepts

[[Cl_over_C0]], [[coherent_vs_incoherent]],
[[s_L_block_weights]], [[sqrt_SH_basis]].
