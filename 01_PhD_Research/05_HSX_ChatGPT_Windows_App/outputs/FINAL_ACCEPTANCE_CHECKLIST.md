# Final acceptance checklist

Date: 2026-07-12  
Package status: **`COMPLETE_WITH_OPEN_GATES`**  
Fabrication/purchase/real-sensor release: **FAIL / HOLD**

Checked boxes mean the engineering-package requirement is objectively present and internally
validated. Empty boxes are release gates; they must be completed with linked evidence before the
stated action. A checked architecture item is not permission to fabricate an unqualified detail.

## A. Project/package completeness

- [x] All governing files, inputs, retained results, netlist, images, PDF and historical CAD were
  inventoried in `00_INVENTORY_AND_GAP_MAP.md`.
- [x] Primary-source claims, exact support and limitations are recorded in
  `05_EVIDENCE_AND_CLAIM_MATRIX.md` and `SOURCE_LEDGER.csv`.
- [x] Wire-bond/join stage completed with orientation gate, alternatives, drawings and a 14-row
  qualification matrix.
- [x] Three-board stage completed with 12 signals, seven spares, six screens, mirror map,
  control/acquisition discussion and pre-power tests.
- [x] Package stage completed with three concepts, 15 drawings, dimension/fastener ledgers and
  real-kernel STEP/STL inspection.
- [x] Separate independent red team completed with 8 BLOCKER, 14 MAJOR, 3 MINOR and 8 NOTE/PASS
  findings; every BLOCKER/MAJOR has a correction and closure test.
- [x] `40_REQUIREMENTS_TRACE.csv` parses as 80 unique requirements: 31 PASS, 27 CONDITIONAL and
  22 FAIL at the Stage-40 baseline.
- [x] Corrected Stage-50 artifacts address the resolvable common-ground, free-nut-reaction and
  undersized-corridor contradictions.
- [x] Required final reports, final maps, drawings, CAD, ledgers, cost basis and qualification plan
  are present and linked in `FINAL_FILE_INDEX.md`.
- [x] Earlier stage markers and `previous_results/` remain preserved as evidence.

## B. Final Question-1 acceptance — die/LCC/fanout

### Architecture/document checks

- [x] Cavity-up view is explicit; chamfer is lower right.
- [x] LCC edge order is top `8..4`, right `3,2,1,20,19`, bottom `14..18`, left `9..13`.
- [x] Physical q map is q1/top->8, q2/right->3, q3/bottom->19, q4/left->14.
- [x] q1-q4 are explicitly not assumed to be p1-p4; all final documents use `P(q)` until sign-off.
- [x] Pad-14/pad-18 inconsistency is resolved as q4->14 plus unordered mirrored-view
  `14<->18` user tie.
- [x] User ties `8<->4`, `3<->9`, `19<->13`, `14<->18` are rejected as the production jumper
  network.
- [x] Final one-side architecture uses same-numbered castellation to protected fanout lane,
  robust permanent pigtail joint, remote service disconnect and independent strain relief.
- [x] Solder is absent from the baseline; 80Au20Sn high-homologous-temperature issue is stated.
- [x] Electrical redundancy and mechanical strain relief are separate.
- [x] Solder, weld, crimp, spring/socket and direct-transition alternatives are compared with
  evidence limits and reversal triggers.

### Release checks — `G50-02`

- [ ] Authoritative die GDS/runsheet or signed microscope evidence identifies physical p1-p4 and
  sign convention.
- [ ] Incoming LCC cavity-up/chamfer and 1-20 shelf-to-castellation continuity pass for the actual
  purchased lot.
- [ ] Actual die-pad, LCC finish, 353ND lot/mix/bondline/cure, Al wire/tool/program and no-mirror
  traveler are frozen.
- [ ] Same-stack continuous-250-deg-C UHV die-attach and Al-bond aging passes resistance,
  pull/shear, fracture-mode, cross-section, contamination and drift endpoints.
- [ ] Exact no-Ni fanout ceramic/metallization/finish and short microtransition process pass DOE
  and aging.
- [ ] Exact robust pigtail weld or crimp wins resistance/pull/cross-section/aging/cleanliness tests.
- [ ] Measured loop/heel envelope, guard clearance, comb and handling jig pass thermal sweep and
  service tests.
- [ ] Complete serialized cartridge passes hot-vacuum, magnetic, proof-load, continuity and
  isolation qualification.

Current Q1 release: **HOLD - DO NOT BOND / DO NOT RELEASE CARTRIDGE**.

## C. Final Question-2 acceptance — three-board system

### Architecture/map checks

