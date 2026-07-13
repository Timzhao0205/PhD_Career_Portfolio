# 00 - Inventory and gap map

Status: stage-00 inventory only. This report does **not** select the final bond map, external join, feedthrough pin map, or ceramic concept.

Evidence labels used here:

- `VERIFIED INPUT`: directly present in an authoritative project file, image, netlist, PDF, or kernel-opened CAD.
- `RETAINED CALCULATION`: reusable arithmetic from `previous_results/`, rechecked where stated.
- `HISTORICAL PROPOSAL`: prior recommendation retained as evidence, not accepted under the new mission.
- `UNRESOLVED GATE`: missing evidence that must be closed before a bond, fabrication release, or purchase.

## 1. Authoritative constraints and source locations

| Requirement | Status | Source |
|---|---|---|
| All in-vessel die, LCC, conductor, joint, insulation, retention, and ceramic parts operate continuously in UHV at 250 deg C; ambient readout stays outside vacuum | `VERIFIED INPUT` | `AGENTS.md`; `MISSION.md`; user kickoff |
| Three mutually orthogonal, electrically isolated, four-terminal Hall sensors; 12 sensor conductors cross the vacuum boundary | `VERIFIED INPUT` | `AGENTS.md`; `inputs/project/HARDWARE_DATA.md` section 4; `inputs/reference/rsi_experiment_and_publication_plan.md` sections 2.2-2.5 |
| Complete installed head, contacts, clamps, fasteners, and harness exits must remain inside a diameter 31.75 mm by height 27.5 mm cylinder | `VERIFIED INPUT` | `AGENTS.md`; `inputs/reference/PACKAGING_3D_ENVELOPE.md`; `inputs/reference/envelope_reference.png` |
| Each bonded die plus purchased Spectrum LCC02046 must be independently removable, reusable, and protected during service; no adhesive in the reusable head baseline | `VERIFIED INPUT` | `AGENTS.md`; `MISSION.md`; `inputs/reference/PACKAGING_3D_ENVELOPE.md` |
| Baseline zirconia has zero tapped/internal threads and favors identical flat parts, smooth holes, accessible external nonmagnetic fasteners, replaceable nuts/nut plates, no hidden/crossing bolts | `VERIFIED INPUT` | `AGENTS.md`; `prompts/30_package.md` |
| Priority after hard safety/physics gates: fabrication cost, bonded sensor/LCC reuse, then electrical/mechanical connection quality | `VERIFIED INPUT` | `AGENTS.md`; `prompts/30_package.md` scoring weights |
| Avoid unqualified PEEK, BeCu relaxation assumptions, magnetic nickel/steel near sensors, blind volumes, inadequate-temperature solder, and structural load through electrical joints | `VERIFIED INPUT` | `AGENTS.md`; `prompts/05_sources.md`; `prompts/40_redteam.md` |
| Board-side sensor convention: J1 pin 1=p1, pin 2=p3, pin 6=p2, pin 7=p4; J3 pin 1=a2, 2=a1, 3=a0, 4=EN; J3 has no ground | `VERIFIED INPUT` | `inputs/project/HARDWARE_DATA.md` section 3; directly checked in `inputs/reference/hsx_2026_v2.net` |
| Three existing single-axis boards are the fixed architectural starting point; one Pico 2 fans out a0/a1/a2/EN; one floating 100 uA source per axis; three analog outputs plus one sync go to simultaneous DAQ | `VERIFIED INPUT` | `inputs/project/CONTEXT_PRIMER.md`; `inputs/reference/rsi_experiment_and_publication_plan.md`; `MISSION.md` |
| Do not infer p1-p4 physical orientation; use an orientation-parametric map and microscope sign-off if authoritative evidence is absent | `VERIFIED INPUT` | `AGENTS.md`; `prompts/10_wirebond.md` |

### Boundary clarification

The 2023 paper, `inputs/reference/2023_IEEE_SensorsLetters_HSX_GaN_Hall.pdf`, visually and textually verifies the earlier architecture: a 5 mm die was Al wire-bonded in a ceramic LCC, encapsulated with EPO-TEK 353ND, vacuum-baked at 150 deg C for 1 h, placed in a zirconia holder, and connected through feedthroughs to ambient electronics. The paper reports 68 HSX shots and functional survival, but it does **not** establish continuous 250 deg C life for the epoxy, bonds, contacts, or harness. It is heritage evidence, not the present qualification basis.

