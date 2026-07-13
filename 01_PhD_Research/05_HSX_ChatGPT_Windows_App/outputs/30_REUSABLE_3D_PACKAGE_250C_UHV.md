# Stage 30 — reusable three-axis package for continuous 250 °C UHV

Date: 2026-07-12  
Release state: **CONCEPT COMPLETE; HOLD — DO NOT FABRICATE OR ORDER**  
Selected concept for red team: **Concept A, modular tri-plate cage**

This package uses the protected bonded-LCC cartridge selected in Stage 10, the twelve-conductor
and six-pair harness boundary fixed in Stage 20, and no adhesive or assumed hot LCC socket. All
three Hall dies face the mutually orthogonal `+X`, `+Y`, and `+Z` directions. Each bonded
LCC02046, guard, tongue, and short pigtail is removed as one protected cartridge; the service
disconnect remains downstream of independent strain relief.

The three concepts pass the concept-level hard envelope and critical-body collision checks. They
are **not fabrication-ready** because the exact mated 19C geometry, zirconia vendor rules, bonded
loop envelope, cable stack, CP-Ti flexure life, miniature fastener delivered state, and service
repeatability remain open gates.

## 1. Recommendation and hard-gate result

| Item | Concept A — tri-plate cage | Concept B — monolithic core | Concept C — split cassette |
|---|---:|---:|---:|
| Continuous 250 °C UHV material architecture | PASS CONCEPT / qualification open | PASS CONCEPT / qualification open | PASS CONCEPT / qualification open |
| Near-sensor magnetic rule | CP-Ti + zirconia proposed; exact delivered hardware held | same | same |
| Three electrically isolated orthogonal sensors | PASS; ceramic cartridge datums | PASS; monolithic ceramic faces | PASS; ceramic rear datums |
| Installed `Ø31.75 × 27.5 mm` envelope | `r=14.354`, `h=26.70` nominal | `r=14.354`, `h=27.00` nominal | `r=14.354`, `h=26.55` nominal |
| Worst-case proposed height | 27.11 mm | 27.36 mm | 26.91 mm |
| Unintended modeled solid overlap | 0.000000 mm³ | 0.000000 mm³ | 0.000000 mm³ |
| Zirconia tapped/internal threads | **0** | **0** | **0** |
| Remove one bonded LCC without removing another | PASS CONCEPT | PASS CONCEPT | PASS CONCEPT |
| Bond wires guarded throughout service | PASS CONCEPT | PASS CONCEPT | PASS CONCEPT |
| Fabrication cost/scrap exposure | **lowest** | highest ceramic single-part risk | medium ceramic / higher Ti mechanism |
| Recommended role | **baseline** | orthogonality-driven alternate | frequent-service alternate |

**Decision:** carry Concept A into Stage 40. It best follows the binding order after hard gates:
fabrication cost first, bonded LCC reuse second, and connection quality third. Three identical flat
zirconia seats isolate ceramic scrap to a small replaceable part; the external Ti cage carries all
threads and tools. Concepts B and C are retained because vendor quotation or service testing may
reverse the choice.

## 2. Status vocabulary and evidence boundary

- **VERIFIED FACT** — direct drawing/vendor evidence or a completed kernel/CSV/XML check.
- **CALCULATION** — arithmetic shown here or in the dimension ledger.
- **ENGINEERING PROPOSAL — VALIDATE** — a dimension, stiffness, force, DFM limit, or process to
  be verified by vendor or coupon.
- **HOLD — DO NOT FABRICATE/ORDER** — a missing input can change fit, material, or lifetime.

No catalog maximum, cleanroom delivery claim, bake result, or material continuous-use statement
is promoted to retained-force or full-assembly life qualification.

## 3. Coordinate system, common installed support, and user-CAD disposition

### 3.1 Datum and axes

- `z=0` is the feedthrough/flange mounting datum used by the concept models.
- Sensors are on `+X`, `+Y`, and `+Z`; local face `+n` points outward.
- The conservative unresolved feedthrough keep-out is `r=11.050 mm`, `z=0…10.410 mm`. The
  10.410-mm feature is taken from the official drawing as a conservative model input, not a
  confirmed mated protrusion.
- The connected CP-Ti base frame begins at `z=11.500 mm`; four post centers are
  `(±9.000, ±9.000) mm`, post radius 1.150 mm.
- The minimum nominal post surface radius is
  `sqrt(9²+9²)-1.15 = 11.578 mm`, 0.528 mm outside the modeled keep-out. Proposed worst case is
  11.387 mm, still positive, but the underlying feedthrough geometry remains a hold.

### 3.2 Connected base and installed harness reservations

The common base is CP-Ti, not a threaded ceramic plate. A 15-mm central frame has four connected
L-shaped ears to the posts. Three open edge slots reserve one independent `3.0 × 3.0 mm` branch
corridor per four-terminal sensor:

