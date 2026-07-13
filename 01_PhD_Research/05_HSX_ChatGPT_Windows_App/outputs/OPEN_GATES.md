# Open gates

Stages append unresolved fabrication, purchase, or qualification blockers here. Do not delete
earlier entries; mark them closed with evidence.

- Physical LCC02046 numbering direction from chamfer.
- Die p1/p2/p3/p4 orientation from GDS or microscope image.
- User's intended fourth inner/outer pad relationship: pad 14 versus pad 18.
- Exact continuous 250 deg C duty cycle and magnetic perturbation budget.
- Available bonding/joining equipment and conductor specification.
- 19C-275 vacuum-side protrusion and supported conductor range.
- Zirconia vendor fired tolerances, minimum wall/radius, processes, and 1/3/10-set quote.

## Stage 00 inventory additions - 2026-07-12

- `G00-01 HOLD - DO NOT BOND`: authoritative gen-2 die p1-p4 physical orientation/sign and alignment datum are absent. Close with GDS/runsheet or microscope sign-off; use only an orientation-parametric map meanwhile.
- `G00-02 CLOSED 2026-07-12 BY STAGE 10 VIEW RECONCILIATION`: the red inner bond is q4->14 in the cavity-up view; the green route is drawn on the mirrored bottom view, where 18 is left and 14 is right. Normalize the passive tie as `14<->18`. This closure does not release the rejected jumper network or the separate die-orientation gate.
- `G00-03 HOLD - DO NOT FABRICATE`: historical p1->1/p3->16/p2->11/p4->6 map is physically misregistered to the local chamfered drawing; top/right/bottom/left mid-side pads in the supplied image are 6/1/16/11. Re-derive under an explicit view/datum.
- `G00-04 HOLD - DO NOT FABRICATE`: the EPO-TEK 353ND die attach in each reusable bonded sensor/LCC has no continuous-250-deg-C UHV life qualification. Close with exact cure/material records and same-stack thermal-vacuum life testing or an authoritative continuous-use basis.
- `G00-05 HOLD - DO NOT FABRICATE`: PEEK insert and BeCu spring concepts are not qualified for retained geometry/force during continuous 250 deg C UHV service; catalog maxima and 200 deg C stress-relaxation data are insufficient.
- `G00-06 HOLD - DO NOT ORDER`: 19C-275 system needs manufacturer drawing/written confirmation for mated vacuum protrusion and diameter, conductor range, pin/contact materials and magnetic budget, exact continuous-temperature interpretation, and current 2026 availability/price; UW must confirm the assigned port and mounting datum.
- `G00-07 HOLD - DO NOT FABRICATE`: zirconia grade, drawing-specific fired tolerances, minimum features/radii/edge distances, post-fire operations, and 1/3/10-set quotes are absent.
- `G00-08`: continuous service duration, thermal ramps/cycle count, UHV pressure, and permissible magnetic perturbation at the Hall dies are not numerically specified; qualification must use a documented conservative envelope until confirmed.
- `G00-09`: available joining/bonding equipment, actual conductor alloy/insulation/gauge, die pad metallization, and wire alloy/diameter are missing.
- `G00-10`: J1 custom footprint physical pad numbering and connector shell-to-GND1 behavior require PCB source inspection or first-article continuity.

## Stage 05 evidence additions - 2026-07-12

