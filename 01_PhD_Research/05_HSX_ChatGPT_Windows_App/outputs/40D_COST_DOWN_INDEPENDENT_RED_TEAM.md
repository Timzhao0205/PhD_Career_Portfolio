# Stage 40D — independent red team of the cost-down package

**Review rule:** Stage-30D files were frozen at commit
`21880b14d9bfd3be4a11b990f571ad4adb73ea19`.  This review did not edit them.
Corrections go only into new final Stage-50D artifacts.

## 1. Executive result

The cost-down direction is sound, but the Stage-30D model is **not yet the controlling final CAD**.
Independent review found eight release BLOCKERs, nine MAJOR findings, three MINOR findings and five
NOTE/PASS findings.

The most important verified positives are:

- the exported modeled assembly independently reimports as 20 solids;
- its bounding box is x/y `-10.150 to +10.450 mm`, z `0.000 to 26.250 mm`;
- conservative radius is `14.778532 mm`, leaving `1.096468 mm`, and height margin is `1.250 mm`;
- modeled part-pair overlaps are zero;
- fixed structural ceramic count and ceramic thread count are zero;
- the cost reduction does not require changing the accepted electrical map or cartridge service
  boundary.

The most important new contradictions are:

1. the CAD hook slots are closed, although the report and service drawing call them open;
2. the stated 0.8-mm clamp slide cannot extract the T-hooks;
3. the separate flat guard lacks the face-screw relief cut into only the cartridge envelope;
4. the three claimed hard-stop lands and protected-cartridge caddy load path are not modeled;
5. the three strain clips are geometrically floating in the cable notches and have no modeled
   screws/nuts;
6. four separate support posts touch the bracket but have no modeled attachment hardware.

These are resolvable without restoring the expensive fixed ceramic seats.  Stage 50D shall keep
the folded flat-part architecture and correct the complete assembly.

## 2. Independent recalculations

### 2.1 Exported STEP bounds

The accepted STEP was opened independently with OpenCascade rather than trusting the generator
report:

| result | independent value |
|---|---:|
| reimported solids | 20 |
| x bounds | -10.150 / +10.450 mm |
| y bounds | -10.150 / +10.450 mm |
| z bounds | 0.000 / 26.250 mm |
| conservative radius | 14.778532 mm |
| radial margin | 1.096468 mm |
| height margin | 1.250000 mm |

The Stage-30D nominal values are correct for the modeled contents.  They do not prove a complete
installed envelope because attachment and strain hardware are missing.

### 2.2 Hook insertion contradiction

Stage-30D constants are:

- face half-width `6.80 mm`;
- hook-slot center `5.80 mm` from face center;
- slot dimension toward the edge `0.90 mm`, half-length `0.45 mm`.

Therefore the slot ends at `5.80 + 0.45 = 6.25 mm`, leaving `6.80 - 6.25 = 0.55 mm` of sheet.
It is a closed slot.  The rear T-lip is 1.30 mm wide while the stem slot is only 0.95 mm wide, so
the lip cannot pass normal through the slot.  To exit through an actually open edge, the stem
center must move from 5.80 mm to beyond `6.80 + 0.30 = 7.10 mm`, requiring at least 1.30 mm
nominal motion.  Stage-30D's 0.8 mm is insufficient.  Stage 50D shall model a true open U-slot and
use **1.4 mm minimum nominal slide** pending a tool/service coupon.

### 2.3 Guard/screw contradiction

The flat guard half-width is `10.90/2 = 5.45 mm`.  The face screw center is 5.50 mm from center and
the shaft radius is 0.50 mm.  Without a relief, the shaft intrudes `5.45 - (5.50 - 0.50) = 0.45
mm` into the guard outline.  The cartridge envelope has a circular relief, but `make_guard()` and
the exported guard STL do not.  Thus the physical collision pass omits the separate manufactured
guard.  Stage 50D shall add the same open screw relief to a single identical guard geometry and
prove its remaining edge strength.

### 2.4 Lowest central hardware

The Z face plane is the base top at 12.70 mm.  Its nut spans local offsets -1.20 to -0.50 mm, so
the actual modeled nut bottom is `12.70 - 1.20 = 11.50 mm`, not 11.00 mm.  Stage-30D used
`12.20 - 0.50 - 0.70 = 11.00 mm`, a conservative but datum-inconsistent expression.  Correct
provisional clearance over the 10.410-mm keepout is 1.090 mm.  The exact mated datum remains open.

## 3. Findings

### BLOCKER findings

