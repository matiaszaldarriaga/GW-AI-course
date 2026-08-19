# Critique of the proposed App. B memo revision

**Verdict (one line).** Accept with revisions — the main reframe is correct and an improvement, but §4/§6 of the sanity-check have at least one concrete numerical error (the 3.8σ "one-sided vs two-sided" worry is unfounded), the §6 $k$-saturation constant is off, and the §5 detection-ratio derivation is dimensionally loose and should be cleaned.

**Date.** 2026-04-20.

**Reviewed documents.**
- Proposal: `wiki/notes/app_B_memo_revision_proposal.md`
- Current memo: `wiki/notes/app_B_coherent_fisher_critique.md`
- Pedagogical note: `references/coherent_vs_stochastic_single_source.md`
- P1: `wiki/notes/app_B_2pol_equivalence_check.md`
- P2: `wiki/notes/app_B_anisotropic_response.md`
- Paper: `references/sufficient_statistics_4-16-2026.pdf`, §IV (pp. 7–10), App. B (pp. 14–15).

---

## 1. Verdict

**Accept with revisions.** The proposal correctly identifies the main defect of the current memo — that the "Step 1 stochasticization demotes $\rho^2$ from $\propto H$ to $\propto H^2$ **at detection**" framing is wrong and conflates two distinct issues (the data-generating-process question, which the pedagogical note settles; and the parameter-estimation question, which is about Fisher curvature, not p-values). The replacement structure — one main critique (the Eq. 50 same-power null) plus two minor ones (parameter-interpretation, anisotropic-response) — is the right decomposition and is internally consistent with P1 and P2. The mathematical core of §4 of the revised memo (the $T_{1^\star} = \max(s - 2 - 2\ln(s/2), 0)$ derivation, its monotone equivalence, and survival under sky-max) is rigorous and imported cleanly from P1. The §5 ceiling, §6 Fisher-on-$q$, and §7 anisotropic-response material are all substantively correct at the level of stated conclusions.

Most important revisions before merging:

1. **Retract the "3.8σ vs 3.6σ" worry in the proposal's §4 sanity check.** The paper's 3.8σ is correct one-sided (3.78σ from $p[\chi^2_4>24] = 7.99\times 10^{-5}$). The proposal's implication that the paper uses a look-elsewhere or kernel correction to bump "3.6" to "3.8" is unfounded and should not appear in the final memo.
2. **Fix the $k$-saturation constant in §6.** For App. B $k=2$ (two complex polarizations, 4 real d.o.f.), so at large $q$ one has $2q^2 F_{qq}(q) \to 2$ — not "a finite constant" left generic, and not $k$ in the real-dimension sense. State it explicitly.
3. **Tighten the §5 "detection ratio" derivation.** The intermediate expression $\hat H|_{H_1}/\langle\hat H|_{H_0}\rangle/2$ = 12 is dimensionally a sanity check, not a significance, and is easy to misread. Collapse to the one-line $\hat H|_{H_0} \sim (f_\sigma H/2)\chi^2_4 \Rightarrow \hat H|_{H_1}=H$ implies $\chi^2_4 = 2/f_\sigma = 24$.
4. **Add a one-line caveat in §4.4** about sky-max survival in the non-isotropic case (P2 is silent; the revised memo's §7 stays silent; the proposal's own sanity note §4.2 flags this — the memo should state explicitly that §4.4's argmax result is only a theorem in the isotropic limit).
5. **Tighten the "typical NG15" language in §7** per the proposal's own §4 sanity item (2). P2 doesn't compute a sky-average; it computes a "typical sky position" number from $r\sim 2$. Keep that phrasing.
6. **Ensure the lead "one-sentence conclusion" states the scope.** The current revised lead doesn't say "in the App. B isotropic toy limit" until the body. A reader skimming the lead could take away the wrong headline. Move "in the toy limit" into the lead explicitly.

The proposal's §1 retain/reframe/remove table, §2 structural rationale, and §3 revised-memo draft are otherwise publishable as-is subject to the fixes in §7 of this critique.

---

## 2. Mathematical issues

1. **"$p[\chi^2_4 > 24] \sim 3\times 10^{-4} \sim 3.8\sigma$" — numeric value is right, the proposal's §4 sanity check is wrong to flag it.** Proposal §4, "Statements needing numerical check": "the $\chi^2_4$ argument used here gives $\simeq 3.6\sigma$, so either the draft is adding a different factor (e.g. accounting for sky max under $H_0$, a look-elsewhere inflation...) or the factor of 12 is not exactly right."

   This is incorrect. Direct computation: $p[\chi^2_4 > 24] = 7.99\times 10^{-5}$. The one-sided Gaussian equivalent is $\Phi^{-1}(1 - p) = 3.78\sigma \approx 3.8\sigma$. The paper's value is exact, no correction factor needed. The "3.6σ" arises only if one reads $p\simeq 3\times 10^{-4}$ (from the proposal's own slightly-loose statement "$\sim 3\times 10^{-4}$", off by a factor of 4 from the true $8\times 10^{-5}$) and then two-sided-converts it. The true $p$ is $8\times 10^{-5}$, and the draft is using the standard one-sided convention.

   **Fix.** Remove the entire §4.1 "numerical item to verify" in the proposal's sanity check. Replace with: "Direct computation gives $p[\chi^2_4 > 24] = 7.99\times 10^{-5} \to 3.78\sigma$ one-sided, matching the draft's '~3.8σ' at the quoted precision." Also tighten the revised memo's §5 text from "$\sim 3\times 10^{-4}$" to "$\sim 8\times 10^{-5}$" to remove the ambiguity that apparently seeded the confusion.

