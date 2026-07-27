# 06 — Advisor meeting brief: Hall + coil hybrid program

Stage 60 (`60_research_program`), Fable 5 (xhigh). One meeting, ~20
minutes of agenda time; designed to ride the already-planned folder-06
advisor meeting (06-M01/M02), not to add a new one. Full detail:
`06_INTEGRATED_RESEARCH_PROGRAM.md` and
`06_DECISION_GATES_AND_ROADMAP.md`. ID conventions as there. Labels:
Observed / Derived / Inferred / Proposed / Unknown.

---

## 1. Decision requested (one sentence)

**Approve folding the hybrid Hall+coil work into the existing PhD plan
as a falsification-gated track: simulation/estimator core first, two
cheap hybrid bench tests added to the already-scheduled calibration
block, the calibration-winding layer and all radiation work behind
explicit go/no-go gates — with radiation collaborator-led, coauthored,
and never on the HSX critical path.**

Sub-decisions (5):

1. Adopt the refined sequence (T0 estimator first; FT-04/FT-05 added
   to the WP-C bench block; ~3–6 marginal bench-days total).
2. Frame P2 (the two-paper-floor second paper) as: identifiability
   theory + honesty-tested estimator + bench validation, claiming only
   the four documented gaps (C36) — not "we hybridized a Hall sensor
   with a coil," which is 26-year-old prior art (C01/C27/C29).
3. Gate tokamak outreach (IPP-Prague, KFE) on the bench result
   (HY-G1); approve the evidence-pack outline now, send nothing yet.
4. Keep radiation as a Phase-4 coauthored work package (TCAD-paper
   model): approach a radiation-effects group only after HY-G3, with
   a coupon-screening protocol, never a commitment on HSX work.
5. Freeze the simulation package at P2 submission (bounded module,
   fixed interface) — it is P2's artifact, not a software project.

## 2. Thirty-second technical summary (Derived, Stages 20–50)

A Hall sensor and a coil do **not** mutually calibrate: the
unreferenced pair has an exact two-parameter blind spot (Theorem 1 —
common-mode gain drift is indistinguishable from a real field change;
Hall offset is indistinguishable from a static field). What *is*
feasible: a calibrated Hall channel corrects coil/integrator drift
(hardware-proven elsewhere: CERN bench, ITER OVSS — C02), and, under a
trusted coil chain plus real field excursions plus external anchors,
the coil can track *relative Hall gain drift* — never offset (C11's
single non-fusion precedent; our bench test FT-05 decides it). All
absolute accuracy comes from anchors: HSX vacuum-shot machine-current
epochs + zero-field epochs + one traceable bench calibration. The
defensible thesis contribution is the identifiability theory plus the
first in-machine demonstration of the reverse direction on a
stellarator — a niche with zero prior literature (C32).

## 3. Evidence base (Observed)

- 219-source verified peer-reviewed ledger (215 verified), 37 typed
  claims, built and audited in this mission (stages 10A–10D); direct
  prior-art timeline 1999–2025 including two active 2025 competitor
  clusters on exactly our gap ([H001], [H002]).
- 18 failure modes, 12 falsification tests (10 radiation-free), 24
  radiation risks, all cross-referenced; every program gate below is
  one of those tests — nothing new was invented for this plan.
- Key hard facts: no GaN/AlGaN Hall-plate neutron dataset exists
  anywhere (C14); cross-species radiation scaling has failed at ~14×
  (C16); the JET radiation-hard Hall system ran 11.5 years /
  >19,000 pulses at 0.07 %-class stability but its same-die self-test
  is structurally blind to common-mode drift (C05).

## 4. What changes in the current plan: almost nothing (Derived)

- P1 (SENSL resubmission) — unchanged in scope and schedule.
- WP-C bench block — +2 tests (FT-04 offset-anchor validity ~1 day;
  FT-05 reverse-direction recovery ~2–3 days) using the same field
  source and transfer standard; one wound/PCB coil added to the BOM.
