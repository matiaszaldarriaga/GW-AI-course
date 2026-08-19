# Conventions

The contract that prevents notation drift. Every concept page, source
page, and paper section is held to these. If a source uses a different
convention, note the translation inline on that source page; never
change the canonical convention in the wiki.

## Angular power spectrum

Three distinct objects with the same symbol are in play in the
literature. In this wiki:

- **$C_\ell \equiv C_\ell^{(P)}$** by default: angular power spectrum of
  the **source-power sky** $P(\hat\Omega) = \sum_a q_a\,
  \delta^{(2)}(\hat\Omega,\hat n_a)$. This is the object the paper
  analyzes and that NANOGrav maps to.
- **$C_\ell^{(b)}$**: angular power spectrum of the **incoherent
  pulsar-power map** $b(\hat p)$. Related to $C_\ell^{(P)}$ by an
  exact transfer function: $b_{LM} = \tau_L p_{LM}$ with
  $\tau_0 = \pi/3,\;\tau_1=\pi/6,\;\tau_2=\pi/30,\;\tau_{L\ge 3}=0$.
  Key consequence: $C_1^{(b)}/C_0^{(b)} = (1/4)\, C_1^{(P)}/C_0^{(P)}$.
- **$C_\ell^{z}$**: angular power of the coherent time-delay map
  $z(\hat p)$. Distinct again. Falls as $\ell^{-4}$ for a single source.

If you see a formula like $C_1/C_0 = p^2/4$, it is the **pulsar-map**
version. The source-sky version is $C_1/C_0 = p^2$. Never conflate.

## Source weights

- $q_a$ = weight of source $a$ in the map (typically $h_s^2$).
- $Q = \sum_a q_a$, $p_a = q_a/Q$, so $\sum_a p_a = 1$.
- $p \equiv p_1 = \max_a p_a$ throughout this project.
- $N_{\rm eff} \equiv 1/\sum_a p_a^2$ (inverse participation ratio).
- $\eta \equiv \sum_{a\ge 2} p_a^2$ used in 1-source+Gaussian
  approximation; $\eta_2 \equiv \sum_{a\ge 3} p_a^2$ for 2-source.

## Two symbols that must not be reused (settled 2026-08-12)

Both collisions were found by the style audit (D-26 finding (v)) and
removed from `paper_v2` in the decision-implementation pass.

- **$\eta$ is the faint-background variance $\sum_{a\ge2}p_a^2$ and
  nothing else.** It used to double as the symmetric mass ratio
  $q/(1+q)^2$ in the single-binary strain formula. That formula now
  writes $[q/(1+q)^2]^2$ inline and the second definition is gone. Do
  not reintroduce $\eta$ for the mass ratio in any paper, note, or
  script docstring.
- **$x$ is the measured dipole $C_1/C_0$ and nothing else.** It used to
  double as the Hellings--Downs variable $(1-\cos\zeta_{ab})/2$. That
  variable is now $u$, in the displayed curve and in the sentence that
  defines it. Nothing else in the project used the second meaning.

## Isotropic-background amplitude significance

$$\Sigma_{\rm bg}^2 \equiv A^2 F_A, \qquad
  F_A = \tfrac12\,\mathrm{Tr}[C_0^{-1}\Gamma^{\rm HD}C_0^{-1}\Gamma^{\rm HD}].$$

Exact value in the noise-dominated uniform-array benchmark (derived by
exact pair-averaging; see `sources/pta_noise_dominated_limit.md` once
ingested):

$$\Sigma_{\rm bg}^2 = \frac{A^2 N_p}{2\sigma_n^4}\left(1+\frac{N_p-1}{48}\right).$$

The $1/48$ comes from the Legendre integral of the HD cross-curve,
$\tfrac12\int_{-1}^1 \chi(\mu)^2\,d\mu = 1/48$. Not to be remembered as
a random number; it has a closed-form origin.

## Block weights $s_L$

