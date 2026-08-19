# $C_\ell/C_0$

The central observable of the paper: the ratio of multipole power to
monopole power for the source-power sky. By default in this wiki,
$C_\ell \equiv C_\ell^{(P)}$ (see [[../conventions|conventions]]).

## Canonical statement

For a discrete source distribution $M(\hat n) = \sum_a q_a\,
\delta^{(2)}(\hat n,\hat n_a)$, using the addition theorem:

$$C_\ell = \frac{1}{4\pi}\sum_{a,b} q_a q_b\,P_\ell(\hat n_a\cdot\hat n_b),
\qquad C_0 = \frac{Q^2}{4\pi},\; Q=\sum_a q_a.$$

Dividing out $C_0$ removes the absolute amplitude:

$$\frac{C_\ell}{C_0} = \sum_{a,b} p_a p_b\,P_\ell(\hat n_a\cdot\hat n_b),
\qquad p_a=q_a/Q,\;\sum_a p_a=1.$$

**The ratio depends only on the normalized source fractions $\{p_a\}$
and their sky positions.** Absolute amplitudes drop out.

## Mean and variance (isotropic positions, fixed weights)

For every $\ell \ge 1$:

$$\mathbb{E}\!\left[\frac{C_\ell}{C_0}\,\bigg|\,\{p_a\}\right]
= \sum_a p_a^2 = \frac{1}{[[N_eff]]}.$$

This is $\ell$-independent.

$$\mathrm{Var}\!\left[\frac{C_1}{C_0}\,\bigg|\,\{p_a\}\right]
= \frac{2}{3}\!\left[\left(\sum p_a^2\right)^2 - \sum p_a^4\right].$$

## Dipole specialization

$P_1(\mu)=\mu$, so $C_1/C_0 = |\mathbf S|^2$ with the weighted 3D random
walk $\mathbf S = \sum_a p_a \hat n_a$. This is the starting point of
all distribution analyses (see [[dipole_distribution]]).

Schema-v2 products evaluate this directly as
$|\mathbf D|^2/Q^2$, $\mathbf D=\sum_s w_s\hat n_s$, including unresolved
random-walk covariance $S_{2,\rm bulk}/3$ per Cartesian component. HEALPix
maps are used only for $\ell\ge2$ and visualization. Because those maps store
power integrated per pixel, their absolute low-moment normalization is
$C_0=4\pi Q^2/N_{\rm pix}^2$ and
$C_1=4\pi|\mathbf D|^2/N_{\rm pix}^2$; the ratio remains the canonical one.

Characteristic function:
$\chi_{\mathbf S}(k) = \prod_a \mathrm{sinc}(p_a k) = \prod_a \sin(p_a k)/(p_a k)$.

## Relation to the pulsar-map $C_\ell^{(b)}$

Do not conflate $C_\ell^{(P)}$ with the incoherent pulsar-power map
$C_\ell^{(b)}$. They are linked by an exact transfer function
(see [[transfer_function]]): $C_1^{(b)}/C_0^{(b)} = (1/4)\,
C_1^{(P)}/C_0^{(P)}$ and $C_2^{(b)}/C_0^{(b)} = (1/100)\,
C_2^{(P)}/C_0^{(P)}$; higher multipoles vanish in the $b$-map.

## Relation to Lin et al. (2026) shot noise

The fractional-fluctuation power spectrum of the pulsar-map satisfies
$\mathbb E[C_\ell^{(\delta M)}]=4\pi/[[N_eff]]$ — the shot-noise floor
quoted in Lin, Lidz & Ma. This is $4\pi$ times the source-sky ratio.
See [[shot_noise]].

## Source pages

- [[../sources/pn_C1_over_C0]] — canonical derivation (exact formula, random walk, mean, variance, pdf approximations).
- [[../sources/pn_coh_vs_incoh_fisher]] — uses $C_\ell/C_0$ as a probe in the incoherent search.
- [[../sources/pta_1src_vs_CL]] — $C_L$-only compression, Fisher penalty.
- [[../sources/pn_coh_vs_quadratic]] — Sec. 9 derives the pulsar-map dipole formula.
- [[../sources/pn_1src_vs_dipole_cov]] — $C_\ell^{(P)}$ vs $C_\ell^{(b)}$ transfer function.
- [[../sources/pta_exact_pair_average]] — $C_\ell^{(P)}$ is the signal in the SNR formula $\mathrm{SNR}_L^2 = \Sigma_{\rm bg}^2 s_L C_L^{(P)}/C_0^{(P)}$.
- [[../sources/pta_1src_vs_cls_toy]] — diagonal-vs-full-covariance contrast.
- [[../sources/draft_sufficient_statistics_2026]] — Eq. 23 gives $C_1/C_0 = 1/4$ and $C_2/C_0 = 1/100$ for a single source on the pulsar-term variance sky (confirms our convention); Eq. 16 is the stochastic HD $C_\ell$.
- [[../sources/pta_source_detection_likelihood]] — Sec 5 derives the response-free source-power-sky identity $C_L^P/C_0^P=(q/(B+q))^2=p^2$ ($L>0$), plus the conversion $h_*^2=B\sqrt{R_*}/(1-\sqrt{R_*})$ from a measured ratio $R_*=C_L^P/C_0^P$.

## Paper uses

- `angular_power_spectrum.tex` — exact formulas, mean, variance, random walk (`eq:cl_exact`, `eq:cl_c0_exact`, `eq:mean_cl`, `eq:dipole`).
- `distribution_c1c0.tex` — distribution of $C_1/C_0$ across realizations.
- `nanograv_prior.tex` — target of the NANOGrav 15yr anisotropy analysis.
- `three_strategies.tex` — compared to the coherent-search channel.

## Related concepts

[[N_eff]], [[brightest_source_fraction]], [[dipole_distribution]],
[[transfer_function]], [[shot_noise]], [[fisher_hierarchy]].

## Notebooks

- [[../notebooks/guide_power_anisotropy]] — full Monte Carlo walkthrough: power maps, $C_\ell/C_0$ spectra, exclusion of top-$N$ sources, $N_{\rm eff}$ scatter.
- [[../notebooks/guide_sqrtSH_model]] — $C_\ell/C_0$ statistics from the NANOGrav sqrt-SH prior; amplitude-cancellation property; $\ell_{\max}^b$ non-convergence.

## Code and figures

- [[../code/gwb_sources_power_anisotropy]] — `compute_power_cls` canonical implementation.
- [[../figures/c1c0_neff_vs_freq]], [[../figures/c1c0_distribution]] — main paper figures.