| Branch | Corridor center `(x,y)` mm | Independent strain-relief axis `(x,y)` mm | Sector |
|---|---:|---:|---|
| Y | `(-6.3,+3.8)` | `(-6.3,+1.6)` | upper `-X` edge |
| X | `(+3.8,-6.3)` | `(+1.6,-6.3)` | right `-Y` edge |
| Z | `(-6.3,-3.8)` | `(-6.3,-6.3)` | lower `-X/-Y` corner |

The routes do not cross and do not enter a hidden groove. Each strain-relief clip has its own
external through-fastener and replaceable Ti nut pad; the clips and fasteners are present in the
kernel envelope. The corridor is only a reserved volume. **HOLD — DO NOT FABRICATE:** actual
KAP301/conductor OD, shield lay, finished bend radius, and proof load must fit it.

### 3.3 Why the supplied historical CAD is not reused as the baseline

**VERIFIED KERNEL OBSERVATION:** the supplied STEP had a `20.375 × 31.75 × 3.0 mm` base with zero
diameter tolerance margin, a `20 × 15 × 15 mm` head, only two sensor plates, and `12 × 12 ×
0.635 mm` carrier stand-ins rather than the `8.89 × 8.89 × about 1.65 mm` LCC02046. Its overall
flange assembly was much larger than the head envelope. The new CAD preserves the useful modular
idea but replaces the dimensions, adds the third axis, includes fastener/head/harness volumes, and
removes PEEK/BeCu/hot-socket assumptions.

## 4. Common protected cartridge and 20/250 °C stack

### 4.1 Mechanical/electrical separation

The cartridge boundary is unchanged from Stage 10:

1. bonded die and LCC02046;
2. orientation-keyed zirconia rear/guard with a measured bond-loop keep-out;
3. four same-numbered castellation microtransitions to the protected one-side tongue;
4. supported welded/crimped transition to a short high-temperature pigtail;
5. independent package strain relief; and
6. a remote, accessible service disconnect.

The clamp bears only on zirconia guard shoulders/hard stops. No force is reacted through an LCC
castellation, bond shelf, wedge bond, fanout lane, weld, crimp, or conductor. Loss of flexure force
cannot release the cartridge: positive screws/pins remain the safety retention. The flexure is an
anti-rattle preload, not the sole retainer.

### 4.2 LCC body pocket

The Spectrum body is `0.350 +0.010/-0.005 in`, or 8.763–9.144 mm. The proposed cartridge pocket is
`9.400 ±0.050 mm`:

- 20 °C diametral clearance: `9.350-9.144 = 0.206 mm` minimum and
  `9.450-8.763 = 0.687 mm` maximum;
- using representative 10.4e-6/K zirconia and 7.2e-6/K alumina CTE over 230 °C, the bounds become
  approximately 0.213–0.695 mm.

This is a clearance sensitivity, not release evidence. **HOLD — DO NOT FABRICATE:** Spectrum must
confirm actual LCC ceramic, thickness/warpage, and purchased-lot body dimensions; the zirconia
vendor must confirm the pocket process.

### 4.3 Cartridge lateral location

For A/B the guard outside width is `10.900 ±0.050 mm`; proposed external Ti locator separation is
`11.150 ±0.050 mm`. Total lateral clearance is 0.150–0.350 mm at 20 °C. Using Ti 9.5e-6/K and
zirconia 10.4e-6/K, it is approximately 0.148–0.348 mm at 250 °C. The hard stop establishes the
normal datum; two orthogonal rails establish lateral position without a tight ceramic pocket.

Concept C uses a `9.800 ±0.050 mm` rear datum and `10.400 ±0.100 mm` Ti rail separation, giving
0.450–0.750 mm total lateral clearance. Pins provide positive retention; compliant rail tabs,
not a tight ceramic slide, remove play.

### 4.4 Proposed anti-rattle preload

The A/B guard shoulder is `2.400 ±0.040 mm`; the formed Ti hard-stop gap is
`2.220 ±0.040 mm`.

At 20 °C:

`δ20 = t_guard - g_Ti = 0.180 mm nominal = 0.100…0.260 mm worst case`.

At 250 °C, using the representative CTE difference:

`Δδ = (10.4-9.5)e-6/K × 2.40 mm × 230 K = +0.00050 mm`, so
`δ250 ≈ 0.1005…0.2605 mm`.

**ENGINEERING PROPOSAL — VALIDATE:** target formed-flexure stiffness is 1–2 N/mm, so the full
arithmetic force range is 0.10–0.52 N per cartridge. If four `1 mm²` hard-stop shoulders share the
maximum force uniformly, average compressive bearing is only 0.13 MPa. That comparison does not
clear edge chips, local contact stress, impact, flexure relaxation, or fired defects.