2. **$k$-saturation constant in §6.** Proposal §3, revised memo §6: "$2q^2 F_{qq}(q) \to k$ — a **finite constant**, independent of measurement quality." Proposal §4, sanity item 3: "For App. B, $k=2$ (two complex polarizations → 2 modes), so the saturation constant is 2, not 1."

   The sanity-check item 3 is correct and the body of the revised memo should state it numerically. More precisely: Parametrization 2 of the current memo (§5.1) already has $F_{qq}(q) \to k/(2q^2)$ where $k$ is the **number of complex modes** = **2** in the App. B case. The saturation is $2q^2 F_{qq} \to 2$. The CMB analogy $\mathrm{Var}(\hat C_\ell)/C_\ell^2 \to 2/(2\ell+1)$ at $N_\ell\to 0$ maps to App. B with effective mode count $1/f_\sigma = 12$ (not 2). The difference between these two numbers — 2 (complex modes per polarization pair) vs 12 (effective modes from the $z_\ell$ kernel) — is not discussed in either the current memo or the revised memo and is the actual substance of the CMB parallel. The revised memo's §6 collapses them in a way that obscures the distinction.

   **Fix.** In §6 of the revised memo, be explicit that there are two Fisher saturations: (a) the $k=2$ complex-polarization saturation, relevant to a single-frequency-bin source with both polarizations live; (b) the $1/(2\ell+1) \leftrightarrow f_\sigma$ kernel-effective-mode count relevant to App. B's $\hat H = |\hat h_{+2}|^2 + |\hat h_{-2}|^2$ power estimator under a realized GWB null. They are different objects. The $3.8\sigma$ ceiling of §5 uses (b), not (a); the cosmic-variance-limited-power-measurement statement of §6 uses (b) for the estimator and (a) for the Fisher on $q$.

