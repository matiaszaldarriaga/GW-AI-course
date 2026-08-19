# Detection statistics for a single source: coherent vs stochastic alternatives

**Source:** `references/coherent_vs_stochastic_single_source.md`
**Type:** Pedagogical note. Self-contained single-bin calculation
separating **detection-test equivalence** from **Fisher-information
inequivalence** for a single-template CW signal modeled either as a
deterministic amplitude $\mu$ or as a stochastic amplitude with
variance $q = \mu^2$.
**Ingested:** 2026-04-20

## Summary

Sharpens the coherent-vs-stochastic discussion at its cleanest toy:
one template $\vec t$, diagonal noise $N$, scalar amplitude. Three
hypotheses:

- $H_0$: $\vec d \sim \mathcal N(0, N)$.
- $H_1$: $\vec d \sim \mathcal N(\mu\vec t, N)$ (coherent, deterministic $\mu$).
- $H_1^\star$: $\vec d \sim \mathcal N(0,\, N + \mu^2 \vec t\vec t^T)$ (stochastic, random $\mu$ with variance $q=\mu^2$).

Two scalars carry all the information in the data:
$$
x \equiv \vec t^T N^{-1} \vec d,\qquad \rho^2 \equiv \vec t^T N^{-1}\vec t,\qquad s \equiv x^2/\rho^2.
$$

The note proves two statements that can easily be confused with each
other and arrives at the correct separation.

**(I) Detection tests are monotone-equivalent.** The maximized LLRs are
$$
T_1(\vec d) = s,\qquad
T_{1^\star}(\vec d) = \max(s - 1 - \ln s,\,0).
$$
For $s \geq 1$ the map $s \mapsto s - 1 - \ln s$ is strictly
increasing, so $T_1$ and $T_{1^\star}$ have **identical p-values,
identical ROC, identical detection significance**, on every
realization — regardless of the truth. Stochasticization of $H_1$ is
*not* lossy at the detection stage in this single-template problem.

**(II) Fisher information differs.** $F_{H_1}(\mu) = \rho^2$
(constant). $F_{H_1^\star}(\mu^2) = \rho^4/[2(1+\alpha)^2]$
with $\alpha = \mu^2\rho^2$. The Cramér–Rao bound on the stochastic
estimator grows like $(1+\alpha)^2$ — a variance-parameter feature,
analogous to the textbook bound $\mathrm{Var}(\hat\sigma^2) \geq 2\sigma^4/n$.

The two results are not in conflict: **test significance** depends on
the peak *value* of the likelihood relative to the null distribution,
while **Fisher information** depends on the peak *curvature*. Different
likelihoods can produce the same peak height but different curvatures.

## Section-by-section synopsis

- **§1 Setup.** Defines $H_0$, $H_1$, $H_1^\star$ and the sufficient
  scalars $(x, \rho^2, s)$.
- **§2 $H_1$ vs $H_0$ LLR.** Because both have covariance $N$, the
  determinant terms cancel. $2\ln\Lambda_1(\mu) = 2\mu x - \mu^2\rho^2$,
  maximizing to $\hat\mu = x/\rho^2$ and $2\ln\Lambda_1|_{\hat\mu} = s$.
- **§3 $H_1^\star$ vs $H_0$ LLR.** Sherman–Morrison + matrix-determinant
  lemma. Using $\alpha = \mu^2\rho^2$,
  $2\ln\Lambda_{1^\star}(\alpha) = -\ln(1+\alpha) + \alpha s/(1+\alpha)$,
  maximizing to $\hat\alpha = s-1$ (clipped at 0) and
  $2\ln\Lambda_{1^\star}|_{\widehat{\mu^2}} = s - 1 - \ln s$.
- **§4 Equivalence of the two tests.** Central result. Monotone
  invariance gives identical p-values. Then a long sub-section
  (*The data-analysis scenario: fixed truth, choice of statistic*)
  untangles what the equivalence does and doesn't claim:
  - Statistic equivalence does not depend on the true data-generating
    distribution.
  - But the data-generating distribution determines the **sampling
    distribution** and hence the ROC:
    - Truth $H_1$ with amplitude $\mu$: $s \sim \chi^2_1(\alpha)$ —
      non-central, mean $1+\alpha$, variance $2(1+2\alpha)$.
    - Truth $H_1^\star$ at matched power $\alpha$: $s \sim (1+\alpha)\chi^2_1$
      — same mean, variance $2(1+\alpha)^2$.
  - At small $\alpha$, the expected LLR (the KL divergence from $H_0$)
    scales **linearly** under $H_1$-truth and **quadratically** under
    $H_1^\star$-truth. *That $\alpha$-vs-$\alpha^2$ gap is a statement
    about physics, not about the analyst's modeling choice.*
  - **Takeaway**: in this single-bin, single-template, Gaussian setting
    the modeling choice between $H_1$ and $H_1^\star$ has **no cost at
    the detection stage**. Where they differ is in **parameter
    interpretation** (amplitude vs variance) and hence in parameter
    precision (§5).
  - Cautionary note: the statistic-level equivalence relies on the
    one-dimensional structure. In multi-parameter, non-Gaussian-prior,
    or non-linear-template settings, the two modeling choices can
    decouple and the coherent likelihood can be strictly more
    informative.
