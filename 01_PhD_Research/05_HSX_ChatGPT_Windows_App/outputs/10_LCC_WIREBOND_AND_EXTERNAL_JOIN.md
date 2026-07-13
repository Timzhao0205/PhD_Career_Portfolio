# Stage 10 - LCC02046 wire-bond and one-side external join

Date: 2026-07-12  
Decision status: recommended architecture selected for downstream design, but irreversible bond,
contact fabrication, and purchase holds remain active where called out.

## 1. Outcome first

Use a **protected removable sensor cartridge** comprising one bonded die/LCC02046 plus a
mechanically captured, vented one-side fanout tongue. Retain the user's short, non-crossing
physical die bonds to shelf pads `8, 3, 19, 14` only after microscope/GDS sign-off identifies the
actual die terminals and verifies bond clearances. Do **not** implement the user's four external
pad-to-pad bridges as the baseline. Take each signal from the same-numbered selected LCC
castellation to the fanout tongue with a qualified short, protected transition; terminate the four
300-deg-C UHV pigtails at the tongue; route them together through a separate ceramic strain-relief
comb to a remote service disconnect.

The cartridge, including its pigtail/tongue, is the reusable replaceable unit. The service
disconnect and harness clamp—not the die bonds, shelf transitions, castellations, or electrical
contacts—carry handling and cable loads. A later custom precious-metal socket can replace the
permanent tongue transitions only if continuous-250-deg-C UHV, magnetic, force, and cycle-life
qualification closes G05-03.

`HOLD - DO NOT BOND`: this recommendation does not authorize bonding until the orientation and
traveler sign-offs in section 5 are complete.

## 2. Controlling view and terminology

- View: **cavity up**, matching the supplied Spectrum drawing and annotated image.
- Datum A: the **pin-1 chamfer at the lower-right corner** in the supplied view.
- Pad sequence in this view:
  - top, left to right: `8, 7, 6, 5, 4`;
  - right, top to bottom: `3, 2, 1, 20, 19`;
  - bottom, left to right: `14, 15, 16, 17, 18`;
  - left, bottom to top: `13, 12, 11, 10, 9`.
- `q1, q2, q3, q4` are **physical annotated die terminals only**: top, right, bottom, left in
  the user's red markup. They are not assumed to be `p1, p2, p3, p4`.
- `P(qi)` is the authoritative p-identity assigned to physical terminal `qi` by the signed
  microscope/GDS traveler.
- An electrical tie is unordered. `a<->b` means pads a and b are the same net; it does not imply
  a signal-flow direction.

The exact drawing and physical carrier remain controlling over this text. Incoming continuity must
verify each shelf pad reaches only the same-numbered castellation before any die is committed.

## 3. Exact resolution of the user's 14/18 notation

The supplied image contains a cavity-up view at left and a mirrored bottom view at right. The red
inner bonds are on the cavity-up view; the green external lines are on the bottom view. This view
change explains why the bottom-view green line is written left-to-right as `18->14` even though
the cavity-up bottom row reads 14-to-18 left-to-right. The supplied image shows:

| Physical die terminal | Red inner shelf bond | Green external statement normalized |
|---|---:|---|
| q1, annotated top | 8 | `8<->4` |
| q2, annotated right | 3 | `3<->9` |
| q3, annotated bottom | 19 | `19<->13` |
| q4, annotated left | 14 | `14<->18` |

The written `18->14` is not a different inner bond. It is a left-to-right line in the mirrored
bottom view. Because a passive jumper has no electrical direction, the normalized interpretation
is **q4 bonds to pad 14 and pads 14 and 18 are externally tied**.
All new drawings/tables therefore use `14<->18`; no document uses a directional arrow for these
ties.

This resolves the notation, but it does **not** validate the jumper concept:

- LCC02046 routes each shelf pad only to its same-numbered castellation; it does not internally
  route 8 to 4, 3 to 9, 19 to 13, or 14 to 18.
- In the cavity-up plan, `8<->4` spans the top row, `3<->9` and `19<->13` span opposing sides,
  and `14<->18` spans the bottom row. Those four duplicate nets around the perimeter; they do not
  place four connector lands on one physical side.
- If the green lines are free wires extended to the right, the one-side result comes from those
  free wires, not from LCC routing. They still need termination, protection, and strain relief.
- A top-side execution crosses or skirts the open cavity and bond field; an underside execution
  interferes with a flat socket/seat and creates hidden joints. Either makes inspection and repair
  worse.

