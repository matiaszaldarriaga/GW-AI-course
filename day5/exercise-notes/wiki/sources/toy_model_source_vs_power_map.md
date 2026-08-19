# Toy model: source vs power-map evidences (NOTEBOOK-READY)

**Source:** `references/toy_model_source_vs_power_map_evidences.md`
**Type:** Self-contained Gaussian pedagogical note (ChatGPT-style), written so
every formula maps directly to a notebook cell.
**Ingested:** 2026-06-13

## Summary

A fully self-contained Gaussian toy that compares, on the *same data*, the
Bayesian evidence ratios (vs a unit-Gaussian null) of six hypotheses: a
known-location coherent (mean-shift) source, a known-location covariance
(rank-one variance) source, a one-source-unknown-location model, an arbitrary
coherent amplitude map, an arbitrary positive power map, and a smooth
power-spectrum ($C_\ell$) model in which the positive power field is the square
of a Fourier-expanded auxiliary field. The data reduce to $N$ orthonormal
scalar projections $z_\alpha = v_\alpha^T d$ with $z_\alpha \sim \mathcal N(0,1)$
under the null and the models depend on the data only through
$s_\alpha \equiv z_\alpha^2$. The central structural lesson is that **one-source
models *sum* over candidate locations (a Bayesian $1/N$ look-elsewhere factor)
while map and $C_\ell$ models *multiply* over pixels** (independent or
Fourier-correlated degrees of freedom). For a true one-source sky, the *averaged*
Bayes factor of the $C_\ell$ model coincides with a single one-pixel covariance
source $b_{\rm cov}(s;V_1)$ with $V_1=\sum_k C_k$ — yet the *typical log*
evidence is penalized because every empty pixel contributes a negative
$\ell_0(q)<0$. This is the Bayesian/Occam-penalty complement to the frequentist
degree-of-freedom penalty in [[pta_source_detection_likelihood]], and it is the
intended substrate for an illustrative Monte-Carlo figure in the paper rewrite
(matched-filter / template-projected $a_{LM}$ vs raw $C_\ell$).

This is a deliberately notebook-ready note: §20 lays out a concrete notebook
structure (mock data, building blocks via Gauss-Hermite quadrature, the four
basic evidences, conditional averages, average log evidences, and the 2D
Gauss-Hermite power-spectrum evidence), and §21 collects all the formulas in
copy-paste form.

## Key equations

- **Setup (§2).** $z_\alpha = v_\alpha^T d$, orthonormal templates
  $v_\alpha^T v_\beta = \delta_{\alpha\beta}$, null $z_\alpha\sim\mathcal N(0,1)$,
  $s_\alpha \equiv z_\alpha^2$. Components orthogonal to $\mathrm{span}\{v_\alpha\}$
  cancel from every evidence ratio.

- **Evidence ratio (§3).** $B_H(z) = p(z|H)/p(z|H_0) = \int d\theta\, p(\theta|H)\,
  p(z|\theta,H)/p(z|H_0)$. This integrates over parameters (Occam penalty from
  prior volume), and is explicitly *not* a profile likelihood (which maximizes).

- **Basic one-pixel likelihood ratio (§12, §21).**
  $$r(s,q) = (1+q)^{-1/2}\exp\!\left[\frac{qs}{2(1+q)}\right].$$

- **Mean (coherent) building block (§4.1).** Closed form,
  $$b_{\rm mean}(s;\sigma^2) = \frac{1}{\sqrt{1+\sigma^2}}\exp\!\left[\frac{\sigma^2 s}{2(1+\sigma^2)}\right],$$
  i.e. $\log b_{\rm mean} = -\tfrac12\log(1+\sigma^2) + \sigma^2 s/[2(1+\sigma^2)]$.
  After marginalizing the Gaussian amplitude prior $a\sim\mathcal N(0,\sigma^2)$,
  the mean model becomes $z\sim\mathcal N(0,1+\sigma^2)$ — a Gaussian coherent
  prior turns a mean-shift into a fixed variance enlargement.

