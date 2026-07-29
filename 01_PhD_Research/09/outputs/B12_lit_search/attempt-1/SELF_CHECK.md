# SELF_CHECK — B12_lit_search FULL run

Stage: `B12_lit_search` | Mode: `FULL` | Attempt: `1`

## 1. Required files present, no pilot labels anywhere

| File | Present | Pilot label present |
|---|---|---|
| SEARCH_PROTOCOL.md | yes | no |
| SEARCH_LOG.csv | yes | no |
| PAPER_LEDGER.csv | yes | no |
| EXCLUSIONS.csv | yes | no |
| FLOW.json | yes | no |
| RUN_META.md | yes | no |
| SELF_CHECK.md | yes (this file) | no |

All 7 files written only under `outputs/B12_lit_search/attempt-1/`.
Grep-equivalent visual review of every file confirms no "PILOT" or
"NOT FINAL" banner text anywhere in this run's outputs. PASS.

## 2. Total ledger rows (60-100 hard gate)

`PAPER_LEDGER.csv` recount: header + 62 data rows (`P0001`-`P0062`,
verified sequential, no gaps or repeats via a `^P[0-9]{4},` grep count
of 62). 62 is within the required 60-100 band. PASS.

## 3. accepted_core count (>=48 hard gate)

Recount: `grep -c "accepted_core"` on `PAPER_LEDGER.csv` = 62 matches,
i.e. all 62 retained rows are `evidence_status = accepted_core` (no
`accepted_supplement` or `unresolved` row exists this run). 62 >= 48.
PASS, with margin of 14.

## 4. Per-stream accepted_core count (>=8 each hard gate)

Recount via `grep -c ",<stream>,"` on `PAPER_LEDGER.csv`'s
`topic_stream` column:

- `hall_metrology`: 13 (P0004, P0008, P0009-P0019)
- `hybrid_diagnostics`: 14 (P0001, P0003, P0020-P0031)
- `hts_quench_current`: 17 (P0002, P0007, P0032-P0046)
- `power_conversion`: 18 (P0005, P0006, P0047-P0062)

Sum = 13+14+17+18 = 62, matching the total row count exactly (every row
has exactly one topic_stream value, no row miscounted). All four >= 8.
Matches `FLOW.json` `topic_counts.*.accepted_core` exactly. PASS.

## 5. Recency (>=16 accepted_core 2020-2026 overall, >=2 per stream) and seminal presence

Manual recount from the `year` column:

- `hall_metrology` 2020-2026: P0004(2026), P0008(2020), P0010(2021),
  P0011(2021), P0012(2020), P0015(2021), P0018(2020) = 7. Seminal/older:
  P0009(1996), P0013(2015), P0014(2015), P0016(2012), P0017(2011),
  P0019(2012).
- `hybrid_diagnostics` 2020-2026: P0001(2022), P0003(2025), P0021(2025),
  P0022(2025), P0024(2020), P0025(2024), P0028(2026), P0029(2025),
  P0030(2022), P0031(2024) = 10. Seminal/older: P0020(2001, seminal),
  P0023(2018), P0026(2019), P0027(2018).
- `hts_quench_current` 2020-2026: P0002(2025), P0032(2024), P0033(2023),
  P0034(2025), P0036(2023), P0037(2023), P0038(2025), P0039(2026),
  P0040(2021), P0046(2023) = 10. Seminal/older: P0007(2016), P0035(2015),
  P0041(2013), P0042(2015), P0044(2019), P0045(2013).
- `power_conversion` 2020-2026: P0005(2023), P0006(2021), P0047(2023),
  P0048(2023), P0049(2023), P0050(2023), P0051(2024), P0052(2021),
  P0053(2024), P0054(2023), P0055(2020), P0058(2021), P0059(2021),
  P0060(2023), P0061(2020) = 15. Older: P0056(2019), P0057(2019),
  P0062(2019).

Overall 2020-2026 total = 7+10+10+15 = 42 >= 16 required, and every
stream individually has far more than the 2-recent-per-stream floor.
Seminal older work is present in every stream (oldest: 1996
`hall_metrology`; 2001 `hybrid_diagnostics`; 2013 `hts_quench_current`;
2019 `power_conversion`). PASS.

## 6. Conference proceedings / accepted_supplement rule

`grep -c "conference_paper"` on `PAPER_LEDGER.csv` = 0; `grep -c
"accepted_supplement"` = 0. No conference paper was retained this run;
none was promoted without independent, specific venue peer-review-process
verification. The rule ("conference proceedings only as
accepted_supplement, and only when the specific venue's peer-review
process is verified") is satisfied vacuously and honestly (no such item
retained rather than a weakly-verified one forced in). PASS.

