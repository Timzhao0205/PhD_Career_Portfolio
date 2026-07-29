# Stage 40 — independent cross-domain red-team review

Date: 2026-07-12  
Review scope: accepted Stages 10, 20 and 30 against governing inputs, source ledger, live netlist,
LCC drawing/user image, 19C drawings, CAD exports, tables/drawings and continuous-250 °C UHV
requirements. Earlier stage outputs were **not edited** during this review.

## 1. Board verdict

The engineering direction is viable, but the package is **not fabrication-ready and not safe to
power with real sensors**. The audit found:

- **8 BLOCKER findings**;
- **14 MAJOR findings**;
- **3 MINOR findings**; and
- **8 NOTE/PASS findings**.

Two blockers are internal contradictions rather than merely missing vendor evidence:

1. the Stage-20 common-ground baseline does not preserve electrical isolation of the three sensor
   circuits because the live board netlist references the selected sense pair to GND1 through
   R2/R3; and
2. the Stage-30 A/B CAD does not provide a connected/captured Ti reaction structure for its face
   nut pads, so its clamp load path is incomplete even though collision checks pass.

A third quantitative blocker is the harness corridor: two KAP301 pairs per sensor require up to
`2 × 1.65 = 3.30 mm`, larger than the 3.00-mm reserved corridor before installation clearance.

The final synthesis must correct the electrical architecture and must not describe Concept A as a
fabrication baseline until a connected vented saddle cage and a real cable stack are re-modeled.
The acceptable mission state is therefore `COMPLETE_WITH_OPEN_GATES`, not an unconditional
release.

**Package disposition: `HOLD - DO NOT FABRICATE/ORDER`.**

## 2. Severity definitions

- **BLOCKER** — violates a hard requirement, makes a released drawing unsafe/ambiguous, or permits
  irreversible fabrication/energization with an unresolved failure path.
- **MAJOR** — does not immediately defeat the concept but materially affects reliability,
  performance, service, cost or qualification.
- **MINOR** — documentation/source precision defect that must be repaired before release.
- **NOTE/PASS** — independently recalculated and accepted, or correctly held by an existing gate.

## 3. Findings register