#### F40D-B01 — closed hook slots make the stated service motion impossible

- Affected: Stage-30D CAD, report Sections 8/12, selected drawing, dimension row D30D-023/037.
- Evidence/calculation: Section 2.2; 0.55 mm of sheet closes each slot and the 1.30-mm T-lip is
  wider than the 0.95-mm stem slot.  Required slide is at least 1.30 mm, not 0.8 mm.
- Required correction: final CAD shall cut each hook slot through the outside face edge, retain a
  narrower 0.95-mm stem path and a rear 1.30-mm lip, and change service slide to 1.4 mm nominal.
- Closure test: exported final STEP shows open U-slots; a clamp can be inserted/removed in a
  kinematic simulation and physical coupon without bending the hook plastically or removing a
  neighbour.

#### F40D-B02 — flat guard collides with the face screw in the released geometry set

- Affected: `30D_GUARD_NFF.stl`, guard drawing/process description and collision claim.
- Evidence/calculation: Section 2.3; the guard has no screw relief although the conceptual
  cartridge envelope does.  The omitted intrusion is 0.45 mm.
- Required correction: one identical flat-guard geometry shall include both the pigtail edge notch
  and an open screw-edge relief.  Each X/Y/Z cartridge shall use rotations only—not a mirrored
  second part—to align the same geometry.
- Closure test: guard solids are included explicitly in final collision checks; screw/guard
  distance is positive through tolerance; all three guards have the same geometry hash/volume.

#### F40D-B03 — claimed three-point load path and rear cartridge datum are not modeled

- Affected: report load path, CAD cartridge contact and selected section drawing.
- Evidence/calculation: the cartridge begins at face offset zero and contacts the full bracket
  ring.  No three coined lands exist.  The ceramic guard is modeled at the cartridge front, so it
  cannot simultaneously be the rear datum that contacts the bracket.
- Required correction: define the protected reusable cartridge as a formed CP-Ti perimeter
  caddy/shoe mechanically capturing the flat ceramic guard, LCC/fanout and pigtail.  The clamp and
  bracket shall contact caddy flanges/rear datum pads only.  Model three integral 0.05-mm nominal
  coined lands per structural face and offset the caddy to them.  No load may cross ceramic guard,
  LCC, bonds or electrical joints.
- Closure test: final CAD has nine explicit land envelopes, three caddy envelopes and zero full
  face contact; land-to-caddy distances are zero; all forbidden load-path parts have positive
  clearance from clamp/reaction features.

#### F40D-B04 — strain-relief parts are incomplete and floating

- Affected: CAD physical envelope, fastener schedule D30D-SR01_to_SR03 and envelope acceptance.
- Evidence/calculation: the three clip boxes sit entirely over 4.20-mm base notches and only touch
  z = 12.70 mm where bracket material has been removed.  No clip hole, screw, nut, support lug or
  ceramic comb is modeled.
- Required correction: move each strain fastener to an adjacent solid base lug; model clip,
  through screw and open nut plate; retain the cable contact as a keepout/qualification envelope.
- Closure test: all three clip reactions contact bracket material; all screws/nuts are inside the
  hard envelope and clear the feedthrough/cables; no pigtail force reaches fanout/bonds.

#### F40D-B05 — separate posts have no modeled bracket attachment hardware

- Affected: complete installed envelope and support load path.
- Evidence/calculation: four vented posts only touch the bracket arms at zero distance; the
  schedule calls for attachment hardware but STEP contains none.
- Required correction: add four top through fasteners/head envelopes and bracket/post holes to the
  final assembly.  Keep the exact lower feedthrough interface gated.
- Closure test: final STEP includes every top attachment solid, has no unintended overlap, and
  preserves post/bracket reaction and feedthrough keepout margins.

#### F40D-B06 — one-screw/two-hook clamp is not structurally released

- Affected: D1 selection, clamp displacement, ceramic protection and reuse.
- Evidence/calculation: no clamp FEA, formed-coupon force, hook-root stress, sheet-slot bearing,
  ceramic/caddy contact pressure or torsion result exists.  A single eccentric screw can rotate
  the ring unless the two hooks and three lands provide controlled reaction.
- Required correction: final architecture shall show two hook reactions, one screw reaction and
  three caddy/land force pads; specify a two-screw-per-face fallback if any coupon/FEA/hot-cycle
  criterion fails.
- Closure test: same-process 20/250-deg-C FEA and coupons pass force, stress, slip, vibration,
  retained height, particle and service-cycle limits from the signed envelope.