## 2. File and artifact inventory

### Current authoritative/reference inputs

- Project intent and facts: all five files under `inputs/project/` were read.
- Packaging references: `inputs/reference/PACKAGING_LCC02046.md`, `PACKAGING_3D_ENVELOPE.md`, `SPECS.md`, the bring-up plan, the RSI plan, the annotated LCC image, the envelope figure, and the starter render were inspected.
- Electrical design: `inputs/reference/hsx_2026_v2.net` and `hsx_2026_v2_bom.csv`; the netlist is KiCad E-format from Eeschema 10.0.3 dated 2026-07-09. Direct checks confirm J1's dedicated `D09S33E6GX00LF` footprint name, the four J1 signal nets, the four logic nets, and J1 spare pins 3/4/5/8/9 as unconnected nets.
- Peer-reviewed heritage: the four-page PDF was text-extracted and all four rendered pages visually inspected.
- Source CAD: `new_3d_idea_assembled.stp`, `new_3d_idea_disassembled.stp`, and `old_1d_sensor.stp` were opened with the build123d/OpenCascade kernel (build123d 0.11.1); no source file was modified.

### Historical processed evidence retained read-only

All reports, CSVs, source models, STEP/STL files, renders, and legacy state under `previous_results/` were inventoried. All 19 historical package renders were visually inspected, the user STEP models and historical Concept B/D STEP files were opened with a real CAD kernel, and the historical reports were read. Particularly reusable items are:

| Historical artifact | Reusable content | Limitation under current mission |
|---|---|---|
| `10_COMPONENTS/COMPONENT_REVIEW.md`, `bom_verdict.csv` | Ambient-board component facts/noise arithmetic; no measured-amplitude dependence | Several vendor facts require fresh primary-source verification; scope is not the in-vessel 250 deg C chain |
| `20_CONNECTIONS/CONNECTION_CHECK.md` | Full net trace, J1 mapping, phase-function interpretation, spare-pin confirmation | J1 physical footprint geometry/shell bond still requires first-article continuity |
| `30_3AXIS_ARCH/ARCHITECTURE_TRADE.md` | Strong case for three replaceable replicated boards | Air-side mechanical space and final cable layout remain inputs to stage 20 |
| `40_PI_FANOUT/PI_FANOUT.md` | Fanout load model and star-return concern | Earlier capacitance/GPIO facts were partly secondary or assumed; refresh from primary data |
| `50_FLANGE/FLANGE_SELECTION.md` | 19C-275 candidate identification and accessory menu | 19C-275 was introduced after the historical wiring/package work; protrusion, materials, conductor range, port fit, and magnetic budget are open |
| `60_WIRING_SHORTS/WIRING_PLAN.md` | FMEA, no-shared-return discipline, staged continuity/IR tests, current-limited fault insight | Written around superseded dual 9C2-275; wrong LCC physical pad association propagates; insulation and temperature assumptions need revision |
| `70_PACKAGING/PACKAGING_REVIEW.md` | Recognition that same-number shelf/castellation connectivity does not reroute pads; need for short noncrossing bonds and mount-level breakout | Assumed p1=N/p2=S/p3=E/p4=W and incorrectly associated pad 1 with the annotated drawing's top mid-side; continuous-250-deg-C Au-Al life was not qualified |
| `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` plus CAD | Real-kernel measurements of user CAD; useful modularity, keying, service, and collision concerns; Concept D flat-seat direction | Historical recommended Concept B uses PEEK and BeCu evidence below the current continuous 250 deg C requirement; complex monolithic ceramic and hidden/crossing hardware conflict with the new baseline rules |
| `90_SYNTHESIS/RED_TEAM.md` | Prior defect list, tolerance-chain warnings, rotation-key requirement, missing contact-detail drawing | Red team predates the 250 deg C continuous-life constraint and did not audit the new 19C-275 path |

## 3. Annotated user proposal and pad conflicts

### What the image actually shows

`inputs/reference/user_2026-07-12_LCC_routing_annotated.png` was inspected at original resolution. With the image viewed cavity-up and the chamfer/pin-1 index at the lower-right corner:

- carrier top row is numbered 8,7,6,5,4 from left to right;
- right row is 3,2,1,20,19 from top to bottom;
- bottom row is 14,15,16,17,18 from left to right in the cavity-up view; the separate bottom view at right is mirrored and shows 18 at left and 14 at right;
- left row is 13,12,11,10,9 from bottom to top;
- the physical mid-side pads in this view are therefore top=6, right=1, bottom=16, left=11;
- red die labels in the annotation are 1 at the top, 2 at right, 3 at bottom, and 4 at left;
- red bonds are drawn to inner shelf pads 8, 3, 19, and 14 respectively.

The user's exact stated proposal is preserved:

- inner shelf bonds: `8, 3, 19, 14`;
- external routes: `8->4, 3->9, 19->13, 18->14`;
- desired result: four conductors exit one side; electrically tied pads were considered as added strength.

### Contradiction and conflict table

| Conflict | Evidence | Current disposition |
|---|---|---|
| Inner fourth pad is 14, while the fourth external route is written 18->14 | Annotated image and `AGENTS.md` | Stage-10 direct view reconciliation found that the green routes are drawn on the mirrored bottom view, where 18 is left and 14 is right. A passive tie is unordered, so the normalized statement is `14<->18`, with q4 still bonded to 14. The notation gate is closed; die p1-p4 identity remains open. |
| Historical map says p1/N -> pad 1, p3/E ->16, p2/S ->11, p4/W ->6 | `previous_results/70_PACKAGING/PACKAGING_REVIEW.md` and downstream tables | The annotated Spectrum drawing physically shows top mid-side=6, right=1, bottom=16, left=11 in this orientation, so the historical physical association is rotated/mirrored relative to the actual drawing. The pad *set* {1,6,11,16} remains the four mid-sides; the terminal-to-pad map does not. Historical fixed numbers are not fabrication-authoritative. |
| Detailed reference says die pads are N/E/S/W; another project summary calls them “corner contacts” | `inputs/reference/PACKAGING_LCC02046.md` vs `inputs/project/REFERENCE_DATA.md` and question wording | The annotated image shows N/E/S/W die labels but is not authoritative evidence of actual gen-2 p1-p4 sign/orientation. Use an orientation-parametric map until microscope/GDS evidence exists. |
| Historical reports interpret parallel electrical pads as improving a connection, while current contract prohibits treating electrical redundancy as strain relief | Historical ST7/ST8 vs `AGENTS.md`/stage-10 prompt | Any jumper or second pad is only an electrical path. Harness strain relief must act on insulation/conductor separately and transfer no service or vibration load through a bond, castellation, weld, crimp, or contact. |

No map is frozen in stage 00. Stage 10 must compare the user's corner-adjacent layout against shortest noncrossing bonds, resolve chamfer/mirroring, and issue an orientation-parametric table with a mandatory microscope sign-off if p1-p4 evidence remains absent.

## 4. Historical conclusions invalidated or weakened by continuous 250 deg C UHV