- `G05-01 PARTIALLY CLOSED / HOLD - DO NOT BOND`: stage 10 resolved pad-14/pad-18 as a cavity-up versus mirrored-bottom-view notation issue and normalized it to `14<->18`. Physical LCC chamfer/pad continuity, purchased-lot metallization, authoritative die p1-p4/GDS or microscope orientation, and signed view datum remain open.
- `G05-02 HOLD - DO NOT RELEASE BONDED HEAD`: record actual die-pad metallurgy, 353ND lot/mix/cure/bondline, Al wire/tool/process, and pass a same-stack continuous-250-deg-C vacuum aging program with resistance, pull, fracture-mode, and contamination evidence. ASTM E595 or initial pull alone does not close this gate.
- `G05-03 HOLD - DO NOT FABRICATE CONTACTS`: the reusable LCC interface needs a frozen contact/pigtail architecture, exact alloy/temper/coating, UHV and magnetic declarations, normal-force and contact-resistance windows, independent strain relief, joining equipment capability, and aged qualification coupons. No catalog-qualified 250-deg-C UHV LCC02046 socket was found.
- `G05-04 HOLD - DO NOT ORDER`: before buying the 19C-275 system, obtain Accu-Glass and UW confirmation of mated vacuum geometry, supported contact/conductor range, exact continuous-temperature interpretation, Ni-Fe pin magnetic budget, port assignment, and mounting datum.
- `G05-05`: freeze the qualification envelope: continuous service duration, ramp rate, cycle count, UHV pressure/outgassing acceptance, permissible magnetic perturbation at each die, handling acceleration, harness proof load, and allowed electrical drift.
- `G05-06`: inspect live PCB source for J1 physical numbering/shell-to-GND1 and net-specific a0/a1/a2/EN fanout; resolve the approximately 109x bench amplitude anomaly before measured output is used as design evidence.
- `G05-07 HOLD - DO NOT FABRICATE CERAMIC`: obtain drawing-specific zirconia grade/process, fired/post-ground tolerances, minimum wall/web/radius, edge-chip allowance, inspection plan, and 1/3/10-set vendor quotes.
- `G05-08 HOLD - DO NOT ORDER NEAR-SENSOR HARDWARE`: identify exact fastener, contact, conductor, and underplate alloys; obtain magnetic permeability or screened-field acceptance and UHV cleaning/outgassing declaration for the delivered state.

## Stage 10 bond/join additions - 2026-07-12

- `G10-01 HOLD - DO NOT BOND`: the 14/18 view notation is closed, but physical LCC chamfer/1-20 continuity, purchased-lot finish, authoritative die p1-p4/GDS-to-microscope identity, no-mirror view, and two-person traveler sign-off remain required before using the physical q1/q2/q3/q4-to-8/3/19/14 map.
- `G10-02 HOLD - DO NOT RELEASE BONDED HEAD`: the actual 353ND/die-pad/Al-wire/LCC stack must pass the continuous-250-deg-C vacuum aging program in `outputs/10_BOND_AND_JOIN_QUALIFICATION.csv` with resistance, pull/shear, fracture-mode, cross-section, and contamination evidence.
- `G10-03 HOLD - DO NOT FABRICATE FANOUT`: select and declare the nickel-free fanout ceramic/metallization/finish, short microtransition, robust lane terminal, pigtail conductor, weld/crimp, magnetic behavior, and UHV cleaning. Qualify sacrificial coupons before exposing a real sensor.
- `G10-04`: inventory the actual wedge/ribbon bonder, tools and loop capability; resistance/parallel-gap welder; exact crimp tooling; pull/shear tester; cross-section/metallography; hot four-wire instrumentation; and 250-deg-C vacuum-aging capacity.
- `G10-05`: stage 30 must dimension and tolerance the vented guard, measured loop envelope, LCC/tongue seat, comb, service access, and independent strain-relief/load path inside the installed envelope.
- `G10-06`: qualification duration, ramps, cycles, sample count, confidence, electrical drift, pull/shear, isolation, outgassing, magnetic and proof-load limits await the signed service/error envelope; all provisional numeric limits remain `ENGINEERING PROPOSAL - VALIDATE`.

## Stage 20 board/harness additions - 2026-07-12