TIMET identifies Grade-4-equivalent TIMETAL 75A as nonmagnetic, with 9.5e-6/K CTE through 300 °C
and typical continuous use to 425 °C. This supports material candidacy, not formed-spring life.
**HOLD — DO NOT FABRICATE:** measure force/free height at 20 °C, during and after continuous
250 °C vacuum dwell, after thermal cycles, and after service cycles. Reject unqualified PEEK or
BeCu preload elements.

### 4.5 Bond-wire and pigtail keep-outs

- Guard clearance is `measured maximum loop envelope + 0.30 mm minimum`:
  **ENGINEERING PROPOSAL — VALIDATE**.
- The open guard window is 6.40 mm; final dimensions follow the actual LCC cavity and loop survey.
- The tongue/pigtail exits the service side without passing above exposed wire.
- Minimum supported bend radius is proposed as `5 × finished cable OD`; exact OD and vendor cable
  limit are missing, so the route is a hold.
- A cartridge is handled only by guard flats with a dedicated tray/jig. No tool or finger enters
  the loop volume.

## 5. Concept A — modular tri-plate cage (**recommended**)

### 5.1 Structure and dimensions

- CP-Ti trihedral cage virtual span: 10.00 mm, beginning at `z=12.50 mm`.
- Three identical zirconia seats: `9.60 × 9.60 × 1.00 mm`, mounted outward on `+X/+Y/+Z`.
- Central seat opening: 6.40 mm; nominal ring width `(9.60-6.40)/2 = 1.60 mm`.
- One open `2.2 × 2.8 mm` tongue notch per seat; the same flat part is rotated for each face.
- Protected cartridge: `10.90 × 10.90 × 2.40 mm` concept envelope.
- External clamp frame: `15.60 × 15.60 × 0.50 mm`, 7.20-mm open window.
- Six face fasteners are outside all ceramic. X/Y use two positions on their unused negative local
  edge; Z uses the `-X` and `-Y` edges.

The plates project outward from a smaller cage. This gives 0.20 mm nominal plate-to-plate gap,
0.55 mm cartridge-to-cartridge gap, and 0.60 mm clamp-to-clamp gap at adjacent positive faces.
Proposed worst cases remain 0.10, 0.425, and 0.410 mm respectively.

### 5.2 Envelope and tolerance

Kernel result: `x/y=±10.150 mm`, `z=0…26.700 mm`; conservative bounding-box radius
`sqrt(10.15²+10.15²)=14.354 mm`. Nominal radial and height margins are 1.521 and 0.800 mm.

Proposed worst-case height:

`26.700 + 0.10 base datum + 0.05 frame + 0.10 cage + 0.05 seat + 0.04 cartridge + 0.04 clamp + 0.03 head = 27.110 mm`.

This leaves 0.390 mm to the height limit under the proposed stack. The exact mated-feedthrough
datum is still a release gate.

### 5.3 Ceramic DFM and stress mode

- Fixed ceramic geometry count: three identical seats; protected cartridge guard is a second
  common ceramic geometry.
- Minimum nominal window ring is 1.60 mm; worst proposed 1.50 mm.
- No ceramic hole, thread, insert, undercut, blind pocket, or hidden nut.
- Proposed internal radius `R0.75 min`, external radius `R0.50 min`, edge break `0.20 min`.
- Loads are broad face bearing/compression at guard shoulders. The thin seat is not bent by screw
  torque because the screw axes and nut pads are in the Ti cage.
- Final flatness, parallelism, surface finish and allowable green/post-fire process are omitted
  intentionally pending vendor redline.

Identical flat seats can be green/near-net machined or possibly cut/ground from fired stock; the
vendor chooses. Shrink scaling and inspection apply to fired dimensions. No claim is made that a
1.00-mm fired zirconia plate is economical or chip-safe until quoted.

### 5.4 Fastener axes, tools, and assembly collision result

For Concept A face center `cz=17.50 mm`:

| Hardware | Global axis/location | Tool direction | Collision control |
|---|---|---|---|
| X-F1/F2 | `y=-6.50`, `z=15.50/19.50` | straight `+X` | both on unused `-Y` edge |
| Y-F1/F2 | `x=-6.50`, `z=19.50/15.50` | straight `+Y` | both on unused `-X` edge |
| Z-F1 | `x=-6.50,y=0` | straight `+Z` | negative edge; no X cartridge |
| Z-F2 | `x=0,y=-6.50` | straight `+Z` | negative edge; no Y cartridge |

`Ø3.0 mm` driver corridors are reserved as **ENGINEERING PROPOSAL — VALIDATE**. Heads, nut pads,
clips, and modeled projections are inside the installed envelope. OpenCascade pairwise checks of
plates, cartridges, clamps, face hardware, and strain-relief hardware found 0.000000 mm³
unintended overlap.

### 5.5 One-cartridge service/remating sequence

1. De-energize, vent, and cool under the laboratory service procedure; identify axis and record
   pre-service continuity/calibration state.
