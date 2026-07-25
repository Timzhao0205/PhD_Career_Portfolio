# 01 — Source coverage report (Stage 10D)

Companion to [`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv),
[`01_LITERATURE_REVIEW.md`](01_LITERATURE_REVIEW.md), and
[`01_EVIDENCE_MAP.csv`](01_EVIDENCE_MAP.csv).

## 1. Deterministic count statement

The merged ledger contains **exactly 231 rows**, `S0001`–`S0231`, every one
with `peer_review_status = verified_peer_reviewed`. Arithmetic:
70 (Stage 10A, `A0001`–`A0070`) + 89 (Stage 10B, `B0001`–`B0089`) + 74
(Stage 10C, `C0001`–`C0074`) = 233 candidate rows; minus 2 same-DOI
cross-lane duplicates (`B0041` ≡ `A0068`; `B0054` ≡ `A0070`) = **231 unique
sources**. 231 ≥ 150, so the `SOURCE_POLICY.md` minimum is met with a
margin of 81 sources (154% of the requirement). No patents, preprints,
standards, theses, webpages, or supplied files appear in the ledger or the
count; the only `source_type` values present are `journal_article` (208),
`review_article` (18), and `conference_paper` (5, all verified
peer-reviewed proceedings: J. Phys. Conf. Ser. 2012, IEEE Sensors 2004,
ASICON 2007, IEEE iSES 2022, American Control Conference 2014).

Verified programmatically at this stage
(`state/tools/10d_validate.py`, run after the final write): 231 rows; exact
required 16-column header; 0 empty required fields; 0 duplicate
`source_id`; IDs strictly sequential `S0001`–`S0231`; 0 blank DOIs; 0
duplicate normalized DOIs; 0 duplicate normalized titles; 0 malformed DOIs;
all `url` fields are `https://doi.org/...` resolver links; all
`quality_tier`/`access_level`/`source_type` values within allowed enums;
all years in 1900–2026. Result: **VALIDATION: PASS**.

## 2. Deduplication method

1. **Normalization.** DOI: lowercased, `https://doi.org/` prefix stripped.
   Title: lowercased, all non-alphanumerics removed.
2. **Primary key: normalized DOI.** Across all 233 rows, exactly two
   normalized DOIs occurred twice: `10.1088/1741-4326/ac8aad`
   (`A0068`/`B0041`, the JET long-term Hall-probe paper) and
   `10.1007/s10582-006-0185-4` (`A0070`/`B0054`, the CASTOR safety-factor
   paper). The 10A copies were kept (A0068 had the better access level,
   `full_text`); topic tags were unioned and lane provenance recorded in
   `notes`. Notably, `A0068`/`B0041` was an overlap Stage 10B itself did
   not flag — it was caught by this stage's programmatic dedup and had
   also been recorded in Stage 10C's exclusion table.
3. **Secondary key: normalized title.** The title pass found the same two
   pairs and no additional near-duplicates under different DOIs.
4. **Pre-merge dedup honored.** Stage 10C had already excluded 25
   candidate rows as exact-DOI duplicates of 10A/10B rows (list in
   `evidence/10C_SYNTHESIS.md` §6). This stage confirmed zero residual
   overlap between the 10C ledger and the other two lanes.
5. **ID assignment.** Stable and deterministic, in lane order with
   duplicates skipped: `A0001`–`A0070` → `S0001`–`S0070`;
   `B0001`–`B0040` → `S0071`–`S0110`; `B0042`–`B0053` → `S0111`–`S0122`;
   `B0055`–`B0089` → `S0123`–`S0157`; `C0001`–`C0074` → `S0158`–`S0231`.
   Every row's `notes` field carries a `[Provenance: <lane id>]` token;
   the full old→new map is at `state/tools/10d_id_map.csv`.

## 3. Verification method and metadata-disagreement resolution

**Lane-level verification (Stages 10A–10C).** Every row was verified at
its origin stage via the Crossref API (`api.crossref.org/works/<doi>`), a
PubMed/PMC record, or a direct publisher DOI-landing-page fetch — never a
search snippet alone. Each row's `verification_basis` records its own
evidence. The lane stages additionally spot-re-verified 8 (10A) and 10
(10B) DOIs in their main sessions.

**Merge-level re-verification (this stage).** This session independently
re-verified **32 DOIs (~14% of the ledger)** against the Crossref API,
stratified across lanes and weighted toward 10C rows, 2025–2026-dated
rows, unusual venues, and the most load-bearing precedents. Result:
**32/32 exact matches** on title/venue/year/authors. Rows re-verified here
carry the suffix "independently re-verified at stage 10D..." in
`verification_basis`.

**Metadata disagreements found and resolved (all against Crossref
records fetched at this stage):**

| Row | Issue | Resolution |
|---|---|---|
| S0070 (was A0070/B0054) | Crossref renders authors inconsistently ("Ďuran/Curan", "Bolshakova/Boshakova") | Standard ASCII transliterations kept (Kovarik; Duran; Bolshakova; Holyaka; Erashok); artifact documented in `notes` |
| S0121 (was B0052) | Lane recorded lead author "Ivan Ceran" | Corrected to Ivan Duran (Crossref: Ivan Ďuran) |
| S0122 (was B0053) | Lane recorded "Ivan Curan"; citation lacked volume | Corrected to Ivan Duran; citation enriched to Fusion Eng. Des. 217, 115180 (2025) |
| S0219 (was C0062) | Lane recorded first author "Coesson" | Corrected to Coisson (Crossref: Marco Coïsson) |
| S0112 (was B0043) | Citation lacked volume/issue | Enriched to Plasma Phys. Control. Fusion 68(6) (2026) |
| S0095 (was B0025) | Citation lacked volume/issue | Enriched to Nucl. Fusion 65(3) (2025) |
| S0205 (was C0048) | Citation lacked issue | Enriched to Nucl. Fusion 66(2) (2026) |
| Venue strings | Same journal rendered two ways across lanes | "Sensors (MDPI)" → "Sensors"; "Materials (Basel)" → "Materials" |

No row failed identity or peer-review verification; **no removals were
required** (task 3 of the stage prompt yielded an empty removal set — the
lane ledgers were already restricted to verified rows, and this stage's
sampling found no counter-evidence).

## 4. Quality-tier rubric (as operationalized across all three lanes)

- **A (137 rows, 59%):** established, field-central peer-reviewed venue
  AND at least one of: foundational/seminal status (e.g. Munter 1990
  S0033, Mirnov 1971 S0071, Kalman 1960 S0171, Lao 1985 S0135), definitive
  design/qualification role (ITER OVSS papers S0113–S0115, S0148–S0149),
  direct topical centrality to the mission (HSX S0132, CTH S0143, JET
  S0068), or authoritative review status (Strait S0108, Pearton S0054).
- **B (86 rows, 37%):** sound peer-reviewed venue and genuine relevance,
  but secondary support role, weaker topical proximity, or quantitative
  content confirmable only at abstract/snippet level.
- **C (8 rows, 4%):** lower-tier conference papers, very short
  status-note formats, or topically peripheral rows kept for a specific
  narrow support purpose, each flagged in its own `notes` (e.g. S0009,
  S0043, S0127, S0204).

## 5. Distributions

**By lane of origin:** 10A (GaN/WBG) 70; 10B (fusion diagnostics) 87;
10C (methods/metrology) 74.

**By year** (range 1960–2026; the 1960 row is Kalman's foundational
filtering paper):

| Period | Rows |
|---|---:|
| pre-1990 | 7 |
| 1990–1999 | 22 |
| 2000–2009 | 41 |
| 2010–2014 | 34 |
| 2015–2019 | 44 |
| 2020–2023 | 48 |
| 2024–2026 | 35 |

36% of the ledger is from 2020–2026, so the state of the art is current;
the pre-2000 tail is deliberately retained foundational theory.

**By venue** (81 distinct venues; top 12):

| Venue | Rows |
|---|---:|
| Review of Scientific Instruments | 29 |
| Nuclear Fusion | 28 |
| Fusion Engineering and Design | 26 |
| Sensors | 22 |
| Plasma Physics and Controlled Fusion | 10 |
| IEEE Sensors Journal | 9 |
| Sensors and Actuators A: Physical | 9 |
| IEEE Transactions on Magnetics | 5 |
| Applied Physics Letters | 4 |
| Physics of Plasmas | 4 |
| Fusion Science and Technology | 3 |
| 70 further venues | ≤2 each |

**By topic category** (rows matching each `SOURCE_POLICY.md` coverage
requirement via `topic_tags`+`claims_supported` keyword audit; rows count
in multiple categories by design):

| SOURCE_POLICY category | Rows |
|---|---:|
| AlGaN/GaN and other WBG Hall/device physics | 77 |
| Hall-sensor geometry/sensitivity/offset/noise/bandwidth/temperature/radiation/packaging/calibration | 117 |
| Magnetic-confinement fusion and plasma magnetic diagnostics | 133 |
| Stellarator/HSX-relevant field measurement and validation | 73 |
| Direct sensors vs inductive/B-dot/Mirnov diagnostics and drift | 109 |
| Uncertainty, repeatability, calibration traceability, instrumentation | 59 |
| Low-fabrication novelty (modeling/inverse/data-fusion/signal-processing/software/ML/digital-twin) | 65 |

Every category clears a material threshold (minimum 59 rows); coverage is
adequate and no supplementary search was required (stage task 5 not
triggered: 231 ≥ 150 and no category gap).

**By access level:** `abstract_metadata` 133 (58%), `metadata_only` 75
(32%), `full_text` 23 (10%).

## 6. What was searched but excluded (for audit)

- 2 cross-lane duplicate occurrences merged at this stage (§2).
- 25 cross-stage duplicate DOIs pre-excluded by Stage 10C (its §6 table);
  confirmed still-zero residual overlap here.
- 13 (10B) + 9 (10C) within-stage duplicate occurrences removed at their
  origin stages.
- 2 off-topic verified peer-reviewed candidates deliberately excluded
  rather than counted (10A: a GMR biosensor paper; 10B: a CERN
  accelerator paper — the latter later included by 10C as `S0180` under
  its explicitly non-fusion-restricted signal-processing bullet, with the
  distinction documented in the row).
- Project 04's 122-row reference registry was treated as a seed only;
  nothing was counted from it without independent re-verification (per
  Stage 00 gate C021).

## 7. Limitations

1. **Access depth.** Only 23/231 rows (10%) were read at full-text level;
   58% at abstract level; 32% are bibliographic-identity-only
   (`metadata_only`). IEEE Xplore, AIP, ScienceDirect, Wiley, and
   Springer blocked most automated full-text fetches (HTTP 402/403) in
   all sessions — a structural limitation, honestly tracked per-row in
   `access_level`. Consequence: any specific number quoted from a
   non-`full_text` row should be re-confirmed against the primary PDF
   before appearing in a manuscript table.
2. **Absence findings are search-bounded.** The ledger's central novelty
   anchor (no GaN/AlGaN Hall sensor found deployed in any
   tokamak/stellarator) is an absence-of-evidence result from three
   independent bounded searches, not proof of global priority.
3. **Peer-review verification is venue-level for older rows.** For
   pre-1990 sources (7 rows, e.g. Soviet Atomic Energy 1971, ASME 1960),
   peer review is established from the venue's scholarly-journal status
   and publisher record, as `SOURCE_POLICY.md` permits; era review
   practices differed from modern norms.
4. **Crossref is the identity backbone.** Bibliographic identity rests on
   Crossref registration records (authoritative registration data, not
   secondary summaries) plus publisher/PubMed pages where fetchable; the
   observed Crossref-side metadata artifacts (diacritic renderings, §3)
   were resolved rather than propagated.
5. **Citations in the review.** 158 of 231 sources are cited inline in
   `01_LITERATURE_REVIEW.md`; every `[S####]` link was programmatically
   checked against the ledger DOI (`state/tools/10d_check_citations.py`,
   PASS). The remaining 73 rows are supporting-depth rows available to
   later stages via the ledger.