- `G20-01 HOLD - DO NOT TERMINATE`: prove and record all 19 vacuum-reference circuits to mirrored air connector cavities on first-article 19C hardware. Connector numbers are not printed and the male-to-male feedthrough reverses physical pin position; photograph the key/position mark and require two-person sign-off.
- `G20-02`: measure all R5-R8 pulldowns on all three boards; freeze final branch cable capacitance/length; validate SN74LVC125A OE safe state, 22-68-ohm branch-resistor selection, far-end levels, threshold recrossing, skew, ringing and analog settling at maximum phase rate.
- `G20-03 HOLD - DO NOT POWER REAL SENSORS`: resolve the approximately 109x amplitude anomaly with a known injected delta-V/gain test and replicate the phase/gain/polarity test on Board X/Y/Z.
- `G20-04 HOLD - PERFORMANCE CLAIM`: reconcile the retained 40-kHz nominal/100-kHz stated upper phase rate with the 10-20-kHz post-recombination target. Eight phases yield only 5-kHz updates at 40 kHz and require 160-kHz phases for 20-kHz updates before filter margin.
- `G20-05 HOLD - DO NOT CONNECT BIAS`: select and verify three current-source channels with true channel-to-channel and chassis isolation, 100-uA accuracy/noise, compliance and fault limiting; a grounded multichannel source is not presumed floating.
- `G20-06`: survey vessel, scope, 24-V supply and facility protective-earth paths; freeze the one AGND_STAR-to-chassis bond, branch bundle/overall-shield terminations, allowable ground current/noise, and the trigger for isolated logic plus differential acquisition.
- `G20-07 HOLD - DO NOT ORDER CABLE/CONNECTORS`: close the exact 19C PEEK/contact continuous-250-deg-C UHV, retained-force, magnetic, mated-geometry and cleaning gates; select exact in-vessel contacts, connector body, tools and screen clamp.
- `G20-08`: select exact ambient branch connectors, DE-9 male plugs/backshells, power distribution/protection, panel BNCs and junction enclosure; refresh 2026 price/stock and continuity-check all mating views.

## Stage 30 package additions - 2026-07-12

- `G30-01 HOLD - DO NOT FABRICATE`: obtain the exact mated 19C vacuum protrusion, diameter, support datum/tolerance, lower post attachment, UW port datum and magnetic/material acceptance. The current 11.050-mm-radius by 10.410-mm-high keep-out is conservative modeling input, not a released interface.
- `G30-02 HOLD - DO NOT FABRICATE HARNESS`: freeze conductor/insulation/shield type, finished OD, four-conductor branch lay, bend radius, proof load, cleaning and fit inside each 3.0-by-3.0-mm reserved corridor.
- `G30-03 HOLD - DO NOT FABRICATE CERAMIC`: obtain vendor-approved zirconia grade/process, fired and post-ground tolerances, radii/walls, flatness/orthogonality, inspection, cleaning and 1/3/10-set quote; confirm actual LCC body/material/thickness/warpage.
- `G30-04 HOLD - DO NOT FABRICATE RETENTION`: freeze exact CP-Ti grade/form/heat treatment, flexure geometry/stiffness/contact pads, 20/250-deg-C retained force/creep, rail compliance, ceramic contact stress and positive-retention proof.
- `G30-05 HOLD - DO NOT RELEASE BONDED CARTRIDGE`: close measured loop/heel envelope, guard clearance, handling jig, same-stack hot-vacuum bond/die-attach qualification and physical LCC orientation.
- `G30-06 HOLD - DO NOT RELEASE SERVICE PROCEDURE`: demonstrate one-axis removal/remating with the other sensors installed, actual chamber tool access, particles/chips, contact/insulation, hot cycle life and calibration repeatability.
- `G30-07 HOLD - DO NOT FABRICATE CONCEPT C`: close actual LCC thickness/warpage and the 0.10-mm nominal axial cassette clearance; freeze rear-tongue/contact detail.
- `G30-08 HOLD - DO NOT ORDER FASTENERS`: freeze exact screw/pin/nut alloy and finish, cleaning/UHV and magnetic declarations, venting/open-hole proof, hot galling/particle/reuse tests, torque and delivered inspection. NBK products are geometry evidence only.
- `G30-09 HOLD - DO NOT ISSUE PRODUCTION CAD`: replace conceptual sharp edges with vendor radii, add GD&T/datum scheme and released tolerance stack, freeze all material/part numbers, and pass the Stage-40 independent red team.

