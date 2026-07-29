# Stage 00 — Conflict ledger

Every material contradiction or ambiguity found while building the Stage 00
baseline is recorded below. None is resolved by convenience; each entry
either names the controlling evidence or is explicitly labeled unresolved.

---

## C1 — "Published in 2023" vs. the supplied 23-Jul-2026 decline letter (the mission's named priority conflict)

**Conflicting claims:**

- Parent root `../CLAUDE.md`: *"2023 — IEEE Sensors Letters (1st author,
  published): AlGaN/GaN Hall sensor deployed in-vessel in HSX; 68 shots;
  voltage-biased, uncalibrated..."*
- Parent folder index `../01_Folder_Info.md`: *"Research arc:
  ... Demonstrated in-situ (2023 Letters) → calibrated spinning-current
  readout..."*
- `../02_HSX_Hall_Sensor_Readout/CLAUDE.md`: *"This system supersedes the
  voltage-bias, uncalibrated readout of the 2023 IEEE Sensors Letters
  deployment."*
- `../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`
  treats the 2023 paper as a closed, published prior work throughout §1.
- The manuscript file itself (`../01_Publications/submitted/regular_lsens/
  regular_lsens.tex`) carries an unedited IEEE class-template copyright
  string, `1949-307X (c) 2023 IEEE...`, near line 438, and a separate copy at
  `../01_Publications/tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX_2023.pdf`
  carries a "_2023" filename suffix.

**Contradicting primary evidence (supplied in `inputs/`):**

- `inputs/IEEE_submission_bundle_2026-07-02.pdf` — Atypon ReX submission
  export, "PDF Generation 02 Jul 2026 18:55:21 EST," Submission ID
  `b16111d9-5cc0-4019-a52d-6a06d1bf6edb`, Manuscript ID
  `SENSL-26-07-RL-1061` — proves the manuscript was **submitted 2 July 2026**.
- `inputs/Decision_Letter_IEEE_2026-07-23.pdf` — IEEE Author Portal export,
  letter dated **23-Jul-2026**, email sent "22 July 2026 at 18:13 GMT-7,"
  from `sensl-admin@ieee.org`, signed by AEIC Dr. Giacomo Langfelder —
  states the manuscript was reviewed and **declined**, with an invitation to
  revise and resubmit under a new manuscript ID.
- The manuscript's own DOI and Associate Editor fields are **blank**
  (`regular_lsens.tex` lines ~389–390).
- No acceptance letter, proof, DOI record, or publisher page for any 2023
  (or any other) accepted/published version was supplied anywhere in
  `inputs/` or the parent tree.

**Assessment / controlling evidence:** The IEEE Author Portal decision
letter and Atypon ReX submission bundle are primary-source,
platform-generated records with internal dates, IDs, and sender/recipient
metadata that are internally consistent with each other (same manuscript
title, same Manuscript ID `SENSL-26-07-RL-1061`, submission-then-decision
sequence 2-Jul-2026 → 23-Jul-2026). They **control**: as of the evidence
supplied to this mission, the manuscript was submitted in July 2026 and
declined (not accepted) on 23-Jul-2026. It has **not** been shown to have
been published in 2023 or at any other date. The "2023" appearing in the
parent `CLAUDE.md`, the folder index, project 02's `CLAUDE.md`, the
`_2023` filename suffix, and the IEEE template's boilerplate copyright
string are all most plausibly explained as (a) an unedited LaTeX
class-template artifact and (b) a parent-project narrative that was written
before, or without reference to, the actual 2026 submission/decision
timeline — not as independent corroborating evidence of an actual 2023
publication.

**Status:** Not resolved by this stage — the parent root memory's "2023,
published" framing is **flagged as unsupported by supplied evidence** and
should not be treated as fact by later stages (`20_direction`, `30_manuscript`,
`60_timeline`, and especially any claim of prior peer-reviewed publication in
`80_synthesis`). This mission does not have write access to correct
`../CLAUDE.md` or `../01_Folder_Info.md` (they are outside the
mission folder), so the user should be told directly that the parent-level
project memory contains this unverified claim.