3. **Detection-ratio form in §5.** Proposal §3, revised memo §5: "$\hat H|_{H_1}/\langle\hat H|_{H_0}\rangle/2 = H/(f_\sigma H) = 1/f_\sigma = 12$, a number independent of $H$."

   The object $\langle\hat H|_{H_0}\rangle/2$ is not dimensionally a significance (it is half the null mean), and the division by 2 is ad hoc. The clean statement is: under $H_0$, $\hat H \sim (f_\sigma H/2)\chi^2_4$; under $H_1$ (noise-free), $\hat H = H$ deterministically; so a realized $H_1$ observation gives $\chi^2_4$ tail at the value $2H/(f_\sigma H) = 2/f_\sigma = 24$, which is $p[\chi^2_4>24] = 7.99\times 10^{-5} \to 3.78\sigma$ one-sided.

   **Fix.** Drop the "detection ratio" intermediate. Go directly from the distribution $\hat H|_{H_0} \sim (f_\sigma H/2)\chi^2_4$ to the tail probability at the realized $H_1$ value $\hat H = H$.

4. **Single-template case and $T_{1^\star}^{(k)}$ general formula.** Proposal §3 revised memo §4.5 claims the $T_{1^\star}^{(k)} = \max(s - k - k\ln(s/k), 0)$ family. Verified directly for $k=1$ (pedagogical note §3: $T_{1^\star} = \max(s-1-\ln s, 0)$; yes, zero at $s=1$, derivative $1-1/s>0$, matches) and $k=2$ (P1 §3.3: $T_{1^\star} = \max(s - 2 - 2\ln(s/2), 0)$; derivative $1-2/s>0$ for $s>2$, zero at $s=2$, matches). The derivation via Woodbury + matrix-determinant-lemma in P1 §3.1-3.2 is correct. The $1+\alpha \to s/2$ substitution in P1 §3.3 is algebraically clean. **No error here**, just marking verified.

5. **Sky-maximization argument.** Pedagogical note, P1 §5, and proposal §3 revised memo §4.4 all invoke "max of a non-decreasing function = function of max" to argue that sky-maximization preserves monotone equivalence. The argument is correct **in the isotropic limit** where $\rho^2$ is sky-independent so $s(\hat n_s)$ is the only $\hat n_s$-dependence in both statistics. Outside the isotropic limit, $\rho^2_{1,2}(\hat n_s)$ are both sky-dependent and the map $\vec v \mapsto T_{1^\star}(\vec v)$ depends on $\hat n_s$ explicitly through the eigenvalues, so the "function of max" argument fails. P2 is silent on this, and P2's §3.2 numbers are explicitly at **fixed sky**, per the proposal's own §4.2 sanity check. **This is correctly flagged by the proposal** but the proposal's own revised memo §7 does not state it clearly enough.

   **Fix.** Add a sentence to the revised memo §4.4: "The argmax-$\hat n_s$ coincidence is a theorem only in the isotropic limit; in the realistic case the argmax sky direction can differ between $T_1$ and $T_{1^\star}$ at the level of the eigenvalue spread, and this is a second piece of the §7 breakdown."

6. **$F_{H_1^\star}(\mu^2) = \rho^4/[2(1+\alpha)^2]$.** Proposal §2 "What to check" item A.6. Pedagogical note §5.2 derives this via $\vec t^\dagger \Sigma^{-1}\vec t = \rho^2/(1+\alpha)$ squared, times $1/2$ from the $\tfrac12\mathrm{tr}[\cdots]$ Gaussian covariance term. Verified. **No error.**

7. **CMB cosmic-variance expression $\mathrm{Var}(\hat C_\ell) = 2(C_\ell+N_\ell)^2/(2\ell+1)$.** Standard, stated correctly. **No error.**

8. **Anisotropic-response eigenbasis formulas in P2 §3.1, carried to revised memo §7.** $T_1 = \sum_i |v_i|^2/\rho_i^2$ and $T_{1^\star} = \sum_i w_i |v_i|^2/\rho_i^2 - \sum_i\ln(1+q\rho_i^2)$ with $w_i = q\rho_i^2/(1+q\rho_i^2)$. Derived in P2 §3.1 via diagonalization of $F = U^\dagger N^{-1} U$. Correct, though the revised memo should note that the $T_1$ form assumes the **profile** (over $\vec h$) LLR; for the specific App. B toy of equal eigenvalues ($F\propto I_2$) both reduce correctly to the §4 results. The "monotone iff all $\rho_i^2$ equal" claim is also correct by the P2 §3.1 reweighting argument. The numerical entries in the table ($r=1.1 \to \Delta = 0.24$, $r=2 \to \Delta = 1.67$, $r=10 \to \Delta = 4.09$) come from the explicit formula $\Delta = 5(r-1)/(r+1)$ which is algebraically right for the "$T_1 = 10$, $q\rho_2^2 = 1$" setup. **No numerical error, but the table's interpretation needs to match P2's own wording** (see §2.5 below).

