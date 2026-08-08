# Complete chat handoff: Hall/coil PhD, Folder 06, startup alignment, and Claude package

Created: 2026-07-27  
Purpose: attach this file to a new ChatGPT conversation so the work can
continue without asking the user to repeat the project history.

## Instruction to the next ChatGPT conversation

Read this file completely before advising the user or changing any package.
Treat the section **Current authoritative state** as the latest state. Earlier
packages, policies, and attempted repairs are historical and may have been
superseded.

The user wants accurate, evidence-backed work, but is exhausted by repeated
PowerShell/package failures. Do not provide another incremental patch. If a
code defect is found, produce a newly validated, complete, standalone ZIP with
one start/resume command.

## Coverage note

This is a comprehensive operational handoff assembled from the conversation
content available to ChatGPT, retrieved continuity context, uploaded-file
metadata, console logs, screenshots, decisions, and completed deliverables. It
is designed for continuing the work, not as a byte-for-byte account export of
the ChatGPT interface.

For an account-level raw export, ChatGPT provides **Settings > Data controls >
Export data**:
https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data

---

# 1. Current authoritative state

## Latest complete package

Use:

`PHD_ALIGN_POWER_PILOT_FULL_FIXED_V2.zip`

SHA-256:

`2928d057739b44dda451acf20b351f94f8c08aff5664eebdeecfa31d276a3b5b`

The ZIP was saved to the user's ChatGPT Library on 2026-07-27. It is a
standalone package, not a patch. Its extracted root is:

`PHD_ALIGN_POWER_PILOT_FULL_FIXED`

The user should extract it into a fresh, short location such as `C:\AI\PAP`,
enter the directory containing `START.ps1`, and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
```

The same command begins or resumes. Do not merge the ZIP into an earlier
mission directory.

## What that command performs

1. A local, no-model launcher regression test.
2. A live isolated pilot across all nine configured model/effort routes.
3. A fresh two-pass Fable 5/xhigh reproducibility check of Folder 06.
4. The complete nine-stage research mission.

Validated components and completed stages are skipped on later runs.

## Latest package validation already completed

- ZIP CRC test: PASS.
- Fresh extraction: PASS.
- All 130 extracted files matched the source tree byte-for-byte.
- Nine PowerShell scripts parsed without syntax errors using an independent
  PowerShell grammar.
- PowerShell scripts contain ASCII only, avoiding Windows PowerShell 5.1
  no-BOM encoding ambiguity.
- No obvious PowerShell 7-only syntax was found.
- Maximum archive path: 84 characters.
- Maximum archive path component: 34 characters.
- No absolute paths, parent traversal, backslash ZIP entries, duplicate
  entries, case/Unicode collisions, Windows-reserved names, or symlinks.
- 26 JSON, 3 JSONL, and 13 CSV files parsed.
- Inputs contain 24 unique startup ideas, 126 unique raw Folder 06 candidates,
  129 unique priority source leads, and 18 specialized-power leads.
- The nine-stage route table was checked, including six critical Fable
  5/xhigh stages.
- Folder 06 contains completed Fable 5/xhigh/no-downgrade provenance for 15
  required seed, P3R2, and adjudication tasks.
- Stage 10 and Stage 25 canonical-schema regression fixtures are included.
- No automatic invocation of another AI provider is present.

## Status after delivery

The package has been built and saved, but the user has not yet reported the
result of running this newest V2 ZIP. The next operational event should be the
user running the one command above and sharing the console output only if it
does not continue.

---

# 2. Exact cause of the most recent false failure

The preceding package displayed:

```text
==== Package validation ====

START FATAL: Package validation failed. The pilot and research were not started.
```

No `CHECK.ps1` failure lines appeared. The validator had not actually failed.

The old `START.ps1` used:

```powershell
function Invoke-Component {
    ...
    & $hostPath ... -File ... @Arguments
    return $LASTEXITCODE
}

