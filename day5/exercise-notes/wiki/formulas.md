# Formulas

Master index of the equations that matter. Each row points to its
canonical concept page (where the derivation and context live) and any
paper label (for the subset used in the paper).

## Paper-labelled equations

| Label | File | Statement | Canonical concept | Source note |
|---|---|---|---|---|
| `eq:cl_exact` | `angular_power_spectrum.tex` | $C_\ell = \frac{1}{4\pi}\sum_{ab}q_a q_b P_\ell(\hat n_a\cdot\hat n_b)$ | [[concepts/Cl_over_C0]] | [[sources/pn_C1_over_C0]] Sec. 2-3 |
| `eq:cl_c0_exact` | `angular_power_spectrum.tex` | $C_\ell/C_0 = \sum_{ab}p_a p_b P_\ell(\hat n_a\cdot\hat n_b)$ | [[concepts/Cl_over_C0]] | [[sources/pn_C1_over_C0]] Sec. 3 |
| `eq:neff` | `angular_power_spectrum.tex` | $N_{\rm eff} = 1/\sum p_a^2$ | [[concepts/N_eff]] | [[sources/pn_C1_over_C0]] Sec. 7.2 |
| `eq:mean_cl` | `angular_power_spectrum.tex` | $\mathbb E[C_\ell/C_0\mid\{p_a\}] = 1/N_{\rm eff}$ for $\ell\ge 1$ | [[concepts/Cl_over_C0]] | [[sources/pn_C1_over_C0]] Sec. 7.2 |
| `eq:dipole` | `angular_power_spectrum.tex` | $C_1/C_0 = \|\mathbf S\|^2$ with $\mathbf S=\sum p_a\hat n_a$ | [[concepts/dipole_distribution]] | [[sources/pn_C1_over_C0]] Sec. 5 |
| `eq:1src_gauss` | `distribution_c1c0.tex` | Noncentral Maxwell pdf | [[concepts/dipole_distribution]] | [[sources/pn_C1_over_C0]] Sec. 10 |
| `eq:2src_gauss` | `distribution_c1c0.tex` | $\Phi$-differences (multline) | [[concepts/dipole_distribution]] | [[sources/pn_C1_over_C0]] Sec. 11 |
| `eq:p1_given_x` | `distribution_c1c0.tex` | $P(p_1\mid C_1/C_0>v)\propto\pi(p_1)\int d\eta\,S(v\mid p_1,\eta)P(\eta\mid p_1)$; $S$ = survival fn (exceedance prob) of `eq:1src_gauss`. $\pi(p_1)$, $P(\eta\mid p_1)$ taken from Monte Carlo; evaluated by importance-reweighting each realization by $S$ | [[concepts/dipole_distribution]] | [[notebooks/guide_power_anisotropy]] §10f |
| `eq:p1_given_x_simple` | `distribution_c1c0.tex` | $\langle p_1\mid x\rangle\simeq\sqrt{x}$ (brightest-dominated limit; slight overestimate — MC: $\langle p_1\mid x\rangle\approx0.85\sqrt{x}$) | [[concepts/brightest_source_fraction]] | [[notebooks/guide_power_anisotropy]] §10f |
| `eq:neff_given_x` | `dipole_source.tex` | $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$ is an empirical conditional trend with broad scatter; it does not follow algebraically from $E[x\mid\{p_a\}]=1/N_{\rm eff}$ | [[concepts/N_eff]] | schema-v2 full-moment Monte Carlo |
| `eq:hc_sum` | `astrophysical_model.tex` | $h_c^2(f)=\sum_k\bar N(f,M_k)\,h_s^2(f,M_k)$ (mean total = sum over mass bins $k$) | [[concepts/SMBH_population_model]] | [[sources/arxiv_2406_17010]] |
| `eq:hs2_single` | `astrophysical_model.tex` | $h_s^2\propto(GM)^{10/3}\,\eta^2\,(1+z)^{4/3}/\chi^2(z)\,f^{4/3}\,(f/\Delta f)$, $\eta=q/(1+q)^2$ (per-source char. strain²; inclination/pol averaged, distance via $(1+z)/\chi$, $f/\Delta f$ = cycles per bin) | [[concepts/SMBH_population_model]] | [[sources/arxiv_2406_17010]] Eq. 10 |
| `eq:R_ratio` | `distribution_c1c0.tex` | $R\equiv h_{s,\max}^2/\langle h_c^2\rangle(f)$ (brightest-source power / fixed mean background; comparable to NANOGrav CW limits) | [[concepts/brightest_source_fraction]] | [[notebooks/guide_power_anisotropy]] |
| `eq:F_coh` | `three_strategies.tex` | Coherent Fisher block-diagonal in $(A_{\rm iso},a)$ | [[concepts/coherent_vs_incoherent]] | [[sources/pn_coh_vs_incoh_fisher]] Sec. 4.2 |
| `eq:F_inc` | `three_strategies.tex` | Incoherent $2\times 2$ covariance-space Fisher | [[concepts/coherent_vs_incoherent]] | [[sources/pn_coh_vs_incoh_fisher]] Sec. 5.2 |
| `eq:F_marg` | `three_strategies.tex` | $F^{\rm inc,marg}_{qq}=\langle\Delta\Gamma_\perp,\Delta\Gamma_\perp\rangle_{C_0}$ | [[concepts/source_background_degeneracy]] | [[sources/pn_coh_vs_incoh_fisher]] Sec. 5.3 |
| `eq:F_cl_final` | `three_strategies.tex` | $F_{pp}^{(C_L)}=2p^2\Sigma_{\rm bg}^4\sum_L s_L^2/(2L+1)+O(p^4)$ | [[concepts/fisher_hierarchy]] | [[sources/pta_1src_vs_CL]] Sec. 5 |
| `eq:hierarchy` | `three_strategies.tex` (App. A) | $D_{\rm coh}\propto p,\; D_{\rm inc}\propto p^2,\; D_{C_\ell}\propto p^4$ | [[concepts/fisher_hierarchy]] | [[sources/pta_1src_vs_CL]] Secs. 3-5 + [[sources/pn_coh_vs_incoh_fisher]] Secs. 8-9 |
| `eq:HD` | `source_detection.tex` | $\Gamma_0(\zeta_{ab})=\tfrac12-\tfrac{x}4+\tfrac{3x}2\ln x$, $x=(1-\cos\zeta_{ab})/2$ (Hellings--Downs curve; isotropic-background pair pattern) | [[concepts/coherent_vs_incoherent]] | [[sources/pta_point_source_multipole]] Sec. 2 |
| `eq:sigma_bg` | `source_detection.tex` | $\rho_0\equiv\Sigma_{\rm bg}$, $\Sigma_{\rm bg}^2=A^2 F_A$, $F_A=\tfrac12\mathrm{Tr}[\bar C_0^{-1}\Gamma_{\rm iso}\bar C_0^{-1}\Gamma_{\rm iso}]$ (background-amplitude significance; per-bin NG15 $\rho_0\sim1$, future benchmark $\rho_0\simeq20$) | [[concepts/s_L_block_weights]] | [[sources/pta_point_source_multipole]] Sec. 2 |
| `eq:KL` | `source_detection.tex` | $K_L=\sum_{\ell=1}^L(2\ell+1)=L(L+2)$ anisotropy modes / sky beams | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Sec. 8 |
| `eq:gamma_src` | `source_detection.tex` | $\gamma_{ab}(\hat s)=F_a^+ F_b^+ + F_a^\times F_b^\times$ (point-source pair response; analogue of $\Gamma_0$ for a single direction) | [[concepts/coherent_vs_incoherent]] | [[sources/pta_point_source_multipole]] Secs. 3-4 |
| `eq:rho_ps` | `source_detection.tex` | $\rho_{\rm ps}=\alpha_{\rm ps}\,p_1\,\rho_0$, $\alpha_{\rm ps}=\sqrt5\simeq2.24$ (large equal-noise array) | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Secs. 3-4 |
| `eq:alpha_ps` | `source_detection.tex` | $\alpha_{\rm ps}^2=6-1=5$ (ratio $\langle\gamma_s^2\rangle/\langle\Gamma_0^2\rangle=(1/18)/(1/108)=6$ minus the shared monopole; monopole-fit cost $\sqrt{5/6}\simeq0.91$) | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Sec. 4 |
| `eq:Fpp_cl` | `source_detection.tex` | $F_{p_1 p_1}^{(C_\ell)}\propto p_1^2\,\Sigma_{\rm bg}^4$ ⇒ $D_{C_\ell}\sim\tfrac12 p_1^2 F^{(C_\ell)}_{p_1p_1}\propto p_1^4$; $\sigma_{p_1}$ larger than full fit by $\propto1/(p_1\Sigma_{\rm bg})$ | [[concepts/fisher_hierarchy]] | [[sources/pta_point_source_multipole]] Sec. 5 |