Verdict: the `14<->18` ambiguity is closed as an interpretation, while the four-jumper network is
rejected as the production baseline.

## 4. Orientation-parametric electrical map

The physical bond map may be inspected without guessing p-identities:

| Physical terminal | Recommended physical shelf pad after sign-off | Same-numbered castellation | Fanout lane | Electrical identity after sign-off | Board endpoint rule |
|---|---:|---:|---|---|---|
| q1, top | 8 | 8 | L1 | `P(q1)` | p1->J1.1; p3->J1.2; p2->J1.6; p4->J1.7 |
| q2, right | 3 | 3 | L2 | `P(q2)` | same rule |
| q3, bottom | 19 | 19 | L3 | `P(q3)` | same rule |
| q4, left | 14 | 14 | L4 | `P(q4)` | same rule |

The 8/3/19/14 map is recommended because the supplied overlay shows four short, separated,
non-crossing approaches. It is **not** released from the drawing alone. At microscope sign-off,
the bonder must overlay actual die-pad coordinates, wedge-foot direction, shelf landing area,
tool access, and loop keep-outs. If any landing is not safe, choose the nearest clear shelf pad in
the same quadrant and regenerate every drawing/table before bonding; do not improvise at the
bonder.

### Rotation table, usable only after cyclic order is verified

If and only if the GDS/microscope proves the clockwise physical order is
`p1, p3, p2, p4`, the four non-mirrored rotations are:

| Signed orientation | q1/top -> pad 8 | q2/right -> pad 3 | q3/bottom -> pad 19 | q4/left -> pad 14 |
|---|---|---|---|---|
| R0 | p1 / J1.1 | p3 / J1.2 | p2 / J1.6 | p4 / J1.7 |
| R90 | p4 / J1.7 | p1 / J1.1 | p3 / J1.2 | p2 / J1.6 |
| R180 | p2 / J1.6 | p4 / J1.7 | p1 / J1.1 | p3 / J1.2 |
| R270 | p3 / J1.2 | p2 / J1.6 | p4 / J1.7 | p1 / J1.1 |

Mirrored variants are forbidden unless the authoritative die documentation explicitly shows a
mirror. If the cyclic order differs, use the generic `P(q)` table, not this rotation shortcut.

No LCC pad is inherently “bias” or “sense.” During spinning the terminal roles change. Durable
labels are p1-p4 and axis X/Y/Z; the ambient board convention remains p1=J1.1, p3=J1.2,
p2=J1.6, p4=J1.7.

## 5. Mandatory pre-bond microscope/GDS sign-off

The traveler must contain all of the following on one page:

1. Die lot/wafer/die coordinates and a microscope image after die attach.
2. LCC lot and Spectrum drawing revision; cavity-up photo with lower-right chamfer circled as
   Datum A.
3. Shelf-to-castellation continuity results for pads 1-20 and isolation to neighbors/ring.
4. Authoritative GDS/runsheet screenshot identifying physical p1-p4 and the sign convention.
5. Hand-entered `P(q1)..P(q4)` plus independent second-person verification.
6. Selected physical bond landings; default 8/3/19/14 or a formally revised map.
7. Board endpoints derived mechanically from p-identity, never from q-number.
8. Die-pad metal stack, LCC purchased-lot finish, wire alloy/diameter, wedge/tool, bonder, and
   recipe revision.
9. A bond-field image showing wire paths, no crossings, clearance to die edges/mesa, shelf steps,
   seal ring, fanout transitions, and the future vented guard.
10. Explicit boxes: `NO MIRROR`, `VIEW=CAVITY UP`, `CHAMFER=LOWER RIGHT`, `14<->18 USER TIE NOT
    USED IN RECOMMENDED BASELINE`, inspector names, date, and release signature.

Any missing or contradictory item leaves `G05-01 HOLD - DO NOT BOND` open.

## 6. Concept comparison A-E

### A. User four-corner/four-jumper concept

Configuration: q1/q2/q3/q4 to 8/3/19/14, then 8<->4, 3<->9, 19<->13, 14<->18.

Strengths:

- The four red inner bonds appear short, separated, and non-crossing.
- Duplicate electrical landings could permit a second probe point or redundant electrical bond.

Failures/risks:

- Four pad-to-pad ties are not internal traces and do not create four lands on one side.
- They add at least four spans and eight terminations before the harness connection.
- Top-side ties enter the open bond/guard field; underside ties are hidden and obstruct a flat
  seat; perimeter ties are long and vulnerable.
- Thermoelectric, resistance, inspection, and repair asymmetries increase.
- A parallel pad or parallel wire can improve electrical redundancy only after qualification; it
  is not strain relief and must never be used to justify harness load on the carrier.

Disposition: **reject external jumper network; retain the physical inner map only after sign-off**.

### B. Shortest non-crossing die bonds plus separate one-side breakout

Configuration: bond each physical terminal to its nearest clear shelf pad, then connect the four
same-numbered castellations to a separate fanout element outside the bond field.

Strengths: minimum bond span, no crossing, low unmatched parasitics, clean microscope inspection,
and separation of die bonding from harness routing.

Risks: the breakout element needs a qualified nickel-free metallization/contact process and must
fit the head cartridge.

Disposition: **adopt as the electrical geometry principle**.

### C. Welded/crimped flying leads directly at selected castellations

Configuration: preattach a bondable/weldable tab or lead to castellations 8/3/19/14, route four
300-deg-C UHV conductors to one side, and make any crimp/weld at a larger supported terminal.

Strengths: low part count, cheap prototype, cartridge can travel with its pigtail, remote service
disconnect preserves reuse.

Risks: resistance/parallel-gap welding directly on thin Au ceramic metallization is not qualified;
heat/force can crack ceramic or peel metallization. A crimp cannot be made directly to a
castellation. Direct stranded wire introduces uncontrolled flex at the brittle edge unless clamped
immediately.

Disposition: **credible runner-up** if direct castellation coupons demonstrate metallization
integrity and aged resistance. Never weld a real sensor first.

### D. Reusable high-temperature socket/spring/contact

Configuration: custom Paliney-class or other declared nonmagnetic spring fingers contact the four
selected castellations; LCC is clamped into a zirconia seat.

Strengths: fastest sensor exchange; no permanent external bonds; best reuse if qualified.

Risks: no catalog-qualified LCC02046 socket was found for continuous 250 deg C UHV. Exact alloy,
temper, plating/underplate, magnetic permeability, UHV cleaning/outgassing, normal force,
relaxation, fretting, contact resistance, and envelope remain open. PEEK and assumed BeCu retention
are not accepted baselines.

Disposition: **development option, not current baseline**. Flip to this option only after G05-03
is closed with exact-part evidence and life coupons.

### E. Protected hybrid cartridge with fanout tongue - recommended

Configuration:

1. Use B's signed shortest non-crossing die bonds.
2. Mechanically co-capture the LCC and a thin, vented, nickel-free ceramic fanout tongue in the
   removable cartridge; no adhesive in the head structure.
3. Connect each selected same-numbered castellation to the adjacent lane pad/tab with a short
   qualified transition. First qualification candidate: redundant Al wedge/ribbon bonds to a
   declared bondable Au finish. Direct resistance-welded tab is the alternate DOE arm.
4. Join the four KAP301-class 300-deg-C UHV conductors at large supported lane terminals using a
   qualified resistance weld or exact-contact crimp. Do not crimp or weld directly on the LCC in
   the baseline.
5. Clamp the pigtail in a separate ceramic strain-relief comb on the tongue/cartridge before it
   bends toward the one-side exit.
6. Cover die bonds and external microbonds with a removable **vented zirconia guard**. The guard
   is not a hermetic lid, contains no trapped cavity, and clears the measured loop envelope.
7. Put the service disconnect downstream of the strain relief, accessible without touching the
   bonded carrier.

Why this wins:

- It isolates the fragile LCC metallization and microbonds from harness loads.
- The die/LCC/tongue/pigtail remains an independently removable and reusable protected cartridge.
- It uses the same Al-on-thin-Au evidence family for the short microbond transitions while moving
  the robust Cu-wire weld/crimp to a large supported terminal.
- It avoids a PEEK body, unqualified BeCu preload, solder at 0.946 homologous temperature, hidden
  underside joints, and internal ceramic threads.
- It has more custom content than C but less continuous-force risk than D and far fewer fragile
  free spans than A.

Disposition: **recommended for stage-30 packaging and coupon development**. The exact fanout
substrate/finish and microbond style are `HOLD - DO NOT FABRICATE` until supplier declarations and
qualification coupons pass.

