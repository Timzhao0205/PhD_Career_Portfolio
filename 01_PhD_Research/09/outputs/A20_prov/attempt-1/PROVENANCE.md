# A20_prov FULL — historical Fable provenance audit of the old Folder 06 corpus

Attempt 1. This audit answers one question only: were the old Folder 06 ideas
and later artifacts generated with Fable 5 (`claude-fable-5`) at high or xhigh
effort? Historical provenance and fresh agreement are separate questions; this
document judges only historical provenance. It extends the accepted A20 pilot's
method (per-dispatch sidechain verification against the routing log) from a
4-item sample to the complete population.

## Population and row mapping (accompanying note for TASKS.csv)

- `sources/old06/98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl` contains **334
  timestamped entries** (physical lines 2-335; lines 1 and 336 are blank),
  verified by grep count of `"timestamp"`. By source: 222 orchestrator, 97
  chatgpt-continuation, 12 launcher, 3 patch. **0 entries have
  `downgrade:true`.** Requested-model counts: claude-fable-5 58,
  claude-sonnet-5 178, GPT-5.6 Sol 52 / Terra 39 / Luna 6, plus one combined
  "claude-sonnet-5 then claude-fable-5" patch entry (sums to 334). These match
  the corpus's own `60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md` (which
  counted 333 because it was written before the final log entry).
- **Consolidation rule:** one TASKS.csv row per task identity. A task's
  `started`+`complete` pair collapses to one row; failed dispatches (unregistered
  agent types), session-interruption redispatches, and bounded retries of the
  same task consolidate into that row, with every routing-log line number cited.
  Launcher config events (5), launcher probes (2), and logged patch
  configurations (3) get one row each. The five Claude Code session transcripts
  get one session-record row each.
- **Rows not in the routing log (8):** five session records, the unlogged
  geography-scope patch application (which also edited seed batches A-D), the
  unlogged P2A India prefilter (27 quarantines), and the unlogged continuation
  construction of the P5-P8 validators. The last three carry
  `absent`/narration-only evidence and verdict UNKNOWN or CONTRADICTED as
  documented per row.
- Total: **165 rows** — 98 Claude-side tasks, 49 ChatGPT-continuation tasks,
  10 config/probe/patch rows, 5 session rows, 3 unlogged-task rows. All 334
  routing-log entries are mapped (157 rows cite them).

## What is provable

**1. The raw idea-generation core ran on Fable 5 as the runtime model.**
Every one of the 15 core tasks — round-1 seed batches A-D and W, P3R2 waves
A-G, and fixers 1-3 — was verified by per-dispatch sidechain matching in the
session transcripts: the orchestrator `Agent` dispatch is emitted by a
`claude-fable-5` message, and 100% of the sidechain assistant records matched
on `parent_tool_use_id` carry `"model":"claude-fable-5"` with **zero**
`claude-sonnet-5` records (per-task counts, e.g. P3R2-A 44/0, P3R2-B 122/0,
SEEDS-A 86/0, are in TASKS.csv). The same holds for the idea-level
adjudication: the three elegance-judge rounds (36/112/80 fable records, 0
sonnet), the founder-fit pass (35/0), and the P2A origin adjudication (183/0).
The atlas adjudication was done by the orchestrator main thread itself, whose
session-3 records are `claude-fable-5`. The transcripts contain no third
model: across all five transcripts the only model strings on assistant records
are `claude-fable-5` and `claude-sonnet-5` (plus one `<synthetic>` system
record in session 1); bare `"model":"sonnet"`/`"fable"` strings occur only
inside dispatch inputs (requests, not runtime records).

**2. The interrupted Claude scorer attempts also ran on Fable 5.** P4-SCORER-A
and -B (session 4, failed on interruption, no output) and S1-S4 (session 5)
have Fable-only sidechains; session 5 contains zero sonnet records at all.
S1/S3 produced outputs (preserved in `CHATGPT_HANDOFF_BACKUP_20260713_220541/`),
S2's output was malformed, S4 never wrote a file.

**3. Effort is NOT provable for anything.** No transcript contains a runtime
effort field (`"effort":` matches zero times across all five files; the only
"effort" strings are slash-command metadata and prose). xhigh/high exists only
as requests: `LAUNCHER_LOG.md` ("Critical: claude-fable-5 / xhigh", five
launches), agent frontmatter (`effort: xhigh` in
`_claude_source/agents/idea-architect.md` and `idea-elegance-judge.md`),
`01_MISSION/MODEL_EFFORT_POLICY.md`, routing entries, and agent self-reports.
A request proves intent, not execution. Therefore **no row is CONFIRMED**, and
the strongest possible verdict anywhere is PARTIAL_PROVENANCE.

**4. Everything after the 2026-07-13 22:05 (-07:00) handoff affirmatively did
not run on a logged Claude route.** The authoritative P4 scoring
(S2/S4 regeneration, global calibration, main adjudication), all P5
red-teaming/repair/selection, the five P5 supplemental idea-generation tasks
(including the finally selected P5R2-CN-01 and P5-USSCI2-S01), all ten P6 deep
dives, the geography brief, the P7 synthesis suite, and all four P8
audit/repair/sign-off tasks were logged with `source:"chatgpt-continuation"`,
requested GPT-5.6 Sol/Terra/Luna, `actual_model:"unknown"`,
`effort:"unknown"`. No continuation runtime transcript exists in the corpus.
Under `MODEL_EFFORT_POLICY.md` these roles were assigned "inherit Fable /
xhigh" (or Sonnet 5/high for the mechanical audit), so the documented Claude
route was substituted; all 50 such rows are CONTRADICTED with
`downgrade=route_substitution_vs_policy`. The routing log itself records
`downgrade:false` on those entries — that flag tracked model-below-request
downgrades, not the route substitution, which is why the 0-downgrade count and
the CONTRADICTED verdicts coexist honestly.