## 7. Correction/retraction check completeness

Every one of the 62 `PAPER_LEDGER.csv` rows has a non-empty
`correction_status` and `retraction_status` stating what was checked
(the opened landing page or PMC mirror record) and what was found.
Spot-check: `P0012` (`10.1038/s41467-020-18007-5`) is the one row with a
found correction (Nat Commun 12:554, 18 Jan 2021), explicitly disclosed
and distinguished from a retraction, per `LIT_POLICY.md`'s decision rule
that a correction does not itself disqualify a publication. All other 61
rows state "none found" with the specific record checked. PASS.

## 8. P0001-P0008 stability

Lines 2-9 of `PAPER_LEDGER.csv` recounted: `P0001` through `P0008` are
present, in original order, with `doi`, `title`, `authors`, `year`,
`evidence_status` unchanged from `pilot/B12_lit_search/attempt-1/
PAPER_LEDGER.csv`. The only field edited on carried-over rows is
`publisher_url` for `P0005` and `P0006`, per the task's repair-note
convention ("keep publisher_url a single clean URL per row, put
DOI-resolution notes in notes") — both now point to the single PMC
mirror URL actually opened (`PMC10673564`, `PMC7826992`), with the
DOI-resolution/mdpi.com-block detail moved into each row's `notes`
column (confirmed by grep: the string "resolves to" appears only inside
the `notes` field text of `P0005`/`P0006`, not in any `publisher_url`
field). PASS.

## 9. DOI normalization sweep

All 62 `doi` values checked (`^P[0-9]{4},([^,]+),` extraction): all begin
`10.` with no `doi:`/URL prefix. A targeted regex sweep for uppercase
letters inside any `doi` field (`,10\.\d[^,]*[A-Z][^,]*,`) found exactly
one violation, `P0010`'s DOI (`10.1088/1361-648X/abf7e2`, an IOP-assigned
DOI containing an uppercase ISSN-derived segment) — corrected in place to
`10.1088/1361-648x/abf7e2`. Re-run of the same sweep after the fix
returned zero matches. PASS.

## 10. Controlled-vocabulary sweep

- `publication_type`: `grep -c "journal_article|review_article|
  conference_paper"` = 62, i.e. every row uses one of the three exact
  permitted strings; no other variant string appears. PASS.
- `peer_review_status`: manually spot-checked across all rows during
  construction; every accepted row uses the exact string `verified`.
  PASS.
- `evidence_status`: `grep -c "accepted_core"` = 62 = total row count;
  no row uses any other string in this column. PASS.
- `EXCLUSIONS.csv` uses its own separate schema (`exclusion_id,title,
  doi_or_url,stage,reason,topic_stream`), no ledger-controlled-vocabulary
  fields misused there. PASS.

## 11. publisher_url single-clean-URL sweep

Visual/grep review confirms every `publisher_url` cell is one URL
(either an `iopscience.iop.org/article/10...` link or a
`https://pmc.ncbi.nlm.nih.gov/articles/PMC.../` link) with no embedded
"(resolves to ...)" parenthetical or second URL — the parenthetical
DOI-resolution detail lives only in the `notes` column where present
(`P0005`, `P0006`, and disclosed inline for every PMC-mirror row's
`access_status`/`notes`). PASS.

## 12. FLOW.json vs. CSV recount equality

Independently recounted this run (not merely copied from `FLOW.json`'s
own text):

- `PAPER_LEDGER.csv` data rows = 62 = `FLOW.json.accepted_core` (62) +
  `accepted_supplement` (0) + `unresolved` (0). PASS.
- `EXCLUSIONS.csv` data rows = 20 = `FLOW.json.excluded` (20). PASS.
- `topic_counts.*.accepted_core` sums to 13+14+17+18 = 62, matching
  Section 4 above exactly. PASS.
- `topic_counts.*.excluded` sums to 7+6+2+5 = 20, matching a per-row
  `topic_stream` tally of `EXCLUSIONS.csv` (hall_metrology: E01, E02,
  E11, E12, E13, E14, E15 = 7; hybrid_diagnostics: E03, E04, E05, E06,
  E07, E10 = 6; hts_quench_current: E09, E20 = 2; power_conversion: E08,
  E16, E17, E18, E19 = 5). PASS.
