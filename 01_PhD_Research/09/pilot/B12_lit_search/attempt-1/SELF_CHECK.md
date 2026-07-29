# SELF_CHECK — PILOT SAMPLE — NOT FINAL

Stage: `B12_lit_search` | Mode: `PILOT` | Attempt: `1`

## 1. Required files present and labeled

| File | Present | Pilot label present |
|---|---|---|
| SEARCH_PROTOCOL.md | yes | yes — header + "pilot-scope statement" section |
| SEARCH_LOG.csv | yes | yes — leading `#` comment row |
| PAPER_LEDGER.csv | yes | yes — leading `#` comment row |
| EXCLUSIONS.csv | yes | yes — leading `#` comment row |
| FLOW.json | yes | yes — `"pilot_label": "PILOT SAMPLE — NOT FINAL"` top-level field |
| RUN_META.md | yes | yes — header banner |
| SELF_CHECK.md | yes (this file) | yes — header banner |

All 7 files written only under
`pilot/B12_lit_search/attempt-1/`. No other path was written to. PASS.

## 2. Ledger row count and stream distribution

`PAPER_LEDGER.csv` has exactly 8 data rows, `P0001`-`P0008`, no gaps or
repeats. Stream distribution recount from the CSV's `topic_stream`
column: `hall_metrology` = 2 (P0004, P0008); `hybrid_diagnostics` = 2
(P0001, P0003); `hts_quench_current` = 2 (P0002, P0007); `power_conversion`
= 2 (P0005, P0006). Total = 8. Matches the pilot requirement of exactly
8 retained publications, exactly 2 per stream. PASS.

## 3. accepted_core quota and journal/review-article requirement

