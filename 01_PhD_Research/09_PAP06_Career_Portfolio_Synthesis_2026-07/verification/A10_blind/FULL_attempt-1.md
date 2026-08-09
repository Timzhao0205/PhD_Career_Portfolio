# Independent verification report — A10_blind FULL attempt-1

- Stage: `A10_blind` (FULL)
- Candidate: `outputs/A10_blind/attempt-1/`
- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: `Fable 5 / xhigh`
- Observed verifier model: runtime self-identification `Fable 5`
  (`claude-fable-5`); observed effort: `NOT_EXPOSED` (not guessed)
- Date of verification: 2026-07-28

## Scope and inputs

Verified independently against:

- `state/CURRENT_VERIFY.md` (verification card and hard gates)
- `workflow/stages/A10_blind.md` (stage specification)
- `.claude/skills/pap06-native/references/ACCEPTANCE.md` (global rules)
- `workflow/ROUTE.json` (required filenames, model/effort route)
- `MODEL_POLICY.md` (requested/observed evidence conventions)
- Ground truth: `evidence/blind/MANIFEST.json`, `evidence/blind/POOL_1.json`,
  `evidence/blind/POOL_2.json`, `evidence/blind/POOL_3.json`
- Candidate files: `SELECTION.json`, `TOP10.json`, `METHOD.md`, `RUN_META.md`,
  `SELF_CHECK.md` (all read in full)

This stage is blind and web-free; no WebSearch/WebFetch was used for content
verification. All content checks were made against the shards and manifest
only. No candidate or immutable file was edited; the only file written is this
report.

## Check-by-check findings

### 1. Required files present and non-empty — PASS

All five files exist in `outputs/A10_blind/attempt-1/` and are non-empty:
`SELECTION.json` (514 lines), `TOP10.json` (60 lines), `METHOD.md` (311
lines), `RUN_META.md` (72 lines), `SELF_CHECK.md` (93 lines). ROUTE.json's
required set for A10_blind (`SELECTION.json`, `TOP10.json`, `METHOD.md`) plus
the globally required `RUN_META.md` and `SELF_CHECK.md` are all covered.

### 2. SELECTION.json structure — PASS

- Exactly 24 selection objects; `selection_count: 24`. Independent counts:
  `"rank"` occurs 24 times; the nine rubric component keys occur 216 times
  total (9 x 24); `idea_id`/`concept`/`decision`/`evidence_from_candidate`/
  `uncertainty`/`principal_risk`/`falsifier` occur 168 times total (7 x 24).
- Ranks 1–24 each appear exactly once (verified by full read, sequential).
- 24 unique idea_ids: E-01, C-05, D-01, C-09, D-02, A-14, E-14, C-08, A-10,
  C-07, C-04, E-10, C-14, D-10, C-22, F-02, A-05, C-15, A-02, F-01, E-04,
  C-12, D-09, C-13 (all P3R2-prefixed, all distinct).
- Every object carries all nine score components, each with an integer 1–5
  score and a written reason, plus uncertainty, principal_risk, falsifier.
- No false precision: coarse integers only, no decimals, no weighted totals;
  `score_scale` explicitly disclaims numeric aggregation and states ranks are
  holistic ordinal judgments.

### 3. TOP10.json — PASS

Exactly 10 entries, ranks 1–10, 10 unique IDs (E-01, C-05, D-01, C-09, D-02,
A-14, E-14, C-08, A-10, C-07), identical to SELECTION.json ranks 1–10 in the
same order; all 10 contained in the 24.

### 4. METHOD.md 126/126 coverage proof — recounted, PASS

I independently extracted every `idea_id` from the three shards (regex over
the shard files) and compared against METHOD.md's coverage table:

- POOL_1.json: 42 IDs = P3R2-A-01..A-22 (22) + P3R2-B-01..B-20 (20). Matches
  the METHOD Shard-1 table row for row.
- POOL_2.json: 42 IDs = P3R2-B-21, P3R2-B-22 + P3R2-C-01..C-22 (22) +
  P3R2-D-01..D-18 (18). Matches the METHOD Shard-2 table row for row.
