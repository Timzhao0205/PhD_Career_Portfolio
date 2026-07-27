# 04 — Application and collaboration strategy

Stage 40 (`40_applications_collaboration`). Model/effort: Sonnet 5 (xhigh),
per `MODEL_POLICY.md` ("substantial judgment, but bounded by the
Fable-reviewed technical analysis"). Source IDs (`Hxxx`, `Rxxx`, `Pxxx`)
cite `outputs\01_SOURCE_LEDGER.csv`; claim IDs (`Cxx`) cite
`outputs\01_EVIDENCE_MAP.csv`; `CASE x` / gates `G0`–`G5` / tiers `T0`–`T3`
cite `outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md` and
`outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md`. Labels: **Observed /
Derived / Inferred / Proposed / Unknown** per `CLAUDE.md`.

**No contact, submission, or external write occurred in producing this
document.** Every "scientific ask" below is explicitly a non-sent outline,
labeled **PROPOSED, NOT SENT**, per `MISSION.md` and `AGENTS.md`.

---

## 1. Scope and inherited constraints

This stage does not re-derive technical feasibility; it applies the
vetoes already proven in stages 20 and 30 to six candidate application
lanes and scores what remains. Two hard constraints from prior stages
bind every judgment here:

1. **Stage 20 (Theorem 1):** an unreferenced Hall+coil pair can never
   identify absolute scale or Hall offset; only specific engineered
   anchors (machine-current + field model, zero-field epochs, embedded
   calibration winding, material-diverse witness) restore
   identifiability, and each anchor has a stated cost and failure mode
   (`02_MUTUAL_CALIBRATION_FEASIBILITY.md` §2–3).
2. **Stage 30 (§9.4, binding):** tiers T0–T2 (simulation, bench truth,
   self-test hybrid) involve no radiation exposure and constitute the
   complete architecture-validation content relevant to the user's
   current first-author HSX work. Tier T3 (environmental qualification)
   is collaborator-led and is **never** a prerequisite for any HSX
   deliverable. This stage's recommendations preserve that boundary: no
   application recommendation below asks the user to acquire a radiation
   experiment.

An application "wins" here only if it clears the calibration-path and
simpler-alternative vetoes stated in `DECISION_FRAMEWORK.md` — a large
market or a famous facility cannot override those vetoes (mission rule).

---

## 2. Scoring rubric (scale and weights)

`outputs\04_APPLICATION_SCORECARD.csv` has no `notes` column, so the
rubric is recorded here per the stage instruction ("show scoring
scale/weights in notes or the collaboration document").

Each of six sub-criteria is scored **0–5, 5 = most favorable**:

- `hybrid_value` — technical fit of the DC(Hall)+AC(coil) complementarity
  for this application (`DECISION_FRAMEWORK.md` criterion 2).
- `identifiability_path` — whether a stage-20 CASE anchor is realistically
  available (criterion 4).
- `radiation_fit` — whether the architecture's radiation-compensation
  contribution is actually relevant to this application's stressor
  (criterion 3). Where radiation is not the dominant/relevant stressor by
  design (e.g. the user's own HSX work, or a cryogenic-dominated
  application), this is scored **3/5 "neutral/not-applicable-by-design"**
  rather than penalized — absence of a radiation requirement is not a
  technical weakness for a lane that never needed one.
- `experimental_access` — realistic access within 24 months (criterion 6).
- `publication_value` — criterion 7.
- `collaboration_leverage` — criterion 8.

Two more sub-criteria are scored **0–5, but 5 = LEAST favorable** (highest
cost / highest risk) and are **inverted** (`5 − score`) before averaging:

- `prototype_cost` (criterion 9).
- `thesis_dilution_risk` (criterion 10).

Composite scores:

```text
technical_score  = mean(hybrid_value, identifiability_path, radiation_fit)
strategic_score  = mean(experimental_access, publication_value,
                         collaboration_leverage,
                         5 − prototype_cost, 5 − thesis_dilution_risk)
overall priority = mean(technical_score, strategic_score)   [ranking only]
```

Novelty-after-prior-art (criterion 5) is not a separate numeric column
because it acts as a **veto**, not a weight, in three of six lanes
(accelerator magnets C29, tacit in the "mature prior art" framing for
SC/HTS C28); per `DECISION_FRAMEWORK.md`, "a high score cannot override
… direct prior art that removes the proposed novelty." Vetoes are recorded
in the `veto` column and always win regardless of the numeric scores.

**Overall priority ranking (for reference; full justification per lane in
§4 and in `04_APPLICATION_SCORECARD.csv`):**

| Rank | Application | technical_score | strategic_score | veto |
|---|---|---|---|---|
| 1 | Stellarator field mapping (HSX-class) | 3.7 | 4.0 | none |
| 2 | Tokamak long-pulse | 4.0 | 3.4 | none |
| 3 | Accelerator magnets | 1.7 | 2.2 | yes — novelty (C29) |
| 4 | Superconducting/HTS magnets, motors/generators | 1.7 | 1.8 | yes — structural (C28) |
| 5 | Magneto-inertial fusion/plasma-jet | 1.3 | 1.0 | partial (C35) |
| 6 | Z-pinch/pulsed power | 1.0 | 1.2 | yes — no-advantage + no-path (C30) |

---

## 3. Ranked recommendation summary

| Rank | Application | Recommendation | Why (one line) |
|---|---|---|---|
| 1 | Stellarator field mapping | **Approach-now (internal)** | The user's own facility; zero external-access barrier; the necessary T1/T2 validation venue every other lane depends on. |
| 2 | Tokamak long-pulse | **Approach-after-bench-proof** | Strongest external precedent (C02/C27) and sharpest open gap (C06), but reverse-direction and radiation claims are unproven — needs a bench result first. |
| 3 | Accelerator magnets | **Monitor** (technique only) | Mature prior art vetoes the architecture (C29); the in-situ rotating-coil self-calibration technique (P057) is already absorbed by citation into stage 30 §5.5. |
| 4 | Superconducting/HTS magnets, motors/generators | **Monitor** (data only) | Structural veto (C28: coil blind to a static trapped field); cryogenic Hall temperature-coefficient literature (P050/P051) is reusable by citation. |
| 5 | Magneto-inertial fusion/plasma-jet | **Do-not-prioritize** | Probes already abandoned in the highest-stress region (C35); boundary niche unevidenced. |
| 6 | Z-pinch/pulsed power | **Do-not-prioritize** | Community solved redundancy without Hall (C30); no persistent DC baseline within a shot. |

---

## 4. Per-application detail

### 4.1 Stellarator field mapping — approach-now (internal)

This is not an "approach another group" case in the ordinary sense: the
execution venue is the user's own HSX facility and existing UW-Madison
collaboration (Goodman, Gallenberger, Geiger), already funded as projects
02/03. **Recommendation:** proceed with the planned HSX MVD hardware
install (target August 2026) as stage-30 tier T1; no outreach question is
gated on this stage.

- **Prerequisites (internal):** stage-30 **G0** (T0 simulation honesty
  test, in progress this mission) before **G1** (bench-repeatable
  anchored-hybrid calibration, ≥3 cycles within predicted uncertainty;
  `α_S`, `β_b` characterized).
- **External monitoring only:** the Wendelstein 7-X MHD Research Unit
  (IPP Greifswald, `outputs\04_COLLABORATOR_CANDIDATES.csv` rank 3) is a
  benchmarking-only candidate — no stated need for a Hall+coil hybrid
  exists in their literature (C32), so any future contact should be
  scoped narrowly to comparing trim-coil/error-field correction workflows
  after the user has an HSX-side G1 result to offer, not before.
- **Risk/fallback:** the main risk is treating this lane's low external-
  collaboration score (2/5) as a weakness — it is not; it reflects that
  the primary partner is already in place. If the HSX install slips past
  August 2026, the tokamak lane's "approach-after-bench-proof" gate slips
  with it, since G1 evidence is meant to be demonstrated here first.

### 4.2 Tokamak long-pulse — approach-after-bench-proof

**Recommendation:** do not approach yet. Reach stage-30 **G1** (ideally
using an HSX or public-tokamak CASE-D demonstration, ≥2 field levels plus
a ramp+flat-top segment, `02_OBSERVABILITY_AND_IDENTIFIABILITY.md` CASE D)
before any contact.

- **Staged prerequisites:** (1) G0 simulation pass including the
  non-identifiability honesty test T-NI; (2) G1 bench pass; (3) a written
  one-page technical note (not this stage's job to draft) stating the
  specific open gap being offered for discussion — the reverse-direction
  coil-informs-Hall claim (C06) and the common-mode-blindness limit
  (Theorem 1, C05 limitation) — so the approach leads with a contribution,
  not a request.
- **Non-sent scientific-ask outline (by candidate, full detail in
  `04_COLLABORATOR_CANDIDATES.csv` ranks 1, 2, 4, 5, 6):**
  - *IPP CAS Prague* (rank 1): compare their 11.5-year same-die self-test
    record (H003/H007, C05) against the stage-20 proof that same-die
    self-test cannot see common-mode drift; ask about their antimony-Hall
    program's (H065) calibration architecture as a design comparison.
  - *KFE/KSTAR* (rank 2): ask whether their 2025 Kalman-fusion framework
    (H001) has real-hardware validation or remains simulation-only (C09),
    and offer the stage-20 identifiability proof as a cross-check on its
    implicit known-gain assumption.
  - *PPPL/NSTX-U, ITER/ITPA, CEA/WEST* (ranks 4–6): lower-confidence,
    monitor-only until either NSTX-U exits its recovery project, a named
    WEST contact is identified, or an ITPA-adjacent venue becomes
    accessible through the user's advisor.
- **Risks:** (a) approaching before G1 risks presenting an unproven claim
  as settled — explicitly guarded against by gating on G1; (b) IPP-Prague
  and KFE are the closest thing to competitors on the C06 gap — leading
  with the user's own derivation, not a data request, mitigates this;
  (c) any conversation must not imply a commitment to radiation testing
  (T3 stays collaborator-led per stage-30 §9.4) — this is a hard
  boundary, not a negotiable framing choice.
- **Fallback:** if no tokamak group responds or a shared problem cannot be
  agreed, the tokamak-relevant identifiability claims remain fully
  supportable from the HSX/stellarator demonstration alone (rank 1);
  external validation strengthens but is not required for the
  dissertation-level claim.

### 4.3 Accelerator magnets — monitor (technique only), do-not-prioritize as application

**Recommendation:** do not approach as a collaboration target. The
architecture-level "Hall+coil hybrid" is not novel here (C29) — CERN,
FNAL, and HIAF already run Hall+rotating-coil+NMR as decades-old
production metrology, including in-situ rotating-coil self-calibration
(P057). This is the sharpest **novelty veto** in the scorecard, and no
score can override it (`DECISION_FRAMEWORK.md`).

- **What is still usable, with no contact required:** the in-situ
  rotating-coil self-calibration protocol (P057) already informed the
  triangle-closure consistency test in `03_RADIATION_COMPENSATION_ARCHITECTURE.md`
  §5.5 by citation. This is the model for how to extract value from a
  mature-prior-art lane without pursuing it as an application.
- **Non-sent scientific-ask outline (only if ever revisited):** a narrow
  question about the P057 protocol's uncertainty budget — not an
  application-level collaboration ask.
- **Risk:** none material, since no approach is recommended. CERN's own
  group-level micro-site could not be independently verified live this
  session (DNS failures on every `te-msc-*.web.cern.ch` variant tried;
  `04_COLLABORATOR_CANDIDATES.csv` rank 8) — recorded honestly rather than
  asserted, and irrelevant to the recommendation since no contact is
  proposed.

### 4.4 Superconducting/HTS magnets, motors/generators — monitor (data only), do-not-prioritize as application

**Recommendation:** do not approach as a collaboration target. A coil is
structurally blind to a static trapped field (no `dB/dt` once
magnetization completes) — the field's own accepted precision reference
for the persistent state is NMR, not a coil (C28). This is a **structural
veto**, not a low score to be improved with better instrumentation.

- **What is still usable, with no contact required:** cryogenic Hall
  temperature-coefficient literature (P050, P051, to 0.001 %/K by doping)
  is directly reusable as a design input to the `α_S` characterization
  task in `03_RADIATION_COMPENSATION_ARCHITECTURE.md` §2.1, already cited
  there.
- **Non-sent scientific-ask outline (only if ever revisited):** a narrow
  question to the Cambridge Bulk Superconductivity Group about
  temperature-coefficient characterization methodology — not the hybrid
  architecture, which does not apply in this regime.
- **Risk:** none material, since no approach is recommended.

### 4.5 Magneto-inertial fusion/plasma-jet — do-not-prioritize

**Recommendation:** do not pursue. Where the environment is most severe
(MagLIF load region), the field has already abandoned magnetic probes
entirely for optical (PDV, P031) or spectroscopic (Zeeman, P032) methods
— a hybrid sensor adds no survivability there (C35). A boundary/wall-
location niche at lower-field, single-shot devices is conceivable but
**wholly unevidenced** (Unknown, not a documented opportunity).

- **Fallback if ever revisited:** the boundary niche would need its own
  dedicated G0-equivalent simulation feasibility study before any
  hardware or outreach step — it cannot inherit gates from the
  stellarator/tokamak MVD plan, because no persistent-field anchor
  (CASE D analog) has been shown to exist at this timescale.
- **Access note:** LANL's Plasma Liner Experiment appears to be in an
  ownership/relocation transition as of a September-2025 secondary-source
  signal (unconfirmed on an official page; `04_COLLABORATOR_CANDIDATES.csv`
  rank 10) — a further reason not to prioritize near-term access planning
  here.

### 4.6 Z-pinch/pulsed power — do-not-prioritize

**Recommendation:** do not pursue. This lane carries the scorecard's
clearest **double veto**: "no credible advantage over a simpler
single-sensor solution" (the community already fused two inductive
sensors — B-dot + Rogowski, ±13–15 % — deliberately bypassing Hall, C30,
P025) and "no identifiable calibration path" (no persistent DC baseline
within a single ns–µs shot for any stage-20 CASE anchor). Hall-effect
current sensors are independently documented as EMI-susceptible (P028),
reinforcing rather than merely failing to rebut the incumbent's choice.

- **Risk/fallback:** none recommended; this lane is retained in the
  scorecard and candidate list only because the stage prompt requires
  Sandia Z/Mykonos to be evaluated by name, not because a path exists.

---

## 5. Cross-cutting risks

1. **Scope creep toward radiation testing.** Every "approach-after-
   bench-proof" recommendation above is scoped to algorithm/architecture
   discussion, never to a joint radiation-qualification commitment. Stage
   30 §9.4 and root `CLAUDE.md` both bind this: T3 stays collaborator-led,
   and the user's first-author HSX work never acquires a radiation
   requirement by association with these conversations.
2. **Competition/IP framing.** The two tokamak-lane approach-worthy
   candidates (IPP-Prague, KFE) are also the closest technical
   competitors on the mission's sharpest open gap (C06). Every proposed
   ask above is framed to lead with the user's own derived contribution
   (the stage-20 identifiability proofs), not a request to see unpublished
   work — this is the concrete mitigation, not merely a stated intention.
3. **Export control / classification.** Not evaluated in depth for the
   two do-not-prioritize national-lab lanes (Sandia, LANL) because no
   approach is recommended; flagged for completeness in
   `04_COLLABORATOR_CANDIDATES.csv` ranks 9–10 in case either lane is
   revisited later.
4. **Access-verification honesty.** Two candidate pages could not be
   independently confirmed live this session despite being genuine,
   search-indexed official pages: CERN's TE-MSC Magnetic Measurements
   micro-site (DNS failures from this environment) and the canonical
   `www.pppl.gov` domain (site-wide HTTP 403 to automated fetch, mitigated
   by a live Google Sites NSTX-U mirror). Both are recorded as
   unverified-this-session rather than asserted, consistent with
   `SOURCE_POLICY.md`'s access-level honesty rule and the stage-10C
   precedent (Lviv Polytechnic LSE page).
5. **Numeric figures carried from stage 10C remain unconfirmed at full
   text:** JT-60SA's 200 °C/9 MGy figures (P006) and the Rogacki et al.
   ppm/mrad precision figures (P054) are abstract/search-derived, not
   independently re-read — do not quote them as hard numbers in any
   downstream manuscript without re-verification.

---

## 6. Fallback path if no external collaboration materializes

The dissertation-relevant claims in this mission do not depend on any
external approach succeeding:

- The stellarator/HSX lane (rank 1) is fully self-contained (own
  facility, own data, own timeline) and alone supports the RSI (~Mar
  2027) vector-probe paper (project 03).
- The tokamak-lane identifiability claims (rank 2) are supportable from
  simulation (T0) and HSX-analog bench data (T1) alone; external
  validation from IPP-Prague/KFE would strengthen the novelty argument
  (C36) but is not required to state it.
- No recommendation in this document creates a dependency on Tier T3
  (environmental qualification) occurring, consistent with stage-30 §9.4
  and the root `CLAUDE.md` scope rule that no neutron/gamma experiment is
  planned for the user's first-author work.

---

## 7. Consistency statement

Every recommendation in §3–§4 traces to a veto or score already computed
in `outputs\04_APPLICATION_SCORECARD.csv`; no recommendation here
introduces a new technical judgment not present in that file. No
application-level veto proven in stage 20/30 (Theorem 1, CASE A/F,
common-mode blindness, C28, C30, C35) is relaxed by any collaboration or
publication-value consideration in this stage, per the binding instruction
in `40_applications_collaboration.md` ("scores do not override technical
vetoes"). No contact, submission, or external write occurred in producing
this document or the two accompanying CSVs.