$checkExit = Invoke-Component -ScriptName 'CHECK.ps1'
```

In PowerShell, every success-stream result produced inside a function becomes
function output, not only the expression following `return`. Therefore,
`$checkExit` received an array containing the child validator's console text
plus the integer exit code. Comparing that array with zero produced a truthy
failure result even when `CHECK.ps1` exited successfully.

The V2 package fixes this by:

- not assigning an output-producing function invocation to the exit variable;
- sending child success output through `Out-Host`;
- storing `$LASTEXITCODE` separately in
  `$script:LastComponentExitCode` as an integer;
- running `LAUNCH_TEST.ps1` automatically before package validation;
- checking a child that emits output and exits `0`;
- checking another child that exits `7`;
- stopping before any model call if either scalar exit code is not preserved;
- making real `CHECK.ps1` failure lines visible above the final error.

Optional launcher-only test:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1 -LauncherSelfTestOnly
```

The normal one-command run already includes this test automatically.

Relevant PowerShell documentation:

- Function output/return behavior:
  https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_return
- `$LASTEXITCODE` behavior for `powershell.exe -File`:
  https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Core/about/about_automatic_variables?view=powershell-5.1

---

# 3. User profile and research context relevant to this work

- The user is a second-year Stanford Electrical Engineering PhD student.
- Undergraduate background: Computer Engineering.
- The user wants work that supports both a defensible PhD and possible
  high-end technical startup directions around 2030.
- Research themes include harsh-environment magnetic sensing, GaN
  Hall-effect sensors, fusion diagnostics, high-density magnetic arrays,
  current-distribution reconstruction, HTS systems, and potentially battery
  current distribution.
- A manuscript titled **“AlGaN/GaN Hall-Effect Sensor for In-Situ Magnetic
  Field Monitoring of the HSX Stellarator”** was submitted as a Regular Letter
  to IEEE Sensors Letters.
- Reported manuscript/system details include HSX operation under UHV, 1 T, up
  to 200 kW ECRH, stable operation over 68 shots, a 1 MHz readout, and
  correlation with plasma stored energy.
- Reported sensor implementation details include a GaN Hall die wire-bonded to
  a ceramic LCC, EPO-TEK 353ND, a 150 °C one-hour vacuum bake, a zirconia
  holder, grounded graphite shield, Keysight DSOX1204G biasing, INA849 plus
  two OPA814 stages, total gain 200 V/V, and 1 MHz bandwidth.

## Overall PhD direction already recommended

`OPT2` was interpreted as the overall PhD direction, not merely one project:

1. First establish the Hall-effect sensor itself as a calibrated, validated,
   uncertainty-bounded scientific instrument.
2. Then integrate Hall sensing with inductive coils as a hybrid diagnostic.
3. Deliver a reusable module plus simulation/reconstruction package for
   subsequent research and applications.

The core thesis framing was:

> An absolutely calibrated GaN Hall diagnostic for HSX, extended into a
> hybrid Hall–inductive measurement architecture.

Suggested publication structure:

- P1: calibrated sensor/instrument paper;
- P2: hybrid fusion diagnostic and reconstruction/software paper;
- P3: vector-probe or broader application upside, if justified.

Mandatory near-term technical work previously identified:

- resolve the approximately 109× anomaly;
- locate and health-check the deployed module;
- establish absolute calibration;
- create a complete uncertainty budget;
- establish repeatability;
- correct bandwidth/performance analysis;
- reanalyze 2025 data;
- revise P1;
- obtain advisor approval before expanding scope.

---

# 4. Hall plus inductive-coil architecture: questions to preserve

The user proposed the following reasoning:

- Radiation and neutron exposure may change Hall sensitivity, bias, offset,
  noise, and long-term stability.
- Compensation or recalibration will therefore be needed.
- An inductive coil measures changing magnetic field and might help calibrate
  Hall sensitivity.
- The Hall sensor might in turn help calibrate the coil.
- The user wants the two sensors to provide mutual consistency and possibly
  mutual calibration.

The next chat should preserve, but critically test, this distinction:

- Hall sensors can measure DC and low-frequency field but have offset,
  sensitivity drift, temperature dependence, and radiation sensitivity.
- Inductive coils measure `dB/dt`; they do not directly supply an absolute
  static-field reference.
