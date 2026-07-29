# Decision log

For each decision record: ID, timestamp, stage, decision, alternatives, evidence/calculation,
consequences, confidence limitation, and what new evidence would reverse it.

## D00-01 - Historical fixed LCC map is not fabrication-authoritative

- Timestamp/stage: 2026-07-12T20:27:23-07:00, stage 00.
- Decision: retain the historical mid-side pad set `{1,6,11,16}` as a comparison only; do not reuse the historical p1->1/p3->16/p2->11/p4->6 physical association. Stage 10 must use the supplied chamfered top-view drawing and remain orientation-parametric until microscope/GDS sign-off.
- Alternatives: copy the historical map; accept the user's 8/3/19/14 map immediately.
- Evidence: original-resolution inspection of `inputs/reference/user_2026-07-12_LCC_routing_annotated.png` shows top/right/bottom/left mid-side pads 6/1/16/11 and red corner-adjacent bonds 8/3/19/14; gen-2 die p-label orientation remains absent.
- Consequence: prevents a mirrored/rotated irreversible bond; delays no reversible work.
- Reversal trigger: authoritative physical carrier/drawing plus die GDS/microscope traveler proving a fixed mapping.

## D00-02 - Continuous 250 deg C life invalidates prior PEEK/BeCu qualification claim

- Timestamp/stage: 2026-07-12T20:27:23-07:00, stage 00.
- Decision: treat PEEK inserts, BeCu springs, 353ND die attach, and Au-Al bonds as unqualified at continuous 250 deg C UHV until exact-material life evidence or same-stack testing closes the gate.
- Alternatives: accept catalog maximum/bake survival; reject every material without testing.
- Evidence: historical reports rely on 150 deg C bake survival, 200 deg C BeCu data, and catalog continuous-use maxima rather than continuous 250 deg C system qualification; current contract explicitly prohibits those substitutions.
- Consequence: stage 05 must seek higher-temperature contact/insulation alternatives and a qualification plan; historical geometry can still be reused.
- Reversal trigger: primary continuous-life data at the actual stress/environment or passed thermal-vacuum coupons with retained force/resistance/dimensions.

## D00-03 - Reuse historical measurements, not historical recommendation

- Timestamp/stage: 2026-07-12T20:27:23-07:00, stage 00.
- Decision: preserve kernel-measured user-CAD dimensions, netlist traces, FMEA logic, and prior red-team findings; re-evaluate the bond, feedthrough, and package baseline under the new constraints.
- Alternatives: discard prior work; copy the prior synthesis.
- Evidence: supplied/historical STEP files reopened successfully; historical Concept B omits its asserted contacts and violates current material/thread-access preferences, while user-CAD measurements reproduce.
- Consequence: saves deterministic work without inheriting obsolete assumptions.
- Reversal trigger: none; this is the evidence-separation rule for the mission.

## D05-01 - Catalog maximum is a boundary, not continuous-life margin

- Timestamp/stage: 2026-07-12T20:40:52-07:00, stage 05.
- Decision: classify exact-250-deg-C PEEK cables/connectors, 19C feedthrough interpretation, and nominal 250-deg-C contact claims as conditional until exact-material continuous-life evidence or same-stack testing exists.
- Alternatives: accept maximum operating temperature at face value as unlimited continuous-life qualification; reject all exact-250-deg-C products outright.
- Evidence/calculation: Accu-Glass lists 250 deg C as both maximum operating and bake temperature for the 19C PEEK cable; Victrex distinguishes Tg/RTI categories; Materion identifies time-temperature stress relaxation. The operating point has zero catalog temperature headroom.
- Consequences: favor higher-temperature ceramic/Kapton/metal elements where practical and retain controlled qualification gates for unavoidable exact-rated components.
- Confidence limitation/reversal: written manufacturer continuous-duty declaration for the exact assembly plus retained-property data, or passed project coupons, can close a specific gate.

## D05-02 - No catalog-qualified LCC02046 reusable socket has been established

- Timestamp/stage: 2026-07-12T20:40:52-07:00, stage 05.
- Decision: treat the reusable LCC disconnect as a designed subsystem; compare a custom qualified contact cartridge against a permanently joined LCC pigtail with a remote high-temperature service terminal in stage 10.
- Alternatives: assume a standard LCC socket; permanently entomb the carrier; place the service joint in the die-bond load path.
- Evidence/calculation: Spectrum allows sockets generally but supplies no 250-deg-C UHV socket qualification; Accu-Glass has 400-deg-C bare in-line terminals at larger scale; Deringer-Ney offers custom 250-deg-C contacts without UHV/magnetic qualification.
- Consequences: the final package must give independent strain relief and must protect each bonded die/LCC during removal.
- Confidence limitation/reversal: an exact part with continuous-250-deg-C UHV, magnetic, force, resistance, cycle-life, and dimensional evidence would replace the custom subsystem.

