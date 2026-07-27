# 00 — Conflict ledger (Stage 00)

Prepared by: Claude Code, stage `00_inventory`, requested model Sonnet 5 /
High. Each entry states the conflicting sources, the practical impact, and
a resolution/rationale. None of these resolutions asserts a new technical
conclusion about calibration, radiation compensation, or application
priority — those remain for stages 20/30/40/50/60.

---

## C1 — Original user request wanted an automatic Codex/MCP fallback; this mission (like folder 06) implements manual-only pause

**Sources in conflict:**
- `06\inputs\ORIGINAL_REQUEST.txt` (the only verbatim user-request text found
  in this provenance chain): *"If downgrade of fable 5 occur for the first
  time, I would like you to pause, regenerate prompt a try again with fable
  5. If downgrade occur again, use codex (mcp) 5.6 sol with corresponding
  efforts... If Claude code does not response after 20 minutes. Automatically
  switch to codex for further operations with equivalent models."*
- This mission's `CHECKPOINT_PROTOCOL.md` ("Second failure... No silent
  provider fallback"), `MODEL_POLICY.md` ("No silent provider or model
  substitution"), `AGENTS.md` ("Do not invoke another AI provider or
  external agent runtime"), and `OFFICIAL_SETUP_REFERENCES.md` (runner
  passes `--disallowedTools mcp__*`) all implement: first failure → clarified
  Fable retry; second failure → quarantine, checkpoint, and pause for manual
  review; no automatic external-provider call; no 20-minute inactivity
  auto-switch (`inactivity_timeout_enabled=$false` in the runner's own
  handoff-state schema).

**Impact:** if a second Fable-integrity failure or a long stall ever occurs,
this mission will **not** automatically continue on Codex/MCP as the user's
original text requested — it will stop and wait for the user.

**Resolution:** honor this mission's own written policy. `AGENTS.md`
(mirrored in `prompts\_shared_system.md`) states that "the files in this
mission, not prior chat memory, are authoritative," and MCP invocation is
disabled at the CLI-argument level, not merely by convention — there is no
mechanism inside a stage session to reach Codex even if instructed to. This
is not a new deviation introduced by this mission; it exactly mirrors
folder 06's own documented conflicts C3/C4
(`06\outputs\00_CONFLICT_LEDGER.md`, restated in
`06\outputs\FINAL_EXECUTIVE_STRATEGY.md` §8 and
`06\outputs\FINAL_AUDIT.md` R012/R013 as "DEVIATED BY DESIGN (documented)").
**Flagged for the user's awareness, not resolvable inside a research
stage** — if automatic cross-provider fallback is still wanted, it requires
a runner/policy change outside this mission's write boundary.

---

## C2 — Root `01\CLAUDE.md`'s escalation-ladder exemption names folder "06" but not "08"

**Sources in conflict:**
- Root `01\CLAUDE.md`: *"The root default is Sonnet at high effort. The
  autonomous mission under `06` always passes an explicit stage model and
  effort, so do not override its Fable/Sonnet allocation."*
- This mission (`08`) is a structurally identical autonomous,
  PowerShell-runner-driven mission with its own `EXECUTION_PLAN.md`/
  `MODEL_POLICY.md` stage-model table, but the root file's exemption
  sentence was not literally updated to name `08`.

**Impact:** read literally, the root escalation ladder (intended for
interactive sessions launched by Tim directly) could be misapplied to
override this mission's per-stage model assignments, contradicting
`MODEL_POLICY.md`'s explicit routing table and the runner's hard-coded
`--model`/`--effort` arguments.

**Resolution:** this mission is evidently the same class of "autonomous
mission" the root file already carves out an exemption for — same runner
pattern, same durable-state/checkpoint design, same per-stage model/effort
table format, produced as a direct extension of the `06` package per this
mission's own `README_START.md` ("It extends folder `06`; it does not
overwrite it"). Treated as covered by the same exemption. This is a root
documentation gap, not a substantive conflict; recommend the user update
root `01\CLAUDE.md` to read "the autonomous missions under `06` and `08`"
for clarity. No stage in this mission should apply the interactive
escalation ladder to override `EXECUTION_PLAN.md`/`MODEL_POLICY.md`.

