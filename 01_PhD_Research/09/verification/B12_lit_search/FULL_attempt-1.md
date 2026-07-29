# Independent verification report — B12_lit_search FULL attempt-1

- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Observed runtime identity:
  the session self-identifies as Fable 5 (model id `claude-fable-5`); no
  independent effort string was exposed, so effort is recorded as requested,
  not observed.
- Date of verification and of all live web checks: 2026-07-28
- Candidate verified (read-only): `outputs/B12_lit_search/attempt-1/`
  (`SEARCH_PROTOCOL.md`, `SEARCH_LOG.csv`, `PAPER_LEDGER.csv`,
  `EXCLUSIONS.csv`, `FLOW.json`, `RUN_META.md`, `SELF_CHECK.md`)
- Inputs read: `state/CURRENT_VERIFY.md`, `workflow/stages/B12_lit_search.md`,
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`, `LIT_POLICY.md`,
  `SOURCE_POLICY.md`, `MODEL_POLICY.md`, `pilot/B12_lit_search/attempt-1/
  PAPER_LEDGER.csv`, `pilot/B12_lit_search/attempt-1/EXCLUSIONS.csv`,
  `.claude/agents/pap06-sonnet-high.md`
- All counts below are my own recounts from the CSVs (grep + full read), not
  the candidate's figures. All live-source checks below are pages I opened
  myself via WebFetch during this verification.

## 1. Files, structure, schemas

- All 7 required files present and non-empty. FLOW.json parses as valid JSON
  (verified by full read; balanced structure, quoted keys).
- `PAPER_LEDGER.csv` header has the exact 17 spec columns in spec order:
  paper_id,doi,title,authors,year,venue,publisher,publication_type,
  peer_review_status,publisher_url,topic_stream,relevance,evidence_status,
  access_status,correction_status,retraction_status,notes. PASS.
- `SEARCH_LOG.csv` header row exactly matches the spec 8 columns. A single
  leading `#` comment line documents the timestamp convention; this mirrors
  the accepted pilot's leading-comment convention and does not alter the
  schema. Timestamps use `2026-07-28T NOT_EXPOSED` — honest, disclosed.
- `EXCLUSIONS.csv` header exactly matches the spec 6 columns
  (exclusion_id,title,doi_or_url,stage,reason,topic_stream). PASS.
