# POWER — B25_power (FULL)

Stage: `B25_power` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Specialized power converter/electronics/supply analysis across 31 distinct
ideas from the frontier (A30/B20) universe and the STARTUP corpus. Every
material claim maps to B15 evidence rows (EVxx) / papers (Pxxxx), B15
gap/bridge IDs (G/M/BT-x), B10 claims (Cxx), B20 alignment rows and
founder-fit corrections, A30-verified items (A30:*), corpus records cited by
path, or sources in SOURCES.csv (S-B25-xx; S-B20-xx = B20's opens).
Corpus-dated facts are record-vintage unless a live open is cited. This file
makes no portfolio ranking (disposition is not a B40 rank).

## 1. Scope, inclusion boundary, and sweep account

**Inclusion boundary (stated up front).** An idea is included when its
product, decisive engineering risk, or purchased deliverable is
(i) power conversion / supply / protection hardware (converters, supplies,
breakers, PMAD, drives, dump systems), or (ii) precision electrical
current/power/energy measurement, acceptance, or qualification serving
power-carrying systems. Boundary cases inside the map are labeled in their
`role` cells (C-05 energy-balance metrology; D-09 beam-current metrology;
D-10 power-adjacent only; D-19 power infrastructure with non-power decisive
risk).

**Sweep account — B20's 39-idea universe.** All 39 B20 rows were re-read
this run. Included (23): P3R2-C-01, C-13, F-06, E-10 (pilot four), A-02,
C-05, C-07, C-09, C-14, C-15, C-22, D-01, D-09, D-10, D-16, D-19, E-14,
F-01, F-02, F-03, F-12, F-23, G-03. Excluded, with reasons:

- **D-02** (tape QC metrology): measurement tool, but the measurand is tape
  Ic/defects, not electrical power — the primary alignment candidate lives
  in B20/B30, not here.
- **A-10** (IEDF metrology + bias retrofit): phase-1 core is plasma
  metrology; its phase-2 tailored-waveform bias engine is power-adjacent but
  the record's decisive risks are plasma-facing — the same-lane power idea
  F-01 is included instead, noted here so the exclusion is visible.
- **A-14** (300C instrumentation electronics): instrumentation ICs, not
  power conversion (its power-analog in the startup corpus, C27, fell from
  that corpus's own top-7 — S-B25-12).
- **E-04** (cryo readout), **G-01** (UHV conditioning), **A-05** (NEG
  coating), **A-22/F-16** (plasma process/materials), **C-04** (two-phase
  cooling), **C-08** (PCHE), **D-12** (EHD cold plates), **F-19** (coolant
  chemistry), **P5-USSCI2-S01/P5R2-CN-01/P5R2-CN-03**: thermal/fluids,
  materials, imaging, or commodity-metering disciplines — no power
  conversion or precision electrical metrology at their core.
- **C-12** (turbo-Brayton cryocoolers): thermodynamic machines; decisive
  risk is gas-bearing rotordynamics, not the drive electronics.

The task card's "A-01" has no corresponding row in B20's 39-idea universe
(checked against the full ALIGNMENT.csv); A-02 is the protection idea of
that class and is included.

**Sweep account — STARTUP corpus (8 rows).** Per B00's handoff, the audited
canonical synthesis (startup/01 `60_PHASE6_SYNTHESIS/00_EXECUTIVE_SUMMARY.md`)
was read, plus the Round-2 showdown, the startup/03 C10 deep dive and
founder profile, four startup/03 invention disclosures (ID_08, ID_10, ID_12
full; ID_13 partial), and the startup/05 CryoFree mission + strategy +
ID_04 disclosure. Included: **ST01-C10, ST01-C11, ST01-C06P** (startup/01
ideas C10, C11, C06-pivot — recorded IDs verbatim after a corpus prefix),
**ST03-ID_08, ST03-ID_10, ST03-ID_12, ST03-ID_13** (startup/03
`50_INVENTIONS` IDs), **ST05-CF-4** (startup/05 candidate CF-4 / disclosure
ID_04). Considered and not rowed: CF-1/CF-2/CF-6 (magnet-internal
interfaces/detection thresholds — not power electronics), CF-3 (DEFER per
its own strategy; sim self-flagged as artifact), CF-5 (killed DUPLICATED),
CF-7 (current-lead co-qualification — power-path-component acceptance, but
its disclosure was not read this run; noted rather than rowed), C12/C33/C15
(winding machines / coil QC / test magnets — magnet manufacturing, not
power), C01/C03 and C27 and C23 and V01 (aviation bricks, 250C power
platform, WBG characterization appliance, plasma-torch PSU — record support
read only at executive-summary/showdown level; V01's NO-GO and C-14's
convergence are used as evidence, and C23/C27/C01-C03 are named here so the
boundary is auditable rather than silently drawn). Audit status carried
from B00: startup/01 is the only audited startup sub-mission; startup/03 is
in-progress/unaudited; startup/05 self-reports complete with no audit
folder and a served-model caveat its own files repeat — all rows built on
them say so.

**Pilot carry disclosure.** The four pilot rows (C-01, C-13, F-06, E-10)
are carried with these disclosed refinements and no others: pilot-run
self-references removed; proof-experiment cells now point at the full
ladder (PB-x); C-01 gains the ST01-C06P cross-corpus triangulation and its
falsifier is sharpened by the startup corpus's record-vintage
shipping-SSCB claim; F-06's demand facts are refreshed live (S-B25-16/17,
with the official-NERC 403 and the stale Pattern page disclosed) and its
disposition is updated from "preliminary wedge candidate pending full-set
retest" to the full-set verdict of §9; E-10's disposition now names D-16 as
sharing the identical reverse channel. The old06 F-06 evidence record,
read only to line 80 in the pilot, was read in full this run (S-B25-10).

## 2. The map at a glance

| idea_id | Architecture (short) | Role | Status base | Disposition class |
|---|---|---|---|---|
| P3R2-C-01 | 800VDC protection shelf | full end product | consensus winner, WEAK fit | context for wedge, not founder-led |
| P3R2-C-13 | GaN pump-driver module | subsystem | WEAK | deprioritize; telemetry sliver only |
| P3R2-F-06 | Precision DC sensing platform | measurement tool | MEDIUM-boundary, weak commercially | W1 embodiment |
| P3R2-E-10 | Rad-tolerant GaN PPU | reference design | WEAK, killed canonical | retire; PB-7 channel |
| P3R2-A-02 | MVDC hybrid SSCB | full end product | killed | retire |
| P3R2-C-07 | AFE rectifier retrofit | full end product | killed, A30-verified | retire |
| P3R2-C-09 | Pulsed-power module platform | platform + reference design | split decision | PhD-independent |
| P3R2-C-14 | MW plasma-torch PSU | full end product | blind-only reject | retire (double-killed cross-corpus) |
| P3R2-C-15 | MW charge/swap infra | full end product | killed canonical | retire |
| P3R2-C-22 | Electrolyzer stress benches | qualification platform | OLD-2 winner class | PhD-independent; loses W1 retest |
| P3R2-C-05 | Thermal conformance metrology | qualification platform (boundary) | winner class, A30-verified revival | W1 family |
| P3R2-D-01 | Quench detection + protection | subsystem | winner class, MEDIUM | W2 family anchor (frontier side) |
| P3R2-D-09 | Traceable beam-current metrology | measurement tool (boundary) | revived, MEDIUM | W1 family (sleeper) |
| P3R2-D-10 | CBC phase-control engine | boundary (power-adjacent) | ADVERSE | retire |
| P3R2-D-16 | Space Brayton PCU + PMAD | full end product | killed/revived NEW-24 | retire; PB-7 channel |
| P3R2-D-19 | Flywheel kinetic buffers | full end product (boundary) | killed/revived NEW-20 | retire |
| P3R2-E-14 | MTDC relay + HIL platform | product + qualification platform | winner class, WEAK fit | HIL leg in W1 comparison |
| P3R2-F-01 | RF impedance-match engines | subsystem | OLD-4, WEAK fit | PhD-independent |
| P3R2-F-02 | Magnet BoP skids (10 ppm) | subsystem/product | NEW-cut, slivers | reconciled with ST01-C10 (§8) |
| P3R2-F-03 | Turbo-gen + converter cartridge | full end product | OLD-only 24 | retire |
| P3R2-F-12 | Marine DC protection stacks | full end product | OLD-only 17 | retire |
| P3R2-F-23 | Electrolyzer envelope controllers | subsystem | OLD-22/NEW-23 | retire |
| P3R2-G-03 | DC acceptance instrumentation | measurement tool | boundary WEAK/MEDIUM | W1 family (nearest-term) |
| ST01-C10 | Fast-dynamics magnet converters | full end product family | startup rank-2, Medium | W2 application field |
| ST01-C11 | Detection-first MPMU | subsystem/product line | startup rank-4, rescoped | W2 detection leg |
| ST01-C06P | 800VDC protection intelligence | subsystem | startup rank-3, Medium | W1/W2-adjacent applied lane |
| ST03-ID_08 | FastCoil PWM-locked chain | reference design / building block | red-teamed INVENT | W2 evidence; PB-4 |
| ST03-ID_10 | Quench-safe converter system | full end product | red-teamed INVENT | W2 boundary exemplar |
| ST03-ID_12 | Self-calibrating ppm chain | measurement tool | red-teamed INVENT | W2 calibration exemplar |
| ST03-ID_13 | Per-coil 4Q array drive | subsystem | red-teamed INVENT (partial read) | W2 family context |
| ST05-CF-4 | Cold-head ramp governor | subsystem | NARROW-NOVEL, G-PHYS REVISE | context; designs AROUND Hall lane |

All four roles are populated: 12 full end products, 10 subsystems, 6
measurement/qualification platforms, 3 reference-design/platform rows.
Winners (C-01, C-05, C-22, D-01, E-14, F-01, ST01-C10) and killed/cut ideas
(A-02, C-07, C-14, C-15, D-16, D-19, F-03, F-12, F-23, E-10's canonical,
D-09's OLD kill) are both represented, as required.

## 3. Where Hall/coil sensing concretely enters — across the full set

Bandwidth reality first, carried from B15 and unchanged by the larger set:
the power-conversion stream's requirement synthesis (EV27/P0050) puts WBG
switching-current measurement at ~50 MHz-class need; Hall responds typically
below ~100 kHz with temperature/offset drift burdens; TMR is usually
low-pass-filtered below ~50 kHz in switching environments (EV28/P0050).
**Trip-grade and edge-fidelity sensing is shunt/CT/Rogowski territory
(P0048/P0056); the Hall/TMR class competes only for DC/low-frequency
content those AC devices cannot see (EV27/EV34).** The seven stage-named
functions, applied where the full set makes them concrete:

- **Ripple.** Rectifier/electrolyzer DC ripple metering (C-07/C-22/F-23
  applications; F-06's electrolyzer leg); drive-current ripple as pump-diode
  stability telemetry (C-13); interleave-residual ripple in precision magnet
  converters — where ST03-ID_08's whole inventive step is that ripple and
  switching edges alias INTO the zero-flux measurement chain unless the
  chain's clocks are locked to the PWM ensemble. Ripple is thus not only a
  measurand but a corruption mechanism for the DC channel itself (PB-4).
- **Transients.** Precharge/inrush profiling and hot-swap verification
  (C-01); nanosecond pulse fidelity (C-13 — CT/Rogowski territory per
  P0048/P0056); HVDC fault recording (F-06/E-14); pulsed-power droop/jitter
  acceptance (C-09); trip-event capture with common-clock timestamping
  (ST03-ID_13 claim 6).
- **Current sharing.** Paralleled feeds/shelves (C-01); paralleled GaN
  stages and diode strings (C-13); parallel rectifier/stack paths (F-06);
  N+1 module paralleling to multi-kA (ST01-C10); coordinated dump-duty
  shares across converter+absorber modules (ST03-ID_10); per-coil channels
  on a shared bus with energy recycling (ST03-ID_13). The array
  current-measurement error literature (EV17) is occupied ground any such
  product must meet.
- **Ramp/dump.** The full set gives this function real native instances the
  pilot four mostly lacked: magnet drive-and-dump skids (F-02), quench-safe
  dump supervision with pre-ramp stored-energy verification (ST03-ID_10),
  magnet-current excursion capture (F-06's magnet leg — precisely the
  trusted-excursion infrastructure the PhD's coil-referenced tests need,
  BT-3/FT-05, PB-5), and thermal-budget-governed ramping (ST05-CF-4 — which
  deliberately uses NO magnetic sensing, see §6 note).
- **Protection.** The microsecond trip itself needs di/dt- or shunt-class
  speed everywhere (C-01, A-02, E-14, F-12, ST03-ID_10); DC-capable
  channels serve the slower layers: precharge supervision, overload
  trending, reverse-current checks, capacity-verification interlocks
  (ST03-ID_10's L-measurement), and detection statistics (D-01, ST01-C11).
- **Fault localization.** Series-arc signature discrimination and
  ground-fault LOCATION on ungrounded DC buses — the EV27-class
  weak-signal-plus-EV16-class inverse-localization sliver B20 found inside
  C-01, which the startup corpus independently scoped as an entire product
  (ST01-C06P); distributed station metering (F-06); arc localization prior
  art exists (P0025/EV16).
- **Calibration.** The function that separates the wedge rows from the
  rest: F-06 sells it; G-03 sells the signed dossier; C-05 sells the
  round-robin; D-09 sells the traceable reference; ST03-ID_12 productizes
  in-operation self-calibration WITH a divergence watchdog; ID_10 publishes
  self-measured latency as a machine-readable figure. Uncalibrated
  telemetry is a commodity feature every vendor ships; every acceptance- or
  warranty-grade claim in the set routes through §6's discipline.

## 4. Converter-stack reality check — what the PhD does NOT cover

A real specialized-converter product stands on: topology selection and
control design; gate drive (open WBG burden — EV08, review-level, headline
figures still untraced, PB-6); SiC/GaN device selection and reliability
(EV31); magnetics; insulation coordination; EMI/EMC compliance; thermal
design; deterministic controls and HIL validation; safety engineering and
certification (IEC 62477-1 class for <=1500 VDC systems, S-B25-01; NRTL
UL 61010-class for lab/test products per the startup record; classification
rules for marine, F-12; ECSS-class for space, E-10/D-16); manufacturing/
DFM; reliability; field service; supply chain. Protection products add
fault-energy absorption, interruption physics, and arc validation; pulsed
power adds HV insulation and test technique (IEC 60060-1-class,
B20-recorded, C-09); utility-facing rows add qualification authority and
safety-rated field work (E-14, G-03, F-06).

Against B10's ledger the PhD demonstrably covers **none of that stack** —
in any of the 31 rows. What it does cover: instrumentation-grade bench
readout design and EMI discipline (C03/C13 — small-signal,
emulator-validated, ~109x anomaly C04 open); harsh-environment sensor
packaging (C46/C01); proposed traceable-calibration methodology (C06,
gated by C04); proposed estimator/identifiability methodology (C23/C31,
pre-redteam C40). B15's structural adjudication is explicit: in specialized
converter work, application-specific topology/control differentiates and
measurement is supporting infrastructure (EV30); GaN materials vocabulary
is not a competitive capability in power-device markets (EV31). The startup
corpus's own deep dive lands on the same split from the commercial side:
"ppm-class stability does not live in the switch. It lives in the
measurement chain" (S-B25-13).

**Plainly: magnetic-sensor expertise — even excellent, demonstrated
magnetic-sensor expertise — does not suffice to design, qualify, or certify
a power converter, a protection product, or a power supply, and nothing in
this stage's 31 rows should be read as implying it does.** The startup
corpus's founder-profile assertions of power-electronics capability are not
adopted (POWER_SKILLS.md §3). Missing capabilities are named per-row;
acquisition paths are costed in POWER_SKILLS.md.

## 5. Radiation compensation vs bandwidth fusion — separate problems

The three-way separation established at pilot holds across the full set and
gains one more instance:

1. **Bandwidth fusion** (C08 class): DC-capable channel + AC channel
   spanning DC-to-MHz. Cross-domain convergence is real (EV34: P0003
   synthetic Hall+coil; P0031 hardware TMR+CT). An estimator/architecture
   problem with no radiation content. PB-1/PB-4 territory.
2. **Radiation compensation** (C09 class): separating radiation-driven from
   temperature-driven *sensor drift* with anchors and witness channels.
   Zero GaN/AlGaN data either way (M1/EV09/C29); ~14x wrong-species scaling
   failure forbids substitution (C29). PB-7 territory, collaborator-led.
3. **SET/SEB mitigation in power devices** (E-10's and now also D-16's
   actual problem): single-event transients/burnout in switching topologies
   — device-level power reliability engineering (EV31), not sensor drift.

Conflating any two is the vocabulary trap B20 documented on E-10 and D-16
("GaN + radiation" / "space + radiation" are not mechanisms). A
power-facing sensing product can need (1) without (2); a space PPU/PMAD
needs (3) and neither of the others; only a radiation-environment
instrument needs (1) and (2) together — and they still fail independently
and must be tested separately (PB-1 vs PB-7; FT-11 vs bench fusion tests).

## 6. Traceability and uncertainty discipline

**Mutual Hall/coil (or any channel-pair) consistency is NOT absolute
calibration.** Formal basis carried: for an unreferenced DC + inductive
pair with constant gains/offsets, a two-parameter gauge transformation
leaves every measurement identical (C23 Theorem 1; C07) — the pair detects
disagreement but cannot attribute drift, and a DC-channel offset is
observationally identical to a static shift the inductive channel cannot
see. No corpus paper calibrates a DC channel from a coil reference (EV32);
the field's flagship hybrid deployment never bench-calibrated its coils
(EV04/P0001).

The full set adds a striking industrial echo: **ST03-ID_12's dissimilar-
sensor divergence watchdog exists precisely because "a self-correcting
chain can self-corrupt"** — its divergence trend gates every correction's
validity, and the record's own metrology honesty routes ABSOLUTE accuracy
through an external DMM+shunt anchor at 10-20 ppm while claiming only
RELATIVE ppm drift-tracking against a referee DCCT. That is the C23
discipline rediscovered in product form: divergence detection is
consistency information; absoluteness enters only through a certificated
reference chain. Likewise ST03-ID_10's "latency contract" publishes a
self-MEASURED figure with freshness gating — a qualification artifact, not
a self-certification.

Power-domain consequence, unchanged and now broader: converter telemetry
that "agrees with" its companion Rogowski/CT is not thereby calibrated;
acceptance-grade or warranty-grade claims (C-01's condition monitoring,
C-13's calibrated telemetry, G-03's dossiers, C-22's bankability data,
ST01-C06P's discrimination verdicts, everything F-06 and ST03-ID_12 sell)
require an external reference chain — zero-flux/calibrated-shunt class
(S-B25-02 1 ppm-linearity merchant grade; S-B25-15 10 ppm catalog supply
grade) — plus a GUM-style budget. The corpus's single traceable-budget
exemplar (EV01/P0008, ±150 mT, room temperature) and the unpublished
tesla-scale/harsh/traceable combination (EV35/G3/M3) still bound what
exists; WP-C (C06) is the proposed route to that scarce skill and remains
gated by C04. Note also ST05-CF-4's inverse lesson: the startup corpus
deliberately EXCLUDED magnetic-field sensing from its ramp governor to
stay clear of the funded lane and of FSU/NHMFL claims — the founder's own
missions do not treat Hall sensing as the power wedge.

## 7. Full end products vs measurement/qualification/reference platforms

Across 31 rows the role structure sharpens the pilot's finding:

- **Full end products** (12 rows) all carry the §4 stack plus a
  certification or classification campaign (IEC 62477-1 class C-01;
  MV switchgear A-02; CCS marine F-12; NRTL/CE ST01-C10/ID_10; space
  D-16/E-10-adjacent), high capital, and design-in/vertical-integration
  risk (CFS-style bundling recurs in F-02, ST01-C10, ST03-ID_13). In
  every one, the PhD contributes at most a non-core sliver. Consensus
  strength does not change this (C-01 is the corpus's top consensus idea
  and still WEAK on mechanism — B20's independence of axes).
- **Subsystems** (10 rows) trade certification for OEM-qualification
  burden; sockets are won on power-electronics performance (edge speed,
  BOM, restrike, recycling, dump duty), not measurement. The PhD-adjacent
  lanes are telemetry/detection slivers whose value must be proven as
  *calibrated/statistical* claims (PB-1/PB-3).
- **Measurement/qualification platforms** (6 rows) invert the structure:
  the product IS measurement authority (F-06 instruments, G-03 dossiers,
  C-05 round-robins, D-09 traceable references, C-22 bankability benches,
  ST03-ID_12 embedded calibration). Their safety burden is
  instrument-class; their hard burden is qualification authority itself.
  This is the only role class where the PhD's discipline is the core
  skill — with the honest caveat that C-22's core skill is
  electrochemical attribution, which is why it loses the §9 retest.
- **Reference designs/platforms** (3 rows) show that platform status does
  not lower the capability bar: E-10's credibility requires space-power
  qualification; C-09's requires HV pulsed-power authority; ST03-ID_08's
  requires converter bring-up. A reference design is a claim about
  qualified engineering, not a way to avoid it.

## 8. Technical/commercial comparison by family

- **DC protection family** (C-01, A-02, F-12, C-15, ST01-C06P, E-14's
  relay): converging demand story (DC buildout at rack, MV, marine, port,
  grid scale), converging risk story (interruption physics + certification
  + incumbent switchgear majors), and one converging surviving layer —
  protection INTELLIGENCE (discrimination/localization/condition
  monitoring). Two corpora reached that layer independently (B20's C-01
  sliver; startup C06-pivot's whole thesis), which is the strongest
  cross-corpus signal in this stage. Founder-led breaker/relay products:
  no. Founder-relevant discrimination statistics + calibrated telemetry:
  PB-3/PB-1 testable now.
- **Rectifier/electrolyzer family** (C-07, C-22, F-23): killed retrofit,
  qualification benches, envelope controllers. The measurement-flavored
  layer (bankability acceptance data) is real but the scarce skill is
  electrochemical attribution (B20), and A30-verified facts impaired the
  US retrofit window. No founder wedge; C-22 remains the family's honest
  venture.
- **Pulsed/RF family** (C-09, C-14, F-01, D-10 boundary): power-conversion
  platform engineering with acceptance-metrology slivers (droop/jitter,
  calibrated RF sensing). Cross-corpus note: the startup corpus's V01
  plasma-torch PSU reached NO-GO on the same buyer-structure grounds that
  killed C-14 — two independent pipelines, one verdict. D-10 stays ADVERSE.
- **Magnet-power family** (F-02, D-01, ST01-C10, ST01-C11, ST03-ID_08/10/
  12/13, ST05-CF-4): the deepest family, and the one where the frontier and
  startup corpora describe the SAME market layer from two sides — F-02's
  "10 ppm skids vs OCEM/Danfysik incumbents" is ST01-C10's "hole between
  CAENels catalog and OCEM/Danfysik customs" (incumbent grade verified
  live: Danfysik 10 ppm catalog, S-B25-15; demand context verified live:
  power systems the top fusion supply-chain bottleneck at 48%, S-B25-18).
  Within the family, every record that survives its own red team locates
  the durable value in the measurement chain (DD-C10's RT-4 concession;
  ID_08's timing architecture; ID_12's self-calibration; ID_10's latency
  contract; C11's detection-first rescope) — while the switching hardware
  is where the missing capabilities and capital sit. Reconciliation: one
  market layer, two entry postures — converter company (requires the §4
  stack, a 3-5 person team, unproven willingness-to-pay) vs
  measurement/qualification supplier to that layer (adjacent to
  demonstrated PhD discipline, PB-testable).
- **Space family** (E-10, D-16): both retired; both preserve the same
  reverse irradiation-piggyback channel, folded into PB-7 once.
- **Machines** (F-03, D-19): rotor/machine engineering dominates; retired.
- **Metrology/qualification family** (F-06, G-03, C-05, D-09, C-22's
  acceptance layer, E-14's HIL leg, ST03-ID_12): compared in §9.

## 9. Preferred wedges (full-set verdict; falsifiable)

The pilot's preliminary wedge — the measurement/qualification/telemetry
layer, not any converter end product — was retested against the complete
qualification-platform family (C-05, C-22, G-03, E-14's HIL leg, D-09) and
the startup corpus. It **survives, and resolves into two genuine wedges**
(plural because they have different buyer communities, different record
bases, and different failure modes):

**W1 — DC-asset measurement & qualification authority** (grid/datacenter/
industrial DC): the F-06 instrument-plus-open-protocol posture, the G-03
signed-dossier acceptance lane (nearest-term, lowest capital), the
C-05-class round-robin method authority (proves the wedge class
generalizes), and D-09 as the sleeper traceable-reference instrument.
Reasoning: (a) every non-WEAK forward mechanism B20 found runs through
measurement authority; (b) the corpus-verified scarce skill is traceable
uncertainty at scale (EV01 single exemplar; EV35/G3); (c) the demand wave
is live-refreshed (PRC-028-1 full compliance 2030-01-01, S-B25-16;
Southern Spirit 2029/2032 targets, S-B25-17 with staleness disclosed);
(d) the family's losing member is instructive — C-22 fails the retest
because its scarce skill is electrochemical, confirming the wedge is
metrology authority, not "testing" generically. Against: E-14's HIL leg
shows qualification platforms can still demand domain firmware skills the
founder lacks; W1 plays must stay on the measurement-uncertainty side of
that line.

**W2 — magnet-power measurement-chain and protection-detection authority**
(fusion/magnet community): the calibrated DCCT-chain qualification,
in-operation calibration (ST03-ID_12 class), published-latency/verification
metrology (ST03-ID_10's contract elements), and detection statistics with
estimator honesty (D-01 + ST01-C11, BT-1/FT-02 discipline) — sold as
modules, benches, and qualification services into whoever builds the
converters (ST01-C10's market, whose live-verified bottleneck evidence is
S-B25-18). Reasoning: the startup corpus's own red-teamed records
repeatedly locate the ownable layer in the measurement chain; the buyer
community overlaps the PhD's own facility network; and the family gives
the PhD's ramp/dump and excursion-chain functions real hosts (PB-5).
Against: it rides on the same proposed-only methodology (C06 gated by C04;
C23/C31 pre-redteam) and on a market whose willingness-to-pay is unproven
by the startup corpus's own admission.

**Explicit non-wedges:** founder-led converter, breaker, relay, PSU, PPU,
or PMAD products in any family (missing §4 stack); protection actuation
hardware; space qualification; anything in D-10's controlled regime.

**Honesty bounds:** both wedges are bets on Element-1 execution (C06 after
C04 closes) exactly as B20 §8 warned; F-06's commercial evidence is weak
(old rank 23, NEW cut) and its demand is pre-order (S-B25-10); W2's
strongest supporting records (startup/03/05) are unaudited or
self-reported-complete per B00 and are used as documented engineering
analyses, not as verified market facts; no row here is a B40 portfolio
decision.

## 10. Honesty notes

- Record-vintage vs live: all venture timing/capital/market facts are
  corpus-dated except the live opens S-B25-01/02/03 (pilot, reused) and
  S-B25-15/16/17/18 (this run). The official NERC PRC-028-1 PDF returned
  HTTP 403; the compliance dates rest on a secondary page (S-B25-16)
  consistent with the record's NAES citation. The Pattern Energy page's
  content appears not updated since ~2023 (S-B25-17, disclosed).
- BT-8 primary tracing of EV07/EV08 headline WBG figures was again NOT
  performed; no conclusion above depends on those numbers (they appear
  only as direction-of-travel context). PB-6 keeps the obligation visible.
- Partial reads disclosed: ST03-ID_13 to §7's opening; startup/05
  RND_STRATEGY to line 120; startup/01 executive summary to line 160;
  DD_C11 and the startup/01 C06 deep dive not opened (rows rest on the
  audited executive summary). B20-universe rows other than F-06 rest on
  B20's accepted row-level record reads, per the task card's allowance.
- The ECCN 3A226 threshold text in ST01-C10's row is the record's own
  snippet-level caveat, carried as such — not verified against the CCL.
- Startup-corpus founder-capability assertions are recorded but not
  adopted (POWER_SKILLS.md §3); nothing here is legal, safety, export, or
  certification advice (SOURCE_POLICY).