---

## C3 — Folder 06's topic-tag taxonomy does not map 1:1 onto this mission's four topic quotas

**Sources in conflict:**
- `06\outputs\01_SOURCE_COVERAGE.md` §5: seven topic categories (WBG Hall/
  device physics 77; Hall-sensor geometry/sensitivity/offset/noise/
  bandwidth/temperature/radiation/packaging/calibration 117; fusion
  diagnostics 133; stellarator/HSX 73; direct-vs-inductive/drift 109;
  uncertainty/calibration-traceability 59; low-fabrication novelty 65).
  There is no standalone "radiation" category.
- This mission's `SOURCE_POLICY.md`: four topic quotas — hybrid/coil/
  integrator/sensor fusion (25), radiation/irradiation (30), applications/
  alternatives (25), calibration/observability/uncertainty (20).

**Impact:** stage 10d cannot simply re-read `06`'s topic tags and remap them
arithmetically to this mission's quotas; the category boundaries differ
(most importantly, `06` has no isolated radiation bucket at all, which is
consistent with `06`'s deliberate out-of-scope treatment of radiation, not
an oversight).

**Resolution:** not a substantive contradiction — it is direct evidence for
why this mission exists (radiation was deliberately scoped out of `06` per
root `01\CLAUDE.md` and `06\MISSION.md`). Stage 10d must independently tag
every row against this mission's own `SOURCE_POLICY.md` quota definitions
rather than reuse or infer from `06`'s tags. This is recorded as a data
point in `00_INPUT_INVENTORY.md` §3.2, not treated as a defect in `06`.

---

## C4 — Folder 06 endorsed hybrid Hall+coil fusion (WP-D) as feasible by literature precedent; this mission's DECISION_FRAMEWORK.md requires an independent identifiability derivation