- POOL_3.json: 42 IDs = P3R2-D-19, P3R2-D-20 + P3R2-E-01..E-14 (14) +
  P3R2-F-01..F-23 (23) + P3R2-G-01..G-03 (3). Matches the METHOD Shard-3
  table row for row.
- Total: 126 distinct IDs, no duplicates, no gaps; each ID appears exactly
  once in the coverage table. Matches MANIFEST.json (`row_count` 126,
  `unique_id_count` 126, 42 rows per shard).
- Selected/not-selected split recounted: Shard 1 = 4 selected + 38 not;
  Shard 2 = 14 + 28; Shard 3 = 6 + 36; total 24 + 102 = 126, matching the
  candidate's own coverage-check paragraph.
- Rubric (nine components matching the stage spec), tie-handling rules,
  limitations, and an explicit "no prior rankings were read" statement are all
  present in METHOD.md.

### 5. ID preservation and selected-object spot-checks — PASS

All 126 IDs in the candidate are verbatim shard IDs. I spot-checked 10 of the
24 selected objects against the actual shard records, including 4 from TOP10
ranks 1–5:

1. **P3R2-E-01 (rank 1, POOL_3):** concept verbatim; painful_job citations
   (L02-043/044, L08-017/019/020/021, L02-010), OCP Mount Diablo / NVIDIA
   800VDC trigger, GE Vernova $2.4B/quarter (L08-033), $350k first
   experiment, v1 $3–8M, TW/JP secondaries, TRL 4, mid-2033 design-win kill
   gate, and the <10 microsecond/selectivity/false-positive falsifier all
   match the record exactly.
2. **P3R2-C-05 (rank 2, POOL_2):** concept verbatim; GB200-class spec
   conflict (L14-044), 7+ Deschutes-spec CDU vendors (L14-043), Vertiv +50% /
   $15B backlog (L14-048), T/CIEP 0263-2025 and GB 40879 (L14-039/035), $150k
   experiment, v1 $3–8M, "export separability excellent", TRL 5, and the
   blind round-robin falsifier all match.
3. **P3R2-D-01 (rank 3, POOL_2):** concept verbatim; voltage-tap failure
   citations (L03-004/018/020/021), CFS-to-Realta/WHAM (L03-035), FY2027
   milestone-program boundary (L03-032), $250k campaign, v1 $3–8M, "no
   merchant vendor ... identified in the atlas" (verbatim), TRL 3, 2033-12
   kill date, and the >=100 ms / <1% false-trigger falsifier all match.
4. **P3R2-C-09 (rank 4, POOL_2):** concept verbatim; five incompatible
   designs (L05-003/005/006/007/008), IEC 60060 gap (L05-043), +25% YoY and
   >$55M cargo orders (L05-033), EtO duopoly backlog (L05-028), CGN Dasheng
   RMB340M H1-2025 (L05-035), open-interface "OCP of pulsed power" wedge,
   $500k two-module 50kV/500A demo, v1 $6–15M, end-2033 design-in kill all
   match.
5. **P3R2-A-14 (rank 6, POOL_1):** concept verbatim; 225C ceiling, CISSOID
   last-time-buy/Honeywell exit, SUPERHOT (L15-029) and FORGE (L15-027/028),
   packaging bottleneck (L15-005, L15-025), $850k soak experiment, v1 $8–18M,
   CN chapter explicitly excluded, 500-thermal-cycle falsifier all match. The
   "$2.0B New Energy (L15-040)" figure is not in A-14's own record but appears
   verbatim in D-14 (POOL_2 line 2403) and E-09 (POOL_3 line 633) — the two
   records A-14's decision explicitly absorbs; pool-supported, not fabricated.
6. **P3R2-E-14 (rank 7, POOL_3):** concept verbatim; L08-004..007, Southern
   Spirit $2.6B + $360M DOE construction 2029 (L08-041), ~$10B HVDC backlog
   (L08-033), PRC-029-1 (L08-043), KR localization (L08-038/039), $300k
   RTDS/HIL + <1ms relay, v1 $3–8M, "owns the test everyone must pass"
   (verbatim), 2033 engagement kill gate all match.
