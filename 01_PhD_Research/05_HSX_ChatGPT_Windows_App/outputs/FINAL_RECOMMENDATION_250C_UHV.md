# Final recommendation — HSX reusable three-axis Hall head at continuous 250 deg C UHV

Date: 2026-07-12  
Project state: **`COMPLETE_WITH_OPEN_GATES`**  
Release disposition: **`HOLD - DO NOT FABRICATE/ORDER`** and **do not connect real sensors**.

This is the controlling cross-domain recommendation. Stages 10, 20 and 30 remain design evidence;
the Stage-40 findings and the corrected Stage-50 artifacts control where they disagree.

## 1. Direct answers

### Question 1 — die to LCC and one-side harness

Use the supplied short physical bond geometry only after a signed, non-mirrored microscope/GDS
traveler:

- `q1/top -> LCC inner shelf 8`;
- `q2/right -> shelf 3`;
- `q3/bottom -> shelf 19`; and
- `q4/left -> shelf 14`.

`q1..q4` are physical locations, not guessed `p1..p4`. Record `P(q1)..P(q4)` first. In the
cavity-up view the LCC chamfer is lower right. The pad-14/pad-18 issue is resolved: q4 bonds to
14; the user-drawn green bottom-view connection is the unordered tie `14<->18`. The proposed
four perimeter ties `8<->4`, `3<->9`, `19<->13`, `14<->18` do not create a low-risk one-side
breakout and are **rejected** as the production jumper network.

From the selected shelves, use the same-numbered castellations and short qualified Al
microtransitions to four protected lanes on a permanently attached fanout tongue. Terminate the
tongue to the hot pigtail by a supported resistance weld or an exact-contact crimp selected by
coupon testing. Put the demountable service boundary at a protected remote four-circuit
disconnect, not at the fragile LCC metallization. Use no solder in the baseline and transfer all
harness load to an independent ceramic comb and CP-Ti cage clip.

### Question 2 — three boards to three sensors

Keep the 12 unique Hall conductors and the accepted feedthrough/J1 allocation, but replace the
Stage-20 common-ground panel with **three galvanically separate ambient board domains**:
`GND1_X`, `GND1_Y`, and `GND1_Z`.

Each domain has its own board, RS6 output domain, isolated 100-uA current source, four-line
galvanically isolated phase-control receiver, and isolated/differential measurement channel. One
Pico phase state, one protected upstream 24-V source, and one acquisition timebase may be shared
only on the input/common side of the barriers. Do not bridge GND1 domains with BNC shells, USB,
logic returns, current-source returns, chassis, or an `AGND_STAR`.

Use V1-V4 for X, V5-V8 for Y and V9-V12 for Z; reserve V13-V19. Six pair screens terminate at the
CF flange/chassis and use no signal pin. Acquire X/Y/Z plus frame sync simultaneously after
isolation. The exact sources, isolation components and DAQ remain a purchase/design gate, and the
approximately 109-times board-amplitude anomaly must close with emulator tests before a real die
is connected.

### Question 3 — reusable low-cost ceramic head

Use corrected Concept A: three identical flat 9.60-mm zirconia seats in a single connected,
open CP-Ti base/backframe/nut-reaction cage. The ceramic thread count is **zero**. Each face uses
two externally accessible screws, a formed compliant clamp/hard stop, and a replaceable vented
nut plate in an open negative-edge cassette. A keeper prevents the nut from dropping during
service but does not carry clamp load.

The corrected kernel model fits the hard envelope at a conservative physical radius of
14.354 mm and height of 26.750 mm, includes three 3.80-by-3.80-mm cable corridors, has one
connected cage solid, six closed nut-reaction contacts, 39 re-imported solids and zero unintended
overlap. It remains NOT FOR FABRICATION because the exact feedthrough datum, zirconia process,
flexure, fasteners/keepers, cable, guard, GD&T and qualification evidence are unresolved.

## 2. Evidence language and release rules

The package uses four evidence classes:

- **VERIFIED FACT** — directly supported by an authoritative input or current primary source.
- **VERIFIED CALCULATION** — reproducible arithmetic or CAD-kernel result from stated inputs.
- **ENGINEERING PROPOSAL - VALIDATE** — a plausible design value or architecture awaiting
  measurement, supplier acceptance or qualification.