## C2 — Project 03's RSI plan silently inherits the same unverified "closed, published" framing

`../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`
§1 builds its entire narrative arc — and its "first absolutely calibrated...
upgrading 2023's 'temporal correlation' to numbers with uncertainties" thesis
statement — on the assumption that the 2023 Sensors Letters paper is
finished, published prior work. Per C1, that assumption is unverified.

**Status:** Unresolved. This does not invalidate project 03's engineering
plan, but stage `30_manuscript` (which must compare "revise Sensors Letters"
vs. "arXiv + RSI") must independently re-derive the publication-route
comparison from the decision letter, not from project 03's own framing,
since project 03's framing already assumes one branch of the comparison
(Sensors-Letters-is-done) that the primary evidence contradicts.

## C3 — Automatic Codex/MCP fallback (as originally requested) vs. the implemented manual-only continuation

**Original user request** (`inputs/ORIGINAL_REQUEST.txt`, paragraph 6):
*"If downgrade of fable 5 occur for the first time, I would like you to
pause, regenerate prompt a try again with fable 5. If downgrade occur again,
use codex (mcp) 5.6 sol with corresponding efforts."*

**As actually governed by this mission's own files:**
- `CLAUDE.md` (mission contract): *"Do not invoke another AI provider or
  external agent runtime."* / stage instructions: *"Do not invoke another AI
  provider, external agent CLI, or MCP server."*
- `MODEL_POLICY.md`: on a second Fable-integrity failure, "Claude stops and
  writes `CHATGPT_HANDOFF_REQUIRED`" — a **manual** continuation in the
  ChatGPT Windows desktop app, not an automatic Codex/MCP call.
- `../CLAUDE_ONLY_MIGRATION_2026-07-24.md` documents that MCP/Codex runtime
  files (`CODEX_MCP_CLIENT.ps1`, `TEST_MCP_CONNECTION.ps1`,
  `INVOKE_CODEX_EXEC_CHILD.ps1`, `.mcp.codex.json`) were **deliberately
  removed** from this package: *"The PowerShell workflow now invokes Claude
  Code only. It never calls another AI provider and contains no active MCP
  server configuration."*
- `../FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md` restates: *"No Claude-to-
  Codex call, MCP runtime, or automatic alternate-provider route is
  enabled."*

**Assessment:** This is a **documented, deliberate deviation** from the
user's literal original request, made at mission-packaging time (dated
2026-07-24, the same day as this run) — not a silent omission. The
mission's own governing files are internally consistent with each other on
this point and postdate the original request, so they control *current
operating behavior*. However, the ledger records this as a conflict rather
than silently accepting it, because the user-facing original request and
the currently governing policy genuinely disagree, and it is not this
stage's role to decide whether the user re-confirmed that change.

**Status:** Named-evidence conflict, not silently resolved. `CLAUDE.md`,
`MODEL_POLICY.md`, and `CLAUDE_ONLY_MIGRATION_2026-07-24.md` control
*current execution behavior* (no automatic external-provider calls will be
made by this or any later stage in this run). The discrepancy from the
user's original literal ask should be surfaced to the user in the final
synthesis, not silently treated as if the user asked for manual-only
fallback from the start.

## C4 — 20-minute auto-switch-to-Codex request vs. disabled inactivity timeout

**Original user request** (`inputs/ORIGINAL_REQUEST.txt`, paragraph 8):
*"If Claude code does not respond after 20 minutes. Automatically switch to
codex for further operations with equivalent models."*

**As actually implemented:** `state/PROJECT_STATE.md` — *"Inactivity
timeout: disabled; the user may stop PowerShell manually."* No file among
`CLAUDE.md`, `MODEL_POLICY.md`, `EXECUTION_PLAN.md`, or
`CHECKPOINT_PROTOCOL.md` contains any elapsed-time-triggered
provider-switch logic.

