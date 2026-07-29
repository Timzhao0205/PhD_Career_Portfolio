# Final patch and provenance record

Date: 2026-07-12  
Final state: `COMPLETE_WITH_OPEN_GATES`

This record distinguishes retained evidence from new engineering work and identifies every final
supersession. `previous_results/` was treated as read-only historical evidence and was not edited.

## 1. Provenance hierarchy

When sources disagree, the final package uses this order:

1. binding project constraints in `AGENTS.md`, `MISSION.md` and authoritative input specifications;
2. physical inspection/continuity/CMM evidence for the actual serialized hardware;
3. current manufacturer drawings/data and active standards;
4. live board netlist/BOM and reproducible CAD-kernel calculations;
5. peer-reviewed/government evidence with explicit transfer limitations;
6. engineering proposals carrying validation gates;
7. retained historical results as hypotheses/context only.

No historical confidence score is used to hide missing fabrication or life evidence.

## 2. Retained inputs and historical evidence used

| Retained item | Data reused | Verification/restriction in final package |
|---|---|---|
| user annotated LCC routing image | physical red q locations and proposed shelves 8/3/19/14; green route labels | re-opened at original resolution; reconciled cavity-up and mirrored bottom views; p identity remains unknown |
| Spectrum LCC02046 drawing | body/pad layout, chamfer and numbering framework | live primary drawing reopened; same-lot physical continuity still required |
| project hardware data | J1 convention p1/p3/p2/p4 = 1/2/6/7; board component/net values | checked against live `hsx_2026_v2.net`; physical footprint/shell remains first-article gate |
| live board netlist | GND1, R2/R3, mux/amplifier/control connections | controlling evidence for rejecting common GND1; no historical topology claim overrides it |
| 2023 paper/input PDF | Hall/readout experiment context | used for context, not as package or continuous-life qualification |
| envelope specification | 31.75-mm diameter by 27.5-mm height; 19C context | hard bound retained; exact mated feedthrough/UW datum remains held |
| user/reference STEP files | existing package/feedthrough geometry and concept scale | opened with OpenCascade; treated as reference, not released geometry |
| historical connection/fanout/flange/wiring reports | candidate maps, board plan, connector views and failure hypotheses | claims re-derived from primary sources/netlist; conflicting or unsupported claims were rejected |
| historical package renders/STEP concepts | alternative packaging ideas and user priorities | PEEK/BeCu/hidden-thread assumptions rejected; geometry not copied as production CAD |
| retained 109-times anomaly observations | known board inconsistency | preserved as a real-sensor power blocker; no speculative root cause declared |

## 3. Primary evidence captured or reverified

`SOURCE_LEDGER.csv` contains 55 unique direct URLs with exact support and limitations. Critical
families reopened during the workflow include:

- Spectrum LCC02046 drawing/product information;
- EPO-TEK 353ND data and NASA outgassing context;
- DLA MIL-STD-883 bond-pull framework;
- SINTEF 250-deg-C Al/thin-Au bond-aging evidence and NASA degradation caution;
- Accu-Glass 19C drawing, 19C-275 product data and wiring/contact catalogs;
- Allectra KAP301 drawing/data;
- TI SN74LVC125A, Analog Devices muxes, RECOM RS6 and Keysight DSOX1204G;
- TIMET CP-Ti and Kyocera zirconia representative material data;
- vacuum fastener/venting geometry evidence.

Limitations are carried forward. Examples:

- maximum operating/bake temperature is not continuous-life qualification;
- general Al/Au aging evidence is not qualification of the exact die/LCC/adhesive/fanout stack;
- the 19C drawing's rear pattern is usable evidence, while its “9C” caution text is not treated as
  definitive proof of a 19-circuit permutation;
- DSOX1204G channel count/sample-rate data do not establish galvanic channel isolation or the
  required aperture skew;
- representative CP-Ti/zirconia properties do not establish flexure life or vendor DFM.

## 4. Stage-to-final lineage