2. Support only the selected guarded cartridge with its keyed service jig.
3. Open the selected remote four-lane disconnect, then release only that branch strain-relief
   clip. Other branches remain clamped.
4. Remove the two external face screws with straight access; capture/replace their external nut
   pads. Remove the Ti clamp without crossing the guard window.
5. Withdraw the guarded cartridge normal to its face. Do not slide it tangentially or remove any
   other sensor/seat.
6. Inspect loop/guard, LCC body, pigtail strain relief, seat chips, hard stops, screw/nut galling,
   and cartridge dimensions. Quarantine failures.
7. Insert the replacement/reused guarded cartridge normal to the same keyed face. Draw the clamp
   to its Ti hard stops; screw torque is not used to set ceramic preload.
8. Restore branch strain relief and the remote disconnect. Perform four-wire continuity/contact
   resistance, insulation, polarity, noise, axis-sign and full three-axis calibration checks.

No adhesive is broken and no electrical joint is used as a pull handle or retention member.

### 5.6 Part count and cost drivers

The concept CAD contains 38 modeled physical groups excluding three reserved harness volumes and
unresolved lower post attachment detail. The cost-relevant custom items are:

- six fired custom ceramic pieces: three identical fixed seats plus three common cartridge guards;
- one low-complexity CP-Ti base/cage set, four posts, three rear cage rails;
- three repeated clamp frames, six repeated nut pads/face screws;
- three repeated strain-relief clip/nut/screw sets.

Cost advantages are repetition, small flat ceramic scrap, no post-fire orthogonal cube grinding,
no ceramic holes/threads, and replacement of one chipped seat rather than a whole core. Cost
penalties are Ti assembly count, inspection of three bolted seat datums, and mandatory vector
calibration after service.

## 6. Concept B — monolithic zirconia core with external saddle clamps

### 6.1 Structure and dimensions

- One `11.30 mm` zirconia cube/core on the connected CP-Ti base.
- Open-bottom `8.00 × 8.00 mm` cavity; nominal side wall 1.65 mm.
- Each active face has only a shallow `6.80 × 6.80 × 0.60 mm` open relief and a straight harness
  slot; no 9.5-mm pocket and no ceramic fastener hole.
- Same `10.90 × 10.90 × 2.40 mm` protected cartridges and A/B clamp frames.
- An external CP-Ti saddle cage carries all six screws and nut pads outside the core.

The core-to-cartridge adjacent-face gap is 0.200 mm nominal and 0.125 mm proposed worst case. The
clamp-to-clamp gap is 0.250 mm nominal and 0.110 mm proposed worst case. These are positive but
must be preserved in the vendor drawing.

### 6.2 Envelope and tolerance

Kernel result: conservative radius 14.354 mm; `z=0…27.000 mm`. Nominal height margin is 0.500 mm.

Proposed worst-case height:

`27.000 + 0.10 base datum + 0.05 frame + 0.10 core + 0.04 cartridge + 0.04 clamp + 0.03 head = 27.360 mm`.

Only 0.140 mm remains under the proposed stack, so B has the lowest height tolerance margin.

### 6.3 Ceramic DFM and stress mode

- Custom ceramic count: one core plus three common cartridge guards; two ceramic geometries.
- Minimum open-bottom side wall is 1.65 mm nominal, 1.55 mm proposed worst case.
- Face-relief perimeter wall is 2.25 mm nominal, 2.15 mm proposed worst case.
- All inner transitions require vendor-approved `R0.75 min` proposal; CAD sharp edges are
  conceptual and not production geometry.
- No ceramic thread/hole receives a fastener. External saddle hardware bears against broad face
  datums/hard stops.

The monolithic core can provide the best as-made orthogonality, but firing distortion, three-face
datum grinding, inspection setup, and whole-part scrap dominate NRE/per-unit risk. A chipped face
can scrap the common core and disturb all three axes.

### 6.4 Fasteners, service, and collision result

For core face center `cz=18.15 mm`, X screw levels are 16.15/20.15 mm and Y levels are
20.15/16.15 mm. Z screws remain at global `(-6.50,0)` and `(0,-6.50)`. All tools approach
straight out of the selected face. Kernel critical-body overlap is 0.000000 mm³.

Service follows the Concept-A sequence, except the fixed datum is the monolithic face and the
external saddle clamp is removed. No other sensor is removed. Inspect the entire core for corner
chips/cracks after any service event.

### 6.5 Part count and cost drivers

The CAD contains 33 modeled physical groups excluding harness reservations and unresolved lower
post attachments. Ceramic piece count is lower than A, assembly is simpler, and orthogonality may
be better. The disadvantages are complex green machining, firing distortion, optional three-face
post-grinding, more expensive inspection, high single-part scrap exposure, and a common-core
failure that can strand three reusable LCCs during repair.