- WP-D (P2 desk work) — becomes the T0 simulation/estimator package
  with a pre-registered honesty test; same timeline (Aug–Dec 2026),
  stronger paper.
- Campaigns #1/#2 — hybrid items are piggyback-only (vacuum-shot
  anchors, repeated-waveform floors, EMI survey); no new machine-time
  request; a campaign slip degrades hybrid upside, never the P1/P2
  floor.
- Radiation — explicitly *removed* from the first-author path
  (confirming the existing scope rule), parked behind four gates and
  a future collaborator agreement.

## 5. Unresolved risks (honest list)

1. **C14 (Unknown):** GaN radiation-drift magnitude — unknowable
   without Phase-4 exposure; until then all cadence/threshold choices
   are provisional, bounded by labeled InSb/graphene analogs.
2. **Common-mode blindness (RR-13, irreducible):** between anchors,
   a shared gain drift of both channels is invisible in principle;
   we bound it by anchor cadence and report growing uncertainty —
   any reviewer told otherwise would be right to object.
3. **Single-source precedents:** the coil-calibrates-Hall direction
   ([H059]) and the metallic-Hall witness null ([R071]) each rest on
   one paper; FT-05 and FT-11(ii) test them rather than trust them.
4. **P2 novelty race:** two groups published fusion Kalman-fusion
   papers in 2025; our differentiator (joint identifiability with
   unknown gains + honest non-identifiability handling + stellarator
   demonstration) is documented as absent from their work — but the
   window is not indefinite.
5. **Schedule inheritance:** the whole bench sequence sits behind the
   ~109× anomaly closure (06-G1), exactly as the existing plan
   already requires.

## 6. Lowest-cost next experiment

**Zero-hardware:** FT-02, the estimator honesty test — the T0
simulator must *refuse* to recover parameters that are provably
non-identifiable (state freezing + inflated uncertainty on the
Theorem-1 scenarios) and must show prior-insensitivity on identifiable
ones. Pure desk work, already specified scenario-by-scenario; it gates
every dollar after it.

**First hardware:** FT-04, one bench-day — zero-field/180°-flip offset
reads against a fluxgate-audited zero. If offset anchoring fails,
the offset half of the calibration story is unsupported and no
winding or estimator can substitute (structural result) — we would
need to know that before writing P2's claims.

## 7. Questions for the advisor

1. Does the P2 framing (identifiability + honest estimator + bench
   validation, stellarator demonstration as the application) fit your
   view of the two-paper floor, given the 2025 competitor papers?
2. Bench-days: are ~3–6 marginal days inside the WP-C window
   acceptable, or should FT-05 wait for the post-P1 lull?
3. Outreach: comfortable with the HY-G1 gate before any IPP-Prague/
   KFE contact, and with leading that contact with our derivation
   (they are the closest competitors)?
4. Radiation collaborator: which relationship (existing TCAD
   coauthors? a UW/national-lab contact?) is the natural Phase-4
   partner when the time comes — and do you agree it stays coauthored
   and off the HSX critical path?
5. Module release: freeze-and-release the simulation package with P2
   (subject to the existing IP/disclosure gates), or hold it to the
   dissertation?
6. Any HSX operational constraint that would change the vacuum-shot
   anchor plan (≥2 field levels, ramp+flat-top, ≥3 epochs,
   between-shot zero-field reads)?

## 8. Bring to the meeting

1. This brief. 2. `06_INTEGRATED_RESEARCH_PROGRAM.md` (open at §1
verdict + §3.0 phase table + §6 tiers). 3.
`06_DECISION_GATES_AND_ROADMAP.md` (open at §1 gate table). 4.
`02_MUTUAL_CALIBRATION_FEASIBILITY.md` §1 (the plain-language verdict,
if the "why can't they calibrate each other" question comes up).
