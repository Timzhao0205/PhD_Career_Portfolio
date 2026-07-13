# Final file index

Date: 2026-07-12  
Package state: `COMPLETE_WITH_OPEN_GATES`

This index lists every report, CSV, SVG and CAD artifact under `outputs/`. Stage files are design
and audit history. `50_*` and `FINAL_*` files are the controlling corrected synthesis where they
disagree with earlier stages. Every STEP/STL remains NOT FOR FABRICATION.

## 1. Controlling final reports

| File | Purpose | Control status |
|---|---|---|
| [FINAL_RECOMMENDATION_250C_UHV.md](FINAL_RECOMMENDATION_250C_UHV.md) | direct answers to the three mission questions; final bond/join, isolated boards, corrected package, alternatives, build/cost/qualification/gates | controlling recommendation |
| [FINAL_ACCEPTANCE_CHECKLIST.md](FINAL_ACCEPTANCE_CHECKLIST.md) | package-completeness and fabrication/purchase/power release checklist | controlling release state |
| [FINAL_PATCH_AND_PROVENANCE.md](FINAL_PATCH_AND_PROVENANCE.md) | retained evidence, new work, supersessions, CAD provenance and unresolved limits | controlling lineage |
| [FINAL_FILE_INDEX.md](FINAL_FILE_INDEX.md) | complete report/CSV/SVG/CAD index | this file |
| [OPEN_GATES.md](OPEN_GATES.md) | cumulative G00-G50 gate history | controlling open-gate register; G50 consolidates release effects |

## 2. Stage reports and independent audit

| File | Purpose | Status |
|---|---|---|
| [00_INVENTORY_AND_GAP_MAP.md](00_INVENTORY_AND_GAP_MAP.md) | full input/historical inventory, constraints, conflicts and missing inputs | accepted Stage 00 evidence |
| [05_EVIDENCE_AND_CLAIM_MATRIX.md](05_EVIDENCE_AND_CLAIM_MATRIX.md) | source-audited verified/conditional/rejected claim matrix | accepted Stage 05 evidence |
| [10_LCC_WIREBOND_AND_EXTERNAL_JOIN.md](10_LCC_WIREBOND_AND_EXTERNAL_JOIN.md) | orientation-parametric LCC map, join concepts, selected cartridge fanout and qualification | accepted Stage 10 evidence |
| [20_THREE_BOARD_READOUT_ARCHITECTURE.md](20_THREE_BOARD_READOUT_ARCHITECTURE.md) | original board/pin/DAQ architecture and tests | accepted Stage 20 history; common-GND1 section superseded by final isolated domains |
| [30_REUSABLE_3D_PACKAGE_250C_UHV.md](30_REUSABLE_3D_PACKAGE_250C_UHV.md) | A/B/C package trade, original dimensions, service, DFM and scoring | accepted Stage 30 history; A/B reaction/corridor geometry superseded by final CAD |
| [40_INDEPENDENT_RED_TEAM.md](40_INDEPENDENT_RED_TEAM.md) | independent cross-domain findings, recalculations, corrections and closure tests | accepted Stage 40 audit |

## 3. Source and requirements ledgers

| File | Rows / scope | Status |
|---|---|---|
| [SOURCE_LEDGER.csv](SOURCE_LEDGER.csv) | 55 unique primary-source URLs with exact support and limitations | controlling source ledger |
| [40_REQUIREMENTS_TRACE.csv](40_REQUIREMENTS_TRACE.csv) | 80 requirements; Stage-40 PASS/CONDITIONAL/FAIL mapping | controlling audit trace |

## 4. Bond, pin and ambient-domain CSVs

| File | Scope | Status |
|---|---|---|
| [10_BOND_AND_JOIN_QUALIFICATION.csv](10_BOND_AND_JOIN_QUALIFICATION.csv) | 14 incoming/coupon/aging/service/identity qualification tests | supporting detailed bond plan |
| [20_PIN_AND_CABLE_MAP.csv](20_PIN_AND_CABLE_MAP.csv) | original 25-row signal/spare/shield map | accepted history |
| [50_FINAL_INTERFACE_MAP.csv](50_FINAL_INTERFACE_MAP.csv) | controlling 12 signal + 7 spare + 6 shield map with P(q), V/A, J1 and domain rules | controlling final map |
| [50_FINAL_AMBIENT_DOMAIN_MAP.csv](50_FINAL_AMBIENT_DOMAIN_MAP.csv) | GND1_X/Y/Z power/current/control/acquisition isolation boundaries | controlling final board topology |