- A coil can provide a strong dynamic cross-check during known field
  transitions and can improve bandwidth fusion.
- A Hall channel can constrain integration drift and supply DC/low-frequency
  information.
- Mutual consistency is not automatically absolute self-calibration.
- Identifiability depends on known excitation, geometry, timing,
  transfer-function models, temperature measurement, and at least one
  traceable reference or redundant constraint.
- Radiation-induced sensitivity changes still require irradiation campaigns,
  reference fields/currents, redundant channels, periodic calibration, or a
  validated physics/statistical drift model.
- Bandwidth fusion and radiation-damage compensation must be treated as
  separate problems.

The user explicitly invited disagreement and alternative architectures.

## Requested application/collaboration assessment

The user asked whether to approach groups working on:

- Z-pinch current measurement;
- tokamak plasma diagnostics;
- magneto-inertial-confinement fusion;
- stellarator coil-current distribution and high-accuracy alignment;
- superconducting motors;
- other magnetic-diagnostic applications.

The user also requested comparison against:

- other Hall-effect sensors;
- optical current/field sensing;
- zero-flux sensors;
- shunts;
- current transformers;
- Rogowski coils;
- fluxgates;
- other magnetic diagnostic approaches.

The user wants maximum accuracy while controlling cost.

---

# 5. Startup and specialized-power alignment scope

The mission must compare:

1. the completed 24-idea Folder 06 startup portfolio;
2. the Hall/GaN/coil PhD direction;
3. shared skills and bridge projects;
4. startup preparation through approximately 2030;
5. specialized power converters, power electronics, power supplies,
   protection, current sensing, drivers, magnet-power balance of plant, and
   qualification systems.

The user expects the PhD to contribute more directly to startup options than
startup work contributes to the PhD, but wants the relationship tested rather
than assumed.

## Previously clarified power-related identifiers

- `P3R2-F-02`: clearest power/current-supply idea in the portfolio; a
  superconducting-magnet precision drive-and-dump system, approximately
  1–50 kA DC and approximately 10 ppm stability; previously reported as rank
  15/24 with score 49.4.
- `P3R2-C-10`: beam-current/radiation-dose measurement.
- `P3R2-C-12`: modular 20–80 K turbo-Brayton cryocooler.
- In earlier HTS files, `C10` can instead refer to magnet power-converter
  interface and protection/control integration.
- In earlier HTS files, `C12` can instead refer to NI/MI-HTS coil winding
  cells, winding-process control, and spatial contact-resistance mapping.

Always identify which naming system is being used; do not silently merge the
two meanings of `C10` or `C12`.

## Required specialized-power stage

The latest package includes `25_power_alignment`, assigned to Fable 5/xhigh.
It must:

- inspect the full idea pool, not only the final 24;
- cover at least 18 distinct ideas;
- analyze direct PhD technology, measurement/qualification enablement,
  transferable skills, or no meaningful support;
- examine Hall/coil sensing for ripple/transient validation, current sharing,
  ramp/dump testing, protection, and calibration;
- separate radiation compensation from bandwidth fusion;
- identify missing converter, gate-drive, WBG, magnetics, insulation,
  thermal, control, HIL, safety, certification, manufacturing, and service
  skills;
- compare full power products, measurement/qualification subsystems, and
  engineering/reference-platform offerings;
- rank inexpensive bridge experiments that retain PhD value even if no
  company is formed.

---

# 6. Final model, effort, logging, and continuation policy

## Authoritative current policy

- Claude Code on Windows PowerShell is the execution environment.
- The package is Claude-only and does not automatically invoke Codex, OpenAI,
  or another provider.
- Fable 5/xhigh must produce the final accepted result for every
  Fable-assigned stage.
- Temporary or auxiliary model activity may be logged and is not by itself a
  downgrade if Fable 5 produces the accepted final response.
- Only Fable-assigned stages enforce downgrade tracking.
- First non-Fable or unverifiable final result:
  - quarantine the affected outputs;
  - save a durable checkpoint;
  - clarify the benign academic/civilian prompt without weakening it;
  - retry Fable 5 once.
