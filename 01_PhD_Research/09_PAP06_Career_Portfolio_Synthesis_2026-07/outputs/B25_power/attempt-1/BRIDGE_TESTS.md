# BRIDGE_TESTS — B25_power (FULL)

Stage: `B25_power` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

RANKED ladder of low-cost experiments. Ranking criterion carried from B15
§5: (decision leverage over the PhD/startup evidence base) x (what the
corpora show nobody else has done) / cost. PB-1 is carried from the
accepted pilot (BT-6 class, extended); PB-2 through PB-6 are added because
the full 31-row set justifies them; PB-7 carries the pilot's BT-5 pointer
into a developed entry. Every cost figure is an EST label, not a quote.
Safety paragraphs are research planning, not safety approvals
(SOURCE_POLICY). §4 records what is deliberately NOT on the ladder.

## Ranked ladder (summary)

| Rank | ID | One line | Cost EST | Ideas de-risked |
|---|---|---|---|---|
| 1 | PB-1 | DC-capable current-channel benchmark under WBG switching EMI, traceable reference chain (BT-6 extended; carried) | $8-25K | C-01, C-13, F-06, G-03, F-01 sliver, ST01-C10 chain, ST03-ID_08/12, W1/W2 |
| 2 | PB-2 | Uncertainty-budgeted acceptance-dossier exercise on purchased transducers (WP-C rehearsal on a current measurand) | $3-10K incremental | G-03, F-06, C-05, D-09, C-22 acceptance layer, C-09 sliver, E-14 thin link, W1 |
| 3 | PB-4 | Fluxgate/zero-flux excitation-band aliasing under switching EMI: locked vs free-running demodulation (PB-1 extension) | $1-4K incremental | ST03-ID_08, ST03-ID_12, ST01-C10 measurement chain, F-06 modality, W2 |
| 4 | PB-3 | Pre-registered DC series-arc / ground-fault discrimination statistics at low-voltage bench scale | $2-8K | C-01 sliver, ST01-C06P, F-12/A-02 family context, D-01/ST01-C11 methodology, W1/W2 |
| 5 | PB-5 | Trusted current/field excursion chain on converter-driven ramps (BT-3/FT-05 linkage) | $1-5K incremental (bench) to partner-scale | F-06 magnet leg, F-02 reverse sliver, ST01-C10 test-stand lane, PhD reverse-direction claim |
| 6 | PB-6 | Desk audits: BT-8 primary tracing of EV07/EV08 headline figures + certification-scope mapping for the product rows | $0 (desk) | hygiene for all converter rows; C-01/ST01-C10 cert planning |
| 7 | PB-7 | Irradiation piggyback: AlGaN/GaN Hall-plate coupons + material-diverse witness on a collaborator's campaign (BT-5/FT-11; collaborator-led) | founder cost low; campaign not founder-funded | E-10, D-16, radiation-instrument variants of F-06/D-09; closes M1 |

## 1. PB-1 — DC-capable current-channel benchmark under WBG switching EMI (carried from the pilot; BT-6 class, extended)

**One-line thesis.** Nobody in the B15 corpus has benchmarked Hall against
TMR (or any DC-capable channel) inside an operating WBG converter cell
(M6/G5, EV28); this is simultaneously the decisive datum for B10's
competing-channel question (C43) and for every power-facing sensing claim
in this stage's 31 rows.

**Measurand.** Current in one conductor of a WBG switching cell,
decomposed into: (a) DC transfer accuracy (gain, offset) against a
traceable reference; (b) small-signal bandwidth (amplitude/phase vs
frequency); (c) transient fidelity during switching edges; (d) EMI-induced
error under realistic dV/dt and dI/dt; (e) offset/gain drift vs
temperature and over a multi-hour soak.

**Devices under test.** (i) Commercial Hall-based current sensor(s)
(open-loop and/or closed-loop); (ii) commercial TMR-based sensor (EV28's
incumbent class, P0060-P0062 lineage); (iii) OPTIONAL, non-gating: the
PhD's GaN Hall die with the C13 readout chain — ONLY if the ~109x anomaly
(C04) has closed; the experiment is decision-grade with commercial sensors
alone and is NOT gated by C04.