## 5. Package, cost and qualification CSVs

| File | Scope | Status |
|---|---|---|
| [30_DIMENSION_AND_COLLISION_LEDGER.csv](30_DIMENSION_AND_COLLISION_LEDGER.csv) | original A/B/C 57-row dimension/collision ledger | Stage-30 history |
| [30_FASTENER_AND_THREAD_SCHEDULE.csv](30_FASTENER_AND_THREAD_SCHEDULE.csv) | original 17-row concept fastener schedule | Stage-30 history; free-nut architecture superseded |
| [50_FINAL_DIMENSION_AND_RELEASE_LEDGER.csv](50_FINAL_DIMENSION_AND_RELEASE_LEDGER.csv) | 38 corrected dimensions, calculations and release holds | controlling final geometry ledger |
| [50_FINAL_FASTENER_AND_THREAD_SCHEDULE.csv](50_FINAL_FASTENER_AND_THREAD_SCHEDULE.csv) | corrected connected-cage/replaceable-nut schedule; zero ceramic threads | controlling final hardware rule |
| [50_FINAL_COST_BASIS_1_3_10.csv](50_FINAL_COST_BASIS_1_3_10.csv) | 1/3/10-set RFQ quantities and NRE/recurring/yield/qualification accounting | controlling cost basis; no price claims |
| [50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv](50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv) | 19 ordered entry/evidence/pass/fail gates | controlling build/qualification order |

## 6. Controlling final SVG drawings

| File | Content | Status |
|---|---|---|
| [drawings/50_final_lcc_and_pin_map.svg](drawings/50_final_lcc_and_pin_map.svg) | cavity-up LCC q->8/3/19/14, P(q) hold, 14/18 resolution, final V/A/J1 map | controlling final electrical map view |
| [drawings/50_final_isolated_readout.svg](drawings/50_final_isolated_readout.svg) | three GND1_X/Y/Z isolation domains, shared-side resources and forbidden cross-ties | controlling final board view |
| [drawings/50_final_corrected_package.svg](drawings/50_final_corrected_package.svg) | corrected connected cage, cable corridors, load path, service axes and disclosures | controlling final package view; not manufacturing drawing |

## 7. Stage-10 and Stage-20 SVG drawings

| File | Content | Status |
|---|---|---|
| [drawings/10_lcc_recommended_top.svg](drawings/10_lcc_recommended_top.svg) | original accepted cavity-up physical LCC map | supporting history |
| [drawings/11_lcc_external_exit.svg](drawings/11_lcc_external_exit.svg) | protected one-side fanout/pigtail concept | supporting final join direction |
| [drawings/20_end_to_end_block.svg](drawings/20_end_to_end_block.svg) | original 12-conductor three-board block diagram | pin-map history; grounding superseded |
| [drawings/21_ground_and_shield.svg](drawings/21_ground_and_shield.svg) | original AGND_STAR/shield drawing | explicitly superseded by final isolated-readout SVG |

## 8. Stage-30 Concept-A SVG set

| File | View | Status |
|---|---|---|
| [drawings/30A_top_envelope.svg](drawings/30A_top_envelope.svg) | original A top/envelope | concept history |
| [drawings/30A_section.svg](drawings/30A_section.svg) | original A section | concept history; reaction topology superseded |
| [drawings/30A_isometric_exploded.svg](drawings/30A_isometric_exploded.svg) | original A exploded view | concept history |
| [drawings/30A_fastener_axes.svg](drawings/30A_fastener_axes.svg) | original A tool/fastener axes | supporting negative-edge rule |
| [drawings/30A_contact_detail.svg](drawings/30A_contact_detail.svg) | original A contact/load detail | concept history; exact retention held |

## 9. Stage-30 Concept-B SVG set

| File | View | Status |
|---|---|---|
| [drawings/30B_top_envelope.svg](drawings/30B_top_envelope.svg) | monolithic-core top/envelope | quoted alternative history |
| [drawings/30B_section.svg](drawings/30B_section.svg) | monolithic-core section | quoted alternative history |
| [drawings/30B_isometric_exploded.svg](drawings/30B_isometric_exploded.svg) | monolithic-core exploded view | quoted alternative history |
| [drawings/30B_fastener_axes.svg](drawings/30B_fastener_axes.svg) | monolithic-core tool axes | quoted alternative history |
| [drawings/30B_contact_detail.svg](drawings/30B_contact_detail.svg) | monolithic-core contact detail | quoted alternative history |