- **Covariance building block (§4.2, §21).** No closed form, but a 1D integral,
  $$b_{\rm cov}(s;\sigma^2) = \mathbb E_{a\sim\mathcal N(0,\sigma^2)}\!\left[r(s,a^2)\right]
   = \int_0^\infty dq\,\frac{e^{-q/2\sigma^2}}{\sqrt{2\pi\sigma^2 q}}\,(1+q)^{-1/2}\exp\!\left[\frac{qs}{2(1+q)}\right].$$
  (Gauss-Hermite quadrature in $a$ in the notebook.)

- **The two blocks agree to $O(\sigma^2)$, first differ at $O(\sigma^4)$ (§4.3).**
  Both equal $1+\tfrac{\sigma^2}{2}(s-1)+O(\sigma^4)$, then
  $b_{\rm mean} = \dots + \tfrac{\sigma^4}{8}(s^2-6s+3)$ vs
  $b_{\rm cov} = \dots + \tfrac{3\sigma^4}{8}(s^2-6s+3)$.

- **Four basic evidences (§9, §21).** With $m(s)\equiv b_{\rm mean}(s;\sigma^2)$,
  $c(s)\equiv b_{\rm cov}(s;\sigma^2)$:
  $$B_{\rm 1src,mean} = \tfrac1N\sum_\alpha m(z_\alpha^2),\quad
    B_{\rm 1src,cov} = \tfrac1N\sum_\alpha c(z_\alpha^2),$$
  $$B_{\rm map,mean} = \prod_\alpha m(z_\alpha^2),\quad
    B_{\rm map,cov} = \prod_\alpha c(z_\alpha^2).$$

- **Central distinction (§9).**
  $$\boxed{\text{one-source models SUM over locations; map models MULTIPLY over pixels.}}$$
  The $1/N$ in the one-source evidences is the Bayesian look-elsewhere penalty
  (prior $p(\alpha)=1/N$); the evidence is an *average* over fixed-location
  evidences, not a max (§6.1).

- **Power-spectrum ($C_\ell$) model (§12–§14).** Auxiliary field
  $g_\alpha = \sum_k[A_k\cos(k\theta_\alpha)+B_k\sin(k\theta_\alpha)]$ with
  $A_k,B_k\sim\mathcal N(0,C_k)$, positive power map $q_\alpha = g_\alpha^2$, and
  for a single mode
  $$B_\ell(C_\ell) = \int dA\,dB\,\frac{e^{-(A^2+B^2)/2C_\ell}}{2\pi C_\ell}
    \prod_{\alpha=1}^N r\!\left(z_\alpha^2,[A\cos(\ell\theta_\alpha)+B\sin(\ell\theta_\alpha)]^2\right),$$
  evaluated by 2D Gauss-Hermite quadrature. Unlike the arbitrary power map
  (independent pixel powers), the $C_\ell$ model has *correlated* pixel powers
  tied to a few Fourier coefficients (§14).

- **Averaged Bayes factor for a true one-source sky in pixel 1, $s=z_1^2$
  (§10, §15, §16, §19, §21).** Using
  $\mathbb E_{Z\sim\mathcal N(0,1)}[r(Z^2,q)]=1$ (empty pixels average to a factor
  of one):
  $$\mathbb E_{\rm empty}[B_{\rm 1src,mean}|s] = 1 + \frac{m(s)-1}{N},\quad
    \mathbb E_{\rm empty}[B_{\rm 1src,cov}|s] = 1 + \frac{c(s)-1}{N},$$
  $$\mathbb E_{\rm empty}[B_{\rm map,mean}|s] = m(s),\quad
    \mathbb E_{\rm empty}[B_{\rm map,cov}|s] = c(s),$$
  $$\boxed{\mathbb E_{\rm empty}[B_\ell(C_\ell)|s] = b_{\rm cov}(s;C_\ell)},\qquad
    \mathbb E_{\rm empty}[B(\{C_k\})|s] = b_{\rm cov}(s;V_1),\ \ V_1=\sum_k C_k.$$
  So **on average the $C_\ell$ model looks exactly like a single one-pixel
  covariance source** with variance parameter $V_1=\sum_k C_k$. (More general
  basis $g_\alpha = \sum_i c_i\phi_i(\theta_\alpha)$ gives $V_1 = \sum_i C_i\phi_i(\theta_1)^2$.)

