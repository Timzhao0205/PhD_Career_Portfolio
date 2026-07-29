# GAPS — B15_lit_synth PILOT

**PILOT SAMPLE — NOT FINAL**

Stage: `B15_lit_synth` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Scope: contradictions, missing experiments, weakly studied regimes, and
candidate bridge tests exposed by the eight adjudicated pilot papers
(P0001-P0008) read against the B10 PhD claims. Absence from these eight
papers is never proof of absence in the wider literature; every gap below is
a candidate for full-corpus re-checking in the full run, not a settled
finding.

## 1. Contradictions and tensions found

**G1 — No fusion-condition hardware demonstration of Hall+coil fusion, and
no support at all for the reverse (coil-to-Hall) direction [EV04].**
P0003's Kalman fusion is validated on synthetic data only; P0001's
high-performance hybrid probe is a proposal. Sharpest point: P0001 reports
its own coils "were not made to be very precise and identical" and were
"not calibrated on bench" — i.e. the flagship deployed Hall+coil system
lacked exactly the trusted coil reference chain that the PhD's proposed
coil-to-Hall reverse calibration (B10 C07/C23) presupposes. The PhD
direction's central assumption is thus contradicted-in-practice by the only
long-term deployed system in this set, while remaining theoretically open.

**G2 — Idealized-simulation vs real-installation regime tension [EV10].**
P0003 (white Gaussian noise, Wiener bias, "drift issue is completely
resolved", ~30x SNR gain) and P0001 (~19% pulse loss, suboptimal coil SNR,
non-identical coils) describe the same architecture class in regimes that
never overlap. Neither is wrong; jointly they show the validation chain
from algorithm to installed instrument has a missing middle.

**G3 — Calibration-regime mismatch across the hall_metrology stream.**
The only traceable-uncertainty exemplar in the set (P0008) operates at
+/-150 mT, room temperature, on gold/graphene sensors; the fusion-facing
Hall work (P0001, P0004) operates to +/-2.5 T in-machine on InSb/Sb with
stability tracking but no formal GUM-style uncertainty budget on the opened
records. No paper in this set does both traceable uncertainty *and*
fusion-relevant conditions.

## 2. Missing experiments (species/regime gaps)

**G4 — No GaN/AlGaN Hall-plate radiation dataset [EV09].** All demonstrated
radiation hardness in this set is InSb (P0001) or Sb (P0004). This
independently matches B10's own ledger finding (C29). B10 additionally warns
(its claim, not this set's) that cross-species radiation scaling has failed
by ~14x in a comparable III-V case — so the InSb/Sb tolerance numbers in
EV02 must not be transferred to GaN.

**G5 — No experimental validation of NI-coil self-protection dynamics
[EV05].** P0007's mechanism is a simulation anchored to one measured
parameter (70 uOhm-cm2); its authors flag that other measured resistivities
(27 uOhm-cm2) would change detection margins. An instrumented quench
experiment testing the predicted along-the-whole-turn redistribution and
<=9 mV voltage signature is absent from this set.

**G6 — Quench-detection data scarcity [EV06].** P0002's entire real
evidence base is 36 quench records from one coil in one lab; performance
already drops to 0.875 across geometry and 0.8056 at 0 dB SNR. No
multi-lab, multi-coil, or in-service dataset appears in this set.

## 3. Weakly studied regimes and stale layers

- **Stellarator-specific Hall/coil work:** absent from this 8-paper set
  (P0001/P0003 are tokamak-facing). Consistent with, but not proof of, B10's
  claimed novelty gap (d) — full-corpus check required.
- **Power-conversion stream rests entirely on reviews here:** both P0005
  and P0006 are syntheses; P0006 is a 2021 snapshot with a 12-day review
  timeline. The stream currently has no primary measurement evidence in the
  pilot set at all, and its headline figures are untraced review citations.
- **Long-pulse (>=1000 s) magnetic measurement:** P0003 names the regime
  and simulates 1 h records, but no hardware evidence at that duration
  exists in this set.

## 4. Candidate bridge tests these papers expose

Ordered roughly cheapest-first; each maps onto B10's own falsification
ladder where one exists.

1. **Replay-validation of the P0003 estimator on real archived data**
   (closes G2; aligns with B10 FT-08/FT-09 intent without machine time):
   run a P0003-class Kalman fusion on existing long-pulse machine archives
   (e.g. P0001-class RHP + coil records) and compare against the synthetic
   ~30x SNR claim.
2. **Bench coil-referenced Hall-gain recovery** (closes half of G1; this is
   exactly B10's FT-05): with a bench-calibrated coil chain and real field
   excursions, test whether coil-to-Hall gain recovery matches the
   Fisher-predicted interval. P0001's uncalibrated-coil disclosure shows
   this test cannot be piggybacked on legacy hardware — the calibrated coil
   chain must be built first.
3. **Traceable calibration at tesla-scale on a fusion-candidate sensor**
   (closes G3; extends P0008's method + B10 WP-C): reproduce the
   P0008-style uncertainty budget on an InSb/Sb/GaN sensor across
   +/-2 T-class fields and elevated temperature.
4. **Species-correct GaN/AlGaN irradiation with a witness channel**
   (closes G4; B10 FT-11, collaborator-led): even a single-fluence-point
   dataset would convert EV09 from "unknown" to bounded.
5. **Instrumented NI-coil quench experiment** (closes G5): direct
   measurement of turn-current redistribution and terminal voltage against
   P0007's predictions, at more than one contact resistivity.
6. **Full-run primary tracing of review figures** (closes the review-only
   weakness of the power_conversion stream): before any converter-related
   conclusion is accepted in the full synthesis, trace EV07/EV08 headline
   numbers to at least one verified primary study each.

## 5. Honesty notes

- Gaps G1-G6 are statements about **this 8-paper set plus B10's disclosed
  claims**, not about the world literature. The 62-paper corpus (and, where
  needed, fresh search) must re-test each in the full run.
- No gap above rests on a retracted or correction-flagged paper (0/8 in
  this set).
- This file identifies evidence gaps; it makes no startup ranking and no
  final novelty verdict.
