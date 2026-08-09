# POWER — B25_power (PILOT)

**PILOT SAMPLE — NOT FINAL**

Stage: `B25_power` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Specialized power converter/electronics/supply analysis, pilot-scoped to
exactly FOUR architectures spanning all four roles. Every material claim maps
to B15 evidence rows (EVxx) / papers (Pxxxx), B15 gap/bridge IDs (G/M/BT-x),
B10 claims (Cxx), B20 alignment rows and founder-fit corrections, corpus idea
records (cited by path), or sources opened live this pilot (S-B25-xx in
SOURCES.csv). The full run must cover >=18 ideas; nothing here is a final
wedge decision.

## 1. Scope and selection

Four architectures chosen from the corpora's power-relevant pool to maximize
role coverage (the pilot rule requires >=2 roles; these span all four):

| idea_id | Architecture | Role | B20 alignment class |
|---|---|---|---|
| P3R2-C-01 | 800VDC rack power-path protection shelf (SSCB + precharge + insulation monitoring + hot-swap) | full end product | WEAK |
| P3R2-C-13 | Precision GaN pump-driver / laser-power module | subsystem (OEM merchant module) | WEAK |
| P3R2-F-06 | Precision wideband DC current/voltage sensing platform (FOCS + zero-flux hybrid) | measurement-qualification tool | MEDIUM (boundary) |
| P3R2-E-10 | Standardized rad-tolerant GaN PPU platform | reference design | WEAK |

Selection rationale: C-01 is the corpus's top consensus power idea and the
sharpest test of the founder-fit-vs-consensus distinction; C-13 is the
designated GaN vocabulary trap with the clearest telemetry sliver; F-06 is
the discipline-nearest idea in the whole universe (its product IS current
metrology); E-10 carries B20's explicit handoff instruction to preserve the
BT-5 irradiation-piggyback channel in B25's experiment planning. Deferred to
the full run: C-07 (AFE rectification — A30-verified kill facts), C-09,
C-14, C-22, E-14, F-01, F-02, F-23, G-03, A-02, C-15, D-16, F-12, F-03 and
the D-10 phase-control engine (ADVERSE per B20; power-adjacent only).

## 2. Where Hall/coil sensing concretely enters each architecture

The stage's seven named sensing functions, applied honestly per
architecture. Bandwidth reality first, because it bounds everything: the B15
power-conversion stream's requirement synthesis (EV27/P0050) puts WBG
switching-current measurement needs at ~50 MHz-class bandwidth, describes
Hall sensors as typically responding below ~100 kHz with temperature/offset
drift burdens, and notes TMR channels are usually low-pass-filtered below
~50 kHz in switching environments (EV28/P0050). So: **trip-grade and
edge-fidelity sensing is shunt/CT/Rogowski territory (P0048/P0056); the
Hall/TMR class competes for the DC/low-frequency content those AC devices
cannot see (EV27/EV34)**.

**C-01 (800VDC protection shelf).**
- *Protection:* the microsecond trip decision itself needs di/dt- or
  shunt-class speed; a Hall/TMR channel cannot carry the trip alone
  (EV27/EV28). A DC-capable channel plausibly serves the slower protection
  layers: precharge supervision, overload trending, reverse-current checks.
- *Transients:* precharge/inrush current profiling and hot-swap sequencing
  verification — DC-to-mid-band content, a genuine DC-channel role.
- *Ripple:* bus-ripple monitoring as a converter-health indicator upstream
  of the shelf — secondary telemetry.
- *Current sharing:* paralleled feed/load-share monitoring across shelves.
- *Ramp/dump:* not a native function here (no stored-energy magnet); the
  analog is capacitor-bank precharge/discharge supervision.
- *Fault localization:* series-arc signature discrimination (spectral
  content in load current) — the EV27-class weak-signal-under-EMI sliver
  B20 identified; algorithmic core is proposed-only PhD material (C23/C31,
  C40).
- *Calibration:* telemetry channels only earn acceptance-grade meaning with
  a calibration chain (see §6); NVIDIA's own architecture note flags fault
  detection in VDC systems as "a key area for innovation" (S-B25-03).
- **Certification reality:** any sensor inside the trip path becomes part of
  the IEC 62477-1-class safety case (S-B25-01) — a sensor vendor cannot
  bolt trip-grade sensing onto someone else's certified breaker after the
  fact.

**C-13 (GaN pump-driver module).**
- *Transients:* nanosecond pulse-current fidelity is CT/Rogowski territory
  (P0048: ~100 MHz nonlinear-model CT, 4% at 50 A; P0056: PCB-embedded
  Rogowski, linear 10 Hz-1 MHz, tested to 400 A); a Hall/TMR channel serves
  the DC bias and envelope content.
- *Ripple:* drive-current ripple feeds directly into pump-diode photon
  output stability — a telemetry selling point the record treats as
  non-core.
- *Current sharing:* paralleled GaN stages and diode strings.
- *Protection:* diode overcurrent/overtemperature interlocks (slow layer).
- *Fault localization:* diode-health trending (forward-drop/current
  signature drift) — the calibrated-telemetry sliver.
