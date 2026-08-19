# Bibliography

Verified bib entries for the paper, with reverse citation index showing
where each one is used.

All metadata verified against `arxiv.org/abs/<id>` and
`ui.adsabs.harvard.edu/abs/arXiv:<id>` on 2026-04-13. Any future
changes must re-run `verify-reference` (see `CLAUDE.md`).

Source file: [`paper/references.bib`](../paper/references.bib).

## Verification discipline

When adding or modifying an entry:
1. Fetch arxiv abstract page AND ADS page.
2. Compare against any existing entry.
3. Present the diff before editing.
4. Update both `paper/references.bib` and this page.

The "Lin & Loeb" incident (2026-04-13) shows what happens when step 1
is skipped: a placeholder was left unverified for months and made it
into several drafts.

## Entries

### PTA detections (cited in `sec:intro`)

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `NANOGrav:2023gor` | Agazie et al. (NANOGrav) | ApJL 951 L8 (2023) | [2306.16213](https://arxiv.org/abs/2306.16213) | `introduction.tex:6` |
| `EPTA:2023fyk` | Antoniadis et al. (EPTA+InPTA) | A&A 678 A50 (2023) | [2306.16214](https://arxiv.org/abs/2306.16214) | `introduction.tex:6` |
| `Reardon:2023gzh` | Reardon, Zic, Shannon et al. | ApJL 951 L6 (2023) | [2306.16215](https://arxiv.org/abs/2306.16215) | `introduction.tex:6` |
| `Xu:2023wog` | Xu, Chen, Guo et al. | RAA 23 075024 (2023) | [2306.16216](https://arxiv.org/abs/2306.16216) | `introduction.tex:6` |

### Core argument references

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `NANOGrav:2023tcn` | Agazie et al. (NANOGrav) | ApJL 956 L3 (2023) | [2306.16221](https://arxiv.org/abs/2306.16221) | `introduction.tex:19`, `nanograv_prior.tex:6` |
| `Banagiri:2021lisa` | Banagiri, Criswell, Kuan, Mandic, Romano, Taylor | MNRAS 507 5451 (2021) | [2103.00826](https://arxiv.org/abs/2103.00826) | `nanograv_prior.tex:7,18` |
| `NANOGrav:2023individual` | Agazie et al. (NANOGrav) | ApJL 951 L50 (2023) | [2306.16222](https://arxiv.org/abs/2306.16222) | `distribution_c1c0.tex` (Sec. IV: R5 text, Table II, Fig. 8) — added 2026-06-22 |

### SMBH population and anisotropy modeling

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `SatoPolito:2024Kam` | Sato-Polito & Kamionkowski | PRD 109 123544 (2024) | [2305.05690](https://arxiv.org/abs/2305.05690) | `introduction.tex:17` |
| `SatoPolito:2023big` | Sato-Polito, Zaldarriaga, Quataert | arxiv only | [2312.06756](https://arxiv.org/abs/2312.06756) | `introduction.tex:10`, `astrophysical_model.tex:7,22` |
| `SatoPolito:2025dist` | Sato-Polito & Zaldarriaga | PRD 111 023043 (2025) | [2406.17010](https://arxiv.org/abs/2406.17010) | `astrophysical_model.tex:25`, `discussion.tex:25` |
| `Liepold:2024big` | Liepold & Ma | ApJL 971 L29 (2024) | [2407.14595](https://arxiv.org/abs/2407.14595) | `introduction.tex:10` |
| `LambTaylor:2024` | Lamb & Taylor | ApJL 971 L10 (2024) | [2407.06270](https://arxiv.org/abs/2407.06270) | `discussion.tex:25` |
| `LinLidzMa:2026` | **Lin, Lidz, Ma** (not Loeb!) | arxiv only | [2602.16808](https://arxiv.org/abs/2602.16808) | `introduction.tex:22`, `discussion.tex:43` |
| `LinLidzMa:2026b` | Lin, Lidz, Ma | arxiv only (v1, 10 Aug 2026) | [2608.09929](https://arxiv.org/abs/2608.09929) | `introduction.tex:21`, `astrophysical_model.tex:219`, `nanograv_prior.tex:59`, `discussion.tex:65` |

**`LinLidzMa:2026b` is in `paper_v2/references.bib` under an explicit
single-source waiver (decision D-02, 2026-08-12).** It is the sequel to
`LinLidzMa:2026`. Title, author list and submission date agree between
`references/2608.09929/main.tex` (the authors' own source) and the arxiv
abstract page. The ADS record is JS-gated and returned nothing, so the second
independent source that `verify-reference` normally requires is missing, and
the paper is days old with no journal reference to check against. The author
waived the two-source rule for this arxiv-only `@misc` rather than leave a
dangling citation. **Open follow-up: re-run the ADS check before the paper is
posted** (see `todo.md`). Analysis page: [[sources/arxiv_2608_09929]].

### Earlier anisotropy methods

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `Mingarelli:2013dsa` | Mingarelli, Sidery, Mandel, Vecchio | PRD 88 062005 (2013) | [1306.5394](https://arxiv.org/abs/1306.5394) | `introduction.tex:17` |
| `Taylor:2013esa` | Taylor & Gair | PRD 88 084001 (2013) | [1306.5395](https://arxiv.org/abs/1306.5395) | `introduction.tex:17` |

### Software and methods (added 2026-06-22, user-approved)

arXiv abstracts verified; published refs are the canonical citations. ADS
pages are JS-gated and were not re-fetched, so re-run `verify-reference`
against ADS if exact volume/page must be re-checked.

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `Gorski:2005fr` | Górski, Hivon, Banday, Wandelt, Hansen, Reinecke, Bartelmann | ApJ 622 759 (2005) | [astro-ph/0409513](https://arxiv.org/abs/astro-ph/0409513) | `astrophysical_model.tex` (Sec. III.C, HEALPix) |
| `Zonca:2019vzt` | Zonca, Singer, Lenz, Reinecke, Rosset, Hivon, Górski | JOSS 4 1298 (2019) | (JOSS, no arXiv) | `astrophysical_model.tex` (Sec. III.C, healpy) |

### Companion paper (now in `references.bib`, added 2026-06-24)

| Key | Authors | Journal | arxiv | Used in |
|---|---|---|---|---|
| `Goncharov:2026joint` | Goncharov, Sato-Polito, Bi, Zaldarriaga | arxiv only (`@misc`) | [2606.18241](https://arxiv.org/abs/2606.18241) | `source_detection.tex:387`, `nanograv_prior.tex:146`, `source_vs_cl_reduced.tex:88` |

Title: *A Joint Optimal Search for Gravitational Waves from Resolved and
Unresolved Supermassive Binary Black Holes with Pulsar Timing Arrays*.
Primary class `astro-ph.HE`. MZ co-author.

Now on arXiv as [2606.18241](https://arxiv.org/abs/2606.18241) and **added
to `paper/references.bib` as `@misc{Goncharov:2026joint}`** (2026-06-24).
arXiv metadata (title, author list, primary class) verified against the
abstract page; ADS is not yet indexing this June-2026 submission, so the
ADS cross-check could not be completed and must be re-run via
`verify-reference` once the record appears. The previous `% TODO bib`
dangling-citation note is resolved.

Published numbers from the companion (supersede draft-era values):
SNR-5 CW detection probability 2% (15 yr) / 5% (20 yr) — was 0.6% / 2%;
21 of 114 AGN candidates in tension — was 24/114. Caveat: the public
analysis uses simulated 15-yr data per an IPTA rule, with the real-data
result verified essentially identical.

## Downloaded tex sources

Tex sources have been downloaded for:
- `references/2103.00826/` — Banagiri et al. 2021
- `references/2305.05690/` — Sato-Polito & Kamionkowski 2024
- `references/2306.16221/` — NANOGrav anisotropy 2023
- `references/2312.06756/` — Sato-Polito, Zaldarriaga, Quataert 2023
- `references/2406.17010/` — Sato-Polito & Zaldarriaga 2024 (distribution)
- `references/2407.06270/` — Lamb & Taylor 2024
- `references/2407.14595/` — Liepold & Ma 2024
- `references/2602.16808/` — Lin, Lidz, Ma 2026

`references/2006.04810/` is present but **not cited** — it is Taylor,
van Haasteren, Sesana "From Bright Binaries To Bumpy Backgrounds,"
mis-attributed to Banagiri in the pre-audit bib. Left on disk as
possibly useful background; safe to delete if unused after Phase 3.

## History

- **2026-06-24**: `Goncharov:2026joint` now on arXiv (2606.18241) and
  added to `references.bib` as `@misc` (authors Goncharov/Sato-Polito/Bi/
  Zaldarriaga, primary class `astro-ph.HE`). Moved out of the "Companion
  drafts (NOT in references.bib)" section. arXiv metadata verified; ADS
  not yet indexing the submission (re-run `verify-reference` once it
  appears). Reverse-citation index curated: cited by `source_detection.tex`,
  `nanograv_prior.tex`, `source_vs_cl_reduced.tex`. Dangling `% TODO bib`
  citation resolved.
- **2026-04-13**: Initial verification pass. Found and fixed:
  - `LinLoeb:2026` → `LinLidzMa:2026` (wrong authors)
  - `Sato-Polito:2023gym` pointed at arxiv 2305.09725 (actually a viscous-fluids paper by Hegade/Ripley/Yunes); real paper is 2312.06756 (Sato-Polito/Zaldarriaga/Quataert), renamed `SatoPolito:2023big`
  - `Sato-Polito:2023spo` was a placeholder ("GWB anisotropies", no arxiv); replaced by `SatoPolito:2024Kam` (real paper by Sato-Polito & Kamionkowski)
  - `Banagiri:2021ovv` and `Banagiri:2021cyp` were two entries; the first pointed at 2006.04810 (not Banagiri). Collapsed to single `Banagiri:2021lisa` → 2103.00826
  - `Liepold:2024woa` had no arxiv; added 2407.14595 and correct title
  - `Lamb:2024gbh` had no arxiv; added 2407.06270 and correct authors (Lamb & Taylor)
  - DOIs and eprint IDs added for all entries where available
  - `SatoPolito:2025dist` dated to 2025 (PRD 111 023043), not 2024
