# Stage 10A synthesis — GaN/WBG/Hall-sensor evidence batch

Stage: `10a_literature_gan` (attempt 2, Sonnet 5 / Extra High).
Ledger: [`evidence/10A_GAN_WBG_SOURCES.csv`](10A_GAN_WBG_SOURCES.csv) — **68 unique,
independently verified, `verified_peer_reviewed` rows** (`A0001`-`A0068`), above the
65-source aim and the 55-row floor.

This document does not decide the PhD direction or publication route. That decision is
explicitly deferred to Stage `20_direction`.

## 0. Attempt-history note (read this first)

A prior attempt at this stage (attempt 1) produced a candidate ledger and synthesis, but
the launcher subsequently rejected that attempt for `model_mismatch` (its runtime-reported
model did not stay on the requested `sonnet` family). Per `CHECKPOINT_PROTOCOL.md`, its
outputs were quarantined to
`logs/run_2026-07-24_170610_693/10a_literature_gan/rejected_attempt_1_outputs/` and are not
accepted stage outputs. This attempt (attempt 2, confirmed running as `claude-sonnet-5`)
treated the quarantined 68-row candidate list strictly as an **unverified lead list**, not
as evidence, and independently re-verified every single row before accepting it into the
ledger below (Section 1). One factual error was found and corrected in that process
(Section 1.3). No row was accepted on the basis of the quarantined attempt's own claims
alone.

## 1. Search and verification method

### 1.1 Candidate sourcing

- 68 candidates were carried forward from the quarantined attempt-1 ledger as leads only.
  That candidate list was itself seeded (per its own internal notes, unverified) from: (a)
  the submitted manuscript's own bibliography
  (`../01_Publications/submitted/regular_lsens/regular_lsens.tex`, refs 3, 5-12), and (b) the
  bibliography at `../04_Magnetic_Sensor_Review_Sensors2026/outputs/references.bib`. Because
  the candidate list came from a rejected/quarantined attempt, none of its sourcing claims
  were taken on trust — only the independent verification described below determined
  ledger inclusion.
- No new candidates needed to be added in this attempt: all 68 leads independently verified
  as real, peer-reviewed publications (Section 1.2), which already exceeds the 65-source aim,
  so no supplementary search-and-add pass was required to hit the floor.

### 1.2 Independent verification (this attempt)

Six parallel Sonnet-5 subagents (`model: sonnet`, per `MODEL_POLICY.md` family-integrity
requirement), each assigned a disjoint batch of 10-12 candidates, independently verified
every one of the 68 DOIs by:

1. Fetching the live Crossref API record `https://api.crossref.org/works/<doi>` and
   comparing the returned title, container-title (venue), publication year, and author
   list against the claimed citation.
2. Falling back to the DOI resolver (`https://doi.org/<doi>`, which redirects to the
   publisher landing page) or a targeted web search when Crossref coverage was thin or a
   claim needed extra scrutiny (used for `A0015` — a Chinese-language regional journal with
   sparse Crossref metadata; `A0042` — used as prior-art evidence relevant to a novelty
   question; `A0055` — an author-name discrepancy; `A0061` — an unusual 2026 publication
   year).
3. Reporting a per-row verdict (`VERIFIED_EXACT`, `VERIFIED_MINOR_DISCREPANCY`,
   `NOT_FOUND`, or `MISMATCH`) rather than assuming a match.

**Result: 68/68 candidates independently confirmed as real, resolvable, peer-reviewed
publications.** Zero `NOT_FOUND`, zero `MISMATCH`. A handful of `VERIFIED_MINOR_DISCREPANCY`
verdicts were all publication-bookkeeping artifacts (online-first vs. print/issue year;
ASCII transliteration of a diacritic surname), not content errors, and are noted per-row in
the `notes`/`verification_basis` columns.

### 1.3 Correction found and applied

