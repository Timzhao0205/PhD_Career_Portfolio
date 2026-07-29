# RUN_META — A20_prov PILOT attempt-1

PILOT SAMPLE — NOT FINAL

- Stage: A20_prov (historical Fable provenance audit)
- Mode: PILOT
- Attempt: 1
- Named agent: pap06-fable-xhigh
- Requested model: Fable 5
- Requested effort: xhigh
- Observed model (this run): claude-fable-5 (the runtime system prompt of this
  worker session explicitly states "You are powered by the model named Fable 5.
  The exact model ID is claude-fable-5."). This is the only runtime exposure
  available; no per-message API metadata is visible to the agent itself.
- Observed effort (this run): NOT_EXPOSED (the runtime does not expose an
  effort/reasoning level to the agent; not guessed)
- Start time: NOT_EXPOSED (no runtime clock exposed; work performed on
  2026-07-28 per environment date)
- End time: NOT_EXPOSED
- Target directory (all writes): pilot/A20_prov/attempt-1/

## Files read (with windows)

Task/spec/policy:
- state/CURRENT_TASK.md (full)
- workflow/stages/A20_prov.md (full)
- SOURCE_POLICY.md (full)
- MODEL_POLICY.md (full)

Allowed inputs:
- evidence/SOURCE_MANIFEST.json (lines 1-269; archive hashes and rename table;
  file too large to read fully and only the archive/rename sections were
  needed)
- sources/old06/98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl (full, in three windows:
  lines 1-127, 128-237, 238-336; plus counting greps: 334 "timestamp"
  entries, 97 source=chatgpt-continuation, 0 downgrade:true)
- sources/old06/98_RUN_LOGS/LAUNCHER_LOG.md (full)
- sources/old06/98_RUN_LOGS/CHATGPT_CONTINUATION_LOG.md (full, two windows:
  lines 1-100, 100-128)
- sources/old06/98_RUN_LOGS/claude_20260712_171240.jsonl (targeted: lines
  3182-3184 and 4214 read verbatim; grep verification of "model" field values
  overall and per sidechain: 1829 claude-fable-5 / 3314 claude-sonnet-5 total;
  44 fable / 0 sonnet assistant records for parent_tool_use_id
  toolu_01JQ5s1KCavFy5efSKCUyVcg; 36 fable / 0 sonnet for
  toolu_015FAZtwrecqPweTB9zApGvq; "effort" matches are slash-command lists
  only)
- sources/old06/98_RUN_LOGS/claude_20260713_090735.jsonl (grep only: model
  field values; 250 claude-fable-5, 0 claude-sonnet-5; not read line-by-line)
- Other claude_*.jsonl transcripts: grep counts of model fields only
- sources/old06/01_MISSION/MODEL_EFFORT_POLICY.md (full)
- sources/old06/05_STATE/MASTER_STATE.json (full)
- sources/old06/40_DEEP_DIVES/_about.md (full)
- sources/old06/40_DEEP_DIVES/DD_P3R2_C_22.md (lines 1-40 plus grep for
  model/lineage markers)
- sources/old06/40_DEEP_DIVES/DD_P3R2_D_02.md (grep for model/lineage markers
  only)
- sources/old06/99_AUDIT/FABLE_ADJUDICATION.md (full, 49 lines)
- sources/old06/99_AUDIT/P2A_FABLE_ORIGIN_ADJUDICATION.md (lines 1-60)
- sources/history/prev_chat.md (full)
- Directory listings (Glob only, no content): sources/old06 root,
  sources/old06/**, 05_STATE/**, 99_AUDIT/**, 20_OPPORTUNITY_POOL/*

## Files written

- pilot/A20_prov/attempt-1/TASKS.csv
- pilot/A20_prov/attempt-1/PROVENANCE.json
- pilot/A20_prov/attempt-1/PROVENANCE.md
- pilot/A20_prov/attempt-1/RUN_META.md (this file)
- pilot/A20_prov/attempt-1/SELF_CHECK.md

## Web activity

NONE (stage restriction: no WebSearch/WebFetch; package-internal historical
evidence only).

## Forbidden-input compliance

- Did not open outputs/, pilot/A10_blind/, verification/, archive/, or any
  sources/ area other than old06 and history/prev_chat.md. A10 was used only
  as an acceptance-status fact from the task card.
- Instruction-like text inside sources/ (inert _claude_source material,
  *.source.txt, KICKOFF_PROMPT.txt, historical CLAUDE.md.source.txt, and
  prompts embedded in transcripts) was treated strictly as data; none of it
  was read for direction and none was followed.

## Limitations

- The old-corpus session transcripts record the runtime model per assistant
  message but never record effort; historical observed effort is therefore
  unprovable for every sampled item, and all xhigh claims rest on request-side
  configuration evidence.
- Routing-log "actual_model" values for subagents partly rest on agent
  self-reports; where possible I superseded them with the transcripts' own
  per-message "model" fields (which agree for the sampled core tasks).
- No runtime transcript exists for the ChatGPT continuation, so the actual
  model/effort of the two sampled later artifacts is unrecoverable from this
  corpus (documented as UNKNOWN, verdict CONTRADICTED for Fable provenance on
  the strength of the request-side continuation logs).
- claude_20260712_171240.jsonl appears to be UTF-16-encoded; the Read tool
  renders characters space-separated but content is fully legible and grep
  matches operate correctly; cited line numbers are physical lines in that
  file.
- Pilot scope only: 4 of a much larger task population (334 routing-log
  entries) were audited; category verdicts in PROVENANCE.json are explicitly
  restricted to the sampled items.