- Second failure in the same Fable policy cycle:
  - pause;
  - preserve all state, prompt, logs, and outputs;
  - require explicit user review/authorization before another Fable-only
    cycle.
- Security/content fallback notices are logged.
- Model, requested effort, reported models, primary/auxiliary models, final
  result model, turns, tokens, duration, web calls, reported cost, and
  downgrade count must be logged.
- Checkpoints must be frequent and resumable.
- Do not claim actual effort was independently observed if the stream only
  proves it was requested.

Older conversations discussed automatic Codex/ChatGPT fallback. That is
superseded for the latest package by the Claude-only/no-automatic-routing
policy above.

## Full research route table

| Stage | Work | Model | Effort | Turn cap | USD ceiling per attempt |
|---|---|---|---|---:|---:|
| `00_inventory` | Input inventory/conflicts | Sonnet 5 | high | 65 | 8 |
| `10_evidence_refresh` | Current evidence refresh | Sonnet 5 | xhigh | 120 | 20 |
| `20_alignment` | Bidirectional PhD/startup alignment | Fable 5 | xhigh | 110 | 18 |
| `25_power_alignment` | Specialized-power/PhD alignment | Fable 5 | xhigh | 120 | 20 |
| `30_skills` | Shared skills and bridge projects | Fable 5 | xhigh | 100 | 15 |
| `40_portfolio` | Re-rank all 24 ideas | Fable 5 | xhigh | 125 | 22 |
| `50_execution` | Time, IP, collaboration, execution | Sonnet 5 | high | 85 | 10 |
| `60_redteam` | Independent red team | Fable 5 | xhigh | 115 | 18 |
| `70_synthesis` | Final synthesis/sign-off | Fable 5 | xhigh | 100 | 15 |

The ceilings are safety caps, not target spending.

---

# 7. Folder 06 Fable provenance

The user repeatedly asked whether Folder 06 ideas were generated using Fable
5/xhigh.

The durable evidence supports:

- Fable 5/xhigh completed seed waves A, B, C, and D;
- Fable 5/xhigh completed P3R2 waves A through G;
- Fable 5/xhigh completed three P3R2 elegance adjudications;
- Fable 5/xhigh completed the P3R2 founder-fit pass;
- no downgrade was recorded for the 15 required completed tasks.

The evidence does **not** support claiming that every later deep dive, repair,
or final synthesis artifact was exclusively generated by Fable 5/xhigh.
Later ChatGPT continuation records did not expose exact model and effort.

The latest package therefore performs a new two-pass Fable 5/xhigh
reproducibility check:

1. reconstruct a 24-idea selection from a score-free snapshot of all 126 raw
   P3R2 candidates;
2. mechanically compute overlap metrics and have a separate Fable session
   interpret the comparison.

The reconstruction runs in bare mode with only the Read tool and three
hash-checked compact shards. Prior scores and adjudication fields are excluded.
This tests result stability without retroactively inventing provenance.

---

# 8. Stage 10 evidence failures and repairs

## First Stage 10 failure

The original run reached:

```text
STAGE_VALIDATION_FAILED: Verified current sources 20 < 30
```

Meaning:

- the item counted was current literature/evidence records, not the number of
  startup ideas;
- Stage 10 required at least 35 rows and at least 30 verified rows;
- only 20 rows had a `verified_*` status.

The workflow correctly paused instead of padding or silently accepting weak
evidence.

## Additive source-pack attempt

The uploaded `02_Startup(1).zip` was inspected and an additive source pack was
created. It installed 129 unique priority leads while preserving state, logs,
outputs, and completion markers.

After the retry, Stage 10 produced:

```text
TotalRows           : 48
VerifiedRows        : 42
InvalidVerifiedRows : 42

17 verified_official
16 verified_peer_reviewed
 9 verified_primary
 6 uncertain
```

The Claude call itself succeeded:

```text
subtype        : success
is_error       : False
num_turns      : 43
total_cost_usd : 10.863896499999997
```

But the acceptance gate reported:

