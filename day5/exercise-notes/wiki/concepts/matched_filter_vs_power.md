# Matched filter vs total power

General information-theoretic result underlying the coherent > incoherent
hierarchy: a statistic linear in the data always dominates a quadratic
statistic at low SNR, and the look-elsewhere penalty for scanning many
templates is only logarithmic in the number of trials.

## Setup (toy model)

$N$ Gaussian data points $x_i = n_i + s_i$, with signal nonzero in
$M \ll N$ of them at amplitude $A$. Direction-like parameter selects
which $M$; $K$ possible templates (or $K_{\rm eff}$ for continuous
parameter).

**Matched filter** at template $k$: $t_k = (1/\sqrt M)\sum_{i\in S_k} x_i$.
- Under noise: $t_k \sim \mathcal N(0,1)$.
- Under signal: $t_k \sim \mathcal N(A\sqrt M,\,1)$.
- $\mathrm{SNR} = A\sqrt M$. **Linear in $A$.**

**Total power**: $P = \sum_i x_i^2$.
- $\mathbb E[P] = N + MA^2$ under signal.
- $\mathrm{Var}(P) \approx 2N$ at weak signal.
- $\mathrm{SNR} = MA^2/\sqrt{2N}$. **Quadratic in $A$.**

## Thresholds

$$A_{\min}^{\rm matched} = \frac{\sqrt{2\ln K} + q}{\sqrt M},\qquad
A_{\min}^{\rm power} = \sqrt{q\sqrt{2N}/M}.$$

Matched filter wins when $\ln K \lesssim \sqrt N$ — essentially always
for PTA-scale arrays.

## Continuous parameter (sky direction)

For a smooth template field on a manifold:

$$K_{\rm eff}^{\rm sphere} \sim 4\pi/\theta_c^2 \sim \sqrt{\det g},$$

where $g_{\mu\nu}$ is the template metric (Fisher metric, second
derivatives of the template autocorrelation). The effective number of
trials is the number of resolution elements. Not a parameter you
choose; set by the physics.

## Relation to the PTA hierarchy

Exactly the mechanism behind [[fisher_hierarchy]]:
- Coherent source = matched filter → $D\propto p$ (linear in source power $q=A^2$, hence linear in $p$).
- **Source-subspace projector** covariance = monotone-equivalent to the matched filter (profiled LR $g_r(T_{\rm coh})$ strictly increasing) → still $D\propto p$, same threshold. *Not* a total-power variant.
- **Power-map / total-power** covariance ($T_{\rm psrc}$, or the full-harmonic $T_{\rm map}$) → $D\propto p^2$; further compression to $C_\ell$ block powers → $D\propto p^4$. See the four-tier table in [[fisher_hierarchy]].

Coherent cannot be beaten by trials penalties in any realistic PTA
setting.

## PTA numbers: alpha_ps = sqrt(5) and the modest C_l detection penalty (2026-06-23)

The rewritten [[../paper/sec_source_detection|Sec. VI]] makes this concrete for
the source-vs-$C_\ell$ comparison (canonical:
[[../sources/pta_point_source_multipole]]; code
[[../code/gwb_sources_source_detection]]):

- **Matched filter for the source:** $\rho_{\rm ps}=\alpha_{\rm ps}p_1\rho_0$,
  $\alpha_{\rm ps}=\sqrt5\simeq2.24$ (large equal-noise array; RMS of the
  monopole-removed source pair pattern over the HD pattern). Truncate at $L$:
  $\alpha_1\simeq0.65$, $\alpha_{\le2}\simeq1.4$.
- **Trials factor.** The unknown-direction scan searches $K_{\rm eff}\approx
  K_L=L(L+2)$ resolution elements — the spherical instance of
  $K_{\rm eff}\sim4\pi/\theta_c^2$ above — so $\rho_{\rm scan,req}\simeq
  \Phi^{-1}(1-p_{\rm fa}/K_L)$.