| Finding | Severity | Affected artifact | Evidence / independent calculation | Required correction | Closure test |
|---|---|---|---|---|---|
| F40-B01 | **BLOCKER** | `20_THREE_BOARD_READOUT_ARCHITECTURE.md`, ground drawing, final board baseline | Live netlist net `GND1` connects R2.1 and R3.2; `/in+` connects R2.2 to U2 and `/in-` connects R3.1 to U2. With three GND1s commoned by scope/AGND_STAR, an active X terminal can reach an active Y terminal through about `2.2k + 2.2k + mux Ron`, so the in-vessel sensors are not galvanically isolated. SN74LVC125A buffering is not isolation. | Replace common-ground baseline with one galvanically isolated four-line control domain per board and isolated/differential acquisition per board. Do not connect grounded BNC shells across GND1 domains in simultaneous operation. Preserve unique 12 sensor nets and independent bias sources. | With all final control/acquisition/power connected, prove no intentional DC continuity between board GND1 domains or sensor networks; pass signed leakage/capacitance/common-mode/fault and simultaneous-capture tests. |
| F40-B02 | **BLOCKER** | Stage-10 pad/bond map and all downstream p labels | 14/18 notation is resolved, but authoritative die p1-p4 physical orientation/sign, GDS datum and no-mirror microscope traveler are absent. Physical q→8/3/19/14 remains conditional. | Keep p identity parametric; acquire signed GDS/microscope orientation and sacrificial LCC chamfer/same-number continuity. Verify reach/tool/heel/loop on actual gen-2 die. | Two-person signed traveler with cavity-up/chamfer photo, P(q1…q4), no-mirror declaration, four continuity paths and bond-program clearance review. |
| F40-B03 | **BLOCKER** | Bonded die/LCC cartridge | SINTEF proves feasibility for 25-µm Al wedge bonds on selected thin-Au systems at 250 °C, not this die/LCC/353ND/UHV stack. NASA observed 30–40% pull loss on thin-film Au after 72 h at 150 °C. 353ND is operated far above listed Tg and lacks continuous-250 °C UHV life evidence. | Freeze actual die pad, LCC lot, Al wire/tool/program, 353ND lot/mix/cure/bondline and qualify same-stack coupons. | Continuous 250 °C vacuum aging with controls, resistance, pull/shear distributions, fracture mode, cross-section, contamination/outgassing and post-aging functional drift to a signed duration/cycle plan. |
| F40-B04 | **BLOCKER** | 19C-275 procurement, mirror map, package datum | Official live product: 19 male/male Ni-Fe Au-plated pins, maximum operating/bake 250 °C and UHV rating. Maximum equals duty with no margin; Ni-Fe magnetic effect is unknown. Connector drawing warns of a male/male mirror but its caution text says “9C”; numbers are not printed. Exact mated protrusion/support geometry is absent. | Obtain Accu-Glass written confirmation for continuous duty, exact mated vacuum geometry/contact/wire range/materials; UW port datum; magnetic screening/budget. Treat mirror table as a traveler hypothesis only. | Vendor/UW signed interface control document; full V1–V19 continuity permutation; installed CMM envelope; hot-vacuum retention; remanence/permeability or field-map acceptance at each die. |
| F40-B05 | **BLOCKER** | Stage-30 Concepts A/B CAD, fastener schedule, service claims | `30_package_concepts.py` creates individual `nutpad` solids at lines 150–160. A adds only three rear rails; B adds no external saddle cage at all. The nut pads are not joined/captured to a base/cage reaction member. Pairwise zero overlap checks collision, not structural connectivity. A's fixed seats therefore also lack a complete retained load path. | Add a continuous CP-Ti saddle/corner cage from base to every face nut reaction location; positively capture replaceable vented nut plates while preserving straight tool access and independent service. Model heads/nuts/capture/clearance. | CAD contact/connectivity graph proves a continuous non-electrical load path from each screw head through clamp/hard stop to base; no free solids; STEP re-import, envelope, tolerance, collision, tool and one-cartridge service tests pass. |
| F40-B06 | **BLOCKER** | Stage-20 cable candidate and Stage-30 3×3-mm branch corridors | Allectra PDF gives KAP301 OD `1.5 ±0.15 mm`; live product fields also show up to 1.65 mm. Two screened pairs per four-terminal sensor require 3.00 mm nominal and 3.30 mm worst case side-by-side, exceeding a 3.00-mm corridor before clearance, bend or clip compression. | Select exact cable/lay or enlarge/re-route each corridor and strain relief. Re-run installed envelope and neighboring-part collision with tolerance and bend sweep. | First-article two-pair branch passes a physical go/no-go corridor, minimum bend, proof-load, abrasion and hot-vacuum test; CAD uses worst delivered OD plus signed installation clearance. |
| F40-B07 | **BLOCKER** | Stage-20 power-up/readout readiness | Three exact floating 100-µA sources are not selected or fault-qualified; the as-built 109× amplitude anomaly remains unresolved. Either defect can damage or invalidate real-sensor measurements. | Select/prove independent current sources, compliance/limit/noise, and resolve gain/bridge anomaly by injected ΔV on X/Y/Z before connecting dies. | Full pre-power sequence passes with emulator loads; measured current independence, compliance, fault energy, J4 gain/polarity/linearity and cross-board isolation are signed. |
| F40-B08 | **BLOCKER** | Stage-30 retention/material release | CP-Ti Grade 4 is a credible material, but the CAD clamp is a flat frame, not a dimensioned formed flexure; proposed `k=1–2 N/mm` and 0.10–0.52 N have no geometry/FEA/coupon. Ti/Ti galling, particles, retained force and positive pin retention at 250 °C UHV are unqualified. | Design exact flexure, hard stops, contact pads, fastener/pin/nut finish and positive capture; avoid torque-defined ceramic load. | 20/250 °C force-displacement and dwell/cycle coupons, FEA/contact check, galling/particle/reuse test, proof load and retained positive-capture inspection pass. |
| F40-M01 | **MAJOR** | Stage-20 performance claim | Eight phases give update `f_phase/8`: 40→5 kHz, 80→10 kHz, 100→12.5 kHz, 160→20 kHz. The retained usable range ends at 100 kHz, so 20-kHz recombined updates are not supported; 10 kHz may be possible at 80 kHz only after settling/noise tests. | Freeze whether the requirement is ≥10 kHz or the full 20 kHz; measure at candidate rates and design anti-alias/demod filters from the accepted rate. | Three-board raw+sync capture demonstrates settling, phase truth, noise, crosstalk and calibrated recombined response to the signed bandwidth. |
| F40-M02 | **MAJOR** | Stage-20 buffer junction | TI requires OE pull-up to VCC for a high-impedance power-up/down state and warns about fast-edge ringing. Exact OE topology, VCC, decoupling, R5–R8, cable C, power sequencing and 22–68 Ω choice are absent. Corrected isolation baseline also makes plain LVC buffers insufficient across domains. | Draw the actual per-domain isolated-control schematic with fail-safe defaults, output series R, local power/decoupling and fault behavior. | Power-order and cable-corner tests pass VIH/VIL, no threshold recrossing/ringing, acceptable skew and analog settling at maximum rate. |
| F40-M03 | **MAJOR** | Stage-20 acquisition | Keysight verifies four analog channels, bandwidth, sample rate and memory, but accessible evidence does not specify galvanic channel isolation or channel-to-channel aperture skew. Grounded BNC shells defeat isolated GND1 domains. | Use isolated/differential simultaneous acquisition or isolated probes with an explicit common timebase and sync channel; document input range/noise/skew. | Inject one edge into all channels and prove channel skew; measure isolation/common-mode; capture three board outputs + sync with no GND1 continuity. |
| F40-M04 | **MAJOR** | Stage-30 virtual-leak control | Through-holes are open, but flat clamp/cartridge/seat interfaces and rear nut pads can form large faying-surface pockets. “Edge vent” is text, not dimensioned CAD. Lower post attachment is unresolved. | Add explicit open edges/vent grooves or stand-offs to every faying interface and nut capture; dimension conductance paths and cleaning access. | Visual borescope/CAD inspection finds no closed volume; helium leak/pump-down comparison and residue/particle inspection pass after assembly. |
| F40-M05 | **MAJOR** | Stage-30 zirconia release | Walls/radii/tolerances are proposals. No zirconia vendor has accepted the 1.00-mm A seat, 1.50-mm minimum ring, core orthogonality, grinding/flatness, cleaning or yield. | Issue drawing-specific A/B/C DFM/RFQ package and receive redlines, process plan and 1/3/10-set quotes. | Vendor-signed DFM and first-article CMM/optical report; fired coupons/parts meet dimensions, chips, flatness, orthogonality and cleanliness. |
| F40-M06 | **MAJOR** | Stage-30 guard/service | Guard clearance is “measured loop +0.30” but no bonded-loop survey, handling jig, chamber-tool model or 25-cycle service data exists. | Measure loop/heel sweep, finalize guard/key/jig, model actual chamber tool envelope and run independent cartridge changes. | Each axis removed/remated with other two installed; zero loop contact/chip/particle; continuity/contact/noise/calibration remain within signed limits. |
| F40-M07 | **MAJOR** | Concept C | Nominal LCC axial clearance is 0.10 mm with missing LCC thickness/warpage/front-guard tolerance; rear tongue/contact and positive pin retainer are not released. | Keep C alternate only; close full axial and rear-contact stack and rail/pin capture. | Worst-case positive clearance at 20/250 °C; 25-cycle hot/cold insertion, contact resistance, retention and guard-clearance tests. |
| F40-M08 | **MAJOR** | Stage-30 score/cost recommendation | A=96 assumes best cost without vendor prices. All concepts still fail unresolved hard material/interface/service gates, so “after hard-gate filtering” is provisional. A may incur more Ti parts/assembly than B. | Label ranking provisional; use vendor NRE/per-piece/yield/inspection and assembly labor in a signed total-cost comparison before selection. | Comparable 1/3/10-set RFQs and assembly-time/scrap model; rerun 30/25/25/10/10 score only for hard-gate survivors. |
| F40-M09 | **MAJOR** | Magnetic compatibility | Near-sensor Ti is documented nonmagnetic only as bulk representative data; delivered fasteners, nut pads, welds, plating, silver-plated cable screen and especially Ni-Fe feedthrough are not screened to a numeric perturbation budget. | Freeze allowed field/remanence and inspect/screen every delivered alloy/finish/assembly in installed geometry. | Three-axis field-map/background measurement before/after hardware installation and bake; material certificates and handheld/fixture screening pass. |
| F40-M10 | **MAJOR** | Harness electrical behavior | KAP301 is 77 pF/m conductor-conductor and about 140 pF/m conductor-screen; actual length is not frozen. At high phase rate this capacitance, mux/source resistance and screens can alter settling/crosstalk. | Freeze length/lay/screen termination and include R/L/C in phase-settling model/test. | Worst-length emulator and final harness pass raw-phase settling, recombined gain/phase/noise and injected screen-current tests. |
| F40-M11 | **MAJOR** | Calibration/orthogonality | No concept has measured hot orthogonality, axis repeatability after service, or final 3×3 calibration stability. A has bolted flat seats; C has rail/pin datums; B has unquoted fired distortion. | Treat mechanical axes as initial datums only; require full vector matrix after bake and every service. | Known-field multi-orientation calibration at 20/250 °C; repeat after thermal/service cycles and meet signed drift/orthogonality limits. |
| F40-M12 | **MAJOR** | LCC material/fit calculation | Stage 30 uses representative alumina CTE; Spectrum drawing/body evidence does not establish the purchased LCC ceramic grade, warpage or lot dimensions. | Measure purchased carriers and obtain vendor material/lot documentation before freezing pocket/thermal clearance. | Incoming lot inspection and 20/250 °C fit coupon close the pocket stack with no bind/chip. |
| F40-M13 | **MAJOR** | Production drawings/GD&T | Concept STEP contains sharp corners, simplified solids, keep-out solids and no production datums/GD&T. Support-post lower attachment and several exact fasteners/contacts are absent. | Produce a separate released assembly/drawing set only after red-team corrections and vendor inputs; retain NOT-FOR-FABRICATION files as evidence. | Cross-artifact audit proves dimensions/pads/chamfer/axes/pins/units/materials identical; CAD includes every installed part and tolerance. |
| F40-M14 | **MAJOR** | Contact/fanout qualification | Stage-10 fanout tongue, microtransition and robust terminal are schematic. No exact nickel-free metallization, weld/crimp/contact alloy/temper/force or qualified process exists. | Freeze exact fanout and permanent pigtail process with independent strain relief; no hot LCC socket assumption. | Same-material DOE passes resistance, pull, cross-section, thermal-vacuum age, handling and magnetic/cleanliness acceptance. |
| F40-N01 | MINOR | 19C connector evidence wording | 110240 is a 19C drawing but its wiring caution explicitly says “9C feedthrough.” Stage 20 appropriately requires continuity, but it should not say the exact permutation is definitively proven by that caution alone. | Final text must distinguish the drawn 19-hole rear pattern from the misnamed caution sentence. | Vendor clarification or first-article V1–V19 traveler. |
| F40-N02 | MINOR | 353ND source durability | The historic direct 353ND URL now redirects to a MED-353ND product page in live browsing; source ledger claims came from the earlier TDS. | Archive the controlling TDS revision/lot document in the qualification traveler; do not rely on a mutable redirect. | Controlled PDF checksum/revision stored with cure traveler. |
| F40-N03 | MINOR | STEP/STL validation wording | STL re-import proves nonempty faces/span but not watertight positive solid volume; the report should not be read as manufacturing mesh validation. | Use STEP as controlling geometry and run mesh watertight/manifold checks only if STL becomes a manufacturing deliverable. | Mesh validator reports closed manifold and unit/orientation consistency. |
| F40-P01 | NOTE/PASS | 14/18 discrepancy | Cavity-up q4 bond is pad 14; green line was on mirrored bottom view where written 18→14 corresponds to unordered `14↔18`. Rejected external jumper network is clearly separated. | No correction. Keep view labels. | Signed LCC traveler. |
| F40-P02 | NOTE/PASS | LCC map/drawing consistency | Current cavity-up rows and lower-right chamfer agree across Stage-10 SVG/table: top 8–4, right 3/2/1/20/19, bottom 14–18, left 9–13. p identity remains gated. | No correction. | Physical sacrificial continuity closes. |
| F40-P03 | NOTE/PASS | Pin count and end-to-end map | CSV independently parses as 12 signals, 7 spares and 6 flange screens. Vacuum and air cavity sets each cover 19 unique positions; mirror permutation is an involution. J1 endpoints match p1/p3/p2/p4=1/2/6/7. | No architecture correction; retain full continuity gate. | First-article traveler. |
| F40-P04 | NOTE/PASS | No shared feedthrough return/shield pin | Twelve sensor terminals use unique pins; screens bond at flange and use no V pin; no sensor return is intentionally shared at feedthrough. | Preserve in corrected isolated ambient architecture. | Isolation/continuity test. |
| F40-P05 | NOTE/PASS | Solder/PEEK/BeCu disposition | No solder is the head baseline; AuSn at 250 °C is correctly rejected without qualification; PEEK and BeCu preload/socket assumptions are rejected. | Preserve. | BOM/material audit finds none in baseline retention/join. |
| F40-P06 | NOTE/PASS | Ceramic threads/hidden bolts | Fastener schedule sums to zero ceramic threads; internal zirconia threads, bonded inserts and cross-bolts are rejected. The separate floating-nut/load-path defect is F40-B05. | Preserve zero-thread rule while redesigning cage. | Production CAD/BOM review. |
| F40-P07 | NOTE/PASS | Envelope arithmetic for modeled solids | OpenCascade and STEP re-import agree: radius 14.354 mm; nominal heights A/B/C 26.70/27.00/26.55 mm; critical modeled overlap zero. This does not include unresolved mated/lower-support or cable stack. | Preserve calculation; re-run after corrections. | Corrected complete assembly passes tolerance envelope. |
| F40-P08 | NOTE/PASS | Electrical-joint load rule | Stage 10/30 explicitly separates mechanical clamp/strain relief from bonds, castellations, fanout, weld/crimp and pigtail. | Preserve in corrected cage/contact design. | Physical proof-load shows zero force at electrical joints. |

