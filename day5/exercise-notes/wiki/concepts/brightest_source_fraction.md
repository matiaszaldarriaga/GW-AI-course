# Brightest-source fraction $p$

The single most important summary statistic in the project. Throughout:

$$p \equiv p_1 = \frac{q_{\max}}{\sum_a q_a}.$$

Per [[../conventions|conventions]], $p$ always means $p_1$. Do not
re-use the symbol for anything else.

## Regimes

- **One-source dominated** ($p_1\to 1$): $C_1/C_0 \to 1$. Dipole distribution is a spike at $p_1^2$.
- **Two-source** ($p_1, p_2$ comparable): dipole distribution is uniform on $[(p_1-p_2)^2,(p_1+p_2)^2]$.
- **Many-source** ($p_1 \ll 1$, broad weight distribution): $C_1/C_0$ small, concentrated near the conditional mean.

## Summary triple $(p_1, p_2, \eta)$

The full distribution of $C_1/C_0$ per realization is nearly determined
by just three numbers:

- $p_1$ = brightest source fraction
- $p_2$ = second-brightest source fraction
- $\eta \equiv \sum_{a\ge 2} p_a^2$ (Gaussian-background variance proxy)

See [[dipole_distribution]] for the four semi-analytic approximations
built on these.

## Inverse: what a measured dipole implies (approximately model-independent)

Conditioning on a measured dipole $C_1/C_0 = x$ pins the brightest-source
fraction through a simple, model-independent estimate (`eq:p1_given_x_simple`):

$$\langle p_1 \mid x\rangle \simeq \sqrt{x}\quad(\text{slight overestimate}),
  \qquad \langle N_{\rm eff}\mid x\rangle \simeq 1/x.$$

Binning $10^4$ realizations of each $\varepsilon$ model by their measured
$x$, the conditional means approximately collapse onto the same curve over the
tested family — the source content implied by a dipole is primarily set by the dipole
rather than by the underlying model
([[../figures/source_content_estimators]]). The reason: the one-source +
Gaussian forward law forces $p_1^2 \gtrsim x$ for a large dipole, nearly
independent of the population prior $\pi(p_1)$; the model only controls *how
often* a large dipole occurs (the exceedance probability), not what it means.
The exact Bayesian inverse (`eq:p1_given_x`) reweights the Monte-Carlo
$(p_1,\eta)$ sample by the survival function of the forward law.
Numerically, over $0.05\le x<0.9$ the rerun gives
$E[p_1\mid x]/\sqrt{x}=0.81$--$0.98$; the cross-model mean-$p_1$ spread is at
most 0.028 in a common bin.

## $p_1$ (relative) vs $R$ (absolute reference)

$p_1$ is *relative*: its denominator $h^2_{\rm tot}$ fluctuates realization to
realization, so a given $p_1$ is not a fixed source brightness. The
complementary **fixed-reference** ratio (`eq:R_ratio`) divides by the model's
(fixed) mean background instead:

$$R \equiv \frac{h^2_{s,\max}}{\langle h_c^2\rangle(f)}.$$

$R$ is directly comparable to what NANOGrav's individual-source (continuous-wave)
search constrains: the brightest source's strain amplitude
$h_0 = \sqrt{h^2_{s,\max}/(f\,T_{\rm obs})}$ against the background
$A=\sqrt{\langle h_c^2\rangle}$. The median brightest source carries only a small
fraction of the background ($R\lesssim 0.13$), but the heavy tail means the
loudest realizations rival it ($R\to 1$). In strain, only the
$\varepsilon=0.66$ model reaches the NANOGrav CW limit $h_0\approx10^{-14}$
(95th percentile $\approx1.2\times10^{-14}$ at the lowest frequency); the
lower-scatter 95th percentiles remain below the deepest best point
([[../figures/pixel_amplitude_h0]]). Table II (`tab:source_ratio`) tabulates
$R$ and $h_0$.

## $p$ is not a regular local coordinate for the coherent problem