## 7. Electrical and physical behavior

### Bond span, loop, crossings, and parasitics

Authoritative die outline/pad coordinates and shelf height are missing, so no fabricated loop
number is released. For each candidate landing, calculate from microscope metrology:

- horizontal span `s_i = sqrt((x_shelf-x_die)^2 + (y_shelf-y_die)^2)`;
- developed wire length from the signed bonder loop program;
- clearance from the entire swept loop to die edge/mesa, neighboring loops, shelf step, guard,
  and any fanout transition;
- terminal mismatch `max(s_i)-min(s_i)` and measured four-path R/L/C after assembly.

Acceptance is based on the same-process control population and aged functional performance, not a
remembered generic loop limit. The four paths shall not cross in plan or in the verified 3D loop
envelope. The bonder must work on each loose, horizontal cartridge; no bonding is attempted on an
assembled vertical cube face.

### Hall symmetry and spinning

Matched path geometry is desirable, but spinning does not excuse a bad connection. Static offsets
may demodulate away only while the connection remains linear and stable. Contact nonlinearity,
phase-dependent settling, intermittent resistance, leakage to a neighbor, or thermoelectric drift
can alias into the recombined signal. Qualification therefore measures every raw phase as well as
the recombined output.

The fanout preserves four independent terminals. No guard, shield, seal ring, spare LCC pad, or
other sensor shares a current return. A spare parallel electrical pad, if ever added, is documented
as the same net and separately tested; it is never a mechanical member.

### Thermoelectric EMF

Dissimilar junctions at a temperature gradient generate offsets. Deringer-Ney, for example, lists
Paliney 7 thermal EMF relative to platinum in the -8 to -10 uV/deg-C range; that number is not the
project stack and shows why exact alloys and gradients matter. Mitigations:

- use identical material stacks, joint processes, lengths, and thermal anchoring on all four lanes;
- cluster the four robust transitions into one isothermal region on the tongue;
- avoid an isolated hot junction on one terminal;
- record temperature at the cartridge and feedthrough during calibration;
- characterize raw-phase zero-field offsets across temperature and gradients;
- use current reversal/spinning as cancellation, then verify residual rather than assuming it;
- prohibit magnetic nickel/steel underplates and avoid closed conductive loops near the Hall
  plate that can support induced currents.

### Thermal cycling and continuous dwell

Differential expansion acts at the die attach, heel, LCC metallization, tongue transition, and
wire clamp. The vented guard and strain-relief comb must not touch or preload a microbond at cold or
hot extremes. Qualification includes ramp/dwell/cycle combinations from the finally approved duty
envelope; `250 deg C reached once` is not an acceptance condition.

### Handling, repair, and reuse

- Handle by protected cartridge datums, never the LCC castellations, die, tongue lanes, or wires.
- Remove the service connector, release the accessible harness clamp, then release the cartridge
  clamp. No other sensor cartridge is disturbed.
- Store removed cartridges in a keyed vented ceramic/metal transport nest with the bond guard in
  place.
- A failed external robust terminal may be reworked under a controlled traveler if the LCC
  microbond field remains untouched and post-repair qualification passes.
- A failed die bond, lifted shelf metallization, cracked ceramic, or unexplained resistance drift
  quarantines the cartridge; do not rebond a flight/experiment carrier by improvisation.

## 8. Solder disposition and cleanliness

80Au20Sn is eutectic at 280 deg C. At 250 deg C:

`T/Tm = (250+273.15)/(280+273.15) = 0.946`.

Thirty degrees Celsius and a homologous ratio of 0.946 are inadequate evidence for a sustained
mechanical/electrical joint with handling load, especially when Accu-Glass's nominal UHV solder
documentation also contains a 280/480-deg-C inconsistency. Flux, residues, wetting, metallization
dissolution, creep, and long dwell remain unqualified. Therefore:

- **No solder is used in the recommended LCC/tongue/harness baseline.**
- 80Au20Sn and the Accu-Glass UHV solder are rejected for any load-bearing or strain-relief role at
  continuous 250 deg C.
- Higher-melting AuGe/AuSi may be studied only on a separately fabricated terminal before die
  attach; process heat, wetting, metallization, UHV cleaning, magnetic content, and aged resistance
  require coupons. They are not a backdoor release for the assembled sensor.
- No flux-bearing process is accepted without supplier chemistry, a controlled cleaning traveler,
  residue inspection, blank/process controls, and vacuum/outgassing acceptance.

