# GAPS — B15_lit_synth (FULL)

Stage: `B15_lit_synth` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Contradictions, missing experiments, weakly studied regimes, novelty
uncertainties, and prioritized decisive bridge experiments, adjudicated
over the full 62-paper B12 corpus (P0001-P0062) read against the B10 PhD
claims (C01-C50). Every gap below is bounded by this corpus plus B10's
disclosed search scope; absence from this evidence base is never proof of
absence in the world literature. Paper IDs resolve to B12's ledger; EVxx
rows to this stage's EVIDENCE_MAP.csv; Cxx/FT-xx to B10's outputs. The
bridge tests in §5 are ranked by decision value and feed B25/B30.

## 1. Contradictions and tensions (corpus-confirmed)

**G1 — No fusion-condition hardware demonstration of Hall+coil fusion,
and zero corpus support for the reverse (coil→Hall) direction [EV04,
EV32].** Confirmed on the full corpus, not just the pilot 8: P0003's
Kalman fusion is synthetic-only; P0001's hybrid probe is a proposal; the
nearest hardware fused sensor is TMR+CT outside fusion (P0031). Sharpest
point unchanged: P0001 reports its own coils were never bench-calibrated —
the flagship deployed Hall+coil system lacked exactly the trusted coil
reference chain the PhD's coil→Hall step (C07/C23) presupposes. The
reverse direction is simultaneously the PhD's clearest novelty lane (C26
gap b) and its least externally supported assumption.

**G2 — Idealized-simulation vs real-installation regime tension [EV10].**
P0003 (white Gaussian noise, Wiener bias, drift "completely resolved",
~30x SNR) versus P0001 (~19% pulse loss, suboptimal coil SNR,
non-identical coils). No corpus paper bridges the middle. Any hybrid
estimator's credibility rests on closing this.

**G3 — Calibration-regime mismatch across hall_metrology, corpus-wide
[EV35].** The only traceable-budget exemplar (P0008) is ±150 mT/room
temperature/gold-graphene; the fusion-facing work (P0001, P0004) reaches
±2.5 T in-machine with stability tracking but no GUM-style budget; the
best system-level calibration discipline (P0024, 0.1%-class elements) is
coil-only on a 10 s machine. Tesla-scale + traceable budget + harsh
environment never co-occur in this corpus.

**G4 — Incumbent-practice contradiction: a 2020 flagship magnetic
diagnostic redesign is deliberately coil-only [EV19].** P0024 (RFX-mod2,
724 probes) quantifies integrator drift (~0.6 mT over 10 s) and accepts
it rather than adding a DC-capable channel. This does not refute the
long-pulse value case for Hall channels — RFX-mod2 pulses are short — but
it contradicts any claim that the field at large is moving to hybrids.
The hybrid argument must be made regime-specific (1000 s-class machines)
or it fails against incumbent practice.

**G5 — Competing-channel tension in both target domains [EV18, EV28,
EV34].** The only published DC+AC fused current sensor uses TMR, not Hall
(P0031); MR technologies hold the DC-capable power-equipment niche
(P0060-P0062); P0050 describes Hall as bandwidth-limited with drift
burdens while also noting TMR's EMI-driven <50 kHz filtering. No
head-to-head Hall-vs-TMR benchmark under switching EMI exists in the
corpus — the decisive comparison for B10 C43 is simply missing.

**G6 — NI self-protection is conditional, and the boundary matters
[EV05, EV21].** P0007/P0040 support passive recovery at moderate current;
P0043 demonstrates a hard fault mode (quench in ~450 ms from ≥350 A at
4.2 K) requiring an engineered shunt. Papers agree with each other, but
the popular "NI coils are self-protecting" shorthand is contradicted at
high stored energy — and protection scaling beyond lab coils is open
(P0043's own caveat; P0046's 45.5 T insert was damaged after quench).

## 2. Missing experiments (species/regime gaps)

**M1 — No GaN/AlGaN Hall-plate irradiation dataset [EV09].** All
demonstrated radiation hardness is InSb (P0001) or Sb (P0004); the
corpus's radiation work otherwise covers silicon FD-SOI by TCAD only
(P0018) and MR sensors under gamma (P0019). Matches B10 C29 (Unknown),
whose cited ~14x cross-species scaling failure forbids substituting the
InSb/Sb numbers for GaN.