- **HOLD - DO NOT FABRICATE/ORDER** — an open item that can change geometry, materials, purchase
  configuration, safety, sensor survival or performance.

A catalog maximum, bake survival, ASTM E595 screen, short aging experiment or representative
material property is not continuous-life qualification of the complete assembly.

## 3. Final LCC bond and external connection

### 3.1 Controlled view and numbering

Controlling drawing: `drawings/50_final_lcc_and_pin_map.svg`.

Cavity-up LCC sequence:

- top left-to-right: `8, 7, 6, 5, 4`;
- right top-to-bottom: `3, 2, 1, 20, 19`;
- bottom left-to-right: `14, 15, 16, 17, 18`;
- left top-to-bottom: `9, 10, 11, 12, 13`;
- chamfer: lower right.

The physical recommendation is:

| Physical die location | Shelf | Same-numbered castellation | Protected lane | Electrical identity |
|---|---:|---:|---|---|
| q1 / top | 8 | 8 | L1 | `P(q1)` after sign-off |
| q2 / right | 3 | 3 | L2 | `P(q2)` after sign-off |
| q3 / bottom | 19 | 19 | L3 | `P(q3)` after sign-off |
| q4 / left | 14 | 14 | L4 | `P(q4)` after sign-off |

The board identity rule is always `p1->J1.1`, `p3->J1.2`, `p2->J1.6`, `p4->J1.7`. No color,
q-number, LCC pad or geometric rotation substitutes for the signed p identity.

**`G50-02 HOLD - DO NOT BOND`:** authoritative die p1-p4 physical orientation/sign is absent.
The traveler must include the GDS/runsheet or microscope evidence, cavity-up photo, lower-right
chamfer, `NO MIRROR`, P(q) table, shelf-to-castellation continuity, actual pad/finish/wire/tool
materials, and independent verification.

### 3.2 Resolution of the user's four external routes

The user proposal is normalized as:

| Inner shelf bond | User external statement | Correct interpretation | Final disposition |
|---:|---|---|---|
| q1->8 | `8->4` | passive tie `8<->4` | reject jumper; exit from castellation 8 |
| q2->3 | `3->9` | passive tie `3<->9` | reject jumper; exit from castellation 3 |
| q3->19 | `19->13` | passive tie `19<->13` | reject jumper; exit from castellation 19 |
| q4->14 | `18->14` | mirrored-bottom-view tie `14<->18` | reject jumper; exit from castellation 14 |

The 14/18 inconsistency is therefore closed as a view/notation issue. The jumper network is still
rejected because it adds long perimeter spans and joints, does not intrinsically place four robust
lands on one side, creates handling/short risks around the cavity, and has no separate mechanical
support.

### 3.3 Recommended joint stack

From die to service boundary:

1. Hall die attached to LCC by the controlled 353ND process only after same-stack life
   qualification.
2. Short Al wedge bonds from q1-q4 to shelves 8/3/19/14; optional parallel wires are electrical
   redundancy only.
3. LCC internal trace to the same-numbered castellation.
4. Short supported Al wedge/ribbon microtransition from each selected castellation to a no-Ni
   fanout-tongue lane.
5. Supported permanent robust lane terminal to the hot conductor by a resistance weld or exact
   crimp that wins the coupon DOE.
6. Permanent pigtail routed through a ceramic comb and the corrected CP-Ti strain clip.
7. Protected remote four-circuit disconnect used for independent cartridge service.

No stage may use the bond, shelf, castellation, tongue lane, weld/crimp or disconnect as strain
relief or retention.

### 3.4 Join-method comparison