**Reference chain.** DC/low-frequency: zero-flux/fluxgate transducer of
merchant calibration grade (1 ppm-linearity class exists commercially —
Danisense DQ500ID, S-B25-02 — marketed for current calibration; ideally
borrowed/rented with a calibration certificate; the magnet-lab buyer
community, S-B20-02, plausibly enables the loan). Transient: wideband
coaxial shunt (P0048/P0056 establish the CT/Rogowski/shunt class as the
edge-fidelity standard). The reference chain's own uncertainty budget is
constructed GUM-style per the EV01/P0008 template — a direct small-scale
exercise of proposed WP-C methodology (C06) on a current measurand.

**Test bed.** One WBG half-bridge cell (SiC or GaN evaluation
board/module) in (1) double-pulse mode and (2) continuous PWM buck mode
into an inductive load; bus voltage staged (48-100 V first; 400 V-class
only with qualified supervision); sensor heads on the same conductor with
interchangeable positions; temperature chamber or controlled enclosure for
drift runs.

**Measurements (pre-registered).**
1. Static DC sweep over rated range vs the zero-flux reference;
   gain/offset with uncertainty budget.
2. Small-signal frequency response via injected ripple at fixed DC bias.
3. Double-pulse edge capture vs coaxial shunt (amplitude/settling/delay).
4. EMI susceptibility: error vs switching state at measured (not assumed)
   dV/dt and dI/dt, at fixed distances/orientations from the switching
   node; repeated with the sensed conductor at zero current (pure pickup).
5. Temperature drift over a stated range (e.g. 25-85 C, chamber-limited)
   at fixed bias; then an 8-24 h soak at constant conditions.

**Controls.** Reference channels shielded and cross-checked in the overlap
band, with mutual consistency treated as consistency ONLY (C23/Theorem-1
discipline; absoluteness enters solely through the certificated zero-flux
chain); sensor-absent and current-absent runs for noise/pickup floors;
position/orientation swaps to separate conductor-geometry sensitivity
(EV17 class) from technology-intrinsic error; switching-disabled DC-only
runs at matched dissipation to separate thermal from EMI effects;
pass/fail thresholds pre-registered against P0050's requirement synthesis
(EV27) BEFORE data taking; analysis scripts frozen first (FT-02-style
honesty discipline, C31/C48).

**Success criteria.** A defensible, uncertainty-budgeted comparison table
(DC accuracy, usable bandwidth, EMI-induced error, drift) in which the
combined reference uncertainty is demonstrably smaller than the
inter-technology differences being resolved; a clear verdict on whether a
Hall-class DC channel meets, misses, or ties the TMR class against
P0050-derived requirement classes in a switching environment — the
comparison B15 shows is missing (M6) and B10 needs (C43).

**Kill criteria.** Methodological kill: if the reference chain's achieved
uncertainty cannot close below the Hall-vs-TMR differences, the benchmark
is not decision-grade — stop, report, fix the chain. Wedge kill: if BOTH
channel classes' EMI-induced error under realistic switching exceeds their
claimed accuracy class by margins no bolt-on calibration repairs, the
calibrated-telemetry slivers of C-01/C-13 die as differentiators and
F-06's magnetics-adjacent modality option dies with them (B20's stated
F-06 falsifier) — the zero-flux/FOCS incumbent path stands. GaN-die kill
(only if included): die performance uncompetitive with commercial Hall
confirms any GaN-sensor power story is packaging/environment-based, not
performance-based (EV11).

**Cost (EST).** ~$8-25K if scope/DAQ and a chamber exist in-lab: WBG
evaluation cell and gate drive (~$1-3K), commercial Hall/TMR sensors
(hundreds), coaxial shunt (~$1-2K), zero-flux reference (dominant item —
purchase EST $5-15K, or much less borrowed/rented), fixtures/isolation
(~$1-2K). Time EST 3-6 bench-weeks plus analysis.