## D05-03 - Shared digital timing does not authorize shared analog returns

- Timestamp/stage: 2026-07-12T20:40:52-07:00, stage 05.
- Decision: stage 20 may share phase-control logic after fanout verification, but three 100-uA sensor bias loops and analog channels remain independently floating/fault-contained; simultaneous acquisition must use a genuine multi-channel acquisition path rather than assuming the Pico ADC is simultaneous.
- Alternatives: one board receives and retransmits analog data; share sensor returns; sample three Pico ADC pins as if simultaneous.
- Evidence/calculation: RP2350 GPIO and ADG input capacitance make logic fanout credible; RP2350 exposes a shared ADC peripheral; Keysight DSOX1204G has four analog channels; local locked constraints require independent floating bias.
- Consequences: stage 20 will quantify the shared logic network, explicit ground references, three isolated board supplies/biases, and three concurrent analog outputs plus sync.
- Confidence limitation/reversal: a validated local simultaneous digitizer may replace the bench DAQ path, but it does not change four-terminal isolation through the feedthrough.

## D10-01 - Normalize 14/18 by view, not by guessed signal direction

- Timestamp/stage: 2026-07-12, stage 10.
- Decision: use the cavity-up sequence top 8-7-6-5-4, right 3-2-1-20-19, bottom 14-15-16-17-18, left 9-10-11-12-13. Interpret the green bottom-view line as the unordered passive tie `14<->18`, with q4's red inner bond at pad 14.
- Alternatives: retain the earlier mistaken cavity-up bottom sequence; treat `18->14` as evidence that q4 bonds to 18; ask the user to arbitrate an issue resolvable from the drawing views.
- Evidence/calculation: direct original-resolution inspection shows the left drawing is cavity-up and the right drawing is a mirrored bottom view; pin-1/chamfer and all edge labels mirror consistently.
- Consequences: G00-02 closes, G05-01 narrows to orientation/chamfer/lot evidence, and all new drawings can use one unambiguous cavity-up datum. The external four-jumper network remains rejected on engineering grounds.
- Confidence limitation/reversal: only an official revised Spectrum drawing or physical continuity inspection contradicting the supplied view would reverse the numbering convention.

## D10-02 - Put the one-side service boundary in a protected cartridge fanout

- Timestamp/stage: 2026-07-12, stage 10.
- Decision: retain q1/q2/q3/q4-to-8/3/19/14 only as a signed shortest/non-crossing physical map; reject the four external pad-to-pad jumpers; recommend a removable die/LCC/fanout-tongue/pigtail cartridge with short qualified same-numbered castellation transitions, supported robust pigtail joints, a vented zirconia guard, independent ceramic strain relief, and a remote accessible disconnect.
- Alternatives: user's four-jumper network; direct welded/crimped flying lead at each castellation; custom 250-deg-C spring socket; shortest bonds with no protected breakout.
- Evidence/calculation: LCC traces reach only same-numbered castellations; the four user ties do not place four lands on one side and add spans/joints. Al-on-thin-Au has relevant 250-deg-C aging precedent, while no exact continuous-250-deg-C UHV LCC socket was found. The remote terminal allows robust welding/crimping without loading thin ceramic metallization.
- Consequences: stage 30 must fit/protect the cartridge/tongue/guard/comb; the complete bonded unit remains independently removable/reusable; parallel bonds provide only electrical redundancy, never strain relief.
- Confidence limitation/reversal: flip to direct-tab concept C if sacrificial castellation weld coupons outperform the tongue without damage, or to socket concept D if an exact part closes UHV/magnetic/force/resistance/cycle/envelope gates.

## D10-03 - No solder in the baseline continuous-250-deg-C LCC transition

