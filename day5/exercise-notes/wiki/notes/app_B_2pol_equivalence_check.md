# 2-polarization monotone equivalence check

**Date.** 2026-04-20.

**Purpose.** Check whether the single-template monotone equivalence
$T_1 \leftrightarrow T_{1^\star}$ of
[`references/coherent_vs_stochastic_single_source.md`](../../references/coherent_vs_stochastic_single_source.md)
survives in the setting of App. B of the draft (Sato-Polito, Zaldarriaga,
Zackay 2026), which has two complex source amplitudes $h_{+2},h_{-2}$
and a sky-direction $\hat n_s$ to maximize over. We work in the App. B
isotropic toy limit ($N_{\ell m,\ell' m'}=\bar N\,\delta_{\ell\ell'}\delta_{mm'}$,
rotated source-aligned frame). Companion document:
[`wiki/notes/app_B_coherent_fisher_critique.md`](app_B_coherent_fisher_critique.md).

---

## 1. Setup

In the rotated frame, only $m=\pm 2$ carry signal. Following
§3.1 of the App. B critique note, the coherent model is $\vec a = U\vec h + \vec n$
with $\vec n\sim\mathcal{CN}(0,N)$ and $\vec h=(h_{+2},h_{-2})\in\mathbb{C}^2$.
In the two-template notation of this calculation, let $u_+$ and $u_-$
be the columns of $U$ corresponding to $h_{+2}$ and $h_{-2}$. The
App. B isotropy condition ($U^\dagger N^{-1} U \propto I_2$, §6 of the
critique note) translates to

$$
u_+^\dagger N^{-1} u_+ \;=\; u_-^\dagger N^{-1} u_- \;\equiv\;\rho^2,
\qquad u_+^\dagger N^{-1} u_- \;=\; 0.
$$

The rank-2 outer-product matrix is $M \equiv u_+ u_+^\dagger + u_- u_-^\dagger$,
so $U U^\dagger = M$. Define matched filters

$$
x_\pm \;\equiv\; u_\pm^\dagger N^{-1}\vec a
\;\in\;\mathbb{C}.
$$

Under $H_1$ ($\vec a = u_+h_+ + u_-h_- + \vec n$), using orthogonality,

$$
x_\pm \;\sim\; \mathcal{CN}(\rho^2 h_\pm,\,\rho^2).
$$

Normalized projections:

$$
s_\pm \;\equiv\; \frac{|x_\pm|^2}{\rho^2},
\qquad
s \;\equiv\; s_+ + s_-.
$$

Under $H_0$ ($\vec a\sim\mathcal{CN}(0,N)$), $x_\pm\sim\mathcal{CN}(0,\rho^2)$
are independent, so $2s_\pm\sim\chi^2_2$ (exponential) independently and
$2s\sim\chi^2_4$.

---

## 2. Profile LLR $T_1$ (coherent alternative)

Model $H_1:\;\vec a\sim\mathcal{CN}(u_+h_+ + u_-h_-,\,N)$ with
$(h_+,h_-)\in\mathbb{C}^2$ unknown. Model $H_0:\;\vec a\sim\mathcal{CN}(0,N)$.

Since both hypotheses share the covariance $N$, determinants cancel:

$$
2\ln\Lambda_1(h_+,h_-)
\;=\; \vec a^\dagger N^{-1}\vec a
- (\vec a - u_+h_+ - u_-h_-)^\dagger N^{-1}(\vec a - u_+h_+ - u_-h_-).
$$

Using the orthogonality $u_+^\dagger N^{-1} u_-=0$ and
$u_\pm^\dagger N^{-1}u_\pm=\rho^2$, the cross terms separate:

$$
2\ln\Lambda_1(h_+,h_-)
\;=\; 2\,\mathrm{Re}(h_+^* x_+) + 2\,\mathrm{Re}(h_-^* x_-)
 - \rho^2(|h_+|^2 + |h_-|^2).
$$

Maximize over each complex scalar independently:
$\partial/\partial h_\pm^*$ gives $\hat h_\pm = x_\pm / \rho^2$, and
plugging back,

$$
\boxed{\;2\ln\Lambda_1\big|_{\hat h_\pm}
= \frac{|x_+|^2 + |x_-|^2}{\rho^2}
= s_+ + s_- = s.\;}
$$

So $T_1 = s$, a function of $\vec a$ only through the sum $s$. The
individual $s_+$ and $s_-$ do not matter — only their sum. This is the
direct two-polarization generalization of §2 of the single-source note.

