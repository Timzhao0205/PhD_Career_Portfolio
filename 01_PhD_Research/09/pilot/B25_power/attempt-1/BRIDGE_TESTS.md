# BRIDGE_TESTS — B25_power (PILOT)

**PILOT SAMPLE — NOT FINAL**

Stage: `B25_power` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Pilot rule: ONE bridge experiment developed in full form. It builds
directly on B15's ranked bridge test **BT-6** (GAPS.md §5: "Hall-vs-TMR
head-to-head under switching EMI — closes G5/M6"), extended with a
traceable reference chain so it also serves this stage's power rows. The
full run will rank multiple experiments; §3 records two pointers only.

## 1. PB-1 — DC-capable current-channel benchmark under WBG switching EMI (BT-6 class, extended)

**One-line thesis.** Nobody in the B15 corpus has benchmarked Hall against
TMR (or any DC-capable channel) inside an operating WBG converter cell
(M6/G5, EV28); this is simultaneously the decisive datum for B10's
competing-channel question (C43) and for every power-facing sensing claim
in this pilot's rows.

**Measurand.** Current in one conductor of a WBG switching cell, decomposed
into: (a) DC transfer accuracy (gain, offset) against a traceable
reference; (b) small-signal bandwidth (amplitude/phase vs frequency);
(c) transient fidelity during switching edges; (d) EMI-induced error under
realistic dV/dt and dI/dt; (e) offset/gain drift vs temperature and over a
multi-hour soak.