- No `PILOT` / `NOT FINAL` label anywhere in the candidate files (grep: only
  SELF_CHECK's sentence asserting their absence matches). PASS.

## 2. Exact counts (my recounts)

- Ledger data rows: 62 (grep `^P\d{4},` = 62), IDs P0001–P0062 sequential,
  gap-free, no repeats (verified by full read). 62 is within 60–100. PASS.
- `evidence_status`: `,accepted_core,` = 62 = all rows; zero
  `accepted_supplement`, zero `unresolved`, zero `excluded` in the ledger.
  62 >= 48. PASS.
- Per-stream accepted_core (my row-by-row tally): hall_metrology 13 (P0004,
  P0008, P0009–P0019); hybrid_diagnostics 14 (P0001, P0003, P0020–P0031);
  hts_quench_current 17 (P0002, P0007, P0032–P0046); power_conversion 18
  (P0005, P0006, P0047–P0062). Sum 13+14+17+18 = 62. All >= 8. Matches
  FLOW.json topic_counts exactly. PASS.
- 2020–2026 accepted_core, my recount from the year column: hall 7, hybrid
  10, hts 11, power 15 = **43** total. Gate (>=16 overall, >=2 per stream)
  passes with large margin. NOTE: the candidate claims 42 (hts 10) in
  FLOW.json notes and SELF_CHECK §5 — it omitted P0043 (2022, Applied
  Physics Letters) from the hts recency tally (SELF_CHECK's hts recent+older
  lists sum to 16, not 17). The true count is one HIGHER than claimed; the
  gate is unaffected. Recorded as defect 1 (minor).
- Seminal older work per stream (my recount of oldest years): hall 1996
  (P0009), hybrid 2001 (P0020), hts 2013 (P0041, P0045), power 2019 (P0056,
  P0057, P0062) — matches the claimed 1996/2001/2013/2019. PASS.

## 3. Vocabulary / normalization sweeps

- publication_type: only `journal_article` and `review_article` occur
  (grep `conference_paper` = 0 matches in the ledger). PASS.
- peer_review_status: `,verified,` = 62 = every row. PASS.
- evidence_status: only `accepted_core` (see above). PASS.
- DOIs: all 62 extracted and inspected; all begin `10.` with no `doi:`/URL
  prefix; regex sweep for uppercase inside the DOI field = 0 matches
  (P0010's `10.1088/1361-648x/abf7e2` correctly lowercased). All 62
  normalized DOIs are distinct (manual comparison of the full extracted
  list). No duplicate title/year pair found. PASS.
- publisher_url: every cell is a single clean URL (iopscience.iop.org,
  pmc.ncbi.nlm.nih.gov, or jsss.copernicus.org); no parenthetical second
  URL remains anywhere in that column (the pilot's two-URL cells on
  P0005/P0006 were cleaned; the DOI-resolution detail now lives in notes).
  PASS.

## 4. FLOW.json vs my CSV recounts

Using the candidate's stated counting convention: accepted_core 62 = my 62;
accepted_supplement 0 = my 0; unresolved 0 = my 0; excluded 20 = my 20
EXCLUSIONS rows (E01–E20); screened 82 = 62+20; identified 88 = 82 + 6
documented duplicate re-surfacings (Q05/Q06, Q35/Q37, Q40-vs-Q62-adjacent
instances, Q41/Q46, Q44, Q45 noted in SEARCH_LOG); full_text_checked 79 =
82 − 3 title/abstract-stage exclusions (E03, E04, E05) = 62 + 17 full-text-
stage exclusions. Per-stream excluded tallies: hall 7 (E01,E02,E11–E15),
hybrid 6 (E03–E07,E10), hts 2 (E09,E20), power 5 (E08,E16–E19) — all match
FLOW.json. All JSON count fields equal my recounts. PASS. (The only numeric
misstatement found anywhere is the "42" recency figure in the free-text
notes — defect 1.)

## 5. P0001–P0008 stability vs accepted pilot

Field-by-field comparison against `pilot/B12_lit_search/attempt-1/
PAPER_LEDGER.csv`: for all eight rows, paper_id, doi, title, authors, year,
venue, publisher, publication_type, peer_review_status, topic_stream,
evidence_status, correction_status, and retraction_status are identical.
publisher_url changed only on P0005/P0006 (pilot two-URL doi.org cell →
single PMC-mirror URL actually opened), the permitted cleanup. HOWEVER, the
free-text `relevance`/`notes`/`access_status` cells were also lightly
trimmed or reworded on P0001, P0003, P0004, P0005, P0006, P0007, P0008
(e.g. dropping "B10's", "(context only)", "applied here at pilot scale",
"— noted as a limitation, not concealed"). Substantively these edits are
meaning-preserving and partly necessary (the pilot phrase "applied here at
pilot scale" could not be carried into a full-run artifact), so I judge the
stability gate satisfied in substance; but SELF_CHECK §8 ("The only field
edited on carried-over rows is publisher_url for P0005 and P0006") and
FLOW.json's reconciliation line ("all other fields ... unchanged") are
inaccurate self-descriptions. Recorded as defect 2 (minor).

## 6. Correction/retraction completeness, P0012, zero-supplement claim

- All 62 rows have non-empty correction_status and retraction_status naming
  the record checked. PASS.
- P0012: I opened https://pmc.ncbi.nlm.nih.gov/articles/PMC7441171/ myself.
  The live record shows exactly "This article has been corrected. See Nat
  Commun. 2021 Jan 18;12:554" — the ledger's disclosure is verbatim-accurate,
  correctly distinguished from a retraction, and retention as accepted_core
  is consistent with LIT_POLICY. PASS.
- Zero-supplement claim: no conference_paper row exists, no
  accepted_supplement row exists; conference-adjacent candidates (Q17 JPCS
  item, E20 Teion Kogaku item) were excluded, not promoted. Honest and
  consistent. PASS.

## 7. CRITICAL live sampling — 20 rows opened by me (2026-07-28)

Adversarial spread: all four streams; direct-publisher route (9) and
PMC-mirror route (11); years 1996–2026; 3 pilot-carried rows; the
correction case; and all three rows lacking a search-log trail were either
opened or adjacent-checked. Every opened record was compared on
title/authors/year/venue/DOI, venue peer-review character, and
correction/retraction banners.

| Row | Route opened | Result |
|---|---|---|
| P0002 (pilot, hts, 2025) | IOPscience ae26d7 | Exact match (SST 38/12, 125023; OA; no notices) |
| P0004 (pilot, hall, 2026) | IOPscience ae6c59 | Match (PPCF 68/6; live art. no. 065013 not stated in ledger venue; ledger authors transliterate diacritics, e.g. Ďuran→Duran — minor) |
| P0008 (pilot, hall, 2020) | jsss.copernicus.org | Exact match incl. the published review statement (edited by Michael Kraft, two anonymous referees) |
| P0009 (hall, 1996) | IOPscience 0268-1242/11/4/020 | Exact match (Semicond. Sci. Technol. 11, 576; recd 3 Jul 1995 / acc 3 Jan 1996) |
| P0012 (hall, 2020, correction case) | PMC7441171 | Exact match; correction notice verbatim as disclosed; no retraction |
| P0013 (hall, 2015) | PMC4410644 | Exact match (Nat Commun 6:6806) |
| P0016 (hall, 2012) | PMC3304160 | Exact match (Sensors 12/2, 2162; PMID 22438758) |
| P0020 (hybrid, 2001 seminal) | IOPscience 0029-5515/41/6/307 | Exact match (Pustovitov, Nucl. Fusion 41, 721) |
| P0021 (hybrid, 2025) | IOPscience ae1621 | Match (Nucl. Fusion 66/1, 016015; issue year 2026, published online 10 Nov 2025 — ledger uses 2025 with exact dates disclosed in notes; defensible, not material) |
| P0022 (hybrid, 2025) | PMC12115906 | Exact match (Sensors 25/10, 3116) |
| P0028 (hybrid, 2026) | IOPscience ae7719 | Exact match (PPCF 68/6, 065038; single-anonymous, 1 revision as noted) |
| P0031 (hybrid, 2024, E10-supersession) | PMC11435727 | Exact match (Sensors 24/18, 6071 = DOI 10.3390/s24186071, confirming the disclosed E10→P0031 identity) |
| P0034 (hts, 2025; no search-log trail) | IOPscience adb24f | Exact match (Physica Scripta 100/3, 035522) |
| P0037 (hts, 2023) | PMC9937513 | Exact match; author-manuscript status disclosed correctly (IEEE TAS 33/5, 4600105) |
| P0039 (hts, 2026) | IOPscience ae77b2 | Exact match (SST 39/6, 065017) |
| P0041 (hts, 2013 seminal) | PMC7453491 | Exact match per the PMC citation record (TAS 24/3, 4600605, 2013; print issue June 2014 — ledger follows its stated source) |
| P0045 (hts, 2013; no search-log trail) | PMC3828451 | Exact match (SpringerPlus 2:599) |
| P0049 (power, 2023) | PMC10761399 | Exact match (Ann Biomed Eng 52/1, 36–47) |
| P0051 (power, 2024) | PMC10899663 | Exact match (Sci Rep 14:4746) |
| P0057 (power, 2019) | PMC6631602 | Exact match (Micromachines 10/6, 406) |

Result: **zero fabricated rows, zero materially wrong rows, zero
unrecorded retractions/corrections** across a 20-row (32%) adversarial
sample. All sampled venues are established peer-reviewed journals. My own
access: PMC, IOPscience, and Copernicus all opened successfully for me; I
did not need to test the domains the candidate reported as blocked
(mdpi.com, nature.com, pubs.aip.org, link.aps.org, SpringerLink,
ScienceDirect, IEEE Xplore), because every accepted row's recorded
verification URL was directly openable; the candidate's block account is
internally consistent (blocks appear only in EXCLUSIONS/notes, never as a
basis for acceptance). CRITICAL CHECK: PASS.

## 8. Search log / exclusions plausibility, scope boundary

- 62 queries Q01–Q62; my per-stream tally: hall 21, hybrid 14, hts 11,
  power 16 (sum 62) — multiple query families per stream, matching
  RUN_META's ">=10 per stream" claim. Explicit negatives logged (Q50, Q51,
  Q55, Q57, Q60, plus other no-acceptance queries). PASS.
- E01–E20 coherent; pilot E01–E11 carried (with pilot-context phrasing
  adapted and E10 explicitly annotated as superseded by P0031 — disclosed,
  not silent). Exclusion reasons are specific and policy-consistent,
  including the two promoted-refusal cases E19 (peer-reviewed but
  content-type out of scope) and E20 (peer-review status unresolved). PASS.
- SEARCH_PROTOCOL is PRISMA-inspired and explicitly disclaims formal
  systematic review / meta-analysis status. No ranking, novelty, or
  synthesis language anywhere in the candidate (relevance cells state
  topical connection only). PASS.
- Trail gap: P0012, P0034, and P0045 are named in NO SEARCH_LOG.csv note
  (checked by ID, DOI, PMC number, and title terms), contradicting
  SELF_CHECK §18's claim that every new paper_id is named in at least one
  Q11–Q62 note. All three rows are genuine (each verified live above), so
  this is a documentation/self-check accuracy gap, not fabrication.
  Recorded as defect 3 (minor).

## 9. RUN_META / SELF_CHECK honesty; model record

- RUN_META names agent `pap06-sonnet-high`, requested Sonnet 5 / high,
  observed model/effort `NOT_EXPOSED`, start/end `NOT_EXPOSED` — correct
  discipline; requested vs observed kept separate; treated here as missing
  observation, not mismatch and not proof. `.claude/agents/
  pap06-sonnet-high.md` frontmatter independently requests model `sonnet`,
  effort `high`, matching the route. PASS.
- Web-activity accounting is consistent with the logs except one slip:
  "62 successful verification fetches, one per accepted paper P0009–P0062"
  — P0009–P0062 is 54 papers; the arithmetic that reconciles (62 + 2
  excluded-successful + 7 blocked = the stated ~71 attempts) implies the 62
  fetches covered all 62 accepted rows and the range label is wrong.
  Recorded as defect 4 (minor).
- SELF_CHECK recounts otherwise reproduced exactly (rows, streams, DOI
  sweep, vocabulary, FLOW equalities, exclusion tallies), with the three
  specific inaccuracies captured as defects 1–3.

## Defects

1. **Minor** — Recency tally miscount. FLOW.json notes and SELF_CHECK §5
   state 42 accepted_core in 2020–2026 (hts 10); correct recount is 43
   (hts 11) — P0043 (year 2022) was omitted from the hts recency list
   (SELF_CHECK's hts lists cover 16 of 17 rows). Gate unaffected (both
   >= 16; true value higher than claimed). Affected files:
   `outputs/B12_lit_search/attempt-1/FLOW.json` (notes text),
   `outputs/B12_lit_search/attempt-1/SELF_CHECK.md` §5. Acceptance test on
   repair: recount of 2020–2026 rows equals the stated figure.
2. **Minor** — Overstated stability claim. SELF_CHECK §8 and FLOW.json's
   `hard_gate_p0001_p0008_stable` line say only publisher_url changed on
   carried rows; in fact relevance/notes/access_status prose was also
   trimmed/reworded on P0001 and P0003–P0008 (bibliographic and status
   fields byte-identical; edits meaning-preserving and partly required to
   strip pilot-context phrasing). Affected files: SELF_CHECK.md §8,
   FLOW.json. Acceptance test on repair: the stability statement lists the
   actual set of changed cells.
3. **Minor** — False completeness claim for the search trail. SELF_CHECK
   §18 asserts every new paper_id P0009–P0062 is named in a SEARCH_LOG.csv
   note; P0012, P0034, P0045 appear nowhere in the log. The three rows are
   genuine (verified live), but their discovery queries are undocumented.
   Affected files: SELF_CHECK.md §18, SEARCH_LOG.csv. Acceptance test on
   repair: either log the discovery queries or scope the §18 claim to the
   rows it actually covers.
4. **Minor** — RUN_META fetch-accounting label slip: "62 successful
   verification fetches, one per accepted paper P0009–P0062" (a 54-paper
   range) is internally inconsistent; the reconciling reading is 62 fetches
   across all 62 accepted rows. Affected file: RUN_META.md. Acceptance test
   on repair: fetch count and paper-ID range agree.

No critical defects. No major defects. The four minor defects are
self-description inaccuracies; none touches a hard gate, none involves
fabricated or materially wrong citation metadata, and each error's
direction is neutral or against the candidate's own claimed margin.

## Limitations

- I sampled 20 of 62 rows live (32%), risk-weighted toward new 2025–2026
  items, author-manuscript mirrors, seminal old items, the correction case,
  and the three trail-less rows; the remaining 42 rows were verified
  structurally but not re-opened.
- I did not independently query Retraction Watch/Crossref for
  second-source retraction screening (the candidate disclosed the same
  limitation); absence of notices on the opened records is evidence of
  "none found," not proof.
- WebFetch page conversions summarize landing pages; peer-review-process
  details beyond what those pages expose were not independently audited
  for every sampled row.
- Observed worker model identity is `NOT_EXPOSED` in RUN_META; requested
  route intent is verified from the agent definition, and no observation
  contradicts it.

VERDICT: PASS
