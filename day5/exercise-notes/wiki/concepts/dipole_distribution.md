# Distribution of $C_1/C_0$

Four semi-analytic approximations for the conditional distribution of
$U \equiv C_1/C_0$ given the source weights $\{p_a\}$, plus an exact
integral representation. Each approximation requires only
$(p_1, p_2, \eta)$.

## Setup

$\mathbf S = \sum_a p_a \hat n_a$ with isotropic random directions.
$U = |\mathbf S|^2$. See [[Cl_over_C0]].

## Exact conditional pdf (1D Fourier-Bessel integral)

Radial density of $R=|\mathbf S|$:

$$f_R(r\mid\{p_a\}) = \frac{2r}{\pi}\int_0^\infty k\sin(kr)
\prod_a \frac{\sin(p_a k)}{p_a k}\,dk,$$

then $f_U(u) = f_R(\sqrt u)/(2\sqrt u)$.

## Approximation 1 — bright source only ($p_1\to 1$)

$$f_U(u) = \delta(u - p_1^2).$$

## Approximation 2 — two-source uniform

If $p_1$ and $p_2$ are the only anisotropic contributors,
$U$ is **exactly uniform** on $[(p_1-p_2)^2, (p_1+p_2)^2]$:

$$f_U(u\mid p_1,p_2) = \frac{1}{4 p_1 p_2}, \qquad
(p_1-p_2)^2 \le u \le (p_1+p_2)^2.$$

## Approximation 3 — one-source + Gaussian background (noncentral Maxwell)

With $\eta = \sum_{a\ge 2} p_a^2$:

$$f_U(u\mid p,\eta) = \sqrt{\frac{3}{2\pi\eta}}\,\frac{1}{p}\,
\exp\!\left[-\frac{3(u+p^2)}{2\eta}\right]
\sinh\!\left(\frac{3 p\sqrt u}{\eta}\right).$$

Conditional mean $p^2+\eta$, matches exact $\sum_a p_a^2$. Collapses to
$\delta(u-p^2)$ as $\eta\to 0$. Paper eq `eq:1src_gauss`.

## Approximation 4 — two-source + Gaussian background

With $\eta_2 = \sum_{a\ge 3} p_a^2$ and $\sigma=\sqrt{\eta_2/3}$,
$a_\pm = p_1\pm p_2$:

$$f_U(u) = \frac{1}{4p_1 p_2}\!\left[
\Phi\!\tfrac{a_+ - \sqrt u}{\sigma} - \Phi\!\tfrac{a_- - \sqrt u}{\sigma}
- \Phi\!\tfrac{a_+ + \sqrt u}{\sigma} + \Phi\!\tfrac{a_- + \sqrt u}{\sigma}
\right].$$

Paper eq `eq:2src_gauss` (now `multline` for layout).

## Numerical performance

The 1-source+Gaussian approximation is "nearly exact" for the
astrophysical populations considered. Brightest source accounts for
63–75% of $\sum p_a^2$ across realizations at $\varepsilon=0.66$,
see `distribution_c1c0.tex:88`.

## Inverse: $P(p_1 \mid C_1/C_0)$

The four laws above are **forward** ($P(U\mid\{p_a\})$, geometry only). The
inverse $P(p_1\mid U)$ is what answers "given a large dipole, how dominant is
the brightest source?" By Bayes it also needs the population prior $\pi(p_1)$:

$$P(p_1\mid u) = \frac{P(u\mid p_1)\,\pi(p_1)}{P(u)},\qquad
P(u\mid p_1)=\int d\eta\,f_U(u\mid p_1,\eta)\,\pi(\eta\mid p_1).$$

Three nested predictions:

1. **Delta** (Approx. 1): $P(p_1\mid u)=\delta(p_1-\sqrt u)$ — upper envelope.
2. **Mean relation**: $\langle u\mid p_1,\eta\rangle=p_1^2+\eta\Rightarrow
   p_1=\sqrt{u-\eta}$ (offset below the envelope = the sub-dominant power $\eta$).
3. **Noncentral Maxwell inverted** (Approx. 3 read as a function of $p_1$):
   $$P(p_1\mid u)\propto \pi(p_1)\,\frac{1}{p_1}\,e^{-3p_1^2/2\eta}\,
   \sinh\!\Big(\frac{3p_1\sqrt u}{\eta}\Big),$$
   flat-prior mode $p_1^\star\simeq\sqrt u-\eta/(3\sqrt u)$.

