# Anisotropic-response effects on App. B's monotone equivalence

**Purpose.** Quantify how far the profile-vs-Bayes-factor monotone
equivalence of the coherent-vs-stochastic single-source problem
(pedagogical note: `coherent_vs_stochastic_single_source.md`, §4)
extends beyond the isotropic toy limit of App. B of
Sato-Polito–Zaldarriaga–Zackay (2026). The short answer: it is
tied to the property $U^\dagger N^{-1} U \propto I_k$, which in the
PTA case holds only as an average over pulsar sky positions for an
$N_p\to\infty$ uniform array. For any real array it fails at the
tens-of-percent level. The statistics diverge, but not dramatically;
and the qualitative message of §IV (single source vs GWB is sharply
distinguishable when coherent, marginally so when stochasticized) is
robust to this departure.

**Date.** 2026-04-20.

**Sibling page.** `app_B_coherent_fisher_critique.md` (the
stochasticization step: scaling demotion $H\to H^2$; the $3.8\sigma$
ceiling from the power-matching prior). The present note is the
third critique: even holding stochasticization fixed, the draft's
Eq. (B7) / profile-equivalence argument requires a diagonal and
degenerate $U^\dagger N^{-1} U$.

---

## 1. Where the non-isotropy comes from, physically

The App. B data vector for a single frequency bin is
$\vec a = U\vec h + \vec n$, with $\vec h \in \mathbb C^{2N_s}$ the
stack of $(h_{+2},h_{-2})$ polarization amplitudes for $N_s$ sources
and $U$ the Wigner-D design matrix sampled on the $(\ell,m,i)$ grid.
For a single source at $\hat n_s$, $U(\hat n_s)$ is $D\times 2$ and the
relevant Fisher block is the $2\times 2$ matrix
$$\boxed{\; F(\hat n_s) \;\equiv\; U^\dagger(\hat n_s)\,N^{-1}\,U(\hat n_s) \;}$$
with $N$ the $a_{\ell m}$ covariance from Eq. (29) of the draft.
Four distinct physical effects contribute structure to $F(\hat n_s)$:

1. **Non-uniform pulsar sky coverage.** Eq. (29),
   $N_{\alpha\beta} = (4\pi/N_p^w)\,\sigma_{\alpha,n}^2\,\delta_{\alpha\beta} + C_\ell \delta_{\ell\ell'}\delta_{mm'}$,
   is derived under the assumption $\sum_i Y^*_{\alpha,i} Y_{\beta,i} \to (N_p/4\pi)\delta_{\alpha\beta}$
   (Eq. 32). For the NG15 array (67 pulsars, clumped toward the Galactic
   plane — see Fig. 3 of the draft) the off-diagonal terms
   $\sum_i Y^*_{\alpha,i}Y_{\beta,i}$ do not average to zero. Fig. 4 of
   the draft shows per-multipole coupling induced by the pulsar
   distribution at the tens-of-percent level, and the NG15 correlation
   coefficients between $C_2$ and $C_0,C_1,C_3$ were reported in §IV.C
   to be $-0.45$ to $-0.2$.

2. **Unequal per-pulsar noise.** In Eq. (40),
   $\sigma_{i,n}^2 = S_{i,n}(f)/(2\Delta f)$ differs pulsar-by-pulsar by
   more than an order of magnitude (see Fig. 3 left panel:
   J1713+0747, J1909-3744, B1937+21, J1640+2224 dominate). The
   noise-weighted harmonic transform has weights
   $w_{\alpha,i} = Y^*_{\alpha,i}/\sigma_{i,n}^2$, so the effective
   beam-on-the-sphere is anisotropic in a data-driven way that does
   not average to isotropy even for large $N_p$.

3. **Frequency-dependent transmission $\mathcal T(f)$.** The timing-model
   fit absorbs power in a pulsar-specific way, replacing
   $\sigma_{i,n}^2 + \sigma_{i,p}^2 \to \sigma_{i,\mathcal N}^2 \approx (\sigma_{i,n}^2+\sigma_{i,p}^2)/\mathcal T_i(f)$
   (footnote after Eq. 38 of the draft). $\mathcal T_i(f)$ differs
   across pulsars because each has a different timing-model residual
   basis; this amplifies the per-pulsar noise spread in item 2.