**Flip to B — ENGINEERING PROPOSAL — VALIDATE:** only if vendor quotation shows the inspected
core at no more than 1.5 times the complete A seat set after A assembly labor, while guaranteeing
the required face datums/orthogonality and replacement lead time. This ratio is a project decision
threshold, not a vendor quote.

## 7. Concept C — split protected cassette with rear tongue/contacts

### 7.1 Structure and dimensions

- One simple `10.50 mm` open zirconia core, `6.50 mm` bottom cavity, nominal 2.00-mm side walls.
- Per sensor: `9.80 × 9.80 × 1.00 mm` zirconia rear datum; bonded LCC; 0.50-mm vented CP-Ti front
  guard; 3.25-mm total cassette stack.
- The LCC sits between rear datum and front guard with 0.10 mm nominal axial space.
- A rear four-lane tongue leaves behind the LCC and transitions to the same qualified pigtail used
  by A/B; no unqualified hot spring socket is introduced.
- A shared open CP-Ti rail cage guides three cassettes. Shared positive-corner rail material is one
  fused cage feature, not stacked overlapping parts.
- Two positive shoulder/pin screws per cassette pass only through the external rail cage.

**HOLD — DO NOT FABRICATE:** the 0.10-mm nominal axial LCC space cannot be tolerance-closed until
actual LCC thickness/warpage and front-guard flatness are measured.

### 7.2 Envelope and tolerance

Kernel result: conservative radius 14.354 mm; `z=0…26.550 mm`. Nominal height margin is 0.950 mm.

Proposed worst-case height:

`26.550 + 0.10 base datum + 0.05 frame + 0.10 core + 0.08 cassette + 0.03 pin = 26.910 mm`.

The 9.80-mm cassette is smaller than the 10.50-mm core face, giving 0.350 mm nominal and 0.275 mm
proposed worst-case adjacent-face clearance.

### 7.3 Ceramic DFM and stress mode

- Custom ceramic count: one core plus three identical flat rear datums; two geometries.
- Rear datum window ring is 1.70 mm nominal, 1.625 mm proposed worst case.
- Core side wall is 2.00 mm nominal, 1.90 mm proposed worst case.
- Ti front guard, rail cage and pins carry service handling; no pin passes through ceramic.
- Rear datums receive broad compression/hard-stop load. Rails require compliant tabs so lateral
  play is removed without wedging the fired ceramic.

The ceramic work is simple, but the shared Ti rail cage, pin holes, rear tongue, and axial cassette
stack require more precision metal fabrication and assembly qualification than A.

### 7.4 Pin axes, tools, and collision result

For face center `cz=17.75 mm`:

| Hardware | Global level/location | Tool direction |
|---|---|---|
| X-P1/P2 | `y=-6.10`, `z=14.75/16.25` | straight `+X` |
| Y-P1/P2 | `x=-6.10`, `z=18.25/19.75` | straight `+Y` |
| Z-P1 | `x=-6.10,y=0` | straight `+Z` |
| Z-P2 | `x=0,y=-6.10` | straight `+Z` |

X/Y levels have at least 2.00 mm separation; modeled pin diameter is 1.40 mm, leaving 0.60 mm
level clearance even if the axes projected toward one another. Their actual finite axes occupy
different negative-edge sectors and do not cross. Pin-to-core nominal surface clearance is
0.150 mm; proposed worst case is only 0.030 mm, so exact rail/pin tolerances are a red-team and
vendor gate. Critical-body overlap is 0.000000 mm³.

### 7.5 One-cassette service/remating sequence

1. De-energize/vent/cool; record continuity/calibration.
2. Support the selected cassette by its guard jig; open only its remote disconnect and strain
   relief.
3. Remove the two same-side external pin retainers with straight access.
4. Withdraw the cassette normal to its face between the open rails. The guard stays over the bond
   loops; the other two cassettes remain pinned.
5. Inspect rear datum, front guard, pin surfaces/holes, rail tabs, tongue/pigtail, and LCC.
6. Insert/remate normal to the face until the rear hard stop seats; install new/qualified pin
   retainers; restore branch strain relief and remote contact.
7. Repeat continuity, insulation, polarity, noise and full vector calibration.

### 7.6 Part count and cost drivers

The CAD contains 31 modeled physical groups excluding reserved harness volumes and unresolved
lower post attachment. Custom ceramics are simple, but each cassette adds a Ti front guard and the
head needs a shared precision rail cage plus six shoulder/pin retainers. C best contains and
handles each bonded LCC, but the additional metal tolerance stack and rear-tongue remating make it
less reliable/cost-effective than A until proven by cycle tests.

## 8. Common fastener/material disposition

The complete schedule is `outputs/30_FASTENER_AND_THREAD_SCHEDULE.csv`.

- Baseline structural/flexure material: CP-Ti Grade 4 or a supplier-qualified nonmagnetic
  equivalent, clean for UHV, no nickel/steel near sensors.