```text
STAGE_VALIDATION_FAILED: 42 verified sources have incomplete identity, claim,
year, tier, or access data
```

This was an output-schema/field mismatch, not a Claude runtime failure.

## Latest Stage 10 protections

The current package:

- gives the model the exact CSV header;
- requires at least 35 rows and 30 verified rows;
- requires nonblank title, URL, and supported claim for verified rows;
- requires a four-digit year;
- restricts `quality_tier` to `A`, `B`, or `C`;
- restricts `access_level` to `full_text`, `abstract_metadata`, or
  `metadata_only`;
- restricts verification status to
  `verified_peer_reviewed`, `verified_primary`, `verified_official`, or
  `uncertain`;
- logs normalization of a small list of unambiguous aliases;
- gives detailed failed-field counts and example source IDs;
- includes synthetic canonical and prior-alias regression fixtures in the
  pilot/self-test.

---

# 9. Package requirements that must remain intact

- One command to start and the same command to resume.
- Full standalone ZIP; no more patch-only bundles.
- Preserve logs and state across ordinary interruptions.
- Regular checkpoints.
- Windows PowerShell 5.1 compatibility.
- Short, Windows-safe filenames and paths.
- Full permission mode by default, with work restricted to the package.
- Optional guarded mode.
- Live Sonnet 5 and Fable 5 connection tests.
- Quick isolated pilot covering every configured stage route.
- Separate Folder 06 Fable 5/xhigh verification.
- Stage 10 and Stage 25 schema checks before the expensive full run proceeds.
- No silent alternative-provider routing.
- If the package itself is defective, rebuild the complete package rather
  than asking the user to layer another repair ZIP.

---

# 10. Chronological conversation record

This section records the sequence of the visible requests and operational
events in this thread.

## 10.1 OPT2 interpretation

User asked whether OPT2 meant:

1. first validate and measure the Hall-effect sensor itself;
2. then combine it with inductive coils as a hybrid;
3. finally provide a module plus simulation package for future work;
4. likely use output in Folder 06.

The answer carried forward in this handoff is yes, with the important
qualification that the Hall sensor must first become an absolutely calibrated,
uncertainty-bounded instrument and the hybrid stage must not be described as
automatically self-calibrating.

Attachment:

`PHD_FABLE5_FINAL_RESTART_PS51_FIXED_2026-07-24(3).zip`

## 10.2 Requested Hall/coil/radiation research extension

User requested another Claude Code PowerShell operation that would:

- perform a high-quality literature review of the Hall plus coil architecture
  in Folder 06;
- investigate neutron/radiation sensitivity change, bias, and compensation;
- test whether coil output could calibrate Hall sensitivity and vice versa;
- identify other fusion and superconducting-machine groups/applications;
- analyze architecture limitations and potential versus competing magnetic
  diagnostics;
- maximize accuracy while controlling budget;
- assign models/effort in a table;
- use Fable 5/xhigh for the most critical reasoning;
- log every model/effort and performance result;
- detect Fable security-triggered downgrade;
- clarify and retry after the first Fable downgrade;
- pause and checkpoint after the second;
- checkpoint regularly;
- provide a complete run/resume package.

Attachment:

`PHD_FABLE5_FINAL_RESTART_PS51_FIXED_2026-07-24(5).zip`

## 10.3 Windows extraction/path problem

User could not extract:

`PHD_HALL_COIL_HYBRID_RADIATION_CLAUDE_2026-07-27(1).zip`

They asked to check and repair long paths and all extraction errors.

## 10.4 Completed-work description request

User said the work was completed and asked for a description of the results.

Attachment:

`P_FIXED (2).zip`

## 10.5 PhD/startup combined alignment request

User asked for a new one-command Claude Code PowerShell package to:

- test whether future startup directions and PhD research affect one another;
- combine earlier startup ideas with the PhD direction;
- find alignment and shared skills for future preparation;
- retain Windows-safe filenames;
- optimize accuracy versus budget;
- show a model/effort table;
- use Fable 5/xhigh for the most critical reasoning.

Attachment:

`06_Frontier_Idea_Research_2026-07(4).zip`