## Note-derived formulas (not yet paper-labelled)

### Source-power sky statistics

| Statement | Concept | Source |
|---|---|---|
| $\chi_{\mathbf S}(k) = \prod_a \sin(p_a k)/(p_a k)$ | [[concepts/dipole_distribution]] | [[sources/pn_C1_over_C0]] Sec. 6.2 |
| $\mathrm{Var}(C_1/C_0\mid\{p_a\}) = (2/3)[(\sum p_a^2)^2 - \sum p_a^4]$ | [[concepts/Cl_over_C0]] | [[sources/pn_C1_over_C0]] Sec. 7.3 |
| $Q=\sum_s w_s$, $S_2=\sum_s w_s^2$, $N_{\rm eff}=Q^2/S_2$ | [[concepts/N_eff]] | schema-v2 product contract, `gwb_sources/full_moment_schema.py` |
| $S_{2,\rm bulk}=\sum_b n_b E[w_b^2]=\sum_b n_b(E[w_b]^2+\mathrm{Var}[w_b])$ | [[concepts/N_eff]] | full-moment remediation; distinguishes the corrected moment from $nE[w]^2$ |
| $Q=Q_{\rm ledger}+Q_{\rm remainder}$ and $S_2=S_{2,\rm ledger}+S_{2,\rm remainder}$ | [[concepts/brightest_source_fraction]] | schema-v2 ledger/remainder identity |
| $\mathbf D=\sum_s w_s\hat n_s$, $C_1/C_0=|\mathbf D|^2/Q^2$; unresolved component variance $S_{2,\rm bulk}/3$ | [[concepts/dipole_distribution]] | direct low-moment product contract |
| integrated-pixel map convention: $C_0=4\pi Q^2/N_{\rm pix}^2$, $C_1=4\pi|\mathbf D|^2/N_{\rm pix}^2$ | [[concepts/Cl_over_C0]] | `gwb_sources.power_anisotropy` and normalization tests |
| $\mathbb E[C_\ell^{(\delta M)}] = 4\pi/N_{\rm eff}$ (Lin et al.) | [[concepts/shot_noise]] | [[sources/pn_C1_over_C0]] Sec. 19 |
| $R_1\in[\max(0,2p_{\max}-1)^2, 1]$ support bound | [[concepts/brightest_source_fraction]] | [[sources/pn_C1_over_C0]] Sec. 7.1 |