- Timestamp/stage: 2026-07-12, stage 10.
- Decision: prohibit solder in the recommended LCC-to-tongue-to-pigtail baseline and in every structural/strain-relief path.
- Alternatives: 80Au20Sn; Accu-Glass 110796; separately processed AuGe/AuSi terminal.
- Evidence/calculation: 80Au20Sn melts at 280 deg C, so at 250 deg C `T/Tm=523.15/553.15=0.946`; its 30-deg-C margin and high homologous temperature do not establish creep/contact life. Accu-Glass documentation contains a 280/480-deg-C inconsistency. Higher-melting alloys need separate metallization/process/UHV coupons and cannot be applied casually to an assembled sensor.
- Consequences: use qualified Al microbonds plus resistance-welded or exact-contact crimped robust terminals; no flux/residue burden in the baseline.
- Confidence limitation/reversal: a specific soldered joint may be considered only with exact alloy/process/cleaning/metallization, independent strain relief, and passed continuous-life coupons; it would not reopen load-through-joint permission.

## D20-01 - Interface junction plus three parallel analog boards

- Timestamp/stage: 2026-07-12, stage 20.
- Decision: use one ambient interface junction, one Pico state/sync source, three independent quad-buffer branches, three identical `hsx_2026_v2` boards, three independent floating 100-uA sources, and a simultaneous 3-analog-plus-sync DAQ. No analog board receives data or relays to another.
- Alternatives: direct unbuffered star; one analog board as master/data relay; ambient local digitizer; in-vessel digitization.
- Evidence/calculation: live trace gives only 12/12/18/12-pF a0/a1/a2/EN silicon loads across three boards, but R5-R8 and cable loads are unverified. Three quad buffers cheaply isolate branch faults and provide series-resistor/test access. Existing boards output analog only; grounded four-channel scope already supplies concurrent acquisition.
- Consequences: one small ambient junction adds mirror/test/ground discipline without redesigning the analog boards; all 12 sensor nets and three bias loops remain independent.
- Confidence limitation/reversal: bypass buffers only after final-cable criteria pass; adopt a simultaneous junction ADC if long analog runs/automation justify redesign; never move electronics into the hot UHV volume under current constraints.

## D20-02 - Assign 19C by vacuum-reference circuits with explicit air-side mirror

- Timestamp/stage: 2026-07-12, stage 20.
- Decision: define V1-V4=X p1/p3/p2/p4, V5-V8=Y, V9-V12=Z, reserve V13-V19, and wire air connector cavities using the official horizontally mirrored pattern: A1/A12/A11/A10, A9/A8/A7/A6, A5/A4/A3/A2.
- Alternatives: label both connector faces 1-19 without mirror correction; allocate shield/ground pins; share returns; choose a nonsequential performance-optimized pattern.
- Evidence/calculation: Accu-Glass describes straight-through male-to-male construction, pin-position reversal, a 19-cavity rear-view pattern, and numbers not appearing on the part. Nineteen circuits leave seven spares after twelve signals.
- Consequences: the CSV provides a unique circuit/air-cavity/J1 endpoint and a mandatory full continuity traveler. Six screens terminate at the flange rather than consuming pins.
- Confidence limitation/reversal: first-article continuity is controlling and may correct the inferred mirror table before contacts are locked; no termination is released from the drawing alone.

## D20-03 - Controlled common ambient reference, isolated Hall loops

- Timestamp/stage: 2026-07-12, stage 20.
- Decision: intentionally common the three board GND1 references at one AGND_STAR/interface panel because the DSOX1204G BNC shells already common them to protective earth. Use one co-routed branch bundle per board; overall branch shields bond at panel only. Keep 12 Hall terminals, three current-source outputs/returns and all in-vessel circuits isolated from AGND/chassis.
- Alternatives: pretend boards remain galvanically isolated while grounded scope coaxes connect them; add multiple Pico ground straps and long J4 coaxes; isolate only digital control; fully isolated digital and differential acquisition.
- Evidence/calculation: board J3 has no ground pin and J4 return is GND1; RS6 isolation capacitance is 110 pF max and is functional, not protective. A grounded scope creates the common point regardless of intent.
- Consequences: grounding is inspectable and lower cost, but AGND faults are a known shared path. Survey facility earth before adding a link and upgrade both control/acquisition together if common-ground noise fails.
- Confidence limitation/reversal: measured loop current/noise/common-mode failure triggers galvanically isolated control plus differential/isolated simultaneous acquisition.

## D20-04 - Do not claim 20-kHz recombined bandwidth from 40-kHz phases

