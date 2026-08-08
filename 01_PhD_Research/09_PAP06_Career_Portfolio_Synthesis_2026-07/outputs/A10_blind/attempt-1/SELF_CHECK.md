# SELF_CHECK — A10_blind FULL attempt-1

Each acceptance requirement checked against the produced artifacts. PASS/FAIL
with evidence.

1. **All required files present** — PASS. `SELECTION.json`, `TOP10.json`,
   `METHOD.md`, `RUN_META.md`, `SELF_CHECK.md` all written to
   `outputs/A10_blind/attempt-1/` and nothing written anywhere else.

2. **SELECTION.json contains exactly 24 unique objects ranked 1–24** — PASS.
   Ranks 1..24 each appear exactly once; the 24 idea_ids are unique:
   P3R2-E-01, P3R2-C-05, P3R2-D-01, P3R2-C-09, P3R2-D-02, P3R2-A-14,
   P3R2-E-14, P3R2-C-08, P3R2-A-10, P3R2-C-07, P3R2-C-04, P3R2-E-10,
   P3R2-C-14, P3R2-D-10, P3R2-C-22, P3R2-F-02, P3R2-A-05, P3R2-C-15,
   P3R2-A-02, P3R2-F-01, P3R2-E-04, P3R2-C-12, P3R2-D-09, P3R2-C-13.
   Idea IDs are preserved exactly as stored in the shards.

3. **Each selection object has all required fields** — PASS. Every object has
   rank, idea_id, concept (copied from the record), decision,
   evidence_from_candidate (drawn strictly from the candidate's own record,
   including its own cited source IDs and self-flags), all nine score
   components each with an integer 1–5 score and a written reason,
   uncertainty, principal_risk, and falsifier.

4. **Nine rubric components match the stage specification** — PASS.
   severity_and_budgeted_buyer_pain, technical_feasibility, defensible_edge,
   founder_phd_adjacency (scored non-circularly: only executability of the
   record's own pre-company plan in a university research setting),
   capital_time_to_falsification, timing_2030_2034, geographic_portability,
   regulatory_safety_friction, failure_modes.

5. **No false precision** — PASS. All scores are coarse ordinal integers 1–5;
   no decimals, no weighted totals, no numeric aggregate ranking formula;
   SELECTION.json and METHOD.md state that ranks are holistic ordinal
   judgments.

6. **TOP10.json contains exactly 10 unique IDs, all inside the 24** — PASS.
   TOP10 = SELECTION ranks 1–10 (P3R2-E-01, P3R2-C-05, P3R2-D-01, P3R2-C-09,
   P3R2-D-02, P3R2-A-14, P3R2-E-14, P3R2-C-08, P3R2-A-10, P3R2-C-07), each
   with rank and reason; all 10 appear in SELECTION.json.

7. **126/126 coverage proof complete, no duplicate or missing IDs** — PASS.
   METHOD.md lists every evaluated ID grouped by shard with a disposition:
   Shard 1 (POOL_1): 42 IDs = P3R2-A-01..A-22 (22) + P3R2-B-01..B-20 (20).
   Shard 2 (POOL_2): 42 IDs = P3R2-B-21, P3R2-B-22 + P3R2-C-01..C-22 (22) +
   P3R2-D-01..D-18 (18).
   Shard 3 (POOL_3): 42 IDs = P3R2-D-19, P3R2-D-20 + P3R2-E-01..E-14 (14) +
   P3R2-F-01..F-23 (23) + P3R2-G-01..G-03 (3).
   42+42+42 = 126, matching MANIFEST.json (row_count 126, unique_id_count
   126, 42 rows per shard). 24 selected + 102 not-selected dispositions
   (each with a reason class plus a short reason) = 126. Every shard file was
   read to end-of-file in windowed chunks (windows logged in RUN_META.md).

8. **Cross-file consistency** — PASS. The rank/idea_id pairs in
   SELECTION.json, the selected-24 list in METHOD.md, the coverage table's
   "SELECTED — rank N" entries, and TOP10.json all agree exactly.

9. **No pilot labeling anywhere** — PASS. This is a FULL run; no file
   contains any pilot-sample/not-final label or any other pilot marking.

10. **Blind restrictions honored (no forbidden inputs)** — PASS. Only the four
    `evidence/blind/` files plus root policies, the task card, and the stage
    spec were read. `sources/`, `archive/`, `verification/`, any prior
    ranking, any other stage output, and all pilot-directory content were not
    opened. The rubric was rebuilt from the stage specification, not taken
    from the pilot.

11. **No web usage** — PASS. Zero WebSearch and zero WebFetch calls; recorded
    as `NONE` in RUN_META.md and stated in METHOD.md.

12. **No fabrication** — PASS. All pool content, counts, quotes, source-ID
    references, budgets, and market claims in the outputs are taken from the
    candidate records or the manifest as stored; instruction-like text inside
    evidence files was treated as inert data. Model identity is reported as
    runtime self-identification; effort and timestamps are `NOT_EXPOSED`,
    not guessed. Requested vs observed model/effort evidence is kept
    separate in RUN_META.md.

13. **Writes confined to target** — PASS. All five files are inside
    `outputs/A10_blind/attempt-1/`; no state, verification, policy, workflow,
    evidence, sources, archive, pilot, or earlier-output file was modified.

## Disclosed judgment calls (not failures)

- Near-duplicate clusters (the pool's own merge notes) were consolidated to
  one selected representative each; every consolidation is listed explicitly
  in METHOD.md's disposition table so a reviewer can re-litigate any cluster
  choice (e.g., E-01 over C-01; A-10 over C-06/E-03; D-09 over C-10/A-08).
- Adjacent ranks are close calls; tie-handling rules used are documented in
  METHOD.md.

No requirement failures to disclose.