### Covariance benchmark constants

| Statement | Concept | Source |
|---|---|---|
| $\Sigma_{\rm bg}^2 = (A^2 N_p/2\sigma_n^4)(1 + (N_p-1)/48)$ | [[concepts/s_L_block_weights]] | [[sources/pta_exact_pair_average]], [[sources/pta_noise_dominated_limit]] |
| $s_L(N_p,0) = \frac{2L+1}{4\pi}\,\frac{D_L + (N_p-1)O_L}{1+(N_p-1)/48}$ | [[concepts/s_L_block_weights]] | Same |
| $D_1=\pi,\; D_2=\pi/25,\; D_{L\ge 3}=0$ | [[concepts/s_L_block_weights]] | Same |
| $\frac{1}{48} = \tfrac12\int_{-1}^1\chi(\mu)^2 d\mu$ (HD curve integral) | [[concepts/s_L_block_weights]] | Same |
| $\mathrm{SNR}_L^2 = \Sigma_{\rm bg}^2 s_L C_L^{(P)}/C_0^{(P)}$ | [[concepts/s_L_block_weights]] | Same |
| $F_{pp}^{\rm full}=\Sigma_{\rm bg}^2\sum_L s_L$ | [[concepts/fisher_hierarchy]] | [[sources/pn_coh_vs_incoh_fisher]] Sec. 8 |
| $\sigma_p^{(C_L)}/\sigma_p^{\rm full}\sim 1/(p\Sigma_{\rm bg})\sqrt{\sum s_L/\sum s_L^2/(2L+1)}$ | [[concepts/fisher_hierarchy]] | [[sources/pta_1src_vs_CL]] Sec. 5 |