- Timestamp/stage: 2026-07-12, stage 20.
- Decision: architecture supports higher-rate tests, but performance remains held until phase switching, blanking, raw sample rate and demodulated response are measured.
- Alternatives: equate analog component bandwidth with recombined bandwidth; interpret three Pico ADC pins as simultaneous; ignore the eight-phase update cadence.
- Evidence/calculation: one update is `8/f_phase`; 40 kHz gives 5 kHz, 80 kHz gives 10 kHz, 100 kHz gives 12.5 kHz, and 160 kHz gives 20 kHz before filtering. Retained notes call 100 kHz the upper usable phase rate.
- Consequences: sync/raw capture and future ADC criteria are designed for validation, while final bandwidth claims remain G20-04.
- Confidence limitation/reversal: passed settling/noise/demod tests at a signed phase rate close the gate and set the final anti-alias/decimation design.

## D30-01 - Put every service fastener outside zirconia and outside adjacent positive faces

- Timestamp/stage: 2026-07-12, stage 30.
- Decision: use a connected CP-Ti base/cage, open through-fasteners and replaceable external Ti nut pads. A/B side fasteners occupy only the unused negative local edge; top fasteners occupy -X/-Y edges. C pins use the same negative-edge rule and vertically separated X/Y levels. Ceramic thread count is zero and cartridge retention load bypasses all electrical joints.
- Alternatives: M1.6 holes through thin zirconia rings; internal/tapped zirconia holes; opposed bolts at the shared +X/+Y corner; hidden nuts; overlapping rails; blind threaded Ti pockets.
- Evidence/calculation: first kernel iterations exposed weak ceramic ligaments, disconnected posts, crossed axes and adjacent-face collisions. Moving axes outside ceramic and to unused negative edges produced 0.000000-mm3 unintended pairwise overlap for all three concepts. NBK supports the general vacuum-venting rule and miniature Ti geometry, while exact 250 C UHV hardware remains held.
- Consequences: straight external tool access and independent cartridge removal are credible; clamps are larger than cartridges but still far inside the radial limit. More external Ti frame area and custom nut pads are required.
- Confidence limitation/reversal: vendor DFM, hot galling/creep coupons, exact mated feedthrough geometry and service demonstration must pass before release; a qualified alternative may replace the candidate screw while preserving axes and zero ceramic threads.

## D30-02 - Select modular tri-plate Concept A for red team

- Timestamp/stage: 2026-07-12, stage 30.
- Decision: select Concept A as the baseline because, after the same hard material/envelope/reuse gates, three identical flat 9.60-mm zirconia seats minimize ceramic NRE and localize scrap while retaining the Stage-10 protected cartridge and remote pigtail disconnect. Weighted result is A 96, B 81, C 77 using the binding 30/25/25/10/10 weights.
- Alternatives: B monolithic 11.30-mm core; C 10.50-mm core with split rear-datum/Ti-guard cassettes and shared rail cage.
- Evidence/calculation: A/B/C all kernel-pass at conservative radius 14.354 mm, heights 26.70/27.00/26.55 mm and zero critical overlap. Proposed worst heights are 27.11/27.36/26.91 mm. A has the simplest/repeated ceramic parts; B has best orthogonality potential but greatest single-part ceramic risk; C best contains a handled cassette but adds pin/rail/rear-contact stacks.
- Consequences: Stage 40 audits A as recommended and B/C as alternatives. No ceramic or fastener order is authorized; numerical price ranges remain pending 1/3/10-set RFQs.
- Confidence limitation/reversal: choose B if an inspected core meets the explicitly proposed 1.5x all-in A-seat decision threshold and improves repeatability; choose C only if frequent hot/cold service-cycle evidence justifies the mechanism. Any feedthrough, flexure, magnetic, harness or vendor-DFM failure triggers redesign.

## D40-01 - Reject the common-GND1 ambient baseline

- Timestamp/stage: 2026-07-12, stage 40.
- Decision: supersede D20-03 for simultaneous three-axis operation. Use one galvanically isolated power/control/acquisition domain per board; do not connect grounded BNC shells or a common `AGND_STAR` across board GND1 domains while the three Hall sensors are connected.
- Alternatives: retain the controlled common ground; isolate current sources only; buffer shared logic without isolation; sequentially disconnect scope grounds by procedure.
- Evidence/calculation: the live netlist connects each selected `/in+` and `/in-` line to local GND1 through R2/R3=2.2 kohm. Commoning two board grounds therefore provides an intentional sensor-to-sensor path of approximately `2.2k + 2.2k + mux Ron`; a logic buffer is not a galvanic barrier.
- Consequences: Stage 50 must preserve the 12-conductor map but replace the ambient ground/control/DAQ baseline, and it must require an all-cables-installed isolation and simultaneous-capture qualification.
- Confidence limitation/reversal: this decision can be relaxed only if an authoritative revised board topology or measurement proves the sensor networks have no prohibited inter-axis path with the complete acquisition system connected.

