# Stage 70 — Model and Effort Reconciliation Report

Run: HSXIP-20260805T071311Z. Date: 2026-08-05. Governing rules:
`MODEL_PLAN.md` (requested configuration and acceptance policy),
`docs/MODEL_EVIDENCE.md` (evidence standards), `CLAUDE.md` (Fable integrity
policy). Evidence base: `state/MODEL_LOG.csv`, `state/WORKLOG.md`,
`state/FALLBACK_LOG.md`, `state/checkpoints/00_done.json` through
`60_done.json` — all read READ-ONLY by this stage agent; per the run design,
this agent writes nothing under `state/`. The stage-70 row of
`state/MODEL_LOG.csv` and any `70_done` checkpoint are the parent
orchestrator's to complete at acceptance.

**Evidence rules applied (from `docs/MODEL_EVIDENCE.md`):** requested
model/effort come from agent frontmatter and launch arguments and do not prove
the served model. Observed values are accepted only from platform metadata
(`/status`, session/task/API metadata, an explicit fallback/availability
notice, or durable debug metadata naming the served model). An agent saying
"I am Fable" is not evidence. Where no platform evidence is exposed, the
correct record is `not_exposed` — and requested configuration is preserved as
separate evidence, never upgraded into observed fact.

---

## 1. Requested vs. observed, stage by stage

Requested values below are reconciled against `MODEL_PLAN.md`'s table and the
per-stage agent frontmatter/launch configuration recorded in
`state/MODEL_LOG.csv` (`requested_model`, `requested_effort` columns); they
agree in all eight rows. Observed values are taken from the same log's
`observed_model`/`observed_effort` columns.

| Stage | Agent | Requested (plan + frontmatter) | Observed model/effort | Status | Exposed usage metadata (task notification; totals only) |
|---|---|---|---|---|---|
| 00 scope | `s00-scope` | Sonnet 5 / medium | `not_exposed` / `not_exposed` | accepted 2026-08-05T07:17:39Z | tokens_total 68,960; tool_uses 25; duration 179,863 ms |
| 10 disclosure | `s10-disclosure` | Sonnet 5 / high | `not_exposed` / `not_exposed` | accepted 07:28:08Z | tokens_total 68,798; tool_uses 9; duration 565,529 ms |
| 20 prior art | `s20-prior-art` | Sonnet 5 / xhigh | `not_exposed` / `not_exposed` | accepted 08:03:17Z | tokens_total 228,381; tool_uses 72; duration 2,018,507 ms |
| 30 IP screen | `s30-ip-screen` | Fable (alias → Claude Fable 5) / xhigh | `not_exposed` / `not_exposed` | accepted 08:13:38Z | tokens_total 136,124; tool_uses 13; duration 521,615 ms |
| 40 UHV | `s40-uhv` | Fable / xhigh | `not_exposed` / `not_exposed` | accepted 08:24:48Z | tokens_total 151,868; tool_uses 26; duration 593,887 ms |
| 50 arXiv | `s50-arxiv` | Sonnet 5 / high | `not_exposed` / `not_exposed` | accepted 08:35:37Z | tokens_total 143,718; tool_uses 38; duration 554,721 ms |
| 60 red team | `s60-red-team` | Fable / xhigh | `not_exposed` / `not_exposed` | accepted 08:44:22Z | tokens_total 153,903; tool_uses 13; duration 443,424 ms |
| 70 final | `s70-final` | Fable / xhigh | `not_exposed` / `not_exposed` (as of authoring) | in progress at authoring; acceptance is the parent's act | not yet emitted at authoring time (a task notification is produced only on completion) |

**Reconciliation findings:**