- *Ramp/dump:* programmed current ramps for diode life management; no
  stored-energy dump.
- *Calibration:* the sliver's entire value is a *calibrated* claim —
  uncalibrated telemetry is a commodity feature every driver vendor ships.

**F-06 (precision DC sensing platform).** Sensing is not an entry point
here — it is the product. *Calibration* is the core function (traceable
chains, uncertainty budgets — the WP-C methodology class, C06 proposed);
*ripple* metering in electrolyzer/rectifier DC; *transients* as HVDC fault
recording; *ramp/dump* as magnet-system current excursion capture — which
is precisely the trusted-excursion infrastructure the PhD's coil-referenced
tests need (BT-3/FT-05; B20's reverse-channel note); *current sharing*
across parallel rectifier/stack paths; *protection* as the qualification of
others' protection sensing rather than tripping itself; *fault
localization* via distributed station metering. Honest boundary: the
venture's chosen modalities (FOCS, zero-flux DCCT) are not Hall and not
PhD-evidenced hardware (EV20/EV28); merchant zero-flux units already ship
at 1 ppm-linearity class (S-B25-02), so the wedge cannot be sensor novelty.

**E-10 (rad-tolerant GaN PPU reference design).**
- *Protection/current sharing/ripple:* PPU-internal bus telemetry and
  overcurrent protection — standard space power engineering, not
  PhD-differentiated.
- *Transients:* SET/SEB-induced current transients are the design's core
  radiation problem — a power-device reliability problem, not a sensor
  problem (see §5).
- *Calibration:* in-flight telemetry drift management would benefit from
  witness-channel discipline (C09's architecture class), but with zero
  GaN/AlGaN radiation data (M1/C29) nothing quantitative can be claimed.
- *Ramp/dump, fault localization:* thruster current ramps; telemetry-based
  fault isolation — again standard practice, not a wedge.

## 3. Converter-stack realities — and what the PhD does NOT cover

A real specialized-converter product stands on this stack: topology
selection and control design; gate drive (a genuinely open burden for WBG —
EV08, review-level); SiC/GaN/WBG device selection and reliability (EV31 —
its own specialization); magnetics; insulation coordination; EMI/EMC
compliance; thermal design; deterministic controls and HIL validation;
safety engineering and certification (IEC 62477-1 class for <=1500 VDC
systems, S-B25-01); manufacturing/DFM; reliability engineering; field
service; supply chain.

Against B10's ledger, the PhD demonstrably covers **none of that stack**.
What it does cover: instrumentation-grade bench readout design and EMI
discipline (C03/C13 — small-signal, emulator-validated, with the ~109x
anomaly C04 still open); harsh-environment sensor packaging (C46/C01);
proposed traceable calibration methodology (C06 — proposed, gated by C04);
proposed estimator/identifiability methodology (C23/C31 — folder-08,
pre-redteam C40). B15's structural adjudication is explicit: in specialized
converter work, application-specific topology/control differentiates and
measurement is supporting infrastructure (EV30); GaN materials vocabulary
is not a competitive capability in power-device markets (EV31). The
review-layer WBG headline figures (EV07: ~99% efficiency, ~100x frequency,
200-300C SiC) are used here only as direction-of-travel context — BT-8's
primary-tracing hygiene has not been performed, so no downstream conclusion
in this pilot leans on those numbers.

**Plainly: magnetic-sensor expertise — even excellent, demonstrated
magnetic-sensor expertise — does not suffice to design, qualify, or certify
a power converter, and nothing in this stage's analysis should be read as
implying it does.** Missing capabilities are named per-row in POWER_MAP.csv
and costed in POWER_SKILLS.md.

## 4. Radiation compensation vs bandwidth fusion — separate problems

The corpus keeps these distinct (B10 C08 vs C09) and this stage keeps them
distinct in the power domain too — plus a third problem the E-10 row
exposes:

1. **Bandwidth fusion** (C08 class): pairing a DC-capable channel with an
   AC channel to span DC-to-MHz. Cross-domain convergence is real (EV34):
   fusion diagnostics fuse Hall+coil (P0003, synthetic-only), power
   electronics fuses TMR+CT in hardware (EV18/P0031). This is an
   estimator/architecture problem with no radiation content.
2. **Radiation compensation** (C09 class): separating radiation-driven from
   temperature-driven *sensor drift* using anchors and witness channels.
   For GaN/AlGaN Hall plates there is zero data in either direction
   (M1/EV09/C29); the ~14x wrong-species scaling failure (C29) forbids
   substituting InSb/Sb numbers.
3. **SET/SEB mitigation in power devices** (E-10's actual problem):
   single-event transients/burnout in switching topologies — device-level
   power reliability engineering (EV31), not sensor drift at all.

Conflating any two of these is exactly the vocabulary trap B20 documented
(E-10 row: "GaN + radiation" ≠ mechanism). A power-facing sensing product
can need (1) without (2); a space PPU needs (3) and neither of the others;
only a radiation-environment *instrument* needs (1) and (2) together — and
then they still fail independently and must be tested separately (FT-11 vs
bench fusion tests).

## 5. Traceability and uncertainty discipline

**Mutual Hall/coil (or Hall/Rogowski, or telemetry/telemetry) consistency
is NOT absolute calibration.** The corpus's formal basis: for an
unreferenced DC-channel + inductive-channel pair with constant
gains/offsets, a two-parameter gauge transformation leaves every possible
measurement identical (B10 C23, Theorem 1; C07) — the pair can detect that
its channels disagree but cannot attribute which drifted, and the DC
channel's offset is observationally identical to a static field/current
shift the inductive channel cannot see. No corpus paper calibrates a DC
channel from a coil reference (EV32), and the field's own flagship hybrid
deployment never bench-calibrated its coils (EV04/P0001).

Power-domain consequence: a converter telemetry channel that "agrees with"
its companion Rogowski/CT is not thereby calibrated; acceptance-grade or
warranty-grade claims (C-01's condition monitoring, C-13's calibrated
telemetry, everything F-06 sells) require an external reference chain —
zero-flux DCCT / calibrated shunt class (S-B25-02 shows the merchant
reference grade: 1 ppm-linearity fluxgate transducers marketed for
"current calibration purposes") — plus a GUM-style uncertainty budget. The
corpus contains exactly one traceable-budget exemplar (EV01/P0008, ±150 mT,
room temperature) and shows the tesla-scale/harsh-condition/traceable
combination is unpublished (EV35/G3/M3); the acceptance-grade version of
this discipline is the scarce skill the WP-C methodology (C06) would
train — but C06 is proposed-only and gated by the unresolved ~109x bench
anomaly (C04). No calibration credential exists today (C15, C49 context).

## 6. Full end products vs measurement/qualification/reference platforms

The four rows split cleanly:

- **Full end product (C-01)** carries the entire §3 stack plus a
  certification campaign whose standard scope was verified live
  (S-B25-01), high capital, and buyer design-in risk — and the PhD
  contributes only a non-core sliver. Consensus strength (BLIND 1 / NEW 2 /
  OLD 5) does not change that; B20's independence-of-axes finding holds.
- **Subsystem (C-13)** trades certification burden for OEM-qualification
  burden; the socket is won on power-electronics performance (edge speed,
  BOM), not measurement. The PhD-adjacent lane is a telemetry sliver whose
  value must be proven as a *calibrated* claim (PB-1).
- **Measurement-qualification tool (F-06)** inverts the structure: the
  product IS the PhD's discipline class (precision current metrology +
  qualification authority), the safety/certification burden is
  instrument-class, and the missing capabilities are narrower (modality
  hardware, utility qualification) — but the venture-commercial evidence
  is the weakest of the four (old rank 23, NEW cut; incumbents at 1 ppm,
  S-B25-02) and demand is pre-order (record-fetched Southern Spirit
  2029/2032; NERC PRC-028/029 wave — record-vintage).
- **Reference design (E-10)** shows that "platform/reference" status does
  not reduce the capability bar: the qualification data that makes a
  reference design credible is exactly the space-power engineering the PhD
  lacks. Its only durable contribution to this program is the BT-5
  piggyback channel.

## 7. Preliminary preferred wedge (pilot judgment — falsifiable)

On four architectures, the wedge that survives the founder-fit test is
**the measurement/qualification/telemetry layer, not any converter end
product**: concretely, F-06's instrument-plus-qualification-protocol
posture (with modality choice held open pending PB-1), and — as service
lanes rather than products — the calibrated-telemetry slivers of C-01/C-13
sold to whoever builds the converters. Grounds: (a) every non-WEAK
mechanism B20 found in the 39-idea universe runs through measurement
authority; (b) every full-product row here carries a §3 capability stack
absent from B10's ledger; (c) the scarce, corpus-verified under-published
skill (traceable uncertainty at scale — EV35/G3) sits on the measurement
side. Honesty bounds: this leans on *proposed* WP-C methodology (C06,
gated by C04, pre-credential per C49) — the wedge is a bet on Element-1
execution, exactly as B20 §8 warned; and F-06's commercial evidence is
weak. PILOT-scoped: the full run must retest this against the
qualification-platform family (C-05-adjacent, C-22, G-03, E-14's HIL leg)
and the remaining ~14 power ideas before B30/B40 use it.

## 8. Honesty notes

- All venture market/timing facts are corpus-dated except the three live
  opens (S-B25-01/02/03); NERC and Southern Spirit dates are record-vintage
  (old06 fetch, 2026-07-14) and must be refreshed before full-run reliance.
- EV07/EV08 are review-level; BT-8 primary tracing was NOT performed this
  pilot; no conclusion above depends on their headline numbers.
- The C-13 analysis relies on B20's row (which read the old06 deep dive);
  this pilot did not re-open DD_P3R2_C_13.md. The F-06 record was re-opened
  this pilot to its demand/competitor/price sections (first 80 lines).
- Confidence and falsifiers are stated per-row in POWER_MAP.csv; this file
  makes no portfolio ranking (B40's job).