## D40-02 - Retain Concept A only as a corrected procurement direction

- Timestamp/stage: 2026-07-12, stage 40.
- Decision: Concept A remains the preferred low-NRE architecture only after adding a continuous CP-Ti saddle/corner cage from base to every nut reaction, captured vented replaceable nuts and a complete independent strain-relief path. Current A/B CAD is NOT FOR FABRICATION.
- Alternatives: accept collision-free free nut-pad solids as structural hardware; promote B despite the same missing reaction cage; select C before closing its 0.10-mm axial stack and rail/contact details.
- Evidence/calculation: the CAD generator creates separate nut-pad solids; A adds only three rear rails and B no continuous saddle cage. Zero solid overlap proves clearance, not physical capture or a base-connected load path.
- Consequences: Stage 50 must show the corrected load-path topology and require regenerated complete-assembly CAD, connectivity, tolerance, tool, vent and service checks before any released drawing.
- Confidence limitation/reversal: a vendor-developed alternative cage may replace the proposed topology if it preserves zero ceramic threads, straight accessible fasteners, independent service, nonmagnetic/UHV materials and no load through electrical joints.

## D40-03 - Reject the 3.00-mm two-pair harness corridor

- Timestamp/stage: 2026-07-12, stage 40.
- Decision: do not fabricate the Stage-30 3.00-by-3.00-mm branch corridor around two KAP301 screened pairs. Freeze a smaller continuous-250-deg-C UHV cable/lay or enlarge and reroute the corridor before regenerating the package.
- Alternatives: rely on the 1.50-mm nominal diameter with zero clearance; compress two screened cables; omit delivered-diameter tolerance or bend sweep.
- Evidence/calculation: the manufacturer PDF gives `1.5 +/- 0.15 mm`; two worst-case pairs require 3.30 mm before installation clearance, abrasion allowance or clip deformation.
- Consequences: cable selection and package envelope are now one coupled release gate; Stage 50 may specify a sizing rule but cannot release dimensions without delivered cable evidence.
- Confidence limitation/reversal: physical first-article cable measurements and a passed hot-vacuum corridor/bend/proof-load trial control the final geometry.

## D50-01 - Make isolated GND1_X/Y/Z the controlling ambient baseline

- Timestamp/stage: 2026-07-12, stage 50.
- Decision: the final system has three galvanically separate board/current/control/acquisition domains. One Pico phase state, one upstream protected 24-V input and one post-isolation timebase may be shared; GND1_X/Y/Z may not be joined through BNC, USB, logic return, source return, probe or chassis.
- Alternatives: retain D20-03 common AGND_STAR; isolate only the current sources; isolate only digital control; operate by manually removing grounded coaxes.
- Evidence/calculation: D40-01/F40-B01 live-netlist path through R2/R3 proves a common GND1 violates the binding electrical-isolation requirement. The final domain map removes the intentional DC path while preserving the accepted 12-conductor physical map.
- Consequences: exact current sources, four-line barriers and simultaneous isolated/differential DAQ are G50-06 purchase/design gates; direct multi-BNC scope capture is not the baseline.
- Confidence limitation/reversal: a future topology may use a different isolation implementation only if all normal cables installed still prove the signed DC/leakage/capacitance/common-mode/fault and simultaneous-skew requirements.

## D50-02 - Control corrected Concept A and supersede Stage-30 A geometry

- Timestamp/stage: 2026-07-12, stage 50.
- Decision: use three identical flat zirconia seats in one connected CP-Ti base/backframe/reaction cage with six open-sided vented replaceable nut plates, external keepers, straight negative-edge hardware and 3.80-mm branch corridors. All final CAD remains NOT FOR FABRICATION.
- Alternatives: accept Stage-30 free nut pads/3.00-mm corridors; select monolithic B; select split cassette C.
- Evidence/calculation: the corrected generator found and removed previously unscoped base/cartridge, post-spoke/clamp, backframe/seat, strain-rail, bolt and nut-pocket interferences. Final reimport: 39 valid solids; radius 14.354 mm; height 26.750 mm; one cage solid; six zero-distance nut reaction contacts; zero unintended overlap; 0.000000-mm bound delta.
- Consequences: A remains the lowest-NRE procurement direction, but G50-03/04/05 must supply exact cable, feedthrough, zirconia, Ti flexure/hardware, GD&T and service evidence before production CAD.
- Confidence limitation/reversal: B may replace A only after the same hard gates and comparable 1/3/10 total-cost evidence; C only after its axial/contact/service-cycle value closes.