- **Linear (scan) vs quadratic ($C_\ell$).** The Poisson $C_\ell$ statistic
  $\lVert x\rVert^2$ is the total-power analog; required-amplitude penalty
  $\rho_{C_\ell}/\rho_{\rm scan}=1.1$–$1.4$ over $L=1$–$6$, **$1$ at $L=1$**
  (dipole scan max $=\sqrt{C_1}$). The logarithmic-in-$K$ trials cost of the scan
  (this page's main result) is exactly why the penalty stays modest at low
  resolution.

## Source pages

- [[../sources/matched_filter_vs_power]] — canonical, including Rice's upcrossing formula and template-metric derivation.
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — CURN-vs-HD instance: once the mean/amplitude channel (common autos) is closed, HD information is purely quadratic in the cross-covariance; explicit two-pulsar toy gives $D_{\rm KL}\simeq r^2/2$ for small $r$.
- [[../sources/pta_curn_hd_cross_only]] — derives the canonical pairwise cross-correlation pseudo-likelihood (the "optimal statistic" power-type object) from a local Fisher expansion; gives the precise sense in which it is "cross-only" (nuisance-projected HD Fisher) and when that interpretation is undermined (physical boundary $P \ge B$ with $\sigma_P \lesssim \sigma_B$).
- [[../sources/pn_coh_vs_incoh_fisher]], [[../sources/pn_coh_vs_quadratic]] — apply the logic to the PTA problem.
- [[../sources/fisher_src_vs_bg_degeneracy]] — block-diagonal coherent Fisher is the "zero look-elsewhere cost" analog.
- [[../sources/draft_sufficient_statistics_2026]] — App. B of this draft takes a single-source template and, via angle + amplitude marginalization with a Gaussian prior, turns it into a rank-1 covariance addition. In the toy limit of isotropic $U^\dagger N^{-1} U$ the resulting Neyman-Pearson statistic $T(\hat n)$ coincides with the coherent profile-likelihood matched filter, and the two constructions are in fact **monotone-equivalent** (same p-value on every realization) — so stochasticization is free at the detection stage in that limit. The linear-beats-quadratic distinction of this concept page then materializes only when (a) the truth is stochastic (physics of data generation, not modeling), (b) response anisotropy breaks the equivalence, (c) one asks about parameter precision rather than detection, or (d) the null is pinned to the matched-power GWB. The $\sim 3.8\sigma$ ceiling $p[\chi^2_4 > 24] = 7.99\times 10^{-5}$ is specifically case (d) — see [[../notes/app_B_coherent_fisher_critique]] for the full treatment.
- [[../sources/pta_source_detection_likelihood]] — multi-dof realization: projector covariance gives $g_r(T)=T-r-r\log(T/r)$ (rank-one $s-1-\log s$), monotone in $T_{\rm coh}$, so the power test that pays the quadratic price is the one-source power-map $T_{\rm psrc}=(v^Ts)^2/(v^TFv)$ ($\lambda_{\rm psrc}=p^2 v^TFv$), not the source-subspace excess-variance search.
- [[../sources/toy_model_source_vs_power_map]] — Gaussian toy: the $C_\ell$/power-spectrum search responds to squared-data excess $s_\alpha-1$ weighted by squared basis functions (Sec 18), not the signed coherent amplitude — the cleanest linear-beats-quadratic statement in evidence language.

## Paper uses

- Not currently cited explicitly. Could strengthen introduction or
  discussion with the "linear dominates quadratic at weak signal"
  argument.

## References to verify if adding

The `matched_filter_vs_total_power.md` note cites Rice 1944, Adler 1981,
Gross & Vitells 2010, Owen 1996. None are in `references.bib`. Run
`verify-reference` before adding any.

## Related concepts

[[fisher_hierarchy]], [[KL_divergence]], [[coherent_vs_incoherent]].
