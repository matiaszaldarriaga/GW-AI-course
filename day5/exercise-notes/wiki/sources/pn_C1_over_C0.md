# Distribution of $C_1/C_0$ for point-source skies

**Source:** `references/pedagogical_note_C1_over_C0_dollar_math.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives the exact and semi-analytic probability distribution of the
dipole-to-monopole ratio $R_1 \equiv C_1/C_0$ for a sky of discrete point
sources with random isotropic positions and arbitrary source weights $\{q_a\}$.
The central insight is that $C_\ell/C_0$ depends on the amplitudes only through
the normalized fractions $p_a = q_a/\sum_b q_b$, not the overall scale. For
$\ell=1$ specifically, $R_1 = |\mathbf{S}|^2$ where $\mathbf{S} = \sum_a p_a
\hat n_a$ is a weighted 3D random walk, reducing the problem to the squared
norm of a vector sum. The note provides four semi-analytic approximations
(one-source delta, two-source uniform, one-source+Gaussian, two-source+Gaussian)
plus an exact one-dimensional Fourier-Bessel integral, and reconciles the
results with the Lin et al. shot-noise formula $C_\ell^{\rm SN} = 4\pi/N_{\rm eff}$.
It is the analytic backbone for the paper's distribution figures and the
$C_1/C_0$ section.

## Key equations and claims

- **Exact $C_\ell$ at source level:** $C_\ell = \frac{1}{4\pi}\sum_{a,b} q_a q_b
  P_\ell(\hat n_a \cdot \hat n_b)$, with $C_0 = Q^2/(4\pi)$. (Sec.~2)
- **Ratio cancels overall scale:** $C_\ell/C_0 = \sum_{a,b} p_a p_b
  P_\ell(\hat n_a \cdot \hat n_b)$, $p_a = q_a/Q$. (Sec.~3)
- **Dipole as random-walk norm:** $R_1 = C_1/C_0 = |\mathbf{S}|^2$,
  $\mathbf{S} = \sum_a p_a \hat n_a$. (Sec.~5) → paper eq:~\ref{eq:dipole}
- **Conditional mean (all $\ell \ge 1$):** $\mathbb{E}[C_\ell/C_0 \mid \{p_a\}]
  = \sum_a p_a^2 = 1/N_{\rm eff}$. (Sec.~7.2) → paper eq:~\ref{eq:mean_cl}
- **Conditional variance:** $\mathrm{Var}(R_1 \mid \{p_a\}) = \frac{2}{3}
  [(\sum_a p_a^2)^2 - \sum_a p_a^4]$. (Sec.~7.3) → paper eq after~\ref{eq:dipole}
- **Exact characteristic function:** $\chi_\mathbf{S}(k) = \prod_a \sin(p_a k)/(p_a k)$.
  (Sec.~6.2)
- **Exact radial pdf:** $f_R(r) = \frac{2r}{\pi}\int_0^\infty k\sin(kr)
  \prod_a \frac{\sin(p_a k)}{p_a k}\,dk$; then $f_U(u) = f_R(\sqrt{u})/(2\sqrt u)$.
  (Sec.~6.3)
- **One source + Gaussian faint background ($p$, $\eta = \sum_{\rm faint} p_a^2$):**
  noncentral-Maxwell kernel; collapses to $\delta(u-p^2)$ as $\eta\to 0$. (Sec.~10)
  → paper eq:~\ref{eq:1src_gauss}
- **Two sources + Gaussian faint background ($p_1,p_2,\eta_2$):** four-term
  normal-CDF formula with $a_\pm = p_1 \pm p_2$, $\sigma=\sqrt{\eta_2/3}$;
  reduces to uniform law as $\eta_2\to 0$. (Sec.~11) → paper eq:~\ref{eq:2src_gauss}
- **Two sources, no background:** $f_U = 1/(4p_1 p_2)$ uniform on
  $[(p_1-p_2)^2,(p_1+p_2)^2]$. (Sec.~8.2)
- **Shot-noise connection:** $\mathbb{E}[C_\ell^{(\delta M)}] = 4\pi/N_{\rm eff}$
  recovers Lin et al. (2026); the present note extends this to the full pdf.
  (Sec.~19)
- **Support:** $R_1 \in [\max(0,2p_{\max}-1)^2,\,1]$. (Sec.~7.1)

## Concepts touched

- [[concepts/Cl_over_C0]] — derives the exact formula, random-walk picture,
  conditional mean/variance, and four semi-analytic approximations to the
  full pdf
- [[concepts/N_eff]] — established as the inverse-participation ratio
  $N_{\rm eff} = 1/\sum_a p_a^2$; the mean $C_\ell/C_0 = 1/N_{\rm eff}$
  holds for all $\ell \ge 1$
- [[concepts/brightest_source_fraction]] — $p_1, p_2, \eta$ appear as natural
  parameters separating one-source, two-source, and many-source regimes;
  $R_1 \approx p_1^2$ in the one-source+faint-sea limit
- [[concepts/dipole_distribution]] — this note is the primary source for all four
  semi-analytic approximations used in the paper
- [[concepts/shot_noise]] — Sec.~19 reconciles the discrete-source $4\pi/N_{\rm eff}$
  shot-noise floor with the full conditional pdf

## Current paper citations

- `paper/sections/angular_power_spectrum.tex:66` — `\fromnotebook{... Sec.~3}` —
  derives that $\mathbb{E}[C_\ell/C_0] = \sum_a p_a^2 = 1/N_{\rm eff}$ (all $\ell\ge 1$)
- `paper/sections/angular_power_spectrum.tex:90` — `\fromnotebook{... Secs.~5--6}` —
  dipole random-walk identity $R_1 = |\mathbf{S}|^2$, conditional variance, and
  exact characteristic function
- `paper/sections/distribution_c1c0.tex:47` — `\fromnotebook{... Sec.~10}` —
  one-source + Gaussian faint-background noncentral-Maxwell formula
- `paper/sections/distribution_c1c0.tex:64` — `\fromnotebook{... Sec.~11}` —
  two-source + Gaussian faint-background four-CDF formula

## Potential additional uses

- The exact support formula $R_1 \ge \max(0, 2p_{\max}-1)^2$ could tighten the
  discussion of the large-$C_1/C_0$ tail in the angular power spectrum section.
- The beam/smoothing rule $(C_\ell/C_0) \to (W_\ell/W_0)^2 (C_\ell/C_0)$ could
  be cited when discussing how pixelization or bandwidth effects modify the ratio
  (currently unaddressed in the paper).
- Sec.~16 shows $\mathbb{E}[C_\ell/C_0]$ is $\ell$-independent for all
  $\ell \ge 1$ — a useful counter-intuitive point that could strengthen the
  argument that $C_\ell$ compression adds little beyond $C_1$.
- The Gaussian-background variance formula could be cited in any Monte Carlo
  validation section to give analytic error bars on the $C_1/C_0$ histogram.
- Sec.~19.3 on the interpretation of $\langle h^4\rangle$ for point sources
  could be useful if the paper needs to explain the contact-term subtlety
  to referees.

## Relations to other sources

- The note explicitly parallels the characteristic-function approach of
  Sato-Polito and Zaldarriaga (2024) [arXiv:2406.17010] for total-power
  distributions; the dipole-ratio problem is a natural refinement of that work.
- Sec.~19 is a direct comparison with Lin et al. (2026) [arXiv:2602.16808]
  shot-noise expressions.

## Caveats / open questions

- The note covers only $C_1/C_0$; higher-multipole distributions for $\ell \ge 2$
  are mentioned (Sec.~16, mean is the same) but no pdf formula is given beyond
  the first moment.
- All results condition on the weights $\{p_a\}$ being fixed; the further
  astrophysical average over the source-population draw is described
  qualitatively (Secs.~13--14) but not computed in closed form.
- The Gaussian-background approximation leaks outside $[0,1]$ when $\eta \gg p^2$;
  the note flags this as harmless in the expected regime but it should be
  verified for the highest-frequency bins where $N_{\rm eff}$ is small.
- The note does not specify which map quantity $q_a$ represents (strain, power,
  etc.); the paper uses $q_a = h_a^2$, but this is the reader's responsibility
  to supply.