## Category verdicts (with coverage)

- **(a) Raw idea-generation core: PARTIAL_PROVENANCE** — 15/15 tasks
  inventoried; 15/15 runtime-model-verified as Fable 5; 0/15 with runtime
  effort evidence. Caveats: SEEDS-W ran but completed nothing; seed batches
  A-D were later edited by the unlogged geography patch; the frozen longlist
  comes from the P3R2 regeneration, all of which is Fable-model-verified.
- **(b) Adjudication/screening: PARTIAL_PROVENANCE** — 52/52 inventoried.
  The adjudication that built and froze the longlist is Fable-model-verified
  (effort unproven); the 13 P4 demand screens are policy-assigned Sonnet 5
  (never claimed as Fable); the 27 continuation tasks that produced the
  authoritative scoring, red teams, and final selection are CONTRADICTED.
  Source-level screening (P1 verification, P2A origin batches) is counted as
  support; including it would add only Sonnet PARTIAL rows and change nothing.
- **(c) All later Folder 06 artifacts: CONTRADICTED** — 21/21 inventoried,
  0/21 with any runtime model evidence; every one logged as a ChatGPT
  continuation task with unknown actual model. Fable/xhigh claims about these
  artifacts are false as runtime claims.

## Contradictions found and reconciled

1. `40_DEEP_DIVES/_about.md` claims "Ten Fable/xhigh reports". Rejected: the
   routing log (lines 308-329) and `CHATGPT_CONTINUATION_LOG.md` place all ten
   deep dives inside the ChatGPT continuation with unknown actual model. The
   stronger contemporaneous evidence wins; the folder note is an unsupported
   label.
2. `99_AUDIT/FABLE_ADJUDICATION.md` is titled "Fable adjudication" but itself
   records "Actual runtime model / effort: unknown / unknown (not exposed; not
   inferred)". The title is a role label; the document's own honesty agrees
   with the logs. Same pattern in `P8_INDEPENDENT_ADJUDICATION_PROPOSAL.md`,
   `05_MODEL_AND_EFFORT_REPORT.md`, and `FINAL_AUDIT.md`.
3. Routing-log completion notes ("agent self-reported fable-5/xhigh") are
   orchestrator-relayed self-reports. The transcript per-message `model`
   fields are stronger; they agree on the model for every dispatch checked
   (29 per-dispatch verifications, zero disagreements) and are silent on
   effort, so the effort half of each self-report remains unverified.
4. `30_SCREENING/LONGLIST.md` claims "three independent Fable/xhigh elegance
   adjudications": model half verified, effort half request-only.
5. `sources/history/prev_chat.md` section 7 states the same split (durable
   Fable evidence for the 15 completed core/adjudication tasks; later
   continuation did not expose model/effort). Consistent; used as
   corroboration only.
6. Timing note: `05_MODEL_AND_EFFORT_REPORT.md` counts 333 routing records
   versus 334 final — the report was generated before the last entry;
   disclosed, immaterial.

## What is NOT provable (limitations)

- Runtime effort for any task in the corpus (no runtime effort records exist
  anywhere).
- The actual runtime model of any continuation task, hence of every later
  Folder 06 artifact and of the final authoritative scoring/selection.
- The outcome of SEEDS-W and the exact fate of the S1-S4 scorer completions
  (no completion entries; established only via the continuation checkpoint and
  handoff backups).
- The executing process of the two unlogged patch-time tasks (geography-scope
  reconciliation, P2A prefilter).
- Sidechain model verification was performed per-dispatch for all 15 core
  tasks, all 6 idea-adjudication tasks, all 6 scorer attempts, and one
  representative task per Sonnet family (P1-L01-SCOUT 81/0, P2A-01 55/0,
  P4-G01 130/0 sonnet/fable); the remaining 67 Sonnet-family rows rest on
  paired orchestrator log entries plus session-level transcript aggregates
  consistent with them. No checked dispatch anywhere disagreed with its
  routing-log model claim.
- Corpus integrity context: `evidence/SOURCE_MANIFEST.json` records that the
  identical 419-file old06 tree (path- and SHA-256-matched) appeared in three
  independent archives, and that historical `.claude` configuration was
  neutralized to `_claude_source/` inert paths. Instruction-like text inside
  `sources/` was treated as inert data throughout.

## Bottom line

The idea core of old Folder 06 (seeds, P3R2 waves, elegance adjudication,
fixes, founder-fit, and the frozen 65-idea longlist) is proven Fable 5 **as a
model** by independent runtime transcripts, but its xhigh effort was only ever
requested, never observed. Everything downstream of the 2026-07-13 handoff —
the authoritative scores, the final 24/top 10, all deep dives, geography,
synthesis, and the P8 sign-off — was produced by a ChatGPT continuation whose
actual model and effort are unknown, and any Fable/xhigh label on those
artifacts is contradicted by the corpus's own logs.
