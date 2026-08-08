# SELF_CHECK — B40_portfolio FULL attempt-1

Every hard gate from the task card checked against the produced artifacts.
Format: requirement — verdict — evidence.

1. **Exactly 24 ranked directions, unique stable IDs, ranks 1-24, row order
   = rank, convention stated.** PASS. RANKING.csv has exactly 24 data rows;
   manual recount of idea_id values: P3R2-D-02, D-01, C-05, D-09, G-03,
   F-06, A-10, A-14, E-04, F-02, F-01, A-05, C-01, C-04, C-22, E-14, C-13,
   C-08, C-09, F-23, D-19, A-02, C-07, D-10 — 24 values, no duplicates, all
   verbatim members of the A30 41-ID universe. The leading comment row
   states ROW ORDER IS THE RANKING and DECISION.json's ranking array carries
   explicit rank numbers 1-24 in the same order (cross-checked by eye,
   row by row).

2. **Universe reconciliation: 24 + rejected = 41 minus consolidations.**
   PASS. DECISION.json rejected_alternatives has exactly 15 entries (E-10,
   C-14, C-15, C-12, D-12, F-12, G-01, F-03, F-16, F-19, A-22, D-16,
   P5-USSCI2-S01, P5R2-CN-01, P5R2-CN-03); 24 + 15 = 39 = 41 − 2 (SEM-01:
   E-01→C-01; SEM-02: B-01→C-04). No ranked ID appears in the rejected
   list and vice versa (checked pairwise). No semantic duplicate appears
   twice: E-01/B-01 appear only inside origin cells; SEM-03/SEM-04
   counterparts (A-13, A-21) were never universe members.

3. **The 41→24 cut is a decision with every exclusion reasoned.** PASS.
   DECISION.json `selection_rule_41_to_24` states the rule before the
   result; all 15 rejections carry concrete, evidence-cited reasons; no
   prior final-24 was copied (overlaps 20/19/16 vs NEW/BLIND/OLD, §6 of
   PORTFOLIO.md justifies each named divergence).

4. **Schema exact.** PASS. RANKING.csv header is exactly
   `idea_id,name,origin,disposition,score,uncertainty,phd_leverage,power_relevance,first_proof,capital_band,main_risk,falsifier`
   (12 columns); every data row has 12 fields (comma-containing cells
   quoted; no internal double quotes used). SOURCES.csv header is exactly
   the 10-column claim-level schema
   `claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`.

5. **Pilot method carried; pilot rows carried with score changes
   disclosed.** PASS. Scale, bands, weights (sum 1.00), criteria
   definitions, anti-double-counting lines, and disposition vocabulary are
   carried unchanged (DECISION.json scoring_method names the pilot file);
   refinements disclosed in PORTFOLIO.md §3 (tie-break judgments now
   needed; 1.5 band unused; no weight/definition changes). All six pilot
   rows appear in the 24 with scores, uncertainties, and criterion vectors
   UNCHANGED (D-02 3.00/0.80, D-01 2.78/0.84, C-05 2.55/0.90, C-01
   1.57/0.65, C-07 1.07/0.58, D-10 0.65/0.65) — each tagged
   `pilot_row: carried unchanged` in DECISION.json.

6. **Scoring: 0-4 weighted ordinal, declared weights, per-criterion bands,
   conservative half-widths, no false precision; per-criterion audits for
   at least the top 10.** PASS. DECISION.json carries full criterion
   vectors for ALL 24 (top 10 inside top_10, ranks 11-24 inside ranking) —
   exceeding the minimum; aggregates spot-recomputed by hand for D-09
   (2.55), G-03 (2.41), F-06 (2.33), C-04 (1.57), A-02 (1.10) against
   their vectors — all match; uncertainties are weight-x-half-width sums
   (spot-checked D-09 0.975→0.98, E-14 0.69, C-09 0.625→0.63); RANKING.csv
   reports one decimal, DECISION.json two decimals labeled audit-only.

7. **All eleven task criteria scored.** PASS. founder goal, time horizon,
   capital, geography, regulation, technical proof, PhD leverage, shared
   skills, buyer access, defensibility, downside — all present in every
   criterion vector with the pilot's definitions.

8. **Dispositions keep/bridge/watch/stop with pilot definitions; bridge
   cites named B30 gates.** PASS. Counts: bridge 5, watch 12, stop 7,
   keep 0 (the no-keep finding is stated as a finding). Every bridge row's
   first_proof cell names existing BRIDGES.json IDs and gates: D-02 (BR-D,
   BR-B; G-BR-D-pre/exit), D-01 (BR-A/G-BR-A-0, BR-C/G-BR-C, BR-G/G-BR-G),
   D-09 (BR-B PB-2, BR-A Phase 1 PB-5, BR-D-gated credential), G-03 (BR-B
   dossier phase / G-365/W1), F-06 (BR-B PB-1/PB-2, G-365/W1 wedge-kill).
   All cited IDs verified to exist in B30 BRIDGES.json. No new experiment
   was invented. Watch rows name concrete external triggers; stop rows
   state why no trigger exists (or where a family trigger is monitored
   elsewhere).