Under $H_0$, $T_1\sim\chi^2_4/2$ (sum of two independent exponentials).
Under $H_1$, $T_1$ is a non-central $\chi^2_4/2$ with non-centrality
parameter $\rho^2(|h_+|^2+|h_-|^2)/2$.

---

## 3. Bayes-factor LLR $T_{1^\star}$ (stochastic alternative)

Model $H_1^\star$: $(h_+,h_-)\sim\mathcal{CN}(0,qI_2)$ i.i.d. with
$q\geq 0$ unknown. The marginal data distribution is

$$
\vec a \;\sim\; \mathcal{CN}\!\bigl(0,\;\Sigma\bigr),
\qquad
\Sigma \;=\; N + q\,(u_+u_+^\dagger + u_- u_-^\dagger)
\;=\; N + qM.
$$

The log-likelihood ratio is

$$
2\ln\Lambda_{1^\star}(q)
\;=\; \ln\frac{|N|}{|\Sigma|}
 + \vec a^\dagger N^{-1}\vec a - \vec a^\dagger \Sigma^{-1}\vec a.
$$

### 3.1 Inverse via Sherman–Morrison–Woodbury

$\Sigma = N + UQU^\dagger$ with $Q = q I_2$. Woodbury gives

$$
\Sigma^{-1} \;=\; N^{-1} - N^{-1}U\bigl(Q^{-1} + U^\dagger N^{-1}U\bigr)^{-1}U^\dagger N^{-1}.
$$

Using $U^\dagger N^{-1}U = \rho^2 I_2$,

$$
\bigl(Q^{-1} + U^\dagger N^{-1}U\bigr)^{-1}
= \bigl(q^{-1}I_2 + \rho^2 I_2\bigr)^{-1}
= \frac{q}{1+q\rho^2}\,I_2
= \frac{q}{1+\alpha}\,I_2,
$$

where $\alpha\equiv q\rho^2\geq 0$. So

$$
\Sigma^{-1} = N^{-1} - \frac{q}{1+\alpha}\,N^{-1}U U^\dagger N^{-1}.
$$

The quadratic-form difference is

$$
\vec a^\dagger N^{-1}\vec a - \vec a^\dagger \Sigma^{-1}\vec a
\;=\; \frac{q}{1+\alpha}\,\vec a^\dagger N^{-1}U U^\dagger N^{-1}\vec a
\;=\; \frac{q}{1+\alpha}\,(|x_+|^2 + |x_-|^2),
$$

since $U^\dagger N^{-1}\vec a = (x_+, x_-)^T$. Divide numerator and
denominator by $\rho^2$ to rewrite in terms of $s$:

$$
\vec a^\dagger N^{-1}\vec a - \vec a^\dagger \Sigma^{-1}\vec a
\;=\; \frac{\alpha}{1+\alpha}\,s.
$$

### 3.2 Determinant via matrix determinant lemma

The generalized lemma gives

$$
|\Sigma| \;=\; |N|\cdot \bigl|\,I_2 + q U^\dagger N^{-1} U\,\bigr|
\;=\; |N|\,|I_2 + \alpha I_2|
\;=\; |N|\,(1+\alpha)^2,
$$

so

$$
\ln\frac{|N|}{|\Sigma|} \;=\; -\,2\ln(1+\alpha).
$$

### 3.3 Combined form and maximization

Assembling,

$$
2\ln\Lambda_{1^\star}(\alpha)
\;=\; -\,2\ln(1+\alpha) + \frac{\alpha}{1+\alpha}\,s.
$$

Differentiate w.r.t. $\alpha$:

$$
\frac{d}{d\alpha}\!\left[-2\ln(1+\alpha) + \frac{\alpha s}{1+\alpha}\right]
\;=\; -\frac{2}{1+\alpha} + \frac{s}{(1+\alpha)^2}
\;=\; \frac{s - 2(1+\alpha)}{(1+\alpha)^2}.
$$

Setting to zero gives

$$
\hat\alpha \;=\; \frac{s}{2} - 1, \qquad \text{valid when } s\geq 2.
$$

For $s<2$ the positivity constraint $\alpha\geq 0$ is active and the
maximum is at $\hat\alpha=0$, giving $T_{1^\star}=0$. For $s\geq 2$,
substitute $1+\hat\alpha=s/2$:

$$
2\ln\Lambda_{1^\star}\big|_{\hat\alpha}
= -2\ln(s/2) + \frac{s/2 - 1}{s/2}\,s
= -2\ln(s/2) + (s - 2).
$$

So

$$
\boxed{\;T_{1^\star}(\vec a)
\;=\;\max\!\Bigl(\,s - 2 - 2\ln(s/2),\;0\,\Bigr)
\;=\;\max\!\bigl(\,s - 2(1 + \ln(s/2)),\;0\,\bigr).\;}
$$

Sanity check: $T_{1^\star}=0$ at $s=2$ (the boundary), and its derivative
is $1 - 2/s$, which is positive for $s>2$. This is the natural two-mode
generalization of $T_{1^\star}=s-1-\ln s$ from the single-template case:
each complex template contributes "$-1 -\ln(\cdot)$" per expected degree
of freedom, and the power estimator $\hat\alpha$ subtracts **one per
template** of noise power ($s\to s-2$, not $s\to s-1$).

---

## 4. Equivalence test: do $T_1$ and $T_{1^\star}$ rank the same way?

Both statistics depend on the data **only through the scalar
$s = s_+ + s_-$**:

$$
T_1(\vec a) = s,\qquad T_{1^\star}(\vec a) = \max\!\bigl(s - 2 - 2\ln(s/2),\,0\bigr).
$$

Define $g_2(s) \equiv s - 2 - 2\ln(s/2)$ on $s\geq 2$. Then:

- $g_2(2) = 0$.
- $g_2'(s) = 1 - 2/s > 0$ for $s>2$, so $g_2$ is **strictly increasing**
  on $[2,\infty)$.
- $g_2(s)\to\infty$ as $s\to\infty$.

Therefore, in the interesting regime $s\geq 2$, $T_{1^\star}$ is a
strictly monotone function of $T_1 = s$. For any realization with
$s_{\rm obs}\geq 2$,

$$
P_{H_0}\!\bigl(T_{1^\star}\geq g_2(s_{\rm obs})\bigr)
\;=\; P_{H_0}\!\bigl(T_1 \geq s_{\rm obs}\bigr),
$$

so the two tests produce **identical p-values** and **identical
detection significance** on every realization. The profile-LLR and
Bayes-factor-LLR constructions are statistically equivalent at the
detection stage in the App. B isotropic limit.

**Key observation: $s_+$ and $s_-$ do not separately matter.**
Neither $T_1$ nor $T_{1^\star}$ distinguishes between e.g. $(s_+,s_-) = (3,0)$
and $(s_+,s_-) = (1.5,1.5)$; both see $s=3$. This is a direct consequence
of **two features working together**:

1. The template columns $u_+,u_-$ are **$N^{-1}$-orthogonal with equal
   norm** ($u_+^\dagger N^{-1} u_- = 0$, $u_\pm^\dagger N^{-1}u_\pm = \rho^2$).
   This makes $T_1 = |x_+|^2/\rho^2 + |x_-|^2/\rho^2$ already a function
   only of the sum.
2. The prior on $H_1^\star$ is **isotropic**: $(h_+,h_-)\sim\mathcal{CN}(0,qI_2)$.
   This makes $U^\dagger N^{-1}U\to \rho^2 I_2$ and $Q^{-1}+\rho^2 I_2$
   remain a scalar multiple of $I_2$ in Woodbury, collapsing the
   $2\times 2$ matrix inverse to a scalar and giving $|\Sigma|/|N|=(1+\alpha)^2$
   (scalar $\alpha$).

Drop either feature (anisotropic response or non-isotropic prior) and
the two statistics can split into separate functions of $(s_+,s_-)$, see §6.

---

## 5. Sky-direction maximization

The actual App. B statistic maximizes over sky direction. Let $\hat n_s$
run over $S^2$, and write the sky-dependent scalar as $s(\hat n_s)$,
built from the same quadratic form $s = u_+^\dagger(\hat n_s)N^{-1}\vec a u_+^{\dagger\dots}$
-- explicitly, from §3 of the App. B critique, the reduction in the
$N_\ell = \bar N$ limit gives

$$
s(\hat n_s) = \frac{|x_+(\hat n_s)|^2 + |x_-(\hat n_s)|^2}{\rho^2},
$$

with $\rho^2 = \sum_\ell z_\ell^2/(4\bar N)$ — sky-independent in this
limit. The global statistics are