**M2 — No coil-referenced Hall-gain recovery experiment anywhere [EV32].**
B10's FT-05 would be, per this corpus, the first published test of the
reverse direction even at bench level.

**M3 — No traceable tesla-scale Hall calibration [EV35].** WP-C (C06)
executed to target would occupy an under-published niche; its method
template exists (P0008), its regime evidence exists (P0004's ±2.5 T
linearity), the combination does not.

**M4 — No real-data replay validation of Hall+coil fusion [EV10].**
P0003-class estimators have never been run against archived real machine
records (P0001-class) in the corpus.

**M5 — No instrumented independent-group NI redistribution experiment at
multiple contact resistivities [EV05].** P0007's mechanism rests on
70 µΩ·cm²; its authors flag 27 µΩ·cm² as harder; the experimental
corroboration (P0040, P0043) is largely one research lineage.

**M6 — No Hall-vs-TMR (or any DC-channel) benchmark in an operating WBG
converter [EV28].** P0050 sets the requirements; nobody in the corpus runs
the comparison.

**M7 — No Hall-based or hybrid method applied to HTS magnet monitoring
[EV26].** The stream's detection work uses voltage compensation, strain,
microwave, and ML; whether a Hall/coil approach adds value in the
transient/charging regime is untested (and the persistent-mode use case is
already structurally vetoed by B10 C27).

## 3. Weakly studied regimes and stale layers

- **Stellarator magnetics with Hall sensors: absent [EV33].** All fusion
  rows are tokamak/RFP/generic. Consistent with C26 gap (d); HSX remains
  unclaimed ground in this corpus.
- **Long-pulse (≥1000 s) hardware evidence:** P0003 simulates 1 h records;
  no corpus hardware demonstration at that duration. The regime that
  motivates the whole hybrid case is evidenced by extrapolation, not
  measurement.
- **AlGaN/GaN high-temperature Hall data:** the corpus's only statement is
  P0017's 2011 mobility-degradation note with "insufficient published
  data" — fifteen years stale; the current state is unassessed here.
- **Power-conversion review layer staleness:** core WBG consensus figures
  are 2019-2023 reviews (P0005, P0006, P0057); 2024-2026 device
  generations are not represented at review level. Primary corroboration
  in-corpus is partial (P0048, P0056).
- **Graphene/2D sensor stability:** best-in-class noise floors (P0010)
  coexist with unresolved gate-instability and day-to-day drift (P0008's
  9.3%); maturity for deployed instruments is unestablished.

## 4. Novelty uncertainties

- **C26 gap (a) (joint identifiability analysis):** nothing in this corpus
  performs a Hall+coil joint gain/offset/state identifiability analysis —
  but this is a theory contribution, and theory prior art can hide in
  control/estimation literature outside B12's four streams. Uncertainty:
  moderate. A targeted FT-01-class kill search (B10) remains necessary
  before any publication claim.
- **C26 gap (b) (reverse-direction hardware demo):** corpus-verified open
  [EV32]; B10 itself cites one non-fusion precedent (C30) outside this
  corpus — the gap wording must therefore be "in fusion/radiation
  environments", not "anywhere".
- **C26 gap (c) (radiation-aware recalibration with witness sensor):**
  unaddressed in corpus; single-source witness-material dependency flagged
  by B10 (C30) is neither strengthened nor weakened here.
- **C26 gap (d) (stellarator Hall+coil):** corpus-verified open [EV33].
- **Anti-claim guard:** C44's prohibition on "first fusion Hall
  diagnostic" is corpus-enforced — P0001/P0004/P0017 document the
  pre-existing lineage [EV02].

## 5. Prioritized decisive bridge experiments (ranked by decision value; feeds B25/B30)

Ranking criterion: (decision leverage over the PhD/startup evidence base) ×
(what the corpus shows nobody else has done) ÷ cost. Tests 1-4 are
desk/bench-scale; 5-7 need facilities/collaborators; 8 is a desk audit.