9. **Power ideas neither forced up nor down.** PASS (judgment, documented):
   strongest-consensus power products C-01/E-14 rank 13/16 on founder
   evidence; power measurement plays D-09/G-03/F-06 rank 4-6 on the same
   rules; B25's non-wedge rule enforced in every power cell; the bucket
   annotation in DECISION.json states this explicitly.

10. **DECISION.json completeness: top_10 with audits; buckets with
    definitions + membership; dependencies (C04 block, publication gate,
    bridge gates, wedge logic W1/W2, disclosure gates); MULTIPLE
    sensitivity cases including PhD-weight halved/doubled, capital shift,
    time-horizon shift, with honest flip reporting; rejected_alternatives
    complete.** PASS. Three cases, six variants, full 24-score arrays per
    variant; real flips reported (D-09/C-05 twice, F-06/G-03, the
    capital-doubled mid-band reshuffle, C-07/A-02 twice), 0.01 near-ties
    flagged as non-separations, and two variants honestly reported as
    flip-free; cross-case stability statement included. Bucket membership
    (5+12+7=24) matches RANKING.csv dispositions row-for-row (checked).

11. **top_10 = ranks 1-10 of the CSV (internal consistency).** PASS.
    top_10 idea_ids in order: D-02, D-01, C-05, D-09, G-03, F-06, A-10,
    A-14, E-04, F-02 — identical to RANKING.csv data rows 1-10.
    Bucket/disposition/rank cross-references in PORTFOLIO.md tables were
    checked against both files (counts and named IDs agree).

12. **PORTFOLIO.md: reasoning; explicit membership/order comparison vs
    OLD24, NEW24, BLIND24 with counts and named changes and why; next
    decisions.** PASS. §6 gives the count table (vs NEW 20/24; vs BLIND
    19/24 exact, 20 semantic; vs OLD 16/24; top-10 overlaps 5/3/5),
    derived by hand against A30 COMPARE.json membership lists this run,
    with SEM-01/SEM-02 handled per A30's counting rule; every named
    inclusion/demotion/exclusion carries a reason. §8 lists next decisions
    in order. Comparison counts are consistent with A30's membership
    (BLIND/OLD/NEW lists transcribed from COMPARE.json, not from memory).

13. **SOURCES.csv claim-level, decision-critical facts mapped; new live
    opens for unverified decision-hinging facts logged honestly.** PASS
    with disclosure: 30 rows map every decision-critical current-market
    fact to A30/B20/B25/pilot opened primaries (reuse + original claim ID
    noted per row, URLs transcribed from the original ledgers — six URLs
    were corrected against those ledgers during this run rather than
    trusted from memory), to internal prerequisite evidence rows (B15
    paper/EV IDs for literature-backed technical claims), or to this run's
    three live web actions: one FAILED fetch disclosed (B40-01) and two
    discovery-level searches (B40-02/03) that opened no page and are
    labeled as never-evidence. Decision-hinging unverified facts that
    remain unverified (ABB shipping; the eight OLD→NEW reversals; D-09
    demand) are named in RUN_META and DECISION.json limitations.

14. **NO pilot labels.** PASS. No artifact in this directory carries a
    pilot label or sample banner; grep-level scan of my own drafted text
    confirms the word "pilot" appears only in provenance references to the
    accepted pilot stage (method lineage required by the task card), never
    as a label on this run's outputs.

15. **RUN_META.md / SELF_CHECK.md present with required content.** PASS.
    RUN_META records named agent, requested model/effort, observed
    model ID, NOT_EXPOSED entries for runtime effort and clock times,
    complete source list, web activity, and limitations.

16. **Write scope.** PASS. Exactly six files written, all inside
    `outputs/B40_portfolio/attempt-1/`: RANKING.csv, DECISION.json,
    PORTFOLIO.md, SOURCES.csv, RUN_META.md, SELF_CHECK.md. No state,
    verification, policy, workflow, evidence, sources, archive, pilot, or
    earlier-output file was modified.

## Disclosed imperfections (none gate-breaking, stated rather than hidden)

- Two exact base-score ties (ranks 3/4 and 13/14) are resolved by stated
  judgment; under two sensitivity variants the 3/4 pair flips — the
  ordering there is judgment inside overlapping bands, exactly as labeled.
- B15 LIT_REVIEW.md was read to §2.1 plus GAPS.md in full, not
  line-by-line to EOF; the EV rows this stage cites were additionally
  consumed through B20/B25's accepted carrying (disclosed in RUN_META and
  SOURCES.csv). No quantitative literature figure was newly asserted from
  memory.
- The searched pages in B40-02/03 were not opened; both rows are marked
  discovery-only and no score rests on them alone (A-05's and C-05's
  affected cells carry 1.0 bands and their dispositions do not depend on
  the search outcomes).
- RANKING.csv one-decimal scores make four rows display as 1.6 (ranks
  12-15); the two-decimal audit values and row order in DECISION.json are
  the authoritative ordering record, as the comment row states.