$$s_L(N_p,0) = \frac{2L+1}{4\pi}\,
  \frac{D_L + (N_p-1) O_L}{1 + (N_p-1)/48},$$

with exact diagonal contributions $D_1 = \pi$, $D_2 = \pi/25$,
$D_{L\ge 3} = 0$, and off-diagonal $O_L$ obtained from the exact
pair-average integral over the pair cosine $\mu$.

Values for $N_p = 67$ (NANOGrav 15yr):

| $L$ | $s_L$ |
|---:|---:|
| 1 | 0.5663 |
| 2 | 0.8936 |
| 3 | 0.5569 |
| 4 | 0.3674 |
| 5 | 0.2356 |
| 6 | 0.1547 |

Source: exact quadrature, confirmed by Monte Carlo at percent level,
see `sources/pta_exact_pair_average.md` (ingest pending).

## Fisher vs KL divergence

**KL divergence $D$** is the detection figure of merit throughout this
wiki. It is the expected log-likelihood ratio of "signal present" vs
"null" under the signal hypothesis.

Relation to Fisher: for a parameter $\theta$ with a regular expansion
around $\theta=0$, $D(\theta) \approx (1/2)\,\theta^2\,F_{\theta\theta}(0)$.

**Watch out:** if $F_{\theta\theta}$ is itself a function of $\theta$,
the KL scaling is not the same as the Fisher scaling. Specifically, the
$C_L$-only Fisher $F_{pp}^{(C_L)} \propto p^2$, so
$D_{C_\ell}\propto p^2 \cdot F_{pp}^{(C_L)} \propto p^4$, not $p^2$.
This is the bug that lived in the paper until 2026-04-13.

## "Covariance search" is ambiguous — name the construction

The middle ($p^2$) rung of the hierarchy is the **power-map / physical
Gaussian-marginalized** covariance (the one-source statistic
$T_{\rm psrc}=(v^Ts)^2/(v^TFv)$, $\lambda_{\rm psrc}=p^2 v^TFv$). Do
**not** call a generic "incoherent covariance search" the $p^2$ object:
the **source-subspace projector** covariance $C_B(I+\eta\Pi)$ has a
profiled likelihood ratio $g_r(T_{\rm coh})=T-r-r\ln(T/r)$ that is
strictly monotone in the coherent statistic, so it sits at the **$p$**
level with the *same* threshold as the matched filter
($p_{{\rm sub},*}=p_{{\rm coh},*}$). A third object, the arbitrary
harmonic map $T_{\rm map}=s^TF^{-1}s$, keeps the $p^2$ signal norm but
pays an $m$-degree-of-freedom threshold penalty. Only compressing to
block powers $C_L$ (integrating over the $m$-pattern) forces $p^4$.
Canonical: `sources/pta_source_detection_likelihood`; concept owner
`concepts/fisher_hierarchy`. This is the "same question keeps the
information / a different question throws it away" distinction.

## Sqrt-spherical-harmonic basis

The NANOGrav 15yr anisotropy analysis writes the positive GW power as
$P(\hat\Omega) = [\sum_{LM} b_{LM} Y_{LM}]^2$. If the measured
$C_\ell$ goes up to $\ell_{\max}^a$, the underlying $b_{LM}$ expansion
is truncated at $\ell_{\max}^b = \ell_{\max}^a/2$. For the NANOGrav
15yr analysis $\ell_{\max}^a = 6$, so $\ell_{\max}^b = 3$. This comes
from the Clebsch-Gordan selection rule when squaring: a field with
modes up to $L$ produces power up to $\ell = 2L$. Reference:
Banagiri et al. 2021 (2103.00826). See `sources/arxiv_2103_00826.md`
once ingested.

This truncation strongly affects the prior on $C_\ell/C_0$ (see
`concepts/sqrt_SH_basis.md` once written).

## Spherical harmonic conventions

Complex SH with Condon-Shortley convention, matching `healpy`. Real SH
would differ by a basis transform; we verified the $C_\ell$ ratios are
convention-independent (the "3 independent methods" check in memory).