| Final subject | Supporting stage evidence | Final controlling artifact |
|---|---|---|
| input gaps and immutable constraints | `00_INVENTORY_AND_GAP_MAP.md` | final report sections 1-2 and G50 gates |
| source claims/limitations | `05_EVIDENCE_AND_CLAIM_MATRIX.md`, source ledger | final report evidence language and qualification holds |
| physical LCC mapping and joining alternatives | Stage-10 marker, drawings and qualification CSV | `FINAL_RECOMMENDATION_250C_UHV.md`; `drawings/50_final_lcc_and_pin_map.svg` |
| 12-conductor map and board interfaces | Stage-20 marker/CSV/drawings | `50_FINAL_INTERFACE_MAP.csv` |
| three package concepts and original bounds | Stage-30 marker/CAD/drawings/ledgers | alternatives section; not released geometry |
| independent failure findings | Stage-40 review and requirements trace | final correction set, checklist and consolidated G50 gates |
| corrected ambient architecture | F40-B01/D40-01 | `50_FINAL_AMBIENT_DOMAIN_MAP.csv`; isolated-readout SVG |
| corrected package topology | F40-B05/D40-02 plus new kernel iteration | `cad/50A_FINAL_NFF.step`; final dimension/fastener ledgers; package SVG |
| corrected harness corridor | F40-B06/D40-03 | 3.80-mm keepout STEP and final dimension ledger |
| final release sequence | all findings/gates | `50_FINAL_QUALIFICATION_AND_BUILD_PLAN.csv`; checklist |
| cost/reuse decision | binding priorities plus Stage-30 trade evidence | `50_FINAL_COST_BASIS_1_3_10.csv`; no unsupported prices |

## 5. Controlling corrections made after red team

### P50-01 — common ground replaced by three isolated domains

Earlier Stage-20 recommendation intentionally commoned the three GND1 nodes at an ambient star
because grounded oscilloscope shells would do so. Stage 40 proved this violates the binding sensor
electrical-isolation requirement: the live netlist references selected inputs to GND1 through
R2/R3=2.2 kohm, creating an inter-axis path of approximately `2.2k + 2.2k + mux Ron`.

Final correction:

- separate GND1_X/Y/Z;
- one four-line galvanic control barrier per board;
- one isolated current-source domain per board;
- one isolated/differential measurement path per board;
- one timebase after isolation;
- direct common BNC/AGND/USB/probe cross-ties forbidden.

Exact parts and all-cables isolation remain `G50-06`, but the functional contradiction is removed
from the controlling architecture.

### P50-02 — free nut pads replaced by a connected reaction cage

Stage-30 A/B CAD created separate nut-pad solids; zero overlap did not prove structural capture or
a base-connected load path. The final generator adds:

- one fused CP-Ti base/backframe/reaction cage;
- four continuous reaction rails reaching all six face-screw sites;
- six open-sided replaceable nut-plate pockets;
- outward reaction lips and external keeper envelopes;
- seat backframes and diagonal post spokes;
- primary load path independent of electrical joints.

Kernel result: one cage solid, six zero-distance nut reaction contacts, zero unintended pairwise
overlap, 39 valid re-imported solids. Exact keeper/flexure/hardware production design remains
`G50-05`.

### P50-03 — complete physical collision scope expanded

The corrected CAD initially exposed interferences omitted from Stage-30 critical-pair checks:

- bridge/base into the low side-cartridge service volume;
- L-shaped post spokes into side clamps;
- side/top backframe overlap at shared seat edges;
- strain clips into reaction rails;
- an incomplete top bolt clearance cut;
- one top nut pocket width mismatch.

The generator was iterated with open base reliefs, diagonal corner spokes, trimmed backframes,
relocated strain axes, extended through-clearance and corrected nut-pocket orientation. The final
collision audit includes cage, seats, cartridges, clamps, six bolts, six nuts, six keepers and six
strain parts—not only selected critical pairs.

### P50-04 — cable corridor increased from 3.00 to 3.80 mm