4. **Polarization coupling.** The two columns of $U(\hat n_s)$ carry the
   $D^\ell_{m,\pm 2}(\hat n_s)$ Wigner elements. The polarization basis
   couples differently to different pulsars because the spatial
   beam-on-the-sphere (the pulsar's footprint in $a_{\ell m}$ space)
   has a sky-dependent projection onto the two columns. Fig. 2 of the
   draft makes this explicit: the Earth-term SNR$^2$ map
   $\rho^2_e(\hat n_s)$ is dominated by stripes at $m=\pm 2$, peaking
   at $\rho^2 \approx 0.37$ along the equator of the pulsar pole and
   falling to near zero at the poles. The underlying pulsar array
   breaks the SO(3) symmetry, so the $2\times 2$ matrix $F(\hat n_s)$
   is neither diagonal nor isotropic across sky positions.

Of these, (1) and (4) are irreducible geometric effects of a finite,
non-uniform array; (2) and (3) are irreducible data-quality effects.
None goes away in the $N_p\to\infty$ limit unless pulsars are made
uniform on the sphere **and** noise-identical **and** timing-model-identical.

## 2. Structure of $U^\dagger N^{-1} U$ for one source

### 2.1 Isotropic toy limit

Under the Eq. (32) approximation, $N_{(\ell m)(\ell'm')} = N_\ell\,\delta$
is diagonal in the $a_{\ell m}$ basis, and
$\sum_{\ell m} D^{\ell *}_{m,+2}(\hat n_s) D^\ell_{m,-2}(\hat n_s)/N_\ell = 0$
for generic $\hat n_s$ after summing over $\ell$ modes (cross-polarization
orthogonality). The diagonal equals
$$F_{++} = F_{--} = \sum_\ell \frac{|z_\ell|^2}{4 N_\ell}
= \sum_\ell \frac{z_\ell^2}{4 N_\ell}\equiv \rho^2/2,$$
so $F(\hat n_s) = (\rho^2/2)\,I_2$ for every $\hat n_s$. This is the
condition the pedagogical note requires for monotone equivalence.

### 2.2 Realistic pulsar-Fisher block

With pulsar-induced off-diagonal structure in $N$ (and, equivalently,
in $F_{\alpha\beta}$ of Eq. 29), the two columns of $U$ are no longer
noise-orthogonal across $\ell$:
$$F(\hat n_s) = \begin{pmatrix} \rho_+^2(\hat n_s) & \kappa(\hat n_s) \\ \kappa^*(\hat n_s) & \rho_-^2(\hat n_s)\end{pmatrix}.$$
Three things happen:

- **Sky-dependent trace.** $\rho_+^2(\hat n_s) + \rho_-^2(\hat n_s) = \text{tr}\,F(\hat n_s)$
  varies over the sky. This is exactly the Fig. 2 map. At its peak,
  $\text{tr}\,F \approx 0.37$ (Earth term, $\varepsilon=0.1$); in the
  $m=0$ nulls, $\text{tr}\,F\to 0$.
- **Eigenvalue splitting.** The two eigenvalues
  $\rho_{1,2}^2(\hat n_s) = \tfrac12\text{tr}\,F \pm \sqrt{(\tfrac12(\rho_+^2-\rho_-^2))^2+|\kappa|^2}$
  differ. Even when $\rho_+^2=\rho_-^2$ exactly (ensemble over
  pulsar sky positions), a finite realization gives an off-diagonal
  $\kappa$ that lifts the degeneracy.
- **Eigenvector rotation.** The principal axes of $F(\hat n_s)$ are no
  longer aligned with $(h_{+2}, h_{-2})$; they are rotated by a
  sky-dependent angle.

### 2.3 Two-pulsar concrete example

Consider the coarsest possible realistic case: $N_p=2$, white noise
$\sigma_1, \sigma_2$, one pulsar near the source direction
($\hat p_1 \cdot \hat n_s = 1 - \epsilon$) and one far
($\hat p_2\cdot\hat n_s = -1+\epsilon$). At a single frequency bin,
the pulsar-term response is zero for $\hat p_i = \hat n_s$ (since
$1 - \cos\theta_i \to 0$), and the Earth-term response
$h_{m2}^i = D^\ell_{m2}(\hat p_i \to \hat n_s)$ is heavily weighted
toward $m=\pm 2$ modes aligned with $\hat n_s$.

For a pencil-beam array (two pulsars at a single frequency with
$\ell_{\max}=2$), a direct computation gives
$$F(\hat n_s) \approx \begin{pmatrix} 1/\sigma_1^2 & e^{-2i\varphi_2}/\sigma_2^2 \\ e^{2i\varphi_2}/\sigma_2^2 & 1/\sigma_2^2\end{pmatrix}\cdot c(\epsilon),$$
up to geometric prefactors, where $\varphi_2$ is the azimuthal angle
of pulsar 2 relative to $\hat n_s$. The off-diagonal is a pure phase
times the smaller noise inverse — it is not small unless $\sigma_1^2 \ll \sigma_2^2$.
The eigenvalues are
$$\rho_{1,2}^2 = \tfrac12(\sigma_1^{-2}+\sigma_2^{-2})\pm\tfrac12\sqrt{(\sigma_1^{-2}-\sigma_2^{-2})^2+4\sigma_2^{-4}}\;\cdot c(\epsilon).$$
For $\sigma_1=\sigma_2$, the eigenvalue ratio is $\rho_1^2/\rho_2^2 = (1+\sqrt 2)/(1-\sqrt 2) < 0$, i.e. the off-diagonal dominates and one
eigenvalue goes negative — indicating that with only two pulsars the
two polarizations are not simultaneously measurable. This is the
extreme end of the asymmetry axis. For NG15 with 67 pulsars the
degeneracy is averaged down to the tens-of-percent level (see Fig. 2,
peak vs. typical).

## 3. Does the equivalence survive?

### 3.1 General argument

In the $k$-amplitude linear-Gaussian model with design matrix $U$,
prior $\vec h\sim\mathcal{CN}(0,qI_k)$, and $\vec v = U^\dagger N^{-1}\vec a$,
the two statistics are:
$$T_1 = \vec v^\dagger F^{-1} \vec v, \qquad
T_{1^\star} = \vec v^\dagger M \vec v - \ln\det(I + qF),$$
where $F = U^\dagger N^{-1} U$ and
$M = q F (I + qF)^{-1} F^{-1} = F - F(I+qF)^{-1}$, i.e.
$M$ is $F$ in a basis where each eigenvalue $\rho_i^2$ is replaced by
$q\rho_i^4/(1+q\rho_i^2)$. In the eigenbasis of $F$, with
$\vec v = (v_1,\ldots,v_k)$ and $\rho_i^2$ the eigenvalues,
$$T_1 = \sum_i \frac{|v_i|^2}{\rho_i^2}, \qquad
T_{1^\star} = \sum_i \left[\frac{q\rho_i^2}{1+q\rho_i^2}\,\frac{|v_i|^2}{\rho_i^2} - \ln(1+q\rho_i^2)\right].$$
The two statistics are **different weighted sums** of the same $k$
noncentral $\chi^2_2$ variables $y_i \equiv |v_i|^2/\rho_i^2$. The
$T_1$-weights are all $1$; the $T_{1^\star}$-weights are
$w_i \equiv q\rho_i^2/(1+q\rho_i^2) \in [0,1)$.

**They are monotone in each other iff $\rho_i^2$ are all equal.** When
$\rho_i^2 = \rho_*^2$ for all $i$, $w_i = w_*$ is a constant and
$T_{1^\star} = w_*\,T_1 - k\ln(1+q\rho_*^2)$ — an affine, strictly
increasing map. When the $\rho_i^2$ differ, $T_{1^\star}$ is a
$\rho$-dependent reweighting of the same $y_i$'s, which is a linear map
not a monotone map: two realizations $\vec y^{(a)}, \vec y^{(b)}$ can
have $T_1^{(a)} > T_1^{(b)}$ but $T_{1^\star}^{(a)} < T_{1^\star}^{(b)}$.

### 3.2 Worked 2-d toy example

Take $k=2$ with $F = \text{diag}(\rho_1^2, \rho_2^2)$, $\rho_1^2 > \rho_2^2$.
Define $r = \rho_1^2/\rho_2^2 \geq 1$ and fix $q\rho_2^2 = 1$ (order
unity — the interesting regime). Then
- $T_1 = y_1 + y_2$, weights $(1,1)$;
- $T_{1^\star} = \frac{r}{1+r}\,y_1 + \tfrac12 y_2 - \ln(1+r) - \ln 2$,
  weights $(\frac{r}{1+r}, \tfrac12)$.

Two concrete realizations with the **same** $T_1 = 10$:
$$\text{(A)}\;y_1 = 10, y_2 = 0 \quad\Rightarrow\quad T_{1^\star}^{(A)} = \tfrac{10r}{1+r}-\ln(1+r)-\ln 2,$$
$$\text{(B)}\;y_1 = 0, y_2 = 10 \quad\Rightarrow\quad T_{1^\star}^{(B)} = 5-\ln(1+r)-\ln 2.$$
Monotonicity requires $T_{1^\star}^{(A)}=T_{1^\star}^{(B)}$.
The difference is
$$T_{1^\star}^{(A)} - T_{1^\star}^{(B)} = 10\,\tfrac{r}{1+r}-5 = 5\,\tfrac{r-1}{r+1}.$$
This is zero only at $r=1$. For PTA-realistic asymmetry:

| Asymmetry | $r = \rho_1^2/\rho_2^2$ | $\Delta T_{1^\star}$ at fixed $T_1=10$ | Fractional shift |
|---|---|---|---|
| Eigenvalue splitting $\sim 10\%$ | 1.1 | 0.24 | 3% of $T_1$ |
| Fig. 2 equator-to-typical (NG15) | $\sim 2$ | 1.67 | 17% of $T_1$ |
| Near-null direction on $\hat n_s$ | $\sim 10$ | 4.09 | 41% of $T_1$ |
| Two-pulsar extreme (§2.3) | $\to \infty$ | $\to 5$ | 50% of $T_1$ |

So for a "typical" NG15-like realization at fixed sky-position
$\hat n_s$, the rank disagreement between the two statistics is at
the 10–20% level of $T_1$ in the bulk. In a small set of
unfortunate directions (the $m=0$ nulls of Fig. 2), it can reach
40–50% of $T_1$.

### 3.3 What this means for the p-value

Disagreement of test statistics does not automatically imply
disagreement of p-values: two statistics can rank the data differently
on individual realizations yet have nearly identical ROC curves if
their null distributions shift in compensating ways. The question is
whether $T_{1^\star}/T_1$ varies enough across **null realizations**
to change the detection threshold materially.

Quick estimate. Under the null, $y_i\sim \chi^2_2$ (complex amplitude
→ $2$ real d.o.f. per eigenmode). $T_1 = y_1+y_2 \sim \chi^2_4$.
$T_{1^\star}$ is a weighted sum $w_1 y_1 + w_2 y_2$ with $w_1 \geq w_2$.
For $r=2$ ($w_1 = 2/3, w_2 = 1/2$), the $1\%$ quantiles of
$T_1$ and the best monotone relabelling of $T_{1^\star}$ differ by
$\sim 5\%$ of the threshold — a detection at $3\sigma$ from one
statistic corresponds to somewhere between $2.85\sigma$ and $3.15\sigma$
from the other. This is **noise-level** compared to the App. B
$3.8\sigma$ ceiling and the $H\to H^2$ scaling demotion, which cost
orders of magnitude.

## 4. Implication for the critique

### 4.1 Rigorously, the App. B monotone equivalence is toy-limit only

The pedagogical note proves the equivalence for $k=1$ (scalar
amplitude) where $F$ is trivially a scalar and $r$ is undefined. For
$k\geq 2$, the equivalence requires $F\propto I_k$, and the draft
achieves this only under the Eq. (32) isotropy-of-pulsar-distribution
approximation. Any realistic PTA Fisher block has
$F(\hat n_s)$ with eigenvalue spread at the tens-of-percent level
(typical $\hat n_s$) to order-unity level (nulls of Fig. 2). At the
test-statistic level, this produces tens-of-percent relative
reweighting of the two polarization modes. At the p-value level, the
effect is a few-percent shift in the detection threshold.

This is a **third** critique of App. B, separate from the two in
`app_B_coherent_fisher_critique.md`:
1. Stochasticization ($H\to H^2$). Scaling-level, orders of magnitude.
2. Power-matching null ($3.8\sigma$ ceiling). Scaling-level, orders.
3. **Isotropy-of-response.** Threshold-level, few percent on detection
   significance; ranking-level, tens of percent on individual
   realizations.

Critique (3) is **quantitatively mild** compared to (1) and (2). Its
main role is to remove the appearance of a clean closed-form
equivalence: in a realistic PTA the profile and Bayes-factor
statistics are genuinely two different tests, and the "no cost at
the detection stage" theorem of the pedagogical note does not lift to
the multi-parameter setting.

### 4.2 What a realistic-asymmetry calculation would look like

A future paper would:
1. Use the full $F_{\alpha\beta}$ of Eq. (29) (not its diagonal) for a
   specific $N_p=67$ pulsar configuration (NG15 sky coords + NG15
   per-pulsar noise via `hasasia`).
2. For each source direction $\hat n_s$, assemble the $2\times 2$
   $F(\hat n_s) = U^\dagger(\hat n_s) N^{-1} U(\hat n_s)$, not its
   trace or determinant.
3. Compute $T_1(\hat n_s)$ and $T_{1^\star}(\hat n_s)$ separately;
   compare their sampling distributions under $H_0$ (fixed isotropic
   GWB) and under $H_1$ (coherent source at $\hat n_s$, $H$ grid).
4. Report the detection threshold as a **map** on the sky, not a
   single number. Sky-averaging the detection probability (the bottom
   row of Fig. 6) averages over realizations of pulsar-and-source
   geometry but may conceal direction-dependent differences between
   the two statistics.

Steps 1–2 are essentially what §IV.C already does with `hasasia` for
the HD detection SNR $\rho_{\rm HD}=3.14$; only steps 3–4 are new.

### 4.3 Which numerical results survive

- **$\rho_{\rm HD} = 3.14$ for NG15** (§IV.C). This is a full
  Fisher-matrix calculation using Eq. (36) with the actual
  $N_{\alpha\beta}$. It does **not** use the isotropic Eq. (32)
  approximation. **Survives.**

- **$\sigma_{C_2} = 0.9$, i.e. $\rho_2=1.74$ at $\ell_{\max}=5$
  marginalized** (§IV.C). Same calculation as above. **Survives.**

- **$N_s^{\rm eff} \sim 3$ for NG15** (§IV.A, Fig. 5). Uses the
  eigenvalues of $F_h = U^\dagger N^{-1} U$ with full $N$.
  Uses the isotropic toy only in the normalization choice; the
  eigenvalue structure itself already carries the pulsar
  non-uniformity. The number $3$ is robust to factor-of-2 changes in
  $\alpha$ (the effective-modes threshold) and would not change
  qualitatively if critique (3) were corrected. **Survives.**

- **$\sim 3.8\sigma$ ceiling** (Eq. 48). A toy-limit number derived
  under Eq. (32) isotropy. The critique of this section adds
  $\lesssim 0.2\sigma$ uncertainty onto $3.8$; the larger critiques
  are (1) and (2) above. **Toy-limit; numerical value good to
  $\sim 5\%$ of itself.**

- **KL divergence between single-source and GWB maps at NG15**
  (Fig. 9, $D_{\rm KL}\sim 10^{-4}$). Uses the full
  non-diagonal Eq. (A14) estimator per the figure caption — the
  authors already acknowledge the issue there. **Survives and is
  the cleanest number in the paper.**

- **Fig. 6 ROC curves and the targeted-vs-blind comparison** (§IV.B).
  Uses Monte Carlo realizations in the isotropic $N_{\alpha\beta}$
  approximation per the caption; the ROC shapes are robust to the
  $\mathcal O(5\%)$ corrections of critique (3), but the $\ell=2$
  beta-distribution analytical formulas (Eq. 49 and below) rely on
  rotational invariance and would acquire $\sim 10\%$ skew-like
  corrections in a realistic calculation.

## 5. Verdict

**Does the App. B monotone equivalence fail for realistic PTAs?** Yes,
strictly speaking: the equivalence is proven for $k=1$ and for $k\geq 2$
only under $F\propto I_k$, which the draft obtains as a property of the
Eq. (32) isotropic-pulsar approximation. Any real PTA has $F$ with
nondegenerate eigenvalues, so the profile and Bayes-factor statistics
are no longer monotone functions of each other.

**How badly?** Quantitatively mild: $\sim 10$–$20\%$ rank
disagreement on individual realizations for typical sky positions, up
to $\sim 50\%$ in unfortunate ($m=0$ null) directions; a few percent
shift in detection thresholds. This is two orders of magnitude smaller
than the scaling-level critiques of stochasticization ($H\to H^2$) and
of the $3.8\sigma$ ceiling. The main qualitative casualty is the
clean closed-form identity $T_{1^\star} = g(T_1)$ of the pedagogical
note; in a realistic PTA the two statistics are two different tests.

**Net effect on the App. B conclusions.** Critique (3) of this note
does not rescue App. B's $3.8\sigma$ ceiling (that comes from the
power-matching prior), and it does not restore App. B's detection
significance to the linear-in-$H$ scaling of a proper coherent search
(that requires undoing the stochasticization). It does, however,
remove the last remaining reason to treat App. B's stochasticized
likelihood as an intrinsically optimal statistic: in the toy limit it
is the minimum-variance unbiased power estimator; outside the toy
limit it is merely one member of a family of near-equivalent
statistics, the coherent matched filter being another.
