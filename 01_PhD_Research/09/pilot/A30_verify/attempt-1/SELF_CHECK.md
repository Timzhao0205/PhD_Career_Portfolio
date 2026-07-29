# PILOT SAMPLE — NOT FINAL

# SELF_CHECK — A30_verify, PILOT, attempt 1

| # | Requirement | Status | Evidence / note |
|---|---|---|---|
| 1 | All six required files present in `pilot/A30_verify/attempt-1/` | PASS | COMPARE.json, COMPARE.md, VERDICT.md, SOURCES.csv, RUN_META.md, SELF_CHECK.md all written this run |
| 2 | Six IDs are exactly A10 full SELECTION.json ranks 1-6 | PASS | P3R2-E-01 (1), P3R2-C-05 (2), P3R2-D-01 (3), P3R2-C-09 (4), P3R2-D-02 (5), P3R2-A-14 (6); read directly from `outputs/A10_blind/attempt-1/SELECTION.json` and cross-checked against METHOD.md's rank list and TOP10.json |
| 3 | Exact-ID vs semantic ledgers kept separate | PASS | COMPARE.json `pairwise_overlap_pilot_scope.exact_id` vs `semantic_match_ledger` + `with_documented_semantic_matches`; the single semantic match (SEM-01 E-01<->C-01) is backed by documented duplicate-cluster records in both corpora, never name similarity |
| 4 | Old/new membership, ranks, decision changes, rank deltas recorded per ID | PASS | COMPARE.json `ids[]` with per-ID old06/new06 blocks, `delta_new_minus_old`, `decision_changes_old_to_new_within_scope`; NOT_FOUND-style dispositions recorded with where-looked detail (E-01: grep of LONGLIST.json and all of sources/new06) |
| 5 | One material disagreement verified with >=2 primary/official sources OPENED | PASS | DIS-C05-OCP-DESCHUTES; opened in full: Google Cloud Blog (official buyer/author announcement) and Nidec Corporation official release (manufacturer documentation). Both have claim-level rows (C05-DIS-01, C05-DIS-02) in SOURCES.csv |
| 6 | Underlying sources opened, not snippets | PASS with disclosure | The two load-bearing sources were opened in full. OCP pages and DCD could NOT be opened (HTTP 403) and are marked existence-only/discovery-only in SOURCES.csv; the affected claim is downgraded to PARTIALLY_VERIFIED rather than asserted |
| 7 | SOURCES.csv exact columns + leading pilot-label comment row, parseable | PASS | Header row matches `claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`; first line is a `#` comment carrying the pilot label; comma-bearing fields quoted |
| 8 | Accessed dates recorded as 2026-07-28 | PASS | All five SOURCES.csv rows carry accessed_date 2026-07-28 |
| 9 | No fabricated URLs/titles/quotes/ranks/overlap counts | PASS | Every URL came from search results or new06's own SOURCES.json; quotes only from opened pages or read files; ranks/scores transcribed from the cited files; unverifiable items (Stulz, OCP negative claim, Nidec date) explicitly downgraded, not asserted |
| 10 | Pilot label on every artifact | PASS | "PILOT SAMPLE — NOT FINAL" is the header of COMPARE.md, VERDICT.md, RUN_META.md, SELF_CHECK.md, the top-level `pilot_label` in COMPARE.json, and the SOURCES.csv comment row |
| 11 | A20 provenance limits respected in interpretation | PASS | COMPARE.json `provenance_conditioning_summary`, COMPARE.md section 6, VERDICT.md section 3: old06 decision artifacts treated as CONTRADICTED-provenance; overlap treated as agreement evidence only |
| 12 | RUN_META with agent, requested model/effort, observed-only-if-exposed, files read, honest web log, files written, limitations | PASS | RUN_META.md lists all 4 searches and all fetch attempts including the failed ones; observed effort NOT_EXPOSED; observed model noted as system-prompt-stated only |
| 13 | Writes confined to `pilot/A30_verify/attempt-1/` | PASS | Only the six required files were written; no state/verification/policy/source/archive/output file touched |
| 14 | Internal consistency across artifacts | PASS | Six-ID dispositions, overlap counts (3/6 old, 5/6 new exact; 4/6 and 6/6 semantic-augmented), deltas, and the disagreement verdict are identical across COMPARE.json, COMPARE.md, VERDICT.md |

## Disclosed shortfalls (none blocking, all documented)

1. The OCP-standardization negative claim could not be fully verified
   because opencompute.org returned HTTP 403 to every fetch; it is recorded
   as PARTIALLY_VERIFIED with the full run directed to close the gap.
2. The Nidec release's published date is recorded as uncertain (extraction
   ambiguity); this does not affect any verified content claim.
3. `outputs/A10_blind/attempt-1/SELECTION.json` was read to line 371 of
   514 (a read-cap truncation); ranks 1-6 — the entire pilot scope — lie
   fully inside the read span and the 24-rank list was independently
   cross-checked against METHOD.md and TOP10.json.