KAP301 worst delivered OD is 1.65 mm. Two pairs require 3.30 mm before installation clearance;
the earlier 3.00-mm square corridor failed. Final CAD reserves 3.80 mm, leaving 0.50 mm total
width allowance. This is a corrected sizing rule, not a released cable fit; delivered lay, bend,
abrasion, clamp and hot-vacuum testing remain `G50-03`.

### P50-05 — 14/18 normalized without fixing p identity

The original annotation contains cavity-up and mirrored bottom views. Final artifacts use q4->14
and normalize the passive user route as `14<->18`. They do not use a directional `18->14` as a
second inner pad and do not infer p1-p4. The final drawing also corrects the physical q3 bond to
shelf 19 and q4 to shelf 14.

### P50-06 — cost score demoted to quote-dependent trade

Stage-30 A=96/B=81/C=77 used the binding weight order but lacked comparable quotes and preceded
hard-gate failures. The final package retains A as a preferred procurement direction only. It
uses drawing-specific 1/3/10 RFQs and the formula `NRE/Q + recurring + labor + inspection +
yield/scrap + spares`, with qualification cost reported separately.

### P50-07 — performance claim tied to phase cadence and isolated DAQ

Eight phases produce update `f_phase/8`: 40/80/100/160 kHz becomes 5/10/12.5/20 kS/s. The final
package makes no 20-kHz recombined claim from 40 kHz and requires final cable/isolator/DAQ
settling, noise, skew and demodulation evidence.

## 6. Final CAD provenance and reproducibility

Generator: `cad/50_final_corrected_package.py`  
Kernel: build123d/OpenCascade available in the local workspace  
Outputs:

- `cad/50A_FINAL_NFF.step` — complete corrected physical assembly;
- `cad/50A_CERAMIC_NFF.stl` — three-seat ceramic concept mesh;
- `cad/50A_HARNESS_KEEPOUTS_NFF.step` — three corrected cable keepouts;
- `cad/50_CAD_KERNEL_REPORT.txt` — controlling bound/connectivity/contact/collision/reimport log.

The generator is idempotent for its final filenames and reimports its own STEP/STL. The report
records:

- physical bbox x/y +/-10.150 mm; z 0.000 to 26.750 mm;
- conservative radius 14.354 mm;
- one connected cage solid;
- six nut contacts at 0.000000 mm;
- zero unintended overlap;
- feedthrough provisional keepout pass;
- STEP reimport bound delta 0.000000 mm;
- ceramic thread count zero and unique ceramic geometry count one.

All files carry NOT-FOR-FABRICATION status because production tolerances, materials, force and
vendor interfaces remain held.

## 7. Artifact edits and preservation

Stage-40 work did not edit accepted Stage-10, Stage-20 or Stage-30 markers/drawings/CAD. Stage-50
created new `50_*` and `FINAL_*` artifacts and appended consolidated gates; it did not rewrite the
earlier records to make them appear prescient. This preserves the audit trail:

- Stage 20 documents the rejected common-ground decision;
- Stage 30 documents the incomplete conceptual nut-pad/corridor model;
- Stage 40 records the independent findings;
- Stage 50 records explicit corrections and remaining holds.

`previous_results/` remains unchanged. Local Git commits provide an additional checkpoint layer;
the files/state checkpoints remain authoritative for recovery.

## 8. Remaining uncertainty and non-transferable claims

The following are not resolved by the final architecture:

- authoritative die p1-p4 orientation and actual LCC lot continuity/finish;
- exact continuous-250-deg-C UHV life of die attach, Al bonds, fanout and complete cartridge;
- exact 19C configuration, continuous-duty interpretation, magnetics and UW installed datum;
- exact cable, bend, termination, screen clamp and hot-vacuum fit;
- zirconia vendor process/tolerances/GD&T/yield/quotes;
- CP-Ti flexure force/life, contact stress, galling, particles, keeper and lower post detail;
- exact isolated current sources, control barriers and simultaneous acquisition;
- root cause of the approximately 109-times anomaly;
- numerical magnetic/error/service envelope and integrated qualification.

These are consolidated as G50-01 through G50-08 and are explicitly not converted into implied
confidence. The controlling final state is `COMPLETE_WITH_OPEN_GATES`.
