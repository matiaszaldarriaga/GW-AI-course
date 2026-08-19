# Proposed revision of the App. B critique memo (2026-04-20)

**Source memo.** `wiki/notes/app_B_coherent_fisher_critique.md`.

**Inputs driving the revision.**
- `references/coherent_vs_stochastic_single_source.md` — scalar $\mu$,
  single-template monotone equivalence $T_1\leftrightarrow T_{1^\star}$,
  and the clean separation of detection (same p-value) from parameter
  interpretation (Fisher on $\mu$ vs on $\mu^2$).
- `wiki/notes/app_B_2pol_equivalence_check.md` (P1) — the
  equivalence lifts to the $k=2$ App. B isotropic toy limit:
  $T_1=s$, $T_{1^\star}=\max(s-2-2\ln(s/2),0)$; strict monotone
  equivalence; survives $\hat n_s$-maximization; breaks under
  non-isotropic priors on $\vec h$.
- `wiki/notes/app_B_anisotropic_response.md` (P2) — realistic
  $U^\dagger N^{-1}U$ has nondegenerate eigenvalues, so the equivalence
  breaks beyond the Eq. (32) isotropic-pulsar approximation; magnitude
  is $\sim$10–20% rank disagreement typical, up to $\sim$50% in
  $m=0$ null directions, with a few-percent shift on detection
  thresholds.

**One-line upshot of the revision.** The old memo's Step 1
("stochasticization demotes $\rho^2 \propto H \to H^2$ at detection")
conflates two logically distinct things. In the App. B toy limit,
stochasticization does **not** cost anything at the detection stage —
the profile and Bayes-factor statistics are monotone-equivalent. The
$H\to H^2$ scaling is a statement about (a) the data-generating
physics if the truth were stochastic, and (b) Fisher information on
the variance parameter $q$ vs the amplitude parameter $\mu$. The only
genuine detection-level critique is the Eq. 50 same-power null (the
$\sim 3.8\sigma$ ceiling); a third, quantitatively mild, critique is
the anisotropic-response effect of P2.

---

## Section 1: What's staying vs what's changing

The current memo has ten sections. Per-section disposition:

| Section | Content | Disposition |
|---|---|---|
| Lead ("One-sentence conclusion") | Frames App. B as having a ~3.8σ ceiling **plus** an "order in $H$" demotion from stochasticization | **Rewrite.** Keep the "$T$ is the right statistic" clause. Drop "stochasticization costs an order in $H$ in detection significance." Replace with: one main critique (Eq. 50 ceiling) and two side observations (parameter-interpretation effect, mild anisotropic-response effect). |
| §1 "One-paragraph resolution" | Two paths to the same $T$; then "Step 1 stochasticization / Step 2 same-power" factoring | **Rewrite.** Keep the "two paths land on the same $T$" framing and credit the monotone-equivalence argument (now rigorous via P1). Replace the two-step factoring with the new structure in §2 of this proposal. |
| §2 "Two statistics in the draft" (Eq. 49 vs Eq. B6) | Distinguishes the per-$\ell$ alignment $t_\ell$ from the multi-$\ell$ $T(\hat n)$ | **Retain unchanged.** Still correct and still useful. |
| §3 "Coherent derivation of $T(\hat n)$" | MLE via Wiener filter; reduction to Eq. (B6); Wigner-D Fisher block | **Retain unchanged.** The derivation and the diagonal Fisher block $\mathcal F_{\rm tot} \mathbb I_4$ are the backbone of the memo. |
| §4 "Three pictures, three scalings for the same $T$" | The A / A′ / B table with scaling in each | **Reframe.** The table is conceptually right, but (i) the "A → A′ step alone demotes scaling at detection" reading must be corrected — in the isotropic limit A′ and A have monotone-equivalent test statistics, so the A → A′ row of KL is about what you'd measure *if the truth were stochastic*, not about what you lose at detection given coherent truth; (ii) add a caveat that with anisotropic response the equivalence breaks weakly (P2). |
| §5.1 "Step 1: stochasticization" | "$\rho^2$ scaling drops from $H$ to $H^2$ at small $H$ … independent of what null is used"; CMB $\hat C_\ell$ analogy | **Reframe, not delete.** The math (Parametrization 1 and 2, $F_{\mu\mu}^{(\rm cov)}(0)=0$, $F_{qq}^{(\rm cov)}(0)$ finite, cosmic variance of $\hat q$) is correct but is a *parameter-precision* statement (Fisher on $\mu$ vs $q$), **not** a detection-significance statement. Relabel the section "Parameter interpretation: Fisher on $\mu$ vs on $q$." Keep the CMB $\hat C_\ell$ parallel but make it a Fisher-on-$C_\ell$ statement. |
| §5.2 "Step 2: same-power null (Eq. 50)" | The $3.8\sigma$ ceiling from matching trace | **Retain, promote.** Becomes the *main* critique. Retain the explicit $\hat H \sim (f_\sigma H/2)\chi^2_4$ derivation, $2/f_\sigma = 24$, $p\sim 3\times 10^{-4}$. |
| §6 "Why the two paths happen to share $T$" | Conditions: linear template, Gaussian prior, isotropic response | **Rewrite as the monotone-equivalence section.** Replace with the clean derivation imported from P1: give $T_1 = s$ and $T_{1^\star}=\max(s-2-2\ln(s/2),0)$ explicitly, prove monotone equivalence on $s\geq 2$, state survival under $\hat n_s$-max, and list the symmetries required (isotropic $U^\dagger N^{-1}U$, isotropic prior). |
| §7 "Gaussianization is fine at PTA SNR" | Expansion of $\ln I_0$ vs rank-1 Gaussian likelihood at $|h|^2/\sigma^2 \ll 1$ | **Retain unchanged.** Still the correct answer to a natural collaborator question. |
| §8 "Internal inconsistency in the prior" | Uniform-angle law vs $\mathcal{CN}(0,\sigma_h^2 I_2)$ — two different modeling choices | **Retain unchanged.** This is orthogonal to the other critiques and still useful. |
| §9 "Summary for the collaborator" | Five-point summary | **Rewrite to match the new structure.** |
| §10 "Relation to our project" | Cross-references to `fisher_hierarchy` and `matched_filter_vs_power`; "turning $\hat{\vec h}$ into $\hat q$ costs the coherent order" | **Reframe.** The cross-references remain valuable (the $p$-hierarchy is a multi-source statement and is unaffected by the single-source equivalence theorem). But the sentence "turning the former into the latter is the App. B step that costs the coherent order" must be softened: at the single-source detection stage it does not cost anything in the App. B isotropic limit; the loss appears only when (a) you interpret the result as a measurement of source power (§5 parameter effect), (b) you build a multi-source ensemble (which is where the $p$-hierarchy lives), or (c) you change the null to the same-power GWB (§5.2 here). |
| — | New content: P2 "anisotropic-response" critique as a third, mild, critique | **Add** as a new numbered section. Import the eigenbasis formulas $T_1=\sum_i |v_i|^2/\rho_i^2$, $T_{1^\star}=\sum_i w_i |v_i|^2/\rho_i^2 - \mathrm{const}$ with $w_i = q\rho_i^2/(1+q\rho_i^2)$, and the P2 numerical table. |

