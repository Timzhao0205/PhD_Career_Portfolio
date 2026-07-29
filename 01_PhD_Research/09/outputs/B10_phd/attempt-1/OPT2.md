# OPT2 — Future continuation direction (FULL)

This is the full-run OPT2 artifact for stage `B10_phd`. It represents the
"Opt2" continuation direction as defined by `workflow/stages/B10_phd.md`:

1. calibrate/validate a Hall sensor as an uncertainty-bounded instrument;
2. integrate Hall plus inductive coils as a hybrid diagnostic;
3. deliver a reusable module plus simulation/reconstruction package.

Per the B00 inventory handoff, the literal string "Opt2" does not appear
inside `sources/phd`; it is this workflow's label for the subject matter
of `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/`,
which has completed 10 of 12 planned stages (25 output files) and has
**not** produced `70_redteam` or `80_synthesis` outputs — independently
reconfirmed this run by a direct Glob returning exactly 25 files. Every
claim below drawn from folder 08 carries that caveat. All claim IDs
(`Cxx`) resolve in `PHD_FACTS.json`.

## Element 1 — Calibrate/validate a Hall sensor as an uncertainty-bounded instrument

**Status: proposed, not demonstrated (C06).** A bench absolute-calibration
program ("WP-C") is documented: a Helmholtz-coil field source with a
triangulated coil constant (target u(k)/k <= 2%), bipolar DC calibration
(target m +/- ~2% absolute, <0.5% linearity), a GUM/Monte-Carlo
uncertainty budget, and Allan-variance drift characterization. This plan
is gated behind closing the open ~109x bench-emulator anomaly (C04) — the
corpus's own stated rule is "no calibration work starts before this." The
total bench/desk effort to a submittable Tier-1 package is estimated at
~19-29 bench-days (zero cleanroom steps), with nine unresolved inventory
gates named individually (I-1..I-9); the most consequential is that the
deployed 2025 module's post-campaign location and health are undocumented
anywhere in the corpus (C45). No calibration of the real (non-emulator)
device has been performed.

**Distinct sub-elements inside Element 1, kept apart per the extraction
rule:**

- **Absolute calibration itself (C06).** A traceable Helmholtz-coil bench
  standard, not the coil-only anchor discussed under Element 2's mutual
  consistency below (which is an in-machine cross-check, not a metrology
  root).
- **Estimator honesty as a precondition (C31, C48).** Before any hardware
  calibration claim is trusted, the corpus's own proposed falsification
  test FT-02 requires the eventual estimator to freeze states and inflate
  reported uncertainty on scenarios the theory proves are
  non-identifiable, rather than silently converging on the prior — the
  corpus states this single, zero-hardware, desk-only test "gates every
  dollar after it."

Source: `sources/phd/P/01/06/outputs/FINAL_EXECUTIVE_STRATEGY.md`
(WP-C calibration core); `sources/phd/P/01/06/outputs/04_HSX_EXPERIMENT_PLAN.md`
Sections 3-4; `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/outputs/06_ADVISOR_MEETING_BRIEF.md`
Section 6.

## Element 2 — Integrate Hall plus inductive coils as a hybrid diagnostic

The extraction rules require absolute calibration, mutual consistency,
bandwidth fusion, and radiation compensation to be kept as **distinct**
claims. Absolute calibration is Element 1's own claim above (C06). The
remaining three are represented by C07-C09 (kept stable from the pilot)
plus a substantially deeper full-run evidence base (C23-C30, C43),
**each proposed, derived-as-mathematics-only, or inferred — never
demonstrated on hardware**:

- **Mutual consistency (inferred, C07; formal basis C23).** Hall->coil
  correction of the coil's integrator drift is hardware-proven outside
  fusion and deployed at system level (ITER OVSS) per the corpus's cited
  literature. Coil->Hall is only conditionally feasible for gain (needs a
  trusted coil chain plus real field excursions) and can **never**
  deliver Hall offset — offset needs zero-field epochs or an external
  absolute reference. **Full-run addition (C23):** this is not merely a
  qualitative judgment — the source formally derives it as "Theorem 1," a
  two-parameter structural non-identifiability proof (a scale factor and
  an offset shift jointly applied to the field and both channels'
  gains/offsets leave every possible measurement unchanged, for any
  excitation whatsoever), numerically confirmed by a reproducible
  Fisher-information rank test. Nine further identifiability cases are
  derived for specific reference/excitation conditions (C23): e.g. a
  known machine-current field model at >=2 field levels yields *full*
  4-parameter identifiability (the corpus's proposed "workhorse absolute
  anchor" for HSX), while a quasi-static field yields only 2 of 5
  observable quantities and "no mutual calibration content at all." **The
  source explicitly rejects the symmetric phrase "the sensors calibrate
  each other" as misleading without these conditions attached, and states
  no hardware demonstration of the coil->Hall direction exists in fusion
  conditions.** Mutual agreement alone is not automatic absolute
  calibration.
- **Bandwidth fusion (proposed, C08; formal basis in C23's Case 9).** The
  Hall channel is proposed to supply DC/low-frequency field content the
  coil structurally cannot see; an embedded calibration-winding injection
  is proposed to sit in an "overlap band" so injection near/above the
  Hall pole can identify Hall dynamics. The corpus's own formal Case 9
  derivation shows this is excitation-conditional: near-DC operation
  cannot verify Hall bandwidth at all (a numerical demonstration shows the
  pole-carrying signal collapses by an order of magnitude a decade below
  the pole). No bandwidth-fusion hardware test exists yet, and it depends
  on the still-unverified Hall bandwidth figure (C05).
- **Radiation compensation (proposed, C09; magnitude Unknown, C29).** A
  layered "anchored hybrid" architecture is proposed to separate
  temperature-driven from radiation-driven drift. Radiation qualification
  work is explicitly collaborator-led, never on the HSX critical path,
  and never claimed as an experimental result in first-author work. The
  GaN/AlGaN radiation-drift magnitude is stated as **Unknown**: no
  GaN/AlGaN Hall-plate neutron dataset exists in either the 231-source or
  219-source ledger reviewed (C29), and cross-species radiation scaling
  has failed by ~14x in one cited comparable III-V material case, meaning
  wrong-species screening would be actively worse than none.

**Where a simpler single-technology sensor already wins outright (C27),
and what already competes with the hybrid's value case (C43):** the
corpus's own counterexample analysis names six niches (fast MHD/coil,
total-current/Rogowski-or-FOCS, z-pinch/inductive-pair,
persistent-mode-SC/NMR, accelerator-magnet-metrology, gamma-only-TMR)
where a simpler sensor is stated to outright beat the hybrid; separately,
TMR is flagged as the sharpest single-channel challenge to the whole
Hall+coil value proposition (DC-to-broadband in one channel, demonstrated
gamma-radiation tolerance, though with no neutron data either way).

**What is actually novel (C26), stated by the corpus itself, not by this
extraction:** the broad "hybridize a Hall sensor with a coil" idea has 26
years of direct prior art (1999 through 2025, including ITER's OVSS as a
manufactured system-level pairing and two 2025 Kalman-fusion papers on
exactly this problem) and "no publishable claim can rest on" the
architecture concept alone. The corpus names four specific, narrower open
gaps instead: (a) a joint gain+offset+state identifiability analysis with
everything simultaneously unknown; (b) a hardware demonstration of the
reverse (coil-informs-Hall) direction in any fusion or radiation
environment; (c) in-situ radiation-aware recalibration against a
material-diverse witness sensor; (d) any Hall+coil work for stellarator
field mapping specifically.

## Element 3 — Deliver a reusable module plus simulation/reconstruction package

**Status: proposed, not built (C10).** A reusable simulation/estimator
software package ("T0") is specified with a fixed module boundary
(model/schema/estimator/faults/scenarios/metrics/report/tests), a frozen
scientific core that may not change without a new stage-20-class review,
and a regression binding to an existing analysis tool
(`tools/observability_rank_tests.py`). It is proposed to be built
incrementally and frozen at manuscript submission (~Q1-Q2 2027), released
with that publication. No code has been built yet as of the cited
documents. **Full-run addition (C31, C48):** the package's own integrity
gate (falsification test FT-02) is presented by the corpus as the
lowest-cost, highest-priority test in the entire Opt2 program — a purely
desk-based check that the estimator visibly refuses to over-claim on
non-identifiable scenarios before any bench or campaign resource is
spent on it.

Source: `sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/outputs/03_SIMULATION_AND_VALIDATION_PLAN.md`
Section 11; `sources/phd/P/01/08_.../outputs/05_FALSIFICATION_TESTS.md` FT-02.

## Hypotheses (full-run addition)

Stated explicitly per the task requirement, drawn from what the corpus's
own documents already assert as their working hypotheses, not
reformulated beyond that:

1. **Element 1 hypothesis:** the real (non-emulator) GaN Hall die can be
   calibrated to a stable coefficient with u(k)/k <= 2% and <0.5%
   linearity once the ~109x bench anomaly (C04) is understood and closed.
   Falsifiable at gate G1/G-cal (C06); if the anomaly traces to the die or
   packaging, or drift/temperature instability exceeds any honest budget,
   the "finished calibrated output" premise fails.
2. **Element 2 hypothesis (mutual consistency):** a trusted coil chain
   plus real field excursions can recover Hall gain in situ within the
   Fisher-predicted confidence interval, while Hall offset structurally
   cannot be recovered this way (C07, C23). Falsifiable by bench test
   FT-05 (C25): if recovered gains do not match the Fisher-predicted
   interval or the predicted ramp-degeneracy does not appear as derived,
   "the reverse-calibration direction is falsified in practice even under
   ideal bench conditions."
3. **Element 2 hypothesis (radiation compensation):** GaN/AlGaN
   Hall-plate radiation-induced drift is large enough, relative to the
   architecture's tracking floor, to justify the compensation
   architecture's added complexity. This is explicitly Unknown today
   (C29) and is the specific question falsification test FT-11 (C25) is
   designed to answer — including the explicitly acknowledged possibility
   that the honest answer is "no, simplify to scheduled recalibration
   alone," which the corpus states is a good outcome, not a failure.
4. **Element 3 hypothesis:** an estimator built against the frozen T0
   scientific core will report only what the augmented Hall+coil state is
   actually observable, freezing and inflating uncertainty on
   non-identifiable cases rather than over-claiming. Falsifiable by FT-02
   (C31, C48): if any run "recovers" a Theorem-1 gauge-orbit parameter
   with confident (non-inflated) covariance, the corpus's own rule is to
   stop all hardware planning until the estimator/simulator is fixed.

## Experiments (full-run addition — the falsification-test ladder)

The corpus's own 12-item falsification-test ladder (FT-01 through FT-12,
C25), ordered cheapest-to-most-expensive, with ten of twelve tests
requiring zero radiation exposure:

| Test | Cost class | Decides | Radiation-free? |
|---|---|---|---|
| FT-01 | desk (prior-art kill search) | whether any of the four C26 novelty gaps has since been closed | yes |
| FT-02 | simulation (estimator honesty test) | trust in every later gate; "gates every dollar after it" | yes |
| FT-03 | simulation (anchor-cadence sufficiency) | whether realistic anchor cadence bounds common-mode blindness to an acceptable uncertainty | yes |
| FT-04 | bench-day (zero-field/flip offset anchor) | whether zero-field epochs actually recover Hall offset at the architecture's booked accuracy; "no fallback" if it fails | yes |
| FT-05 | bench-days (coil-referenced Hall-gain recovery) | the reverse-direction (coil->Hall) claim itself, under ideal bench conditions | yes |
| FT-06 | bench-days to weeks (embedded winding) | whether the calibration-winding layer delivers continuous gain tracking without polluting the measurement | yes |
| FT-07 | bench-soak, weeks (drift race) | whether the hybrid's continuous tracking measurably beats simple scheduled recalibration for slow drift | yes |
| FT-08 | machine-piggyback, HSX | whether the machine-current absolute anchor works at useful accuracy on a real machine | yes |
| FT-09 | machine-piggyback, HSX | whether repeated-waveform shot-to-shot regression can track gain drift at a useful floor | yes |
| FT-10 | machine-piggyback, HSX plasma shots | whether the tracking layers survive real plasma-operations EMI | yes |
| FT-11 | irradiation facility, collaborator-led | whether GaN radiation drift is even large enough to matter; witness-channel replication; coil-material dose response | no |
| FT-12 | full mixed-field qualification, collaborator-led | whether per-species screening composes correctly in the real mixed-field environment | no |