## 9. Fanout tongue and guard interface handed to stage 30

These are functional requirements, not released dimensions:

- LCC seat fits the 8.89-mm nominal body using supplier drawing tolerance and measured lot data.
- Tongue leaves from one selected service side and carries four uniquely keyed lanes L1-L4.
- All microtransitions are visible before guard installation and remain protected afterward.
- Vented guard has open conductance paths; it does not form a sealed or blind trapped volume.
- Guard-to-loop clearance is based on measured worst-case loop envelope plus assembly/thermal
  tolerance: `ENGINEERING PROPOSAL - VALIDATE` until stage-30 stack-up and coupons.
- LCC and tongue are supported by ceramic datums; cartridge clamp loads do not pass through
  metallization or electrical joints.
- Harness strain relief is downstream of robust lane terminals and upstream of the first free bend.
- All clamps/fasteners are externally accessible, non-crossing, and removable; zero internal
  zirconia threads and no adhesive.
- No Kovar/Alloy-42/Ni/Au CL-30010 lid. Spectrum identifies that combo-lid family as Kovar or
  Alloy 42 with nickel/gold plating and AuSn preform. Use a bare vented zirconia guard instead.
- No closed conductive screen around the die. Harness shields terminate per stage 20/30 grounding
  decision and remain mechanically independent.

## 10. Process flow and hold points

1. **Incoming**: verify LCC lot/drawing/finish, 1-20 continuity/isolation, body/chamfer, flatness,
   ceramic damage, and magnetic screen. `HOLD 1`.
2. **Orientation**: inspect die/GDS; enter `P(q)`; peer verification; select/revise 8/3/19/14;
   approve loop/guard overlay. `HOLD 2 - DO NOT BOND`.
3. **Coupon DOE**: qualify die-to-LCC Al wedge recipe, fanout microtransition, and robust tongue
   weld/crimp on sacrificial hardware. Include unaged controls. `HOLD 3`.
4. **Fanout preassembly**: fabricate/clean tongue, robust terminals, pigtails, and strain relief
   before a real sensor is exposed; verify magnetic/UHV declarations. `HOLD 4`.
5. **Die attach**: controlled 353ND lot/mix/bondline/cure on released coupons/units only; inspect
   wicking and position. `HOLD 5` pending G05-02 qualification status.
6. **Die bonds**: bond q1-q4 to the signed shelf map; record settings and microscope images; pull
   only designated witness units.
7. **External microtransitions**: same-numbered castellations to L1-L4; no user pad-to-pad jumpers;
   no structural load.
8. **Electrical inspection**: four-wire path R, neighbor/ring isolation, polarity/terminal identity,
   raw-phase injected-signal test, and cable flex while monitoring.
9. **Guard/cartridge assembly**: install vented guard and strain relief; verify no loop contact and
   all tools/fasteners accessible.
10. **Qualification**: execute `outputs/10_BOND_AND_JOIN_QUALIFICATION.csv`; thermal-vacuum life,
    pull/shear/witness, resistance, microscopy, cleanliness/outgassing, and service cycles.
11. **Release**: close applicable gates with signed evidence; otherwise status remains
    `COMPLETE_WITH_OPEN_GATES`, never a silent fabrication release.

## 11. Required tests and acceptance basis

The detailed matrix is in `outputs/10_BOND_AND_JOIN_QUALIFICATION.csv`. Key rules:

- MIL-STD-883 Method 2011 supplies a pull-test method/workmanship framework, not the complete
  continuous-life acceptance criterion.
- Numeric drift, pull, shear, leakage, outgassing, magnetic, cycle, and proof-load limits not
  supplied by an exact source are labeled `ENGINEERING PROPOSAL - VALIDATE`.
- Establish unaged control distributions from the same lots/processes. Compare aged populations
  with confidence bounds appropriate to the final reliability target; sample count and statistical
  acceptance remain open until the duty/loss consequence is signed.
- Track absolute path resistance and changes at temperature; a room-temperature post-test value
  alone can miss a hot intermittent.
- Inspect fracture mode, heel cracks, intermetallic/cavity development, lifted metallization,
  ceramic cracks, fretting, wire damage, residue, and guard/strain-relief witness marks.
- Test zero-field raw phases and recombined output before/during/after thermal-vacuum exposure.

## 12. Decision and flip conditions

