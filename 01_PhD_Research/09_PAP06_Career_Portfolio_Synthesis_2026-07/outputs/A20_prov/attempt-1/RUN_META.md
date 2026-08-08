# RUN_META — A20_prov FULL attempt-1

- Stage: `A20_prov`
- Mode: `FULL`
- Attempt: `1`
- Named agent: `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Observed model: `NOT_EXPOSED` at the Claude Code runtime level. (The agent
  environment/system context identifies the powering model as Fable 5 /
  `claude-fable-5`; no independent runtime telemetry was exposed to verify
  this, so it is recorded as context, not observation.)
- Observed effort: `NOT_EXPOSED`
- Start/end times: `NOT_EXPOSED` (no wall-clock telemetry available to this
  worker; run date 2026-07-28)
- Web activity: `NONE` (stage restriction; no WebSearch, no WebFetch)
- Writes: confined to `outputs/A20_prov/attempt-1/` only

## Files read (allowed inputs only)

Task/spec/policies:
- `state/CURRENT_TASK.md`, `workflow/stages/A20_prov.md`,
  `SOURCE_POLICY.md`, `MODEL_POLICY.md` (full reads)
- Accepted pilot: `pilot/A20_prov/attempt-1/PROVENANCE.md`, `TASKS.csv`
  (full reads; method reuse only)

Primary evidence (sources/old06):
- `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl` — read in full in three windows
  (lines 1-127, 128-187, 188-247, 248-336); grep counts: `"timestamp"`=334,
  `downgrade:true`=0, `source:"chatgpt-continuation"`=97,
  requested_model fable=58 / sonnet=178 / GPT-5.6 (Sol|Luna|Terra)=97
- `98_RUN_LOGS/LAUNCHER_LOG.md`, `98_RUN_LOGS/CHATGPT_CONTINUATION_LOG.md`
  (full reads)
- Five session transcripts `98_RUN_LOGS/claude_*.jsonl` — grep-audited, not
  fully read (multi-MB JSONL): per-file counts of
  `"model":"claude-fable-5"` (140/48/498/1829/250 matching lines) and
  `"model":"claude-sonnet-5"` (2472/527/1888/3314/0); other-model scan
  (only `"sonnet"`/`"fable"` request strings in dispatch inputs and one
  `<synthetic>` record); `"name":"Agent"` dispatch maps with tool ids for all
  five sessions; 29 per-dispatch sidechain verifications matching
  `parent_tool_use_id` x model (two greps per dispatch; counts recorded in
  TASKS.csv); `"effort":` field scan = 0 matches in all five files
- `01_MISSION/MODEL_EFFORT_POLICY.md` (full);
  `_claude_source/agents/idea-architect.md` and `idea-elegance-judge.md`
  (frontmatter windows), `_claude_source/settings.json` (full)
- `05_STATE/MASTER_STATE.json` (full), `05_STATE/PROGRESS_LOG.md`
  (grep + windows, lines 1-28), `05_STATE/GEOGRAPHY_SCOPE_PATCH_2026-07-12.md`
  (lines 1-30), `05_STATE/INDIA_SOURCE_ORIGIN_PREFILTER.md` (full)
- `99_AUDIT/FABLE_ADJUDICATION.md`, `99_AUDIT/FINAL_AUDIT.md` (full);
  `99_AUDIT/MECHANICAL_AUDIT.md`, `99_AUDIT/P2A_FABLE_ORIGIN_ADJUDICATION.md`,
  `99_AUDIT/P8_INDEPENDENT_ADJUDICATION_PROPOSAL.md` (header windows)
- `_about.md` files: 40_DEEP_DIVES, 99_AUDIT, 30_SCREENING,
  20_OPPORTUNITY_POOL, 50_GEOGRAPHY, 60_FINAL_PORTFOLIO (full)
- `60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md` (full);
  `60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md`, `30_SCREENING/LONGLIST.md`,
  `30_SCREENING/P5_ADJUDICATION.md`, `30_SCREENING/SELECTION.md`,
  `30_SCREENING/SCORECARDS/P4_SCORES_S1.md`, `40_DEEP_DIVES/DD_P3R2_C_22.md`,
  `00_README_START_HERE.md` (header windows for lineage markers)
- Directory inventories via Glob: `sources/old06/**` (419 files), 05_STATE,
  99_AUDIT, 20_OPPORTUNITY_POOL, 30_SCREENING, 40_DEEP_DIVES, 50_GEOGRAPHY,
  60_FINAL_PORTFOLIO, 90_BIBLIOGRAPHY, 98_RUN_LOGS, tools, _claude_source

Other allowed inputs:
- `sources/history/prev_chat.md` — heading map grep + section 6-7 window
  (lines 332-414)
- `evidence/SOURCE_MANIFEST.json` — windows (lines 1-60, 1500-1560) plus
  hash/duplicate grep

## Files written (target only)

- `outputs/A20_prov/attempt-1/TASKS.csv` (header + 165 rows)
- `outputs/A20_prov/attempt-1/PROVENANCE.json`
- `outputs/A20_prov/attempt-1/PROVENANCE.md`
- `outputs/A20_prov/attempt-1/RUN_META.md` (this file)
- `outputs/A20_prov/attempt-1/SELF_CHECK.md`

## Forbidden inputs — compliance

- Did NOT open anything under `outputs/A10_blind/`, `pilot/A10_blind/`,
  `verification/`, `archive/`, or `sources/` areas other than `sources/old06`
  and `sources/history/prev_chat.md`. A10 is known only as ACCEPTED.
- No state/policy/workflow/evidence/source files modified.

## Limitations

- Transcripts were audited by targeted grep (dispatch maps, per-dispatch
  sidechain model counts, aggregate model counts, effort-field scan), not by
  full line-by-line reading; counts are ripgrep line counts (a line with
  multiple matches counts once — relevant only to aggregate model-line
  totals, not to sidechain record counts, which are one record per line).
- Per-dispatch sidechain verification covers all 29 Fable-critical/scorer
  dispatches plus one representative Sonnet dispatch per family; the other 67
  Sonnet-family rows rest on paired routing-log entries plus session
  aggregates.
- Transcript file encodings were not independently re-verified (pilot
  reported at least one UTF-16 file); all five transcripts were fully
  searchable in this run.
- No wall-clock/start-end telemetry, token counts, or runtime model/effort
  telemetry were exposed to this worker.