$$
T_1^{\max} \;=\; \max_{\hat n_s}\, s(\hat n_s),
\qquad
T_{1^\star}^{\max} \;=\; \max_{\hat n_s}\, \max\!\bigl(g_2(s(\hat n_s)),\,0\bigr)
 \;=\; \max\!\bigl(g_2(T_1^{\max}),\,0\bigr).
$$

The last equality uses the fact that $g_2$ is **monotonically
non-decreasing** on $[0,\infty)$ (zero on $[0,2]$, strictly increasing on
$[2,\infty)$), so $\max_{\hat n_s} g_2(s(\hat n_s)) = g_2(\max_{\hat n_s} s(\hat n_s))$.

Verification: if $f$ is non-decreasing, $f(\max_i y_i)\geq f(y_j)$ for
all $j$, and equality is achieved by $j = \arg\max_i y_i$. So
$\max_i f(y_i) = f(\max_i y_i)$. This is exactly the "max of a
monotone function is the monotone function of the max" statement; it
requires genuine monotonicity (both statistics moving the same way in
$\hat n_s$), which holds here because **both statistics depend on $\hat n_s$
only through the common scalar $s(\hat n_s)$** — the sky direction does
not enter the map $s\mapsto g_2(s)$.

**Conclusion: the equivalence survives sky maximization exactly.**
$T_1^{\max}$ and $T_{1^\star}^{\max}$ are monotonically related on the
regime where either exceeds zero, and the argmax $\hat n_s$ is the same
for both.

One caveat to note for completeness: $\rho^2$ was treated as
sky-independent, which requires the $N_\ell=\bar N$ constant assumption.
If the noise spectrum is $\ell$-dependent but still diagonal, the
normalization $\sum_\ell(z_\ell^2/N_\ell)$ enters but is still
sky-independent in the rotated frame (because the rotation is along
$m$, not $\ell$). So the equivalence argument is robust to dropping
$N_\ell = \bar N$ within the diagonal-noise family, as long as the
isotropy $U^\dagger N^{-1} U \propto I_2$ is preserved.

---

## 6. Variations of the prior — where the equivalence breaks

Replace the isotropic Gaussian prior with a more general
$(h_+,h_-)\sim\mathcal{CN}(0,Q)$ for some $2\times 2$ positive $Q\neq qI_2$.
Then Woodbury gives

$$
\Sigma = N + UQU^\dagger,
\qquad
\vec a^\dagger N^{-1}\vec a - \vec a^\dagger\Sigma^{-1}\vec a
= \vec x^\dagger\bigl(Q^{-1}+\rho^2 I_2\bigr)^{-1}\vec x/\rho^2\cdot\rho^2\ldots
$$

writing it carefully: the cross term is
$\vec x^\dagger R \vec x$ with $\vec x = (x_+,x_-)^T$ and
$R = (Q^{-1}+\rho^2 I_2)^{-1}\cdot$(some factor). If $Q$ has unequal
eigenvalues, $R$ has unequal eigenvalues too, so the quadratic form
$\vec x^\dagger R\vec x$ **weights $|x_+|^2$ and $|x_-|^2$ differently**.
The Bayes-factor statistic then depends on $s_+$ and $s_-$ separately,
whereas the profile statistic $T_1=s_++s_-$ remains the isotropic sum.
The two statistics now rank data differently: a realization with
$(s_+,s_-)=(3,0)$ gives the same $T_1$ as $(s_+,s_-)=(1.5,1.5)$, but
different $T_{1^\star}$. Monotone equivalence is lost.

Likewise, if the prior is correlated between $h_+$ and $h_-$ (off-diagonal
$Q_{+-}\neq 0$), the quadratic form $\vec x^\dagger R\vec x$ mixes
$x_+$ and $x_-$ — in particular through their cross-correlation
$\mathrm{Re}(x_+^* x_-)$, which does not appear in $T_1=s_++s_-$ at all.
Again, equivalence lost.

Physically: the isotropic prior $\mathcal{CN}(0,qI_2)$ respects the same
$U(2)$ symmetry that the profile likelihood respects through its flat
treatment of $(h_+,h_-)$, and both statistics end up depending only on
the invariant $|h_+|^2+|h_-|^2$ and hence on $s$. A non-isotropic prior
breaks the symmetry and splits the two pictures apart.

This is consistent with the cautionary note in §4 of
`coherent_vs_stochastic_single_source.md`: the monotone equivalence is a
1-d feature (here, 1-d in the sense of one quadratic invariant $s$), and
it survives the two-polarization setup **only because the isotropy of
the prior keeps the problem effectively 1-d in the same invariant that
the profile likelihood sees**. Richer priors re-introduce additional
invariants, and the equivalence is lost at that point.