Recommended: **E, protected hybrid cartridge/fanout tongue**, using signed short die bonds and no
pad-to-pad jumper network. Runner-up: **C, direct qualified flying-lead/tab transition**, if coupons
show it does not damage castellation metallization and a separate clamp removes all flex/load. The
reuse-optimized future option is **D**, but it flips to baseline only when an exact socket/contact
system passes continuous-250-deg-C UHV, magnetic, retained-force, contact-resistance, service-cycle,
and envelope qualification.

The recommendation reverses if:

- vendor/lab evidence proves a smaller, lower-cost exact socket closes G05-03;
- the fanout tongue cannot fit the stage-30 envelope/guard/tool access;
- nickel-free bondable tongue metallization cannot be obtained or fails aging;
- direct castellation tab coupons outperform the tongue microbond with equivalent protection;
- the approved service duration/temperature/magnetic budget invalidates the selected materials.

## 13. Open gates carried forward

- `G10-01 HOLD - DO NOT BOND`: G05-01 orientation/chamfer/plating/14-18 sign-off traveler not
  complete. The notation is resolved, but physical p1-p4 identity is still absent.
- `G10-02 HOLD - DO NOT RELEASE BONDED HEAD`: G05-02 actual 353ND/die-pad/Al-wire stack has no
  passed continuous-250-deg-C vacuum life qualification.
- `G10-03 HOLD - DO NOT FABRICATE FANOUT`: exact no-Ni tongue ceramic/metallization/finish,
  microtransition, robust terminal alloy, magnetic declaration, and UHV cleaning are unselected.
- `G10-04`: available bonder, wedge/ribbon capability, resistance/parallel-gap welder, crimp tool,
  pull tester, cross-section capability, and vacuum-aging capacity must be inventoried.
- `G10-05`: guard/loop/seat/strain-relief clearances remain stage-30 dimensions and require
  measured stack-up.
- `G10-06`: qualification duration, ramps, cycles, sample count, statistical confidence, drift,
  pull/shear, leakage, outgassing, magnetic, and proof-load criteria await the signed service
  envelope; every provisional numeric limit must remain `ENGINEERING PROPOSAL - VALIDATE`.

## 14. Drawing/table consistency check

- `drawings/10_lcc_recommended_top.svg`: cavity up; chamfer lower right; pad sequence exactly as
  section 2; q1/q2/q3/q4 to 8/3/19/14; p-identities parameterized; user ties shown only in a
  rejected comparison inset; orientation sign-off box present.
- `drawings/11_lcc_external_exit.svg`: same selected castellations; four protected lanes; one-side
  pigtail exit; microtransition, robust joint, vented guard, separate strain relief, and service
  disconnect labeled; electrical joints explicitly outside the load path.
- `10_BOND_AND_JOIN_QUALIFICATION.csv`: coupon lot, exposure, pull/shear, resistance, microscopy,
  cleaning/outgassing, acceptance, and basis fields present; unsupported limits labeled.

Stage-10 result: **architecture decision complete; fabrication remains held at explicitly listed
orientation, material, equipment, and continuous-life gates**.

## Sources added/used in this stage

See `outputs/SOURCE_LEDGER.csv`, especially S001-S003, S010, S013-S035, and:

- Spectrum LCC02046 drawing: https://www.spectrum-semi.com/sites/default/files/pdfs/LCC02046.pdf
- Spectrum LCC overview: https://www.spectrum-semi.com/products/leadless-chip-carrier
- Spectrum combo lids: https://www.spectrum-semi.com/products/combo-lid-square
- Johannessen et al. Al wedge aging record: https://www.sintef.no/en/publications/publication/1274740/
- DLA MIL-STD-883 Part 2/Method 2011: https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-883/std883-2.pdf
- microJoining stranded-wire resistance welding: https://www.microjoining.com/docs/1352551504_microtip_resistance_stranded_copper_wire.pdf
- microJoining plating effects: https://www.microjoining.com/docs/1352550977_microtip_plating_issues.pdf
- Allectra KAP301 cable: https://www.allectra.com/wp-content/uploads/2025/02/301-KAPM-025-PAIR1.pdf
- Indium Au alloy table: https://scp.indium.com/download-files/power_semiconductor_assembly_98464_r0.pdf
- Deringer-Ney contact manual: https://deringerney.com/wp-content/uploads/2022/04/Ney-Contact-Manual-Revised-1st-Edition.pdf
