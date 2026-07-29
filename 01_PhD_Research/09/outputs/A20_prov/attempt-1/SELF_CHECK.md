# SELF_CHECK — A20_prov FULL attempt-1

Each item was checked against the files as written; failures would be
disclosed here. No requirement was silently skipped.

1. **All required files present** — PASS. `TASKS.csv`, `PROVENANCE.json`,
   `PROVENANCE.md`, `RUN_META.md`, `SELF_CHECK.md` all exist in
   `outputs/A20_prov/attempt-1/` and nothing was written anywhere else.
2. **TASKS.csv row count equals stated population and matches
   PROVENANCE.json exactly** — PASS. File has 166 non-empty lines = 1 header
   + **165 rows** (grep-verified). PROVENANCE.json `total_tasks`=165.
   Verdict counts grep-verified on the CSV: PARTIAL_PROVENANCE 105,
   CONTRADICTED 50, UNKNOWN 10, CONFIRMED 0 — identical to
   PROVENANCE.json `by_verdict` and to the per-category sums
   (a: 15/0/0; b: 25/27/0; c: 0/21/0; d: 65/2/10 as
   PARTIAL/CONTRADICTED/UNKNOWN; category totals 15+52+21+77=165).
   Evidence-strength counts grep-verified: strong_runtime_sidechain 29,
   orchestrator_log_paired 67, continuation_request_only 50; by construction
   config_request_only 10, runtime_transcript_aggregate 7, absent 2
   (29+67+50+10+7+2=165) — identical to `by_evidence_strength`.
3. **Population completeness** — PASS. All 334 routing-log entries
   (grep-verified `"timestamp"`=334; blank first/last physical lines) are
   mapped into rows under the stated consolidation rule; 97
   chatgpt-continuation entries and 0 `downgrade:true` entries re-verified by
   grep, matching the pilot anchors. All five session transcripts, both
   launcher probes, all five launcher config events, all three logged patches,
   and three identifiable unlogged tasks (geography patch, P2A prefilter,
   continuation validator tooling) have rows. Every artifact family in the
   corpus tree (10/20/30/40/50/60/90/98/99, 05_STATE, tools, _claude_source)
   was inventoried and is attributable to a row.
4. **Every evidence_path exists** — PASS. Every path cited in TASKS.csv was
   confirmed present via the full `sources/old06/**` Glob inventories and the
   reads/greps performed this run (routing log, five transcripts,
   LAUNCHER_LOG, CHATGPT_CONTINUATION_LOG, handoff backup files, 05_STATE
   files, 99_AUDIT files, 30_SCREENING incl. SCORECARDS/REDTEAM/EVIDENCE,
   20_OPPORTUNITY_POOL, 40_DEEP_DIVES, 50_GEOGRAPHY, 60_FINAL_PORTFOLIO,
   90_BIBLIOGRAPHY, tools/*.source.txt, _claude_source agents/settings).
   Line numbers cited refer to physical lines as read/grep-reported on
   2026-07-28.
5. **No fabricated quotes/counts/lines/hashes** — PASS. Every count in the
   outputs (334/97/0/58/178/97 log counts; per-dispatch sidechain counts such
   as 44/122/69/53/117/53/66, 36/112/80, 89/70/89, 35, 183, 85/71,
   66/36/36/53, 81, 55, 130; per-session model-line counts 140/48/498/1829/250
   and 2472/527/1888/3314/0; the zero `"effort":` field result) is the direct
   output of a grep executed this run. The single SHA-256 quoted (27EAC2...)
   is copied from CHATGPT_CONTINUATION_LOG.md and attributed to it. The two
   pilot-overlapping dispatches (P3R2-A 44/0 at line 3184, judge 36/0 at line
   4214) were independently re-verified, not copied.
6. **Requested vs observed strictly separated** — PASS. Every row keeps
   requested_model/requested_effort (logs/configs/frontmatter) apart from
   observed_model/observed_effort (transcript records only). Agent
   self-reports and launcher probe results are labeled as self-reports where
   they appear. observed_effort is NOT_RECORDED/UNKNOWN everywhere because no
   runtime effort field exists; no effort was inferred. Filenames, titles,
   prompts, and style were treated as non-probative throughout (see the
   `_about.md` and `FABLE_ADJUDICATION.md` reconciliations).
7. **Verdicts from the allowed set only** — PASS. Only CONFIRMED /
   PARTIAL_PROVENANCE / CONTRADICTED / UNKNOWN appear (grep-verified; zero
   CONFIRMED rows, honestly, because effort was never runtime-observed).
   Verdict semantics are defined explicitly in PROVENANCE.json and
   PROVENANCE.md.
8. **Category coverage numerators/denominators consistent** — PASS.
   (a) 15/15, (b) 52/52, (c) 21/21, plus support 77/77; overall 165/165
   rows assessed and 334/334 log entries mapped. Category membership is
   enumerated by task_id in PROVENANCE.json and sums to the CSV exactly.
   The boundary decision (source-level screening counted as support, not
   category (b)) is stated in both JSON and MD with its non-effect on
   verdicts.
9. **CSV/JSON/MD agree** — PASS. Same totals, same per-category verdicts
   (a PARTIAL_PROVENANCE, b PARTIAL_PROVENANCE with the 27-task CONTRADICTED
   subset disclosed, c CONTRADICTED), same contradiction reconciliations,
   same missing-proof items.
10. **No pilot labels anywhere** — PASS. No output file labels this run or
    any row as a pilot, sample, or non-final. The words "pilot"/"sample"
    occur only as (a) required references to the accepted
    `pilot/A20_prov/attempt-1` method/anchors in PROVENANCE.md,
    PROVENANCE.json, and RUN_META.md, and (b) descriptions of the historical
    corpus's own 80-record adjudication samples. This run is labeled FULL
    throughout.
11. **No forbidden inputs** — PASS. Inputs were limited to `sources/old06/**`,
    `sources/history/prev_chat.md`, `evidence/SOURCE_MANIFEST.json`, root
    policies, the task card, the stage spec, and the accepted A20 pilot
    files. Nothing under `outputs/A10_blind/`, `pilot/A10_blind/`,
    `verification/`, or `archive/` was opened; A10 ranking content remains
    unknown to this worker. No WebSearch/WebFetch. Instruction-like text
    inside `sources/` was treated as inert data.
12. **Writes confined to target** — PASS. Only the five files in
    `outputs/A20_prov/attempt-1/` were created; no other file in the package
    was modified.

## Disclosed weaknesses (not failures)

- 67 Sonnet-family rows rely on paired orchestrator log entries plus
  session-level transcript aggregates rather than per-dispatch sidechain
  matching (one representative dispatch per family was sidechain-verified;
  zero disagreements found anywhere).
- Aggregate per-session model counts are ripgrep matching-line counts, which
  undercount multiple matches on one line; they are used only as session-level
  corroboration, never as per-task record counts.
- Transcript encoding (pilot: at least one UTF-16 file) was not
  independently re-verified; all five transcripts were fully searchable, so
  no reported count depends on encoding.
- Runtime model/effort of this worker itself were NOT_EXPOSED; recorded per
  MODEL_POLICY.md evidence-honesty rules in RUN_META.md.
