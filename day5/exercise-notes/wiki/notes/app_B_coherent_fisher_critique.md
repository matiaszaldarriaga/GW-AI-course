# A coherent re-derivation of Eq. B6 and what App. B is actually testing

**Purpose.** A unified critique of App. B of the draft, written for
the collaborator. One-sentence conclusion:

> **Eq. (B6) is the right statistic in the App. B toy limit, and in
> that toy limit the profile-likelihood and Bayes-factor constructions
> produce monotone-equivalent tests — stochasticization of $\vec h$ is
> free at the detection stage in that limit. The single scaling-level
> critique is the Eq. (50) same-power null, which caps the significance
> at $\sim 3.8\sigma$ no matter how bright the source. Two side
> observations: (i) stochasticization reparameterizes amplitude $\mu$
> to power $q$ with different Fisher information, so a parameter
> measurement is subject to cosmic-variance-limited scatter even
> though the detection call is the same; (ii) a realistic anisotropic
> PTA response breaks the monotone equivalence quantitatively mildly
> ($\sim$few percent on detection thresholds).**

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
function of $T_1$. In the App. B toy limit the equivalence survives
sky-maximization because both statistics depend on $\hat n_s$ only
through the same scalar $s(\hat n_s)$ and "max of a monotone function =
monotone function of max."

Therefore, in the App. B toy limit, stochasticization of $\vec h$ is
**free at the detection stage**: coherent-profile and stochastic-Bayes
analyses of the same data produce identical p-values. App. B's
scaling-level conclusions do not come from this substitution.

Where do they come from, then? From two distinct further steps, of
very different magnitude:

- **Eq. (50) same-power null.** Under $H_0$ pinned to the isotropic
  GWB with trace-matched power, the estimator $\hat H$ inherits the
  cosmic-variance scatter of the GWB's own realizations. The point
  estimate of a $H_1$ source with amplitude $H$ sits at
  $\chi^2_4 = 2/f_\sigma = 24$ in the $H_0$ distribution (with
  $f_\sigma \equiv \sum z_\ell^4/(\sum z_\ell^2)^2 = 1/12$),
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

In the source-aligned, $N_\ell=\bar N$ limit define
$$
x_\pm \equiv u_\pm^\dagger N^{-1}\vec a \in \mathbb{C},\qquad
\rho^2 \equiv u_\pm^\dagger N^{-1}u_\pm = \sum_\ell \frac{z_\ell^2}{4\bar N},
$$
with $u_+^\dagger N^{-1}u_-=0$ ensured by the App. B isotropy
condition. Normalize: $s_\pm \equiv |x_\pm|^2/\rho^2$, $s\equiv s_++s_-$.
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

The equivalence survives $\hat n_s$-maximization **in the isotropic
toy limit** because both statistics depend on $\hat n_s$ only through
the common scalar $s(\hat n_s)$, and the map $s\mapsto g_2(s)$ does
not itself depend on $\hat n_s$; therefore
$\max_{\hat n_s} g_2(s(\hat n_s)) = g_2(\max_{\hat n_s} s(\hat n_s))$
and the argmax sky direction is the same for both. The argmax
coincidence is a theorem **only** in the isotropic limit; in the
realistic case (§7) both $\rho^2_{1,2}(\hat n_s)$ are sky-dependent
and the map $\vec v \mapsto T_{1^\star}(\vec v)$ acquires explicit
$\hat n_s$-dependence through the eigenvalues, so the argmax sky
directions of $T_1$ and $T_{1^\star}$ can differ at the
eigenvalue-spread level.

### 4.5 What the equivalence rests on

Two symmetries:

1. **Isotropic response** $U^\dagger N^{-1} U = \rho^2 I_2$. Required
   to get $s = |x_+|^2/\rho^2 + |x_-|^2/\rho^2$ as the single scalar
   both statistics depend on.
2. **Isotropic prior** $\mathcal{CN}(0,qI_2)$ on $\vec h$. Required to
   collapse $Q^{-1}+U^\dagger N^{-1}U$ to a scalar multiple of $I_2$ in
   Woodbury.

