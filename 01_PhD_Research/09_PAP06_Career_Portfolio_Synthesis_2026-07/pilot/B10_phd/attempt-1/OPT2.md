# OPT2 — Future continuation direction (PILOT)

**PILOT SAMPLE — NOT FINAL**

This document represents, at pilot scope only, the "Opt2" continuation
direction as defined by `workflow/stages/B10_phd.md`:

1. calibrate/validate a Hall sensor as an uncertainty-bounded instrument;
2. integrate Hall plus inductive coils as a hybrid diagnostic;
3. deliver a reusable module plus simulation/reconstruction package.

Per the B00 inventory handoff, the literal string "Opt2" does not appear
inside `sources/phd`; it is this workflow's label for the subject matter
of `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/`,
which per that same inventory has completed 10 of 12 planned stages (25
output files) and has **not** produced `70_redteam` or `80_synthesis`
outputs. Every claim below drawn from folder 08 is marked accordingly:
it is the corpus's own pre-redteam, pre-synthesis material, not a
finished, adversarially-checked conclusion. This pilot extracts five
representative claims (C06–C10 of `PHD_FACTS.json`) across the three
elements; it does not attempt full coverage.

## Element 1 — Calibrate/validate a Hall sensor as an uncertainty-bounded instrument

**Status: proposed, not demonstrated (C06).** A bench absolute-calibration
program ("WP-C") is documented: a Helmholtz-coil field source with a
triangulated coil constant (target u(k)/k ≤ 2%), bipolar DC calibration
(target m ± ~2% absolute, <0.5% linearity), a GUM/Monte-Carlo uncertainty
budget, and Allan-variance drift characterization. This plan is gated
behind closing the open ~109× bench-emulator anomaly (C04 in
`PHD_FACTS.json`) — the corpus's own stated rule is "no calibration work
starts before this." No calibration of the real (non-emulator) device has
been performed. Source: `sources/phd/P/01/06/outputs/FINAL_EXECUTIVE_STRATEGY.md`
§4 item 3; `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/outputs/06_INTEGRATED_RESEARCH_PROGRAM.md`
§3.2.

## Element 2 — Integrate Hall plus inductive coils as a hybrid diagnostic

The extraction rules require absolute calibration, mutual consistency,
bandwidth fusion, and radiation compensation to be kept as **distinct**
claims. Absolute calibration is Element 1's own claim above (C06). The
remaining three are represented here by C07–C09, each **proposed or
inferred, never demonstrated**:

- **Mutual consistency (inferred, C07).** Hall→coil correction of the
  coil's integrator drift is hardware-proven outside fusion and deployed
  at system level (ITER OVSS) per the corpus's cited literature. Coil→Hall
  is only conditionally feasible for gain (needs a trusted coil chain plus
  real field excursions) and can **never** deliver Hall offset — offset
  needs zero-field epochs or an external absolute reference. If both
  channels drift simultaneously and unreferenced, the pair can only detect
  that they disagree, not attribute which one moved. **The source
  explicitly rejects the symmetric phrase "the sensors calibrate each
  other" as misleading without these conditions attached, and states no
  hardware demonstration of the coil→Hall direction exists in fusion
  conditions.** Mutual agreement alone is not automatic absolute
  calibration.
- **Bandwidth fusion (proposed, C08).** The Hall channel is proposed to
  supply DC/low-frequency field content the coil structurally cannot see;
  an embedded calibration-winding injection is proposed to sit in an
  "overlap band" (above drift band, below the Hall pole, inside the coil's
  flat response) so injection near/above the Hall pole can identify Hall
  dynamics. No bandwidth-fusion hardware test exists yet, and it depends
  on a still-unverified Hall bandwidth figure (see PHD_FACTS.json C05).
- **Radiation compensation (proposed, C09).** A layered "anchored hybrid"
  architecture (machine-current/vacuum-field anchors + zero-field offset
  epochs + optional embedded-winding gain tracking + a top-tier
  material-diverse witness Hall die) is proposed to separate
  temperature-driven from radiation-driven drift. Radiation qualification
  work is explicitly collaborator-led, never on the HSX critical path, and
  never claimed as an experimental result in first-author work. The
  GaN/AlGaN radiation-drift magnitude is stated as **Unknown**: no
  GaN/AlGaN Hall-plate neutron dataset exists in the literature reviewed.

## Element 3 — Deliver a reusable module plus simulation/reconstruction package

**Status: proposed, not built (C10).** A reusable simulation/estimator
software package ("T0") is specified with a fixed module boundary
(model/schema/estimator/faults/scenarios/metrics/report/tests), a frozen
scientific core that may not change without a new stage-20-class review,
and a regression binding to an existing analysis tool
(`tools/observability_rank_tests.py`). It is proposed to be built
incrementally and frozen at manuscript submission (~Q1–Q2 2027), released
with that publication. No code has been built yet as of the cited
documents. Source:
`sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/outputs/03_SIMULATION_AND_VALIDATION_PLAN.md`
§11.

## Proposed-vs-demonstrated discipline (this pilot's application)

All five Opt2 claims (C06–C10) are status `proposed` or `inferred`, never
`demonstrated`. The only demonstrated technical result touching this
territory in the pilot's ten claims is the bench-emulator offset
cancellation (C03) and its companion open anomaly (C04) — both explicitly
scoped as emulator-based, not device calibration, and not part of the
hybrid or radiation-compensation architecture itself.

## What the full run must add

- **Hypotheses.** The full run must state each Opt2 element's testable
  hypothesis explicitly (this pilot only extracts the architecture and
  feasibility claims already written in the corpus; it does not
  reformulate them as a hypothesis register).
- **Experiments.** The full run must enumerate the falsification-test
  ladder (the corpus's own FT-01…FT-12 items, referenced but not
  individually extracted here) with acceptance metrics and cost class for
  each.
- **Deliverables.** The full run must map each element to its target
  publication(s) (the corpus's own P1–P4 map) with dependency and gate
  detail, not just the module boundary extracted here.
- **Dependencies.** The full run must extract the full gate/dependency
  graph (the corpus's own DG-00…DG-11 sequence) linking Element 1's
  calibration gate to Element 2's hybrid gates and Element 3's freeze
  date — this pilot cites individual gates inline but does not reproduce
  the graph.
- **Kill criteria.** The full run must extract the corpus's own numbered
  kill criteria (K1–K10) and stop/pivot rules in full; this pilot
  mentions only the calibration precondition ("no calibration before the
  anomaly closes") and the collaborator-gating rule for radiation work.
- **Uncertainties.** The full run must extract the corpus's own named
  single-source dependencies (e.g., the coil→Hall gain-tracking precedent
  and the radiation-null witness result each rest on one cited source)
  and the corpus's own uncertainty-budget structure (§6.3 of the
  radiation-compensation architecture document) in full, rather than the
  summary-level limitations recorded per claim in this pilot.
- **Redteam status.** The full run must explicitly track that folder 08
  has not yet produced its own `70_redteam`/`80_synthesis` outputs, and
  should re-extract once (or flag prominently if) that gap is closed
  before treating folder-08 material with the same confidence as
  folder-06 material.