- [x] Final map contains exactly 12 signal rows, seven spare rows and six shield rows.
- [x] Signal/spare rows occupy V1-V19 and A1-A19 exactly once.
- [x] Mirror permutation is preserved: 1; 2<->12; 3<->11; 4<->10; 5<->9; 6<->8; 7;
  13<->14; 15<->18; 16<->17; 19.
- [x] J1 mapping is p1/p3/p2/p4 = 1/2/6/7 for X/Y/Z.
- [x] Six screens use no feedthrough signal pin and terminate at flange/chassis only.
- [x] No shared return crosses the feedthrough.
- [x] Stage-20 common `AGND_STAR`/grounded-BNC baseline is explicitly superseded.
- [x] Final domains are GND1_X, GND1_Y and GND1_Z with no intentional DC tie.
- [x] Shared vs independent power, timing, control, acquisition, shielding, calibration and fault
  boundaries are explicit.
- [x] One four-line galvanic control barrier and one isolated/differential measurement path are
  required per board.
- [x] One floating/reversing 100-uA source is required per domain.
- [x] Three simultaneous isolated/differential channels plus sync and an aperture-skew test are
  required.
- [x] Eight-phase rates are corrected: 40/80/100/160 kHz -> 5/10/12.5/20 kS/s updates.
- [x] KAP301 capacitance and cable-length settling are included in the final validation scope.

### Release checks — `G50-03/G50-06`

- [ ] Accu-Glass/UW exact 19C configuration, mated geometry, views, wire/contact range,
  continuous-duty interpretation, magnetic acceptance, cleaning and port datum are signed.
- [ ] First-article V1-V19 vacuum-to-air continuity permutation is photographed and independently
  verified before contact lock.
- [ ] Exact six two-pair branches, screens, length/OD/lay/bend/capacitance/termination and 3.80-mm
  corridor fit pass.
- [ ] Three exact isolated 100-uA sources pass accuracy/noise/compliance/reversal/fault-energy and
  channel/chassis isolation.
- [ ] X/Y/Z approximately 109-times anomaly is root-caused and all three boards pass injected
  delta-V gain/polarity/linearity/phase tests.
- [ ] Exact control barriers pass OE/power-order, VIH/VIL, R5-R8, cable-C, series-R, ringing,
  threshold-recrossing, skew and settling tests.
- [ ] Exact isolated/differential simultaneous DAQ passes input/noise/common-mode/isolation,
  common-edge aperture-skew and three-emulator-plus-sync capture tests.
- [ ] With every normal supply/control/DAQ/probe/USB/shield cable installed, GND1_X/Y/Z have no
  intentional DC continuity and pass signed leakage/capacitance/fault limits.
- [ ] Facility protective-earth/chassis survey proves no undocumented domain bridge.

Current Q2 release: **HOLD - DO NOT TERMINATE / DO NOT CONNECT REAL SENSORS**.

## D. Final Question-3 acceptance — reusable ceramic package

### Architecture/kernel checks

- [x] Corrected Concept A uses three identical flat zirconia seats.
- [x] Unique ceramic geometry count is one; seat quantity is three.
- [x] Tapped/internal zirconia thread count is zero.
- [x] No bonded inserts, hidden nuts, crossing bolts or blind zirconia traps are in the baseline.
- [x] Connected base/backframe/nut-reaction cage is one kernel solid.
- [x] Six replaceable nut plates contact the connected reaction lips at zero modeled distance.
- [x] Nut keepers are outside the primary clamp load path.
- [x] Physical load path bypasses all electrical joints.
- [x] Corrected branch corridor is 3.80 mm versus 3.30-mm two-pair worst delivered OD arithmetic.
- [x] Hard envelope model passes: radius 14.354 mm and height 26.750 mm.
- [x] Proposed worst bounds pass arithmetically: radius 14.566 mm and height 27.160 mm.
- [x] Complete physical pairwise overlap is 0.000000 mm3.
- [x] STEP re-import returns 39 valid solids and 0.000000-mm bounding delta.
- [x] Feedthrough provisional keepout arithmetic passes with explicit interface hold.
- [x] Straight +X/+Y/+Z tool directions and negative-edge hardware are shown.
- [x] Each cartridge can be removed without removing either neighboring cartridge at concept level.
- [x] Reusable/sacrificial boundaries and connection remate sequence are explicit.
- [x] Proposed post-fire operations are stated; none includes tapping.
- [x] 1/3/10-set cost basis and NRE/Q formula are explicit without invented prices.
- [x] Monolithic B and split-cassette C remain quoted alternatives with reversal triggers.

### Release checks — `G50-04/G50-05`

- [ ] Zirconia vendor approves exact grade/process, fired/post-ground operations, radii/webs/edges,
  tolerances/GD&T, flatness/orthogonality, cleaning, inspection, yield and 1/3/10 quotes.
