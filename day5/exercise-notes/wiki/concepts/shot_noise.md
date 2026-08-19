# Shot noise

The mean level of anisotropy produced by a finite discrete source
population with isotropic random positions. The floor that all
isotropic-average analyses compare against.

## Lin, Lidz, Ma (2026) formula

For the fractional-fluctuation field $\delta h^2(\hat n)/\langle h^2\rangle$:
$$\mathbb E[C_\ell^{(\delta M)}] = \frac{4\pi}{N_{\rm eff}},\qquad \ell\ge 1.$$

Flat in $\ell$. Independent of absolute source amplitude. The formula
is derived in [[../sources/arxiv_2602_16808]] Eq. 9.

**$N_{\rm eff}$ definition subtlety — resolved 2026-08-11.** In 2602.16808
Lin, Lidz, Ma used the continuum ensemble average
$N_{\rm eff}^{\rm LLM} = \langle h^2\rangle^2/\langle h^4\rangle$
(their Eq. 18 mass-weighted form), which differs from the project's
realized discrete quantity $N_{\rm eff} = 1/\sum_a p_a^2$ (see [[N_eff]]) —
equivalent in the many-source limit, not for a single draw, and the
distinction matters precisely for the tail the project argues dominates.
Their follow-up [[../sources/arxiv_2608_09929]] adopts the realized
definition: their per-realization $\hat C_{\rm shot}/(4\pi) = \sum_i N_i w_i^2$
with $w_i = h_i^2/\sum_j N_j h_j^2$ is **algebraically identical** to
$\sum_a p_a^2$, and they too read it as $1/N_{\rm eff}$. The two groups now
use the same object.

## Source-sky version used in this project

$$\mathbb E[C_\ell/C_0 \mid \{p_a\}] = \sum_a p_a^2 = 1/N_{\rm eff}.$$

Related to the Lin/Lidz/Ma formula by a factor of $4\pi$
(see [[Cl_over_C0]] for the exact normalization).

## Bounds on the realized statistic

$\sum_a p_a^2$ is an inverse participation ratio, hence
$$\frac{1}{N} \le \sum_a p_a^2 \le 1,$$
upper equality iff one source carries all the power, lower equality iff all
sources are equally bright. Derived independently in
[[../sources/arxiv_2608_09929]] §II B (their Eqs. 12–15). The upper bound is
what makes the realized shot noise flatten in frequency relative to the
unbounded moment estimate.

## Frequency scaling

Lin, Lidz, Ma Eq. 12 (GW-driven inspiral): $C_{\ell>0,h^2}^{\rm SN}
\propto f^{8/3}$. Eq. 19 generalizes to $\propto f^\beta$ for arbitrary
residence-time distribution.

**Superseded for the realized statistic (2026-08-11).** The $f^{8/3}$ law is
the scaling of the *moment estimate*. In their own Monte Carlos
([[../sources/arxiv_2608_09929]] §III A) the mean and median of the realized
$\hat C_{\rm shot}$ scale as $f^{1.1-1.2}$, because of the $\le1$ ceiling. Our
sampled Monte Carlos give a median log-log slope of 1.82, 1.17 and 0.53 for
$\varepsilon = 0.20$, $0.38$, $0.66$ between $f = 0.085$ and $1.03\,{\rm yr}^{-1}$:
the slope falls as the population gets more source-dominated, and $\varepsilon
= 0.38$ reproduces their quoted range.

Sato-Polito + Kamionkowski ([[../sources/arxiv_2305_05690]]) give the
equivalent spectrum dependence $C_\ell/C_0\propto 1/[1+(f/f_\ast)^{-11/3}]$
in the source-sky convention. Both are different parameterizations of
the same shot-noise result.

## Large-scale-structure vs shot noise

Lin, Lidz, Ma also compute the LSS contribution to $C_{\ell,h^2}$ via
Limber projection (their Eqs. 24-26). It is **2-3 orders of magnitude
below** the shot-noise floor. This is consistent with what
`discussion.tex:74-76` states in the "what $C_\ell$ searches can still
do" section.

## What this project adds beyond the mean