- **§5 Fisher information.**
  - §5.1 Coherent: only mean depends on $\mu$ →
    $F_{H_1}(\mu) = \rho^2$.
  - §5.2 Stochastic: only covariance depends on $\mu^2$ →
    $F_{H_1^\star}(\mu^2) = \rho^4/[2(1+\alpha)^2]$. In the $\mu$
    parametrization $F_{H_1^\star}(\mu) = 2\alpha\rho^2/(1+\alpha)^2$,
    which **vanishes at $\mu = 0$** — $\mu$ is non-identifiable there
    (sign flip is invariant).
  - §5.3 Cramér–Rao bounds.
  - §5.4 Detection-SNR scaling near the null: $\Lambda \simeq \tfrac12\alpha$
    (linear) under $H_1$-truth, $\Lambda \simeq \tfrac14\alpha^2$
    (quadratic) under $H_1^\star$-truth. **Scalings attached to the
    truth, not the modeling.**
- **§6 Closing remark.** Same test significance, different Fisher
  information — two different features of the log-likelihood
  surface. Report either $\hat\mu \pm 1/\rho$ (coherent) or
  $\hat\alpha \pm \sqrt 2(1+\alpha)$ (stochastic); detection claim is
  the same, parameter meaning differs.

## Key formulas

| Quantity | Formula |
|---|---|
| Sufficient scalar | $s = x^2/\rho^2$, $x = \vec t^T N^{-1}\vec d$, $\rho^2 = \vec t^T N^{-1}\vec t$ |
| Coherent LLR max | $2\ln\Lambda_1\|_{\hat\mu} = s$ |
| Stochastic LLR max | $2\ln\Lambda_{1^\star}\|_{\widehat{\mu^2}} = s - 1 - \ln s$ (for $s\geq 1$) |
| Coherent ML | $\hat\mu = x/\rho^2$ |
| Stochastic ML | $\widehat{\mu^2\rho^2} = \max(s-1, 0)$ |
| $F_{H_1}(\mu)$ | $\rho^2$ |
| $F_{H_1^\star}(\mu^2)$ | $\rho^4/[2(1+\alpha)^2]$ |
| CR bound coherent | $\mathrm{Var}(\hat\mu) \geq 1/\rho^2$ |
| CR bound stochastic | $\mathrm{Var}(\widehat{\mu^2}) \geq 2(1+\alpha)^2/\rho^4$ |
| $s$ under $H_0$ | $\chi^2_1$ |
| $s$ under $H_1$-truth ($\alpha$) | non-central $\chi^2_1(\alpha)$, mean $1+\alpha$, var $2(1+2\alpha)$ |
| $s$ under $H_1^\star$-truth ($\alpha$) | $(1+\alpha)\chi^2_1$, mean $1+\alpha$, var $2(1+\alpha)^2$ |
| KL from $H_0$ (coherent truth) | $\alpha/2$ |
| KL from $H_0$ (stochastic truth) | $\alpha^2/4$ (leading order at small $\alpha$) |

## Implications for our App. B critique memo

This note **substantially refines** the two-step factoring in
[[../notes/app_B_coherent_fisher_critique]]. The earlier memo argued:

> Step 1 (stochasticization, coherent → covariance) demotes
> $\rho^2 \propto H \to H^2$ regardless of null choice. Step 2
> (same-power null, Eq. 50) adds the $\sim 3.8\sigma$ ceiling.

This note shows Step 1 is subtler than the memo stated:

1. **At the detection-test level** in the single-template, single-bin
   toy, stochasticizing $H_1$ does **not** cost anything. $T_1$ and
   $T_{1^\star}$ are monotone-equivalent and give identical p-values
   against $H_0$ = noise. An analyst who uses the stochastic
   likelihood to test a coherent truth is making the same detection
   claim as if they had used the coherent likelihood.
