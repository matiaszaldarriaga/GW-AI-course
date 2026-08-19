# PTA point-source multipoles: alpha, K_eff, and the detection penalty

**Source:** `references/pta_point_source_multipole_note_updated.md` (canonical;
supersedes the shorter `references/pta_point_source_multipole_note.md`, which
stops at the known-direction case).
**Type:** Pedagogical note (author + ChatGPT), to be checked, not ground truth.
**Ingested:** 2026-06-23. **Numerically verified** by
`paper/scripts/verify_source_vs_cl.py` and `tests/test_source_detection.py`
(28/28 independent checks; see history).

## Summary

The operational backbone of the rewritten detection section
([[../paper/sec_source_detection|Sec. VI]], `paper/sections/source_detection.tex`).
It frames detectability in terms of two measured numbers — the background SNR
$\rho_0 \equiv \Sigma_{\rm bg}$ and the brightest-source fraction $p_1$ — and one
property of the array, its angular resolution $L$ (equivalently $K_L=L(L+2)$
anisotropy modes $\approx$ sky beams). The headline results:

- **Coherent source SNR:** $\rho_{\rm ps} = \alpha_{\rm ps}\,p_1\,\rho_0$ with
  $\alpha_{\rm ps}=\sqrt5\simeq2.24$ (large equal-noise array). Truncating the
  template at multipole $L$ gives $\rho_L=\alpha_L p_1\rho_0$,
  $\alpha_1\simeq0.65$, $\alpha_{\le2}\simeq1.4$.
- **Detection is the same whether the source is modelled in the mean or the
  covariance** (Neyman–Pearson monotone equivalence; [[../concepts/matched_filter_vs_power]]).
- **The $C_\ell$ penalty is modest at low resolution:** comparing an
  unknown-direction coherent scan (paying a trials factor $\sim K_L$) to a
  one-parameter Poisson $C_\ell$ statistic, the required source amplitude
  differs by $1.13,1.16,1.21,1.27,1.33,1.38$ for $L=1\ldots6$ ($p_{\rm fa}=0.05$),
  and Monte-Carlo gives an even smaller penalty at low $L$ — **exactly $1$ at
  $L=1$**, where the scan max equals $\sqrt{C_1}$.

## Key equations (each verified)

- **alpha_ps = sqrt(5)** (Sec. 4). Earth-term pair response
  $\gamma_s(a,b)=\tfrac14(1+\mu_a)(1+\mu_b)\cos[2(\phi_a-\phi_b)]$; random-pair
  averages $\langle\gamma_s^2\rangle=1/18$,
  $\langle\Gamma_0^2\rangle=\int_0^1(1/3-x/6+x\ln x)^2dx=1/108$, ratio $6$;
  monopole removal $\Rightarrow \alpha_{\rm ps}^2=6-1=5$. Monopole-fit cost
  $\sqrt{5/6}\simeq0.91$. *Verified:* the project's full antenna patterns
  (`z_plus`/`z_cross`) sky-average to $\tfrac23$ the Hellings–Downs curve,
  consistent with $\Gamma_0(0)=1/3$, so the simplified pattern is legitimate.
- **alpha_L** (Sec. 5–7):
  $\alpha_L^2=(P_\perp T_L,P_\perp T_L)/(\Gamma_0,\Gamma_0)$ with
  $T_L=\sum_{\ell\le L,m}Y^*_{\ell m}(\hat s)\Gamma_{\ell m}$. Bridge to the
  paper's block weights: $\alpha_{\rm ps}^2=\sum_{L\ge1}s_L\to5$ as
  $N_p\to\infty$ (verified: $4.21$ at $L\le6$, $4.885$ at $L\le8$, climbing to
  $5$). See [[../concepts/s_L_block_weights]].
- **K_L = L(L+2)** anisotropy modes (Sec. 8); free map pays a $\chi^2_{K_L}$-dof
  penalty and needs $K_L\lesssim M=N(N-1)/2$.