- **Average log evidence ≠ log of average Bayes factor — the Occam penalty
  (§11, §17, §21).** By Jensen, $\mathbb E_0[\log B] \le \log\mathbb E_0[B] = 0$.
  For the $C_\ell$/power-map case each empty pixel contributes
  $$\boxed{\ell_0(q) \equiv -\tfrac12\log(1+q) + \frac{q}{2(1+q)} < 0\ \ (q>0),}$$
  so
  $$\mathbb E_{\rm empty}[\log\Lambda(z|q)\,|\,s] = \log r(s,q_1) + \sum_{\alpha=2}^N \ell_0(q_\alpha),$$
  and likewise $\mathbb E_{\rm empty}[\log B_{\rm map,mean}|s] = \log m(s) + (N-1)\ell_{\rm mean,0}$
  with $\ell_{\rm mean,0} = -\tfrac12\log(1+\sigma^2) + \sigma^2/[2(1+\sigma^2)] < 0$.
  Empty pixels average to a factor one in $B$, but they cost negative log on
  typical data — a model that predicts variance excess away from the true source
  is penalized.

- **Profile (frequentist) comparison (§6.3).** Mean:
  $\log\Lambda_{\rm mean,prof} = \tfrac12\max_\alpha z_\alpha^2$. Covariance:
  $\hat q_\alpha = \max(0, z_\alpha^2 - 1)$, giving per-pixel
  $\log\Lambda_{\rm cov,prof,\alpha} = [\tfrac12(z_\alpha^2-1) - \log|z_\alpha|]_+$.
  The evidence is a softened (prior-weighted, $1/N$-summed) version of this max.

- **Weak-power expansion of the $C_\ell$ search (§18).**
  $\log r(s,q) = \tfrac{q}{2}(s-1) + q^2(\tfrac14-\tfrac{s}{2}) + O(q^3)$, and for an
  orthonormal basis with $\sum_\alpha\phi_i(\theta_\alpha)^2=1$,
  $$B(\{C_i\}) = 1 + \tfrac12\sum_i C_i\sum_\alpha\phi_i(\theta_\alpha)^2(s_\alpha-1) + O(C_i^2).$$
  At weak power the $C_i$ search looks for excess *squared* data $s_\alpha-1$
  weighted by squared basis functions — it responds to power, not to the signed
  coherent amplitude (the toy analog of a quadratic anisotropy search).

- **Headline (§19, §22).**
  $$\boxed{\text{A single source can produce a large power anisotropy, but a smooth }C_\ell\text{ model is not the same hypothesis as one source.}}$$
  One-source = exactly one active location (sparse); map = every pixel active
  (dense); $C_\ell$ = power everywhere, correlated as a random field (dense but
  structured). Different hypotheses give different evidences on the same data.

## Concepts touched

- [[../concepts/matched_filter_vs_power]] — the coherent vs covariance vs
  power-spectrum split is exactly the linear-beats-quadratic story; §18 shows
  the $C_\ell$ search responds to $s_\alpha-1$ (squared data), not the signed
  amplitude.
- [[../concepts/coherent_vs_incoherent]] — $b_{\rm mean}$ (mean-shift, coherent)
  vs $b_{\rm cov}$ (rank-one covariance, incoherent) are the two one-pixel
  building blocks; they agree to $O(\sigma^2)$ and first differ at $O(\sigma^4)$.