### Transfer function

| Statement | Concept | Source |
|---|---|---|
| $b_{LM} = \tau_L\, p_{LM}$ | [[concepts/transfer_function]] | [[sources/pn_1src_vs_dipole_cov]] Sec. 3 |
| $\tau_0=\pi/3,\;\tau_1=\pi/6,\;\tau_2=\pi/30,\;\tau_{L\ge 3}=0$ | [[concepts/transfer_function]] | Same |
| $C_1^{(b)}/C_0^{(b)} = (1/4)\,C_1^{(P)}/C_0^{(P)}$ | [[concepts/transfer_function]] | Same |
| $C_1^{(b)}/C_0^{(b)} = p^2/4$ (one bright source) | [[concepts/transfer_function]] | [[sources/pn_coh_vs_quadratic]] Sec. 9 |

### Coherent/incoherent Fisher and KL

| Statement | Concept | Source |
|---|---|---|
| $F_{\alpha,B^2}=0$ exactly for coherent source params | [[concepts/source_background_degeneracy]] | [[sources/fisher_src_vs_bg_degeneracy]] Sec. 2 |
| $F_{qq}^{\rm inc}=(u^\dagger C^{-1}u)^2$ (rank-1 identity) | [[concepts/source_background_degeneracy]] | [[sources/fisher_src_vs_bg_degeneracy]] Sec. 5 |
| $\|r\| \sim 1/\sqrt{N_p}$ for known direction | [[concepts/source_background_degeneracy]] | [[sources/fisher_src_vs_bg_degeneracy]] Sec. 6.2 |
| $D_{\rm mean}=\rho_{\rm coh}^2$ (coherent KL = matched-filter SNR²) | [[concepts/KL_divergence]] | [[sources/pn_coh_vs_quadratic]] Sec. 3 |
| $D_{\rm cov}^+ = n\log(1+\rho^2/n)-\log(1+\rho^2)$ (rank-1) | [[concepts/KL_divergence]] | [[sources/pn_coh_vs_quadratic]] Sec. 7 |
| $D_{\rm cov} \approx \tfrac12(1-1/n)\rho_{\rm coh}^4$ (weak rank-1) | [[concepts/KL_divergence]] | Same |

### Source-detection likelihood hierarchy (PTA-native, five likelihoods)

| Statement | Concept | Source |
|---|---|---|
| $\lambda_{\rm coh}=a_s^TU^T(N+B\Gamma_0)^{-1}U a_s = h^2 A_{\rm coh}\simeq BA_{\rm coh}\,p$ (coherent, $\propto p$) | [[concepts/fisher_hierarchy]] | [[sources/pta_source_detection_likelihood]] Sec. 3 |
| $g_r(T)=T-r-r\log(T/r)$ ($T>r$), $g_r'>0$ — projector cov. monotone in $T_{\rm coh}$ (rank-1: $s-1-\log s$) | [[concepts/coherent_vs_incoherent]] | [[sources/pta_source_detection_likelihood]] Sec. 4.2 |
| $p_{{\rm coh},*}=p_{{\rm sub},*}=\lambda_{\rm req}/(BA_{\rm coh}+\lambda_{\rm req})$ (equal thresholds) | [[concepts/fisher_hierarchy]] | [[sources/pta_source_detection_likelihood]] Sec. 4.2/11 |
| $C_L^P/C_0^P=(q/(B+q))^2=p^2$ ($L>0$, response-free) | [[concepts/Cl_over_C0]] | [[sources/pta_source_detection_likelihood]] Sec. 5 |
| $T_{\rm psrc}=(v^Ts)^2/(v^TFv)\sim\chi^2_1$, $\lambda_{\rm psrc}=p^2 v^TF(Q)v$ (one-source power map, $\propto p^2$) | [[concepts/matched_filter_vs_power]] | [[sources/pta_source_detection_likelihood]] Sec. 7 |
| $T_{\rm map}=s^TF^{-1}s\sim\chi^2_m$, same $\lambda=p^2 v^TFv$ but $m$-dof penalty | [[concepts/fisher_hierarchy]] | [[sources/pta_source_detection_likelihood]] Sec. 8 |
| $D_{C_L}=\tfrac{p^4}{4}\sum_L[v_L^TF_L(Q)v_L]^2/(2L+1)+O(p^6)$ (block-resolved $p^4$) | [[concepts/fisher_hierarchy]] | [[sources/pta_source_detection_likelihood]] Sec. 9 |
| $q_*=B\,p_*/(1-p_*)$; $h_*^2=B\sqrt{R_*}/(1-\sqrt{R_*})$, $R_*=C_L^P/C_0^P$ | [[concepts/Cl_over_C0]] | [[sources/pta_source_detection_likelihood]] Sec. 9/11 |