## Stage 40 independent red-team additions - 2026-07-12

- `G40-01 HOLD - DO NOT CONNECT THREE SENSORS`: the existing board netlists tie each selected sensor input to local `GND1` through R2/R3 (2.2 kohm each). Common scope, DAQ, supply, logic or `AGND_STAR` wiring therefore creates inter-axis current paths and violates the electrical-isolation requirement. Redesign around one galvanically isolated power/control/acquisition domain per board, then demonstrate the required isolation with every normal cable and shield installed.
- `G40-02 HOLD - DO NOT ISSUE PACKAGE CAD`: Concept A's CAD contains free nut-pad solids rather than a continuous base-to-nut reaction cage; Concept B is also structurally incomplete. Add a connected CP-Ti saddle/corner cage with captured, vented, replaceable, tool-accessible nonmagnetic nuts and prove that no load crosses an LCC, pad, bond, fanout or contact.
- `G40-03 HOLD - DO NOT FABRICATE HARNESS`: two KAP301 screened pairs can occupy 3.30 mm at the vendor's 1.65-mm structured-data diameter, exceeding the 3.00-mm modeled corridor before clearance or tolerance. Freeze a smaller qualified cable or enlarge the corridor and regenerate the full envelope, bend-radius and service-clearance checks.
- `G40-04 HOLD - DO NOT RELEASE ORIENTED MODULE`: retain the orientation-parametric q-to-pad map until die p1-p4 identity, LCC chamfer, cavity-up view and manufactured 1-20 continuity are recorded by microscope/traveler sign-off. The pad-14/route-18 notation itself is closed and shall not be reopened without contrary physical evidence.
- `G40-05 HOLD - DO NOT RELEASE HOT BONDED STACK`: catalog maxima, short vendor aging statements and generic materials data do not qualify the exact die-pad/353ND/Al-wire/Au-finish/LCC/fanout assembly for continuous 250-deg-C UHV life. Complete same-stack aging with electrical, mechanical, metallographic, contamination and magnetic endpoints.
- `G40-06 HOLD - DO NOT ORDER FEEDTHROUGH SYSTEM`: obtain written configuration evidence for the exact 19C feedthrough and mates, including view/continuity, mated keep-out, contact and pin alloys, supported conductor range, continuous-duty interpretation, magnetic acceptance, cleaning, UW port datum and first-article traveler.
- `G40-07 HOLD - DO NOT POWER REAL SENSORS`: close the approximately 109-times anomaly and qualify three isolated current sources for compliance, reversal, noise, drift, fault limiting and cable/sensor bounds; qualify an isolated simultaneous-sampling acquisition path with explicit aperture-skew and common-mode limits.
- `G40-08 HOLD - DO NOT FABRICATE/ORDER FINAL BASELINE`: Stage 50 must incorporate—not merely cite—the isolation, structural-cage and harness corrections, carry every remaining blocker into the release checklist, reconcile all final drawings/tables/CAD, and leave the project `COMPLETE_WITH_OPEN_GATES` unless objective closure evidence exists.

## Stage 50 consolidated release gates - 2026-07-12