The coherent source enters the data mean as $\mu_{\rm src} \propto
\sqrt{q} = \sqrt{A_{\rm GW} p}$. So $\partial_p \mu \propto 1/\sqrt{p}$
is singular at $p=0$. The Fisher on $p$ is not finite at $p=0$, but the
KL divergence $D_{\rm coh} \propto p$ is perfectly regular. This is why
the coherent hierarchy is written in terms of KL, not Fisher, scaling.
See [[KL_divergence]] and [[fisher_hierarchy]].

## Source pages

- [[../sources/pn_C1_over_C0]] — Sec. 8-11: regimes and approximations.
- [[../sources/pn_coh_vs_incoh_fisher]] — $q = A_{\rm GW} p$ parametrization; p is not a regular coord at 0.
- [[../sources/pta_1src_vs_CL]] — $C_L^P/C_0^P = p^2$ for one bright source.
- [[../sources/fisher_src_vs_bg_degeneracy]] — source-power parameter.
- [[../sources/pn_coh_vs_quadratic]] — $p_\star \equiv q_\star/Q$; $D_{\rm mean}\propto p_\star$, $D_{\rm cov}\propto p_\star^2$.
- [[../sources/pn_1src_vs_dipole_cov]] — $C_1^{(b)}/C_0^{(b)}=p^2/4$.
- [[../sources/pta_1src_vs_cls_toy]] — one-source amplitude parameter.
- [[../sources/joint_search_resolved_unresolved]] — Goncharov et al. 2026: the CW is the dimensional brightest source $h_{\rm cw}=\max_s h_{\rm s}$, with population PDF $p(h_{\rm cw}) = h_{\rm s,peak}^2 (dN/dh_{\rm s}^2)\exp(-\int_x^\infty dN/dx\,dx)$. NB: $h_{\rm cw}$ is the dimensional brightest strain, NOT the dimensionless fraction $p=p_1$ — do not conflate.
- [[../sources/toy_model_source_vs_power_map]] — toy stand-in: a one-source-in-pixel-1 sky with $s=z_1^2$ large and the rest null-like models a single dominant source carrying fraction $p$ of the power.

## Paper uses

- Abstract and introduction — the headline parameter.
- `distribution_c1c0.tex` — four approximations parametrized by $(p_1, p_2, \eta)$.
- `astrophysical_model.tex:60` — computed per realization from the population model.
- `three_strategies.tex` — KL hierarchy in $p$.

## Code and notebooks

- [[../code/gwb_sources_sources]] — `find_brightest_source_strain`, `brightest_n_sources`, top-$N$ ledger.
- [[../notebooks/guide_dipole_analytics]] — verifies $p_1$ alone captures most of the $C_1/C_0$ distribution.
- [[../notebooks/guide_power_anisotropy]] — §10e: joint density of $(p_1, C_1/C_0)$ and the **conditional** $P(p_1\mid C_1/C_0)$. Empirically, a large dipole requires a dominant source: $p_1$ concentrates just below $\sqrt{C_1/C_0}$, with median $p_1\!\approx\!0.4$ at the NANOGrav "limit" $C_1/C_0=0.2$ and $P(p_1>0.5)\!\approx\!0.9$ at $C_1/C_0=0.5$ (the conditional view Fig. 5 omits).
- [[../notebooks/guide_interactive]] — interactive sliders for $p_1$, $p_2$, $\eta$.
- [[../notebooks/guide_model_comparison]] — per-$\varepsilon$ median $p_1$
  (the historical 0.020/0.052/0.155 triple was at the old fiducial
  $\phi_\sigma$; the corrected matched-normalization medians at the lowest
  frequency are 0.0185/0.0523/0.1826 for
  $\varepsilon=0.20/0.38/0.66$).

## Related concepts

[[Cl_over_C0]], [[N_eff]], [[dipole_distribution]],
[[fisher_hierarchy]], [[SMBH_population_model]],
[[../figures/source_content_estimators]], [[../figures/pixel_amplitude_h0]].