## 10.6 First manual continuation screenshot

`image(16).png` showed:

- preflight passed;
- Claude Code 2.1.219;
- Sonnet 5 and Fable 5 access passed;
- Stage `00_inventory` passed with 24 rows;
- Stage `10_evidence_refresh` stopped for manual continuation.

The console said:

```text
Saved for manual continuation
Claude was not routed to another provider.
Review state\CHATGPT_HANDOFF.md.
```

## 10.7 First Stage 10 diagnostic

The user supplied the attempt state:

```text
status: MANUAL_CONTINUATION_REQUIRED
note: STAGE_VALIDATION_FAILED: Verified current sources 20 < 30
requested_model: sonnet
requested_effort: xhigh
reported_models: claude-sonnet-5;claude-haiku-4-5-20251001
primary_models: claude-sonnet-5
auxiliary_models: claude-haiku-4-5-20251001
result_model: claude-sonnet-5
security_fallback_flag: False
downgrade_count: 0
```

There was no stderr output.

The user asked whether “verified current sources” meant publications or
startup ideas and why it failed.

## 10.8 Request to inspect a broader source folder

User asked whether the complete folder contained useful sources and authorized
adding them to a continuation package.

Attachment:

`02_Startup(1).zip`

## 10.9 Additive source pack and second Stage 10 failure

The additive source update reported:

```text
PASS: additive source pack installed.
PASS: 129 unique priority leads.
PASS: state, logs, outputs, and completion markers were preserved.
```

The rerun again stopped at Stage 10. The detailed diagnostic established:

```text
TotalRows: 48
VerifiedRows: 42
InvalidVerifiedRows: 42
```

The model call succeeded, used 43 turns, and reported cost around USD 10.86.
The failure was incomplete or noncanonical identity/claim/year/tier/access
data.

Attachment:

`image(17).png`

## 10.10 User rejected further patch packages

User explicitly said:

> Do not provide me anymore patching package.

They requested:

- one complete package with all errors repaired;
- one begin/resume command;
- all prior Fable 5 policies;
- verification of whether Folder 06 ideas used Fable 5;
- additional specialized power converter, power electronics, and power supply
  ideas;
- a new stage checking how the PhD can support those ideas.

Attachments:

- `06_Frontier_Idea_Research_2026-07(6).zip`
- `02_Startup(2).zip`

## 10.11 User added two required quick components

User requested:

1. a very quick pilot through all stages to catch validation/schema mismatches
   before the full operation;
2. a professionally structured, efficient Fable 5 verification of Folder 06
   to see whether Fable produces similar results.

They requested the complete package and exact commands.

## 10.12 False launcher failure

The user ran:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
```

from:

```text
D:\timzhao\Downloads\PHD_ALIGN_POWER_PILOT_FULL_2026-07\
PHD_ALIGN_POWER_PILOT_FULL
```

The console displayed:

```text
==== Package validation ====

START FATAL: Package validation failed. The pilot and research were not started.
Rerun the same START.ps1 command after repairing the displayed prerequisite.
```

The user said they were tired and had wasted hours because the work had not
started.

Attachment:

`image(18).png`

The exact false-failure root cause and V2 repair are recorded in Section 2.

## 10.13 Latest complete package delivered

The response provided:

`PHD_ALIGN_POWER_PILOT_FULL_FIXED_V2.zip`

with the one command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
```

The response instructed the user to discard the previous extracted package
and use a fresh folder.

## 10.14 Current request

The user asked:

> Save all conversations in this chat to a file for a new chat to use.

This document is the resulting handoff.

---

# 11. Uploaded artifacts referenced in this thread

Chronological filenames:

1. `PHD_FABLE5_FINAL_RESTART_PS51_FIXED_2026-07-24(3).zip`
2. `PHD_FABLE5_FINAL_RESTART_PS51_FIXED_2026-07-24(5).zip`
3. `PHD_HALL_COIL_HYBRID_RADIATION_CLAUDE_2026-07-27(1).zip`
4. `P_FIXED (2).zip`
5. `06_Frontier_Idea_Research_2026-07(4).zip`
6. `image(16).png`
7. `02_Startup(1).zip`
8. `image(17).png`
9. `06_Frontier_Idea_Research_2026-07(6).zip`
10. `02_Startup(2).zip`
11. `image(18).png`
12. `PHD_ALIGN_POWER_PILOT_FULL_FIXED_V2.zip` — latest authoritative package