_(Rewritten 2026-08-11: LLM26b now also gives a PDF, so the boundary moved.)_

**2602.16808 gave only the mean.** Against *that* paper, the project's
addition was the full **probability distribution** of $C_1/C_0$ around the
mean — via [[dipole_distribution]] and the characteristic-function approach of
[[../sources/arxiv_2406_17010]] (SPZ 2025dist). For broad weight distributions
(low $N_{\rm eff}$) it is highly skewed:

- Median much smaller than mean for heavy-tailed populations.
- Long tail driven by individual bright sources.
- Large $C_1/C_0$ happens **if and only if** one source dominates.

**2608.09929 closed that gap from their side**, independently and in
quantitative agreement (95% width 1.7 dex vs our 1.4–2.3 dex; mean/median
$\sim2$ at $30$ nHz vs our 1.5–2.1). What the project still adds beyond
LLM26b:

1. **The angular realization.** Their $\hat C_{\rm shot}$ is
   $\mathbb E[C_\ell/C_0 \mid \{p_a\}]$ — a moment ratio, computed without ever
   placing a source on the sky. The realized $C_1/C_0$ carries an extra
   1.15–1.41 dex of 95% scatter about it (0.22–0.28 dex once averaged over
   $\ell\le6$). Verified in our sampled Monte Carlos, 2026-08-11.
2. **Per-PTA-bin rather than per $d\ln f$ statistics** (they list this as
   future work).
3. **The detection-theory ranking** — $C_\ell$ vs coherent source search — which
   is absent from both LLM papers.
4. **The prior content of the NANOGrav $C_\ell$ bound** that both LLM papers
   compare against; see [[prior_sensitivity]].

## Source pages

- [[../sources/arxiv_2602_16808]] (Lin, Lidz, Ma 2026) — canonical $4\pi/N_{\rm eff}$ derivation, LSS contribution, comparison with NANOGrav bounds.
- [[../sources/arxiv_2608_09929]] (Lin, Lidz, Ma 2026b) — the realization PDF of the same statistic; the $\le1$ bound; the $f^{1.1-1.2}$ realized scaling; conditioning on $\hat h_c^2$; stellar-hardening variant. **Retracts the quantitative predictions of 2602.16808 in the low-source regime.**
- [[../sources/arxiv_2406_17010]] (SPZ 2025dist) — gives the full pdf beyond the mean.
- [[../sources/pn_C1_over_C0]] — Sec. 19 reconciles with Lin et al. in the continuum limit.
- [[../sources/pn_coh_vs_quadratic]] — many-source covariance rate $\langle D_{\rm cov}\rangle\propto Q^2\sum p_s^2$.
- [[../sources/pn_1src_vs_dipole_cov]] — pulsar-map shot-noise $(1/4)\sum p_s^2$ at $L=1$.
- All covariance-Fisher source pages reference this as the "background" against which [[source_background_degeneracy]] is analyzed.

## Spectral variance convergence

The second moment of $h_c^2$ ($\text{Var} = \sum \bar N_k h_{s,k}^4$)
does not converge in MC for heavy-tailed populations: at
$\varepsilon = 0.66$, 99.86% of the theoretical variance comes from bins
with $\bar N < 10^{-7}$, beyond the SPZ grid. Robust statistics (median,
percentiles) converge fine. See [[../sources/spectral_variance_convergence]].

## Paper uses

- `introduction.tex:22` — cites Lin, Lidz, Ma as the "expected shot-noise" benchmark the paper's analysis qualifies.
- `discussion.tex:43` — engages specifically with their detection claim.
- Implicit throughout — shot-noise is the baseline the KL hierarchy is measured against.

## Code and notebooks

- [[../code/gwb_sources_power_anisotropy]] — `compute_power_cls` produces the $C_\ell$ realizations that are compared to the shot-noise mean.
- [[../notebooks/guide_power_anisotropy]] — empirical $C_\ell/C_0$ scatter around the $1/N_{\rm eff}$ mean.

## Related concepts

[[N_eff]], [[Cl_over_C0]], [[brightest_source_fraction]],
[[SMBH_population_model]], [[dipole_distribution]].