If a note uses real SH, convert in the note summary.

## Figure style

Every `paper/scripts/fig_*.py` imports the shared style module
`paper/scripts/_paperstyle.py` and calls `apply_style()` before
plotting. No per-script global rcParams; the module is the single
source of truth.

- **Draw at final printed width.** Figures are sized to the width they
  appear at on the page, so fonts never rescale through LaTeX.
  `figsize_1col(h)=(3.40, h)` for a single-panel / `\columnwidth`
  figure; `figsize_2col(h)=(7.06, h)` for a full-width `\textwidth`
  (`figure*`) figure. `\includegraphics` uses `width=\columnwidth` or
  `width=\textwidth` with no further scaling, so a point is a point in
  every figure.
- **$\varepsilon$ model $\to$ color is fixed**: `EPS_COLORS` maps
  $\varepsilon=0.20\to$ blue (`#1f77b4`), $0.38\to$ orange (`#ff7f0e`),
  $0.66\to$ green (`#2ca02c`). Build models from `EPS_MODELS` so the
  map lives in one place. When a figure shows several **frequencies of
  one model**, distinguish them by line **style** (`FREQ_STYLES =
  ['-', '--', ':']`), never by color, so green never means both
  "$\varepsilon=0.66$" and "a frequency".
- **One recorded exception to the $\varepsilon\to$color map**, granted
  2026-08-12 (decision GS-09): `fig_p1_neff_conditional.py` (paper_v2
  Fig. 7) encodes frequency by *hue* as well as by line style. That
  panel shows a single $\varepsilon = 0.66$ model, so the model--color
  convention carries no information there and cost legibility: all six
  curves came out the same green. Its palette is local to that script
  (`FREQ_COLORS`, chosen away from `EPS_COLORS`) and its caption says
  so. The convention is unchanged in Figs. 3, 5, 6 and 8. This is a
  recorded exception, not drift; do not generalize it.
- **Distinct semantics get distinct maps.** Method comparison uses
  `METHOD_COLORS` (scan=blue, $C_\ell$=red, point-source=black);
  strategy scaling uses `STRATEGY_COLORS` (coherent=blue,
  incoherent=orange, $C_L$-only=green). These are separate from the
  $\varepsilon$ map by design.
- **Linewidths via `LW`**: `primary` 1.5 (the rc default), `secondary`
  1.2, `reference` 1.0. Use `LW[...]`/`MS[...]`/`CAPSIZE` instead of
  literal values.
- **Fonts**: serif body with Computer Modern mathtext
  (`mathtext.fontset='cm'`), base size 9 (labels 9, ticks/legend 8).
  `text.usetex=False` by default so figures build without a LaTeX
  install; flip the one-line `USETEX` toggle in `_paperstyle.py` to
  `True` for the final build to match the paper face exactly.
- **Other rc**: ticks in + minor on, top/right spines ticked;
  frameless legends; grid at `alpha=0.25`; `savefig.dpi=300`,
  `bbox='tight'`.

## Journal conventions in `references.bib`

- APS journals: "Phys. Rev. D" with integer volume and article number
  as pages ("Phys. Rev. D 109 123544 (2024)").
- ApJL: "Astrophys. J. Lett." with volume and `L`-prefixed page.
- A&A: "Astron. Astrophys." with volume and `A`-prefixed page.
- Arxiv-only preprints use `@misc` with `eprint` and `archivePrefix`.
- Always include the eprint ID even if the paper is published. It is
  the single most useful field for future verification.

## Procedural rules

- **No eyeballing.** Any numeric claim must be computed, not estimated
  from a figure. If you need a number, run it; if you can't, add it to
  `todo.md`.
- **No silent bib edits.** Use `verify-reference` (see `CLAUDE.md`)
  before modifying `paper/references.bib`.
- **Source wins.** If the wiki and a verified source disagree, the
  wiki is wrong. Fix the wiki.
- **Memory updates only on user endorsement.** The `memory/` tree is
  for facts the user has confirmed, not draft conclusions.