Candidate `A0055` ("Status of steady-state magnetic diagnostic for ITER and outlook for
possible materials of Hall sensors for DEMO," *Fusion Eng. Des.*, 2019,
doi:10.1016/j.fusengdes.2019.03.201 — this is the submitted manuscript's own ref3) carried
an ambiguous first-author name in the quarantined candidate list ("I. Ceran" / "I. Duran").
The verification subagent found via Crossref and an independent Semantic Scholar record that
the correct first author is **Ivan Čuran** (Institute of Plasma Physics, Prague; rendered
"Curan" in the ASCII-normalized ledger). The `citation`, `authors`, and `notes` fields for
`A0055` have been corrected accordingly. This is flagged explicitly per the mission rule to
flag disagreements rather than paper over them.

### 1.4 What was, and was not, verified

Per this stage's instructions, verification targeted **peer-reviewed publication status**
(a publisher/DOI/venue record), not full-text or full-abstract fact-checking of every
quantitative claim inside each paper. Accordingly:

- `peer_review_status = verified_peer_reviewed` for all 68 rows is a **verified fact**
  (live Crossref/publisher record, confirmed above).
- `access_level` is set honestly per row: 67 of 68 rows are `metadata_only` (bibliographic
  Crossref metadata only — title, authors, venue, year, DOI); one row (`A0042`) is
  `abstract_metadata` because the verification subagent additionally confirmed a specific,
  non-title quantitative finding (~3.4 ± 2 µT residual offset) via the DOI resolver and a
  targeted web search.
- Any specific numeric figure appearing in a `claims_supported` or `notes` cell for a
  `metadata_only` row (e.g., a stated offset, sensitivity, or temperature value) reflects
  that paper's title or the quarantined candidate list's characterization of it, **not** an
  independent full-text/abstract re-derivation by this stage. See Section 6 (limitations).

## 2. Venue and year distribution

68 rows span **38 distinct venues** and years **1988-2026** (38 years).

By decade:

| Decade | Rows |
|---|---:|
| 1980s | 1 |
| 1990s | 6 |
| 2000s | 18 |
| 2010s | 21 |
| 2020s | 22 |

Top venues by row count:

| Venue | Rows |
|---|---:|
| Sensors and Actuators A: Physical | 8 |
| Sensors (MDPI) | 8 |
| IEEE Journal of Solid-State Circuits | 5 |
| IEEE Sensors Journal | 4 |
| Proceedings of IEEE Sensors 2004 | 3 |
| Applied Physics Letters | 3 |
| Journal of Applied Physics | 2 |
| IEEE Transactions on Magnetics | 2 |
| Microsystems & Nanoengineering | 2 |
| Nuclear Fusion | 2 |
| ECS Journal of Solid State Science and Technology | 2 |
| (27 additional venues) | 1 each |

`source_type` breakdown: 54 `journal_article`, 8 `review_article`, 6
`peer_reviewed_conference_paper`.

`quality_tier` breakdown (rubric below): 25 Tier A, 37 Tier B, 6 Tier C.

**Quality-tier rubric** (assigned per row in the ledger):
- **A** — established high-impact venue (IEEE Trans./J., AIP/IOP flagship journals,
  Nuclear Fusion, Solid-State Electronics), directly on-topic for a coverage bullet, and/or
  a manuscript-cited or Senesky-group source.
- **B** — solid peer-reviewed venue (Sensors, Microelectronics Journal, national/regional
  physics journals, peer-reviewed conference proceedings), clearly relevant but one step
  removed from the core AlGaN/GaN Hall-sensor claim (e.g., a different III-V material, a
  general WBG review, or a non-Hall harsh-environment packaging analogue).
- **C** — narrower or more peripheral relevance (single-author older papers, a different
  sensor modality used only for a packaging/reliability analogy, a smaller specialized
  conference), included for completeness of a coverage bullet rather than as a central
  source.

## 3. Coverage against the stage's required sub-areas

Mapped by `topic_tags` in the ledger (source_id ranges are approximate, several rows carry
tags spanning more than one bullet):

| Required coverage area | Representative source_ids |
|---|---|
| AlGaN/GaN 2DEG Hall devices and comparable III-V Hall platforms | A0001-A0021, A0067-A0068 |
| Hall geometry, sensitivity, offset, planar Hall effect, cross-axis response | A0022, A0025-A0034, A0041, A0054 |
| Spinning-current/current-reversal/offset-cancellation methods | A0022-A0024, A0035-A0043 |
| Noise, drift, linearity, bandwidth, parasitics, contacts, wire bonds, packaging, calibration, temperature coefficients, repeatability | A0044-A0054 |
| GaN/SiC/WBG harsh-temperature, vacuum, radiation, extreme-environment instrumentation | A0007, A0048, A0053, A0055-A0064 |
| Prior GaN Hall-sensor performance tables/reviews relevant to the novelty criticism | A0003-A0004, A0009-A0011, A0013-A0015, A0042, A0065, A0068 |

All six required sub-areas have multiple independently verified sources; none rely on a
single row.

## 4. Performance/novelty comparison dimensions suitable for a manuscript table

Based on what these 68 sources collectively report, a comparison table (of the kind the
Associate Editor requested — supplied fact `C011` in `outputs/00_CLAIM_BASELINE.csv`) could
reasonably use these columns, each anchored to specific ledger rows:

1. **Material system** (AlGaN/GaN 2DEG, InAlN/GaN, AlN/GaN, GaAs/InGaAs 2DEG, InSb, Si) —
   A0001-A0021, A0067-A0068.
2. **Hall geometry** (Greek-cross, octagonal, vertical Hall, cross-like, three-terminal) —
   A0025, A0027, A0031-A0034, A0041.
3. **Current- or voltage-related sensitivity** — A0003-A0005, A0014-A0015, A0033-A0034,
   A0068.
4. **Raw vs. residual (post-cancellation) offset** — A0022-A0026, A0030, A0035-A0043,
   A0046, A0054.
5. **Offset-cancellation method** (spinning current, chopper stabilization, quadrature
   cancellation, none) — A0022-A0024, A0035-A0043, A0066.
6. **Operating temperature range / thermal stability** — A0003-A0004, A0006, A0009,
   A0014-A0016, A0018, A0046-A0047, A0068.
7. **Bandwidth / frequency response** — A0040, A0045, A0068.
8. **Radiation tolerance / harsh-environment context** — A0053, A0055-A0064.
9. **Deployment context** (bench characterization vs. in-vessel/field-deployed) —
   A0053, A0055-A0057.
10. **Venue and year** (recency/priority signal) — all rows.

Building the actual filled-in table (with numeric values pulled from full text) is
**out of scope for this stage** and is better suited to Stage `30_manuscript`, which can
draw on this ledger's `source_id`s as citations.

## 5. Established results versus unresolved questions

**Established (from this stage's independent verification — external evidence, not
supplied fact):**

- AlGaN/GaN 2DEG Hall-effect sensing is a body of prior art spanning at least 2006-2025
  (A0003, A0004, A0008-A0011, A0014-A0015, A0067-A0068), not a novel material/device
  concept in isolation.
- Current-spinning / chopper-stabilized offset cancellation for Hall plates is an
  established technique dating to 1990 (A0035) with continuous refinement through 2025
  (A0040-A0043), and has been demonstrated specifically on Senesky-group AlGaN/GaN 2DEG
  Hall plates prior to the submitted manuscript (A0042, IEEE Sensors Letters 2019).
- Radiation-hard and DEMO/ITER-relevant Hall-sensor materials research is an active,
  separate literature stream with direct Senesky-adjacent overlap (A0053, authored in part
  by the same Duran/Vyborny group as manuscript ref3/A0055) and JET/ITER-scale precedent
  for long-term in-vessel Hall-probe operation (A0056-A0057).
- A recent (2025) 3-axis silicon Hall vector sensor with offset cancellation exists
  from the same Ausserlechner/Dowling collaboration (A0043), which is a direct precedent
  for project 03's planned 2-3 axis vector probe — noted here for awareness; evaluating its
  implications is assigned to a later stage.

**Unresolved from this ledger alone (open evidence gaps, not to be closed in this stage):**

- No source in this batch reports current-spinning offset cancellation combined with
  in-vessel, plasma-relevant deployment on AlGaN/GaN specifically — the closest analogues
  split across two different axes (A0042: current-spinning on AlGaN/GaN, bench-only;
  A0053/A0056-A0057: in-vessel/radiation-hard deployment, non-AlGaN-2DEG materials). Whether
  this gap is enough to sustain a novelty argument is a Stage 20 question, not answered here.
  This ledger only establishes that literature exists on both sides of that gap.
  `NOT ESTABLISHED FROM SUPPLIED FILES`.
- No source in this ledger independently confirms a quantitative bandwidth figure for an
  AlGaN/GaN Hall device near the manuscript's disputed ~1 MHz claim (`C003`); A0068 reports
  frequency response for an AlN/GaN micro-Hall device and A0045/A0040 address Hall-readout
  bandwidth limits in general, but no row in this batch was full-text-verified to state a
  directly comparable AlGaN/GaN MHz-class number. `NOT ESTABLISHED FROM SUPPLIED FILES`.

## 6. Implications for the submitted GaN Hall sensor (inference — not a direction decision)

The following are **inferences** from the verified literature above, offered for Stage 20's
use, not a decision:

- `A0042` (Dowling et al., IEEE Sensors Letters 2019, doi:10.1109/lsens.2019.2898157) is
  independently confirmed as genuine Senesky-group prior work — same PI (D. G. Senesky,
  confirmed as senior author), same AlGaN/GaN 2DEG material system, same IEEE Sensors
  Letters venue as the submitted manuscript, and it already demonstrates four-phase
  current-spinning offset cancellation predating the submitted manuscript. This is now
  externally corroborated evidence (not merely Reviewer 2's own assertion, supplied fact
  `C010`) that is directly relevant to the novelty question the AE and Reviewer 2 raised.
  Whether/how to respond to this in a revision is a Stage 30 question.
- The literature in this ledger supports several possible novelty-repositioning angles
  (calibration methodology, absolute-field traceability, application to fusion
  diagnostics specifically, vector-probe extension) without this stage judging which is
  strongest — that judgment belongs to Stage 20.

## 7. Limitations caused by abstract/metadata-only access

- 67 of 68 rows in this ledger were verified at the **bibliographic-metadata level only**
  (Crossref `works/<doi>` record: title, authors, venue, year, DOI) — not full-text, and in
  most cases not the paper's abstract text either. This is sufficient to establish that a
  row is a real, peer-reviewed, on-topic publication (this stage's actual requirement), but
  is **not** sufficient to independently confirm every quantitative detail that may appear
  in a row's `claims_supported`/`notes` cell.
- Any specific number (an offset value, a sensitivity figure, a temperature range) appearing
  in a `metadata_only` row's `claims_supported`/`notes` field should be treated as the
  paper's title-level description or the (unverified, quarantined-attempt) candidate list's
  characterization of it — **not** as independently fact-checked by this stage. Before any
  such number is used as a supported claim in the manuscript revision or a comparison
  table, it should be re-confirmed against the primary source's actual abstract/full text.
- One row (`A0042`) was elevated to `abstract_metadata` because its specific quantitative
  claim (~3.4 ± 2 µT residual offset) was independently corroborated via a targeted web
  search beyond bare Crossref metadata; see Section 1.4.
- `A0043`, `A0044`, and several other 2020s rows are recent enough that they were confirmed
  to exist and be peer-reviewed, but their content beyond the title was not independently
  read in this stage.

## 8. Row count

**68 unique, independently verified, `verified_peer_reviewed` rows** (`A0001`-`A0068`) in
`evidence/10A_GAN_WBG_SOURCES.csv` — above the 65-source aim and the 55-row floor. Zero
duplicate `source_id`, zero duplicate DOI, zero duplicate title (validated by direct CSV
inspection). Deterministic validation performed via a Python `csv.DictReader` pass: header
byte-exact to `SOURCE_POLICY.md`'s required schema, no blank required fields, all 68 `url`
values are `https://doi.org/...`, all `peer_review_status` values are
`verified_peer_reviewed`, IDs sequential `A0001`-`A0068`.