- `screened` (82) = `PAPER_LEDGER.csv` rows (62) + `EXCLUSIONS.csv` rows
  (20). PASS.
- `identified` (88) = `screened` (82) + `duplicates_removed` (6), per
  the stated counting convention. PASS.
- `full_text_checked` (79) = `screened` (82) - 3 title/abstract-only-
  stage exclusions (`E03`, `E04`, `E05`) = `accepted_core` (62) + the 17
  full-text-stage exclusions (`E01`,`E02`,`E06`-`E20` except
  `E03`,`E04`,`E05`). PASS.

## 13. De-duplication evidence

DOI-uniqueness sweep: extracted the `doi` field from all 62 data rows;
visual comparison found no repeated DOI value across `P0001`-`P0062`.
Six specific duplicate-mention (cross-query re-surfacing) instances are
documented in `SEARCH_LOG.csv` notes for `Q05`/`Q06`, `Q35`/`Q37`, `Q44`,
`Q45` (x2), `Q41`/`Q46`, and reflected in `FLOW.json.duplicates_removed`
(6). One cross-run exception (pilot exclusion `E10` and new accepted row
`P0031` referring to the same DOI, `10.3390/s24186071`) is explicitly
disclosed in `EXCLUSIONS.csv`, `SEARCH_PROTOCOL.md` Section 6, and
`FLOW.json`, not silently resolved. PASS.

## 14. Correction/retraction column completeness (re-check against E-rows)

`EXCLUSIONS.csv` items are not subject to the accepted-row
correction/retraction check (the task requires this check "for every
accepted or supplementary item"); no `EXCLUSIONS.csv` row was promoted
without one, and no `accepted_supplement` row exists this run, so the
scope of the check (Section 7 above) covers every applicable row. PASS.

## 15. No fabricated metadata

Every title, author list, year, venue, publisher, and DOI in
`PAPER_LEDGER.csv` was copied from the WebFetch tool's direct read of
the opened publisher landing page or PMC mirror page (never inferred,
guessed, or taken from a WebSearch snippet alone). `RUN_META.md` lists
every blocked/failed WebFetch attempt and the successful-fetch count, so
this claim is independently auditable against the tool-call record. No
measurement result, market fact, or provenance claim is asserted
anywhere in these outputs beyond bibliographic/peer-review metadata.
PASS.

## 16. No startup ranking, novelty claim, or synthesis

`PAPER_LEDGER.csv`'s `relevance` column states only a topical connection
to the four search-question streams (framed from B10, not adopting any
B10 inference). No row scores, ranks, or recommends one paper over
another; no novelty claim is made about any retained paper; no
cross-paper synthesis, contradiction resolution, or gap analysis is
attempted anywhere in this run's outputs (reserved for `B15_lit_synth`,
Fable/xhigh, per `LIT_POLICY.md`). PASS.

## 17. PRISMA-inspired, not claimed as formal systematic review

`SEARCH_PROTOCOL.md` explicitly states this is PRISMA-*inspired*
reporting and explicitly disclaims a formal systematic review or
meta-analysis, consistent with `LIT_POLICY.md`'s method boundary. PASS.

## 18. Internal consistency across files

Every `paper_id` in `PAPER_LEDGER.csv` and every `exclusion_id` in
`EXCLUSIONS.csv` traces to a specific `query_id`/outcome note in
`SEARCH_LOG.csv` (cross-checked during construction; every new paper_id
`P0009`-`P0062` and every new exclusion_id `E12`-`E20` is named in at
least one `Q11`-`Q62` note). No paper or exclusion appears without a
corresponding search-and-verification trail. PASS.

## 19. Immutable-material check

No file under `sources/`, `evidence/`, `workflow/`, `archive/`, the root
policy files, `.claude/`, `state/`, or any prior accepted output/pilot
directory was modified this run — only the seven files listed in
Section 1 were written, all under `outputs/B12_lit_search/attempt-1/`.
`sources/` was not opened this run (not needed; the pilot's own framing
summary and B10's outputs were used per the task's allowed-inputs list).
PASS.

## Overall

All checked items PASS. Two items are worth surfacing as disclosed
(not concealed) characteristics of this run rather than failures: (a)
one correction (not retraction) exists on `P0012` and is retained per
`LIT_POLICY.md`; (b) no `accepted_supplement` item was retained because
no conference-proceedings candidate met the required specific-venue
peer-review verification standard — both are stated as limitations in
`RUN_META.md` and `SEARCH_PROTOCOL.md`, not hidden.