## 4. Independent recalculations and source verification

### 4.1 LCC views and 14/18

The current Stage-10 cavity-up drawing is internally consistent:

- top left-to-right `8,7,6,5,4`;
- right top-to-bottom `3,2,1,20,19`;
- bottom left-to-right `14,15,16,17,18`;
- left top-to-bottom `9,10,11,12,13`;
- lower-right chamfer.

The red q4 bond is to 14. The green route belongs to the mirrored bottom view, where 18 is on the
left and 14 on the right. Passive ties are unordered, so `14↔18` is correct. This closes only the
notation defect; it does not identify die p1-p4.

### 4.2 Feedthrough permutation and count

The CSV has 25 rows: 12 signals, seven spares and six shield records. The 19 signal/spare records
use every V1–V19 and every A1–A19 exactly once. The stated mirror is an involution:

`1`, `2↔12`, `3↔11`, `4↔10`, `5↔9`, `6↔8`, `7`, `13↔14`, `15↔18`, `16↔17`, `19`.

This is internally complete and leaves `19-12=7` spares. It is not an authorization to terminate
because 110240 says numbers are absent and the caution sentence misnames 9C.

### 4.3 Ambient isolation contradiction

The live netlist—not an inference—shows:

- net `GND1` connects R2.1, R3.2, both J4 return pins and the logic pulldowns;
- `/in+` connects R2.2 to U2;
- `/in-` connects R3.1 to U2;
- R2=R3=2.2 kΩ from the authoritative hardware data.