| Historical conclusion | New status | Reason |
|---|---|---|
| PEEK contact insert is acceptable because catalog continuous-use temperature is near 260 deg C and stress is low | `REJECTED AS QUALIFIED BASELINE` | A catalog maximum/CUT and bake survival do not prove continuous UHV dimensional stability, creep, outgassing, or retained contact geometry at 250 deg C. PEEK may remain a coupon candidate only with exact grade, lot, load, atmosphere, duration, and post-exposure validation. |
| Au-plated BeCu leaf springs are acceptable based on 1000 h data at 200 deg C or a 200 deg C connector rating | `REJECTED AS QUALIFIED BASELINE` | No continuous 250 deg C retained-force evidence was supplied; extrapolation from 200 deg C is prohibited. A low-stress alternative alloy/contact or a validated BeCu life coupon is required. |
| EPO-TEK 353ND is acceptable because the 2023 assembly survived a 150 deg C/1 h vacuum bake and shots | `WEAKENED - OPEN GATE` | The bonded sensor/LCC itself must now operate continuously at 250 deg C. Bake survival and ASTM E595 screening do not establish continuous thermo-mechanical bond-line life. This is a reuse-critical qualification gate; the reusable head cannot fix an inadequate die attach. |
| Al wedge on Au is acceptable with a single generic pull threshold and visual after bake | `WEAKENED - OPEN GATE` | Continuous 250 deg C Au-Al intermetallic growth/Kirkendall behavior, actual die metallization, wire alloy/diameter, process window, and life profile must be verified with same-stack coupons and aged pull/shear/resistance/microscopy. |
| All solder should simply be rejected | `WEAKENED - RESEARCH REQUIRED` | Flux/residue, alloy solidus/liquidus, creep margin, metallization, joint stress, and UHV cleaning must be evaluated by process. Conventional soft solder may fail, but the mission requires a fair comparison with high-temperature solder, braze, resistance/laser weld, crimp, and contact options. |
| 19C-275 is purchase-ready after port and contact-size calls | `WEAKENED - HOLD` | The present mission also needs exact 250 deg C continuous-use interpretation, vacuum-side protrusion, material/magnetic content (historical page says gold-plated Ni-Fe pins), conductor range, connector stack, mounting datum, and a complete 12-pin allocation. `HOLD - DO NOT ORDER`. |
| Monolithic SpringClamp cube is lower-cost/optimal | `INVALIDATED AS BASELINE` | No vendor quote supported the monolithic-cost claim; the current contract explicitly prefers identical flat zirconia parts and forbids hidden/crossing bolts. Its PEEK/BeCu interface is unqualified at 250 deg C. The historical geometry remains a comparison concept only. |
| Open exposed bonds are adequately protected by handling procedure | `WEAKENED` | The current requirement adds protection during service. A vented removable guard/frame or service cover must prevent tool/finger/harness sweep without forming a trapped volume or using a magnetic sealed lid. |

## 5. Reusable calculations, CAD, drawings, and sources

### Rechecked calculations

- Envelope square limit: `31.75/sqrt(2) = 22.45 mm` maximum axis-aligned square edge, before protrusions.
- User CAD per-solid measurements reproduced with build123d/OpenCascade:
  - base plate `20.375 x 31.75 x 3.0 mm`, exactly at the radial diameter with no tolerance margin;
  - head block `20 x 15 x 15 mm`;
  - modeled sensor carriers `12 x 12 x 0.635 mm`, not LCC02046 `8.89 x 8.89 x about 1.65 mm`;
  - only two modeled sensor plates;
  - full assembled file contains 13 solids and a `69.342 x 69.342 x 40.640 mm` overall box including the flange.
- Historical Concept B and D STEP files successfully reopened. Concept B contains four solids and omits the asserted insert/contact detail; Concept D contains 14 solids and retains a useful three-identical-seat direction.
- Netlist J1 mapping directly rechecked: `/pin1->J1.1`, `/pin2->J1.6`, `/pin3->J1.2`, `/pin4->J1.7`; logic nets map to J3.3/.2/.1/.4 for a0/a1/a2/EN.

### Reusable visual/source material

- Spectrum mechanical drawing embedded in the annotated image is currently the best local carrier-numbering evidence.
- Historical CAD renders clearly document why slide-in slots, COTS LCC sockets, and hidden monolithic clamp hardware fail or need revision.
- Historical FMEA and staged continuity procedures are reusable after remapping to the selected 19-pin feedthrough and corrected LCC map.
- Primary-source seed URLs in `outputs/SOURCE_LEDGER.csv` and historical Sources blocks are discovery leads only; stage 05 must reopen each source and record exact claim support/limitations.

## 6. Missing inputs and acceptance tests

### Wirebond and one-side transition

| Missing input / gate | Required closure |
|---|---|
| Authoritative gen-2 die p1-p4 physical orientation and sign | GDS/runsheet or microscope image with die alignment datum; signed orientation traveler for each carrier |
| Physical LCC chamfer/numbering confirmation and actual same-number shelf-to-castellation continuity | Inspect purchased part and drawing; four-wire continuity check on a sacrificial/empty carrier |
| Die pad metallization, wire alloy/diameter, wedge tool, bond equipment, die attach cure record | Fab traveler and bonder capability statement |
| Continuous-250-deg-C duty duration, cycle count, vacuum pressure, thermal ramps, and magnetic perturbation budget | User/UW design requirement or explicitly conservative qualification envelope |
| Available weld, crimp, braze, and cleaning processes; proposed conductor alloy/insulation | Shop/vendor capability records and material certificates |
| Join acceptance basis | Coupon matrix: aged pull/shear, four-wire resistance, microscopy/intermetallic section, vacuum exposure, thermal cycling, insulation, cleaning/residue/outgassing; unsupported limits labeled `ENGINEERING PROPOSAL - VALIDATE` |

