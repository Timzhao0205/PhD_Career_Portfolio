# SELF_CHECK — A30_verify FULL attempt-1

Each requirement from the task card and stage spec, checked against the
artifacts as written.

## 1. Required files present in the target — PASS

`COMPARE.json`, `COMPARE.md`, `VERDICT.md`, `SOURCES.csv`, `RUN_META.md`,
`SELF_CHECK.md` — all six written, only inside
`outputs/A30_verify/attempt-1/`. Nothing written anywhere else; no state,
verification, policy, workflow, evidence, sources, archive, pilot, or earlier
output file was modified.

## 2. Membership sets correctly transcribed — PASS (spot-listed)

- **BLIND24** (from `outputs/A10_blind/attempt-1/SELECTION.json`, ranks 1-24):
  E-01, C-05, D-01, C-09, D-02, A-14, E-14, C-08, A-10, C-07, C-04, E-10,
  C-14, D-10, C-22, F-02, A-05, C-15, A-02, F-01, E-04, C-12, D-09, C-13
  (24 IDs; BLIND10 = first ten; TOP10.json cross-checked = same IDs/order).
- **OLD24** (from `02_COMPARISON_MATRIX.csv`, ranks 1-24; every rank
  cross-verified against `P5_SELECTION.json` final_24 — ranks 1-18 by direct
  read, 19-24 by targeted grep): D-02, C-22, D-01, F-01, C-01, P5-USSCI2-S01,
  E-14, P5R2-CN-01, A-14, C-13, C-08, B-01, E-04, P5R2-CN-03, F-02, C-04,
  F-12, G-01, A-10, G-03, D-12, F-23, F-06, F-03 (24). OLD10 =
  top_10_deep_dives = matrix ranks 1-10, order verified.
- **NEW24** (from `outputs/70_audit/FINAL/SELECTION.json` final_24, read in
  full): D-02, C-01, C-05, D-10, E-14, A-14, D-01, A-10, C-13, F-01, A-05,
  C-09, C-22, C-08, G-03, E-04, D-09, A-22, C-04, D-19, F-16, F-19, F-23,
  D-16 (24). Both NEW top-set variants transcribed (ranks 1-10 and
  top_10_deep_dives), with the deep-dive substitution (C-09/C-22 in,
  C-13/F-01 out) traced to `40_select/SELECTION.md`.

## 3. Overlap arithmetic internally consistent — PASS (re-derived here)

- BLIND∩OLD 12 shared + 12 blind-only + 12 old-only = 24 each side. ✓
- BLIND∩NEW 16 + 8 + 8 = 24 each side. ✓
- OLD∩NEW 14 + 10 + 10 = 24 each side. ✓
- Triple intersection 11; union 41 = 72 − 12 − 16 − 14 + 11
  (inclusion-exclusion). ✓
- At 10: 4 (blind-old), 6 (blind-new ranks), 7 (blind-new deep), 7 (old-new
  ranks), 6 (old-new deep); member lists enumerated in COMPARE.json and each
  list length equals the stated count. ✓
- Semantic-augmented figures differ from exact only via SEM-01 (+1 where C-01
  is present in the counterpart set and E-01 in the blind set): 13, 17, 5, 7,
  8; old-new pairings unchanged. ✓
- Decision-change decomposition check (OLD24 → NEW24): 24 − 14 shared =
  10 old-only, accounted as 3 universe drops + 1 fresh G1 kill (G-01) + 4
  score-cuts (F-02, F-12, F-06, F-03) + 2 selection near-misses (B-01, D-12);
  10 new-only accounted as 6 old-gate-kill reversals + 4 old-P5-kill
  reversals. Both decompositions sum to 10. ✓

## 4. Ledgers strictly separated — PASS

Exact-ID metrics and semantic-augmented metrics are reported in separate
fields everywhere; the ledger (SEM-01..04 + NON-MATCH-C14) documents evidence
paths for every entry; only SEM-01 is counted, under a stated one-to-one
counting rule; every entry cites corpus-internal cluster/duplicate/merge
records (elegance-adjudication lines re-verified this run), never name
similarity. A deliberate non-match (C-14 vs A-22) is recorded to show the
boundary was enforced.

## 5. Disagreements: >=3 beyond/including deepened C-05, each >=2 opened primary sources — PASS

