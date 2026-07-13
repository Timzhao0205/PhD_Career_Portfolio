# Stage 30D — cost-down flat-part package for 250 deg C UHV

**Status:** controlling Stage-30 mechanical revision; **`NOT FOR FABRICATION`**.  This addendum
supersedes corrected Concept A only for the physical head.  Accepted wire-bond, cartridge,
feedthrough-map and ambient-electronics decisions remain unchanged.

## 1. Direct answer

Yes.  The package can be simplified without making any bonded sensor/LCC disposable:

1. **Delete the three fixed zirconia seat plates.**
2. Replace the machined CP-Ti cage/backframes with **one laser-cut CP-Ti sheet blank having two
   main 90-degree bends**, plus four simple vented posts.
3. Retain each bonded die/LCC/fanout/pigtail as the same protected removable cartridge, but make
   its protective ceramic a **single identical flat 10.90 x 10.90 x 0.635 mm guard** cut from
   stock substrate.  The guard travels with the cartridge; it is not part of the disposable head.
4. Replace two face screws, two nut plates and two keepers per axis with **one face screw, one
   captive nut plate and two integral open-edge hooks** per clamp.

The kernel-checked concept fits at **radius 14.779 mm** and **height 26.250 mm**, leaving **1.096
mm radial margin** and **1.250 mm height margin** inside the required diameter 31.75 mm by height
27.5 mm cylinder.  The model has zero unintended part overlap and all three 3.80-mm cable
corridors clear the folded bracket.

The high-value reusable unit remains:

`bonded die + LCC02046 + orientation-controlled fanout + flat guard + permanent pigtail`.

Removing the head clamp never loads the bond wires, castellation transitions, fanout lanes,
pigtail conductor or remote disconnect.

**`HOLD - DO NOT FABRICATE/ORDER`** remains in force until Sections 13 and 14 close.

## 2. What became cheaper and what did not change

| Controlled item | Corrected A | Cost-down D1 | Change |
|---|---:|---:|---|
| fixed structural ceramic seats | 3 | **0** | all fixed ceramic CNC seat work removed |
| custom ceramic geometries | one seat geometry plus cartridge protection | **one repeated flat cartridge-guard geometry** | no structural ceramic geometry |
| ceramic part process | zirconia flat seat with through window/notch and post-fire DFM | stock-substrate through-cut guard only | no pocket, step, blind feature, insert or thread |
| structural cage | connected machined CP-Ti cage/backframe/reaction structure | one flat blank, two main bends, four simple posts | complex cage machining removed |
| face retention parts | 3 clamps + 6 screws + 6 nuts + 6 keepers = 21 | 3 hook clamps + 3 screws + 3 captive nuts = **9** | 12 parts removed on this basis |
| other sensors removed to service one axis | 0 | **0** | independent reuse preserved |
| ceramic thread count | 0 | **0** | hard rule preserved |
| cable branches | 3 independent 3.80-mm corridors | **unchanged** | no wiring/short-risk regression accepted |

The real-kernel support-frame material proxy falls from 440.917 mm3 for the previous connected
cage including posts to about 324.6 mm3 for the folded bracket plus four posts, about 26 percent.
That is a geometry comparison, **not a price estimate**.  Vendor process, setup, inspection and
yield determine accepted cost.

## 3. Evidence classes and controlling limitations

- **VERIFIED FACT** — authoritative project input or primary source.
- **VERIFIED CALCULATION** — reproduced arithmetic or real-kernel result.
- **ENGINEERING PROPOSAL - VALIDATE** — a dimension, material or process direction that still
  requires objective evidence.
- **HOLD - DO NOT FABRICATE/ORDER** — insufficient release evidence.

Manufacturer evidence supports the process direction, not this part's qualification:

- Kyocera states that CAD-driven ceramic laser processing supports small-lot production without a
  mold and explicitly identifies mold-cost and lead-time reduction; it lists alumina grades through
  99.6 percent and representative processing rules for material up to 1.0 mm thick
  ([S056](https://global.kyocera.com/prdct/fc/technologies/020.html)).
- Kyocera lists 99.6-percent alumina polished substrate at standard thicknesses 0.25, 0.38 and
  **0.635 mm**, with a representative +/-0.02-mm thickness tolerance below 3 inches square
  ([S057](https://global.kyocera.com/prdct/fc/industries/products/069.html)).
- CeramTec lists stamping, laser cutting, dry pressing and hard machining, and describes laser-cut
  alumina external contours and through features as tooling-free and suitable for prototypes and
  small or large volumes ([S058](https://www.ceramtec-industrial.com/en/products-applications/substrates/manufacturing-and-processing)).
- TIMET's Grade-4-equivalent CP Ti is identified as nonmagnetic, moderately formable and typically
  used continuously to 425 deg C; that supports material candidacy, not the finished UHV flexure or
  cleaning state ([S051](https://www.timet.com/assets/local/documents/datasheets/cpgrades/75a.pdf)).

No source proves that the proposed guard, bend, clamp or nut-lance stack survives the user's exact
continuous-life UHV environment.  Those remain qualification gates.

## 4. Hard gates retained

The redesign does not relax any project requirement:

- all in-vessel parts continuously operate at 250 deg C in UHV;
- three mutually orthogonal, electrically isolated, four-terminal Hall sensors remain installed;
- all physical parts, clamps, heads, posts, strain clips and cable keepouts remain inside diameter
  31.75 mm by height 27.5 mm;
- the bonded sensor/LCC cartridges remain independently removable, reusable and guarded;
- no adhesive is added to the reusable structural head;
- no ceramic receives a tapped/internal thread or bonded insert;
- no PEEK, BeCu, nickel or steel assumption enters the baseline;
- all fasteners and nut plates are external/open and replaceable;
- no retention load passes through an electrical joint;
- p1-p4 orientation remains parametric and requires the existing microscope/traveler sign-off.

## 5. Online geometry inspiration — and what was deliberately not copied

Two online examples helped separate useful architecture from the cost driver:

1. [EPO EP1642365B1](https://data.epo.org/publication-server/rest/v1.2/patents/EP1642365NWB1/document.pdf)
   shows orthogonal ceramic faces accepting individually packaged LCC sensors and explicitly notes
   individual sensor rework.  That supports the reusable-LCC idea, but its recessed monolithic
   ceramic body is exactly the machining/NRE direction now rejected.
2. [SENIS's prismatic three-axis probe](https://www.senis.swiss/wp-content/uploads/2023/03/3-Axis-Prismatic-Hall-Probe-for-K3A-Cryogenic-Magnetic-Field-Transducers_rev.1.0.pdf)
   packages three discrete Hall sensors in a compact printed alumina body with a remote cable.
   This supports compact orthogonal sensing and remote electronics as an inspiration only.  It is
   a different cryogenic product and does not prove 250 deg C UHV, independent LCC removal or the
   no-adhesive HSX service boundary.

The selected design takes the orthogonal/removable idea but moves precision and protection into
three flat cartridges plus calibration, not a complex ceramic cube.

## 6. Cost-down concepts

### D1 — selected: one folded trihedral bracket

- One laser-cut CP-Ti blank forms the +Z base and +X/+Y faces with two main 90-degree bends.
- Windows, post holes, cable notches, screw clearances and hook slots are all cut while flat.
- Three identical protected cartridges land on three coined/formed hard-stop sets.
- Each face uses one windowed clamp strap, two integral T-hooks and one screw/captive nut plate.
- Four simple vented posts retain the existing feedthrough-datum architecture.

Strengths: no fixed ceramic, minimum custom geometry, no weld in the structural corner, lowest
face hardware count, straight +X/+Y/+Z service, and local cartridge scrap rather than whole-head
scrap.

Limitations: bend springback cannot be treated as calibrated orthogonality; coined lands, hook
strength, flexure force, nut-lance capture and hot-cycle matrix stability need proof.

### D2 — runner-up: three identical bent face modules

- Three identical single-bend Ti face modules bolt to a simple planar base.
- The cartridge, guard and one-screw/two-hook clamp are identical to D1.
- Each face module can be replaced without replacing the base.

Strengths: simpler individual bends, identical parts, easier first-article inspection.

Why not selected: six to nine additional Ti joints/fasteners, more virtual-leak and particle sites,
more datum stack and a higher chance that service changes the calibration matrix.

**Reversal trigger:** choose D2 if two sheet-metal vendors show materially lower accepted 1/3/10
cost than D1 and a hot-cycle/service trial proves equal axis-matrix stability.

### D3 — rejected: direct metal clip with commercial insulating buttons

- A formed Ti clip would grip the LCC directly using commercial ceramic stand-offs and omit the
  custom flat guard.

Hard-gate failures: exact LCC rear/edge metallization clearance is not established; conductive Ti
would sit closer to the active sensor; bond-wire protection is weaker; service handling directly
exposes the brittle LCC.  D3 is not scored.

### Corrected A — superseded for cost

Corrected A remains a valid fit/reuse comparison, but its three fixed zirconia seats, six face
screws, six nut plates and six keepers no longer win the user's cost requirement.

## 7. Hard-gate filter and weighted decision

Cost is scored only after UHV/temperature, material, envelope, isolation, protection and service
gates.

| Concept | hard gates | cost /30 | reuse risk /25 | connection/service /25 | thermal/calibration /10 | access /10 | total |
|---|---|---:|---:|---:|---:|---:|---:|
| D1 folded trihedral | PASS conditional | 28 | 24 | 23 | 8 | 9 | **92** |
| D2 repeated face modules | PASS conditional | 25 | 24 | 22 | 7 | 8 | 86 |
| corrected A fixed zirconia seats | PASS conditional but cost superseded | 20 | 24 | 23 | 9 | 8 | 84 |
| D3 direct metal clip | **FAIL** | — | — | — | — | — | not scored |

Scores are an engineering proposal, not a purchase release.  D1 becomes the procurement baseline;
the decision must be rechecked using drawing-identical live quotes.

## 8. Selected D1 construction

### 8.1 Structural blank

**ENGINEERING PROPOSAL - VALIDATE:** 0.50-mm CP-Ti Grade 4 blank:

- central face: 13.60 x 13.60 mm;
- +X and +Y faces: 13.60 x 13.60 mm after bending;
- central active windows: 6.40 x 6.40 mm with vendor-controlled radii;
- three 4.20-mm nominal open base notches around the 3.80-mm cable keepouts;
- four diagonal planar arms to x/y = +/-9.00-mm vented posts;
- one face-screw clearance and two open-edge hook slots per face;
- no blind pocket, hidden nut, bonded insert or weld in the trihedral blank.

The two bends only place the faces near orthogonal.  Three coined/embossed hard-stop lands on each
face define the cartridge plane.  Exact bend relief, neutral axis, minimum bend radius, coining,
flatness and stress relief remain G30D-03.

### 8.2 Reusable flat guard

**ENGINEERING PROPOSAL - VALIDATE:** three identical 99.6-percent alumina guards:

- 10.90 x 10.90 x 0.635 mm;
- 6.40-mm through window;
- one open 1.60 x 2.20-mm pigtail/tongue notch at the negative local-X edge;
- radiused internal corners and vendor-controlled laser edge/heat-affected condition;
- no pocket, step, blind feature, metalization, insert, thread or adhesive.

The 0.635-mm stock thickness and laser route are commercially credible from S056-S058.  The
specific alumina grade is not yet approved for this stack.  Spectrum must confirm LCC02046 ceramic
and dimensional data, and the guard vendor must qualify cleanliness, edge flaws and lot trace.

If alumina fails UHV/edge/field qualification, keep the same flat geometry and quote laser-cut
alumina-zirconia/ZTA or flat zirconia.  Do not return to a monolithic or pocketed 3-D ceramic body.

### 8.3 Face retention

Each face uses:

- one 13.40-mm windowed CP-Ti clamp strap;
- two integral T-hooks separated by 4.60 mm;
- one externally driven proposed miniature Ti screw;
- one open captive vented Ti nut plate;
- an integral bracket retaining lance that prevents the nut from dropping but carries no clamp
  load.

The nominal screw center is 5.50 mm from the face center.  With a 6.80-mm face half-width and
0.70-mm clearance radius, nominal edge ligament is 0.60 mm.  The open hook-slot ligament is 0.55
mm.  These are dimensional facts, **not strength allowables**.  G30D-04 must prove hook, slot,
clamp and sheet stresses with FEA and same-process coupons.

Primary load path:

`screw head + two hook lips -> compliant clamp -> ceramic-guard perimeter/hard stops -> coined Ti
lands -> folded Ti face/base -> four posts -> exact feedthrough datum`.

Forbidden load path:

`die / bond wire / LCC metallization / fanout / weld-crimp terminal / pigtail / disconnect`.

## 9. Envelope, collision and keepout results

All values below are real OpenCascade results or stated calculations from
`cad/30D_cost_down_flat_package.py`:

| quantity | result | evidence class |
|---|---:|---|
| hard radius / height | 15.875 / 27.500 mm | verified requirement |
| physical conservative radius | **14.779 mm** | verified calculation |
| nominal radial margin | **1.096 mm** | verified calculation |
| physical installed height | **26.250 mm** | verified calculation |
| nominal height margin | **1.250 mm** | verified calculation |
| proposed worst radius / remaining margin | 15.099 / 0.776 mm | engineering proposal - validate |
| proposed worst height / remaining margin | 26.630 / 0.870 mm | engineering proposal - validate |
| physical collision envelopes | 20 | verified calculation; not procurement BOM |
| maximum unintended overlap | 0.000000 mm3 | verified calculation |
| STEP reimport bound change | 0.000000 mm | verified calculation |
| cable-to-bracket overlap | 0.000000 mm3 | verified calculation |
| nut-to-bracket reaction distances | three at 0.000000 mm | verified calculation |
| post-to-bracket reaction distances | four at 0.000000 mm | verified calculation |

The proposed tolerance stacks are deliberately conservative linear allowances, not vendor
capability.  Production CAD must be regenerated from the vendor-signed flat pattern, bend model,
cartridge measurement, feedthrough datum and delivered fasteners.

## 10. Thermal, preload and measurement performance

### 10.1 Thermal displacement

Using representative CP-Ti 20-300-deg-C CTE 9.5e-6/K from S051 and representative 99.6-percent
alumina CTE 7.2e-6/K from S056:

- lateral over 10.90 mm and Delta-T = 230 K:
  `(9.5-7.2)e-6/K * 10.90 mm * 230 K = 0.005766 mm`;
- normal over the 2.40-mm cartridge envelope:
  `(9.5-7.2)e-6/K * 2.40 mm * 230 K = 0.001270 mm`.

The Ti face grows slightly more than the alumina guard under those representative values, so the
edge clearance tends to increase.  The normal result is not a force margin.  Actual LCC, guard,
Ti lot and formed-clamp data plus contact geometry control the hot force.

### 10.2 Preload

**ENGINEERING PROPOSAL - VALIDATE:** target 0.15-mm elastic clamp displacement at 20 deg C, with a
0.10-0.22-mm development window and hard stops preventing load transfer into the LCC cavity.

Release needs:

- flexure FEA at 20 and 250 deg C with tolerance extrema;
- ceramic contact-pressure/chip check at three hard stops;
- Ti elastic range, stress relief, free-height and force coupons;
- hot dwell/cycle retained-force measurement;
- one-screw torsion and vibration test;
- hook-root crack/particle and nut-lance dropout inspection.

No catalog bend property or 425-deg-C material use temperature qualifies retained clamp force.

### 10.3 Accuracy/performance protection

The cost reduction must not be bought by silently assuming perfect sheet-metal orthogonality.

- The two bends are manufacturing geometry, not the final vector calibration.
- Measure the three active Hall planes and cartridge seating repeatability after assembly.
- Calibrate the full 3 x 3 sensitivity/axis matrix at 20 and 250 deg C.
- Repeat the matrix after bake, hot cycling and one independent cartridge remove/reinstall cycle.
- Store the matrix with the serialized head/cartridge configuration.
- Reject the design if matrix drift or repeatability exceeds the user-signed error budget.

The numerical angular/magnetic error budget is not yet supplied, so performance remains
**`HOLD - PERFORMANCE CLAIM`** under G30D-07/G50-07.  CP Ti is nonmagnetic per S051, but it is
conductive; the large windows reduce nearby metal but do not replace complete-head field mapping.

## 11. Bond-wire, connection and harness protection

The accepted Stage-10 connection architecture is unchanged:

- orientation-parametric q1/q2/q3/q4 to pads 8/3/19/14;
- the fourth external route remains the resolved 14<->18 unordered connection until traveler
  direction is fixed;
- same-number castellation microtransitions to the protected fanout;
- supported welded/crimped robust terminals to the permanent four-line pigtail;
- remote keyed four-circuit disconnect for service;
- separate ceramic comb/CP-Ti branch strain relief.

The flat guard window and pigtail notch are conceptual envelopes.  G30D-02 must supply:

- actual LCC lot dimensions and metallization keepout;
- microscope survey of maximum die, wire-loop, heel and fanout height;
- minimum 0.30-mm guard clearance above the measured loop through tolerance;
- service sweep showing the guard, clamp and handling jig cannot contact a bond;
- proof that the pigtail exit bend does not rotate the LCC or load a lane;
- continuity/isolation proof before and after hot service.

Three independent 3.80 x 3.80-mm square cable corridors remain.  Two delivered 1.650-mm worst-case
pair ODs occupy 3.300 mm side-by-side, leaving 0.500 mm total width allowance.  Cable lay, bend,
screen clamp and the provisional 5x-OD = 8.25-mm bend rule remain G30D-06.

## 12. Independent one-axis service

For X, Y or Z independently:

1. make the system safe and record terminal identity, continuity and isolation;
2. support only the selected serialized cartridge in its handling jig;
3. release only that branch's strain hardware and keyed remote four-circuit pigtail connection;
4. remove the single external face screw along +X, +Y or +Z;
5. slide the clamp approximately 0.8 mm toward its open hook edge and lift it normal to the face;
6. withdraw the guarded cartridge normal to its face; the other two cartridges remain installed;
7. inspect guard edges, hook roots, nut lance, hard-stop witness, particles, loop witness, fanout,
   pigtail and comb;
8. seat the replacement against the three hard stops, reinstall the qualified clamp/screw and
   remate only its keyed pigtail/strain hardware;
9. repeat terminal identity, all-pairs/chassis isolation, injected-polarity and full vector-matrix
   checks.

The kernel geometry provides noncrossing +X/+Y/+Z driver axes and zero neighbour removal.  A
gloved chamber-tool mockup and hot service-cycle test remain G30D-07.

## 13. Fabrication and inspection plan

### 13.1 Ceramic guard RFQ

Quote the same released 2-D drawing from at least two substrate vendors:

- material candidates separately: 99.6-percent alumina; flat alumina-zirconia/ZTA fallback;
- quantities 3, 9 and 30 accepted pieces for 1, 3 and 10 heads;
- NRE/tooling/programming separately from recurring piece price;
- substrate lot, thickness, flatness, window/notch/edge tolerance and radii;
- laser method, heat-affected/chip limits, edge treatment and cleaning;
- dimensional/visual sampling, yield/scrap and witness coupons;
- UHV cleaning/packaging and material-lot documentation;
- first-article and replacement/spare price.

No lapping, grinding or polishing should be specified unless the vendor proves it is necessary.
The design goal is through-cut stock substrate, not post-fire CNC geometry.

### 13.2 Ti sheet-metal RFQ

Quote:

- one bracket at quantities 1, 3 and 10;
- three hook clamps at quantities 3, 9 and 30;
- flat-pattern laser/waterjet/photochemical process, deburr and cleaning;
- two main bracket bends, bend-relief and springback control;
- nine coined datum lands and their plane/height inspection;
- hook/slot and face-screw ligament inspection;
- stress relief, lot trace and nonmagnetic screen;
- open captive-nut lance development and particle/drop test;
- first-article CMM/optical metrology and hot-cycle witnesses.

### 13.3 Accepted cost comparison

Use `30D_COST_DOWN_RFQ_BASIS_1_3_10.csv` and compare:

`accepted cost/head = NRE/Q + accepted recurring parts + assembly labor + inspection + expected
yield/scrap + service spares`.

Report chamber/qualification/calibration cost separately.  Do not hide a different qualification
scope inside one concept's piece price, and do not infer a dollar-saving percentage from the
26-percent material-volume or 57-percent face-part-count proxies.

## 14. Release gates

| gate | required closure evidence | current state |
|---|---|---|
| G30D-01 flat guard | drawing-specific alumina/ZTA/zirconia DFM; lot properties; laser edge/chip/cleaning limits; first article; hot-UHV witness | **HOLD - DO NOT ORDER** |
| G30D-02 protected cartridge | LCC lot geometry; orientation traveler; loop/fanout/pigtail measurement; guard attachment and sweep; continuity/isolation | **HOLD - DO NOT FABRICATE/BOND** |
| G30D-03 folded bracket | vendor flat pattern, bend radius/relief/springback, coined datum lands, GD&T, stress/cleaning and complete tolerance CAD | **HOLD - DO NOT FABRICATE** |
| G30D-04 clamp and hooks | FEA, same-process flexure/hook coupons, 20/250-deg-C force, vibration and service-cycle proof | **HOLD - DO NOT FABRICATE** |
| G30D-05 nut/hardware | exact Ti screw/nut/lance, venting, galling, torque, retention, particle and no-drop service proof | **HOLD - DO NOT ORDER** |
| G30D-06 interface/harness | exact mated feedthrough datum; cable lot/lay/bend; screen and three independent strain-relief trials | **HOLD - DO NOT FABRICATE** |
| G30D-07 accuracy/service | signed angular/magnetic budget; 20/250-deg-C 3x3 calibration; post-bake/service stability; tool mockup | **HOLD - PERFORMANCE CLAIM** |
| G30D-08 cost decision | comparable drawing-identical 1/3/10 vendor quotes with NRE, inspection, yield and qualification separated | **HOLD - DO NOT ORDER** |

## 15. CAD and drawing package

- generator: `cad/30D_cost_down_flat_package.py`;
- complete assembly: `cad/30D_NFF.step` and `cad/30D_NFF.stl`;
- folded bracket: `cad/30D_BRACKET_NFF.step`;
- repeated guards: `cad/30D_GUARD_NFF.stl`;
- harness keepouts: `cad/30D_KEEP_NFF.step`;
- kernel report: `cad/30D_CAD_KERNEL_REPORT.txt`;
- concept comparison: `drawings/30D_cost_down_concepts.svg`;
- selected envelope/section/service drawing: `drawings/30D_cost_down_selected.svg`;
- rendered CAD visual QA: `drawings/30D_cad_visual_QA.png`;
- calculations: `30D_DIMENSION_AND_COLLISION_LEDGER.csv`;
- hardware: `30D_FASTENER_AND_THREAD_SCHEDULE.csv`;
- cost/RFQ: `30D_COST_DOWN_RFQ_BASIS_1_3_10.csv`.

All CAD and drawings are **NOT FOR FABRICATION**.  The OpenCascade model validates dimensional
architecture, not clamp stress, field error, ceramic flaw tolerance or production GD&T.

## 16. Stage-30D decision

Select **D1, the folded CP-Ti trihedral bracket with three reusable flat-guard cartridges**, as the
new cost-down baseline.

It removes every fixed ceramic seat, eliminates complex ceramic CNC from the structural head,
cuts controlled face-retention parts from 21 to 9, preserves independent cartridge replacement,
and passes the nominal envelope/collision/cable checks.  D2 remains the quote-based runner-up.

The baseline is complete as an RFQ and qualification architecture, not a fabrication release.
Accuracy remains protected by measured datum lands, a full 3x3 vector calibration and mandatory
post-hot-cycle/service stability tests—not by assuming sheet bends are perfect.
