# SELF_CHECK — B20_align (FULL, attempt-1)

Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh
Every check performed against the files as written this run. Failures and
partial passes are disclosed, not hidden.

## 1. Row count equals stated universe, with A30 reconciliation — PASS

- ALIGNMENT.csv contains exactly **39 data rows** (one header comment line +
  one header line + 39 rows).
- Stated universe: the A30 union of 41 IDs, consolidated by A30's documented
  semantic ledger to 39 underlying directions (SEM-01: E-01→C-01; SEM-02:
  B-01→C-04). 39 = 41 − 2. Within the task's expected ~38-41 band.
- Every one of the 41 union IDs accounted for, checked ID-by-ID against
  COMPARE.json's rank_delta_table (41 entries): 39 appear verbatim as row
  `idea_id` values; P3R2-E-01 appears verbatim inside the C-01 row (name +
  source_version) with SEM-01 cited; P3R2-B-01 appears verbatim inside the
  C-04 row with SEM-02 cited. No ID dropped, altered, or double-counted.
  E-10 and C-15 (SEM-03/SEM-04 members whose canonicals are outside the
  universe) are their own rows, per the consolidation ledger in
  ALIGNMENT.md §2.
- Inclusion boundary stated and defended (ALIGNMENT.md §1): the 41, no
  additions — no non-union idea has a deep-dive-class record (verified by
  Glob of old06 40_DEEP_DIVES and new06 FINAL/DEEP against the membership
  lists).

## 2. Both causal directions per row — PASS

All 39 rows populate both `phd_to_startup` and `startup_to_phd` with one of
the four direction classes plus a parenthetical mechanism summary; the
`mechanism` cell states the causal (or absence) chain for both directions.

## 3. All four classes used where genuinely present — PASS

- Direction level: direct leverage (D-02 fwd), adjacent leverage (D-02 rev;
  C-05, A-14, D-01, A-10, E-04, F-06, D-09 fwd), speculative transfer
  (majority), negative interference (D-10 both; C-07, CN-03 rev —
  opportunity-cost-only, at the weak/adverse boundary per the rubric).
- Overall level: STRONG 1 / MEDIUM 7 / WEAK 30 / ADVERSE 1 (ALIGNMENT.md §4
  table matches the rows one-for-one; recounted).
- ADVERSE reserved for idea-specific interference (D-10 only); E-04's
  export-control friction explicitly adjudicated as conflict-short-of-ADVERSE
  with reasoning stated.

## 4. Stable idea IDs verbatim — PASS

All IDs use the exact A30 forms (P3R2-X-NN, P5-USSCI2-S01, P5R2-CN-01,
P5R2-CN-03). Spot-checked every row ID against COMPARE.json membership
arrays.

## 5. Material claims mapped to B15 paper/EV IDs or stronger sources — PASS

- Every technical mechanism claim cites B10 Cxx (demonstrated vs proposed
  status preserved; proposed Opt2 capabilities are explicitly marked
  conditional/pre-redteam C40 wherever load-bearing) and/or B15 EVxx/Pxxxx/
  gap IDs (EV01-EV35, P0008/P0017/P0033/P0038/P0046/P0050 etc., G1-G6,
  M1-M7, BT-1/3/5).
- Current-market claims map to A30-verified opened primaries (A30:C05/C07/
  C09/D10-DIS rows) or stage-opened sources (S-B20-01..03); all other market
  facts are labeled corpus-dated/refresh-sensitive in-cell, including F-19's
  A30-flagged unverified reversal.
- No citation, DOI, market figure, or model-identity fact invented; no paper
  cited merely because B12 found it — every EV/P citation is tied to a
  specific mechanism or boundary adjudication.

## 6. Pilot analyses carried; corrections kept — PASS

- All six pilot rows (D-02, D-01, A-14, C-13, D-10, C-07) carried with
  substance unchanged; refinements disclosed in ALIGNMENT.md §9 (A-14's
  old06 deep dive now read — confirms, does not change, the class; gap-ID
  cross-references added).
- The pilot's founder-fit corrections (new06 D01 §14; D04 "home ground")
  kept verbatim in the rows; three NEW corrections added (D02 §14, D03,
  D08 §14), each checked against B10's demonstrated-vs-proposed ledger.

## 7. Counterfactuals present — PASS