**Safety.** Bench power-electronics practice: interlocked/enclosed DUT,
capacitor-discharge verification before touching, rated
differential/isolated probes, no live probing at elevated bus, staged
voltage escalation, thermal monitoring. Honest note: safe practice at
elevated DC bus is itself a competence not evidenced in B10's ledger —
supervision or partnership with a power-electronics lab is part of the
design, not optional.

**PhD value.** Closes B15 gaps M6/G5 (a head-to-head the corpus's own
review layer calls for and nobody has published); informs C43 (TMR as the
sharpest single-channel challenger); exercises WP-C-class uncertainty
budgeting (C06) on a bench current measurand; plausible
instrumentation-comparison publication regardless of any venture;
independent of HSX machine time and, with commercial sensors, of C04.

**Startup value / ideas de-risked.** C-01: whether the
condition-monitoring sliver can carry an acceptance-grade (calibrated)
claim under switching EMI. C-13: the same for pump-driver telemetry
against P0048/P0056-class references. F-06: the modality question
(Hall/TMR vs zero-flux/FOCS), B20's named falsifier in both directions.
G-03: the instrument-island content at bench scale. ST01-C10/ST03-ID_08/
ID_12: whether magnetics-adjacent channels have any place in the precision
measurement chain the magnet-converter records center on. Feeds B40 the
decisive datum B15's BT-6 entry anticipated.

## 2. PB-2 — Uncertainty-budgeted acceptance-dossier exercise (W1's product motion, rehearsed at bench scale)

**Thesis.** Every W1 wedge row (G-03, F-06, C-05, D-09) sells the same
artifact class: a signed, uncertainty-budgeted acceptance dossier built on
purchased instruments. The corpora show the skill is scarce (EV01 single
traceable-budget exemplar; EV35/G3/M3) and the wedge's commercial test is
whether such a dossier is producible at credible quality by this founder —
before any customer engagement exists.

**Measurand/measurements.** DC transfer and drift of a complete purchased
current-measurement chain (zero-flux transducer + burden + DAQ) on a bench
current loop: (1) full GUM-style budget with every component named
(reference certificate, burden TC, DAQ linearity, thermal, EMI floor from
PB-1 data); (2) a repeat-measurement campaign (>=3 re-setups) testing
whether the budget's reproducibility term is honest; (3) a written
acceptance dossier in G-03's artifact format (protocol, results, budget,
pass/fail against a pre-stated spec class).

**Controls.** Budget frozen before the repeat campaign (FT-02-style);
deliberately perturbed setup (cable swap, position shift) to test whether
the budget catches its own stated sensitivities; a second analyst pass on
the raw data (or a re-derivation after an interval) to test dossier
reproducibility.

**Success.** The repeat campaign lands inside the pre-stated budget at the
stated coverage; the dossier is complete enough that a third party could
re-execute the protocol. **Kill.** Repeats fall outside the budget and the
discrepancy cannot be attributed within the budget's own terms — the
methodology claim (C06-class) is not yet credible at even bench scale;
report and fix before any W1 customer conversation.

**Cost (EST).** $3-10K incremental over PB-1 (reuses its reference chain;
adds calibration certificate costs and bench time). 2-3 bench-weeks.

**Safety.** Low-voltage bench practice; same staging rules as PB-1.

**PhD value.** Direct rehearsal of WP-C's uncertainty discipline (C06) on
hardware not gated by C04; produces a worked GUM template transferable to
the field-measurand version; methodology-practice value even if no
startup occurs.

**Startup value / ideas de-risked.** G-03 (the dossier IS its product);
F-06 (open-protocol credibility); C-05 (method-authority class
generalization); D-09 (traceability rehearsal); C-22/E-14/C-09 thin-link
conditions (each requires exactly this deliverable class to upgrade);
W1 as a whole.

## 3. PB-4 — Fluxgate excitation-band aliasing under switching EMI (PB-1 extension; the startup corpus's mechanism, tested)

**Thesis.** ST03-ID_08's claimed inventive mechanism — unsynchronized WBG
edge fields alias into a zero-flux transducer's second-harmonic detection
band as a drifting false DC that a regulation loop would servo onto — is
asserted by the record, untaught in its charted prior art, and
undemonstrated. It is a pure measurement-physics question, answerable
without building any converter product, and it decides how much of the W2
measurement-chain thesis is real.