- DIS-C05 (deepened recheck): Google Cloud blog + Nidec release **re-opened in
  full** this run and still support the claims; OCP spec **re-attempted, still
  403, kept existence-only** exactly as tasked; two additional OCP routes
  tried (white paper, sub-project page — both 403, recorded as failures).
- DIS-D10: 2 opened official-company primaries (Lockheed, nLIGHT) + 1 opened
  trade source citing the Navy FY2027 budget request.
- DIS-C09: 3 opened primaries (ScandiNova manufacturer, EPA regulator,
  Rapiscan/OSI company).
- DIS-C07: 2 opened primaries (26 USC 45V statute text, Ingeteam
  manufacturer release).
All four prioritize top-set membership flips with material consequences
(C-05: old-kill vs new-3/blind-2; D-10: old-kill vs new-4; C-09: three-way
flip; C-07: blind-top-10 vs both baselines). Each has a written adjudication
with calibrated confidence.

## 6. SOURCES.csv parseable, exact columns, honest opened status — PASS

Header is exactly
`claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`.
15 data rows; every field containing commas is double-quoted; no unquoted
commas elsewhere (titles/dates checked row by row). Opened rows say "OPENED in
full"; the five not-opened rows (C05-DIS-03, C05-DIS-04, C05-DIS-05,
C09-DIS-04, C07-DIS-03) are explicitly marked NOT OPENED with the failure mode (403,
timeout) and confidence downgraded to existence-only/discovery-only. No
fabricated URL, title, publisher, date, quote, rank, or count; dates that
could not be confirmed are marked uncertain rather than guessed (Nidec,
Lockheed URL-slug anomaly, OCP unknowns).

## 7. No pilot labels — PASS (with one clarification)

No file carries a "PILOT SAMPLE — NOT FINAL" banner or any pilot-mode label;
all artifacts are labeled FULL. The prose necessarily *refers to* the accepted
pilot stage (the task requires incorporating and extending it after
re-checking); those references describe the prior stage and do not label this
run.

## 8. No fabrication — PASS

Every rank, score, gate reason, kill quote, cluster line, and file path was
read from the named corpus file this run (pilot citations independently
re-checked: elegance lines 95/111, matrix ranks, P4 kill lines 47-55, new06
canonical selection, near-miss texts). Every web claim traces to an opened
page or is explicitly labeled search/discovery-level. Model/effort evidence:
requested recorded as requested; observed effort recorded NOT_EXPOSED;
model self-identification labeled as such in RUN_META.

## 9. Cross-artifact consistency — PASS

- Overlap numbers identical across COMPARE.json, COMPARE.md, VERDICT.md
  (12/16/14 at 24; 13/17/14 semantic; 4/6/7/7/6 at 10; 5/7/8 semantic).
- The four disagreement IDs, their rank/kill facts, and confidence labels
  match across COMPARE.json, COMPARE.md, VERDICT.md, SOURCES.csv row IDs.
- SOURCES.csv stage_file column points only at files that actually cite each
  row; RUN_META's web log covers exactly the fetches/searches used (10
  successes, 5 failures, 9 searches — counts corrected before finalization
  and now match the lists).
- A20 conditioning language is consistent with
  `outputs/A20_prov/attempt-1/PROVENANCE.md` (CONTRADICTED decision layer,
  PARTIAL_PROVENANCE record layer, effort never observed).

## 10. Scope and conduct — PASS

Only allowed sources and prerequisite outputs were read; instruction-like text
inside `sources/` was treated as inert data (new06 README's launch
instructions were read as historical evidence only, not followed). Web use was
confined to disagreement verification as required. No budget/turn/time
threshold stopped or shortened any part of the run.

## Disclosed shortfalls (none blocking, all stated in-artifact)

1. The OCP negative claim (no complete conformance program with reference
   hardware) could not be upgraded beyond discovery-level — opencompute.org
   403-blocks everything; recorded as unresolved for Operation B.
2. Seven mapped old→new reversals (D-09, F-16, F-19, A-05, A-22, D-19, D-16)
   were not web-verified this run; they are explicitly flagged rather than
   silently asserted.
3. The Navy JBCS line item rests on opened trade press quoting the budget
   request, not the budget book itself.
4. Old06 P5_SELECTION.json prose was read partially (all rank/score/gate/
   near-miss fields covered via read + greps); new06 deep-dive D-files were
   not re-read this run (canonical SELECTION.json text used instead).