### Source detection: alpha coefficients and detection thresholds

Anchor: [[concepts/matched_filter_vs_power]], [[concepts/fisher_hierarchy]].
Canonical source [[sources/pta_point_source_multipole]]; code
[[code/gwb_sources_source_detection]]; verified by
`paper_v2/scripts/verify_source_vs_cl.py`.

| Statement | Concept | Source |
|---|---|---|
| $\alpha_{\rm ps}^2=\langle(\gamma_s-\Gamma_0)^2\rangle/\langle\Gamma_0^2\rangle=(1/18-1/108)/(1/108)=5$ | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Sec. 4 |
| monopole-fit cost $=\sqrt{5/6}\simeq0.91$ (9%) | [[concepts/matched_filter_vs_power]] | Same |
| $\alpha_L^2=(P_\perp T_L,P_\perp T_L)/(\Gamma_0,\Gamma_0)$; $\alpha_1\simeq0.65$, $\alpha_{\le2}\simeq1.4$ | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Secs. 5-7 |
| bridge: $\alpha_{\rm ps}^2=\sum_{L\ge1}s_L\to5$ as $N_p\to\infty$ | [[concepts/s_L_block_weights]] | this work, verified |
| $\rho_{\rm scan,req}\simeq\Phi^{-1}(1-p_{\rm fa}/K_L)+\Phi^{-1}(P_{\rm det})$ | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Sec. 9.2 |
| Poisson $C_\ell$ stat $\lVert x\rVert^2\sim\chi^2_{K_L}(\rho^2)$; $\rho_{C_\ell,req}$ from non-central $\chi^2$ | [[concepts/Cl_over_C0]] | [[sources/pta_point_source_multipole]] Sec. 9.3 |
| independent-beam analytic upper estimate $\rho_{C_\ell}/\rho_{\rm scan}=1.13,1.16,1.21,1.27,1.33,1.38$ ($L=1..6$, $p_{\rm fa}=0.05$) | [[concepts/fisher_hierarchy]] | `tab:detection`, [[sources/pta_point_source_multipole]] Sec. 9.4 |
| fixed/common-variate full-sky MC ratio $=1.0000\pm0$, $1.0831\pm0.0048$, $1.1384\pm0.0051$, $1.2072\pm0.0038$ for $L=1..4$; $L=1$ equality exact | [[concepts/fisher_hierarchy]] | `paper_v2/data/detection_penalty_mc.json` |
| NP equivalence: covariance profiled LR $T_\star=\max(s-1-\ln s,0)$ monotone in coherent $s$ ⇒ equal $P_{\rm det}$ | [[concepts/matched_filter_vs_power]] | [[sources/pta_point_source_multipole]] Sec.; [[sources/pn_coherent_vs_stochastic_single_source]] |
| required $p_1=\rho_{\rm req}/(\alpha\rho_0)$; e.g. $\rho_0=20,L\le2$: scan $0.09$, $C_\ell$ $0.10$ | [[concepts/brightest_source_fraction]] | [[sources/pta_point_source_multipole]] |