7. **P3R2-C-08 (rank 8, POOL_2):** concept verbatim; most-cited bottleneck,
   Chaotan One 30 MW (L04-048/051) with the single-source retrofit flag
   preserved, NRC Part 53 effective 2026-04 (L04-031), $600k 1,000-cycle rig,
   v1 $15–35M, C-19 pairing, end-2033 merchant-order kill all match. The
   falsifier's ">2-5% effectiveness loss" band is a fair synthesis of the
   explicitly merged cluster's own thresholds (A-12 <5%, B-07 <5%, E-08 <2%).
8. **P3R2-E-10 (rank 12, POOL_3):** concept verbatim; 50+-year
   non-convergence (L09-001/003/006/008), missile-focused parent (L09-041),
   SEE at ~50% rated voltage (L09-014/020/103/104), AEPS $67M / NEXT-C $18.4M
   (L09-034/012), SDA EP content honestly flagged inferred (L09-039), $400k
   experiment, v1 $4–9M, JP/KR channels, 2033 flight-qual kill all match.
9. **P3R2-A-05 (rank 17, POOL_1):** concept verbatim; SAES single source
   (L07-037), 30-hour 250C bakeouts, DOE $625M QIS (L13-028), ITER-class
   tenders (L07-041..044), $250k TiZrV replication, v1 $2–6M, <=200C
   activation / 20%-of-SAES falsifier all match.
10. **P3R2-D-09 (rank 23, POOL_2):** concept verbatim; two independent
    2024-2025 groups / BCT corruption (L05-023/024), ISO 11137-1:2025
    (L05-042), A-08 sterilization-QA tier merge stated in the record itself,
    Bergoz storage-ring incumbency (L05-049), $150k side-by-side campaign, v1
    $1.5–4M, tens-of-millions ceiling all match. The falsifier's "<1-2% ...
    across three orders of dose-rate magnitude" synthesizes D-09 (<1%) and
    merged A-08 (<2%; "1,000x conventional" = three orders); pool-supported.

No fabricated or distorted pool content was found in any checked object.
Every number, source ID, named buyer, TRL, budget, capital range, and kill
gate traced either to the selected record or to a cluster member the decision
text explicitly declares as merged.

### 6. Not-selected disposition spot-checks — PASS

Checked 9 of the 102 dispositions against shard content:

1. **A-01** (DUP-MERGED, cluster rep E-01): same 800VDC rack-protection
   concept, same lane/sector; plausible and consistent with E-01's decision
   text naming A-01 as a near-duplicate.
2. **A-08** (DUP-MERGED, cluster rep D-09): D-09's own product field says
   "Merged extension (from A-08)". Accurate.
3. **B-05** (ACCESS): record's timing_window_risk says "SEVERE
   export-control/access risk" verbatim. Accurate.
4. **B-20** (WEAK-EV): record says "Weakest-thesis seed - kept as a
   discardable extra" and flags 2021-vintage data. Accurate, near-verbatim.
5. **C-18** (INCUMBENT): record says "this is the batch's highest
   commoditization risk and is included as a discardable aggressive bet";
   Vicor/Delta/Navitas named in the record. Accurate.
6. **D-11** (PHYSICS-OPT): record has `current_trl: 2`, "the 5% CE is
   modeling-only", "this is an option purchase", acqui-license exit stated.
   Accurate.
7. **F-21** (DUP-MERGED + NICHE): record says "likely folded into F-02's
   platform" and its kill date says "fold into F-02"; F-02's selection cites
   the ~$200k entry-SKU figure matching F-21's budget. Accurate.
8. **F-23** (CONTINGENT): record contains "BINDING 2029 GATE" and "the demand
   mechanism is anticipatory - developers buy only if lenders force it"
   verbatim. Accurate.
9. **G-02** (WEAK-EV): record says "Component-level pain is INFERRED ... this
   is the seed's honest gap" and prices JV copying risk. Accurate.

