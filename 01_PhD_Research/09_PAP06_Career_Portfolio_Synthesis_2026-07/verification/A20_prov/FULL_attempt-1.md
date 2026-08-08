# Independent verification — A20_prov FULL attempt-1

## Scope and inputs

- Verifier: `pap06-verifier`, requested Fable 5 / xhigh. Observed model/effort
  at the Claude Code runtime level: `NOT_EXPOSED` (the agent environment
  context identifies the powering model as Fable 5 / `claude-fable-5`;
  recorded as context, not observation, per MODEL_POLICY).
- Candidate verified (read-only): `outputs/A20_prov/attempt-1/` —
  `TASKS.csv`, `PROVENANCE.json`, `PROVENANCE.md`, `RUN_META.md`,
  `SELF_CHECK.md`.
- Authority: `state/CURRENT_VERIFY.md`, `workflow/stages/A20_prov.md`,
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`, `MODEL_POLICY.md`,
  `SOURCE_POLICY.md`.
- Ground truth opened independently: `sources/old06/98_RUN_LOGS/
  MODEL_ROUTING_LOG.jsonl`, all five `claude_*.jsonl` transcripts,
  `LAUNCHER_LOG.md`, `CHATGPT_CONTINUATION_LOG.md`, the handoff backup
  directory, `05_STATE/*`, `99_AUDIT/*`, `40_DEEP_DIVES/*`,
  `20_OPPORTUNITY_POOL/*`, `30_SCREENING` samples, `50_GEOGRAPHY`,
  `60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md`,
  `sources/old06/_claude_source/agents/*`, `sources/history/prev_chat.md`,
  `evidence/SOURCE_MANIFEST.json`.
- Web use: NONE (stage is web-free; verified against package-internal ground
  truth only). Writes: this report only.
- This verification is independent; no reasoning was continued from the
  candidate worker. All counts below are my own re-executions.

## Check-by-check findings

### 1. Required files, parseability, columns — PASS

All five required files exist in `outputs/A20_prov/attempt-1/` and are
non-empty; the directory contains exactly those five files. `TASKS.csv` has a
header plus 165 data rows (lines 2-166; trailing blank line). The header
carries exactly the ten required columns (task_id, artifact_scope,
requested_model, requested_effort, observed_model, observed_effort,
evidence_path, evidence_strength, downgrade, verdict). I read every data row;
quoting is consistent and each row ends in a controlled verdict token (my
line-end greps for the four verdicts sum to exactly 165, confirming no
malformed final fields).

### 2. Ground-truth recount of the routing log — PASS

My independent greps on `MODEL_ROUTING_LOG.jsonl`:

- `"timestamp"` = 334 (physical lines 2-335; lines 1 and 336 blank — read
  directly). Candidate claim 334: MATCH.
- `"source":"chatgpt-continuation"` = 97. Candidate 97: MATCH.
- `"downgrade": true` = 0. Candidate 0: MATCH.
- By source: orchestrator 222, launcher 12, patch 3 (222+97+12+3=334):
  MATCH with PROVENANCE.json.
- requested_model: claude-fable-5 58, claude-sonnet-5 178, GPT-5.6 Sol 52 /
  Terra 39 / Luna 6, combined "claude-sonnet-5 then claude-fable-5" 1
  (sums to 334): all MATCH.

Mapping completeness: I recomputed the union of routing-log line numbers
cited across the CSV. The 50 continuation rows cite exactly 97 distinct
continuation lines (per-row citation counts sum 97 with no overlap). The
Claude-side rows cite launcher lines 2-5/67-68/77-78/131-132/231-232 (12),
patch lines 128-130 (3), and orchestrator ranges 6-66, 69-76, 79-127,
133-230, 233-238 (222). Total 334/334 mapped; the candidate's 157-rows-cite /
8-rows-uncited split (5 sessions + 3 unlogged tasks) is arithmetically
consistent (157+8=165).

### 3. Row-count and count consistency CSV vs JSON — PASS

- CSV data rows = 165 = PROVENANCE.json `total_tasks`.
- Verdict recount on the CSV (line-end match): PARTIAL_PROVENANCE 105,
  CONTRADICTED 50, UNKNOWN 10, CONFIRMED 0 — identical to `by_verdict`.
- Per-category sums reconcile: PARTIAL 105 = 15(a)+25(b)+65(d);
  CONTRADICTED 50 = 27(b)+21(c)+2(d); UNKNOWN 10 = 10(d);
  15+52+21+77 = 165. Category membership lists in PROVENANCE.json enumerate
  15, 52, and 21 task_ids respectively and match the CSV rows and their
  verdicts (verified by reading every row).
- Evidence-strength recount (delimited field match):
  strong_runtime_sidechain 29, runtime_transcript_aggregate 7,
  orchestrator_log_paired 67, config_request_only 10,
  continuation_request_only 50, absent 2; sum 165 — identical to
  `by_evidence_strength`, and every row carries exactly one allowed value.

### 4. Verdict vocabulary — PASS

Only CONFIRMED / PARTIAL_PROVENANCE / CONTRADICTED / UNKNOWN appear as row
verdicts (165/165 rows end in one of the four; the lowercase word
"contradicted" inside two artifact_scope notes is descriptive text, not a
verdict field).

### 5. Row spot-checks against ground truth — PASS (14 rows checked, zero discrepancies)

Core idea-generation (including both pilot-overlap rows):

- **P3R2-A** (pilot overlap): routing lines 173 (started) / 177 (complete)
  read and match; dispatch confirmed at transcript line 3184 of
  `claude_20260712_171240.jsonl` (assistant message model=claude-fable-5,
  Agent tool_use id `toolu_01JQ5s1KCavFy5efSKCUyVcg`,
  subagent_type=idea-architect, "P3R2 batch A US seeds"); my sidechain
  recount: 44 records with that parent_tool_use_id and
  model=claude-fable-5, 0 with claude-sonnet-5 — exactly as claimed.
- **SEEDS-A**: routing lines 119/127 read and match; dispatch at line 5195 of
  `claude_20260712_105503.jsonl`; sidechain recount 86 fable / 0 sonnet —
  exact match.
- **SEEDS-W**: routing line 124 is the only seeds-W entry (started only —
  grep over the whole log); no SEEDS_W artifact exists in
  `20_OPPORTUNITY_POOL` (full directory glob); sidechain recount 47 fable /
  0 sonnet — all three claims verified.
- Remaining core rows (SEEDS-B/C/D, P3R2-B..G, fixers): routing lines
  119-127 and 173-198 read in full; every cited started/complete line number
  and note is faithful.

Adjudication (both required plus one more):

- **P3R2-ELEGANCE-JUDGE** (pilot overlap): routing lines 183/184 match;
  dispatch at transcript line 4214 (fable-emitted Agent dispatch,
  subagent_type=idea-elegance-judge); sidechain recount 36 fable / 0 sonnet —
  exact match.
- **P2A-FABLE-ADJUDICATION**: routing lines 171/172 match (completion note
  "agent self-reported fable-5/xhigh" quoted faithfully); dispatch at line
  2739; sidechain recount 183 fable / 0 sonnet — exact match. The artifact
  header ("Fable 5 (claude-fable-5), xhigh effort") exists as described and
  is correctly treated as a self-report, not runtime proof.
- **P2-ATLAS-ADJUDICATION**: routing lines 117/118 read and match
  (orchestrator main-thread work, fable actual_model in log); ATLAS.md
  exists.

ChatGPT-continuation rows (seven verified, more than the three required):

- **CHATGPT-CHECKPOINT-DIAGNOSIS** line 239, **CHATGPT-P4-S2-REGEN** lines
  240/249/250/251 (started/failed/retry/complete chain read in full),
  **CHATGPT-P5-SELECTION** line 307 (complete-only), **CHATGPT-P6-DD-P3R2-D-02**
  lines 308/313, **CHATGPT-P7-SYNTHESIS** line 331,
  **CHATGPT-P8-MECHANICAL-AUDIT** line 334, **CHATGPT-P8-FINAL-COMPLETION**
  line 335. Every one is `source:"chatgpt-continuation"`,
  requested GPT-5.6 Sol/Terra, `actual_model:"unknown"`,
  `effort:"unknown"` — exactly as the rows state. Cited output artifacts
  (deep dives, SELECTION.md, GEOGRAPHY_BRIEF.md, P4_SCORES_S2_REGENERATED.json,
  P5_RT_G01.md, FABLE_ADJUDICATION.md, FINAL_AUDIT.md) exist.

Unlogged/UNKNOWN rows (two verified):

- **PATCH-GEOGRAPHY-SCOPE**: `05_STATE/GEOGRAPHY_SCOPE_PATCH_2026-07-12.md`
  exists; PROGRESS_LOG.md line 18 is the 20:34:49Z scope-patch checkpoint as
  cited; a grep for "geography" over the routing log hits only P6
  continuation entries (lines 247-333) — no routing entry for the patch
  application. UNKNOWN with `absent` evidence is correct.
- **P2A-PREFILTER**: `INDIA_SOURCE_ORIGIN_PREFILTER.md/.json` exist;
  PROGRESS_LOG.md line 20 is the 23:56:53Z prefilter checkpoint; "prefilter"
  has zero hits in the routing log. Correct.

Sonnet-side representatives: **P4-G01** sidechain recount 130 sonnet /
0 fable (dispatch line 5820); **P1-L01-SCOUT** 81 sonnet records with the
cited parent id; **P2A-01** four-entry chain at lines 133/137/141/145 read in
full (failed unregistered-agent dispatch then sonnet-pinned retry — described
faithfully). The L13-L16 interrupted-redispatch chains (lines 63-98) were
read in full and match the consolidated rows' citations exactly.

No fabricated line, count, or quote was found anywhere I checked.

### 6. Requested vs observed separation; effort claim — PASS

Every row keeps requested_* (logs/config/frontmatter) separate from
observed_* (transcript records or explicit UNKNOWN/NOT_APPLICABLE). Launcher
probe results and agent self-reports are labeled as self-reports in the rows
where they appear. No row treats a filename, folder note, title, prompt, or
style as runtime observation. The central claim — no runtime effort field
exists anywhere — was verified beyond the required two files: `"effort":`
has ZERO matches in all five transcripts. observed_effort is
NOT_RECORDED/UNKNOWN on every row; no CONFIRMED verdict exists, consistent
with that. I additionally verified the "no third model" claim: all model
strings on transcript records are claude-fable-5, claude-sonnet-5, or one
`<synthetic>` system record in session 1; the 82 bare `"model":"sonnet"`/
`"fable"` strings are dispatch-input request parameters whose line numbers
match the CSV's cited dispatch lines. Per-session aggregate counts
(fable 140/48/498/1829/250; sonnet 2472/527/1888/3314/0) reproduce exactly.
Agent-dispatch counts per session (32/4/22/50/4) match the candidate's
session-3 "22 dispatches" and session-4 "50 dispatches" claims.

### 7. Contradiction reconciliation honesty — PASS

- `40_DEEP_DIVES/_about.md` reads verbatim "Ten Fable/xhigh reports on the
  selected...". Routing lines 308-329 place all ten deep dives in the
  continuation with unknown actual model. The candidate's REJECTED resolution
  is correct and honest.
- `99_AUDIT/FABLE_ADJUDICATION.md` line 6 reads verbatim "**Actual runtime
  model / effort:** `unknown` / `unknown` (not exposed; not inferred)". The
  candidate's title-is-a-role-label treatment is accurate.
- `30_SCREENING/LONGLIST.md` line 6 contains "three independent Fable/xhigh
  elegance adjudications"; the candidate's half-evidenced resolution matches
  my sidechain recounts (36/112 claimed—36 verified here—/80, 0 sonnet).
- `60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md` states "Routing
  records: 333." and that actual model/effort remain unknown — the disclosed
  333-vs-334 discrepancy is real and correctly characterized as immaterial.
- `sources/history/prev_chat.md` section 7 (line 384 ff.) states the same
  split the candidate reports; correctly used as corroboration only.
- The routing-log `downgrade:false` on continuation entries vs the rows'
  `route_substitution_vs_policy` is explained honestly in PROVENANCE.md (the
  historical flag tracked model-below-request downgrades, not the route
  substitution); both facts verified.

### 8. Category verdict logic — PASS

- (a) PARTIAL_PROVENANCE, 15/15: every core task's model half is
  sidechain-evidenced (my spot recounts agree; zero sonnet records in any
  checked core sidechain) while the effort half is request-only everywhere
  (zero runtime effort fields). PARTIAL, not CONFIRMED, is the honest
  ceiling. Caveats (SEEDS-W incompletion, geography-patch edits) verified.
- (b) PARTIAL_PROVENANCE with the 27-task CONTRADICTED subset disclosed,
  52/52: the 25 Claude-side rows and the 27 continuation rows are enumerated;
  the decisive-later-adjudication-was-non-Fable disclosure matches the log.
- (c) CONTRADICTED, 21/21, 0 runtime model evidence: all 21 rows verified
  as continuation-logged with unknown actual model; the corpus policy route
  for that work was Claude (inherit Fable/xhigh), so the substitution reading
  is supported by the corpus's own records.
- Coverage numerators/denominators (15/15, 52/52, 21/21, 165/165, 334/334,
  5/5 transcripts) are internally consistent and consistent with the CSV.

### 9. Pilot labels, A10-blindness, web, write confinement — PASS

No output is labeled as a pilot/sample/non-final; the word "pilot" appears
only in references to the accepted `pilot/A20_prov/attempt-1` (method
anchors) and in RUN_META/SELF_CHECK compliance prose — permitted. Nothing in
the candidate references A10 ranking content; RUN_META documents A10 as
status-only. No web activity is documented or evidenced (stage-compliant;
this verification also used no web). The candidate directory contains exactly
the five required files and nothing else; no immutable file shows candidate
modification in anything I opened.

### 10. RUN_META / SELF_CHECK honesty — PASS

RUN_META names the worker `pap06-fable-xhigh` with requested Fable 5/xhigh —
matching the route card. Observed model/effort are `NOT_EXPOSED`, with the
environment-context identification explicitly demoted to context rather than
observation — exactly the MODEL_POLICY posture. Treated as missing
observation, not mismatch and not proof. No invented timestamps (start/end
recorded as NOT_EXPOSED with run date only). Every RUN_META/SELF_CHECK count
I re-executed (334/97/0/58/178/97; 44/0 at 3184; 36/0 at 4214; 86/183/130/81
sidechain counts; per-session aggregates; zero effort fields; 419 manifest
files; SHA-256 27EAC27E... in the continuation log) reproduced exactly.
SELF_CHECK's disclosed weaknesses (67 log-paired Sonnet rows, line-count vs
occurrence-count caveat, encoding not re-verified) are accurate disclosures,
not overstatements.

## Defects

No critical or major defects found. Minor nits, explicitly flagged and
non-blocking:

1. (minor) `TASKS.csv` rows LAUNCH-PROBE-CRITICAL/-SCOUT assign
   PARTIAL_PROVENANCE on launcher self-report evidence
   (`config_request_only`); UNKNOWN would have been the strictest reading.
   The self-report-only basis is disclosed on the rows and in
   PROVENANCE.json missing_proof, so no claim is overstated.
   Affected file: `outputs/A20_prov/attempt-1/TASKS.csv` (rows 2-3 of data).
2. (minor) PROVENANCE.json category (b) `runtime_model_evidence_numerator`
   = 25 counts 12 P4 screens whose model rests on paired orchestrator log
   entries plus session aggregates (not per-dispatch sidechain) as
   model-evidenced; the basis text and per-row evidence_strength disclose
   this precisely. Affected file: `PROVENANCE.json`.
3. (minor) Row CHATGPT-P5P8-VALIDATOR-TOOLING cites the continuation log
   "23:16:53 section: validators added"; that section's body confirms the
   red-team and selection validators, while the deep-dive/portfolio/mission
   validators are narrated in later sections of the same log. Citation is
   directionally faithful but slightly imprecise. Affected file: `TASKS.csv`.
4. (minor) RUN_META says the routing log was read "in three windows" but
   lists four line ranges — a trivial prose slip with no evidentiary effect.
   Affected file: `RUN_META.md`.

## Limitations of this verification

- Sidechain model recounts were performed for 7 dispatches (P3R2-A, SEEDS-A,
  SEEDS-W, elegance judge R1, P2A-FABLE-ADJUDICATION, P4-G01, P1-L01-SCOUT);
  the candidate's remaining 22 per-dispatch counts were not all individually
  re-executed, but every one I tested reproduced exactly, and the aggregate
  per-session counts (which bound the totals) reproduced exactly.
- Routing-log mapping completeness was verified by arithmetic over the cited
  line ranges plus full reads of lines 1-6, 63-98, 115-145, 171-200,
  229-251, 306-314, and 330-336; the uninspected middle windows are covered
  by the range arithmetic rather than line-by-line reads.
- Grep counts are ripgrep matching-line counts, the same method the
  candidate disclosed; transcript file encodings were not independently
  re-verified (all five files were fully searchable in this run).
- This verifier's own runtime model/effort were not exposed; identity is
  recorded per MODEL_POLICY evidence-honesty rules above.

VERDICT: PASS