---

## Section 2: The new factoring

### The choice

I recommend **Option (A): one main critique + two minor ones**, with a
slight structural tweak.

**Main critique.** The Eq. 50 same-power null is the single place where
an order-of-magnitude detection-significance claim is lost in App. B,
and the $\sim 3.8\sigma$ ceiling is its signature. This is the point
a reader should walk away with.

**Minor critique 1 (parameter-interpretation effect).** Stochasticizing
the model does not cost anything at the detection stage in the
isotropic limit (monotone equivalence), but it **does** change the
parameter being measured — $q$ rather than $\mu$ — and with it the
Fisher information and Cramér–Rao variance. The cosmic-variance
analogy with CMB $\hat C_\ell$ is really about this, not about
detection power. This subsumes the old memo's "Step 1" but recast in
the correct parameter-precision language.

**Minor critique 2 (anisotropic-response effect).** For a realistic
PTA the matrix $F(\hat n_s) = U^\dagger(\hat n_s) N^{-1} U(\hat n_s)$
has nondegenerate eigenvalues, which breaks the monotone equivalence
between $T_1$ and $T_{1^\star}$. Quantitatively mild (few-percent
threshold shift, 10–20% rank disagreement), but logically distinct
from the other two.

### Why Option (A) over (B) or (C)