1. **BT-1 — Estimator honesty test (B10 FT-02 verbatim; zero hardware).**
   Build the T0 estimator skeleton and verify it freezes states and
   inflates uncertainty on Theorem-1 non-identifiable scenarios (C23,
   C31). Decision value: highest per dollar — B10's own rule says it
   gates every later claim, and the corpus shows the field's algorithm
   evidence (P0003) has never been subjected to such a test [EV10].
   Kills/validates: Element 3's integrity premise before any bench cost.
2. **BT-2 — Replay validation of a P0003-class Kalman Hall+coil fusion on
   real archived machine data (closes G2/M4).** Use existing long-pulse
   archives (P0001-class RHP + coil records, or HSX archives per C01)
   with no machine time. Decision value: converts the architecture's core
   quantitative claim (~30x SNR, drift removal) from synthetic to real
   evidence — or breaks it early. Direct feed to B10 FT-08/FT-09.
3. **BT-3 — Bench coil-referenced Hall-gain recovery (B10 FT-05; closes
   G1's testable half, M2).** Calibrated coil chain + real field
   excursions; compare recovered gain against the Fisher-predicted
   interval (C23). Decision value: first published test of the reverse
   direction per this corpus [EV32]; failure retires C26 gap (b) claims
   and collapses the architecture to the proven forward direction —
   itself a clean, publishable negative result.
4. **BT-4 — Traceable tesla-scale calibration of a fusion-candidate
   sensor (closes G3/M3; extends P0008 + B10 WP-C).** Reproduce a
   P0008-style GUM budget on the GaN die (post-anomaly-closure, C04) or
   on an InSb/Sb reference across ±1-2 T and elevated temperature.
   Decision value: makes WP-C's output externally benchmarkable and fills
   an under-published niche [EV35]; blocked until the ~109x anomaly
   closes (C04) — which is itself B10's prior gate, not a literature gap.
5. **BT-5 — Species-correct GaN/AlGaN irradiation with a witness channel
   (B10 FT-11; closes M1).** Even a single-fluence-point dataset converts
   EV09 from Unknown to bounded, and decides whether radiation
   compensation (C09) is needed at all — B10 explicitly names "no" as a
   good outcome. Collaborator-led; never on the critical path (C09).
6. **BT-6 — Hall-vs-TMR head-to-head under switching EMI (closes G5/M6).**
   Instrument one WBG converter cell (P0048/P0056-class test bed) with
   both channels; measure usable bandwidth, drift, and EMI-induced error
   against P0050's requirement list. Decision value: settles the
   competing-channel question (C43) that both the fusion and
   power-conversion transfer cases hinge on; also the decisive datum for
   any startup-facing sensing claim (adjudicated in B40, not here).
7. **BT-7 — Instrumented NI-coil quench redistribution experiment at ≥2
   contact resistivities, independent group (closes M5, tests G6).**
   Direct measurement of turn-current redistribution and terminal-voltage
   signature against P0007/P0032 predictions. Decision value: moderate
   for the PhD (context stream), high for any HTS-monitoring
   instrumentation thesis [EV26].
8. **BT-8 — Primary tracing of the review-layer headline figures
   (closes the review-only weakness of EV07/EV08).** Trace the ~99%
   efficiency, ~100x frequency, and 200-300 C SiC figures to at least one
   verified primary study each before any converter-related conclusion is
   reused downstream. Desk-only; low decision value for the PhD, but
   required hygiene for B25/B30 reuse of EV07/EV08.

## 6. Honesty notes

- G1-G6 and M1-M7 are statements about this 62-paper corpus plus B10's
  disclosed claims, not about the world literature. Bridge test BT-3's
  "first published test" framing is corpus-bounded and must be re-verified
  by a fresh kill search (B10 FT-01) before any publication claim.
- No gap above rests on retracted work (0/62 found retracted); the single
  corrected paper (P0012) carries no load in any gap.
- Review-derived statements (P0046's monitoring gap, P0050's requirement
  synthesis) are labeled as review conclusions wherever they appear.
- This file identifies evidence gaps and decisive tests; it makes no
  startup ranking and no final novelty verdict.