- `G50-01 HOLD - DO NOT FABRICATE/ORDER`: sign the governing service and error envelope: continuous 250-deg-C duration, ramps/cycles, UHV pressure/outgassing/contamination, magnetic perturbation at each die, bandwidth/update/noise/drift, proof load/shock, insulation/leakage and service-cycle limits. Provisional numerical limits do not close this gate.
- `G50-02 HOLD - DO NOT BOND/RELEASE CARTRIDGE`: close physical P(q1..q4), cavity-up/chamfer/no-mirror continuity, die/LCC/353ND/Al-wire same-stack life, measured loop/guard, exact no-Ni fanout/metallization, robust weld/crimp terminal, independent strain relief, cleaning and magnetic qualification. The 14/18 notation is closed; the user jumper network remains rejected.
- `G50-03 HOLD - DO NOT ORDER/FABRICATE HARNESS`: close the exact 19C configuration/mirror/mated datum/contact/wire/magnetic/continuous-duty evidence and UW interface. Freeze the exact two-pair branch cable, delivered OD/lay/length/capacitance/bend/screen clamp/termination; prove it in the corrected 3.80-mm corridor or regenerate CAD.
- `G50-04 HOLD - DO NOT FABRICATE CERAMIC/ISSUE PRODUCTION CAD`: obtain zirconia grade/process, post-fire operations, radii/web/edge/tolerance/GD&T/cleaning/yield and 1/3/10-set RFQs. Regenerate complete CAD with vendor and feedthrough inputs; pass envelope/tolerance/contact/connectivity/collision/tool/bend/service and drawing-table audits.
- `G50-05 HOLD - DO NOT FABRICATE/ORDER RETENTION`: freeze CP-Ti grade/form/heat-treatment/finish, connected cage manufacture, formed flexure and hard stops, contact stress, six vented nut plates/keepers, post/lower interface and strain clips. Pass 20/250-deg-C force/dwell/cycle, FEA/contact, galling/particle/reuse, vent/pump-down, magnetic and proof-load tests.
- `G50-06 HOLD - DO NOT CONNECT REAL SENSORS`: implement and qualify three separate GND1_X/Y/Z power/control/acquisition domains; select isolated 100-uA sources, four-line barriers and simultaneous isolated/differential DAQ. Resolve the approximately 109-times anomaly and prove all-cables-installed DC isolation, leakage/capacitance/common-mode/fault, logic/OE/ringing/skew/settling and emulator performance.
- `G50-07 HOLD - DO NOT ORDER NEAR-SENSOR HARDWARE/PERFORMANCE CLAIM`: freeze the numerical magnetic-error budget; screen delivered feedthrough, fasteners, nut plates, keepers, clamps, cable screens, contacts, underplates, welds and assembled head before/after bake. Complete hot three-axis vector calibration and service repeatability.
- `G50-08 HOLD - DO NOT RELEASE`: execute `50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv`, link objective evidence to every applicable checklist line, and run a final independent configuration review. Until then the package status is `COMPLETE_WITH_OPEN_GATES`; no fabrication, order, real-sensor energization or performance claim is authorized by these documents.

## Stage 30D cost-down package additions - 2026-07-13