Several branches are explicitly named as *good* outcomes that simplify
the architecture rather than represent project failure (e.g. FT-06/FT-07
failing means "descope to the simpler anchor-only design"; FT-11 finding
GaN drift below the detection floor means "in-situ radiation recal is
unnecessary").

## Deliverables (full-run addition)

Per the corpus's own folder-06 paper sequence (P1/P2/P3) and folder-08's
proposed integration into it (C32), described here without repeating the
corpus's internal numeric scoring:

- **P1 (SENSL revision).** Unchanged by the Opt2 continuation; remains
  the campaign-independent, bench-only critical-path paper.
- **P2 (hybrid-architecture paper).** Reframed by folder-08's analysis to
  claim only the four specific gaps (C26), not "we hybridized a Hall
  sensor with a coil"; proposed content: identifiability theory (C23) +
  an honesty-tested estimator (C31/C48) + bench validation (FT-04/FT-05
  results). Same existing timeline (Aug-Dec 2026 desk/bench work).
- **P3 (RSI vector-probe paper).** Unaffected in scope by the Opt2
  continuation; a piggyback opportunity for hybrid data (vacuum-shot
  anchors, repeated-waveform floors, EMI survey), never a new
  machine-time request.
- **T0 (Element 3's software package).** Frozen and released with P2,
  per the corpus's own stated plan (C10, C32).
- **A radiation-compensation capstone (Phase 4, collaborator-led).**
  Explicitly deferred, coauthored, and never on the HSX critical path
  (C09, C32); its publishability is entirely contingent on FT-11's
  outcome.

## Dependencies (full-run addition)

The corpus's own dependency structure (C06, C31, C32, C45), stated as a
chain rather than reproduced as the corpus's internal gate-graph
diagram:

1. **Anomaly closure (C04)** gates **absolute calibration (C06)**, which
   gates any tesla-denominated claim anywhere in P1 or P2.
2. **Estimator honesty (FT-02, C31, C48)** gates all further simulation
   or hardware work on Element 2/3 — the corpus's own stated
   highest-leverage, lowest-cost gate.
3. **Deployed-module location/health (C45, gate I-4)** gates both the
   repeatability study (WP-B) and the retroactive Fig.-5 field-unit
   conversion of the existing 2025 dataset — undocumented anywhere in the
   corpus as of this run.
4. **Offset-anchor validity (FT-04, C31)** gates every downstream
   accuracy budget that assumes Hall offset is recoverable at all; a
   failure here has "no fallback," per the corpus's own words.
5. **Advisor + Stanford OTL pre-disclosure screen (C33, C34)** gates any
   arXiv posting, conference talk, or public code/firmware repository for
   any of the three Opt2 elements — an explicit hard gate (G-C), not yet
   concluded per the corpus's own milestone tracker.
6. **Folder-08's own redteam/synthesis stages (C40)** have not run —
   every claim resting on folder 08 alone (C07-C10, C17, C23-C32, C43,
   C48) is accordingly pre-adversarial-review within the corpus's own
   process, independent of this ledger's own confidence labeling.

## Kill criteria (full-run addition)

Named stop/pivot conditions the corpus itself states, collected here
without repeating the corpus's internal weighted-score language:

- **G1/anomaly (C04, C06):** if the ~109x anomaly does not close, no
  calibration claim exists anywhere in P1; the corpus's own fallback is
  to re-scope P1 around non-calibration content and drop the finished-
  calibrated-instrument claim.
- **FT-02 estimator-honesty failure (C31, C48):** if any simulation run
  "recovers" a formally non-identifiable (Theorem-1 gauge-orbit)
  parameter with confident, non-inflated covariance, the corpus's own
  rule is to stop *all* hardware planning until the estimator/simulator
  is fixed — because a package that flatters itself would poison every
  later gate.
- **FT-04 offset-anchor failure (C25, C31):** if zero-field/flip offset
  reads do not repeat at the predicted accuracy, "the offset half of the
  calibration story is unsupported," with no fallback stated, since AC
  injection can structurally never supply offset (Theorem 1, C23).
- **FT-05 reverse-direction failure (C25):** if coil-referenced Hall-gain
  recovery does not match the Fisher-predicted interval under ideal bench
  conditions, "the reverse-calibration direction is falsified in
  practice"; the architecture then collapses to the already-proven
  Hall->coil direction only, and the specific novelty claim (C26 gap b)
  is retired.
- **FT-07 no-advantage failure (C25):** if a single Hall channel with
  scheduled recalibration matches the hybrid's tracking accuracy within
  uncertainty for slow drift, "the hybrid layer is not earning its
  complexity" and the "better measurement performance" value class is
  falsified for that regime — the hybrid then survives only on its
  fault-detection value.
- **Direction gate G5 (~month 12, from folder 06, C38, C47):** requires
  both an accepted/in-revision first-author paper AND real-die absolute
  calibration; either condition failing is named as the trigger to pivot
  toward the corpus's own documented fallback direction (a
  reconstruction-methods track), a pivot the corpus states is
  low-additional-cost because it reuses the same data pipelines and
  collaborator relationship the Opt2 work would already have built.

## Uncertainties (full-run addition, beyond per-claim limitations)

- **Single-source dependencies (C30):** the only real-world coil-to-Hall
  gain-tracking precedent and the only radiation-null witness-material
  reference each rest on exactly one cited source in the corpus's
  219-source ledger; the corpus flags both explicitly rather than hiding
  them, and this ledger reports that flagging rather than resolving it.
- **Absence-of-evidence, not proof-of-absence (C26, C29):** the "no
  Hall+coil stellarator literature exists" and "no GaN neutron dataset
  exists" findings are bounded by the corpus's own documented search
  scope (219-450 sources across the two ledgers), not a claim that no
  such evidence exists anywhere in the world literature.
- **Redteam status (C39, C40):** folder 06's claims have passed an
  independent (same-model-family, not cross-provider) red-team audit
  finding 0 critical/high defects; folder 08's claims have not yet
  reached that stage in the corpus's own process. Any future re-run of
  this extraction should re-check whether folder 08 has since produced
  `70_redteam`/`80_synthesis` outputs before treating its claims with the
  same confidence as folder-06 material.
- **Provenance (C50):** all of the analysis, scoring, and planning
  content summarized in this document (identifiability theory, failure
  modes, falsification tests, application scoring, IP screening,
  roadmap) was produced by AI-agent research-strategy missions the
  researcher commissioned, not hand-derived by the researcher personally
  — a fact this ledger states explicitly rather than letting a reader
  infer.