**Measurand/measurements.** Demodulated DC-output error of a
fluxgate-principle head with ACCESSIBLE excitation (a hand-wound
nanocrystalline-toroid head with own excitation/demodulation AFE, per the
record's own $800 BOM line — built as an instrument, not a converter),
mounted on PB-1's switching cell: (1) in-band residue spectrum near the
excitation second harmonic vs switching state; (2) DC-output error with
free-running excitation vs excitation phase-locked to the PWM clock;
(3) error vs deliberate excitation/PWM frequency-ratio detuning (mapping
the alias structure); (4) zero-current runs (pure pickup) at both
settings.

**Controls.** Same cell, same position, lock on/off as the ONLY variable;
sham-lock control (locked to an unrelated clock) to separate locking per
se from the specific phase relation; edge-rate variation via gate-resistor
swaps to test the claimed edge-rate dependence; commercial sealed head
alongside as the it-cannot-be-fixed-in-package baseline.

**Success.** A quantified alias map: reproducible in-band residue that
converts to a DC error of stated magnitude, reduced by a stated factor
(the record's own gate is >20 dB) under lock. **Kill.** Free-running
residue at realistic edge rates is negligible or trivially filterable —
ID_08's core mechanism (and part of ID_12's premise) loses value; PB-1's
DC channels are cleaner than feared; report the negative result (it is
publishable either way).

**Cost (EST).** $1-4K incremental over PB-1 (toroids, AFE PCB, clock
hardware). 2-4 bench-weeks.

**Safety.** As PB-1; no new hazard class.

**PhD value.** A novel, publishable instrumentation-noise mechanism study
squarely in the EV27/EV28 gap family (EMI-limited DC-capable sensing in
switching environments); exercises exactly the weak-signal-under-EMI
discipline (C03 class) the PhD claims; zero dependence on C04 or HSX.

**Startup value / ideas de-risked.** ST03-ID_08 (its non-obviousness
evidence or its kill); ST03-ID_12 (whether in-operation chains need
divergence protection against this mechanism); ST01-C10 (whether the
measurement-chain moat is real physics or packaging); F-06 (modality
robustness under converter EMI).

## 4. PB-3 — DC series-arc / ground-fault discrimination statistics at low-voltage bench scale

**Thesis.** The one sliver two corpora independently converged on
(P3R2-C-01's condition-monitoring/arc-discrimination layer; ST01-C06P's
entire product) is a detection-statistics claim: that arc/ground-fault
signatures on a DC bus can be discriminated from load noise with
qualifiable false-alarm/missed-detection rates. Founder-scale evidence is
buildable at low voltage with honesty-test discipline.

**Measurand/measurements.** On a 48-100 VDC bench bus with realistic
switching-converter load noise (PB-1's cell as the noise source):
(1) labeled signature library — series-arc events from a controlled
arc-generator fixture (opening-contact type), plus ground-leakage steps
via switched resistor paths to a grounded plane; (2) spectral/temporal
feature statistics of events vs load-transient confounders (converter
start/stop, load steps); (3) pre-registered detector evaluation:
ROC-style false-alarm vs detection rates on a held-out event set;
(4) localization trial: leakage-step attribution between two bus segments
from distributed current measurements (EV16-class inverse reasoning at
toy scale).

**Controls.** Detector thresholds and features frozen before the held-out
set is unblinded (FT-02/C31 discipline — the estimator-honesty test
applied to a detection product); confounder-only runs; arc-fixture
electrode conditioning logged (arc statistics are notoriously
condition-dependent); repeat days to expose drift in the signature
library.

**Success.** A pre-registered detector achieving stated false-alarm and
detection rates on held-out events, with localization attribution better
than chance between segments; an honest transferability statement.
**Kill.** Discrimination statistics cannot beat trivial threshold
detectors on held-out data — the protection-intelligence sliver
(C-01/ST01-C06P) has no technical premise at founder scale; report.

**Explicit scale honesty.** Results at 48-100 V do NOT transfer directly
to 800 VDC arc physics or to any certification claim; the 800 V version
requires partner infrastructure and a power lab (ST01-C06P's own
venture-level proof). This test buys the statistics methodology and a
bench-truth dataset, nothing more.

**Cost (EST).** $2-8K (arc fixture, contactors, resistor networks, DAQ
reuse). 3-5 bench-weeks.

**Safety.** DC arcs are an ignition and eye hazard even at low voltage:
enclosed arc fixture, fume handling, eye protection, current limiting,
no flammables, interlocked supply; ground-fault injections only on the
isolated bench bus. Staying at <=100 V is a deliberate safety boundary of
this design.

**PhD value.** A real detection-statistics dataset under converter EMI
for estimator-honesty methodology (C23/C31 practice, BT-1-adjacent);
weak-signal discrimination is the same problem class as quench-detection
false-trigger statistics (EV06/EV23) — one methodology, two applications.

**Startup value / ideas de-risked.** ST01-C06P (its founder-scale
technical premise); C-01 (the sliver's upgrade condition evidence); D-01/
ST01-C11 (the shared false-trigger methodology); F-12/A-02 (family
context).

## 5. PB-5 — Trusted excursion chain on converter-driven ramps (BT-3/FT-05 linkage)

**Thesis.** The PhD's most distinctive unsupported claim — coil-referenced
Hall-GAIN recovery (C26 gap b; EV32: no corpus precedent) — requires a
trusted current/field excursion chain. The power-map rows that own such
chains (F-02's skids, ST01-C10's test stands, F-06's magnet leg) make the
power domain the natural host: a converter-driven inductive-load ramp IS
the excursion source B10's FT-05 needs.

**Measurand/measurements.** On PB-1's bed (bench tier) or a magnet-lab
partner's drive (partner tier): (1) programmed current ramps through an
inductive load generating a known field excursion at a Hall/coil sensor
pair via a calibrated field coil; (2) coil-chain reference established
against the certificated DC chain (PB-2's budget); (3) Hall gain recovered
from the excursion per the FT-05 protocol; recovered gain compared against
the Fisher-predicted interval (C23); (4) offset explicitly NOT claimed
recoverable (Theorem-1 discipline — the test verifies the estimator
refuses it).

**Controls.** Excursion profiles varied (rate, amplitude, dwell) to test
identifiability predictions (C23 Case structure); chain swapped between
certificated and uncertificated references to demonstrate that gain
recovery quality tracks reference trust (the entire point of §6's
discipline); frozen analysis before unblinding.

**Success.** Gain recovered within the predicted interval using the
trusted chain, degraded exactly as predicted with the untrusted chain; a
clean, publishable first test of the reverse direction (corpus-bounded
claim per B15's honesty rule — FT-01 kill search still required before
any publication novelty claim). **Kill.** Recovery fails with the trusted
chain — C26 gap (b) claims retire; the architecture collapses to the
proven forward direction (itself a publishable negative, per BT-3).

**Cost (EST).** $1-5K incremental at bench tier (field coil, fixtures);
partner tier is a collaboration ask into the S-B20-02 magnet community,
not a purchase. 2-4 bench-weeks.

**Safety.** Bench tier as PB-1. Partner tier inherits the host lab's
stored-energy safety regime — founder does not run magnet hardware.

**PhD value.** Directly executes FT-05/BT-3, the decisive
reverse-direction test (M2); links it to C23's predictions; independent
of HSX scheduling at bench tier.

**Startup value / ideas de-risked.** F-06's magnet-system leg (excursion
capture as a product function); F-02's reverse sliver and B20 upgrade
condition; ST01-C10's test-stand lane (a trusted excursion service is a
W2 offering); demonstrates to the magnet community exactly the
qualification competence W2 sells.

## 6. PB-6 — Desk audits: BT-8 primary tracing + certification-scope mapping

**Thesis.** Two obligations the full run inherits but does not discharge:
(1) B15's BT-8 — trace the review-layer WBG headline figures (~99%
efficiency, ~100x frequency, 200-300C SiC; EV07/EV08) to verified
primaries before ANY downstream conclusion reuses those numbers (none
does yet, and none may until this closes); (2) the product rows'
certification surfaces are cited at scope level only (S-B25-01 abstract;
record-cited UL 61010 class; unverified ECCN 3A226 snippet) — a
desk mapping of which certification regime binds which row, with primary
scope documents opened, is required before B30/B50 use any of them for
planning.

**Method.** Desk-only: retrieve primaries for each headline figure;
record match/mismatch; open official scope pages for the named standards
where accessible (the IEC full text is paywalled — scope-level honesty
maintained); record failures honestly (the NERC official-PDF 403 this run
is the pattern). **Success.** Each reused figure either traced or struck;
each product row's certification cell either scope-verified or flagged.
**Kill criterion (for claims, not the test).** Any headline figure that
fails tracing is removed from all downstream use.

**Cost.** $0; 1-3 desk-days. **Safety.** None. **PhD value.** Citation
hygiene for any power-adjacent publication. **Startup value.** Prevents
building W1/W2 collateral on untraced review numbers; keeps
certification planning honest.

## 7. PB-7 — Irradiation piggyback (carried BT-5/FT-11 channel, now with two host candidates)

**Thesis.** E-10 and D-16 both preserve the same reverse channel: any
space-power qualification campaign buys irradiation access that could
host AlGaN/GaN Hall-plate coupons plus a material-diverse witness
channel, closing B15 gap M1 (zero GaN/AlGaN irradiation data; C29) as a
side effect. Collaborator-led by design (C09); NEVER on the PhD critical
path.

**Measurand/measurements.** Pre/post (and where possible in-situ) Hall
sensitivity, offset, and mobility-proxy parameters of packaged AlGaN/GaN
Hall plates at stated fluence points, species-matched to the host
campaign's spectrum; a metallic-Hall witness coupon per C30's
single-source reference (explicitly testing that thin dependency).

**Controls.** Unirradiated control coupons from the same wafer/packaging
lot; temperature logging separating thermal from radiation drift (the
C09 separation — this test is the (2)-problem of POWER.md §5 and must
not be conflated with SET/SEB device testing happening on the same
campaign); blind parameter extraction before dose labels are attached.

**Success.** Even a single-fluence-point dataset converts EV09/M1 from
Unknown to bounded — and B10 explicitly names "radiation compensation
unnecessary" as a good outcome. **Kill.** None at the idea level (any
outcome is informative); the channel dies only if no host campaign
materializes — in which case it stays a documented option, not a plan.

**Cost.** Founder-side: coupon packaging and characterization (EST low
$K, reuses C46 process); campaign costs are the host's. **Safety.**
Radiological safety is entirely the host facility's regime;
founder-side work is pre/post bench characterization only.

**PhD value.** Closes M1; decides whether C09's architecture is needed
at all; coupons reuse the demonstrated packaging process (C46).
**Startup value.** E-10/D-16 record closure; any future
radiation-environment instrument variant of F-06/D-09 inherits the
dataset.

## 8. Explicit separations and non-entries

- Radiation compensation is tested ONLY in PB-7; PB-1 through PB-5 are
  bandwidth/EMI/drift/statistics experiments (C08-class territory) with
  no radiation content — the POWER.md §5 separation enforced at ladder
  level.
- Mutual channel consistency is used only as cross-check everywhere;
  every absolute statement routes through certificated references
  (C23/EV32 discipline; PB-2 exists to institutionalize it).
- **Not on the ladder:** the startup corpus's own RTP plans (ID_08's
  $19.3K converter bench, ID_10's $14.7K protection bench, ID_12's
  $19.8K 90-day campaign, CF-4's sub-$1.5K rig) — they are converter/
  protection/control builds presuming capabilities B10 does not evidence,
  and they carry their own IP-wall and counsel gates that are that
  corpus's business, not this stage's. PB-4 deliberately extracts
  ID_08's measurement-physics core in an instrument-only form instead.
  ST05-CF-4 gets no slot for the same reason (thermal-control build; its
  own record bars safety representations pending sim rebuild).