### Source-vs-power-map evidence toy (Gaussian, notebook-ready)

| Statement | Concept | Source |
|---|---|---|
| $r(s,q)=(1+q)^{-1/2}\exp[qs/(2(1+q))]$ (one-pixel LR) | [[concepts/coherent_vs_incoherent]] | [[sources/toy_model_source_vs_power_map]] Sec. 12 |
| $b_{\rm mean}(s;\sigma^2)=(1+\sigma^2)^{-1/2}e^{\sigma^2 s/2(1+\sigma^2)}$; $b_{\rm cov}(s;\sigma^2)=\mathbb E_{a\sim N(0,\sigma^2)}[r(s,a^2)]$ | [[concepts/coherent_vs_incoherent]] | [[sources/toy_model_source_vs_power_map]] Sec. 4 |
| One source SUMS over locations ($N^{-1}\sum$); maps MULTIPLY ($\prod$) | [[concepts/matched_filter_vs_power]] | [[sources/toy_model_source_vs_power_map]] Sec. 9 |
| $\mathbb E_{\rm empty}[B_\ell(C_\ell)\mid s]=b_{\rm cov}(s;V_1)$, $V_1=\sum_k C_k$ (averaged Bayes factor) | [[concepts/source_background_degeneracy]] | [[sources/toy_model_source_vs_power_map]] Secs. 15-16 |
| $\ell_0(q)=-\tfrac12\log(1+q)+q/(2(1+q))<0$ (per-empty-pixel typical-log-evidence penalty) | [[concepts/KL_divergence]] | [[sources/toy_model_source_vs_power_map]] Sec. 17 |

### Joint resolved+unresolved SMBHB search (companion draft)

| Statement | Concept | Source |
|---|---|---|
| $p(h_{\rm cw})=h_{\rm s,peak}^2\,(dN/dh_s^2)\,\exp(-\int_{x}^\infty dN/dx\,dx)$ (brightest-source PDF) | [[concepts/brightest_source_fraction]] | [[sources/joint_search_resolved_unresolved]] App. p_hmax |
| $N_c$ as SMBHB-origin detection statistic; $N_c\ge1000$ Gaussian-limit null | [[concepts/SMBH_population_model]] | [[sources/joint_search_resolved_unresolved]] |
| NG15 CW detection prob.: $0.6\%$ (15yr) / $2\%$ (20yr) at SNR 5; 24/114 AGN candidates in tension | [[concepts/fisher_hierarchy]] | [[sources/joint_search_resolved_unresolved]] |

### Matched filter vs power (toy)

| Statement | Concept | Source |
|---|---|---|
| $\mathrm{SNR}_{\rm matched}=A\sqrt M$ | [[concepts/matched_filter_vs_power]] | [[sources/matched_filter_vs_power]] Sec. 2.2 |
| $\mathrm{SNR}_{\rm power}=MA^2/\sqrt{2N}$ | [[concepts/matched_filter_vs_power]] | [[sources/matched_filter_vs_power]] Sec. 2.4 |
| $K_{\rm eff}^{\rm sphere}\sim 4\pi/\theta_c^2$ | [[concepts/matched_filter_vs_power]] | [[sources/matched_filter_vs_power]] Sec. 3.6 |
| Rice upcrossing: $\langle N_{\rm up}(u)\rangle = \sqrt\Lambda\,e^{-u^2/2}$ | [[concepts/matched_filter_vs_power]] | [[sources/matched_filter_vs_power]] Sec. 3.5 |

### Prior sensitivity (toy)

| Statement | Concept | Source |
|---|---|---|
| Ridge posterior $p(c\mid S)\propto p(c)L_{\rm off}(c)\prod_i\pi_v(u_i-c)$ | [[concepts/prior_sensitivity]] | [[sources/pta_prior_sensitivity]] Sec. 3 |
| Hierarchical factor $[b+\sum_i(u_i-c)]^{-(a+N_p)}$ | [[concepts/prior_sensitivity]] | [[sources/pta_prior_sensitivity]] Sec. 5 |

### Sqrt-SH basis and NANOGrav methods