- NBK SNZT M1.6 cleanroom Grade-1 Ti screws demonstrate 3–6-mm miniature geometry and nonmagnetic
  material availability. They are **not** a released 250 °C UHV part.
- Open through-holes and external replaceable nut pads avoid blind trapped volumes. Where a thread
  cannot be fully open, it must be longitudinally vented.
- No lubricant, MoS2, silver plate, or anti-seize is permitted without material/magnetic/UHV and
  250 °C qualification. Dry Ti/Ti galling and particle generation are explicit test gates.
- Candidate screw/nut sets are consumables after service until hot repeated-use testing clears a
  reuse rule.
- Tightening torque is not the preload-setting method. Hard stops establish geometry; exact torque
  is set only after screw/nut and galling coupons.
- Total threads in zirconia across all schedules: **zero**.

## 9. DFM, parts, and RFQ cost plan

### 9.1 Proposed vendor drawing rules

| Feature | Proposal | Release state |
|---|---:|---|
| Minimum ceramic wall/web | 1.50 mm | ENGINEERING PROPOSAL — VALIDATE |
| Internal ceramic radius | R0.75 mm minimum | ENGINEERING PROPOSAL — VALIDATE |
| External ceramic radius | R0.50 mm minimum | ENGINEERING PROPOSAL — VALIDATE |
| Edge break/chamfer | 0.20 mm minimum | ENGINEERING PROPOSAL — VALIDATE |
| Tapped/internal zirconia threads | 0 | binding design rule satisfied |
| Blind nut traps/undercuts | 0 | binding design rule satisfied |
| Critical post-ground features | only pocket/seat datums vendor identifies | HOLD pending quote |
| All dimensions | fired/finished millimetres | required RFQ note |

Kyocera documents near-net forming followed by final grinding and lists representative zirconia
properties; Precision Ceramics reports approximately 20% shrinkage for zirconia processing. The
vendor owns green scaling and lot compensation. The CAD contains sharp conceptual corners that
must be replaced by approved radii before any production drawing.

### 9.2 Relative cost drivers

| Driver | A | B | C |
|---|---|---|---|
| Unique custom ceramic geometries | 2 | 2 | 2 |
| Custom fired ceramic pieces/head | 6 | 4 | 4 |
| Flat repeated ceramic parts | 3 seats + 3 common guards | 3 common guards | 3 rear datums |
| Complex monolithic ceramic | none | one three-face core | one simpler small core |
| Expected post-fire datum work | individual flat seats only | highest; three-face core/orthogonality | rear flats + core faces |
| Ceramic scrap consequence | one small seat/guard | whole common core | one rear or core |
| Ti mechanism/assembly | medium | medium-low | highest |
| Calibration repeatability risk | bolted seat datum | lowest if core holds orthogonality | pin/rail stack highest |

No direct 1/3/10-set vendor price is available. Supplying invented dollar ranges would violate the
evidence rules. The following RFQ must be issued before a fabrication decision:

| RFQ lot | Concept A | Concept B | Concept C | Price field |
|---|---|---|---|---|
| 1 installed set | 3 seats + 3 guards; quote 2 spare seats | 1 core + 3 guards | 1 core + 3 rear datums; quote 2 spare rears | **PENDING VENDOR RFQ** |
| 3 installed sets | 9 seats + 9 guards; quote 2 spare seats | 3 cores + 9 guards; quote 1 spare core | 3 cores + 9 rear datums; quote 2 spare rears | **PENDING VENDOR RFQ** |
| 10 installed sets | 30 seats + 30 guards; quote 2–5 spare seats | 10 cores + 30 guards; quote 1 spare core | 10 cores + 30 rear datums; quote 2–5 spare rears | **PENDING VENDOR RFQ** |

Require separate NRE/tooling, green machining, sintering/HIP if proposed, post-fire grinding,
inspection/CMM, cleaning/packaging, first-article, per-lot, yield/scrap, lead-time and expedite
line items. Ask each vendor to redline every proposed wall/radius/tolerance rather than quote a
silent exception.

## 10. Weighted score after hard-gate filtering

Score is 1–5; weighted contribution is `weight × score/5`. All three remain conditional concepts,
not released hardware.

| Criterion | Weight | A score / contribution | B score / contribution | C score / contribution | Basis |
|---|---:|---:|---:|---:|---|
| Fabrication cost/simplicity | 30 | **5 / 30** | 3 / 18 | 3 / 18 | A uses identical flat seats; B has core distortion/scrap; C has precision rail/pin mechanism |
| Bonded LCC reuse/damage risk | 25 | **5 / 25** | 4 / 20 | **5 / 25** | all guarded; B common-core chip affects all; C best cassette containment |
| Connection reliability/serviceability | 25 | **5 / 25** | **5 / 25** | 4 / 20 | A/B retain Stage-10 permanent pigtail with simplest face clamp; C adds rear cassette stack/pins |
| Thermal/tolerance/calibration | 10 | 3 / 6 | **5 / 10** | 3 / 6 | B best monolithic orthogonality; A bolted seats and C rail/pin stack require more recalibration evidence |
| Assembly/tool access | 10 | **5 / 10** | 4 / 8 | 4 / 8 | A has small replaceable seats and straight tools; B core inspection and C pins add steps |
| **Total** | **100** | **96** | **81** | **77** | A selected |