- **Detection thresholds** (Sec. 9): scan
  $\rho_{\rm scan}\simeq\Phi^{-1}(1-p_{\rm fa}/K_L)$; Poisson $C_\ell$ statistic
  $\lVert x\rVert^2\sim\chi^2_{K_L}(\rho^2)$, required $\rho$ from the exact
  non-central $\chi^2$. Ratio table reproduced to $<1\%$.
- **K_eff trials factor** $=1/{\rm Tr}\,B^2$ (Sec. 9.1), $=K_L$ for the ideal
  flat case; the $K_{\rm eff}=K_L$ approximation over-counts the continuous-scan
  trials, so it **over**states the low-$L$ penalty (MC is smaller).

## Concepts touched

- [[../concepts/matched_filter_vs_power]] — $\alpha_{\rm ps}=\sqrt5$, the
  linear-(scan)-vs-quadratic-($C_\ell$) detection comparison, $K_{\rm eff}$
  trials.
- [[../concepts/fisher_hierarchy]] — **reconciliation** (see below): the modest
  detection penalty vs. the large $\sigma_p$ / $p^4$ estimation penalty.
- [[../concepts/Cl_over_C0]] — Poisson shape $C_L^P/C_0^P=p_1^2$, one parameter.
- [[../concepts/brightest_source_fraction]] — $p_1$ is the input; required-$p_1$
  thresholds tie to the Sec. IV "$p_1\sim0.6$ at the NANOGrav limit" result.
- [[../concepts/s_L_block_weights]] — $\alpha_L^2$ vs $\sum s_L$ bridge.

## Consistency note: "modest penalty" vs. the wiki's "5–7× / p^4"

This is the crux of the 2026-06-23 rewrite and must not be misread as a
contradiction. The earlier framing ([[../concepts/fisher_hierarchy]],
`pta_point_source_vs_CL_note`) states that the $C_\ell$-only Fisher gives
$\sigma_p^{(C_L)}/\sigma_p^{\rm full}\sim5$–$7$ at $p^2\sim0.1$ — a **parameter-
estimation** (error-bar) ratio, governed by the $p^4$ vs $p^2$ Fisher scaling,
which diverges as $p\to0$. The note's "modest" claim is a **detection** statement:
the required source *amplitude* for a fixed false-alarm/detection probability, at
*fixed angular resolution*, comparing the unknown-direction scan (which itself
pays the trials factor) to the Poisson $C_\ell$. Converting a significance ratio
to an amplitude takes a square root, and at low resolution the scan's trials
factor closes most of the gap. **Both numbers are correct; they answer different
questions** ([[../concepts/fisher_hierarchy]] "Detection vs estimation"). The
paper's earlier "$C_\ell$ is catastrophic / threshold $>1$" conclusion conflated
them; the rewrite corrects this.

## Paper uses

- `paper/sections/source_detection.tex` (Sec. VI) — `eq:KL`, `eq:rho_ps`,
  `tab:detection`, figures `fig:source_snr_res`, `fig:cl_penalty`. Cited via
  `\fromnotebook`.
- Implemented and unit-tested in [[../code/gwb_sources_source_detection]].

## Related wiki pages

- [[pta_source_detection_likelihood]] — the rigorous PTA-native five-likelihood
  derivation; this note is its operational, number-bearing companion. The
  monotone-equivalence ($g_r$, $s-1-\ln s$) and $C_L^P/C_0^P=p^2$ identities are
  shared.
- [[toy_model_source_vs_power_map]] — Bayesian-evidence face (SUM vs MULTIPLY).
- [[joint_search_resolved_unresolved]] — the real-data coherent CW search
  (Goncharov et al.), the top rung in practice.

## History

- **2026-06-23**: Ingested + numerically verified (28/28). Backbone of the
  rewritten Sec. VI; the old Secs. VI–VIII moved to Appendices A–C.