2. **The $\alpha \to \alpha^2$ scaling is a property of the data
   generating truth**, not of the analyst's modeling choice. If the
   truth is a coherent single source (the physical case of an SMBHB),
   the expected LLR under truth scales linearly in $\alpha$, period,
   whether analyzed with $H_1$ or $H_1^\star$. Only if the truth is
   itself stochastic does the expected LLR scale as $\alpha^2$.
3. **What the stochastic model does lose** is *parameter
   interpretation*: it reports $\hat \alpha$ (a variance) rather than
   $\hat\mu$ (an amplitude), and the Fisher information on the
   variance parameter degrades as $(1+\alpha)^{-2}$.
4. **The App. B $\sim 3.8\sigma$ ceiling** is therefore not the result
   of "stochasticization demoting detection." It is a consequence of
   what the draft **compares against**: a GWB null with matched total
   power (Eq. 50). That is a same-power-discrimination problem,
   fundamentally different from detection-against-noise, and it is
   the sole source of the ceiling in the single-template logic.

The cautionary clause at the end of §4 of the note — equivalence can
break in multi-parameter / non-Gaussian / nonlinear settings — is the
escape hatch for the project's general "linear beats quadratic"
hierarchy; but it does not apply to App. B's isotropic two-polarization
toy limit, where the 2-template analog of the §4 equivalence should
also hold (the Bayes factor and the profile likelihood are both
monotone in $s_+ + s_-$).

The App. B critique memo should be revised at a third pass:

- The "two separable lossy steps" factoring should be replaced by one
  lossy step (the same-power null via Eq. 50) plus an
  *interpretational* effect (reporting a Fisher-poor variance
  parameter instead of a Fisher-rich amplitude).
- The monotone-equivalence argument of §4 of this note should be
  imported as the first thing after the three-picture table, to
  sharpen the claim that "the stochasticization alone is not what
  demotes the scaling in the single-template case."
- §5.1 of the memo (stochasticization) should be rewritten around
  the physics-vs-modeling distinction: the KL-scaling is a property
  of what generates the data; the cosmic-variance formula
  $\mathrm{Var}(\hat q) \geq q^2/k$ is still correct and is what
  drives the Fisher-information degradation on the stochastic
  *parameter*.
- The CMB cosmic-variance parallel should be labeled as a statement
  about parameter precision (Fisher on $C_\ell$), not about
  detection power of a $C_\ell$ test.

Flagged for a Phase-3 revision of the memo; the user may want to
pass first.

## Concepts touched

- [[../concepts/matched_filter_vs_power]] — this note is the sharpest
  single-template realization of that concept page's theorem, and
  clarifies that the "linear beats quadratic" statement applies to
  the **physics** of the data (KL from truth to null), not to the
  analyst's modeling choice of $H_1$ vs $H_1^\star$ in the single-
  template case.
- [[../concepts/fisher_hierarchy]] — the $O(\mu^2)$ vs $O(\mu^4)$
  KL result of the project-level hierarchy is physically correct but
  must be read as "data generated by a single source gives linear KL;
  data generated by a stochastic background at matched power gives
  quadratic KL" — not "whether you call the source $\mu$ or $\mu^2$
  changes your detection significance."
- [[../concepts/coherent_vs_incoherent]] — same refinement applies.
- [[../concepts/KL_divergence]] — the $\alpha/2$ vs $\alpha^2/4$
  scalings of §5.4 are direct KL-from-null results.

## Relation to other sources

- [[pn_appendixB_coherent_vs_covariance]] — ChatGPT's App. B critique.
  Consistent at the level of "App. B derivation is lossy as a
  derivation," but this note tightens the single-template statement
  into monotone equivalence and thus implies that §7.4 of the ChatGPT
  note ("the step is lossy in an information-theory sense") applies
  to the many-to-one map in the multi-parameter setting, not to the
  single-template/single-bin reduction proved here.
- [[draft_sufficient_statistics_2026]] — the draft's App. B + Eq. 50
  + Eq. 48 ceiling. This note localizes the source of the ceiling
  entirely to the Eq. 50 same-power construction.
- [[pn_coh_vs_incoh_fisher]], [[pn_coh_vs_quadratic]] — our earlier
  pedagogical notes on coherent-vs-incoherent Fisher decomposition.
  Consistent; this note is the scalar-amplitude specialization with
  a more careful test-vs-Fisher separation.