| Method | Final use | Reason |
|---|---|---|
| Al wedge bond on exact die/LCC/thin-Au stack | preferred microjoint after qualification | relevant 250-deg-C feasibility exists, but exact stack/duration is unqualified |
| Al wedge/ribbon LCC-to-tongue transition | preferred protected microtransition after DOE | low mass and no solder; must prove no metallization lift/heel aging |
| resistance/parallel-gap weld | candidate robust pigtail joint | no flux; process can be logged; requires exact alloy/plating/heat-damage coupons |
| exact-contact crimp | co-equal robust pigtail candidate | serviceable process control and no flux; exact conductor/contact/tool/retention must qualify |
| spring/socket at LCC | development alternate only | reusable, but no exact continuous-250-deg-C UHV, low-magnetic, retained-force LCC02046 socket is qualified |
| 80Au20Sn solder | reject baseline | 280-deg-C liquidus gives `T/Tm=523.15/553.15=0.946` at 250 deg C; no creep/life/process margin proof |
| other solder | hold alternate | exact alloy/metallization/process/cleaning/aging required; never structural |
| user's four perimeter jumpers | reject | extra spans/joints and no protected one-side mechanical architecture |

SINTEF evidence demonstrates selected thin-Au/25-um Al wedge feasibility at 250 deg C over a
limited interval, not this complete lifetime. NASA evidence of substantial thin-film Au bond pull
loss after 72 hours at 150 deg C is a warning. The 353ND bonded stack, actual LCC finish and fanout
remain `G50-02`.

### 3.5 Cartridge service boundary

The reusable serialized unit is the bonded die + LCC + fanout tongue + guard + permanent pigtail.
The remote disconnect and pigtail arrangement must be keyed so that lane identity survives
removal. A hot LCC socket is not the baseline.

To replace one module:

1. make the system safe, discharge and document all isolation/continuity states;
2. support the selected cartridge in its handling jig;
3. disconnect only its four remote pigtail circuits and screen/strain hardware as specified;
4. remove that face's two external screws and open clamp;
5. withdraw the guarded cartridge normal to its face without removing X/Y/Z neighbors;
6. inspect the nut keeper, seat, guard, loop witness, pigtail, comb and particles;
7. install the keyed replacement against the hard stops, reinstall qualified replaceable hardware,
   remate the four-circuit remote connection and its independent strain clip;
8. repeat terminal identity, isolation, injected-signal polarity and vector calibration checks.

This process remains `G50-02/G50-05/G50-06` until a three-axis instrumented service trial passes.

## 4. Final three-board readout architecture

### 4.1 Why the earlier ambient star is rejected

The live netlist connects R2.1 and R3.2 to local `GND1`, with `/in+` through R2 and `/in-`
through R3. R2=R3=2.2 kohm. If two board GND1 nodes are joined by scope BNC shells or an ambient
star, a selected sensor terminal in one axis can reach another axis through approximately
`2.2k + 2.2k + mux Ron`. That is an intentional inter-axis electrical path. An SN74LVC125A buffer
does not supply galvanic isolation.

The final architecture therefore supersedes the common-GND1 decision. It is shown in
`drawings/50_final_isolated_readout.svg` and tabulated in `50_FINAL_AMBIENT_DOMAIN_MAP.csv`.

### 4.2 Domain architecture

For each axis i in X/Y/Z:

- shared protected 24 V input -> independent fuse/current limit/disconnect -> `RS6_i` input;
- RS6 isolated output rails and `GND1_i` power only that board-domain circuitry;
- one floating, reversible 100-uA source remains wholly in the same domain;
- common Pico a0/a1/a2/EN enters one four-line galvanic barrier for that domain;
- barrier outputs use local GND1_i, fail-safe defaults, local decoupling and selected series R;
- board J4_i enters an isolated/differential acquisition channel;
- all three isolated measurement channels share one timebase only after isolation;
- one frame-sync channel accompanies them.

Allowed shared resources:

- one versioned phase sequence and frame definition;
- input-side Pico/timing ground;
- protected upstream 24-V source and its input return;
- common DAQ timebase after the three measurement barriers;
- chassis/vessel/CF flange and screen termination structure;
- common calibration procedure.

Required independent resources:

- the 12 Hall terminals and their 19C circuits;
- the six screened pairs;
- GND1_X/GND1_Y/GND1_Z;
- three board analog chains and RS6 output rails;
- three 100-uA sources/returns and compliance/fault limits;
- three four-line isolation receiver output sides;
- three isolated/differential measurement front ends;
- per-axis gain/offset records, faults, disconnects and cartridge travelers.

Forbidden connections:

- GND1_i to another GND1;
- any GND1 to Pico/control input ground;
- direct grounded oscilloscope BNC shells on multiple J4 outputs;
- current-source return to chassis or another source;
- screen to a Hall terminal, J1 signal, cartridge or GND1;
- USB/probe/protection-earth paths that silently bridge domains.