When U2 selects a sensor pair, each selected input has a 2.2-kΩ path to its board GND1. Commoning
three GND1s through grounded BNC shells/AGND_STAR produces an inter-axis DC path of approximately
4.4 kΩ plus mux resistance. The current sources may still be individually isolated devices, but
the sensor circuits are not electrically isolated. A buffer changes drive impedance, not galvanic
isolation. Therefore the conditional isolation upgrade in Stage 20 must become the final baseline.

### 4.4 Phase/update rate

`T_update=8/f_phase`; therefore:

| Phase rate | Recombined update before filtering |
|---:|---:|
| 40 kHz | 5 kHz |
| 80 kHz | 10 kHz |
| 100 kHz | 12.5 kHz |
| 160 kHz | 20 kHz |

The arithmetic is correct. A 10-kHz target may be reachable within the retained 100-kHz phase
range; 20 kHz requires operation beyond it and needs new settling/noise evidence.

### 4.5 Cable geometry/electrical load

Allectra's 2024 PDF states `1.5 ±0.15 mm` cable OD, 77 pF/m conductor-conductor and about 140 pF/m
conductor-screen. Two pairs per sensor give 3.00 mm nominal and 3.30 mm worst-case simple width;
the Stage-30 corridor is 3.00 mm. The live product page inconsistently shows 1.55 mm in descriptive
text and 1.65 mm in a structured OD field, so the larger delivered bound is the only safe input.