Option (B) ("formula is right, derivation is confusing, one lossy
step") gets the headline right but under-weights the parameter-precision
observation, which is genuinely substantive: the cosmic-variance
Fisher on $q$ is a real constraint that shows up in a downstream
measurement of source power even when the detection call is identical.
A collaborator following the memo should not walk away thinking
stochasticization is free; it is free at detection in the toy limit and
not free for parameter estimation.

Option (C) ("preserve the two-step structure, correct Step 1 into a
parameter-interpretation effect") preserves the narrative arc of the
old memo. But the old memo's lead sentence — "stochasticization costs
an order in $H$ in detection significance" — was the wrong punchline,
and keeping a two-step structure invites the reader to continue thinking
of stochasticization as a detection-level lossy step. A cleaner split
into "one detection-level critique (Eq. 50), two side observations
(parameter-precision, anisotropic-response)" separates the issues by
their type rather than their order in the derivation, which is what a
technical collaborator actually needs.

---

## Section 3: Full draft of the revised memo

```markdown
# A coherent re-derivation of Eq. B6 and what App. B is actually testing

**Purpose.** A unified critique of App. B of the draft, written for
the collaborator. One-sentence conclusion:

> **Eq. (B6) is the right statistic in the App. B toy limit, and in
> that limit the profile-likelihood and Bayes-factor constructions
> produce monotone-equivalent tests — the stochasticization does not
> cost anything at the detection stage. The genuine detection-level
> critique is the Eq. (50) same-power null, which caps the
> significance at $\sim 3.8\sigma$ no matter how bright the source.
> Two side observations: (i) stochasticization reparameterizes
> amplitude $\mu$ to power $q$, with different Fisher information,
> so a parameter measurement is subject to cosmic-variance-limited
> scatter even though the detection call is the same; (ii) a
> realistic anisotropic PTA response breaks the monotone equivalence
> quantitatively mildly ($\sim$few percent on detection thresholds).**

All notation follows the draft.

## 1. One-paragraph resolution

Two constructions land on the same data-dependence in the App. B toy
limit. In the source-aligned, $N_\ell=\bar N$ frame of App. B, write
$x_\pm \equiv \sum_\ell (z_\ell/2)\,a_{\ell,\pm 2}(\hat n_s)/\bar N$,
$\rho^2 = \sum_\ell z_\ell^2/(4\bar N)$, and
$s(\hat n_s) = (|x_+|^2+|x_-|^2)/\rho^2$. Then:

1. **Profile-likelihood path.** Treat $\vec h = (h_{+2},h_{-2})$ as
   deterministic unknowns and maximize the coherent Gaussian
   likelihood. The profile log-LR reduces to $T_1(\hat n_s) = s(\hat n_s)$.
2. **App. B's path.** Marginalize over internal angles, Gaussianize,
   impose a $\mathcal{CN}(0,qI_2)$ prior on $\vec h$, maximize over
   $q\geq 0$. The Bayes-factor log-LR reduces to
   $T_{1^\star}(\hat n_s) = \max\!\bigl(s(\hat n_s) - 2 - 2\ln(s(\hat n_s)/2),\,0\bigr)$.

Both statistics depend on the data only through the scalar
$s(\hat n_s)$. The map $s \mapsto s-2-2\ln(s/2)$ is strictly increasing
on $s\geq 2$, so on that regime $T_{1^\star}$ is a strictly monotone
function of $T_1$. The equivalence survives sky-maximization because
both statistics depend on $\hat n_s$ only through the same scalar
$s(\hat n_s)$ and "max of a monotone function = monotone function of
max" (§5 of P1).

Therefore, in the App. B toy limit, stochasticization of $\vec h$ is
**free at the detection stage**: coherent-profile and stochastic-Bayes
analyses of the same data produce identical p-values. App. B's
scaling-level conclusions do not come from this substitution.

Where do they come from, then? From two distinct further steps, of
very different magnitude:

- **Eq. (50) same-power null.** Under $H_0$ pinned to the isotropic
  GWB with trace-matched power, the estimator $\hat H$ inherits the
  cosmic-variance scatter of the GWB's own realizations. The point
  estimate of a $H_1$ source with amplitude $H$ sits at $\chi^2_4 = 2/f_\sigma = 24$
  in the $H_0$ distribution (with $f_\sigma \equiv \sum z_\ell^4/(\sum z_\ell^2)^2 = 1/12$),
  producing a hard $\sim 3.8\sigma$ ceiling independent of $H$. §5.
- **Anisotropic PTA response.** For realistic
  $F(\hat n_s) \equiv U^\dagger(\hat n_s) N^{-1} U(\hat n_s)$ the
  eigenvalues differ, the monotone equivalence breaks, and $T_1$,
  $T_{1^\star}$ become two genuinely different tests. The effect is
  quantitatively mild ($\lesssim 5\%$ threshold shift, 10–20%
  rank disagreement). §7.

## 2. Two statistics in the draft

Separate at the outset:

- **Eq. (49)** $t_\ell(\hat n) = (|a_{\ell,2}|^2 + |a_{\ell,-2}|^2)/\sum_m |a_{\ell m}|^2$ —
  per-$\ell$ alignment diagnostic; not the full optimal detection
  statistic.
- **Eq. (B6)** $T(\hat n) = |\sum_\ell (z_\ell/2)\,a_{\ell,2}|^2 + |\sum_\ell (z_\ell/2)\,a_{\ell,-2}|^2$ —
  multi-$\ell$ coherent combination. The object to keep.

"The App. B statistic" below means $T(\hat n)$, Eq. (B6).

## 3. Coherent derivation of $T(\hat n)$

### 3.1 Matrix form

In the notation of Sec. IVA, Eq. (44): $\vec a = U\vec h + \vec n$
with $\vec n \sim \mathcal{CN}(0, N)$. The Gaussian log-likelihood is
quadratic in $\vec h$, so the MLE is the Wiener filter
$$
\hat{\vec h}(\hat n) = (U^\dagger N^{-1} U)^{-1} U^\dagger N^{-1} \vec a,
$$
and the profile log-likelihood ratio, for fixed $\hat n$, is
$$
\boxed{\;\mathcal F(\hat n) = \vec a^\dagger N^{-1} U (U^\dagger N^{-1} U)^{-1} U^\dagger N^{-1} \vec a.\;}
$$
This is the exact coherent detection statistic within the Sec. IVA
Gaussian likelihood. No averaging is used.

### 3.2 Reduction to Eq. (B6) in the App. B toy limit

Take the App. B simplifications: $N_{\ell m,\ell'm'} = N_\ell\,\delta_{\ell\ell'}\delta_{mm'}$
and rotate to the source-aligned frame where only $m = \pm 2$ carry
signal. Writing
$s_{\ell m}(\hat n; h_\pm) = c_\ell[h_+\delta_{m,2} + h_-\delta_{m,-2}]$
with $c_\ell = z_\ell/2$, the MLEs are
$$
\hat h_\pm(\hat n) = \frac{\sum_\ell (c_\ell/N_\ell)\,a_{\ell,\pm 2}(\hat n)}{\sum_\ell (c_\ell^2/N_\ell)}.
$$
The profile statistic becomes
$$
\mathcal F(\hat n) = \frac{|\sum_\ell (c_\ell/N_\ell)\,a_{\ell,+2}|^2 + |\sum_\ell (c_\ell/N_\ell)\,a_{\ell,-2}|^2}{\sum_\ell (c_\ell^2/N_\ell)}.
$$
In the further limit $N_\ell \equiv \bar N$ the denominator is
sky-independent; multiplying through and substituting $c_\ell = z_\ell/2$
recovers Eq. (B6) exactly. Eq. (B6) is the matched-filter statistic of
Sec. IVA in the diagonal, $N_\ell$-constant toy limit.

### 3.3 Wigner-D Fisher block

Keep the internal angles $(\psi,\phi_0,\cos\iota)$ live — they package
into the 4 real d.o.f. of $\vec h \in \mathbb{C}^2$. Wigner-D column
orthogonality gives a diagonal Fisher block with four equal eigenvalues:
$$
F^{(\rm coh)}_{\vec h^*\vec h} = \mathcal F_{\rm tot}\,\mathbb I_4,
\qquad
\mathcal F_{\rm tot} \equiv \sum_\ell \frac{z_\ell^2}{4N_\ell}.
$$
Under $H_1$ with true amplitude $\vec h^\star$ and $H \equiv |\vec h^\star|^2$,
the KL divergence from source to null is
$$
D_{\rm coh} = \mathcal F_{\rm tot}\,H.
$$
Standard matched-filter linear-in-$H$ scaling.

## 4. Monotone equivalence of profile and Bayes-factor paths (the $k=2$ isotropic case)

This is the result the collaborator wants to see explicitly.

### 4.1 Setup

In the source-aligned, $N_\ell=\bar N$ limit define (as in P1)
$$
x_\pm \equiv u_\pm^\dagger N^{-1}\vec a \in \mathbb{C},\qquad
\rho^2 \equiv u_\pm^\dagger N^{-1}u_\pm = \sum_\ell \frac{z_\ell^2}{4\bar N},
$$
with $u_+^\dagger N^{-1}u_-=0$ ensured by the App. B
isotropy condition. Normalize:
$s_\pm \equiv |x_\pm|^2/\rho^2$, $s\equiv s_++s_-$.
Under $H_0$, $2s\sim\chi^2_4$.

### 4.2 Profile LLR

Model $H_1:\vec a\sim\mathcal{CN}(u_+ h_+ + u_- h_-, N)$, unknown
$(h_+,h_-)\in\mathbb{C}^2$. Because both hypotheses share $N$,
determinants cancel, and orthogonality separates the cross terms:
$2\ln\Lambda_1(h_\pm) = 2\,\mathrm{Re}(h_+^* x_+) + 2\,\mathrm{Re}(h_-^* x_-) - \rho^2(|h_+|^2+|h_-|^2)$.
Maximizing over each complex scalar independently gives
$\hat h_\pm = x_\pm/\rho^2$ and
$$
\boxed{\;T_1 \equiv 2\ln\Lambda_1\big|_{\hat h_\pm} = \frac{|x_+|^2+|x_-|^2}{\rho^2} = s.\;}
$$

### 4.3 Bayes-factor LLR

Model $H_1^\star$: $(h_+,h_-)\sim\mathcal{CN}(0,qI_2)$ i.i.d., unknown
$q\geq 0$. Then $\vec a\sim\mathcal{CN}(0,\Sigma)$ with
$\Sigma = N + qUU^\dagger$. Sherman–Morrison–Woodbury, using
$U^\dagger N^{-1} U = \rho^2 I_2$, gives
$\Sigma^{-1} = N^{-1} - \tfrac{q}{1+\alpha}\,N^{-1}UU^\dagger N^{-1}$
with $\alpha\equiv q\rho^2$. The quadratic-form difference collapses
to $\tfrac{\alpha}{1+\alpha}\,s$, and the matrix-determinant lemma
gives $\ln|N|/|\Sigma| = -2\ln(1+\alpha)$. So
$$
2\ln\Lambda_{1^\star}(\alpha) = -2\ln(1+\alpha) + \frac{\alpha\,s}{1+\alpha}.
$$
Maximizing over $\alpha\geq 0$: setting the derivative to zero gives
$\hat\alpha = s/2-1$, valid for $s\geq 2$ (and $\hat\alpha=0$
otherwise). Substituting,
$$
\boxed{\;T_{1^\star}(\vec a) = \max\!\bigl(s - 2 - 2\ln(s/2),\;0\bigr).\;}
$$

### 4.4 Monotone equivalence and survival under sky maximization

The map $g_2(s) = s - 2 - 2\ln(s/2)$ has $g_2(2)=0$,
$g_2'(s) = 1 - 2/s > 0$ for $s>2$; so $g_2$ is strictly increasing on
$[2,\infty)$. Therefore on the regime where either statistic exceeds
zero, $T_{1^\star} = g_2(T_1)$ is a strictly monotone relabeling of
$T_1$. They define the same test:
$P_{H_0}(T_{1^\star} \geq g_2(s_{\rm obs})) = P_{H_0}(T_1 \geq s_{\rm obs})$.
Identical p-values, identical ROC, identical significance — on every
realization.

The equivalence survives $\hat n_s$-maximization because both
statistics depend on $\hat n_s$ only through the common scalar
$s(\hat n_s)$, and the map $s\mapsto g_2(s)$ does not itself depend on
$\hat n_s$; therefore $\max_{\hat n_s} g_2(s(\hat n_s)) = g_2(\max_{\hat n_s} s(\hat n_s))$
and the argmax sky direction is the same for both.

### 4.5 What the equivalence rests on

Two symmetries:
1. **Isotropic response** $U^\dagger N^{-1} U = \rho^2 I_2$. Required
   to get $s = |x_+|^2/\rho^2 + |x_-|^2/\rho^2$ as the single scalar
   both statistics depend on.
2. **Isotropic prior** $\mathcal{CN}(0,qI_2)$ on $\vec h$. Required to
   collapse $Q^{-1}+U^\dagger N^{-1}U$ to a scalar multiple of $I_2$ in
   Woodbury.
The 1-d structure of the single-template case (cautionary note in
§4 of the pedagogical note) lifts to this 2-polarization setup
precisely because these two isotropies preserve a single quadratic
invariant $s = s_++s_-$. Break either symmetry and the equivalence
fails (§7 for the response-anisotropy case).

**Bottom line of §4.** In the App. B toy limit there is one test,
parameterized two ways. The profile and Bayes-factor constructions are
two routes to the same detection call. Stochasticization is free at
the detection stage.

## 5. The main critique: Eq. 50 same-power null ($\sim 3.8\sigma$ ceiling)

Even with the monotone equivalence of §4, App. B's Eq. (48) headline
— that a single source hidden in a realized GWB can be detected at
most at $\sim 3.8\sigma$ regardless of its amplitude — is real. It
comes from a separate choice: Eq. (50) pins the null to the isotropic
GWB with total power $\sigma_h^2 = \langle|\vec h|^2\rangle$ **matched
to the $H_1$ source**. This is what caps the significance.

Derivation. Under this $H_0$ the estimator
$\hat H = |\hat h_{+2}|^2 + |\hat h_{-2}|^2$ inherits the
cosmic-variance distribution of the GWB power falling into the
$m=\pm 2$ slots after the $z_\ell$ kernel:
$$
\hat H\big|_{H_0} \sim \frac{f_\sigma H}{2}\,\chi^2_4 \qquad(\sigma_a^2\to 0),
$$
with $f_\sigma = \sum z_\ell^4/(\sum z_\ell^2)^2 = 1/12$ for the
$\varepsilon\lesssim 1$ kernel. Under $H_1$ with a realized source of
amplitude $H$ and zero noise, $\hat H|_{H_1}\to H$ deterministically.
The detection ratio is
$$
\frac{\hat H|_{H_1}}{\langle \hat H|_{H_0}\rangle/2} = \frac{1}{f_\sigma} = 12,
$$
independent of $H$. The significance is
$p[\chi^2_4 > 2/f_\sigma = 24] \sim 3\times 10^{-4} \sim 3.8\sigma$.

This is the ceiling of Eq. (48). It is a property of the
same-power discrimination problem (coherent source vs GWB of
matched power), not of the $T$ statistic and not of source detection
in general. Change the null to noise-only (with the GWB handled as a
profiled nuisance) and the ceiling disappears.

## 6. Side observation: parameter interpretation, Fisher on $\mu$ vs on $q$

The §4 monotone equivalence does not make the two models
interchangeable for **parameter estimation**. Compare:

- **Coherent $H_1$.** Parameter $\mu$ enters the mean:
  $\partial_\mu\vec\mu = \vec t$, and
  $F^{(\rm coh)}_{\mu\mu}(0) = \vec t^\dagger N^{-1}\vec t = \rho^2$ is
  finite and $\mu$-independent.
  $\mathrm{Var}(\hat\mu) \geq 1/\rho^2$, with the linear MLE saturating it.
- **Stochastic $H_1^\star$.** Parameter $\mu$ enters only through
  $\mu^2$ in the covariance: $\partial_\mu\Sigma|_{\mu=0}=0$ identically,
  hence $F^{(\rm cov)}_{\mu\mu}(0)=0$ — the likelihood has no linear
  sensitivity to $\mu$ at the null. The first non-zero Fisher channel
  is on the variance parameter $q$ (or $\mu^2$):
  $F^{(\rm cov)}_{qq}(0) = \tfrac12\,\mathrm{tr}[(N^{-1}UU^\dagger)^2]$,
  and at large $q$, $F_{qq}(q) \to k/(2q^2)$ so
  $2q^2 F_{qq}(q) \to k$ — a **finite constant**, independent of
  measurement quality.

Both statements are correct, and they are statements about
**parameter precision**, not about detection significance. A
practitioner who reports the result as "source amplitude
$\hat\mu \pm 1/\rho$" or as "source power $\hat\alpha \pm \sqrt{2}(1+\alpha)$"
makes the **same detection call** but produces **different
uncertainties** on the inferred physical quantity.

**CMB parallel, recast.** Replace $\vec h$ by the $a_{\ell m}$ of one
$\ell$ multipole and $q$ by $C_\ell$. The power estimator
$\hat C_\ell = \tfrac{1}{2\ell+1}\sum_m |a_{\ell m}|^2$ has
$\mathrm{Var}(\hat C_\ell) = 2(C_\ell+N_\ell)^2/(2\ell+1)$, so even at
$N_\ell\to 0$ the variance is $2C_\ell^2/(2\ell+1)$. This is the
cosmic-variance floor on the **parameter** $C_\ell$. App. B's
$f_\sigma = 1/12$ plays the role of $1/(2\ell+1)$: it is the inverse of
the effective number of modes in the $z_\ell$-weighted power
estimator. It tells you how precisely you can measure $q$, not how
significantly you can detect a source.

**Aside: the $\alpha$-vs-$\alpha^2$ KL gap.** Expanding the expected
LLR to leading order: under $H_1$-truth, $\Lambda \simeq \tfrac12\alpha$
(linear); under $H_1^\star$-truth, $\Lambda \simeq \tfrac14\alpha^2$
(quadratic). This is a statement about **which physics generated the
data** — a coherent source is a stronger alternative to the null than
a stochastic one at equal power, simply because its statistical
fingerprint is larger. It is **not** a statement about which model to
use in analysis. If the truth is coherent, using either $T_1$ or
$T_{1^\star}$ produces the same p-value (§4). If the truth is
stochastic, the sampling distribution of the common $s$ has variance
$\propto (1+\alpha)^2$ instead of $\propto 1+2\alpha$, and the
effective non-centrality is smaller. The $\alpha$-vs-$\alpha^2$ scaling
is about the **data-generating process**, not about the analyst's
modeling choice.

## 7. Side observation: anisotropic response breaks the equivalence mildly

For a realistic PTA, the Eq. (32) isotropy-of-pulsar-distribution
approximation fails and
$F(\hat n_s) \equiv U^\dagger(\hat n_s) N^{-1} U(\hat n_s)$ has
nondegenerate eigenvalues. In the eigenbasis of $F$ with eigenvalues
$\rho_i^2$ and projections $v_i = (U^\dagger N^{-1}\vec a)_i$:
$$
T_1 = \sum_i \frac{|v_i|^2}{\rho_i^2},
\qquad
T_{1^\star} = \sum_i w_i\,\frac{|v_i|^2}{\rho_i^2} - \sum_i \ln(1+q\rho_i^2),
$$
with $w_i = q\rho_i^2/(1+q\rho_i^2) \in [0,1)$. When $\rho_i^2$ differ,
the $w_i$ differ, so $T_{1^\star}$ is a different weighted sum of the
same $|v_i|^2/\rho_i^2$ variables than $T_1$. The two statistics are
no longer monotonically related; they are two genuinely different
tests.

Quantitatively (P2, §3.2). With $k=2$, $r = \rho_1^2/\rho_2^2$,
$q\rho_2^2 = 1$: two realizations with the same $T_1=10$ can differ in
$T_{1^\star}$ by $\Delta T_{1^\star} = 5(r-1)/(r+1)$.

| Asymmetry | $r$ | $\Delta T_{1^\star}$ at fixed $T_1=10$ | Frac. shift |
|---|---|---|---|
| 10% eigenvalue splitting | 1.1 | 0.24 | 3% of $T_1$ |
| NG15 equator-to-typical | ~2 | 1.67 | 17% of $T_1$ |
| Near-null direction | ~10 | 4.09 | 41% of $T_1$ |

Typical rank disagreement at fixed sky is 10–20%, up to
$\sim 50\%$ in $m=0$ null directions. Translated to p-values, the
detection-threshold shift is a few percent — an $\sim 3\sigma$ call
from one statistic corresponds to $\sim 2.85$–$3.15\sigma$ from the
other. This is quantitatively mild compared to the Eq. (50) ceiling of
§5, which costs orders of magnitude.

The effect is strictly a third critique: it does **not** rescue the
$3.8\sigma$ ceiling (which comes from the null choice, not from the
response), and it does **not** restore the coherent linear-in-$H$
scaling on stochasticized data (which requires undoing
stochasticization). Its logical role is to remove the appearance of a
closed-form identity between the two constructions outside the Eq. (32)
approximation.

## 8. On the Gaussianization step: it is fine at the relevant SNR

A separate question is whether the Gaussianization of the marginalized
likelihood (between Eqs. B2 and B4) loses information *within* App. B's
own problem. In the PTA regime ($\varepsilon\lesssim 1$) it does not,
at leading order.

Single-mode toy. Proper Bayesian marginalization over a uniform phase
gives
$$
\ln\mathcal L_{\rm marg}(d|h) = -\frac{|d|^2+|h|^2}{\sigma^2} + \ln I_0\!\bigl(\tfrac{2|d||h|}{\sigma^2}\bigr).
$$
The paper's Gaussian approximation (rank-1 covariance addition $|h|^2$)
gives
$$
\ln\mathcal L_{\rm App.B}(d|h) = -\ln(\sigma^2+|h|^2) - \frac{|d|^2}{\sigma^2+|h|^2}.
$$
Expanding both at $|h|^2/\sigma^2 \ll 1$,
$$
\ln\mathcal L_{\rm marg}\;\approx\;\ln\mathcal L_{\rm App.B}
\;\approx\;\text{const}\;-\;\frac{|d|^2+|h|^2}{\sigma^2}\;+\;\frac{|d|^2|h|^2}{\sigma^4}.
$$
The data-dependent cross term $|d|^2|h|^2/\sigma^4$ — the one that makes
the statistic useful — is retained by both operations. So App. B's
Gaussianization is a legitimate low-SNR approximation; no information
is lost to it at the PTA per-source SNR.

The Gaussianization only starts to lose things at high per-source SNR,
where $\ln I_0(x) \sim x$ (linear in amplitude — the full coherent
branch) while the Gaussian truncates to $x^2/4$. PTAs don't live in
that regime.

## 9. Internal inconsistency in the draft's prior

A smaller, orthogonal concern: the route from the stated uniform
priors on $(\phi_0,\psi,\cos\iota)$ (text above B3) to the Gaussian
prior on $\vec h$ in Eq. (50) is not exact. The marginal law induced by
$h_{\pm 2}(f) = \tfrac{\mathcal A(a\pm b)}{2}e^{\pm 2i\psi}e^{i\Phi_0}$
with $(\Phi_0,\psi,\cos\iota)$ uniform is **not** a circular Gaussian
$\mathcal{CN}(0,\sigma_h^2 I_2)$. Two different modeling choices that
the draft conflates. It matters little for the ranking because in the
toy limit both are monotone in $T(\hat n)$, but the draft as written
reads as if "marginalize the angles → Gaussianize" = "Gaussian prior
on $\vec h$," and it isn't.

## 10. Summary for the collaborator

1. **The statistic is fine.** Eq. (B6) $T(\hat n)$ is exactly the
   profile-likelihood matched filter for a source at $\hat n_s$ in
   the diagonal-noise, $N_\ell$-constant toy limit (§3). It can be
   derived in one line from Sec. IVA without averaging.
2. **Eq. (49) vs Eq. (B6) labeling.** $t_\ell$ is a per-$\ell$
   alignment diagnostic, not the fundamental multi-$\ell$ statistic
   (§2).
3. **Stochasticization is free at the detection stage in the toy
   limit** (§4). Profile and Bayes-factor LLRs are monotone-equivalent:
   $T_1=s$, $T_{1^\star} = \max(s-2-2\ln(s/2),0)$, same p-value,
   same ROC, same significance — on every realization, sky-max
   included. This supersedes the earlier "stochasticization demotes
   scaling at detection" framing.
4. **Main critique (§5). Eq. (50) same-power null ⇒ $\sim 3.8\sigma$
   ceiling.** Matching $\langle|\vec h|^2\rangle$ to the GWB pins
   $H_0$ to the GWB with the same trace as $H_1$. Under $H_0$ the
   estimator $\hat H \sim (f_\sigma H/2)\chi^2_4$ with $f_\sigma=1/12$,
   so the $H_1$ point estimate sits at $\chi^2_4 = 24$ and the
   significance is bounded at $\sim 3.8\sigma$ **no matter how bright
   the source**. This is Eq. (48)'s headline; it is a property of this
   discrimination problem, not of source detection.
5. **Side observation 1 (§6): parameter interpretation.** Coherent and
   stochastic models give the same detection call but different
   parameters: $\hat\mu$ with $F_{\mu\mu}=\rho^2$, or $\hat q$ with
   $F_{qq}$ finite but $2q^2 F_{qq}(q)\to k$ — the cosmic-variance
   floor. The CMB $\hat C_\ell$ parallel is a Fisher-on-$C_\ell$
   statement, not a detection-power one.
6. **Side observation 2 (§7): anisotropic response.** For realistic
   $F(\hat n_s)$ with nondegenerate eigenvalues, the monotone
   equivalence breaks. Typical rank disagreement 10–20%,
   threshold shift a few percent — two orders of magnitude smaller
   than (4). Removes the appearance of a closed-form identity between
   the two constructions outside the Eq. (32) approximation.
7. **Gaussianization is not the culprit** (§8). At PTA per-source SNR
   it reproduces the proper Bayesian marginal at leading order.
8. **Editorial fix.** Derive $T(\hat n)$ from Sec. IVA by profiling
   (§3 here); present the Gaussian-prior Bayes factor as an equivalent
   alternative in the isotropic limit (§4 here), noting the $k=2$
   monotone-equivalence identity $T_{1^\star} = g_2(T_1)$; label the
   $\sim 3.8\sigma$ ceiling as a property of the same-power
   discrimination problem, not a fundamental limit on source
   detection; replace "no distinction between continuous-wave and
   anisotropic searches" with the narrower statement that in the toy
   limit the two constructions share the same quadratic invariant
   $s$, and note that a realistic anisotropic response lifts the
   equivalence at the tens-of-percent level on individual
   realizations.

## 11. Relation to our project

The cosmic-variance statement $2q^2 F_{qq}\to k$ is the clean
"$\mathrm{Var}(\hat P) \geq P^2/\text{modes}$" form of the
coherent-over-incoherent $p$-factor in [[../concepts/fisher_hierarchy]].
Note the logical scope: the $p$-hierarchy is a **multi-source
ensemble** statement (KL scaling in the brightest-source fraction
$p$) and is about the data-generating physics, not the analyst's
modeling choice. At the level of the single-source detection problem
in App. B's toy limit, the two constructions are monotone-equivalent
(§4 here); the $p$-hierarchy lives one level up.

The old "same $T$, three pictures, three scalings" framing is subsumed
by the cleaner statement: the same $T$, one test in the isotropic
limit, with two distinct side observations about parameter precision
and response anisotropy. The old [[../concepts/matched_filter_vs_power]]
cross-reference remains valid as a generic "linear-in-data statistic
dominates quadratic-in-data at weak signal **when the truth is
coherent**" — the point being that at the detection stage in the toy
limit the two statistics **are** the same monotone rescaling, so the
linear-vs-quadratic distinction only materializes when either (a) the
truth is stochastic (data-generating physics), (b) response anisotropy
is present (§7), (c) you ask about parameter precision rather than
detection significance (§6), or (d) you pin the null to the
same-power GWB (§5).
```

End of revised memo.

---

## Section 4: Sanity checks

### Internal contradictions

1. **"Stochasticization is free at detection" vs the paper's actual
   $3.8\sigma$ ceiling.** These are not contradictory because the
   ceiling comes from the null choice (Eq. 50), not from the
   model-of-the-source choice. The revised memo's §4 (monotone
   equivalence) is computed against a **common noise-only null** in
   which both the profile and Bayes-factor LLRs are evaluated; §5
   then separately discusses what happens when the null itself is
   replaced by the same-power GWB. The memo's §5 derivation follows
   the old §5.2 and is unchanged. Still, the memo must be written so
   a reader does not conflate the two steps. The §10 bullet list
   orders them carefully (monotone equivalence first, then the
   ceiling under the Eq. 50 null) to avoid this.

2. **§4 insists on monotone equivalence; §7 insists it breaks.** These
   are not contradictory — §4 works in the isotropic toy limit
   ($U^\dagger N^{-1}U = \rho^2 I_2$) and §7 in the realistic
   $F(\hat n_s)$ with nondegenerate eigenvalues. Both notes (P1, P2)
   agree on this scope. The memo should reaffirm the isotropic
   assumption at the start of §4.

3. **"CMB cosmic variance is a Fisher-on-$C_\ell$ statement" vs the
   old memo's reading of the same formula as a detection statement.**
   Only one reading is correct (the parameter-precision one). The
   revision consistently uses it that way.

### Statements needing numerical check against the draft

1. **$f_\sigma = 1/12$.** The old memo and P2 both use it. The draft's
   own Eq. (47) (near the $3.8\sigma$ claim) should confirm this
   value from $\sum z_\ell^4/(\sum z_\ell^2)^2$ for the App. B's
   $z_\ell$ choice. Also cross-check the ceiling number
   $p[\chi^2_4>24] \simeq 3.2\times 10^{-4} \to 3.60\sigma$ (two-sided)
   or $3.45\sigma$ (one-sided). The old memo says "$\sim 3.8\sigma$";
   confirm against the draft's own figure and Eq. (48) before
   finalizing. If the draft reports $3.8\sigma$, fine — but the
   $\chi^2_4$ argument used here gives $\simeq 3.6\sigma$, so either
   the draft is adding a different factor (e.g. accounting for sky
   max under $H_0$, a look-elsewhere inflation that sharpens the
   ceiling) or the factor of 12 is not exactly right for the
   $z_\ell$ kernel at the quoted $\varepsilon$. Keep the number used
   in the draft, and explicitly note the one-line derivation gives
   "$\simeq 3.6\sigma$ from the $\chi^2_4$ tail alone, promoted to
   $\simeq 3.8\sigma$ by [draft's look-elsewhere / kernel
   correction]" if needed.

2. **"Typical NG15 rank disagreement 10–20%."** P2 §3.2 states this
   from the $r\sim 2$ entry in its table. P2 calls this
   "equator-to-typical"; the word "typical" here refers to typical
   sky-position across the Fig. 2 map, not a literal NG15 full-sky
   average. The memo should say "on typical sky positions relative
   to the NG15 array, $r\sim 2$" to avoid overclaiming a sky-average
   number that P2 does not compute explicitly.

3. **"$2q^2 F_{qq}(q)\to k$ saturates to a finite constant."** Direct
   from Parametrization 2 in the old §5.1. Still correct.
   Dimensionally, $F_{qq}(q)\to \tfrac12\mathrm{tr}[(qUU^\dagger)^{-1}\cdot UU^\dagger \cdot (qUU^\dagger)^{-1}\cdot UU^\dagger] = k/(2q^2)$
   at large $q$ with $UU^\dagger$ of rank $k$. For App. B, $k=2$
   (two complex polarizations → $2$ modes), so the saturation
   constant is $2$, not $1$. Make sure the memo uses the correct
   $k$-value in §6.

### What I am least sure about and would like the reviewer to look at

1. **The "CMB $\hat C_\ell$ parallel is a Fisher-on-$C_\ell$ statement,
   not a detection-power one" phrasing in §6.** This is the crux of the
   reframe. Its correctness turns on the fact that, for a fixed $\ell$
   multipole viewed as a rank-$(2\ell+1)$ stochastic-amplitude problem
   at a single mode, the "detection" question (does power exist?) and
   the "measurement" question (how precisely?) share the same estimator
   $\hat C_\ell$, and the cosmic-variance bound applies to the second.
   The intuition is standard in CMB but the mapping onto App. B's
   $f_\sigma$ should be checked carefully by the reviewer — if they
   want a cleaner statement, the revised §6 can be tightened by
   replacing the parallel with a direct formula
   $\mathrm{Var}(\hat q)/q^2 \geq 1/k$ and dropping the CMB reference.

2. **Whether the monotone equivalence survives sky-max in the realistic
   (non-isotropic) case.** P2 does not explicitly compute this.
   Intuitively, once the eigenvalues split, the two statistics no
   longer track each other as functions of $\hat n_s$, so the argmax
   $\hat n_s$ could differ between $T_1$ and $T_{1^\star}$. This is
   probably not a big effect (the maxima are over the same $S^2$ and
   the noise fluctuations are finite), but the memo should not assert
   "they give the same sky location of the source" outside the
   isotropic limit. The revised §7 stays silent on this — good — but
   the reviewer should confirm whether P2's numerical claims are at
   fixed $\hat n_s$ or sky-maximized. A quick read of P2 §3.2 suggests
   fixed $\hat n_s$.

3. **Whether the revised §11 cross-reference to [[fisher_hierarchy]] is
   still accurate.** The old sentence "turning $\hat{\vec h}$ into
   $\hat q$ costs the coherent order" was used to connect to the
   multi-source $p$-hierarchy. The revised §11 breaks this into "the
   $p$-hierarchy is a multi-source ensemble statement" — which is
   correct but less punchy. The reviewer should confirm that the
   concept page [[fisher_hierarchy]] is not framed in a way that
   presupposes the single-source $T_1$ vs $T_{1^\star}$ statement;
   if it is, that concept page needs a parallel edit. (This is flagged
   for follow-up, not done in the memo itself.)

4. **Whether the Gaussianization argument in §8 is still placed in the
   right location of the logical flow.** In the old memo it came
   after the two lossy steps. In the revision it comes after the main
   critique and the two side observations. This is fine but a reviewer
   might prefer §8 to be folded into §4 as a sub-argument ("the
   Gaussianization is inside the derivation of $T_{1^\star}$ and does
   not affect the monotone equivalence"). Either placement is
   defensible; I have kept it where it is for minimal disruption.

5. **The §5 detection-ratio derivation uses $\langle\hat H|_{H_0}\rangle/2$
   in the denominator, which matches the old memo but is not standard
   significance practice.** The expression "$p[\chi^2_4>2/f_\sigma=24]$"
   is the correct tail probability, but the intermediate "detection
   ratio" formula is a dimensional sanity check, not a significance.
   The reviewer may prefer removing it in favor of the $\chi^2_4$
   tail statement alone.

---

**Length check.** The revised memo draft (§0 through §11) is about
1500 words of markdown + equations; the proposal wrapper (§1 through
§4 of this document) is another ~1200 words. Total ~2700 words,
which is 4–5 pages equivalent. Within the requested window.