#### F40D-B07 — flat-guard material and cartridge capture are not qualified

- Affected: reuse, bond protection and cost selection.
- Evidence/calculation: S056-S058 prove commercial process capability only.  No exact alumina lot,
  laser edge flaw, UHV cleaning, clamp/contact strength, guard-to-caddy capture or continuous-life
  evidence exists.  The original project preference was zirconia toughness.
- Required correction: final recommendation shall be geometry-controlled and material-neutral:
  quote 99.6-percent alumina and flat ZTA/zirconia to the same drawing; choose only after edge,
  cleaning, magnetic and hot-UHV coupons.  The caddy must mechanically capture the guard without
  adhesive.
- Closure test: drawing-specific vendor DFM/quotes and first articles pass dimensional, edge,
  cleanliness, flexural/contact and hot-vacuum tests; handling jig protects the complete cartridge.

#### F40D-B08 — formed-sheet accuracy and magnetic stability are unqualified

- Affected: user's accuracy/performance priority and three-axis calibration.
- Evidence/calculation: a static 3x3 matrix can correct fixed nonorthogonality but not bend/land,
  caddy seating or conductive-Ti perturbation that changes with temperature/service.  No signed
  angular/magnetic budget exists.
- Required correction: keep bends out of the claimed accuracy chain; measure nine lands and three
  active planes; calibrate the full 3x3 matrix at 20/250 deg C; repeat after bake, hot cycles and
  each cartridge service; field-map the complete delivered head.
- Closure test: matrix and magnetic-error change remain inside the signed budget across required
  life and service cycles.  Until then: `HOLD - PERFORMANCE CLAIM`.

### MAJOR findings

#### F40D-M01 — lowest-hardware datum expression is inconsistent

- Evidence: Section 2.4; actual modeled Z nut bottom 11.50 mm versus reported 11.00 mm.
- Correction: final dimension ledger shall use the actual plane chain and preserve the exact mated
  datum gate.
- Closure: final report, ledger and CAD report agree on one value.

#### F40D-M02 — identical guard orientation is not controlled end-to-end

- Evidence: X/Z screws use negative local-Y while Y uses positive local-Y; the one-edge pigtail
  notch is held fixed in local coordinates.  Adding the missing screw relief could create mirrored
  variants if the cartridge coordinate system is not frozen.
- Correction: final CAD shall use one reference guard with pigtail notch at local -X and screw
  relief at local -Y.  X/Y/Z face frames may rotate that part but may not mirror it.  Link local
  guard axes to LCC chamfer and the existing orientation-parametric traveler.
- Closure: identical guard geometry hashes/volumes and a drawing orientation table for X/Y/Z.

#### F40D-M03 — captive nut lance is asserted but absent

- Evidence: nut solids exist, but no formed pocket/lance or keeper envelope prevents dropout.
- Correction: final CAD/drawing shall include a positive open no-drop lance/pocket envelope that
  carries no screw clamp load.
- Closure: inverted/no-screw shake and service tests retain each nut without blocking replacement;
  pump-down/particle audit passes.

#### F40D-M04 — folded bracket is not a released developable sheet part

- Evidence: the kernel bracket uses overlapping sharp-corner boxes.  Bend radius, relief, neutral
  axis and flat pattern are absent.
- Correction: retain the model as NFF architecture, add bend/relief keepouts and require a vendor
  flat-pattern/redline before production CAD.
- Closure: vendor-signed flat pattern reimports to the released formed bounds and passes GD&T.

#### F40D-M05 — cost proxies omit added cartridge and attachment details

- Evidence: 21-to-9 is explicitly a face-retention basis; it excludes three cartridge caddies,
  strain hardware and post fasteners.  Volume is not process cost.
- Correction: final cost table shall keep the 21-to-9 statement narrowly labeled, add caddy and
  complete hardware quote lines, and make no dollar/percentage claim without live quotes.
- Closure: drawing-identical 1/3/10 quotes report NRE, accepted recurring parts, assembly,
  inspection, yield/scrap, spares and qualification separately.

#### F40D-M06 — installed collision check is not a service tool sweep

- Evidence: driver axes are stated, but no driver-body, finger/jig, 1.4-mm slide or cartridge
  withdrawal swept volume is modeled.
- Correction: add service keepout envelopes for +X/+Y/+Z driver, hook slide and normal withdrawal.
- Closure: chamber mockup with neighbours/harness installed completes X/Y/Z service without touch.

#### F40D-M07 — cable boxes do not validate bends or strain hardware