- `G30D-01 HOLD - DO NOT ORDER FLAT GUARD`: obtain drawing-specific 99.6-percent alumina and flat ZTA/zirconia alternate DFM, material-lot data, laser edge/chip/heat-affected limits, cleaning/packaging, first-article inspection, hot-UHV witness and comparable 3/9/30-piece quotes. Commercial substrate capability does not qualify the HSX guard.
- `G30D-02 HOLD - DO NOT FABRICATE/BOND CARTRIDGE`: record the purchased LCC lot geometry/metallization and physical orientation; measure die/bond-loop/heel/fanout/pigtail envelopes; freeze the flat-guard attachment and minimum 0.30-mm loop clearance; pass service sweep, continuity/isolation and same-stack hot-vacuum qualification.
- `G30D-03 HOLD - DO NOT FABRICATE FOLDED BRACKET`: obtain vendor flat-pattern, bend radius/relief/neutral-axis/springback/stress-relief, coined three-point lands, face/window/slot/ligament GD&T, material/cleaning and complete tolerance CAD. Two bends are not assumed to be calibrated orthogonality.
- `G30D-04 HOLD - DO NOT FABRICATE CLAMPS`: close one-screw/two-hook flexure FEA, ceramic contact pressure, hook/slot/0.60-mm screw-ligament stresses, 20/250-deg-C free height/force/dwell/cycles, vibration and repeated service coupons.
- `G30D-05 HOLD - DO NOT ORDER FACE HARDWARE`: freeze exact Ti screw, vented captive nut plate and integral no-drop lance; prove reaction load bypasses the lance, and pass torque, galling, particle, venting, magnetic, retention and replacement tests.
- `G30D-06 HOLD - DO NOT FABRICATE INTERFACE/HARNESS`: close the exact mated feedthrough datum/lower post attachment and three delivered cable branch OD/lay/bend/screen/comb/strain-relief trials in the 3.80-mm paths.
- `G30D-07 HOLD - PERFORMANCE CLAIM/SERVICE RELEASE`: sign the angular/magnetic error budget; measure the three active planes; pass 20/250-deg-C full 3x3 vector calibration stability after bake, hot cycles and independent remove/reinstall; pass a gloved chamber-tool service trial with zero neighbour removal.
- `G30D-08 HOLD - DO NOT ORDER`: obtain comparable drawing-identical 1/3/10-head RFQs with NRE, accepted parts, assembly, inspection, yield/scrap, service spares and qualification separated. Part/volume reduction is not a dollar quote.

## Stage 40D independent cost-down red-team additions - 2026-07-13

- `G40D-01 HOLD - DO NOT ISSUE COST-DOWN CAD`: replace the closed hook slots with true open U-slots, use at least 1.4-mm nominal disengagement motion, add the missing screw-edge relief to one identical guard geometry, and include the guards explicitly in collision/identity checks.
- `G40D-02 HOLD - DO NOT RELEASE CARTRIDGE LOAD PATH`: define and model a formed perimeter cartridge caddy that mechanically captures the flat guard/LCC/fanout/pigtail and alone receives clamp/datum loads; add nine coined structural lands and prove three-point caddy reactions with no load through ceramic/LCC/electrical joints.
- `G40D-03 HOLD - DO NOT CLAIM COMPLETE ENVELOPE`: add three supported strain clips with adjacent solid lugs/screws/open nuts, four top post fasteners and positive no-drop nut-lance/pocket envelopes; rerun all installed-envelope, feedthrough and collision checks.
- `G40D-04 HOLD - DO NOT FABRICATE ONE-SCREW CLAMP`: prove two-hook/one-screw/three-pad load sharing, open-slot bearing, torsion, ceramic/caddy contact, 20/250-deg-C force/dwell/cycles, vibration and service particles; revert to two screws per face if any acceptance limit fails.
- `G40D-05 HOLD - DO NOT FREEZE CERAMIC MATERIAL`: the cost-down decision controls flat geometry, not 99.6-percent alumina. Quote alumina and flat ZTA/zirconia to the same drawing and select only after edge, cleaning, magnetic and hot-UHV first-article/coupon evidence.
- `G40D-06 HOLD - PERFORMANCE CLAIM`: measure coined lands and active planes; field-map the complete delivered Ti/caddy/fastener head; pass full 3x3 vector-matrix stability at 20/250 deg C after bake, hot cycles and independent service within a signed angular/magnetic budget.
- `G40D-07 HOLD - DO NOT CLAIM DOLLAR SAVINGS`: include caddies and all post/strain/nut hardware in the cost basis. Keep 21-to-9 limited to face-retention parts and 26.4-percent limited to geometric material volume; obtain comparable drawing-identical 1/3/10 quotes.
- `G40D-08 HOLD - DO NOT RELEASE FINAL BASELINE`: Stage 50D must implement F40D-B01 through B08 and every resolvable MAJOR correction in new complete CAD, drawings, ledgers and final reports, repeat whole-package checks, and preserve all unresolved external gates.