The 1-d structure of the single-template case lifts to this
2-polarization setup precisely because these two isotropies preserve a
single quadratic invariant $s = s_++s_-$. Break either symmetry and the
equivalence fails. The empirically relevant breakdown is the
response-anisotropy one — §7. For completeness: a non-isotropic prior
$Q\neq qI_2$ would also break the equivalence (the Bayes factor would
depend on $s_+$ and $s_-$ separately rather than on $s=s_++s_-$), but
this is not a modeling concern for App. B as written since its prior
is isotropic by choice.

**Bottom line of §4.** In the App. B toy limit there is one test,
parameterized two ways. The profile and Bayes-factor constructions are
two routes to the same detection call. Stochasticization is free at
the detection stage.

## 5. The main critique: Eq. 50 same-power null ($\sim 3.8\sigma$ ceiling)

*The ceiling is a property of the choice of null, not of the choice of
statistic.*

Even with the monotone equivalence of §4, App. B's Eq. (48) headline
— that a single source hidden in a realized GWB can be detected at
most at $\sim 3.8\sigma$ regardless of its amplitude — is real. It
comes from a separate choice. The paper uses Eq. (50) as a Gaussian
prior on the source amplitudes,
$\ln\pi(\vec h|\sigma_h^2)\propto -|\vec h|^2/(2\sigma_h^2)$, and then
equates its variance $\sigma_h^2$ to the GWB power, which is
equivalent to pinning the null to the matched-power GWB in the
subsequent Neyman–Pearson comparison. That combined choice is what
caps the significance.

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
The realized $H_1$ value therefore sits at a $\chi^2_4$ tail
$$
\chi^2_4 \;=\; \frac{2\,\hat H|_{H_1}}{f_\sigma H} \;=\; \frac{2}{f_\sigma} \;=\; 24,
$$
independent of $H$. The significance is
$p[\chi^2_4 > 24] = 7.99\times 10^{-5} \sim 3.78\sigma$ one-sided, the
draft's $\sim 3.8\sigma$ ceiling.

This is the ceiling of Eq. (48). It is a property of the same-power
discrimination problem (coherent source vs GWB of matched power), not
of the $T$ statistic and not of source detection in general. Change
the null to noise-only (with the GWB handled as a profiled nuisance)
and the ceiling disappears.

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
  finite. At large $q$, $F_{qq}(q) \to k/(2q^2)$ so
  $2q^2 F_{qq}(q) \to k = 2$ for App. B (two complex polarization
  modes, 4 real d.o.f.). The saturation constant is the polarization
  mode count.

Both statements are correct, and they are statements about
**parameter precision**, not about detection significance. A
practitioner who reports the result as "source amplitude
$\hat\mu \pm 1/\rho$" or as "source power $\hat\alpha \pm \sqrt{2}(1+\alpha)$"
makes the **same detection call** but produces **different
uncertainties** on the inferred physical quantity.

**Two distinct Fisher saturations — don't conflate.** Two different
"mode counts" enter the App. B problem, and it is worth keeping them
separate:

- (a) **Polarization-mode count $k=2$**, controlling the Fisher
  saturation $2q^2 F_{qq}(q) \to k$ just above. It is a statement
  about the number of complex amplitudes being measured: two
  (for $h_{+2}, h_{-2}$).
- (b) **Kernel effective-mode count $1/f_\sigma = 12$**, controlling
  the cosmic-variance distribution of the **power estimator**
  $\hat H$ under a realized GWB: $\hat H|_{H_0} \sim (f_\sigma H/2)\chi^2_4$.
  It is a statement about how many effective harmonic modes feed the
  $z_\ell$-weighted power estimator after the HD kernel, and it is what
  appears in the §5 ceiling.

These are different objects. The polarization count (a) tells you how
precisely the variance parameter $q$ can be measured at large $q$
(§6 here). The kernel count (b) tells you how wide the null
distribution of $\hat H$ is when the null is the GWB with matched
power (§5 here). Both are Fisher/parameter-precision statements in
structure, but they appear in different places in the App. B argument.