**Devices under test.** (i) A commercial Hall-based current sensor
(open-loop and/or closed-loop class); (ii) a commercial TMR-based current
sensor (EV28's incumbent class, P0060-P0062 lineage); (iii) OPTIONAL and
non-gating: the PhD's GaN Hall die with the C13 readout chain — included
ONLY if the ~109x anomaly (C04) has closed; the experiment is deliberately
designed to be decision-grade with commercial sensors alone, so it is NOT
gated by C04.

**Reference chain (the "extended" part, beyond B15's BT-6 sketch).**
DC/low-frequency reference: a zero-flux/fluxgate transducer of the
merchant calibration grade (1 ppm-linearity class exists commercially —
Danisense DQ500ID, opened live, S-B25-02; marketed explicitly for "current
calibration purposes"), ideally borrowed/rented with a current calibration
certificate. Transient reference: a wideband coaxial shunt (P0048/P0056
establish the CT/Rogowski/shunt class as the edge-fidelity standard). The
reference chain's own uncertainty budget is constructed GUM-style per the
EV01/P0008 template — this is a direct, small-scale exercise of the
proposed WP-C methodology (C06) on a current (not field) measurand.

**Test bed.** One WBG half-bridge cell (SiC or GaN evaluation
board/module), driven in (1) double-pulse mode and (2) continuous PWM buck
mode into an inductive load; bus voltage escalated in stages (first
48-100 V, then only with qualified supervision toward 400 V-class); sensor
heads mounted on the same conductor section with interchangeable positions;
temperature chamber (or controlled hotplate enclosure) for drift runs.

**Measurements (pre-registered).**
1. Static DC sweep over each sensor's rated range vs the zero-flux
   reference; gain/offset with uncertainty budget.
2. Small-signal frequency response via injected ripple at fixed DC bias.
3. Double-pulse edge capture vs coaxial shunt (amplitude/settling/delay).
4. EMI susceptibility: error vs switching state at the dV/dt and dI/dt the
   cell actually produces (measured, not assumed), sensor at fixed
   distances/orientations from the switching node; repeat with the sensor
   conductor carrying zero current (pure interference pickup).
5. Temperature drift over a stated range (e.g. 25-85 C, chamber-limited)
   at fixed bias; then an 8-24 h soak at constant conditions.

**Controls.**
- Reference channels shielded and cross-checked against each other in the
  overlap band (and their mutual consistency treated as consistency ONLY —
  per C23/Theorem-1 discipline, mutual agreement is never absolute
  calibration; absoluteness enters solely through the certificated
  zero-flux chain).
- Sensor-absent and current-absent runs to establish noise/pickup floors.
- Position/orientation swaps to separate conductor-geometry sensitivity
  (EV17 class) from technology-intrinsic error.
- Switching-disabled (DC-only) runs at matched dissipation to separate
  thermal from EMI effects.
- Pass/fail thresholds pre-registered against P0050's requirement
  synthesis (EV27) BEFORE data taking; analysis scripts frozen first
  (FT-02-style honesty discipline, C31/C48).

**Success criteria.** A defensible, uncertainty-budgeted comparison table
(DC accuracy, usable bandwidth, EMI-induced error, drift) in which the
combined reference uncertainty is demonstrably smaller than the
inter-technology differences being resolved; a clear verdict on whether a
Hall-class DC channel meets, misses, or ties the TMR class against
P0050-derived requirement classes in a switching environment — the
comparison B15 shows is missing (M6) and B10 needs (C43).

**Kill criteria.**
- Methodological kill: if the reference chain's achieved uncertainty
  cannot be closed below the Hall-vs-TMR differences, the benchmark is not
  decision-grade — stop, report, fix the chain before rerunning.
- Wedge kill: if BOTH channel classes' EMI-induced error under realistic
  switching exceeds their claimed accuracy class by margins that no
  bolt-on calibration discipline repairs, the calibrated-telemetry slivers
  of C-01/C-13 die as differentiators, and F-06's magnetics-adjacent
  modality option dies with them (B20's stated F-06 falsifier) — the
  zero-flux/FOCS incumbent path stands.
- GaN-die kill (only if the optional die is included): die performance
  uncompetitive with commercial Hall confirms that any GaN-sensor power
  story is packaging/environment-based, not performance-based (EV11).

**Cost range (EST, labeled).** ~$8k-25k if scope/DAQ and a chamber exist
in-lab: WBG evaluation cell and gate drive (~$1-3k), commercial
Hall/TMR sensors and eval boards (hundreds of dollars), coaxial shunt
(~$1-2k), zero-flux reference (dominant item — purchase EST $5-15k, or
substantially less if borrowed/rented from a magnet lab or metrology
group, which the F-06/F-02 buyer community plausibly enables per B20),
fixtures/isolation (~$1-2k). Time EST: 3-6 bench-weeks plus analysis.

**Safety.** Bench power-electronics practice: interlocked/enclosed DUT,
capacitor discharge verification before touching, appropriately rated
differential/isolated probes, no live probing at elevated bus, staged
voltage escalation (48-100 V first; 400 V-class only with qualified
supervision), thermal monitoring of the cell and load. Honest note: safe
practice at elevated DC bus is itself a competence not evidenced in B10's
ledger — supervision or partnership with a power-electronics lab is part
of the experiment design, not optional. This paragraph is research
planning, not a safety approval (SOURCE_POLICY).

**PhD value (publishable even if no startup occurs).** Closes B15 gaps
M6/G5 — a head-to-head that the corpus's own review layer (P0050) calls
for and nobody has published; directly informs B10 C43 (TMR as the
sharpest single-channel challenger), the decisive competing-channel datum
for the whole hybrid-diagnostic value case; exercises WP-C-class
uncertainty budgeting (C06) on a bench current measurand, producing
methodology practice and a plausible instrumentation-comparison
publication regardless of any venture; independent of HSX machine time
and, with commercial sensors, independent of the C04 anomaly.

**Startup value (which ideas it de-risks).** C-01: tests whether the
condition-monitoring/telemetry sliver can carry an acceptance-grade
(calibrated) claim under switching EMI — the only PhD-adjacent lane in the
corpus's top consensus idea. C-13: same test for pump-driver telemetry
against P0048/P0056-class references. F-06: resolves the modality
question (Hall/TMR vs zero-flux/FOCS) that its record leaves open, and is
B20's named falsifier for the F-06 bridge in both directions. Feeds B40
the "decisive datum for any startup-facing sensing claim" that B15's BT-6
entry already anticipated.

## 2. Explicit separations honored

- Radiation compensation is NOT tested here and is not claimed: PB-1 is a
  bandwidth/EMI/drift experiment (C08-class territory), not a C09
  experiment. Radiation work stays collaborator-led (C09) — see BT-5
  pointer below.
- Mutual channel consistency within PB-1 is used only as a cross-check;
  every absolute statement routes through the certificated zero-flux
  chain (C23/EV32 discipline).

## 3. Pointers preserved for the full run (NOT developed here)

- **BT-5 piggyback (from E-10/B20 handoff):** add AlGaN/GaN Hall-plate
  coupons plus a material-diverse witness channel to any collaborator's
  scheduled irradiation campaign — closes M1, decides whether radiation
  compensation is needed at all (B10 names "no" as a good outcome).
  Collaborator-led, never on the PhD critical path (C09).
- **BT-8 desk audit:** trace EV07/EV08's review-layer headline figures
  (~99% efficiency, ~100x frequency, 200-300C SiC) to verified primaries
  before any full-run conclusion reuses them. Required hygiene; desk-only.