At 20 °C the PDF gives 548 Ω/km per conductor. A one-metre two-conductor bias loop is about
1.096 Ω; using a copper-like 0.00393/K coefficient only as sensitivity gives roughly 2.09 Ω at
250 °C and 0.209 mV drop at 100 µA. Resistance is unlikely to consume compliance, but cable
capacitance and thermoelectric/mismatch effects still require final-length tests.

### 4.6 Package bounds and omitted stack

The kernel values for modeled solids are reproduced and STEP re-import matches. Proposed height
worst cases also arithmetically pass. However, hard envelope closure is conditional because the
exact mated 19C top/datum, lower post attachment, real cable bundle/clip deformation and corrected
saddle cage are not in the released model. B's claimed 0.140-mm proposed height margin is
especially too small to absorb an unmodeled interface.

### 4.7 Preload/contact stress

The thermal displacement increment is correctly tiny:

`(10.4-9.5)e-6/K × 2.40 mm × 230 K = 0.00050 mm`.

But `F=kδ` is only arithmetic because `k` is proposed and the flat-frame CAD has no flexure beam.
The 0.13-MPa average stress also assumes four 1-mm² pads that are not dimensioned. These values
must not appear as qualified margins.

## 5. Named hazard audit

| Required search item | Red-team result |
|---|---|
| 14/18 mismatch | resolved correctly; F40-P01 |
| mirror/chamfer/die orientation | feedthrough and die orientation remain blockers; F40-B02/B04 |
| crossed/overlong bonds | no drawn crossing; actual reach/loop/tool absent; F40-B02/M06 |
| load through electrical joints | proposal correctly avoids; F40-P08; physical proof still required |
| solder margin/flux | no-solder baseline; AuSn correctly held; F40-P05 |
| intermetallic aging | exact Al/Au/353ND stack unqualified; F40-B03 |
| PEEK creep | rejected as baseline; exact 19C connector remains F40-B04 |
| BeCu relaxation | rejected as 250 °C baseline; F40-P05 |
| nickel/steel magnetic effects | Ni-Fe feedthrough and delivered hardware remain F40-B04/M09 |
| virtual leaks/trapped volumes | faying/nut/post vents not dimensioned; F40-M04 |
| blind/crossing bolts | crossing axes corrected; no ceramic blind threads; floating nut/load path F40-B05 |
| inaccessible nuts | A/B nut capture/access is not physically established; F40-B05 |
| ceramic chipping | vendor/first-article/service holds; F40-M05/M06 |
| rotated LCC | key/microscope traveler absent; F40-B02 |
| bond-wire sweep | measured envelope absent; F40-M06 |
| pin shortage | pass: 19-12=7 spares; F40-P03 |
| shared returns | no feedthrough return; ambient common creates resistive sensor coupling; F40-B01/P04 |
| unsynchronized DAQ | common sync proposed; exact isolated simultaneous capture/skew open; F40-M03 |
| unsupported tolerance/price | clearly labeled but ranking remains provisional; F40-M05/M08/M13 |
| drawing/table disagreement | pad/pin tables agree; package CAD lacks claimed A/B saddle reaction; F40-B05 |