No disposition misdescribes its candidate in the checked sample.

### 7. No pilot labels — PASS

Case-insensitive scan of all five candidate files for `PILOT`, `pilot
sample`, and `NOT FINAL`: no pilot-sample labeling exists. All matches are
ordinary domain words ("pilot-plant", "US pilot lineage", "pilot PO") or
truthful statements that the pilot directory was not opened. The separate
`pilot/A10_blind/attempt-1/` directory exists with all five files, consistent
with the pilot-before-full route requirement.

### 8. Blind compliance as documented — PASS

RUN_META.md and METHOD.md both state: no `sources/`, no `archive/`, no
`verification/`, no prior rankings, no other stage output, no pilot content
opened, and zero web calls. SELF_CHECK.md items 10–11 agree. The declared
read list (task card, stage spec, four blind files, root policies) is
internally consistent across all three documents, and matches the stage
specification's allowed-evidence list. RUN_META's windowed-read claims check
out against reality: POOL_1 ends at line 2558, POOL_2 at 2681, POOL_3 at 2524,
and the per-shard record ranges claimed in RUN_META match my independent ID
extraction exactly. No internal contradiction found. (As an external verifier
I cannot observe the worker's actual tool calls; I verified that the
documentation is complete, specific, internally consistent, and factually
correct wherever checkable.)

### 9. Cross-file consistency — PASS

SELECTION.json ranks 1–24, METHOD.md's "Selected 24 (rank order)" list,
METHOD.md's coverage-table "SELECTED — rank N" annotations (all 24 recomputed
individually), TOP10.json's 10 rank/ID pairs, and SELF_CHECK.md's 24-ID list
agree exactly, with no divergence anywhere.

### 10. RUN_META / SELF_CHECK honesty — PASS

- Named agent `pap06-fable-xhigh`, requested `Fable 5 / xhigh`: matches the
  verification card, ROUTE.json (`fable`/`xhigh`), and MODEL_POLICY routing.
- Requested vs observed evidence kept separate: observed model is reported
  only as runtime self-identification (`claude-fable-5`) with an explicit
  caveat that this is not provider-side telemetry; observed effort and
  timestamps are `NOT_EXPOSED`, not guessed. Per MODEL_POLICY and the
  verification rules, `NOT_EXPOSED` is a missing observation, not a mismatch
  and not proof; no explicit mismatch exists.
- No invented timestamps, counts, or observations found: every checkable
  count in RUN_META and SELF_CHECK (record ranges, shard line totals, file
  inventory, 24/102/126 splits) was independently confirmed correct.
- SELF_CHECK claims map one-to-one onto verifiable artifact properties; none
  overstate.

## Defects found

None (no critical or major defects).

Minor observations (documentation nits only; explicitly not FAIL-forcing, as
they do not affect correctness and are disclosed by the candidate itself):

1. Minor — `SELECTION.json` `evidence_from_candidate` for merged selections
   (e.g., A-14's "$2.0B New Energy", C-08's "2-5% effectiveness", D-09's
   "<1-2% / three orders") draws some figures from cluster-member records
   rather than solely the headline record. Every such figure is verbatim
   pool-supported and every merge is disclosed in the object's own decision
   text and in METHOD.md; no fabrication or distortion. A stricter format
   would tag each figure's donor record inline.

## Limitations of this verification

- Spot-check based: 10 of 24 selected objects and 9 of 102 dispositions were
  verified against shard text; the remaining objects were verified
  structurally (fields, counts, IDs, cross-file consistency) but not line by
  line against records.
- Blind protocol compliance is verified from the candidate's documentation
  and its factual consistency with the repository; the worker's actual tool
  invocations are not observable to a post-hoc verifier.
- Observed model/effort for both worker and verifier rest on runtime
  self-identification and `NOT_EXPOSED` conventions per MODEL_POLICY; no
  provider-side telemetry was available.
- Source IDs quoted inside pool records (e.g., L02-043) were verified as
  faithfully quoted from the shards, not externally validated — external
  validation is forbidden in this blind, web-free stage.

VERDICT: PASS