**Status:** Same class of documented deviation as C3, for the same reason
(no-automatic-external-provider-call is a hard mission-contract rule). Not
silently resolved; recorded for the user's awareness. `CHECKPOINT_PROTOCOL.md`
substitutes a manual-interruption-safe design (durable per-event flushing,
so a manually closed PowerShell window loses no confirmed progress) as the
practical mitigation for the same underlying worry (a stuck/unresponsive
session), rather than an automatic timeout.

## C5 — Project 05's two internal status files disagree with each other

`../05_HSX_ChatGPT_Windows_App/outputs/FINAL_ACCEPTANCE_CHECKLIST.md`
(dated 2026-07-12) declares status `COMPLETE_WITH_OPEN_GATES` (with
fabrication/purchase release explicitly `FAIL/HOLD`), while
`../05_HSX_ChatGPT_Windows_App/state/PROJECT_STATE.md` (dated 2026-07-13,
one day later) shows `Mission status: IN_PROGRESS`, "Current stage: 50
cost-down corrected synthesis / IN_PROGRESS" — i.e., a revision pass was
opened after the "complete" checklist was written and was not closed out
in the supplied copy of the folder.

**Status:** Unresolved; not adjudicated here. Project 05 is outside this
mission's topical scope (mechanical/packaging design, not literature,
manuscript, or PhD strategy), so this is recorded for completeness per the
stage instruction to inspect the folder, not carried forward as load-bearing
evidence for later stages.

## C6 — "Calibrated" readout language (project 02) is aspirational, not achieved

`../02_HSX_Hall_Sensor_Readout/CLAUDE.md` and `docs/SPECS.md` describe the
2026 current-spinning system in language that reads as an accomplished
capability ("This system supersedes the voltage-bias, uncalibrated readout
of the 2023... deployment"; comparison table lists 2026 calibration as
"absolute, Helmholtz + in-situ"). The same folder's own `NOTES.md` and
`journal/2026-07-08_spinning_emulator_20mA.md` show only: a resistor-ring
emulator bench test (not the real GaN die), a demonstrated offset-
cancellation result, and an explicit, unresolved ~109× magnitude anomaly
with the instruction "don't calibrate to these magnitudes yet." No
Helmholtz-coil calibration run, coefficient, or report exists anywhere in
the folder.

**Assessment:** The journal/NOTES.md bench log is the controlling evidence
for *current state* (nothing dated after 2026-07-08 exists); the CLAUDE.md/
SPECS.md "supersedes...calibrated" language describes the **target design**,
not a completed calibration.

**Status:** Flagged so that `20_direction` and `40_experiment` do not
inherit "calibrated" as an accomplished fact for the 2026 single-axis
system. It is a design target with one resolved sub-result (offset
cancellation demonstrated on an emulator) and one open blocker (the
magnitude anomaly).

## Non-conflicts checked and found consistent (recorded to show the search was performed)

- Manuscript gain/bandwidth claim ("total voltage gain of 200 V/V and a
  bandwidth of 1 MHz," `regular_lsens.tex` line 483) is consistent with
  `../02_HSX_Hall_Sensor_Readout/docs/SPECS.md`'s 2023-vs-2026 comparison
  table entry for the 2023 system ("INA849+2×OPA814 G=200, 1 MHz raw BW").
  No conflict.
- `inputs/INPUT_CHECKSUMS.sha256` matches all five recomputed SHA-256 hashes
  of the `inputs/` files exactly. No integrity conflict.
- The manuscript's shot numbers referenced in Fig. 4/5 (63, 65, 68, 21, 18,
  19) all have corresponding raw files in
  `../07_HSX_august2025_results/hsx_20250821/`. This is consistent with,
  but does not by itself independently prove, that the packaged zip is the
  exact dataset underlying the submitted figures (no per-figure
  reproduction was attempted in this stage).