## 6. Required final-baseline corrections

Stage 50 must carry the following hierarchy:

1. **Ambient electrical baseline:** one isolated digital-control output domain per board, three
   truly independent floating current sources, and isolated/differential simultaneous acquisition.
   No common grounded-scope BNC connection across board GND1 domains during three-axis operation.
2. **In-vessel electrical baseline:** twelve unique Hall conductors and six screens remain; p
   identity is signed at each cartridge; 19C mirror is continuity-proven.
3. **Mechanical baseline:** Concept A remains a preferred procurement direction only after adding
   a continuous CP-Ti saddle/corner cage with captured vented replaceable nut plates and after
   re-sizing the cable corridors. Current Stage-30 CAD remains NOT FOR FABRICATION.
4. **Qualification:** bonded stack, connector/feedthrough magnetic/mechanical/life, flexure/
   fastener/ceramic, cable and one-cartridge service remain explicit release gates.
5. **Performance:** claim only the phase/update/bandwidth actually measured with final harness,
   isolated control/acquisition and all three boards.

## 7. Requirements-trace summary

`outputs/40_REQUIREMENTS_TRACE.csv` maps every governing requirement and named audit item. Summary
status after this review:

- PASS: view reconciliation, 12 unique pin map, seven spares, no solder/PEEK/BeCu baseline, zero
  ceramic threads, nominal modeled bounds, independent service intent, explicit status labels.