The RS6 barrier is functional isolation, not a protective safety rating. Protective-earth and
personnel safety remain governed by the laboratory system design.

### 4.3 Complete sensor/feedthrough/J1 allocation

| Axis | Terminal | Pair | Vacuum circuit | Mirrored air cavity | Board endpoint |
|---|---|---|---:|---:|---|
| X | p1 | XA | V1 | A1 | Board X J1.1 |
| X | p3 | XA | V2 | A12 | Board X J1.2 |
| X | p2 | XB | V3 | A11 | Board X J1.6 |
| X | p4 | XB | V4 | A10 | Board X J1.7 |
| Y | p1 | YA | V5 | A9 | Board Y J1.1 |
| Y | p3 | YA | V6 | A8 | Board Y J1.2 |
| Y | p2 | YB | V7 | A7 | Board Y J1.6 |
| Y | p4 | YB | V8 | A6 | Board Y J1.7 |
| Z | p1 | ZA | V9 | A5 | Board Z J1.1 |
| Z | p3 | ZA | V10 | A4 | Board Z J1.2 |
| Z | p2 | ZB | V11 | A3 | Board Z J1.6 |
| Z | p4 | ZB | V12 | A2 | Board Z J1.7 |

V13/A14, V14/A13, V15/A18, V16/A17, V17/A16, V18/A15 and V19/A19 are individual capped
spares. No spare is paralleled for strength or used as a return without a controlled architecture
revision. The full 25-row signal/spare/shield map is `50_FINAL_INTERFACE_MAP.csv`.

The vacuum-to-air mirror is internally an involution, but first-article V1-V19 continuity is
controlling because the connector numbers are not printed and the 19C drawing contains a caution
sentence that says “9C.” Do not terminate from the drawing alone.

### 4.4 Cable and shielding

Use two screened pairs per axis: A carries p1/p3 and B carries p2/p4 under the fixed J1 convention.
Roles change during spinning; neither pair is permanently “bias” or “sense.”

Each in-vessel screen stops before the cartridge guard and terminates at the CF flange. The
air-side continuation screen terminates to the same chassis region and floats at the board end.
No screen crosses the feedthrough as a signal pin. The exact hot screen clamp/contact process is
`G50-03`.

KAP301 evidence gives OD `1.5 +/-0.15 mm`, 300-deg-C/UHV catalog ratings, about 77 pF/m
conductor-to-conductor and about 140 pF/m conductor-to-screen. Two worst-case pair cables require
3.30 mm; the final concept reserves 3.80 mm. This is 0.50 mm total width allowance, not a released
fit. Installed length, lay, bend, capacitance, abrasion, termination and proof-load testing remain
`G50-03`.

### 4.5 Phase control, acquisition and performance claim

The isolator output side must meet the board's actual a0/a1/a2/EN VIH/VIL, R5-R8, cable-C and
power-sequence conditions. TI requires a safe OE bias and fast edges can ring; select series
resistance only after far-end threshold/no-recrossing tests.

One recombined update requires eight phase states:

| Phase rate | Update rate before filtering |
|---:|---:|
| 40 kHz | 5 kS/s |
| 80 kHz | 10 kS/s |
| 100 kHz | 12.5 kS/s |
| 160 kHz | 20 kS/s |

Do not claim 20-kHz recombined bandwidth from the retained 40-100-kHz phase range. A 10-kS/s
update may be possible at 80 kHz only after final cable, isolator, mux, amplifier, filter and noise
tests. A 20-kS/s update needs at least 160-kHz phases before settling/filter margin and is a held
performance target.

The acquisition system must prove:

- three isolated/differential simultaneous channels plus sync;
- input range, noise, common-mode and fault survival;
- bounded channel-to-channel aperture skew from a common-edge test;
- at least the signed raw samples per phase;
- raw phase truth, blanking/settling, demodulated gain/phase, crosstalk and export integrity;
- no DC GND1 cross-tie with every normal cable/probe/USB path connected.

The four-channel DSOX1204G data sheet establishes channel count/sample-rate class, not galvanic
channel isolation or the required aperture-skew bound. Direct multi-BNC use is therefore not the
final baseline.

