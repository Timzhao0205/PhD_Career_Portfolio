# PILOT SAMPLE — NOT FINAL

A20_prov PILOT, attempt 1. Historical Fable provenance audit of the old
Folder 06 corpus, restricted to a deterministic four-item sample: two clearly
logged core idea-generation/adjudication tasks and two later Folder 06
artifacts. Historical provenance and fresh agreement are separate questions;
this document judges only historical provenance.

## Sampling rule (stated so the full run can extend it)

1. Core tasks. In `sources/old06/98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`,
   restrict to tasks with `requested_model=claude-fable-5`, a matched
   `started`+`complete` entry pair, surviving output artifacts in the corpus,
   and a locatable Agent dispatch plus subagent sidechain in a Claude Code
   session transcript. Take, in file order, the first idea-architect
   (idea-generation) dispatch of the P3R2 regeneration round — `P3R2-A`
   (log line 173) — and the first idea-elegance-judge (adjudication)
   dispatch — `P3R2-ELEGANCE-JUDGE` (log line 183). The P3R2 round was chosen
   because it produced the frozen longlist; the superseded P3 round-1 seed
   batches remain in scope for the full run.
2. Later artifacts. Among the ten P6 deep-dive tasks in the same log, take the
   first two `complete` entries in file order — `DD_P3R2_C_22.md` (line 311)
   and `DD_P3R2_D_02.md` (line 313) — and audit those files in
   `sources/old06/40_DEEP_DIVES/`.

## What is provable for the sampled items

### Core tasks: model YES (runtime logs), effort NO (request only)

The Claude Code session transcript
`sources/old06/98_RUN_LOGS/claude_20260712_171240.jsonl` is genuine runtime
evidence: every assistant message records a `"model"` field.

- `P3R2-A` (idea generation): the orchestrator dispatch (transcript line 3184,
  `subagent_type":"idea-architect"`, tool id `toolu_01JQ5s1KCavFy5efSKCUyVcg`)
  was emitted by a `claude-fable-5` message, and all 44 sidechain assistant
  records belonging to that subagent (matched on `parent_tool_use_id`) record
  `"model":"claude-fable-5"`; zero record `claude-sonnet-5`. The routing log
  (lines 173/177) independently records started/complete with
  `actual_model=claude-fable-5` and completion note "22 US seeds ... agent
  self-reported fable-5/xhigh". Output artifacts
  `20_OPPORTUNITY_POOL/P3R2_A_us_pain.json/.md` exist.
- `P3R2-ELEGANCE-JUDGE` (adjudication of all 100 P3R2 seeds): dispatch at
  transcript line 4214 (`idea-elegance-judge`, tool id
  `toolu_015FAZtwrecqPweTB9zApGvq`); all 36 sidechain assistant records are
  `claude-fable-5`, zero sonnet. Routing log lines 183/184 match. Output
  artifacts `20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION.md/.json` exist.

Effort is different. No runtime record anywhere in the transcripts carries an
effort field (the only "effort" strings are slash-command name lists in
session metadata). xhigh is evidenced solely as a request: launcher
configuration (`98_RUN_LOGS/LAUNCHER_LOG.md`: "Critical: claude-fable-5 /
xhigh"), agent frontmatter (`effort=xhigh` quoted in routing entries), and
`01_MISSION/MODEL_EFFORT_POLICY.md`. A request proves intent, not execution.

Verdict for both sampled core tasks: **PARTIAL_PROVENANCE** — Fable 5 as the
runtime model is strongly evidenced; high/xhigh effort is requested-only and
was never runtime-observed.

### Later artifacts: Fable provenance CONTRADICTED

Both sampled deep dives were generated on 2026-07-14 during the documented
ChatGPT continuation, not in a Claude session:

- `MODEL_ROUTING_LOG.jsonl` lines 308-313 (`source":"chatgpt-continuation`)
  record both tasks with `requested_model":"GPT-5.6 Terra"` and
  `actual_model":"unknown"`.
- `98_RUN_LOGS/CHATGPT_CONTINUATION_LOG.md` states the runtime "does not
  expose an exact ChatGPT model/effort identifier" and narrates P6 completion.
- No runtime transcript of the continuation exists in the corpus, and the
  artifacts themselves carry no model lineage marker.

The strongest contemporaneous evidence therefore affirmatively places
generation on a requested non-Claude route. Verdict for both sampled later
artifacts: **CONTRADICTED** (with respect to the claim of Fable 5 high/xhigh
generation). The exact GPT model/effort that ran is UNKNOWN, but unknown
identity within a ChatGPT continuation does not restore Fable provenance.

## Contradictions found and reconciled

- `40_DEEP_DIVES/_about.md` claims "Ten Fable/xhigh reports". This conflicts
  with the routing log and continuation log and has no supporting runtime
  evidence; it is rejected as an unsupported folder note.
- `99_AUDIT/FABLE_ADJUDICATION.md` (final P8 sign-off titled "Fable
  adjudication") itself honestly records "Actual runtime model / effort:
  unknown / unknown (not exposed; not inferred)" — consistent with the
  continuation logs, and a warning that "Fable" in later artifact titles is a
  role label, not runtime proof.
- `sources/history/prev_chat.md` (section 7) corroborates the same split as
  secondhand narrative (Fable evidence for seeds/P3R2/adjudications; later
  ChatGPT continuation did not expose model/effort). Used as corroboration
  only.

## What is NOT provable for the sampled items

- Runtime effort for any sampled item (no runtime effort records exist).
- The exact runtime model of the two sampled later artifacts (continuation
  logged `unknown`).
- Routing-log completion notes such as "agent self-reported fable-5/xhigh"
  are agent self-reports relayed by the orchestrator; the independent
  transcript `"model"` fields are the stronger evidence and agree on the
  model.

## What the full run must cover

- All 334 timestamped entries of `MODEL_ROUTING_LOG.jsonl` (97 are
  chatgpt-continuation entries; 0 record `downgrade=true`), producing one
  TASKS.csv row per identifiable idea-generation/adjudication/screening/
  repair/deep-dive/synthesis task: P3 round-1 seed batches A-D and W, P3R2
  waves A-G, elegance-judge rounds R1-R3, fixers 1-3, founder-fit, P2A
  batches and Fable adjudication, P1 scout/verify waves, P4 groups and
  scorers S1-S4 (noting the interrupted Claude scorer attempts and the
  ChatGPT S2/S4 regeneration), and every P5/P6/P7/P8 continuation task.
- Sidechain model verification in all five `claude_*.jsonl` session
  transcripts, plus `LAUNCHER_LOG.md`, `CHATGPT_CONTINUATION_LOG.md`,
  `CHATGPT_HANDOFF_BACKUP_20260713_220541/`, `05_STATE/` state files
  (MASTER_STATE.json, PROGRESS_LOG.md), `99_AUDIT/` statements, and artifact
  lineage markers, reconciling every contradiction of the `_about.md` type.
- Attachment hashes/duplicate facts in `evidence/SOURCE_MANIFEST.json` where
  lineage depends on which archive supplied a file.