---

## 3. Conceptual issues

1. **Internal tension between the "three pictures" table (revised §4 in the proposal's retain/reframe map) and the reframed §5.1.** The proposal's retain/reframe table says §4 (three pictures / three scalings) is "reframed, not dropped." But the revised memo in §3 of the proposal simply drops the A / A′ / B table entirely in favor of the monotone-equivalence treatment in revised-§4. The A / A′ / B three-column table does not appear anywhere in the revised-memo draft in §3 of the proposal.

   Is dropping it right? In my reading, **yes**: the A-A′-B row "lossy step taken" in the current memo's §4 embeds the same conflation that the reframe is fixing. Keeping the table and trying to add caveats in-line would just muddy the presentation. But the proposal's retain/reframe table advertises "reframe" when in practice the draft "removes". This is a cosmetic inconsistency in the proposal — and a reader using the retain/reframe table as a diff checklist will notice.

   **Fix.** Change the disposition of §4 in the proposal's §1 table from "Reframe" to "Remove; its content is absorbed into the new §4 (monotone equivalence) and §5 (ceiling)". No change to the actual revised memo is needed.

2. **"Physics vs modeling" distinction.** The proposal correctly separates (a) the $\alpha$-vs-$\alpha^2$ KL gap that lives in the data-generating process (§5.4 of the pedagogical note) from (b) the $T_1$-vs-$T_{1^\star}$ analyst-modeling choice. Revised §6 of the proposed memo has the Aside "the $\alpha$-vs-$\alpha^2$ KL gap" which is a faithful import of §4 of the pedagogical note. **No conflict remaining.**

3. **Why does the 3.8σ ceiling appear if monotone equivalence holds?** This is the conceptually tricky question the caller flagged. The answer, which the revised memo §5 essentially gets right: the monotone equivalence (§4) is computed **against a noise-only null** — both $T_1$ and $T_{1^\star}$ are constructed as log-LRs vs $H_0: \vec a \sim \mathcal{CN}(0, N)$. The paper's $3.8\sigma$ ceiling is **not against this null**; it is against the **same-power GWB null** of Eq. (50), $H_0: \vec a \sim \mathcal{CN}(0, N + q_{\rm GWB}UU^\dagger)$ with $q_{\rm GWB}$ matched to the $H_1$ power. Changing the null changes the null distribution of the **same statistic** (both $T_1$ and $T_{1^\star}$ inherit the ceiling, not just $T_{1^\star}$).

   Verify by reading p. 8 of the draft: the $\hat H|_{H_0} \sim (f_\sigma H/2)\chi^2_4$ distribution of Eq. (48) is the null distribution of the matched-filter amplitude estimator $\hat H = |\hat h_{+2}|^2 + |\hat h_{-2}|^2$ (which is $T_1$ up to a sky-independent factor) **under the GWB null**. So the ceiling lives in the **choice of null**, not in the choice of statistic. The revised memo states this correctly in §5's last paragraph: "Change the null to noise-only (with the GWB handled as a profiled nuisance) and the ceiling disappears."

   **This is a significant conceptual improvement over the current memo**, which wraps the ceiling together with the stochasticization into a single "two lossy steps" narrative. The proposal's disentangling is correct.

4. **Is the anisotropic-response critique stated at the right level of strength?** The revised memo §7 says "quantitatively mild ($\lesssim 5\%$ threshold shift, 10–20% rank disagreement)". P2 §5 says "two orders of magnitude smaller than the scaling-level critiques". These agree, but the revised memo's §7 language could be read as saying the *equivalence breaks* only slightly; P2's own verdict is that the equivalence **strictly fails** (rank disagreement is not small — 10–20% is big on an individual-realization basis), but the p-value consequences are small. The revised memo preserves this distinction well with the explicit "two orders of magnitude smaller than the Eq. (50) ceiling" qualifier, but it could be one sentence sharper.

   **Fix (optional).** In §7, add a sentence: "The rank-level disagreement (10–20% of $T_1$ on typical sky positions) is not itself small; the smallness is specifically in the p-value shift, because the null distributions shift in compensating ways (P2 §3.3)."

5. **§11 cross-reference to `fisher_hierarchy`.** The proposal's revised §11 says the $p$-hierarchy is a multi-source ensemble statement and is orthogonal to the single-source equivalence theorem. Reading `wiki/concepts/fisher_hierarchy.md`, this is correct: the hierarchy is derived for a population with brightest-source fraction $p$, not for a single source. The single-source problem of App. B is exactly the limit where the hierarchy degenerates (there is only one source, so $p = 1$). No conflict. **Reframing is correct.**

   One note: `fisher_hierarchy.md` says "The linear-in-data object here is $\hat{\vec h}$; the quadratic-in-data object is $\hat q = |\hat{\vec h}|^2/k$. Turning the former into the latter is the App. B step that costs the coherent order." This language is **from the current memo's §10** and is now superseded by the proposal. If `fisher_hierarchy.md` were to be updated later it would need a parallel edit, but that is not the scope here. The proposal's §4.3 sanity check flags this for follow-up, which is correct.

---

## 4. Fidelity to the paper

1. **Eq. 48 and how the 3.8σ is derived.** Paper, p. 8 bottom / p. 9 top:
   > "This shows that, even if $\sigma_a^2 \to 0$, the matched filter statistic cannot distinguish between a GWB and a single source to infinite significance. If we define the estimator for the amplitude of a source as $\hat H = |\hat h_2|^2 + |\hat h_{-2}|^2$, then $\hat H = (f_\sigma H/2)\chi^2_4$ for $\sigma_a^2 \to 0$. The detection significance is then given by $p[\hat H > H] = p[\chi^2_4 > 2/f_\sigma = 24]$. This yields a maximum possible significance of ~3.8σ."

   So the paper derives the ceiling **exactly as the proposal's revised §5 reproduces it**, with $f_\sigma = 1/12$ and the $\chi^2_4$ tail at 24. The derivation in §5 of the revised memo is a faithful reproduction. **Fidelity confirmed.**

2. **Eq. 50's role.** Paper, p. 9, bottom-left column, immediately after §IV.A and before launching §IV.B:
   > "In order to enforce that the power spectra are the same, we introduce the prior probability [Eq. 50]: $\ln\pi(\vec h|\sigma_h^2) \propto -|\vec h|^2/(2\sigma_h^2)$, and marginalize $p(\vec a|\vec h, H_1)$ over the amplitudes $\vec h$."

   Read in context, Eq. 50 is a **prior on the source amplitude** used to construct the $H_1^\star$ likelihood by marginalization. The matching of power spectra ("enforce that the power spectra are the same") between $H_0$ and $H_1^\star$ is accomplished by choosing $\sigma_h^2$ such that $\langle|\vec h|^2\rangle = \sigma_h^2$ equals the GWB power. So Eq. 50 is logically two things at once:
   (a) the Gaussian prior needed to marginalize and get a closed-form $H_1^\star$ likelihood (the stochasticization);
   (b) the choice of $\sigma_h^2$ that enforces the power-matching with $H_0$.

   The proposal's language, revised §1: "**Eq. (50) same-power null.** Under $H_0$ pinned to the isotropic GWB with trace-matched power...". This is substantively right — Eq. 50 *does* produce the same-power null when the $\sigma_h^2$ is matched — but it slightly collapses (a) and (b). A precise reading of the paper: Eq. 50 is the prior, the power-matching is the **choice of $\sigma_h^2$ in Eq. 50**, and the combination is what pins the null to the matched-power GWB in the following Neyman-Pearson comparison.

   **Fix.** In the revised memo §5, replace "Eq. (50) pins the null to the isotropic GWB with total power $\sigma_h^2$ matched to $\langle |\vec h|^2\rangle$" with the cleaner "The paper uses Eq. (50) as a Gaussian prior on the source amplitudes and then equates its variance $\sigma_h^2$ to the GWB power, which is equivalent to pinning the null to the matched-power GWB in the comparison." A small edit, but avoids a reader objecting "Eq. 50 is a prior, not a null."

3. **Does the paper work in the isotropic limit throughout?** Paper pp. 8-10: the analytical $3.8\sigma$ derivation (Eq. 48) sits in a paragraph that begins "Suppose we are trying to fit a single source in the $\hat z$ direction and assume that the noise covariance is diagonal $N_{\alpha\beta} = 4\pi/N_p^w \delta_{\alpha\beta} \equiv \sigma_a^2 \delta_{\alpha\beta}$" — so yes, the analytical ceiling uses the **diagonal / isotropic** approximation (Eq. 32 cited on p. 9).

   §IV.C (marked p. 10+ in the PDF but truncated in the reading) reports NG15 numbers $\rho_{\rm HD}=3.14$, $\sigma_{C_2}=0.9$ etc., and §IV.A Fig. 5 uses the full Fisher matrix $F_h = U^\dagger N^{-1}U$ without the isotropic approximation for the NG15 eigenvalue plot. So **P2's claim that the analytical ceiling is isotropic-limit only, but the NG15 numbers use the full Fisher, is correct**. The proposal §4 sanity item (and the proposal's imported P2 §4.3 list of which numerical results survive) is accurate.