### 4.6 Pre-power sequence

Before a real cartridge:

1. close the physical q/p traveler and V1-V19 mirror traveler;
2. prove all 12 unique paths and all-pairs/chassis isolation with boards disconnected;
3. inspect J1 physical pin numbers and shell behavior;
4. select and limit all three current sources; test compliance, reversal, noise and fault energy;
5. verify GND1_X/Y/Z isolation with every power/control/acquisition cable installed;
6. power each board domain individually with EN in its safe state;
7. verify isolation-barrier defaults, local logic levels, ringing, skew and settling;
8. inject known delta-V into X/Y/Z and close the approximately 109-times anomaly;
9. run the full eight-phase sequence on emulator loads and acquire X/Y/Z+sync simultaneously;
10. connect one qualified real cartridge at a time only after the release board signs the evidence.

All of this remains `G50-06 HOLD - DO NOT CONNECT REAL SENSORS`.

## 5. Final reusable package

### 5.1 Selected architecture

Corrected Concept A consists of:

- one open connected CP-Ti base/backframe/reaction cage;
- four open through-attached feedthrough posts at x/y=+/-9.00 mm;
- three identical finished flat zirconia seat plates, one per +X/+Y/+Z face;
- three protected bonded cartridges with guarded fanout and permanent pigtails;
- three open formed CP-Ti clamps with hard stops;
- six external negative-edge face screws;
- six open-sided replaceable vented nut plates and six external retainers/keepers;
- three independent CP-Ti/ceramic-comb harness strain-relief locations;
- three corrected 3.80-by-3.80-mm cable corridors.

The primary load path for each face is:

`external screw head -> formed clamp -> qualified hard-stop/contact pads -> zirconia seat/backframe -> connected CP-Ti cage -> support posts/feedthrough datum`.

The nut keeper is only positive retention during service. The die, bonds, LCC metallization,
fanout, robust terminal, pigtail conductor and remote disconnect carry no retention load.

### 5.2 Recalculated geometry

Controlling files: `cad/50A_FINAL_NFF.step`, `cad/50A_HARNESS_KEEPOUTS_NFF.step`,
`cad/50_CAD_KERNEL_REPORT.txt`, `50_FINAL_DIMENSION_AND_RELEASE_LEDGER.csv`.

| Quantity | Result | Evidence class |
|---|---:|---|
| hard envelope | diameter 31.750 mm; height 27.500 mm | verified requirement |
| physical conservative radius | 14.354 mm | verified calculation |
| physical radial margin | 1.521 mm | verified calculation |
| physical height | 26.750 mm | verified calculation |
| physical height margin | 0.750 mm | verified calculation |
| proposed worst height | 27.160 mm; 0.340-mm margin | engineering proposal — validate |
| proposed worst radius | 14.566 mm; 1.309-mm margin | engineering proposal — validate |
| corrected corridor | 3.80 mm square; two-pair stack 3.30 mm | calculation + proposal |
| connected cage solid count | 1 | verified kernel calculation |
| nut reaction contact | 6/6 at 0.000000-mm distance | verified kernel calculation |
| unintended physical overlap | 0.000000 mm3 | verified kernel calculation |
| STEP reimport | 39 valid solids; bound delta 0.000000 mm | verified kernel calculation |
| feedthrough provisional keepout | 0.528-mm radial and 1.090-mm axial clearance | conditional proposal |

The CAD intentionally remains NFF. It corrects the Stage-30 free-nut-pad/load-path and cable-fit
contradictions, but it is not a production tolerance or stress model.

### 5.3 Required package disclosures