- [[../concepts/KL_divergence]] — the note works in evidence/Bayes-factor
  language; the Jensen gap $\mathbb E_0[\log B]<0$ and the per-empty-pixel
  $\ell_0(q)<0$ are the typical-data (KL-flavored) counterpart of the averaged
  Bayes factor.
- [[../concepts/source_background_degeneracy]] — "averaged $C_\ell$ evidence =
  one covariance source $b_{\rm cov}(s;V_1)$" is the evidence-language statement
  that a single source and a smooth power model are confusable in covariance but
  distinct as hypotheses.
- [[../concepts/Cl_over_C0]] — the $C_\ell$ toy is the analog of the angular
  power spectrum of a positive power map; $V_1 = \sum_k C_k$ is the toy
  total-power at the source pixel.
- [[../concepts/fisher_hierarchy]] — the same coherent/covariance/$C_\ell$
  ordering appears here as an evidence hierarchy; the empty-pixel Occam penalty
  is the Bayesian face of the $p^2$-vs-$p^4$ degradation.
- [[../concepts/brightest_source_fraction]] — the one-source-in-pixel-1 sky with
  $s=z_1^2$ is the toy stand-in for a single dominant SMBHB carrying fraction
  $p$ of the power.

## Paper uses

Not currently cited. No `\fromnotebook{toy_model_source_vs_power...}` exists in
`paper/sections/` (verified by grep on 2026-06-13).

## Could be cited

- `three_strategies.tex` — the cleanest illustrative statement that coherent
  source fitting, incoherent covariance, and $C_\ell$ compression are *different
  hypotheses*, with a controlled Gaussian toy backing the ordering.
- `angular_power_spectrum.tex` — the "averaged $C_\ell$ evidence looks like one
  covariance source $b_{\rm cov}(s;V_1)$, but the typical log evidence is
  penalized by $\ell_0(q)<0$ in empty pixels" is a sharp, citable formalization
  of why a single source can mimic a $C_\ell$ on average yet be disfavored.
- `appendix_fisher.tex` / a new toy-model appendix — §20–§21 are an
  implementation-ready recipe for the illustrative Monte-Carlo figure the rewrite
  wants (template-projected $a_{LM}$ / matched filter vs raw $C_\ell$).
- `discussion.tex` — the §22 conceptual summary (sparse vs dense vs structured
  hypotheses) is a candidate for the closing discussion.

## Related wiki pages

- [[pta_source_detection_likelihood]] — the frequentist (profile-likelihood,
  dof-penalty) companion of this note; together they give the two-language
  (frequentist + Bayesian) version of the power-vs-coherent story.
- [[pta_1src_vs_CL]] — canonical one-source-vs-$C_\ell$ note in the real PTA
  setting; this toy is its stripped-down Gaussian analog.
- [[pta_1src_vs_cls_toy]] — companion toy Fisher note (dipole capture fraction);
  same one-source-vs-power-spectrum theme in Fisher rather than evidence
  language.
- [[matched_filter_vs_power]] — general linear-vs-quadratic source page.
- [[pn_coh_vs_quadratic]] — self-contained coherent-vs-covariance pedagogical
  note; shares the two one-pixel building blocks.
- [[pn_coherent_vs_stochastic_single_source]] — single-template monotone
  equivalence of coherent and stochastic *profile* statistics; complements this
  note's *evidence* treatment.
- [[draft_sufficient_statistics_2026]] — companion draft; its App. B
  stochasticization ($\vec h\mapsto\vec h\vec h^\dagger$, $\partial C/\partial\mu|_0=0$)
  is the structured-PTA version of $b_{\rm mean}\to b_{\rm cov}$ here.
- [[pn_appendixB_coherent_vs_covariance]] — ChatGPT critique of that App. B;
  same coherent→covariance reduction and Occam/cosmic-variance themes.
