# Stage 10D — Final evidence-base coverage report

Final ledger: `outputs\01_SOURCE_LEDGER.csv` (219 rows). Companion files:
`outputs\01_NEW_SOURCE_AUDIT.csv` (219 rows, 1:1 with the ledger) and
`outputs\01_EVIDENCE_MAP.csv` (37 typed claims). All counts below were
computed by `tools\validate_10d_outputs.py` from the written files, not from
lane self-reports (validator output: 21/21 checks PASS).

## 1. Counts

### Peer-review status (all 219 rows)

| Status | Rows |
|---|---|
| `verified_peer_reviewed` | **215** (gate ≥120 — PASS) |
| `peer_review_uncertain` | 4 — H006 (Sensor Letters 2007, venue-quality concern + unobtainable full text), R015 (AIP Conf. Proc.), R016 (J. Phys. Conf. Ser.), R033 (ECS Transactions) |
| `not_peer_reviewed` | 0 |

P063 was `peer_review_uncertain` in lane 10C solely for an unresolved author
list; stage 10D retrieved the complete 15-author list from the live Crossref
record and upgraded it to `verified_peer_reviewed` (documented in the row).

### New vs. reused relative to folder `06` (231-row baseline)

| Category | Rows |
|---|---|
| New (no normalized-DOI or normalized-title match in `06`) | 202 total; **198 verified** (gate ≥75 — PASS) + 4 uncertain |
| Reused (exact folder-06 overlap, individually flagged) | 17 (all verified): H001→S0118, H002→S0122, H003→S0068, H004→S0179, H005→S0180, H008→S0173, H009→S0105, H010→S0069, H011→S0111, H034→S0033, H035→S0041, H042→S0051, H048→S0074, H049→S0076, H065→S0067, R066→S0082, R069→S0151 |

### Topic quotas (verified rows only; quota tags embedded in `topic_tags`)

| Quota | Required | Achieved |
|---|---|---|
| hybrid/coil/integrator/sensor-fusion (`quota_hybrid_coil`) | 25 | **70** |
| radiation/irradiation (`quota_radiation`) | 30 | **79** |
| applications/alternatives (`quota_applications_alternatives`) | 25 | **76** |
| calibration/observability/uncertainty (`quota_calibration_observability`) | 20 | **50** |

Quota assignment was deterministic from lane topic tags (mapping documented in
the 10D build): no row was relabeled to reach a quota, and every quota is met
with ≥2× margin, so no padding pressure existed.

### Quality tier (verified rows)

| Tier | Rows |
|---|---|
| A | 77 |
| B | 111 |
| C | 27 |

Stage-10D tier re-evaluation changed one row: R011 A→B (device is a digital
Hall *switch* IC, one step removed from metrological linear Hall sensing —
relevance-based, documented in the row). H059's planned downgrade was
*reversed* after its abstract was retrieved and read at 10D, confirming its
previously snippet-only central claim (see §3).

### Access level (verified rows) — honesty statement

| Access | Rows |
|---|---|
| `full_text` | 14 |
| `abstract_metadata` | 102 |
| `metadata_only` | 99 |

99 verified rows rest on Crossref-verified bibliographic identity plus
secondary content description (publisher pages consistently returned HTTP
402/403 to automated fetch across all three lanes). Every such row carries the
limitation in its own `verification_basis`/`notes`. Numeric claims from
`metadata_only` rows are not load-bearing anywhere in the three reviews
without an explicit flag.

### Source type and year (verified rows)

| Type | Rows |
|---|---|
| journal_article | 190 |
| conference_paper | 16 |
| review_article | 9 (used for mapping only, per `SOURCE_POLICY.md`) |

| Decade | 1960s | 1970s | 1980s | 1990s | 2000s | 2010s | 2020s |
|---|---|---|---|---|---|---|---|
| Rows | 1 | 3 | 3 | 17 | 45 | 74 | 72 |

### Evidence role (verified rows; tags overlap)

| Role | Rows |
|---|---|
| Direct Hall+coil hybrid (`direct_hybrid`) | 14 (15 tagged incl. uncertain H006) |
| Direct Hall-device radiation (`direct_hall_*`) | 20 |
| Enabling physics/theory (`enabling_*`) | 46 |
| Context only | 12 |
| Lane origin | 10A: 65, 10B: 74, 10C: 76 |

## 2. Deduplication method

- Normalization: DOI lowercased, `https://doi.org/`-style prefixes stripped;
  title lowercased, punctuation removed, whitespace collapsed (per
  `SOURCE_POLICY.md`).