| Statement | Concept | Source |
|---|---|---|
| $P(\hat\Omega) = [\sum_{LM}b_{LM}Y_{LM}]^2$ | [[concepts/sqrt_SH_basis]] | [[sources/arxiv_2103_00826]] Sec. 3, [[sources/arxiv_2006_04810]] Appendix A |
| $c_{\ell m}=\sum b_{LM}b_{L'M'}\beta^{LM,L'M'}_{\ell m}$ (CG coupling) | [[concepts/sqrt_SH_basis]] | [[sources/arxiv_2103_00826]] Eq. 3.7 |
| $\ell_{\max}^b=\ell_{\max}^a/2$ (CG truncation) | [[concepts/sqrt_SH_basis]] | [[sources/arxiv_2103_00826]] Sec. 3; [[sources/arxiv_2006_04810]] App. A |
| Hellinger distance $H(P,Q)=\tfrac{1}{\sqrt 2}\sqrt{\sum(\sqrt{p_i}-\sqrt{q_i})^2}$; NANOGrav finds $H\approx 0$ at all $\ell,f$ | [[concepts/sqrt_SH_basis]] | [[sources/arxiv_2306_16221]] Fig. 5 |
| ORF: $\Gamma_{ab}\propto \int P(\hat\Omega)[F^+_a F^+_b + F^\times_a F^\times_b]d^2\Omega$ | [[concepts/transfer_function]] | [[sources/arxiv_2306_16221]] |

### Shot noise and LSS

| Statement | Concept | Source |
|---|---|---|
| $C^{\rm SN}_{\ell>0,h^2}=4\pi/N_{\rm eff}$ (flat in $\ell$) | [[concepts/shot_noise]] | [[sources/arxiv_2602_16808]] Eq. 9 |
| $C^{\rm SN}_{\ell>0,h^2}\propto f^{8/3}$ (GW-driven inspiral) | [[concepts/shot_noise]] | [[sources/arxiv_2602_16808]] Eq. 12 |
| $\langle h^4\rangle\propto \int dM\,M^5\,dn/dM$ | [[concepts/shot_noise]] | [[sources/arxiv_2602_16808]] Eq. 18 |
| $C_{\ell,h^2}^{\rm LSS}$ from Limber projection | [[concepts/shot_noise]] | [[sources/arxiv_2602_16808]] Eqs. 24–26 |
| $C_\ell/C_0\propto 1/[1+(f/f_\ast)^{-11/3}]$ | [[concepts/shot_noise]] | [[sources/arxiv_2305_05690]] |
| $\hat C_{\rm shot}/(4\pi)=\hat h_c^4/(\hat h_c^2)^2=\sum_a p_a^2$ (per realization; $=1/N_{\rm eff}$) | [[concepts/N_eff]] | [[sources/arxiv_2608_09929]] Eq. 10 |
| $1/N \le \sum_a p_a^2 \le 1$ (inverse participation ratio bounds) | [[concepts/shot_noise]] | [[sources/arxiv_2608_09929]] Eqs. 12-15 |
| realized $\hat C_{\rm shot}\propto f^{1.1-1.2}$, **not** $f^{8/3}$ (the $\le1$ ceiling) | [[concepts/shot_noise]] | [[sources/arxiv_2608_09929]] Sec. III A |
| $P(y\mid\tilde x)=\int dx\,P(y\mid x)P_{\rm noise}(x\mid\tilde x)$, $x=\log_{10}\hat h_c^2$ | [[concepts/shot_noise]] | [[sources/arxiv_2608_09929]] Eq. 16 |
| $\left.\frac{dt_r}{d\ln f_r}\right|_{\rm tot}=\left.\frac{dt_r}{d\ln f_r}\right|_{\rm GW}[1+(f_b/f_r)^\kappa]^{-1}$, $\kappa=10/3$ | [[concepts/SMBH_population_model]] | [[sources/arxiv_2608_09929]] Eq. 17 |

### Population model (SMBH)

