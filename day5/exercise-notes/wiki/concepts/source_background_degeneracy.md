# Source–background degeneracy

How much does a bright source look like a slightly louder isotropic
background? The answer differs between coherent and incoherent
searches, and this distinction underlies the KL hierarchy.

## Coherent — zero degeneracy, exact

For all source parameters $\alpha \in \{|A|, \psi, \theta_s, \phi_s\}$:

$$F_{\alpha, B^2} = 0 \quad \text{exactly.}$$

Reason: the source lives in the mean, the background in the covariance.
In the Gaussian Fisher formula the cross-term vanishes whenever one
derivative acts on the mean and the other on the covariance. This is
structural and holds for any source direction, any number of pulsars,
any noise level.

Consequence: coherent source detection and background amplitude
measurement are independent problems.

## Incoherent, known direction

$$F_{q,B^2} = u^\dagger C_0^{-1}\Gamma^{\rm HD}C_0^{-1} u \ne 0.$$

Orthogonalize $\Gamma_{\rm src}=\alpha \Gamma_{\rm iso}+\Delta\Gamma_\perp$:
after floating the isotropic amplitude,
$$F^{\rm inc,marg}_{qq}=\langle\Delta\Gamma_\perp,\Delta\Gamma_\perp\rangle_{C_0}.$$

Normalized correlation in the noise-dominated limit:
$$|r| \sim 1/\sqrt{N_p} \approx 0.12\quad\text{for}\ N_p=67.$$

The smallness comes from the rank-1 source perturbation $uu^\dagger$
being nearly orthogonal to the rank-$N_p$ Hellings-Downs matrix in the
$N_p\times N_p$ matrix space. Bound: $|r|\le 1$ with equality iff
$uu^\dagger \propto \Gamma^{\rm HD}$ (never achieved).

## Incoherent, direction marginalized

Schur-complement correction from the direction block:
$$\Delta F^{\rm marg} = \begin{pmatrix} g_q \\ g_B \end{pmatrix} G^{-1} \begin{pmatrix} g_q^T & g_B^T \end{pmatrix}.$$

Numerical for $N_p=67$: $|r|$ shifts from $\sim 0.037$ (known direction)
to $\sim 0.24$ (marginalized). The ensemble identity
$\langle uu^\dagger\rangle_{\hat\Omega_s} \propto \Gamma^{\rm HD}$ does
**not** imply full degeneracy, because marginalization in Fisher space
is not the same as averaging the covariance perturbation.

## Apparent contradiction with the analytical estimate

The analytical $1/\sqrt{N_p}\approx 0.12$ and the numerical $0.037$
differ by a factor of 3. This is order-of-magnitude consistent but the
numerical value is smaller; the difference comes from partial
cancellation of the HD off-diagonal structure not captured by the naive
counting. See `appendix_fisher.tex` and
[[../sources/fisher_src_vs_bg_degeneracy]].

## Source pages

- [[../sources/fisher_src_vs_bg_degeneracy]] — canonical, three tiers of model complexity.
- [[../sources/pn_coh_vs_incoh_fisher]] — orthogonalization construction, Schur complement.
- [[../sources/pn_coh_vs_quadratic]] — general floating-amplitude argument.
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — CURN-null analog: $\partial C/\partial A$ (block-diagonal) vs $\partial C/\partial \eta$ (purely block-off-diagonal) gives $F_{A\eta}=0$, the same structural orthogonality.
- [[../sources/pta_curn_hd_cross_only]] — exact $F_{PB}=0$ in the $(P, B)$ parametrization $C = N + PI + BX$ ($X_{ii}=0$, $D$ diagonal). Makes the cross-only quadratic estimator the nuisance-projected HD Fisher score; adds a physical-boundary analysis ($P \ge B$) that reintroduces diagonal information when $\sigma_P \lesssim \sigma_B$.
- [[../sources/pta_source_detection_likelihood]] — the fair-anisotropy convention tests about the monopole-floated $C_Q=N+Q\Gamma_0$ (not $C_B$), with each anisotropic response orthogonalized to the isotropic direction, $\Gamma_{\alpha,\perp}=\Gamma_\alpha-(\langle\Gamma_\alpha,\Gamma_0\rangle/\langle\Gamma_0,\Gamma_0\rangle)\Gamma_0$.
- [[../sources/toy_model_source_vs_power_map]] — evidence-language form: for a true one-source sky the AVERAGED $C_\ell$ Bayes factor equals a single covariance source $b_{\rm cov}(s;V_1)$, $V_1=\sum_k C_k$ — a single source and a smooth power model are confusable in covariance but are distinct hypotheses.

## Paper uses

- `three_strategies.tex:194-195` — cites in the hierarchy discussion.
- `appendix_fisher.tex` — numerical verification for $N_p=67$.

## Related concepts

[[coherent_vs_incoherent]], [[fisher_hierarchy]],
[[KL_divergence]].