4. **The "no distinction between continuous-wave and anisotropic searches" paper language.** Paper p. 9, top-right column:
   > "Note that this leads to an exact correspondence between template-based and stochastic searches, shown in Ref. [17]. Thus, there is no distinction between continuous-wave and anisotropic searches in the following discussion."

   This is exactly the claim the revised memo §4 rigorizes **and** the revised memo §7 qualifies. The proposal's editorial recommendation (revised §10 item 8) to "replace 'no distinction between continuous-wave and anisotropic searches' with the narrower statement that in the toy limit the two constructions share the same quadratic invariant $s$" is a substantive improvement and is fully faithful to the paper's derivation + P2's correction. **Well-aimed.**

---

## 5. Completeness and clarity

1. **What from the current memo is being dropped that shouldn't be?**
   - The current memo's §4 (three-picture table A / A′ / B) is dropped. **Agree it should be dropped**; see §3.1 of this critique.
   - The current memo's §5.1 (Parametrization 1 and 2 analysis, $F_{\mu\mu}^{\rm cov}(0)=0$ identity) is retained as §6 of the revised memo, reframed as "parameter interpretation". **Agree.**
   - The current memo's §6 ("Why the two paths happen to share $T$: three conditions") is replaced by the revised §4.5. **Agree.** The three-condition list is preserved in §4.5 with more rigor.
   - The current memo's §8 ("Internal inconsistency in the prior") survives as §9 of the revised memo. **Agree, retained.**