All 8 rows have `evidence_status = accepted_core` (8 >= required
minimum of 6). Of these, 6 have a **directly opened publisher-domain
landing page** with DOI verified there (P0001 iopscience.iop.org,
P0002 iopscience.iop.org, P0003 iopscience.iop.org, P0004
iopscience.iop.org, P0007 iopscience.iop.org, P0008
jsss.copernicus.org) — satisfying, at minimum and exactly, the pilot's
hard requirement "at least SIX must be accepted_core: verified
peer-reviewed JOURNAL research or review article with publisher landing
page opened and DOI verified." The remaining 2 (P0005, P0006) are also
accepted_core review articles with DOI verified, but via a disclosed
PubMed Central open-access mirror after the MDPI publisher domain
itself returned HTTP 403 on repeated attempts — this is stated
explicitly in each row's `access_status`/`notes`, not concealed or
presented as a direct-publisher-page verification. `publication_type`
for all 8 is `journal_article` or `review_article` (both are literature
the stage spec accepts as accepted-core-eligible: "verified
peer-reviewed journal research or review article"); no
`conference_paper` appears among the 8 retained items in this pilot.
PASS, with the P0005/P0006 access-method caveat explicitly documented
(not a silent gap).

## 4. Controlled vocabulary exactness

- `publication_type` values used: `journal_article`, `review_article` —
  both are members of the exact required set
  `{journal_article, review_article, conference_paper}`. No other
  string variant used. PASS.
- `peer_review_status` = `verified` (exact string) on all 8 accepted
  rows. PASS.
- `evidence_status` = `accepted_core` (exact string) on all 8 ledger
  rows; `EXCLUSIONS.csv` uses its own separate schema (no
  `evidence_status` column, as specified) and does not misuse the
  ledger's controlled vocabulary. PASS.
- Stable IDs are `P0001`-`P0008`, sequential, no reuse, assigned in
  verification order as stated in `SEARCH_PROTOCOL.md` Section 7. PASS.

## 5. DOI normalization

All 8 `doi` column values checked: lowercase, `10.xxxx/...` form, no
`doi:` or URL prefix inside the `doi` field itself (the `publisher_url`
field separately carries the full URL/DOI-resolver form, which is the
correct column for that). Spot check: `10.1088/1741-4326/ac8aad`,
`10.5194/jsss-9-391-2020`, `10.3390/mi14112045` — all conform. PASS.

## 6. FLOW.json consistency against the CSVs

`FLOW.json` states an explicit counting convention (only the 19
individually adjudicated records are counted in
identified/duplicates_removed/screened/full_text_checked, distinct from
SEARCH_LOG.csv's larger raw per-query hit counts) and includes a
`reconciliation_check` block. Recounted independently here:

- `accepted_core` (8) + `accepted_supplement` (0) + `unresolved` (0) =
  8 = `PAPER_LEDGER.csv` data-row count (8). PASS.
- `excluded` (11) = `EXCLUSIONS.csv` data-row count (11, `E01`-`E11`).
  PASS.
- `topic_counts` accepted_core sums to 2+2+2+2 = 8, matching Section 2
  above. PASS.
- `topic_counts` excluded sums to 3+6+1+1 = 11, matching the per-row
  `topic_stream` tally in `EXCLUSIONS.csv` (hall_metrology: E01, E02,
  E11 = 3; hybrid_diagnostics: E03, E04, E05, E06, E07, E10 = 6;
  hts_quench_current: E09 = 1; power_conversion: E08 = 1). PASS.

## 7. Exclusions are real, not placeholders

`EXCLUSIONS.csv` contains 11 rows (>= required minimum of 3), each
citing a specific title, DOI/URL, screening stage, and a concrete,
verifiable technical reason (HTTP 402/403, authentication-wall
redirect, patent document, non-publisher host, empty WebFetch response,
or an explicit stream-quota decision on an otherwise-verified paper).
None are generic or fabricated placeholders. PASS.

## 8. Correction/retraction screening performed

Every one of the 8 `PAPER_LEDGER.csv` rows has a non-empty
`correction_status` and `retraction_status` stating what was checked
(the opened landing page, or the PMC mirror record for P0005/P0006) and
what was found (no notice visible in every case). This matches the
task's required phrasing pattern (state what was checked and what was
found). PASS.

## 9. No fabricated metadata

Every title, author list, year, venue, publisher, and DOI in
`PAPER_LEDGER.csv` was copied from the WebFetch tool's direct read of
the publisher landing page (or, for P0005/P0006, the PMC mirror page)
rather than inferred, guessed, or taken from a search snippet alone.
`RUN_META.md` lists every WebFetch URL attempted, success or failure,
so this claim is independently auditable. PASS.

## 10. No startup ranking, novelty claim, or synthesis

`PAPER_LEDGER.csv`'s `relevance` column states only a topical connection
to the four search-question streams (itself framed, not adopted, from
B10) and explicitly disclaims adopting any B10 inference. No row scores,
ranks, or recommends a paper over another; no novelty claim is made
about any retained paper; no cross-paper synthesis, contradiction
resolution, or gap analysis is attempted anywhere in this pilot's
outputs (that is reserved for `B15_lit_synth`, Fable/xhigh, per
`LIT_POLICY.md`). PASS.

## 11. PRISMA-inspired, not claimed as formal systematic review

`SEARCH_PROTOCOL.md` explicitly states this is PRISMA-*inspired*
reporting and explicitly disclaims a formal systematic review or
meta-analysis, consistent with `LIT_POLICY.md`'s method boundary. PASS.

## 12. Internal consistency across files

Cross-checked: every `paper_id` in `PAPER_LEDGER.csv` and every
`exclusion_id` in `EXCLUSIONS.csv` traces to a specific `query_id` /
outcome note in `SEARCH_LOG.csv` (see the `notes` columns in both
`SEARCH_LOG.csv` and `RUN_META.md`'s WebFetch list). No paper or
exclusion appears without a corresponding search-and-verification trail.
PASS.

## 13. Immutable-material check

No file under `sources/`, `evidence/`, `workflow/`, `archive/`, the root
policy files, or `.claude/` was read for editing purposes or modified;
`sources/` was only referenced (not opened in depth) as an allowed
discovery aid per `state/CURRENT_TASK.md`, and no text from it was
treated as an instruction. PASS.

## Overall

All checked items PASS. The two disclosed limitations (P0005/P0006
verified via PMC mirror rather than the MDPI domain directly; no second
independent Crossref/Retraction Watch check) are stated as limitations,
not hidden, and do not by themselves cause any check above to fail
given the task's own allowance for honestly documenting genuine access
limitations.