- CONDITIONAL: continuous materials, feedthrough, magnetics, cable electrical behavior, package
  dimensions after correction, ceramic DFM, calibration, DAQ timing and cost.
- FAIL in current baseline: ambient sensor electrical isolation; A/B structural nut/load-path
  connectivity; KAP301 worst-case fit in 3.00-mm corridors; fabrication/energization readiness.

## 8. Source re-verification

Primary sources re-opened during this audit include:

- Spectrum LCC02046 drawing and product page;
- Accu-Glass 110240 19C connector drawing and live 19C-275 product page;
- Allectra KAP301 PDF/live product;
- TI SN74LVC125A Rev. T;
- RECOM RS6 Rev. 10/2024;
- Keysight DSOX1204G product page and 1000 X-Series data-sheet asset;
- SINTEF Al-wire aging publication record;
- NASA CR-143946 record;
- DLA MIL-STD-883 active-document record;
- TIMETAL 75A and Kyocera zirconia data.

Direct URLs and limitations remain in `outputs/SOURCE_LEDGER.csv`, expanded by S055 for the
Keysight data-sheet asset.

## 9. Red-team acceptance result

- Every prompt-named hazard explicitly audited: **PASS**.
- Maps, count, mirror involution, phase rates, cable geometry, package bounds, thermal displacement
  and ground path independently recalculated: **PASS**.
- Exact primary-source support re-opened for irreversible claims: **PASS WITH LIMITATIONS**.
- BLOCKER/MAJOR findings include affected artifact, evidence, correction and closure: **PASS**.
- Requirements trace covers hard constraints, stage deliverables and named hazards: **PASS**.
- Earlier Stage-10/20/30 outputs edited: **NO**.

Stage 40 result: **COMPLETE — BASELINE REQUIRES FINAL CORRECTIONS AND REMAINS WITH OPEN GATES**.