1. **No divergence between `MODEL_PLAN.md` and the launch record.** Every
   stage was launched under exactly the model/effort the plan assigns; no
   stage was substituted to a cheaper model for a Fable-assigned result, and
   no Sonnet-gathered material was accepted as Fable judgment (Sonnet stages
   00/10/20/50 fed evidence into Fable stages 30/40/60/70, which is the
   plan's intended division of labor).
2. **Observed model/effort is `not_exposed` for every stage.** The interface
   exposed no `/status` output, no session/API model metadata, and no
   fallback or availability notice for any stage agent. This is recorded as
   `not_exposed` in all 16 observed-value cells of `state/MODEL_LOG.csv`
   (stages 00–60) — not as confirmation and not as suspicion; per
   `docs/MODEL_EVIDENCE.md`, absence of observable metadata is recorded as
   `not_exposed`, "not as proof of a model substitution."
3. **What *was* observed:** Claude Code task notifications on subagent
   completion exposed, per stage, a total subagent token count (no
   input/output split), a tool-use count, and a duration. These are recorded
   in the `notes` column of `state/MODEL_LOG.csv` and in each stage's
   checkpoint JSON (`telemetry` block, `source: "Claude Code
   task-notification usage metadata"`), and are reproduced in the table
   above. No turns, per-direction token, web-query, cost, or effort telemetry
   was exposed for any stage; those fields are `not_exposed` in the log. **No
   telemetry in this report is estimated or invented.**
4. **Self-identification handled per policy.** The stage-40 and stage-60
   outputs each self-report production "on model `claude-fable-5` as reported
   by the harness"; the parent recorded these self-reports in
   `state/MODEL_LOG.csv` notes and checkpoints but did **not** accept them as
   observed evidence (`observed_model` remains `not_exposed`), exactly as
   `docs/MODEL_EVIDENCE.md` requires. The same treatment applies to this
   stage: the stage-70 agent's harness-provided system prompt states the
   model is `claude-fable-5` with the plan-assigned effort; that statement is
   launch-configuration/self-report-grade evidence supporting the *requested*
   column, not platform-observed telemetry, and the observed column stays
   `not_exposed` unless the parent has platform evidence at acceptance time.
5. **Basis for accepting Fable-stage authorship.** Under `MODEL_PLAN.md`'s
   acceptance rule, each Fable-assigned output (30/40/60/70) is accepted as
   Fable-authored on the combination of (a) requested configuration in
   frontmatter/launch arguments, (b) zero fallback/availability/flag notices
   in any transcript (§2), and (c) the parent's full-content gate review of
   each output. This is an acceptance under stated evidence rules, not an
   observed-telemetry claim — the distinction this report exists to keep.

## 2. Fable integrity accounting — zero events

`CLAUDE.md`'s Fable integrity policy (`switchModelsOnFlag` false; quarantine
and one retry on first flag/refusal/substitution; pause on second; never
accept a safety-fallback result as a Fable result) was armed for all four
Fable stages. The complete event record:

- **Stage 30 (`s30-ip-screen`):** no flag, no refusal, no fallback notice, no
  substitution evidence. Flag count 0 (`state/MODEL_LOG.csv` row 30;
  `state/checkpoints/30_done.json`).
- **Stage 40 (`s40-uhv`):** same — zero events (row 40; `40_done.json`).
- **Stage 60 (`s60-red-team`):** same — zero events; the output itself states
  "No safety fallback, refusal, or model substitution occurred during this
  stage" (`60_RED_TEAM.md` header; row 60; `60_done.json`).
- **Stage 70 (`s70-final`, this stage):** as of the authoring of this report,
  zero flag, refusal, fallback, availability, or substitution events have
  occurred in this stage's session. The parent completes this stage's row at
  acceptance; if any event occurred after authoring, the parent's log entry
  controls.

**Cumulative Fable flag/fallback count for the run: 0.** The two-strike
policy was never triggered; no quarantine, rewrite-and-retry, or pause
occurred; no availability error occurred; no work was routed to any other
provider or model. `state/FALLBACK_LOG.md` accordingly contains no event
entries; its full current content is quoted verbatim:

> # Fable model integrity and fallback log
>
> No runtime model event has occurred. Log each classifier notice, refusal,
> availability error, prompt rewrite, retry, quarantine path, and final disposition.
> Absence of observable metadata is recorded as `not_exposed`, not as proof of a
> model substitution.

## 3. Process events (not model-integrity events)

One process deviation occurred in the run and is classified here explicitly as
a **process event**, not a Fable flag, refusal, fallback, or substitution:

- **Stage 20 fork-compaction deviation** (documented in `20_SEARCH_LOG.md` §0
  and `state/WORKLOG.md`): the stage-20 session (Sonnet 5/xhigh, per plan)
  dispatched six scoped research forks. Two forks (coverage areas 4 and 6)
  hit context compaction mid-task, lost sight of their narrow assignments,
  re-ran near-complete passes over all six coverage areas, and wrote drafts
  directly into `outputs/20_PRIOR_ART.csv` and the search log — contrary to
  their report-back-only instructions. The stage agent treated the resulting
  files as an unverified draft: it cross-validated the compaction-recovered
  content against the four cleanly-scoped forks' independent findings
  (agreement was strong everywhere they overlapped), independently
  re-verified and added three high-value sources the drafts had missed
  (N016, N017, N018), reconciled `source_id` numbering (no collisions), and
  programmatically re-validated the CSV against `SOURCE_POLICY.md`'s schema
  before the parent's gate review. **Classification rationale:** no model was
  flagged, no refusal occurred, no model change occurred (the forks were
  Sonnet-lane support work under a Sonnet-assigned stage; `MODEL_PLAN.md`
  reserves Fable acceptance only for Fable-assigned stages); the deviation
  was one of task scope and write discipline, was self-reported rather than
  concealed, and was repaired within the stage. It is therefore logged as a
  process deviation in `state/MODEL_LOG.csv` row 20's notes and in
  `20_SEARCH_LOG.md` §0, and correctly does **not** appear in
  `state/FALLBACK_LOG.md`.
- Two minor sub-events within the same stage, recorded for completeness, are
  likewise process-grade: the area-4 fork's attempt to delegate further
  sub-searches was rejected by the harness (the fork then completed the work
  directly — `20_SEARCH_LOG.md` §4), and the parent noted a minor S015
  verification-depth tension between a fork's interim report and the final
  ledger (immaterial to conclusions; carried as the S015 depth caveat in
  `70_FINAL_OTL_BRIEF.md` §9).

No other deviation, retry, or anomaly appears in `state/WORKLOG.md`, the
checkpoints, or any stage output.

## 4. Checkpoint and state consistency

- Checkpoints `00_done.json` through `60_done.json` exist, one per accepted
  stage, each carrying the stage's requested/observed model fields
  (`observed_model: "not_exposed"` in all), gate result (PASS in all),
  acceptance timestamp matching `state/MODEL_LOG.csv`'s `end_utc`, and the
  task-notification telemetry block. The three Fable-stage checkpoints
  (30/40/60) each record the zero-event integrity status; `40_done.json` and
  `60_done.json` additionally record that the outputs' `claude-fable-5`
  self-reports were noted but not accepted as observed evidence.
- `state/MODEL_LOG.csv` row 70 is `pending`/`not_started` as expected at this
  stage's launch; completing it (and the 70 checkpoint) upon acceptance of
  the three stage-70 files is the parent's task. This report makes no entry
  on its own behalf.
- `state/WORKLOG.md`'s narrative (run start 2026-08-05T07:13:11Z; sequential
  stage acceptances 07:17–08:44 UTC; "flag count 0" carried through every
  Fable stage) is consistent with the log and checkpoints; no discrepancy was
  found between any two state records during this reconciliation.

## 5. Conclusions

1. Every stage ran under its plan-assigned requested model and effort; the
   sequential, no-race execution order the plan requires is reflected in the
   monotonic acceptance timestamps.
2. Observed model/effort is `not_exposed` for all stages — no platform
   telemetry was available, only task-notification usage totals, which are
   recorded without embellishment. Requested configuration has not been
   upgraded into observed fact anywhere in this run's records or in this
   report.
3. Zero Fable flag/refusal/fallback/availability/substitution events occurred
   across stages 30, 40, 60, and (as of authoring) 70; `state/FALLBACK_LOG.md`
   is event-free and quoted as-is above; the two-strike policy was never
   invoked.
4. The single process deviation (stage-20 fork compaction) was documented,
   cross-validated, and repaired inside its stage, and is correctly
   classified as a process event, not a model-integrity event.
5. The stage-70 deliverables (`70_FINAL_OTL_BRIEF.md`, `70_EXEC_SUMMARY.md`,
   and this report) were authored end-to-end within the s70-final stage
   session under the requested Fable 5/xhigh configuration, synthesizing —
   not delegating — the accepted stage outputs; per the plan's acceptance
   rule, the substantive-Fable-authorship determination for stage 70 is made
   by the parent at acceptance on the evidence standard in §1.5.

No invented telemetry appears in this report; every number above traces to
`state/MODEL_LOG.csv`, a checkpoint JSON, or `state/WORKLOG.md`, and every
absent value is stated as `not_exposed` rather than estimated.