| Required disclosure | Final statement |
|---|---|
| tapped/internal ceramic threads | **0** |
| bonded inserts in ceramic | **0** |
| unique ceramic geometry count | **1** repeated seat geometry |
| identical seat quantity | **3** |
| proposed seat size | 9.60 x 9.60 x 1.00 mm; vendor approval required |
| post-fire operations | proposed flat grinding/lapping and through-window/exit-notch finishing; edge/radius process vendor-controlled; no tapping |
| external tool directions | straight +X, +Y and +Z; negative-edge heads/nut keepers |
| one-axis replacement | remove only that face's two screws/clamp and its remote pigtail connection; withdraw guarded cartridge normal to face |
| connection remate | keyed remote four-circuit pigtail disconnect plus independent strain clip; then complete identity/isolation/polarity tests |
| reusable high-value unit | serialized bonded die/LCC/fanout/guard/permanent-pigtail cartridge |
| reusable structure | seat/cage/clamp only after dimensional/force/cleanliness inspection |
| sacrificial/replaceable parts | face screws, nut plates, keepers/retainers, strain-relief hardware, damaged contact terminals, qualification witnesses |
| cost basis | comparable drawing-specific 1/3/10-head RFQs with NRE/Q + accepted parts + labor + inspection + yield/scrap + qualification shown separately |

Every post-fire operation, tolerance, edge condition and cleaning step remains `G50-04 HOLD - DO
NOT FABRICATE CERAMIC` until the zirconia vendor signs the DFM/process plan.

### 5.4 Preload, contact, venting and fasteners

The first-order CTE displacement increment over a 2.40-mm shoulder from 20 to 250 deg C is only
`(10.4-9.5)e-6/K * 2.40 mm * 230 K = 0.00050 mm`. This does not qualify force. The prior
0.10-0.26-mm displacement and 1-2-N/mm stiffness were proposals without a formed-flexure
geometry. The final CAD therefore does not claim a qualified preload.

`G50-05` must close:

- exact CP-Ti grade, form, heat treatment, finish, cleanliness and delivered magnetics;
- formed flexure geometry, hard stops, contact pads and FEA/contact stress;
- 20/250-deg-C force-displacement, dwell, cycles and positive capture;
- vented screw/nut geometry, open keeper retention, hot galling, particles and reuse rule;
- lower post/feedthrough attachment;
- pump-down/borescope proof of no trapped faying/nut volumes;
- proof load with zero force at electrical joints.

### 5.5 Bond protection and service

The guard height rule remains measured maximum loop/heel envelope plus at least a proposed
0.30 mm. No loop survey exists. Before integrated service, measure all loops and run thermal sweep,
handling-jig, adjacent-tool and witness-wire tests.

Service must demonstrate X, then Y, then Z removal/remating with the other two installed. Record
tool access, particles/chips, contact resistance, insulation, p identity, raw phase polarity,
calibration shift and any accidental load. A procedure is not accepted merely because the CAD
shows straight axes.

### 5.6 Alternatives and reversal triggers

| Concept | Retained role | Strength | Why not baseline now | Reversal trigger |
|---|---|---|---|---|
| corrected A: three identical flat seats | preferred procurement direction | one ceramic geometry; localized scrap; simple external service | still needs cage/flexure/cable/vendor release | survives all hard gates and wins comparable total-cost RFQs |
| B: monolithic open zirconia core | quoted alternate | potentially better as-fired orthogonality and fewer ceramic interfaces | high single-part ceramic NRE/scrap; prior reaction cage incomplete; height margin small | vendor proves process/orthogonality/yield and accepted total cost beats A |
| C: split protected cassette | service alternate | best handling containment and reusable cassette concept | 0.10-mm axial stack unresolved; rail/pin/contact complexity | qualified frequent-service value exceeds added parts/contact/cycle cost |

Do not reuse Stage-30 A=96/B=81/C=77 as a release decision. The weight order is valid, but scores
were provisional and predated the hard-gate failures. Re-score only hard-gate survivors with live
1/3/10 RFQs.

## 6. Cost strategy

The controlling basis is `50_FINAL_COST_BASIS_1_3_10.csv`; it intentionally contains no invented
prices. For each concept and quantity Q in 1, 3 and 10 heads, compare:

`accepted cost/head = NRE/Q + accepted recurring parts + assembly labor + inspection + expected yield/scrap + service spares`.

Report qualification/chamber/coupon cost separately so it is not hidden in one concept's part
price. Obtain the same drawing/process assumptions from at least two ceramic vendors where
possible. Quote identical seats as 3/9/30 production pieces plus explicit qualification/spares;
quote cages 1/3/10; clamps and cartridges 3/9/30; fastener/service kits by six per head; and the
complete feedthrough/cable/ambient-isolation system at 1/3/10.