- [ ] Actual LCC body material, dimensions, warpage and cartridge/guard stack are measured.
- [ ] Exact CP-Ti grade/form/heat treatment/finish, cage process and delivered magnetic behavior
  are frozen.
- [ ] Exact flexure/hard-stop/contact-pad geometry passes FEA/contact stress and 20/250-deg-C
  force-displacement/dwell/cycle tests.
- [ ] Exact screws, vented nut plates, keepers/retainers, post attachment and strain hardware pass
  UHV cleaning, galling, particles, reuse, proof-load and magnetic tests.
- [ ] Every faying/nut/post interface has a released open vent path and passes borescope/pump-down
  review.
- [ ] Exact cable/lay/bend/clip geometry replaces keepouts in regenerated complete assembly CAD.
- [ ] Production CAD contains every installed part, datums/GD&T, vendor radii, materials and a
  closed hot/cold tolerance stack.
- [ ] Production assembly passes full envelope, contact/connectivity graph, collision, tool, cable
  bend and service-motion audit.
- [ ] X/Y/Z independent service demonstration passes with adjacent instrumented bonds and
  particle/calibration checks.

Current Q3 release: **HOLD - DO NOT FABRICATE CERAMIC/RETENTION OR ISSUE PRODUCTION CAD**.

## E. Cross-domain continuous-life and magnetic release

- [ ] `G50-01` signed service/error envelope exists: duration, ramps/cycles, UHV/outgassing,
  magnetic, bandwidth/noise/drift, proof load/shock, insulation and service limits.
- [ ] No material/component is accepted solely from catalog maximum or bake survival.
- [ ] Complete in-vessel stack passes signed continuous-250-deg-C UHV exposure, not only component
  coupons.
- [ ] Exact feedthrough Ni-Fe/contact assembly and every near-sensor alloy/finish are screened to
  the signed magnetic budget before and after bake.
- [ ] Complete head passes three-axis field-map/background test.
- [ ] Hot 3x3 vector calibration passes at 20/250 deg C and after bake/service.
- [ ] Cleaning, chamber blanks/witnesses, pressure/outgassing/contamination and particles pass the
  vacuum-owner criteria.

Current cross-domain release: **HOLD - DO NOT ORDER NEAR-SENSOR HARDWARE / DO NOT CLAIM PERFORMANCE**.

## F. Final artifact consistency audit

- [x] Final LCC drawing and report agree on q1/q2/q3/q4 -> 8/3/19/14.
- [x] Final artifacts use cavity-up, lower-right chamfer and `14<->18`; no final artifact fixes
  p1-p4 without P(q) sign-off.
- [x] Final report, interface CSV and map drawing agree on V1-V12, A mirror and J1 pins.
- [x] Final report/domain CSV/readout drawing agree on isolated GND1_X/Y/Z and forbid common BNC.
- [x] Final report/dimension CSV/CAD report/package drawing agree on 14.354-mm radius,
  26.750-mm height, 3.80-mm corridor, one cage solid, six contacts and zero overlap.
- [x] Final report/fastener CSV/package drawing agree on zero ceramic threads, one ceramic geometry,
  external +X/+Y/+Z access and replaceable nut hardware.
- [x] Final cost report and CSV make no unsupported price claim.
- [x] All unverified fabrication/purchase details carry explicit HOLD language.
- [x] `FINAL_PATCH_AND_PROVENANCE.md` identifies every controlling supersession.
- [x] `FINAL_FILE_INDEX.md` lists all reports, CSVs, SVGs, STEP/STL and generator/report files.

## G. Release sign-off block

The following must all be checked before state may change from `COMPLETE_WITH_OPEN_GATES`:

- [ ] G50-01 service/error envelope closed with document ID: ____________________
- [ ] G50-02 bonded cartridge closed with qualification report: ____________________
- [ ] G50-03 19C/cable interface closed with ICD/traveler: ____________________
- [ ] G50-04 zirconia/production CAD closed with drawing release: ____________________
- [ ] G50-05 retention/fastener/service closed with report: ____________________
- [ ] G50-06 isolated electronics/DAQ/anomaly closed with report: ____________________
- [ ] G50-07 magnetic/calibration closed with report: ____________________
- [ ] G50-08 independent final configuration review minutes: ____________________

Engineering: ____________________  Date: __________  
Vacuum owner: ____________________  Date: __________  
Electrical/DAQ: ____________________  Date: __________  
Packaging/ceramic: ____________________  Date: __________  
Independent reviewer: ____________________  Date: __________

Current final disposition: **`COMPLETE_WITH_OPEN_GATES` — `HOLD - DO NOT FABRICATE/ORDER`**.