**CMB parallel, recast.** Replace $\vec h$ by the $a_{\ell m}$ of one
$\ell$ multipole and $q$ by $C_\ell$. The power estimator
$\hat C_\ell = \tfrac{1}{2\ell+1}\sum_m |a_{\ell m}|^2$ has
$\mathrm{Var}(\hat C_\ell) = 2(C_\ell+N_\ell)^2/(2\ell+1)$, so even at
$N_\ell\to 0$ the variance is $2C_\ell^2/(2\ell+1)$. This is the
cosmic-variance floor on the **parameter** $C_\ell$. The role of
$1/(2\ell+1)$ in CMB maps to App. B's $1/f_\sigma = 12$ — the
"effective number of modes in the power estimator" count of (b) above
— not to the polarization-mode count $k=2$ of (a). The CMB parallel is
a parameter-precision statement, not a detection-power one.

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

Quantitatively. With $k=2$, $r = \rho_1^2/\rho_2^2$, $q\rho_2^2 = 1$:
two realizations with the same $T_1=10$ can differ in $T_{1^\star}$ by
$\Delta T_{1^\star} = 5(r-1)/(r+1)$.

| Asymmetry | $r$ | $\Delta T_{1^\star}$ at fixed $T_1=10$ | Frac. shift |
|---|---|---|---|
| 10% eigenvalue splitting | 1.1 | 0.24 | 3% of $T_1$ |
| Typical sky positions on NG15 array | $\sim 2$ | 1.67 | 17% of $T_1$ |
| Near-null direction ($m=0$ on $\hat n_s$) | $\sim 10$ | 4.09 | 41% of $T_1$ |

Typical rank disagreement at fixed sky is 10–20%, up to
$\sim 50\%$ in $m=0$ null directions. The rank-level disagreement is
not itself small; the smallness is specifically in the **p-value
shift**, because the null distributions of $T_1$ and $T_{1^\star}$
shift in compensating ways. A detection at $\sim 3\sigma$ from one
statistic corresponds to $\sim 2.85$–$3.15\sigma$ from the other.
This is quantitatively mild compared to the Eq. (50) ceiling of §5,
which costs orders of magnitude.

The effect is strictly a third critique: it does **not** rescue the
$\sim 3.8\sigma$ ceiling (which comes from the null choice, not from
the response), and it does **not** restore the coherent linear-in-$H$
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
   included. This supersedes any earlier "stochasticization demotes
   scaling at detection" framing.
4. **Main critique (§5). Eq. (50) same-power null $\Rightarrow \sim 3.8\sigma$
   ceiling.** Using Eq. (50) as a Gaussian prior on $\vec h$ with
   $\sigma_h^2$ matched to the GWB power pins $H_0$ to the GWB with
   the same trace as $H_1$. Under $H_0$ the estimator
   $\hat H \sim (f_\sigma H/2)\chi^2_4$ with $f_\sigma=1/12$, so the
   $H_1$ point estimate sits at $\chi^2_4 = 24$ and the significance
   is bounded at $p[\chi^2_4>24] = 7.99\times 10^{-5} \sim 3.8\sigma$
   **no matter how bright the source**. This is Eq. (48)'s headline;
   it is a property of this discrimination problem, not of source
   detection.
5. **Side observation 1 (§6): parameter interpretation.** Coherent and
   stochastic models give the same detection call but different
   parameters: $\hat\mu$ with $F_{\mu\mu}=\rho^2$, or $\hat q$ with
   $F_{qq}$ finite and $2q^2 F_{qq}(q)\to k=2$ (polarization mode
   count). The CMB $\hat C_\ell$ parallel maps $1/(2\ell+1)$ to
   App. B's $1/f_\sigma = 12$ (kernel-effective-mode count), not to
   $k=2$; the two saturations are distinct. Both are
   Fisher-on-parameter statements, not detection-power ones.
6. **Side observation 2 (§7): anisotropic response.** For realistic
   $F(\hat n_s)$ with nondegenerate eigenvalues, the monotone
   equivalence breaks. Typical rank disagreement 10–20%, threshold
   shift a few percent — two orders of magnitude smaller than (4).
   Removes the appearance of a closed-form identity between the two
   constructions outside the Eq. (32) approximation.
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
ensemble** statement (KL scaling in the brightest-source fraction $p$)
and is about the data-generating physics, not the analyst's modeling
choice. At the level of the single-source detection problem in
App. B's toy limit, the two constructions are monotone-equivalent
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