IMPACT_MAP.md contains explicit with-Opt2 vs without-Opt2 counterfactuals
for: the STRONG idea (D-02, §3), the ADVERSE idea (D-10, §5 zero-delta
control), a MEDIUM representative (D-01, §4), both mechanism clusters
(§6 traceability cluster, §7 demonstrated-asset cluster — covering all
seven MEDIUM ideas), and the overall portfolio (§8) with the class-shift
consequences stated in both branches.

## 8. Schema exact — PASS

ALIGNMENT.csv header is exactly:
`idea_id,idea_name,source_version,phd_to_startup,startup_to_phd,mechanism,evidence,dependency,time_horizon,conflict,confidence,falsifier,action`
(13 columns, matching the pilot and the stage spec). All 39 rows carry 13
fields with comma-containing fields quoted. SOURCES.csv header is exactly
`claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`.
One legend comment line precedes each CSV header, matching the accepted
pilot's format precedent.

## 9. No pilot labels — PASS

No output file carries a PILOT SAMPLE / NOT FINAL label or pilot-mode
header; all six files are marked Mode: FULL. References to the accepted
pilot appear only as provenance ("carried from pilot"), which the task
requires.

## 10. No ranking — PASS

No file orders ideas by attractiveness, assigns scores, or recommends a
portfolio. Corpus ranks are quoted as source facts (A30 data); alignment
classes are classifications with stated rubric, not rankings; action cells
route ideas to B25/B30/B40 without ordering them. The explicit no-ranking
disclaimers appear in ALIGNMENT.md §0/§11 and IMPACT_MAP.md §9.

## 11. Internal consistency — PASS

- Class distribution in ALIGNMENT.md §4 recounted against the CSV rows:
  1/7/30/1 = 39. IMPACT_MAP's "~79% untouched" = 31/39 ✓.
- Consolidation ledger (§2) consistent with row contents and with the
  reconciliation in check 1.
- Direction-class usage listed in ALIGNMENT.md §4 matches the CSV cells.
- Record-read list in RUN_META matches the `source_version` citations in
  every row (spot-checked all 39).
- The rubric text is carried verbatim-in-substance from the accepted pilot.

## 12. Other stage-spec obligations

- Support-stage error correction: PASS — five new06 founder-fit
  overstatements (D01 §14, D02 §14, D03, D04, D08 §14) corrected against
  B10; A30's C-09 EtO reversal applied to the C-09 row's demand framing.
- Both-directions honesty per the stage spec (moat, credibility, data,
  tools, buyer access, timing, constraints, opportunity cost / requirements,
  experiments, datasets, collaborators, publication risk, scope drift,
  conflicts, research value): PASS — encoded across the mechanism/
  dependency/time_horizon/conflict cells rather than as fourteen named
  sub-fields; the load-bearing items for each idea are stated explicitly.
- Efficiency rule (tight rows for far ideas, no padding): PASS — 30 WEAK
  rows each carry a one-to-three-sentence mechanism-absence statement with
  a falsifier; depth is reserved for the 9 significant-coupling/adverse
  ideas.
- Web logging: PASS — one new open (S-B20-03) logged with limitation; two
  pilot rows carried with reuse disclosed; discovery queries listed.

## 13. Disclosed shortfalls (none concealed)

1. `PHD_CORE.md` not opened this run and `LIT_REVIEW.md` only header-read
   (RUN_META limitations); no claim rests on unread material — PHD_FACTS.json
   (C01-C50, full), OPT2.md (partial), EVIDENCE_MAP.csv (full), GAPS.md
   (full) are the cited bases.
2. Record-depth stratification: 7 NEW24 far-domain ideas analyzed from the
   canonical new06 SELECTION.json entries without opening their old06
   evidence files; 8 old06 evidence files read at header depth; CN-03's only
   record anywhere is a screening JSON entry. Each such row discloses its
   record basis, and G-03's row names the fuller-read upgrade path
   explicitly. I judge these sufficient for mechanism-absence determinations;
   a verifier could legitimately demand fuller reads for G-03 and C-22.
3. The MEDIUM class contains four boundary cases (C-05, D-09, E-04, F-06)
   whose classification depends on the rubric's "proposed assets onto core
   elements = adjacent" rule; the rows state the downgrade condition for
   each, so the classifications are falsifiable rather than smoothed.
4. Only one new web source opened; the pilot's two are carried on a same-date
   basis. All market claims are provenance-labeled accordingly.