### Boards, feedthrough, DAQ

| Missing input / gate | Required closure |
|---|---|
| 19C-275 mechanical drawing, mated vacuum connector protrusion/diameter, pin material and magnetic response, conductor size, exact continuous-temperature statement | Manufacturer drawing and written vendor confirmation; `HOLD - DO NOT ORDER` until captured |
| HSX assigned-port CF size, bore/envelope datum, allowed mount points, bake profile | UW mechanical confirmation/drawing |
| Actual Pico-to-board and board-to-DAQ cable lengths/types; board rack location | Installation layout |
| Scope/DAQ simultaneous sampling mode, per-channel sample rate/memory, trigger and clock interfaces | Instrument manuals and intended shot configuration |
| J1 custom footprint pad-to-physical-pin and shell-to-GND1 behavior | PCB source/footprint or first-article continuity |
| Board test acceptance | Full 12-wire continuity/channel-swap test; inter-axis insulation; isolated-source fault test; injected bridge signals; simultaneous acquisition/skew; grounding/shield current and crosstalk checks |

### Reusable ceramic head

| Missing input / gate | Required closure |
|---|---|
| Zirconia grade, green/fired tolerances, minimum wall/hole/radius/edge distance, shrinkage control, flatness/orthogonality, post-fire operations | Vendor DFM response and drawing-specific quote |
| 1/3/10-set price and lead time for identical flat seats, monolithic core, and clamshell/cartridge alternatives | Budgetary RFQ; until received all numerical cost ranges are `ENGINEERING PROPOSAL - VALIDATE` |
| Continuous-250-deg-C retained force/contact resistance for candidate spring/contact materials | Same-stack thermal-vacuum life coupons and vendor materials data |
| Full conductor/contact/strain-relief envelope and service-tool sweeps | Dimensioned CAD/drawings including every screw head, nut, tool axis, wire bend, and guard |
| Ceramic/contact acceptance | Dimensional CMM/optical inspection, carrier insertion/removal cycles, contact resistance hot/cold, preload measurement, thermal-vacuum cycling, vibration/handling, independent carrier replacement, post-service calibration repeatability |

## 7. File-level plan for new work

Historical material remains untouched. New work will be limited to `outputs/`, `state/`, and `logs/`:

1. Stage 05: expand `outputs/SOURCE_LEDGER.csv`; write `05_EVIDENCE_AND_CLAIM_MATRIX.md`; update `OPEN_GATES.md`.
2. Stage 10: write the bond/external-join report, two dimensioned SVGs, and qualification CSV; keep the die map orientation-parametric until sign-off evidence exists.
3. Stage 20: write the three-board architecture, complete 12-conductor CSV, end-to-end and ground/shield SVGs, and procurement list with unverified items marked.
4. Stage 30: write three thread-free concepts, dimension/collision and fastener/thread ledgers, per-concept SVG sets, and only dimensionally validated `NOT FOR FABRICATION` CAD under `outputs/cad/`.
5. Stage 40: create an independent findings report and full requirements trace without editing stages 10/20/30.
6. Stage 50: create the final recommendation, acceptance checklist, patch/provenance report, and file index; carry unresolved purchase/fabrication items as `HOLD - DO NOT FABRICATE/ORDER` and declare `COMPLETE_WITH_OPEN_GATES` unless all are closed.

## Stage-00 acceptance check

- Constraints and sources mapped: PASS.
- Retained evidence and CAD inventoried without modification: PASS.
- User proposal and 14/18 conflict captured: PASS.
- Conflicts with the historical pad map exposed: PASS.
- Continuous-250-deg-C invalidations identified: PASS.
- Missing inputs and qualification tests listed: PASS.
- New-output plan preserves `previous_results/`: PASS.