## 10. Stage-30 Concept-C SVG set

| File | View | Status |
|---|---|---|
| [drawings/30C_top_envelope.svg](drawings/30C_top_envelope.svg) | split-cassette top/envelope | service alternative history |
| [drawings/30C_section.svg](drawings/30C_section.svg) | split-cassette section | service alternative history |
| [drawings/30C_isometric_exploded.svg](drawings/30C_isometric_exploded.svg) | split-cassette exploded view | service alternative history |
| [drawings/30C_fastener_axes.svg](drawings/30C_fastener_axes.svg) | split-cassette pin/tool axes | service alternative history |
| [drawings/30C_contact_detail.svg](drawings/30C_contact_detail.svg) | split-cassette contact detail | service alternative history |

SVG generator: [drawings/30_make_package_svgs.py](drawings/30_make_package_svgs.py) reproduces the
Stage-30 SVG set; it is not the final corrected package generator.

## 11. Controlling corrected CAD

| File | Content | Validation/status |
|---|---|---|
| [cad/50_final_corrected_package.py](cad/50_final_corrected_package.py) | parametric corrected Concept-A generator and checks | controlling reproducible generator |
| [cad/50_CAD_KERNEL_REPORT.txt](cad/50_CAD_KERNEL_REPORT.txt) | bounds, cage connectivity, nut contact, collision, keepout and reimport report | controlling CAD calculation record |
| [cad/50A_FINAL_NFF.step](cad/50A_FINAL_NFF.step) | corrected 39-solid physical assembly | OpenCascade reimport valid; NOT FOR FABRICATION |
| [cad/50A_CERAMIC_NFF.stl](cad/50A_CERAMIC_NFF.stl) | three identical-seat ceramic concept mesh | nonempty/bounds inspected; NOT FOR FABRICATION |
| [cad/50A_HARNESS_KEEPOUTS_NFF.step](cad/50A_HARNESS_KEEPOUTS_NFF.step) | three 3.80-mm branch keepout volumes | included in envelope check; NOT FOR FABRICATION |

## 12. Stage-30 CAD and reports

| File | Content | Status |
|---|---|---|
| [cad/30_package_concepts.py](cad/30_package_concepts.py) | original A/B/C generator | historical; critical-pair scope and free nut pads superseded |
| [cad/30_CAD_KERNEL_REPORT.txt](cad/30_CAD_KERNEL_REPORT.txt) | original A/B/C bounds/reimport report | historical calculation evidence |
| [cad/30A_triplate_cage_NOT_FOR_FABRICATION.step](cad/30A_triplate_cage_NOT_FOR_FABRICATION.step) | original Concept-A assembly | historical NFF; do not fabricate |
| [cad/30A_triplate_cage_ceramic_NOT_FOR_FABRICATION.stl](cad/30A_triplate_cage_ceramic_NOT_FOR_FABRICATION.stl) | original A ceramic mesh | historical NFF |
| [cad/30B_monolithic_core_NOT_FOR_FABRICATION.step](cad/30B_monolithic_core_NOT_FOR_FABRICATION.step) | original Concept-B assembly | historical NFF |
| [cad/30B_monolithic_core_ceramic_NOT_FOR_FABRICATION.stl](cad/30B_monolithic_core_ceramic_NOT_FOR_FABRICATION.stl) | original B ceramic mesh | historical NFF |
| [cad/30C_split_cassette_NOT_FOR_FABRICATION.step](cad/30C_split_cassette_NOT_FOR_FABRICATION.step) | original Concept-C assembly | historical NFF |
| [cad/30C_split_cassette_ceramic_NOT_FOR_FABRICATION.stl](cad/30C_split_cassette_ceramic_NOT_FOR_FABRICATION.stl) | original C ceramic mesh | historical NFF |

## 13. External retained evidence

Inputs are under `inputs/`; historical processed work is under read-only `previous_results/`.
Those trees are inventoried in `00_INVENTORY_AND_GAP_MAP.md` rather than duplicated here. The
source URLs and limitations are in `SOURCE_LEDGER.csv`.

## 14. Use warning

The presence of a STEP, STL, SVG or dimension does not close its associated release gate. Use
`FINAL_ACCEPTANCE_CHECKLIST.md` and G50-01 through G50-08 before any bond, fabrication, purchase,
installation, real-sensor power or performance statement.