Cost remains the first weighted priority only after safety, physics, envelope, isolation,
continuous-life, service and fabrication gates pass. The reusable bonded LCC module is never
counted as a disposable fastener/contact item.

## 7. Controlled build and qualification order

The detailed 19-step gate sequence is `50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv`. Condensed order:

1. freeze the complete service/error envelope (`G50-01`);
2. close LCC/die orientation and incoming continuity;
3. qualify 353ND same-stack die attach;
4. qualify die-to-LCC Al bonds;
5. qualify fanout microtransition and robust pigtail terminal;
6. obtain exact 19C/UW interface and first-article continuity/magnetic/thermal evidence;
7. select and qualify the two-pair cable branch in the 3.80-mm corridor;
8. obtain zirconia DFM, first article and 1/3/10 RFQs;
9. qualify CP-Ti cage/flexure/nut/keeper/fastener/strain hardware;
10. regenerate production-intent CAD and GD&T with all actual inputs;
11. qualify three isolated current-source domains;
12. close the X/Y/Z gain and approximately 109-times anomaly;
13. qualify isolated control fanout and maximum phase rate;
14. qualify isolated simultaneous acquisition and all-cables isolation;
15. qualify complete protected cartridges;
16. integrate three emulator cartridges and pass vacuum/mechanical/electrical fault tests;
17. demonstrate independent X/Y/Z service;
18. perform 20/250-deg-C three-axis vector calibration and repeat after bake/service;
19. run the final configuration/release review.

Do not consume a real die before its prerequisite coupon stages pass. Do not order a geometry-
changing item before its interface and DFM gates close.

## 8. Consolidated decision gates

The final release gates are:

- `G50-01`: signed service/error envelope;
- `G50-02`: orientation, bonded stack, fanout, pigtail and cartridge release;
- `G50-03`: exact 19C/UW interface and cable/harness release;
- `G50-04`: zirconia DFM/RFQ and complete production CAD;
- `G50-05`: CP-Ti cage/flexure/fastener/nut/keeper/vent/service hardware;
- `G50-06`: isolated three-domain electronics, current sources, anomaly and simultaneous DAQ;
- `G50-07`: numerical magnetic budget, delivered hardware screen and hot vector calibration;
- `G50-08`: objective final qualification/configuration review.

Earlier G00-G40 items remain historical traceability and are not deleted. G50 consolidates their
remaining release effects. Closure requires evidence linked in `FINAL_ACCEPTANCE_CHECKLIST.md`,
not a confidence score or verbal waiver.

## 9. Final artifact hierarchy

Use in this order:

1. this report for the controlling recommendation;
2. `FINAL_ACCEPTANCE_CHECKLIST.md` for release state;
3. `50_FINAL_INTERFACE_MAP.csv` and `50_FINAL_AMBIENT_DOMAIN_MAP.csv` for interfaces;
4. `drawings/50_final_lcc_and_pin_map.svg`, `50_final_isolated_readout.svg`, and
   `50_final_corrected_package.svg` for the corrected views;
5. `50_FINAL_DIMENSION_AND_RELEASE_LEDGER.csv`, `50_FINAL_FASTENER_AND_THREAD_SCHEDULE.csv` and
   `cad/50_CAD_KERNEL_REPORT.txt` for package calculations;
6. `50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv` and `50_FINAL_COST_BASIS_1_3_10.csv` for execution;
7. `FINAL_PATCH_AND_PROVENANCE.md` for supersessions and source reuse;
8. `FINAL_FILE_INDEX.md` for the complete artifact set;
9. Stages 00-40 as supporting evidence and audit history.

## 10. Final status

All three mission questions are answered with a self-consistent corrected architecture. The final
map, isolation topology, package load path, cable corridor, dimensions, service boundary, cost
basis and qualification order are explicit and cross-linked.

The package is nevertheless **`COMPLETE_WITH_OPEN_GATES`**, not fabrication-ready. Objective
orientation, complete-stack life, exact feedthrough/cable, ceramic DFM, retention, isolated
electronics/DAQ, magnetic budget and integrated qualification evidence do not exist. Therefore:

**`HOLD - DO NOT FABRICATE/ORDER`**  
**`HOLD - DO NOT BOND`**  
**`HOLD - DO NOT CONNECT REAL SENSORS`**