- Cross-lane: 2 DOI collisions found and merged — **R005→H007**
  (10.1109/TNS.2012.2188816) and **R077→H031**
  (10.1016/j.fusengdes.2021.112228). The keeper rows carry the merged topic
  tags and a `MERGED at stage 10D` note preserving the radiation lane's
  framing. IDs R005/R077 do not exist in the final ledger; citations use
  H007/H031.
- 0 normalized-title collisions across different DOIs.
- Versus folder `06`: every final row checked against all 231 baseline rows by
  both normalized DOI and normalized title; 17 overlaps (all by DOI, none
  title-only), each retained but flagged `reused` in the audit CSV. Reused
  rows count toward the 120-verified gate (they are part of this mission's
  evidence base) but not toward the 75-new gate.

## 3. Stage-10D independent verification (what Fable actually re-checked)

1. **All 219 final DOIs** re-queried against the live Crossref API
   (2026-07-27), comparing registered title (normalized word-overlap) and
   year: 214 exact-clean; 5 old IEEE proceedings records (H035, H036, H053,
   H055, R043) carry no year field in Crossref but match title and authors
   exactly (noted per-row). Full results retained in
   `tools\crossref_verification_10d.json`; re-runnable via
   `tools\verify_crossref_10d.py`. This covers every tier-A source, every
   direct Hall+coil paper, and every central radiation paper — not a sample.
2. **All six PMC IDs** underlying `full_text` access claims (H004, H005,
   H021, R003, R044, R063) re-confirmed via the NCBI eutils API; titles match.
3. **Targeted content re-checks** via the Semantic Scholar API for five rows
   whose *content* (not identity) was flagged unverified: H059's abstract was
   retrieved and read, **confirming** the cryogenic-Hall-cross-calibrated-
   in-situ-by-induction-coils claim; H010, H002, H063, P003 returned no
   abstract and keep their conservative labels.
4. **Corrections made at 10D** (each documented in the affected row):
   - P063: status upgraded to `verified_peer_reviewed` (15-author list
     resolved from Crossref).
   - P008: first author corrected from "Y. Chen" to **D. L. Chen** (Crossref
     record; title/venue/year exact match — author-metadata error, not a
     wrong paper).
   - P011: named author list resolved (Y. Zhang et al., 6 named authors).
   - H059: claim-confirmation note added; tier A retained.
   - R011: tier A→B (relevance re-evaluation).
5. **Metadata conflicts inherited from lanes** re-confirmed as resolved: the
   `LITERATURE_SEEDS.md` title error for 10.3390/s19245455 (H005 is
   "...Feed-Forward Correction", not "...Extended Kalman Filtering") and the
   PMC7412317 seed mismatch (R044 is the TCAD simulation paper, not an
   experimental SOI irradiation study) — both verified against the actual
   records at 10D.

## 4. Unresolved gaps (carried forward, not resolved by this stage)

1. No bare GaN/AlGaN Hall-plate neutron irradiation study exists (any
   spectrum) — the largest direct-evidence gap for the user's device family
   (claim C14).
2. No in-situ, during-irradiation Hall-sensitivity recalibration against a
   material-diverse reference is reported for any material (C21).
3. No joint gain+bias+state identifiability proof exists for a Hall+coil (or
   any heterogeneous absolute+rate) sensor pair (C03).
4. 14 MeV D-T direct Hall-device data is absent; the only in-machine D-T
   radiation dataset is the (coil-adjacent, optical) JET FOCS (C20).
5. Access ceiling: 99/215 verified rows are `metadata_only`; per-row-flagged
   numbers (e.g., H038's mT/A figures, H002's validation basis, P006's
   200 °C/9 MGy, P054's ppm/mrad figures, R056–R060 RIEMF dose curves) need
   institutional full-text access before quantitative downstream use.
6. Integrator/timing-reference radiation sensitivity is single-source and
   space-contextualized (R067); connector/feedthrough qualification is
   programmatic only (R054).
7. The metallic-Hall neutron null result (R071) is single-source at one
   fluence/temperature envelope.
8. H010's claimed EAST Hall+coil content remains unverifiable (no abstract
   retrievable); it stays `context_only`.
9. No neutron displacement-damage data exists for TMR/AMR alternatives
   (P062/P063 are gamma/X-ray only).
10. H006 (2007 self-diagnostic concept) remains full-text-unobtainable; no
    novelty claim may rest on it alone (H007 is the defensible citation).