2. **Is there content from P1 and P2 that should be in the revised memo but isn't?** P1 §6 "Variations of the prior — where the equivalence breaks" (the non-isotropic prior case) is not imported into the revised memo. This is a **different** breakdown mechanism from the anisotropic-response breakdown of P2/§7 — it concerns the $Q\neq qI_2$ prior, not the $F \neq \rho^2 I_2$ response. The proposal's revised §4.5 briefly mentions "isotropic prior" as one of two symmetries required and notes that breaking either breaks the equivalence, but the memo doesn't state the non-isotropic-prior case as a separate observation.

   **Optional fix.** Add one sentence to §4.5: "For completeness: the equivalence would also break under a non-isotropic prior $Q\neq qI_2$, as the resulting Bayes factor would depend on $s_+$ and $s_-$ separately rather than on $s = s_++s_-$ (P1 §6). This is not a modeling concern for App. B as written, since its prior is isotropic by choice; the empirically-relevant breakdown is the response-anisotropy one of §7."

3. **Is the one-sentence headline the right one?** The current revised lead:
   > "Eq. (B6) is the right statistic in the App. B toy limit, and in that limit the profile-likelihood and Bayes-factor constructions produce monotone-equivalent tests — the stochasticization does not cost anything at the detection stage. The genuine detection-level critique is the Eq. (50) same-power null, which caps the significance at $\sim 3.8\sigma$ no matter how bright the source..."

   This is the right headline. Two suggestions:
   - The headline should call out "in the App. B toy limit" at the beginning of the second sentence too, since the "stochasticization does not cost anything at the detection stage" clause will be quoted out of context otherwise.
   - The phrase "the genuine detection-level critique" is slightly odd because §6 and §7 are also stated as critiques, just not at the detection stage. Fine as is, but consider "the single scaling-level critique" instead of "genuine."