---

## 7. Verdict

1. **At fixed sky direction**, in the App. B isotropic toy limit,
   the profile LLR and the Bayes-factor LLR both depend on the data
   only through $s = s_+ + s_-$:
   $$T_1 = s,\qquad T_{1^\star} = \max\bigl(s - 2 - 2\ln(s/2),\,0\bigr).$$
   The map $s\mapsto s-2-2\ln(s/2)$ is strictly increasing on $[2,\infty)$,
   so the two statistics are **monotonically equivalent** and give
   **identical p-values** on every realization with $s\geq 2$.
2. **After maximizing over $\hat n_s$**, the equivalence survives
   exactly, because both statistics are the same monotone function of
   the common scalar $s(\hat n_s)$; the argmax sky direction is the
   same for both. "Max of a non-decreasing function equals the function
   of the max" applies because the map $s\mapsto g_2(s)$ does not
   depend on $\hat n_s$.
3. **Equivalence is fragile under prior choice.** It rests on the
   **isotropic** prior $\mathcal{CN}(0,qI_2)$, which preserves the same
   $U(2)$ symmetry that the profile likelihood has. A non-isotropic or
   correlated prior ($Q\neq qI_2$) makes $T_{1^\star}$ depend on
   $(s_+,s_-)$ separately, while $T_1$ remains a function of $s_++s_-$
   alone. Equivalence is then lost.
4. **Relation to the cautionary note.** The single-template note warns
   that the monotone equivalence is a 1-d feature that can break in
   multi-parameter settings. The App. B two-polarization isotropic
   setup is the special higher-dimensional case in which the equivalence
   **does** extend — because the two enlargements (2 templates, 4 real
   amplitudes) are "absorbed" by the isotropic prior and the orthogonal
   equal-norm response, leaving the problem effectively 1-d in a single
   invariant $s$. The warning applies as soon as either symmetry is
   broken.

### Caveats / surprises

- The $-\ln$ correction in the two-template case has **coefficient 2**
  (not 1), reflecting two complex d.o.f. in the prior. The formula
  generalizes to $T_{1^\star}^{(k)} = \max(s - k - k\ln(s/k),0)$ for $k$
  isotropic complex templates. This is the isotropic-$\chi^2_{2k}$-type
  fingerprint.
- The equivalence at fixed sky is a **strict result**, not an
  approximation. It does not require small-$H$, low-SNR, or any of the
  usual toy-limit conditions beyond the isotropy assumptions.
- The equivalence is about **detection significance only**. As
  emphasized in §5 of the single-source note and §5.1 of the App. B
  critique, the Fisher information on the amplitude parameter still
  scales differently ($F_{H_1}\propto$ finite at null; $F_{H_1^\star}\propto 0$
  at null, quadratic in the direction away from it). The *parameter
  interpretation* is different even when the test is the same. This is
  consistent with the §10 conclusion of the App. B critique: the
  ceiling and the $H\to H^2$ demotion in App. B's scaling come not from
  $T_{1^\star}$ being a worse statistic than $T_1$ at fixed $\hat n_s$
  (they are the same statistic up to monotone rescaling), but from the
  separate choice of null (Eq. 50, same-power GWB) and from interpreting
  the detection as a measurement of source power rather than source
  amplitude.
- So Sec. V of the App. B critique remains accurate as written: the
  equivalence of the two statistics does **not** rescue App. B's
  scaling. What this note establishes is only the narrower statement
  that, within Problem B (stochastic source, any null), the two ways of
  deriving the detection statistic — profile over $\vec h$ vs.
  marginalize over $\vec h$ with Gaussian prior — agree at the
  detection stage in the isotropic limit, and do so after sky
  maximization. The scaling losses come from the upstream modeling
  choices (§5.1, §5.2 of the critique note), not from whether one
  profiles or marginalizes.

---

## Appendix: quick consistency check against the $k=1$ note

Set $k=1$ (a single complex template). The boxed result from §3.3
generalizes to $T_{1^\star}^{(k)} = \max(s - k - k\ln(s/k), 0)$. At
$k=1$ this gives $s-1-\ln s$, exactly matching the boxed result in §3
of `coherent_vs_stochastic_single_source.md`. At $k=2$ (the App. B
case) it gives $s-2-2\ln(s/2)$, matching the boxed result of §3.3
above. Consistent.