Unlike the forward laws (pure geometry), the inverse mixes in astrophysics
through $\pi(p_1)$ (depends on $\varepsilon$, frequency). Marginalizing $\eta$
**properly** over $P(\eta\mid p_1)$ — by importance-sampling the realizations
with weights $f(x\mid p_{1,j},\eta_j)$, which also folds in $\pi(p_1)$ — (3)
reproduces the Monte-Carlo conditional to $\sim$1–2% on the median at
$C_1/C_0\in\{0.05,0.1,0.2,0.5\}$; the $\eta$-spread barely shifts the centre
(mean-$\eta$ plug-in ≈ marginalized). Verified in
[[../notebooks/guide_power_anisotropy]] §10f.

The same inversion gives $P(N_{\rm eff}\mid C_1/C_0)$ with $N_{\rm eff}=
1/\sum_a p_a^2=1/(p_1^2+\eta)$ (see [[N_eff]]): since $\langle C_1/C_0\rangle=
1/N_{\rm eff}$, a dipole $x$ implies $N_{\rm eff}\approx 1/x$ — a handful of
sources ($\approx2$ at $x=0.5$, $\approx5$ at the NANOGrav limit $0.2$).

## How much variance a moment-only treatment misses (measured 2026-08-11)

$\sum_a p_a^2$ is the *direction-average* $\mathbb E[U\mid\{p_a\}]$, not $U$
itself. A pipeline that computes only strain moments — as
[[../sources/arxiv_2608_09929]] §II B does, on the grounds that "the shot-noise
is $\ell$-independent and its amplitude is determined by these moments" — gets
the ensemble mean right but omits the scatter of $U$ about it. Measured from
the sampled Monte Carlos of `new_montecarlos_codex/results/sampled_power_anisotropy_eps*.npz`:

| | $\varepsilon=0.20$ | $\varepsilon=0.38$ | $\varepsilon=0.66$ |
|---|---|---|---|
| 95% range of $(C_1/C_0)/\sum_a p_a^2$, $f=0.085/{\rm yr}$ | 1.41 dex | 1.38 dex | 1.24 dex |
| same, $f=1.03/{\rm yr}$ | 1.28 dex | 1.23 dex | 1.15 dex |
| after averaging $\ell\le3$ | 0.47–0.52 | 0.44–0.49 | 0.41–0.44 |
| after averaging $\ell\le6$ | 0.26–0.28 | 0.24–0.27 | 0.22–0.24 |

The median of the ratio is $0.94$–$0.98$ and its mean is $1.00$ to three
digits, so the moment estimator is unbiased in the mean, as claimed; and the
realized $C_\ell/C_0$ is flat in $\ell$ over $1$–$6$ in the ensemble mean,
confirming their $\ell$-independence. The gap is entirely in the spread, and it
is only material for a single-multipole measurement. For a broadband
$\ell$-averaged amplitude (NANOGrav's $\tilde C_{\ell>0}/\tilde C_0$) the
moment-only PDF is adequate.

## Source pages

- [[../sources/pn_C1_over_C0]] — canonical, all four approximations derived in Secs. 8-11.
- [[../sources/pn_1src_vs_dipole_cov]] — dipole as low-pass projection of source-power sky.
- [[../sources/arxiv_2608_09929]] — the moment-only realization PDF this page's angular scatter sits on top of.

## Notebooks and figures

- [[../notebooks/guide_dipole_analytics]] — validates all four approximations, 3D walk, statistics table.
- [[../notebooks/guide_power_anisotropy]] — §10e/§10f: joint $(p_1,C_1/C_0)$ density, MC conditional $P(p_1\mid C_1/C_0)$, and the analytic inversion of the forward laws above (matches MC to ~1–2%).
- [[../notebooks/guide_interactive]] — same four approximations benchmarked interactively.
- [[../figures/c1c0_distribution]] — the paper figure showing all four approximations overlaid on Monte Carlo.

## Paper uses

- `distribution_c1c0.tex` — Section 4 and equations `eq:1src_gauss`, `eq:2src_gauss`, Figure `fig:c1c0_pdf`.

## Related concepts

[[Cl_over_C0]], [[brightest_source_fraction]], [[N_eff]].