4. **"Integrate likelihood vs log-likelihood" from the earlier iteration.** I do not see this content appearing in either the current memo or the revised memo. The pedagogical note does not address it either. Looking at the current memo: §7 handles the Gaussianization step but not specifically an "integrate $\mathcal L$ vs $\ln\mathcal L$" distinction. If there was an earlier iteration that had this material, it has been **dropped**, and it should be assessed whether that drop was deliberate. My read: it was subsumed correctly under the broader "Gaussianization is fine at PTA SNR" argument (§7 of current / §8 of revised). **No action required** unless the user wants the distinction made explicit.

5. **Project $p$-hierarchy.** Revised §11 handles this cleanly. See §3.5 of this critique. **No issue.**

6. **Overall length.** Proposal says ~1500 words of revised memo + ~1200 of wrapper, 4-5 pages. Realistic. Reasonable.

7. **Missing: a one-line "where the 3.8σ comes from, precisely" in §5.** The revised §5 derives the ceiling correctly but a reader who wants the one-liner has to read through the whole section. Consider adding an italicized one-liner at the top of §5: "*The ceiling is a property of the choice of null, not of the choice of statistic.*"

---

## 6. Approved text

The following sections of the revised memo (proposal §3) are ready to merge unchanged, subject to the fixes in §2 and §5 of this critique:

1. **Revised §2 "Two statistics in the draft."** Retained verbatim from current §2. Correct and useful.
2. **Revised §3 "Coherent derivation of $T(\hat n)$."** §3.1, §3.2, §3.3 are verbatim from current §3 and correctly derive Eq. B6 as the matched filter in the diagonal-noise / $N_\ell$-constant toy limit. Well-written.
3. **Revised §4.1–§4.3** (setup, profile LLR, Bayes-factor LLR). Direct import from P1 §1-§3. Rigorous.
4. **Revised §4.4** (monotone-equivalence theorem and survival under sky-max). Import from P1 §4-§5, subject to the §2.5 caveat about the non-isotropic case above.
5. **Revised §8 "Gaussianization is fine at PTA SNR."** Retained verbatim from current §7. The expansion argument ($\ln\mathcal L_{\rm marg} \approx \ln\mathcal L_{\rm App.B}$ at $|h|^2/\sigma^2\ll 1$, both retaining the $|d|^2|h|^2/\sigma^4$ cross term) is correct and well-presented. **Good as-is.**
6. **Revised §9 "Internal inconsistency in the prior."** Retained verbatim from current §8. Correct observation about the uniform-angle-law vs circular-Gaussian distinction. **Good as-is.**
7. **Revised §11 "Relation to our project."** The reframing to "the $p$-hierarchy is a multi-source ensemble statement" is correct and well-scoped. Subject only to a later-round update of `fisher_hierarchy.md` concept page (flagged by the proposal §4.3; not in scope here).

---

## 7. Summary of suggested revisions