### Reversal triggers

- **A → B:** inspected B core meets vendor redlines and costs no more than the proposed 1.5×
  A-seat-set decision threshold after assembly labor, while materially improving calibrated
  orthogonality/repeatability.
- **A → C:** the operating program requires frequent cartridge swaps and C passes 25 hot/cold
  removals with lower damage/contact/calibration drift than A, enough to justify its rail/pin cost.
- **Any concept → redesign:** actual mated 19C geometry consumes the proposed post/base clearance;
  wire stack does not fit 3×3-mm corridors; flexure force relaxes below acceptance; CP-Ti hardware
  galls/particles; magnetic screening fails; or vendor cannot meet positive adjacent clearances.

## 11. Calibration and qualification required before release

1. **Dimensional first article:** CMM/optical check all fired datums, windows, walls/radii,
   orthogonality, adjacent clearances, envelope, post/feedthrough clearance and tool corridors.
2. **Cartridge lot survey:** LCC body/thickness/warpage, guard pocket, loop envelope, tongue and
   pigtail dimensions; signed chamfer/orientation traveler remains mandatory.
3. **Preload coupon:** formed CP-Ti force-displacement at 20/250 °C; continuous dwell, thermal
   cycles, free-height/force recovery, hard-stop wear and ceramic contact microscopy.
4. **Fastener coupon:** exact alloy/finish/cleaning, torque-to-hard-stop, galling, particles,
   repeated service, venting and hot vacuum exposure. Do not use NBK catalog data as life proof.
5. **Harness article:** actual six-pair/12-conductor branch stack through three corridors; bend,
   proof load, abrasion, strain relief, insulation and resistance before/after hot vacuum.
6. **Service demonstration:** independently remove/remate each axis with the other two installed;
   video/tool witness, no loop contact, no connector load, no chip/particle, continuity and contact
   resistance before/after. Minimum proposed 25 cycles.
7. **Thermal-vacuum assembly:** full head at continuous 250 °C UHV with resistance/noise/leak and
   magnetic background monitoring; inspect/measure after dwell and cycles.
8. **Calibration:** full 3×3 sensitivity/orthogonality matrix at operating temperature after bake
   and after every cartridge service. A/B/C mechanical orthogonality is not a substitute for
   measured vector calibration.
9. **Handling:** qualified acceleration/vibration/proof-load envelope using measured cartridge and
   harness mass; no unsupported numerical g limit is asserted here.

## 12. CAD and drawing index

### Parametric/kernel artifacts

- `outputs/cad/30_package_concepts.py`
- `outputs/cad/30_CAD_KERNEL_REPORT.txt`
- `outputs/cad/30A_triplate_cage_NOT_FOR_FABRICATION.step`
- `outputs/cad/30A_triplate_cage_ceramic_NOT_FOR_FABRICATION.stl`
- `outputs/cad/30B_monolithic_core_NOT_FOR_FABRICATION.step`
- `outputs/cad/30B_monolithic_core_ceramic_NOT_FOR_FABRICATION.stl`
- `outputs/cad/30C_split_cassette_NOT_FOR_FABRICATION.step`
- `outputs/cad/30C_split_cassette_ceramic_NOT_FOR_FABRICATION.stl`

The STEP files contain concept solids, reserved harness volumes and installed fastener/clip
envelopes. The ceramic STLs contain only custom ceramic concept bodies. Production fillets,
surface callouts, exact contacts and released fasteners are intentionally absent.

### Per-concept SVGs

| View | Concept A | Concept B | Concept C |
|---|---|---|---|
| Isometric/exploded | `drawings/30A_isometric_exploded.svg` | `drawings/30B_isometric_exploded.svg` | `drawings/30C_isometric_exploded.svg` |
| Top envelope | `drawings/30A_top_envelope.svg` | `drawings/30B_top_envelope.svg` | `drawings/30C_top_envelope.svg` |
| Axial section | `drawings/30A_section.svg` | `drawings/30B_section.svg` | `drawings/30C_section.svg` |
| Contact detail | `drawings/30A_contact_detail.svg` | `drawings/30B_contact_detail.svg` | `drawings/30C_contact_detail.svg` |
| Fastener/pin axes | `drawings/30A_fastener_axes.svg` | `drawings/30B_fastener_axes.svg` | `drawings/30C_fastener_axes.svg` |

Detailed numeric records:

- `outputs/30_DIMENSION_AND_COLLISION_LEDGER.csv`
- `outputs/30_FASTENER_AND_THREAD_SCHEDULE.csv`

## 13. Stage-30 fabrication/procurement gates

1. `G30-01 HOLD — DO NOT FABRICATE`: obtain the exact mated 19C vacuum protrusion, diameter,
   support datum/tolerance, lower post attachment, UW port datum and magnetic/material acceptance.
2. `G30-02 HOLD — DO NOT FABRICATE HARNESS`: freeze conductor/insulation/shield type, finished OD,
   four-conductor branch lay, bend radius, proof load and 3×3-mm corridor fit.
3. `G30-03 HOLD — DO NOT FABRICATE CERAMIC`: vendor-approved zirconia grade/process, fired and
   post-ground tolerances, radii/walls, flatness/orthogonality, inspection, cleaning and 1/3/10-set
   quote; confirm actual LCC body/material/warpage.
4. `G30-04 HOLD — DO NOT FABRICATE RETENTION`: exact CP-Ti grade/form/heat treatment, flexure
   geometry/stiffness/contact pads, 20/250 °C retained force/creep, rail compliance, ceramic contact
   stress and positive-retention proof.
5. `G30-05 HOLD — DO NOT RELEASE BONDED CARTRIDGE`: measured loop/heel envelope, guard clearance,
   handling jig, same-stack hot-vacuum bond/die-attach qualification and physical LCC orientation.
6. `G30-06 HOLD — DO NOT RELEASE SERVICE PROCEDURE`: demonstrate one-axis removal/remating with
   other sensors installed, tool/chamber access, particles/chips, contact/insulation, hot cycle life
   and calibration repeatability.
7. `G30-07 HOLD — DO NOT FABRICATE CONCEPT C`: close actual LCC thickness/warpage and 0.10-mm
   nominal axial cassette clearance; freeze rear-tongue/contact detail.
8. `G30-08 HOLD — DO NOT ORDER FASTENERS`: exact screw/pin/nut alloy and finish, cleaning/UHV and
   magnetic declarations, venting/open-hole proof, hot galling/particle/reuse tests, torque and
   delivered inspection. NBK parts are geometry evidence only.
9. `G30-09 HOLD — DO NOT ISSUE PRODUCTION CAD`: replace conceptual sharp edges with vendor radii,
   add GD&T/datum scheme and released tolerance stack, freeze all material/part numbers, and pass
   Stage-40 independent red team.

## 14. Primary sources added for this stage

- Kyocera zirconia process/properties:
  https://global.kyocera.com/prdct/fc/technologies/001.html
- TIMETAL 75A Grade 4 CP-Ti:
  https://www.timet.com/assets/local/documents/datasheets/cpgrades/75a.pdf
- NBK M1.6 cleanroom titanium screw geometry:
  https://www.nbk1560.com/en-US/products/specialscrew/nedzicom/titaniumscrew/SNZT/SNZT-M1.6/
- NBK vacuum-fastener venting basis:
  https://www.nbk1560.com/en/products/specialscrew/nedzicom/vacuumscrew/
- Kyocera representative alumina CTE:
  https://global.kyocera.com/prdct/fc/technologies/003.html

Source-specific claim limits are in `outputs/SOURCE_LEDGER.csv`. Earlier Spectrum, Accu-Glass,
wirebond, die-attach, conductor, ceramic-DFM and board sources remain controlling for their own
claims.

## 15. Stage acceptance result

- Three required manufacturable directions: **PASS**.
- Hard envelope including modeled fasteners, posts, strain relief and reserved harness volumes:
  **PASS CONCEPT; exact feedthrough/cable tolerance held**.
- Carrier tolerance, 20/250 °C displacement and force arithmetic: **PASS WITH VALIDATION HOLDS**.
- Walls/edges/radii/stress modes: **DOCUMENTED; VENDOR REDLINE HELD**.
- Every face fastener/pin axis, nut location, tool direction, crossing rule and assembly sequence:
  **PASS CONCEPT; exact hardware held**.
- Wire bend/bond keep-out and independent replacement/remating: **DOCUMENTED; PHYSICAL TEST HELD**.
- Part count, unique ceramics, DFM/NRE/per-unit drivers and 1/3/10-set RFQ plan:
  **PASS; NUMERICAL PRICES UNAVAILABLE AND NOT INVENTED**.
- Required score weights applied after hard-gate filtering: **PASS; A selected 96/100**.
- Fifteen required SVG views: **PASS XML; representative render/visual QA passed**.
- Parametric CAD and three STEP/STL pairs: **PASS KERNEL; clearly NOT FOR FABRICATION**.
- Ceramic thread count: **0 in every concept**.

Stage 30 result: **COMPLETE WITH OPEN FABRICATION, MATERIAL, SERVICE, AND PROCUREMENT GATES**.