## D50-03 - Complete the engineering package with explicit open gates

- Timestamp/stage: 2026-07-12, stage 50.
- Decision: declare the requested engineering-package work `COMPLETE_WITH_OPEN_GATES`, with G50-01 through G50-08 controlling and explicit holds on fabrication, purchase, bonding, real-sensor power and performance claims.
- Alternatives: stop at IN_PROGRESS because qualification inputs are absent; declare unconditional COMPLETE; ask the user to guess orientation, duty duration or magnetic budget.
- Evidence/calculation: all seven stage markers pass their acceptance checks; final recommendation/checklist/provenance/index and corrected maps/drawings/CAD/ledgers exist; the whole-package audit passes 17/17; remaining items require external vendor, physical, facility or qualification evidence and cannot be truthfully manufactured from chat analysis.
- Consequences: the package is a complete decision, RFQ and qualification basis, not a fabrication release. Closure requires objective checklist evidence, not confidence scoring.
- Confidence limitation/reversal: state may change to unconditional COMPLETE only after every fabrication/order-blocking checklist line and G50 gate is objectively closed and independently reviewed.

## D30D-01 - Replace fixed ceramic seats with a folded flat-part package

- Timestamp/stage: 2026-07-13, Stage 30 cost-down revision.
- Decision: supersede corrected Concept A's physical head with D1: one laser-cut/two-main-bend CP-Ti trihedral bracket, four simple vented posts, three existing protected cartridges using one identical flat 10.90 x 10.90 x 0.635-mm ceramic guard geometry, and one-screw/two-hook face clamps. Fixed structural ceramic count becomes zero; ceramic thread count remains zero.
- Alternatives: D2 three repeated Ti face modules; D3 direct Ti-to-LCC clip; retain corrected A with three fixed zirconia seats.
- Evidence/calculation: primary manufacturers support stock alumina substrate and tooling-free CAD laser cutting as a small-lot process direction (S056-S058). OpenCascade reimport proves radius 14.779 mm, height 26.250 mm, zero unintended overlap, three clear 3.80-mm cable corridors, three nut and four post reaction contacts, and zero bound delta. Controlled face-retention parts fall from 21 to 9.
- Consequences: complex fixed ceramic CNC and the machined connected backframe are removed; the user's reusable bonded LCC service boundary is preserved. Accuracy is protected by measured coined lands and a full 3x3 hot vector calibration, not an assumed perfect bend. G30D-01 through G30D-08 control fabrication, purchase and performance release.
- Confidence limitation/reversal: choose D2 only if drawing-identical RFQs and hot service/metrology show lower accepted cost with equal matrix stability. If alumina fails its UHV/edge gate, retain the same flat geometry in qualified ZTA/zirconia; do not return to a pocketed monolithic ceramic body.

## D40D-01 - Retain the flat-part direction but reject Stage-30D as final CAD

- Timestamp/stage: 2026-07-13, Stage 40D independent delta review.
- Decision: D1 survives as the cost-down architecture, but the frozen Stage-30D geometry is audit evidence only. Final CAD must use true open hook slots, 1.4-mm slide, one identical screw-relieved guard, a load-bearing perimeter cartridge caddy, nine coined lands, complete strain/post/nut-retention hardware and recalculated bounds.
- Alternatives: release Stage-30D despite open/closed slot and guard contradictions; revert to the fixed zirconia seats; reject the one-screw cost-down direction without a coupon fallback.
- Evidence/calculation: independent STEP reimport confirms the nominal 20-solid bounds but direct code/geometry review proves closed hook slots, insufficient 0.8-mm motion, 0.45-mm screw intrusion into the unrelieved guard, absent hard-stop/caddy geometry, floating strain clips and missing post fasteners. Eight BLOCKERs and nine MAJOR findings have explicit final corrections/closure tests.
- Consequences: cost-down still does not require any fixed/monolithic ceramic. The final face-retention claim remains a validation target with a two-screw fallback. Flat guard material remains unselected between alumina and qualified flat ZTA/zirconia. No dollar saving is asserted without RFQ.
- Confidence limitation/reversal: D1 may be replaced by D2 or two-screw D1 only if complete hardware/CAD or hot-service evidence fails. No design may remove independent cartridge reuse or restore internal ceramic threads.