**Sources in conflict:**
- `06\outputs\02_RESEARCH_DIRECTION_DECISION.md` §3.2 and the WP-D row of
  its work-package table cite tokamak-side Kalman-filter coil+Hall
  data-fusion papers (KSTAR, COMPASS-U/JET lineage — the same two 2025
  papers seeded in this mission's `LITERATURE_SEEDS.md`) as "precedent/
  template" and conclude WP-D is a viable, campaign-uncoupled work package.
  No observability, rank, or structural-identifiability derivation for the
  specific Hall-gain/bias vs. coil-gain/integrator-drift confounding
  problem appears anywhere in `06`.
- This mission's `DECISION_FRAMEWORK.md`: *"The architecture is not accepted
  merely because one channel measures DC and the other measures AC.
  Determine the rank/observability or structural identifiability of the
  augmented state under each scenario."* This folder's `CLAUDE.md` states
  the same requirement even more strongly: *"Do not call mutual calibration
  feasible until the relevant state/parameter observability or
  identifiability condition is shown."*

**Impact:** if stage 20 (or any later stage) simply cited `06`'s WP-D
endorsement as already having answered the identifiability question, it
would be treating feasibility-by-precedent (an inference from other
facilities' successful Kalman fusion) as equivalent to a derived
observability proof for this specific architecture — exactly the shortcut
`MISSION.md` warns against: *"Redundancy does not automatically reveal
which device drifted."*

**Resolution:** not a contradiction between `06` and this mission — a scope
difference. `06`'s WP-D endorsement is a legitimate stage-20-of-06-level
conclusion (feasible enough to plan a bench-only work package around,
which is what that mission needed), but it is not this mission's stage-20
deliverable. Stage 20 of *this* mission must independently derive (or
falsify) the observability/identifiability condition per scenario before
any claim of "mutual calibration is feasible" may be repeated or
strengthened. `06`'s WP-D conclusion may be cited as motivating precedent,
never as a substitute for the derivation.

---

## C5 — The user's three-phase hypothesis for this mission is only partly a restatement of folder 06's conclusions

**Sources in conflict:** see `00_INPUT_INVENTORY.md` §2 for the full
evidentiary comparison. Summary: (a) "Hall validation first" is backed by a
genuine hard gate in `06` (G1/WP-C before calibration claims); (b)
"hybridization second" holds only as a paper-numbering label — `06`
explicitly permits WP-D/P2 to draft in parallel with P1's review and even
to proceed on synthetic/2025 data as a named fallback, i.e., not strictly
serial; (c) "reusable module and simulation package third" has no textual
precedent anywhere in `06` — `06`'s third paper (P3) is the RSI
vector-probe **hardware** instrument paper, not a software module/
simulation package.

**Impact:** if later stages treated the user's three-phase framing as
already validated by `06`, they would be retrofitting a conclusion to fit
a hypothesis rather than testing it — the exact failure mode
`MISSION.md` warns against.

**Resolution:** classified per sub-claim in `00_INPUT_INVENTORY.md` §2 as
CONFIRMED (2.1) / PARTLY CONFIRMED (2.2) / NOT CONFIRMED (2.3). Stage 60
(`60_research_program`) must independently decide and justify the actual
recommended sequence and deliverable structure for this mission, treating
both the user's framing and `06`'s paper order as candidate hypotheses,
not settled premises.

---

## C6 — Practical constraint: DECISION_FRAMEWORK.md's radiation-scenario reference requirements exceed what Tim's own HSX program can supply

**Sources in conflict:**
- This mission's `DECISION_FRAMEWORK.md` "Radiation exposure" scenario row
  requires, as a candidate reference: *"embedded calibration coil,
  dosimetry, material-diverse reference."* `SOURCE_POLICY.md`'s "Radiation
  discipline" section requires recording particle/species, fluence/dose,
  dose rate, temperature, bias state, and annealing/time-after-exposure —
  the vocabulary of an actual irradiation facility campaign.
- Root `01\CLAUDE.md` scope rule: *"No neutron/gamma radiation experiments
  are planned"* for Tim's experimental (HSX) work; this mission's own
  `MISSION.md` boundary condition: *"The user's current first-author HSX
  work does not automatically acquire a radiation-test requirement...
  Radiation can remain a later, coauthored, or collaborator-led work
  package."*

**Impact:** stage 30's radiation-compensation architecture must be
specified in enough operational detail to be useful (per
`SOURCE_POLICY.md`'s discipline), while simultaneously never implying that
Tim's own HSX program will supply the irradiation facility, dosimetry, or
exposure campaign needed to validate it.

**Resolution:** not a contradiction — a scoping instruction. Stage 30 must
produce an architecture and simulation/validation plan written as a
*specification* (what a collaborator, facility, or the co-authored
TCAD-adjacent effort would need to execute), explicitly labeled proposed
[PX]/inferred, never as a claim that Tim will personally run an
irradiation campaign. This is consistent with, not opposed to, root
`01\CLAUDE.md`'s trajectory item 4 (the separate co-authored TCAD radiation
paper, simulation-only) and should be cross-referenced there rather than
duplicated as new experimental scope.

---

## Summary

Six conflicts identified, none blocking this stage's completion:

| ID | Type | Blocking? | Owner of resolution |
|---|---|---|---|
| C1 | Original request vs. implemented policy | No — documented, inherited from 06 | User/advisor, if automatic fallback is still wanted |
| C2 | Root-file documentation gap | No — resolved by evident intent | User (optional root-file edit) |
| C3 | Taxonomy mismatch between 06 and 08 | No — expected, not a defect | Stage 10d (independent re-tagging) |
| C4 | Precedent vs. derivation (identifiability) | No — clarifies stage 20's actual job | Stage 20 |
| C5 | User hypothesis vs. 06's actual conclusions | No — clarifies stage 60's actual job | Stage 60 |
| C6 | Architecture detail vs. no-radiation-experiment scope | No — a specification/labeling discipline, not a scope violation | Stage 30 |

No conflict required modifying any sibling file, and none asserts a new
technical conclusion about calibration feasibility, radiation compensation
design, or application priority.