| Statement | Concept | Source |
|---|---|---|
| $\hat P(\omega)=\exp[\int dh_s^2\,(dN/dh_s^2)(e^{i\omega h_s^2}-1)]$ (char. fn.) | [[concepts/SMBH_population_model]] | [[sources/arxiv_2406_17010]] |
| $h_c^2=h_{c,0}^2\,\exp(\tfrac{25}{18}\varepsilon^2\ln^2 10)$ (scatter boost) | [[concepts/SMBH_population_model]] | [[sources/arxiv_2312_06756]] |
| $\rho_{\rm BH}=\rho_{\rm BH,0}\,\exp(\tfrac12\varepsilon^2\ln^2 10)$ (density boost) | [[concepts/SMBH_population_model]] | [[sources/arxiv_2312_06756]] |
| $N_c\sim 1\cdot(h_c/2.4\times 10^{-15})^2(M_{\rm peak}/10^{10}M_\odot)^{-10/3}(f/0.3\,{\rm yr}^{-1})^{-11/3}$ | [[concepts/SMBH_population_model]] | [[sources/arxiv_2406_17010]] |
| Double-Schechter GSMF (Liepold-Ma) → single-Schechter BHMF | [[concepts/SMBH_population_model]] | [[sources/arxiv_2407_14595]] Eqs. 3-4 |

### Amplitude normalization and individual-source strain

| Statement | Concept | Source |
|---|---|---|
| $\langle h_c^2\rangle\propto\phi_\sigma$ (linear; $h_s^2$ independent of $\phi_\sigma$) → exact calibration to $\sqrt{\langle h_c^2\rangle(1\,{\rm yr}^{-1})}=2.5\times10^{-15}$ | [[concepts/SMBH_population_model]] | `gwb_sources.calibrate_phi_sigma`; [[reproducibility]] |
| $\kappa(\varepsilon)=$ 13.26 (0.20), 6.14 (0.38), 0.72 (0.66) — $\phi_\sigma$ multipliers vs fiducial $2.611\times10^{-2}$ | [[concepts/SMBH_population_model]] | this work, 2026-06-22 |
| $h_s^2 = h_0^2\,(f/\Delta f) = h_0^2\,f\,T_{\rm obs}$ ($T_{\rm obs}=16.03$ yr) → $h_0=\sqrt{h_s^2/(f\,T_{\rm obs})}$ (per-source char. strain ↔ incl/pol-avg CW amplitude) | [[concepts/brightest_source_fraction]] | [[sources/arxiv_2406_17010]] Eqs. h0, tildehs2 |

### Polarization weights

| Statement | Concept | Source |
|---|---|---|
| $g_I=(1+\cos^2\iota)^2/4+\cos^2\iota$; $g_V=\cos\iota(1+\cos^2\iota)/2$; $g_L=\sin^4\iota/4$ | [[concepts/SMBH_population_model]] | [[sources/arxiv_2305_05690]] |
| $\int g_I^2/4\pi=284/315$; $\int g_V^2/4\pi=92/105$; $\int g_L^2/4\pi=8/315$ | [[concepts/SMBH_population_model]] | [[sources/arxiv_2305_05690]] |

### Spectral variance

| Statement | Concept | Source |
|---|---|---|
| ${\rm Var}[\Omega_{\rm GW}]\propto f^{26/3-\lambda}$ | [[concepts/SMBH_population_model]] | [[sources/arxiv_2407_06270]] Table 1 |
| ${\rm Var}/{\rm Mean}$ is $\lambda$-independent | [[concepts/SMBH_population_model]] | [[sources/arxiv_2407_06270]] |

### Isotropy matching (from 2006.04810)

| Statement | Concept | Source |
|---|---|---|
| M=0.98 ORF match: SMBHB-population sky vs isotropy | [[concepts/sqrt_SH_basis]] | [[sources/arxiv_2006_04810]] |
| Suboptimal/optimal SNR ratio ≈ 0.97 for SMBHB isotropic template | [[concepts/source_background_degeneracy]] | [[sources/arxiv_2006_04810]] |

## Naming discipline

- A formula has at most **one** canonical owner (the concept page in the "Concept" column).
- Paper labels are the identity for equations that appear in the paper.
- Adding a paper equation: add a `\label{eq:…}`, append a row above,
  set its concept owner, and reference the source section.