Earlier intermediate packages mentioned in the workspace or conversation
included:

- `PHD_STARTUP_ALIGN_CLAUDE_2026-07.zip`
- `PHD_ALIGN_CONTINUE_V2.zip`
- `PHD_ALIGN_STAGE10_FIX_V3.zip`
- `PHD_ALIGN_POWER_FULL_2026-07.zip`
- `PHD_ALIGN_POWER_PILOT_FULL_2026-07.zip`

Those are historical. Do not use them instead of the V2 fixed package.

---

# 12. What the next chat should do

## If the user has not run V2 yet

Tell the user to extract V2 into a fresh short path, enter the folder containing
`START.ps1`, and run the single command. Do not ask them to layer the ZIP over
an old directory.

## If V2 starts correctly

Help interpret:

- launcher regression output;
- package validation;
- nine pilot routes;
- Folder 06 Fable comparison;
- stage logs and outputs;
- any normal pause caused by usage/authentication rather than a code defect.

## If V2 stops

Ask for:

1. the full console text beginning at the first `====` section;
2. `state\CHATGPT_HANDOFF.md` if it exists;
3. the current `state\attempts\<stage>.json` if a research stage began;
4. the newest `stderr.txt` only if it is nonempty.

Distinguish:

- launcher/package defect;
- Claude authentication/availability/usage issue;
- Fable final-result policy event;
- ordinary runtime interruption;
- stage-output acceptance failure.

Do not call an ordinary schema failure a security downgrade. Do not count
auxiliary Haiku or Opus use as a Fable downgrade if Fable produced the accepted
final result.

If a package code defect is confirmed, rebuild and validate another full
standalone package. Do not provide another patch ZIP.

## If the research completes

Create reader-friendly results in two forms:

1. a faithful detailed account of the outputs;
2. a plain-language version explaining the conclusions, limitations,
   evidence, recommended PhD sequence, startup alignment, specialized-power
   options, shared skills, and next experiments.

Clearly separate:

- evidence-supported conclusions;
- model judgment;
- unresolved hypotheses;
- required physical experiments;
- startup opportunities that genuinely align with the PhD;
- attractive ideas that would require an effectively separate career track.

---

# 13. Communication preferences

- Lead with the answer and concrete evidence.
- Use plain language for explanations while preserving technical accuracy.
- The user values tables for model/effort routing and comparisons.
- The user wants source quality and reliability checked rather than assuming
  every source in an archive is acceptable.
- The user repeatedly invokes web search and expects current claims to be
  verified.
- The user wants accuracy but is cost-conscious.
- Do not make the user repeat long console diagnostics already preserved.
- Do not reassure vaguely; identify the precise failure and the exact next
  action.
- The user has spent significant time on failed packages. Minimize manual
  steps and avoid speculative repair cycles.

---

# 14. Compact new-chat starting prompt

The user may paste this after attaching this handoff and the latest ZIP:

```text
Read CHAT_HANDOFF_HALL_COIL_STARTUP_2026-07-27.md completely and treat its
"Current authoritative state" as binding. Continue the Hall/coil PhD,
Folder 06, startup, and specialized-power workflow from the latest state.
Do not give me another patch package. Preserve the one-command Windows
PowerShell 5.1 workflow, Fable 5/xhigh final-result policy, model/effort and
performance logs, two-strike Fable handling, checkpoints, Windows-safe paths,
all-stage pilot, and Folder 06 Fable verification. The current authoritative
ZIP is PHD_ALIGN_POWER_PILOT_FULL_FIXED_V2.zip. First determine whether I am
reporting a new run result, an error, or asking for analysis, and act directly
without making me repeat the earlier history.
```

END OF HANDOFF