A checklist an editor or the next agent can act on directly:

- [ ] **[M1, critical]** Remove the proposal's §4 sanity-check "3.6σ vs 3.8σ" discussion; the paper's 3.8σ is correct (one-sided, $p = 7.99\times 10^{-5}$). Update revised memo §5 to quote $p \sim 8\times 10^{-5}$ (not $3\times 10^{-4}$), to forestall the ambiguity.
- [ ] **[M2, critical]** In §6 of the revised memo, state explicitly that the App. B $k=2$ saturation gives $2q^2 F_{qq}(q) \to 2$, and separate this object from the $1/(2\ell+1)\leftrightarrow f_\sigma = 1/12$ kernel-effective-mode count that appears in §5.
- [ ] **[M3, medium]** Tighten §5's "detection ratio" derivation: go directly from $\hat H|_{H_0} \sim (f_\sigma H/2)\chi^2_4$ and $\hat H|_{H_1} = H$ (noise-free) to $\chi^2_4$ tail at $2/f_\sigma = 24$, without the intermediate $\langle\hat H|_{H_0}\rangle/2$ ratio.
- [ ] **[M4, medium]** In §4.4, note that the argmax-$\hat n_s$ coincidence is a theorem only in the isotropic limit; in the realistic case the argmax sky direction can differ between $T_1$ and $T_{1^\star}$ at the eigenvalue-spread level.
- [ ] **[M5, light]** In §7, use "typical sky positions on the NG15 array ($r\sim 2$)" instead of language suggesting a sky-averaged NG15 number, consistent with what P2 actually computes.
- [ ] **[C1, cosmetic]** Change the disposition of old-§4 in the proposal's §1 retain/reframe table from "Reframe" to "Remove (absorbed into new §4 and §5)".
- [ ] **[C2, cosmetic]** Move "in the App. B toy limit" into the lead sentence of the revised memo explicitly, so the out-of-context quote of the second sentence still has scope. Consider "the single scaling-level critique" instead of "the genuine detection-level critique."
- [ ] **[C3, optional]** In §5, add an italicized one-liner at the top: "*The ceiling is a property of the choice of null, not of the choice of statistic.*"
- [ ] **[C4, optional]** In §4.5, add a sentence noting the non-isotropic-prior breakdown (P1 §6) alongside the existing two-symmetry list, as a completeness note.
- [ ] **[C5, optional]** In §7, add a sentence clarifying that the 10-20% rank disagreement is real but the p-value shift is small because the null distributions shift in compensating ways (P2 §3.3).
- [ ] **[C6, editorial]** In §5, clarify that Eq. 50 is a Gaussian prior on $\vec h$ and the power-matching is a specific choice of $\sigma_h^2$; the combination is what pins the null to the matched-power GWB.
- [ ] **[F1, follow-up, out of scope]** `wiki/concepts/fisher_hierarchy.md` carries language from the old memo ("turning $\hat{\vec h}$ into $\hat q$ costs the coherent order"). This concept page should be updated in a separate pass to match the new single-source framing, but this is not blocking for the memo revision.

---

## Closing note

The proposal is a substantive improvement over the current memo and the core reframe — one detection-level critique (Eq. 50 ceiling, §5), two side observations (Fisher-on-$q$, §6; anisotropic response, §7) — is the right structure for a rigorous collaborator-facing document. The mathematical core (§4 of the revised memo, imported from P1) is rigorous and correct. The errors flagged above are mostly at the level of polish (§7 checklist) with one substantive error in the proposal's own sanity-check (the 3.6-vs-3.8σ worry, M1).

The proposal's §4 sanity check is itself valuable; two of its five items (items 2 on NG15 averaging language, 3 on $k$-value) identify real fixes; one (item 1, the 3.6σ) is its own error; one (item 4, §7 logical placement) is a legitimate editorial judgement call that the current placement resolves defensibly; one (item 5, "detection ratio" in §5) should be acted on. With M1–M5 applied, this revision is ready to merge.