- Evidence: 3.80-mm vertical boxes prove width/path only; they do not model delivered lay,
  minimum bend, screen clamp, comb, pigtail exit or clip compression.
- Correction: retain corridor as a sizing rule, add selected cable/lay/strain geometry after
  delivered measurement, and regenerate the final sweep.
- Closure: hot-vacuum installation/proof-load trial passes with continuity/isolation and no bond
  motion.

#### F40D-M08 — ceramic edge and contact flaw tolerance are unknown

- Evidence: 0.635-mm thickness and +/-0.05-mm laser capability are representative values, not
  allowable edge flaw/contact stress for a windowed guard.
- Correction: vendor controls radii, chip/HAZ, edge treatment and inspection; proof/contact coupons
  use the same material lot and process.
- Closure: accepted first articles and coupons meet signed proof/load/life/cleanliness limits.

#### F40D-M09 — STL “faces=1” is only a nonempty check

- Evidence: OpenCascade imports the triangulated compound as one mesh face/shell; this does not
  verify three guard instances or triangle integrity.
- Correction: final validator shall inspect binary STL triangle count and use STEP solid count plus
  per-guard volume/hash for identity.
- Closure: triangle count positive and stable; STEP has expected solids; three guard volumes match.

### MINOR findings

#### F40D-m01 — cost ledger rounds final support volume

`30D_COST_DOWN_RFQ_BASIS_1_3_10.csv` states 324.6 mm3 while the kernel report states 324.651 mm3.
Final artifacts shall use 324.651 mm3 or label a one-decimal rounded value consistently.

#### F40D-m02 — selected top drawing radial arrow is schematic

The horizontal arrow labeled R = 14.779 mm is not drawn to the bounding-box corner that generates
the conservative radius.  Final drawing shall label it “conservative bbox radius” and show the
corner calculation.

#### F40D-m03 — section drawing assigns load to the guard

The selected section says “guard hard stops.”  Corrected load path shall say caddy flange/rear pads;
the ceramic guard and LCC are protected contents, not clamp reaction parts.

### NOTE/PASS findings

#### F40D-N01 — modeled nominal envelope is valid

Independent STEP reimport matches the Stage-30D nominal radius and height.  No correction to those
historical results is required; final geometry must be recalculated after additions.

#### F40D-N02 — zero ceramic threads is preserved

The fastener schedule has ceramic-thread count zero in every row.  No insert or bonded structural
fastener is introduced.

#### F40D-N03 — primary-source limitations are honestly stated

S056-S058 are used as process capability, not life or price qualification.  No unsupported vendor
price is stated.

#### F40D-N04 — electrical and orientation maps are not silently changed

Stage-30D does not replace the q-to-pad, 14<->18, V1-V19 or J1 mapping.  The physical p1-p4 map
remains parametric pending microscope sign-off.

#### F40D-N05 — cost/reuse/connection are scored only after hard gates

D3 is rejected rather than rewarded for low apparent cost, and corrected A remains a comparison.
The priority ordering remains compliant.

## 4. Required Stage-50D correction set

Stage 50D shall generate a complete corrected package rather than merely cite these findings:

1. true open U-hook slots and 1.4-mm nominal slide;
2. one identical flat guard with pigtail notch plus screw-edge relief;
3. a protected cartridge-caddy envelope that carries clamp and datum loads around the LCC/guard;
4. nine modeled coined lands and three caddy-to-land three-point reactions;
5. three complete strain clips, adjacent solid lugs, screws and open nut plates;
6. four modeled top post fasteners;
7. positive no-drop nut-lance/pocket envelopes;
8. corrected 11.50-mm provisional lowest central hardware and recalculated complete bounds;
9. service driver/slide/withdrawal keepouts;
10. a full cost table including caddies and complete hardware, with no inferred dollar saving;
11. material-neutral flat-guard release language and alumina/ZTA/zirconia parallel RFQs;
12. explicit one-screw validation gate and two-screw fallback;
13. measured-land/full 3x3 hot calibration and complete-head field-map gate.

## 5. Review disposition

The design direction **survives** red team because every identified geometry contradiction can be
corrected with flat ceramic and flat/formed Ti parts; none requires restoring a costly monolithic
or fixed-seat ceramic structure.

However, Stage-30D CAD cannot be issued for fabrication.  Stage 50D must create a corrected complete
assembly and repeat envelope/collision/drawing/table validation.  The final project shall remain
`COMPLETE_WITH_OPEN_GATES` because material, clamp, service, feedthrough, magnetic and hot-life
evidence are external release gates.
