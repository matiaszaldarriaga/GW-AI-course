# One Source vs Dipole in PTA Covariance Searches

**Source:** `references/pedagogical_note_one_source_vs_dipole_covariance_pta.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives the exact transfer function from the source-power sky $P(\hat\Omega)$ to the
incoherent pulsar-power map $b(\hat p)$, and uses it to prove that — once one compresses to the
dipole ($L=1$) — a one-source incoherent search and a dipole anisotropy search are identical.
The kernel $T(x)=[(1+x)/4]^2$ has a Legendre expansion that terminates at $P_2$, so $b(\hat p)$
contains no information above the quadrupole regardless of array size. The $\tau_L$ coefficients
are computed in closed form. A toy uniform-array Fisher matrix shows all low multipoles share the
same normalization $\Sigma_0^2/(4\pi)$. The note is self-contained and explicitly lists what it
does *not* derive (finite-array multipole-dependent response, full pipeline Fisher matrix).

## Key equations and claims

- **Kernel (Sec. 2):** $T(x) = [(1+x)/4]^2 = 1/12 + (1/8)P_1(x) + (1/24)P_2(x)$. Exact.

- **Transfer function (Sec. 3):**
  $$b_{LM} = \tau_L\,p_{LM}, \qquad
    \tau_0=\frac{\pi}{3},\quad
    \tau_1=\frac{\pi}{6},\quad
    \tau_2=\frac{\pi}{30},\quad
    \tau_{L\ge3}=0.$$

- **Power-spectrum ratios (Sec. 4):**
  $$\frac{C_L^{(b)}}{C_0^{(b)}} = \left(\frac{\tau_L}{\tau_0}\right)^2
    \frac{C_L^{(P)}}{C_0^{(P)}},$$
  giving exact suppression factors $1/4$ at $L=1$ and $1/100$ at $L=2$.

- **One source + isotropic remainder (Sec. 5):** For $P = (1-p)/(4\pi) + p\,\delta^{(2)}$,
  $C_\ell^{(P)}/C_0^{(P)} = p^2$ for all $\ell>0$, hence
  $C_1^{(b)}/C_0^{(b)} = p^2/4$ and $C_2^{(b)}/C_0^{(b)} = p^2/100$.

- **One-source = dipole at $\ell=1$ (Secs. 7–9):**
  The $\ell=1$ projection of the one-source sky is
  $P^{(\ell=1)} = (1/4\pi)[1 + 3p\,\hat n\cdot\hat\Omega]$,
  a pure dipole with amplitude $p$ and direction $\hat n$. After profiling over the
  unknown direction, the score reduces to $|\mathbf{x}|^2$, the dipole power — the
  same statistic used in a rotationally invariant dipole search.

- **Toy Fisher matrix (Sec. 10):** For $N_p$ uniform equal-noise pulsars,
  $F_{LM,L'M'} \simeq [\Sigma_0^2/(4\pi)]\,\delta_{LL'}\delta_{MM'}$
  with $\Sigma_0^2 \equiv N_p[A/(A+\sigma_n^2)]^2$.

## Concepts touched

- transfer_function
- dipole_distribution
- Cl_over_C0
- brightest_source_fraction
- coherent_vs_incoherent
- matched_filter_vs_power
- shot_noise
- fisher_hierarchy
- s_L_block_weights

## Current paper citations

(None yet.)

## Potential additional uses

- **Discussion or numerical_estimates section:** The exact $\tau_L$ values
  ($\tau_0=\pi/3$, $\tau_1=\pi/6$, $\tau_2=\pi/30$, $\tau_{L\ge3}=0$) give a
  principled reason why $C_\ell$-based searches are restricted to $L\le2$ in the
  incoherent map. This directly underpins the paper's argument that $C_\ell$
  compression discards no information at $L\ge3$ for $b(\hat p)$, but still loses
  the coherent signal.
- **Transfer-function discussion:** The exact $1/4$ and $1/100$ suppression factors
  at $L=1$ and $L=2$ can be cited whenever the paper compares $C_\ell^{(b)}$ to
  $C_\ell^{(P)}$. The conventions already in `wiki/conventions.md` record
  $C_1^{(b)}/C_0^{(b)} = (1/4)\,C_1^{(P)}/C_0^{(P)}$; this note is the derivation.
- **One-source search equivalence:** Useful if the paper discusses why a
  direction-resolved one-source incoherent search reduces to dipole power after
  marginalizing direction — relevant to the KL hierarchy narrative and to any
  comparison with NANOGrav's dipole-only or one-source pipelines.

## Relations to other sources

- Provides the derivation backing the transfer-function entry already canonicalized
  in `wiki/conventions.md` (the $b_{LM}=\tau_L p_{LM}$ entry and the
  $C_1^{(b)}/C_0^{(b)}=p^2/4$ formula).
- Complements the earlier note on the coherent time-delay field $z(\hat p)$
  (referenced in Sec. 6 but not named); that note showed harmonic coefficients
  $a_{\ell m}\propto\sqrt{(\ell-2)!/(\ell+2)!}$ for a source on the $z$-axis.
- The toy Fisher normalization $\Sigma_0^2$ parallels the isotropic-background
  significance $\Sigma_{\rm bg}^2$ defined in `wiki/conventions.md`, but applies
  to the diagonal power-map model, not the off-diagonal HD cross-correlation model.

## Caveats / open questions

- The kernel $T(x)=[(1+x)/4]^2$ is stated as "exactly the kernel for the PTA
  response" (Sec. 2) but the derivation of this kernel from first principles is
  deferred to "an earlier note." That earlier note is not identified by name here;
  the transfer function should be traced to a concrete source before citing $\tau_L$
  values in the paper.
- The toy Fisher matrix (Sec. 10) assumes a uniform equal-noise pulsar array. The
  note explicitly flags that this is a toy model. The $\Sigma_0^2/(4\pi)$ value
  should not be used for NANOGrav-specific numerical estimates without replacing it
  with the exact pair-average result from `wiki/conventions.md`.
- Sec. 9 states the look-elsewhere penalty is "already built into" using
  $|\mathbf{x}|^2$ rather than one fixed component, but does not quantify the
  threshold shift. This may matter if the paper makes a numerical claim about
  detection thresholds for a one-source vs dipole search.
