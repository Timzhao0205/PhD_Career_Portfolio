# P3R2 fix-application log

Applied 2026-07-13 by the Fable 5/xhigh fix-application agent (claude-fable-5, effort xhigh), implementing `P3R2_ELEGANCE_ADJUDICATION.json` rulings across the five seed batches (JSON + MD). No seed records were deleted; rejects and merged seeds remain as audit trail.

## Verdict marking (all 100 seeds)

- 21 seeds marked `PROMOTE`.
- 23 FIX seeds edited in place and marked `FIX_APPLIED`: A-03, A-11, A-16, B-06, B-14, B-22, C-02, C-03, C-04, C-12, C-13, C-19, C-21, D-07, D-08, D-11, D-12, D-16, D-18, D-19, D-20, E-02, E-11.
- 2 FIX seeds whose required fix WAS a merge: B-21 -> `MERGED_INTO_P3R2-A-10`, C-20 -> `MERGED_INTO_P3R2-C-09` (their unique content imported into the canonicals).
- 14 named-alternate duplicates marked `MERGED_INTO_<canonical>` with content imported: A-01/E-01 -> C-01; C-06 -> A-10; D-05 -> C-09; C-11 -> D-02; A-04/E-07 -> D-01 (E-07 split-imported to D-01 and D-02); A-15/B-02 -> C-05; E-09/D-14 -> A-14; E-10/D-15 -> A-13; C-16 -> E-14.
- 31 remaining duplicates marked `REJECT` with `duplicate_of`; judge-specified unique content imported into their canonicals (B-03/B-04 -> C-01; B-05/E-03 -> A-10; A-12/B-07/E-08 -> C-08; A-07/B-09/E-05 -> C-09; A-08 -> D-09 (C-10 fake-dual: nothing imported); A-09 -> D-08; C-17 -> D-01; B-10 -> D-02; B-11/D-03 -> C-12; B-12 -> A-05 (nothing importable); A-06/D-17 -> E-04; A-18/B-19 -> C-13; A-17 -> D-10; A-19/B-13 -> C-07; C-15 -> A-21; B-17 -> A-14 (CN chapter kept out); E-12 -> D-18 (upside only); B-18 -> D-19 (license-note only); E-13 -> D-11; B-08 -> C-19).
- 9 pure rejects marked `REJECT` (A-20, E-06, B-15, B-16, B-20, C-14, C-18, D-04, D-06).
- Every seed also carries `adjudication_note` quoting the judge's reasoning.

## China-flag changes (honesty rule applied)

- **P3R2-A-10**: primary_market US -> US+CN, china_beachhead false -> true. The imported CN leg (B-05/C-06) is independent and cited to eligible CN evidence (L06-042/043/044/048/054); conditions documented: mature-node (>=28nm) scope only, two-entity export partition, 2027 export-counsel gate.
- **P3R2-C-12**: primary_market US+CN -> US, china_beachhead true -> false. Judge required license-only CN participation (quantum-adjacent export exposure); CN chapter kept in text.
- **P3R2-C-21**: primary_market US+CN -> US, china_beachhead true -> false. Judge required license-out-only CN participation (Sungrow/Huawei incumbency); CN policy leg kept in text. v1 capex also capped $12-30M -> $10-25M.
- Endorsed licensed-CN-leg canonicals C-01, C-05, C-07, C-08, C-09, D-02 were already US+CN with china_beachhead true and independent CN evidence - flags unchanged, CN chapters strengthened. E-14, D-01, D-19, A-14, A-21, D-09 received CN/license notes in text WITHOUT flag changes (evidence conditional or access license-only). No CN credibility was fabricated to hit quotas.

## Source-ID imports

- 90 source-ID additions to canonical seeds, all validated against `90_BIBLIOGRAPHY/sources.json` (accepted + india_origin_audit verified).
  - P3R2-C-04 technical_source_ids: +L14-053
  - P3R2-C-12 demand_source_ids: +L03-043
  - P3R2-C-12 demand_source_ids: +L07-045
  - P3R2-C-12 technical_source_ids: +L03-025
  - P3R2-C-12 technical_source_ids: +L03-026
  - P3R2-D-08 technical_source_ids: +L05-009
  - P3R2-D-08 technical_source_ids: +L05-015
  - P3R2-D-08 technical_source_ids: +L05-016
  - P3R2-D-11 technical_source_ids: +L12-001
  - P3R2-D-11 technical_source_ids: +L12-002
  - P3R2-D-11 technical_source_ids: +L06-016
  - P3R2-D-11 technical_source_ids: +L06-017
  - P3R2-D-19 demand_source_ids: +L02-048
  - P3R2-D-19 demand_source_ids: +L02-049
  - P3R2-C-01 competitor_source_ids: +L02-046
  - P3R2-C-01 competitor_source_ids: +L02-051
  - P3R2-A-10 demand_source_ids: +L06-042
  - P3R2-A-10 demand_source_ids: +L06-043
  - P3R2-A-10 demand_source_ids: +L06-044
  - P3R2-A-10 demand_source_ids: +L06-054
  - P3R2-A-10 technical_source_ids: +L06-002
  - P3R2-A-10 technical_source_ids: +L06-008
  - P3R2-A-10 technical_source_ids: +L06-024
  - P3R2-A-10 technical_source_ids: +L06-025
  - P3R2-A-10 technical_source_ids: +L06-005
  - P3R2-A-10 technical_source_ids: +L06-006
  - P3R2-A-10 competitor_source_ids: +L06-050
  - P3R2-A-10 competitor_source_ids: +L06-042
  - P3R2-C-09 demand_source_ids: +L05-042
  - P3R2-C-09 demand_source_ids: +L05-012
  - P3R2-C-09 demand_source_ids: +L05-013
  - P3R2-C-09 demand_source_ids: +L07-045
  - P3R2-C-09 technical_source_ids: +L05-007
  - P3R2-C-09 technical_source_ids: +L05-008
  - P3R2-C-09 technical_source_ids: +L05-010
  - P3R2-C-09 technical_source_ids: +L05-044
  - P3R2-C-09 competitor_source_ids: +L05-037
  - P3R2-C-09 competitor_source_ids: +L05-029
  - P3R2-D-01 demand_source_ids: +L03-042
  - P3R2-D-01 demand_source_ids: +L03-043
  - P3R2-D-01 demand_source_ids: +L03-030
  - P3R2-D-01 demand_source_ids: +L03-044
  - P3R2-D-01 technical_source_ids: +L03-005
  - P3R2-D-01 technical_source_ids: +L03-006
  - P3R2-D-01 technical_source_ids: +L03-007
  - P3R2-D-01 technical_source_ids: +L03-008
  - P3R2-D-02 demand_source_ids: +L03-041
  - P3R2-D-02 demand_source_ids: +L03-031
  - P3R2-D-02 demand_source_ids: +L03-029
  - P3R2-D-02 demand_source_ids: +L03-037
  - P3R2-D-02 demand_source_ids: +L03-032
  - P3R2-D-02 demand_source_ids: +L03-035
  - P3R2-D-02 technical_source_ids: +L03-050
  - P3R2-C-05 demand_source_ids: +L14-033
  - P3R2-C-05 demand_source_ids: +L14-034
  - P3R2-C-05 technical_source_ids: +L14-002
  - P3R2-C-05 technical_source_ids: +L14-003
  - P3R2-C-05 technical_source_ids: +L14-022
  - P3R2-C-05 technical_source_ids: +L14-028
  - P3R2-C-05 competitor_source_ids: +L14-045
  - P3R2-C-05 competitor_source_ids: +L14-046
  - P3R2-C-07 technical_source_ids: +L11-004
  - P3R2-C-07 technical_source_ids: +L11-031
  - P3R2-C-07 technical_source_ids: +L11-012
  - P3R2-C-07 technical_source_ids: +L11-013
  - P3R2-C-08 demand_source_ids: +L04-047
  - P3R2-C-08 technical_source_ids: +L04-101
  - P3R2-C-08 technical_source_ids: +L04-109
  - P3R2-C-08 technical_source_ids: +L04-111
  - P3R2-C-08 competitor_source_ids: +L04-028
  - P3R2-A-13 demand_source_ids: +L09-037
  - P3R2-A-13 technical_source_ids: +L09-001
  - P3R2-A-13 technical_source_ids: +L09-008
  - P3R2-A-14 technical_source_ids: +L15-011
  - P3R2-A-21 technical_source_ids: +L10-045
  - P3R2-A-21 technical_source_ids: +L10-046
  - P3R2-D-09 demand_source_ids: +L05-031
  - P3R2-D-10 demand_source_ids: +L12-033
  - P3R2-D-10 demand_source_ids: +L12-042
  - P3R2-D-10 demand_source_ids: +L12-047
  - P3R2-D-10 technical_source_ids: +L12-009
  - P3R2-D-10 technical_source_ids: +L12-010
  - P3R2-D-10 technical_source_ids: +L12-011
  - P3R2-D-10 competitor_source_ids: +L12-034
  - P3R2-D-10 competitor_source_ids: +L12-045
  - P3R2-E-04 competitor_source_ids: +L13-046
  - P3R2-E-04 competitor_source_ids: +L13-038
  - P3R2-E-14 demand_source_ids: +L08-034
  - P3R2-E-14 technical_source_ids: +L08-001
  - P3R2-E-14 technical_source_ids: +L08-003
- No requested import ID failed eligibility.

## Detailed change log

### P3R2-A-03
- demand_trigger_2030_2034: rewrote a passage (NERC PRC-029-1 compliance/enforcement phase-in and post-disturbance re... -> NERC PRC-029-1 compliance/enforcement phase-in and post-disturbance re...)
- precompany_plan_2026_2029: appended: FIX gate (2027): obtain written regional-entity compliance guidance or two owner-operator LOIs evidencing that...
- competition_outlook_2030: appended: Positioning per adjudication: field-hardware complement to P3R2-E-14's relay/HIL qualification platform, not a...
- fix_applied_notes recorded
### P3R2-A-11
- precompany_plan_2026_2029: appended: FIX additions: 2026-27 includes a quantified $/tool/year throughput-value model vs OEM qualification switching...
- timing_window_risk: appended: Adjudication: incumbent (Horiba/Brooks/MKS) catch-up could close the window before 2030; the 2028 dual-sourcin...
- fix_applied_notes recorded
### P3R2-A-16
- product: rewrote a passage (A TIM system, not a paste: liquid-metal/sintered-metal composite with ... -> A TIM system, not a paste and not a service: a productized SKU family ...)
- precompany_plan_2026_2029: appended: FIX gate (2028): anchor-packager LOI on the SKU + process-license model. Kill gate: the head-to-head reliabili...
- fix_applied_notes recorded
### P3R2-B-06
- product: appended: Initial scope (FIX): mature-node (>=28nm) and panel/display tools only, for export-control safety; leading-edg...
- demand_trigger_2030_2034: appended: FIX condition: this trigger is inferential (localization gap + research base), not a named ESC tender; P4 must...
- competition_outlook_2030: appended: P4 verification task: confirm AE/MKS clamp-supply bundling (L06-039) does not foreclose the merchant socket....
- fix_applied_notes recorded
### P3R2-B-14
- precompany_plan_2026_2029: appended: FIX gate (2028): documented evidence that one named export program (XCMG-Fortescue delivery chain or an SPIC s...
- timing_window_risk: appended: Fold-in path (pre-agreed per adjudication): if the swap architecture fails offshore, the dual-personality conv...
- fix_applied_notes recorded
### P3R2-B-22
- product: appended: FIX: defined as a retrofit SKU (clip-on sensing module + gateway) with the cross-vendor failure database as th...
- precompany_plan_2026_2029: appended: FIX gate (2028): LOI from one named design-win path - a PSU/UPS vendor or a third-party maintenance operator; ...
- timing_window_risk: appended: Keep the US secondary market active from day one so the business is not hostage to CN vendor access....
- fix_applied_notes recorded
### P3R2-C-02
- precompany_plan_2026_2029: appended: FIX additions: 2026-27 quantified cost-parity model vs distributed electrolytic banks and vs BBU shelves (the ...
- timing_window_risk: appended: Codified kill trigger (FIX): if OCP/NVIDIA specs an in-rack buffer function or Delta/Vicor-class vendors ship ...
- fix_applied_notes recorded
### P3R2-C-03
- precompany_plan_2026_2029: rewrote a passage (2026-28: university/consortium work (DC-GRIDS-adjacent, L02-034) on HF... -> Pre-company scope strictly limited (FIX): HF-insulation/partial-discha...)
- timing_window_risk: appended: FIX: the 2028 standards+procurement gate is binding; a blocked certification category must not carry $25-60M c...
- confidence: 'medium' -> 'low'
- fix_applied_notes recorded
### P3R2-C-04
- product: rewrote a passage (A sealed pumped two-phase loop (cold plate + micro-pump + condenser + ... -> Primary variant (merged from P3R2-B-01): a sealed negative-pressure (s...)
- technical_source_ids: added eligible IDs ['L14-053']
- timing_window_risk: appended: FIX: the 2031 fluid-availability kill trigger is retained and extended to cover the subatmospheric-water varia...
- confidence: 'high' -> 'medium'
- fix_applied_notes recorded
### P3R2-C-12
- competition_outlook_2030: appended: FIX (pre-promotion P4 requirement): full competitor map of the 100W-2kW @ 20K band - Air Liquide/Linde turbo-B...
- timing_window_risk: rewrote a passage (Plan: US/allied beachhead 2030; CN served only for grid/science via li... -> FIX: CN participation is license-only (no CN beachhead entity) and the...)
- precompany_plan_2026_2029: appended: FIX: capex staged - component/cold-head work only until a named buyer LOI is in hand; no full-skid integration...
- product: appended: Product definition imported from merged duplicates D-03/B-11: catalog-priced skids with ~6-month lead times, N...
- named_buyer_examples: added ['mid-scale national-lab/university magnet and accelerator programs (US, from D-03)', 'KEPCO/LS superconducting datacenter-grid lineage (KR side market, L03-043, from D-03)', 'IHEP-class Chinese facility programs (procurement style per HEPS tenders, L07-045; license-only channel, from B-11)']
- demand_source_ids: added eligible IDs ['L03-043', 'L07-045']
- technical_source_ids: added eligible IDs ['L03-025', 'L03-026']
- primary_market: 'US+CN' -> 'US'
- china_beachhead: True -> False
- fix_applied_notes recorded
### P3R2-C-13
- product: appended: Imported differentiator (from merged A-18): integrated diode-health telemetry (droop, threshold-drift tracking...
- precompany_plan_2026_2029: appended: FIX gate (2028): OEM buy-vs-build discovery must convert to two PAID evaluations (one US, one CN commercial); ...
- timing_window_risk: appended: FIX: the US(DEW)/commercial two-entity partition is a day-one structural requirement, not a contingency....
- demand_trigger_2030_2034: appended: CN demand chapter (merged from B-19): the fiber-laser price war is pushing Han's/Raycus up-market into ultrafa...
- fix_applied_notes recorded
### P3R2-C-19
- product: appended: Structural pairing (FIX): develop and pitch jointly with P3R2-C-08 as one high-temperature-components company ...
- precompany_plan_2026_2029: appended: FIX gate (2028): proceed past test-cell work only on machine-build signals - STEP Phase 2 hardware orders (US)...
- competition_outlook_2030: appended: P4 requirement: map the seal-major incumbent response (John Crane/EagleBurgmann-class) before promotion....
- fix_applied_notes recorded
### P3R2-C-21
- product: rewrote a passage (Multiport DC-DC power blocks (1-10MW): PV-string/BESS MVDC input to 80... -> Multiport DC-DC power blocks (1-10MW): PV-string/BESS MVDC input to 80...)
- precompany_plan_2026_2029: appended: FIX gate (2028): a named US campus/IPP DC-coupling pilot commitment; absent it, re-batch the seed....
- timing_window_risk: rewrote a passage (Protection/standards immaturity (DC breakers unconverged, L08-001/003/... -> Protection/standards immaturity (DC breakers unconverged, L08-001/003/...)
- primary_market: 'US+CN' -> 'US'
- china_beachhead: True -> False
- v1_capital_range_usd: [12000000, 30000000] -> [10000000, 25000000]
- fix_applied_notes recorded
### P3R2-D-07
- precompany_plan_2026_2029: appended: FIX additions: 2026-27 includes fleet-size and $-per-efficiency-point arithmetic from named facilities (SLAC-c...
- fix_applied_notes recorded
### P3R2-D-08
- launch_2030_timing_thesis: rewrote a passage (The EtO forcing function is durable regulatory pressure, not a one-cyc... -> Working hypothesis with three load-bearing assumptions, each gated (FI...)
- product: appended: Deployment options (FIX, absorbing A-09): the same accelerator/RF core ships either as a central contract-ster...
- technical_source_ids: added eligible IDs ['L05-009', 'L05-015', 'L05-016']
- precompany_plan_2026_2029: appended: FIX gates: 2027 backlog-persistence check (kill if IBA/L3 clear backlogs and cut prices); 2028 SSPA-vs-klystro...
- fix_applied_notes recorded
### P3R2-D-11
- commercial_readiness_kill_date: '2032-12' -> '2033-12 (stricter imported gate: kill unless tin-droplet CE >=4% at relevant rep-rate is demonstrated by end-2033)'
- first_experiment: appended: Continue/kill ladder (FIX): 2028 experimental CE >=3% to continue; imported E-13 gate: CE >=4% at relevant rep...
- precompany_plan_2026_2029: appended: FIX capital rule: no capital beyond the consortium-scale droplet experiment until the CE gate passes. Likely e...
- demand_trigger_2030_2034: appended: Second-buyer hedge (merged from E-13): Gigaphoton (Komatsu group) as the named second source-developer custome...
- technical_source_ids: added eligible IDs ['L12-001', 'L12-002', 'L06-016', 'L06-017']
- fix_applied_notes recorded
### P3R2-D-12
- precompany_plan_2026_2029: appended: FIX gate (2028): a named cold-plate OEM or COOLERCHIPS-lineage co-development agreement - the demand bridge th...
- first_experiment: rewrote a passage (EHD-assisted two-phase microchannel plate on a 500 W emulator: demonst... -> EHD-assisted two-phase microchannel plate on a 500 W emulator: demonst...)
- timing_window_risk: appended: Hard fluid-intersection gate (FIX): the working fluid must simultaneously be dielectric, non-PFAS, and low-GWP...
- fix_applied_notes recorded
### P3R2-D-16
- precompany_plan_2026_2029: rewrote a passage (2026-27: cycle/mass optimization studies against the 100 kWe RFI spec;... -> HELD AS OPTION (FIX): studies/SBIR only - no hardware capex until FSP ...)
- product: appended: Fold-down path (FIX): define a terrestrial micro-Brayton variant (remote/microgrid gensets, industrial heat re...
- first_experiment: appended: (Conditional on the 2028 FSP-contract checkpoint; until then, studies only.)...
- fix_applied_notes recorded
### P3R2-D-18
- precompany_plan_2026_2029: appended: FIX gate (2028): a second named demand anchor - another program office, a prime teaming agreement, or a Phase ...
- competition_outlook_2030: appended: P4 requirement: incumbent mapping - Echodyne-class metamaterial ESA vendors and prime GaN AESA cost curves - t...
- timing_window_risk: appended: KR allied-variant (merged from E-12: the KRISS-to-KER transfer model, L16-018) is upside only - excluded from ...
- fix_applied_notes recorded
### P3R2-D-19
- precompany_plan_2026_2029: rewrote a passage (2026-27: rotor/bearing design and loss modeling; quantify AI-cluster l... -> 2026-27 (FIX-hardened): instrumented load-spectrum study with a datace...)
- demand_trigger_2030_2034: appended: CN market (merged from B-18): Dong-Shu-Xi-Suan hub parks and 800VDC rollouts (L02-048, L02-049) are a license-...
- demand_source_ids: added eligible IDs ['L02-048', 'L02-049']
- fix_applied_notes recorded
### P3R2-D-20
- precompany_plan_2026_2029: appended: FIX gates: 2028 - at least one liquid-metal thermal-battery developer must show a commercial order book, else ...
- named_buyer_examples: added ['solar-thermochemical pilot developers (buyer-hypothesis broadening, FIX)', 'metallurgy/process-heat pilot lines handling molten metals (buyer-hypothesis broadening, FIX)']
- fix_applied_notes recorded
### P3R2-E-02
- precompany_plan_2026_2029: rewrote a passage (2028-29: joint validation slots at NTT Facilities' DC Cooling Hub (JP)... -> 2028-29: joint validation slots at NTT Facilities' DC Cooling Hub (JP)...)
- timing_window_risk: appended: The two-phase shipment-share kill trigger (<5% of liquid-cooling shipments by 2033) is binding (FIX)....
- fix_applied_notes recorded
### P3R2-E-11
- precompany_plan_2026_2029: appended: FIX gate (2028): documented CPO volume-ramp evidence (switch-vendor roadmap commitments/orders) PLUS one switc...
- timing_window_risk: appended: Explicit LPO-substitution monitor (FIX): track linear-drive pluggable share each optics generation; sustained ...
- fix_applied_notes recorded
### P3R2-B-21
- fix_applied_notes recorded
### P3R2-C-20
- fix_applied_notes recorded
### P3R2-C-01
- product: appended: Imports from merged duplicates: fleet-wide DC arc-signature analytics with a UL/IEC listing-path emphasis (fro...
- competitor_source_ids: added eligible IDs ['L02-046', 'L02-051']
- secondary_markets: ['TW', 'JP'] -> ['TW: ODM co-design and manufacturing wedge - Delta and the Taipei 800VDC ecosystem build the racks this unit slots into (L02-037, L02-046) [from E-01]', 'JP: SiC device supply and co-qualification with ROHM-class 750V/1200V parts (L02-051) [from E-01]']
- merge_import_notes recorded
### P3R2-A-10
- product: appended: Merged extensions: (1) company structure = two-entity export partition (from C-06) - the US entity serves lead...
- demand_trigger_2030_2034: rewrote a passage (Sub-2nm/backside-power etch capacity ramps at CHIPS-funded US fabs 203... -> US: sub-2nm/backside-power etch capacity ramps at CHIPS-funded US fabs...)
- precompany_plan_2026_2029: appended: Merged gates: export-control counsel review of the two-entity partition is a 2027 gate (before any CN-facing w...
- named_buyer_examples: added ['AMEC (CN, via partitioned >=28nm entity, from B-05)', 'NAURA / Piotech (CN, via partitioned >=28nm entity, from B-05)']
- demand_source_ids: added eligible IDs ['L06-042', 'L06-043', 'L06-044', 'L06-054']
- technical_source_ids: added eligible IDs ['L06-002', 'L06-008', 'L06-024', 'L06-025', 'L06-005', 'L06-006']
- competitor_source_ids: added eligible IDs ['L06-050', 'L06-042']
- primary_market: 'US' -> 'US+CN'
- china_beachhead: False -> True
- merge_import_notes recorded
### P3R2-C-09
- product: appended: Merged product-family extensions: a published open module/interconnect interface spec offered as a de facto st...
- first_experiment: appended: RF-drive line decisive experiment (from C-20): 20kW 500MHz GaN SSPA block with envelope tracking demonstrating...
- demand_trigger_2030_2034: appended: Acceptance-protocol emphasis (from A-07): the published acceptance-test protocol aligned to IEC 60060-1:2025 i...
- named_buyer_examples: added ['SLAC GREEN-RF commercialization lineage / DOE facility RF upgrades (US, from C-20)', 'KR channel: Vitzro Nextec / Pohang Accelerator Laboratory klystron-localization ecosystem as manufacturing partner and validation site (L05-037, from E-05)']
- demand_source_ids: added eligible IDs ['L05-042', 'L05-012', 'L05-013', 'L07-045']
- technical_source_ids: added eligible IDs ['L05-007', 'L05-008', 'L05-010', 'L05-044']
- competitor_source_ids: added eligible IDs ['L05-037', 'L05-029']
- secondary_markets: ['KR', 'JP'] -> ['KR: Vitzro Nextec/PAL klystron-localization ecosystem as manufacturing partner and validation site (L05-037) [from E-05]', 'JP']
- merge_import_notes recorded
### P3R2-D-01
- product: appended: Merged extensions: delivered with a published acceptance-test protocol and warranty-support framing for mercha...
- demand_trigger_2030_2034: appended: Side market (from E-07): KEPCO + LS Cable/LS Electric superconducting datacenter-grid MOU as a cable-monitorin...
- named_buyer_examples: added ['US-ITER/ORNL magnet operations (from A-04/E-07, L03-030)']
- demand_source_ids: added eligible IDs ['L03-042', 'L03-043', 'L03-030', 'L03-044']
- technical_source_ids: added eligible IDs ['L03-005', 'L03-006', 'L03-007', 'L03-008']
- secondary_markets: ['JP', 'KR'] -> ['JP: Furukawa/Fujikura REBCO ecosystem as conductor-QA partners (L03-044) [from E-07]', 'KR: KEPCO + LS Cable datacenter superconducting-grid MOU as cable-monitoring side market (L03-042, L03-043) [from E-07]']
- merge_import_notes recorded
### P3R2-D-02
- product: appended: Merged extensions: 10kA-class cable/CICC acceptance stations and financier/insurer-grade data packages (from C...
- demand_trigger_2030_2034: appended: Additional evidenced demand (merged): DOE milestone-program QA needs and CFS magnet-as-product certification (...
- named_buyer_examples: added ['Western Superconducting Technologies (CN, ITER strand lineage, L03-031, from B-10)', 'ASIPP Hefei high-field magnet program (CN, L03-029/037, from B-10)']
- demand_source_ids: added eligible IDs ['L03-041', 'L03-031', 'L03-029', 'L03-037', 'L03-032', 'L03-035']
- technical_source_ids: added eligible IDs ['L03-050']
- merge_import_notes recorded
### P3R2-C-05
- product: appended: Merged extensions: precision flow/enthalpy calorimetry benches specified to <=1% energy-balance closure and ac...
- named_buyer_examples: added ['fluid makers (Chemours/Honeywell archetype) qualifying post-PFAS fluids (from A-15)', 'Chinese certification/inspection labs adopting T/CIEP 0263-2025 (from B-02)']
- demand_source_ids: added eligible IDs ['L14-033', 'L14-034']
- technical_source_ids: added eligible IDs ['L14-002', 'L14-003', 'L14-022', 'L14-028']
- competitor_source_ids: added eligible IDs ['L14-045', 'L14-046']
- merge_import_notes recorded
### P3R2-C-07
- product: appended: Merged extensions: per-cell/per-stack telemetry with a financier-grade measurement-and-verification (M&V) prot...
- precompany_plan_2026_2029: appended: Beachhead sequencing (from A-19): US copper-electrowinning tankhouses first (policy-independent energy lever),...
- technical_source_ids: added eligible IDs ['L11-004', 'L11-031', 'L11-012', 'L11-013']
- merge_import_notes recorded
### P3R2-C-08
- product: appended: Merged extensions: sold as catalog frames with published delivery times, not EPC subprojects (from A-12); grad...
- precompany_plan_2026_2029: appended: Added task (from E-08): pre-commitment triangulation of the CN retrofit TAM from eligible sources - the RMB100...
- named_buyer_examples: added ['TC Energy-Hanwha pipeline waste-heat lineage (US/KR, L04-047, from E-08)']
- demand_source_ids: added eligible IDs ['L04-047']
- technical_source_ids: added eligible IDs ['L04-101', 'L04-109', 'L04-111']
- competitor_source_ids: added eligible IDs ['L04-028']
- secondary_markets: ['KR', 'JP'] -> ['KR: KAERI/KAIST/Jinsol sCO2 consortium and Hanwha Power Systems as first-adopter partners and channel (L04-028, L04-047) [from E-08]', 'JP: MHI-owned Turboden ORC channel as adjacent heat-to-power distribution relationship (L04-044) [from E-08]']
- merge_import_notes recorded
### P3R2-A-05
- merge_import_notes recorded
### P3R2-A-13
- product: appended: Merged extensions: SEE-map-first sequencing - publish device SEE/TID maps before module qualification - and a ...
- demand_trigger_2030_2034: appended: Additional trigger (from D-15): Space Force Maneuverable-GEO-class programs (L09-037). SDA EP content remains ...
- demand_source_ids: added eligible IDs ['L09-037']
- technical_source_ids: added eligible IDs ['L09-001', 'L09-008']
- secondary_markets: ['JP'] -> ['JP: JAXA-Furukawa J-SPARC GaN Hall-thruster power-supply commercialization as validation-pattern partner/licensee (L09-042) [from E-10]', 'KR: KARI full-electric-propulsion GEO design studies as an emergent 2030s buyer (L09-019) [from E-10]']
- merge_import_notes recorded
### P3R2-A-14
- product: appended: Merged extensions: packaging-first qualification strategy - advanced die-attach/ceramic packaging is the docum...
- precompany_plan_2026_2029: appended: Added roadmap steps: the 1,000h powered-soak artifact is the flagship qualification datum (from E-09); a FORGE...
- technical_source_ids: added eligible IDs ['L15-011']
- secondary_markets: ['JP'] -> ['JP: Fukushima-decommissioning robotics ecosystem as a qualified-electronics side market (L15-011) [from E-09]']
- merge_import_notes recorded
### P3R2-A-21
- product: appended: Merged extensions: optional dual-standard capability - IEC MCS and Chinese swap-station DC interface personali...
- technical_source_ids: added eligible IDs ['L10-045', 'L10-046']
- merge_import_notes recorded
### P3R2-D-09
- product: appended: Merged extension (from A-08): a sterilization-QA product tier - per-unit calibration certificates for e-beam/X...
- demand_source_ids: added eligible IDs ['L05-031']
- merge_import_notes recorded
### P3R2-D-10
- product: appended: Merged extension (from A-17): an environmental-grade deformable-mirror control and turbulence/jitter-compensat...
- demand_trigger_2030_2034: appended: Additional demand leg (from A-17): NNSA Expanded Yield Capability (EYC) execution beyond CD-1 (L12-042) and DA...
- demand_source_ids: added eligible IDs ['L12-033', 'L12-042', 'L12-047']
- technical_source_ids: added eligible IDs ['L12-009', 'L12-010', 'L12-011']
- competitor_source_ids: added eligible IDs ['L12-034', 'L12-045']
- merge_import_notes recorded
### P3R2-E-04
- product: appended: Merged framing (from A-06): sold on channels-per-watt economics (qualified heat load per channel), not per-cab...
- timing_window_risk: appended: Substitution risks kept on record (from D-17): on-chip 1000:1 multiplexing, SFQ readout, cryo-CMOS moving cont...
- competitor_source_ids: added eligible IDs ['L13-046', 'L13-038']
- merge_import_notes recorded
### P3R2-E-14
- demand_trigger_2030_2034: appended: CN chapter (from C-16, license-only): Chinese converter-valve/protection suppliers (XJ Electric-class) need fa...
- competition_outlook_2030: appended: Scope coordination (adjudication): E-14 owns the relay + qualification layer; P3R2-A-02 owns breaker hardware;...
- demand_source_ids: added eligible IDs ['L08-034']
- technical_source_ids: added eligible IDs ['L08-001', 'L08-003']
- merge_import_notes recorded
### P3R2-B-01
- merge_import_notes recorded
### P3R2-A-01
- elegance_verdict = MERGED_INTO_P3R2-C-01, duplicate_of = P3R2-C-01
### P3R2-A-02
- elegance_verdict = PROMOTE
### P3R2-A-03
- elegance_verdict = FIX_APPLIED
### P3R2-A-04
- elegance_verdict = MERGED_INTO_P3R2-D-01, duplicate_of = P3R2-D-01
### P3R2-A-05
- elegance_verdict = PROMOTE
### P3R2-A-06
- elegance_verdict = REJECT, duplicate_of = P3R2-E-04
### P3R2-A-07
- elegance_verdict = REJECT, duplicate_of = P3R2-C-09
### P3R2-A-08
- elegance_verdict = REJECT, duplicate_of = P3R2-D-09
### P3R2-A-09
- elegance_verdict = REJECT, duplicate_of = P3R2-D-08
### P3R2-A-10
- elegance_verdict = PROMOTE
### P3R2-A-11
- elegance_verdict = FIX_APPLIED
### P3R2-A-12
- elegance_verdict = REJECT, duplicate_of = P3R2-C-08
### P3R2-A-13
- elegance_verdict = PROMOTE
### P3R2-A-14
- elegance_verdict = PROMOTE
### P3R2-A-15
- elegance_verdict = MERGED_INTO_P3R2-C-05, duplicate_of = P3R2-C-05
### P3R2-A-16
- elegance_verdict = FIX_APPLIED
### P3R2-A-17
- elegance_verdict = REJECT, duplicate_of = P3R2-D-10
### P3R2-A-18
- elegance_verdict = REJECT, duplicate_of = P3R2-C-13
### P3R2-A-19
- elegance_verdict = REJECT, duplicate_of = P3R2-C-07
### P3R2-A-20
- elegance_verdict = REJECT
### P3R2-A-21
- elegance_verdict = PROMOTE
### P3R2-A-22
- elegance_verdict = PROMOTE
### P3R2-B-01
- elegance_verdict = PROMOTE
### P3R2-B-02
- elegance_verdict = MERGED_INTO_P3R2-C-05, duplicate_of = P3R2-C-05
### P3R2-B-03
- elegance_verdict = REJECT, duplicate_of = P3R2-C-01
### P3R2-B-04
- elegance_verdict = REJECT, duplicate_of = P3R2-C-01
### P3R2-B-05
- elegance_verdict = REJECT, duplicate_of = P3R2-A-10
### P3R2-B-06
- elegance_verdict = FIX_APPLIED
### P3R2-B-07
- elegance_verdict = REJECT, duplicate_of = P3R2-C-08
### P3R2-B-08
- elegance_verdict = REJECT, duplicate_of = P3R2-C-19
### P3R2-B-09
- elegance_verdict = REJECT, duplicate_of = P3R2-C-09
### P3R2-B-10
- elegance_verdict = REJECT, duplicate_of = P3R2-D-02
### P3R2-B-11
- elegance_verdict = REJECT, duplicate_of = P3R2-C-12
### P3R2-B-12
- elegance_verdict = REJECT, duplicate_of = P3R2-A-05
### P3R2-B-13
- elegance_verdict = REJECT, duplicate_of = P3R2-C-07
### P3R2-B-14
- elegance_verdict = FIX_APPLIED
### P3R2-B-15
- elegance_verdict = REJECT
### P3R2-B-16
- elegance_verdict = REJECT
### P3R2-B-17
- elegance_verdict = REJECT, duplicate_of = P3R2-A-14
### P3R2-B-18
- elegance_verdict = REJECT, duplicate_of = P3R2-D-19
### P3R2-B-19
- elegance_verdict = REJECT, duplicate_of = P3R2-C-13
### P3R2-B-20
- elegance_verdict = REJECT
### P3R2-B-21
- elegance_verdict = MERGED_INTO_P3R2-A-10, duplicate_of = P3R2-A-10
### P3R2-B-22
- elegance_verdict = FIX_APPLIED
### P3R2-C-01
- elegance_verdict = PROMOTE
### P3R2-C-02
- elegance_verdict = FIX_APPLIED
### P3R2-C-03
- elegance_verdict = FIX_APPLIED
### P3R2-C-04
- elegance_verdict = FIX_APPLIED
### P3R2-C-05
- elegance_verdict = PROMOTE
### P3R2-C-06
- elegance_verdict = MERGED_INTO_P3R2-A-10, duplicate_of = P3R2-A-10
### P3R2-C-07
- elegance_verdict = PROMOTE
### P3R2-C-08
- elegance_verdict = PROMOTE
### P3R2-C-09
- elegance_verdict = PROMOTE
### P3R2-C-10
- elegance_verdict = REJECT, duplicate_of = P3R2-D-09
### P3R2-C-11
- elegance_verdict = MERGED_INTO_P3R2-D-02, duplicate_of = P3R2-D-02
### P3R2-C-12
- elegance_verdict = FIX_APPLIED
### P3R2-C-13
- elegance_verdict = FIX_APPLIED
### P3R2-C-14
- elegance_verdict = REJECT
### P3R2-C-15
- elegance_verdict = REJECT, duplicate_of = P3R2-A-21
### P3R2-C-16
- elegance_verdict = MERGED_INTO_P3R2-E-14, duplicate_of = P3R2-E-14
### P3R2-C-17
- elegance_verdict = REJECT, duplicate_of = P3R2-D-01
### P3R2-C-18
- elegance_verdict = REJECT
### P3R2-C-19
- elegance_verdict = FIX_APPLIED
### P3R2-C-20
- elegance_verdict = MERGED_INTO_P3R2-C-09, duplicate_of = P3R2-C-09
### P3R2-C-21
- elegance_verdict = FIX_APPLIED
### P3R2-C-22
- elegance_verdict = PROMOTE
### P3R2-D-01
- elegance_verdict = PROMOTE
### P3R2-D-02
- elegance_verdict = PROMOTE
### P3R2-D-03
- elegance_verdict = REJECT, duplicate_of = P3R2-C-12
### P3R2-D-04
- elegance_verdict = REJECT
### P3R2-D-05
- elegance_verdict = MERGED_INTO_P3R2-C-09, duplicate_of = P3R2-C-09
### P3R2-D-06
- elegance_verdict = REJECT
### P3R2-D-07
- elegance_verdict = FIX_APPLIED
### P3R2-D-08
- elegance_verdict = FIX_APPLIED
### P3R2-D-09
- elegance_verdict = PROMOTE
### P3R2-D-10
- elegance_verdict = PROMOTE
### P3R2-D-11
- elegance_verdict = FIX_APPLIED
### P3R2-D-12
- elegance_verdict = FIX_APPLIED
### P3R2-D-13
- elegance_verdict = PROMOTE
### P3R2-D-14
- elegance_verdict = MERGED_INTO_P3R2-A-14, duplicate_of = P3R2-A-14
### P3R2-D-15
- elegance_verdict = MERGED_INTO_P3R2-A-13, duplicate_of = P3R2-A-13
### P3R2-D-16
- elegance_verdict = FIX_APPLIED
### P3R2-D-17
- elegance_verdict = REJECT, duplicate_of = P3R2-E-04
### P3R2-D-18
- elegance_verdict = FIX_APPLIED
### P3R2-D-19
- elegance_verdict = FIX_APPLIED
### P3R2-D-20
- elegance_verdict = FIX_APPLIED
### P3R2-E-01
- elegance_verdict = MERGED_INTO_P3R2-C-01, duplicate_of = P3R2-C-01
### P3R2-E-02
- elegance_verdict = FIX_APPLIED
### P3R2-E-03
- elegance_verdict = REJECT, duplicate_of = P3R2-A-10
### P3R2-E-04
- elegance_verdict = PROMOTE
### P3R2-E-05
- elegance_verdict = REJECT, duplicate_of = P3R2-C-09
### P3R2-E-06
- elegance_verdict = REJECT
### P3R2-E-07
- elegance_verdict = MERGED_INTO_P3R2-D-01, duplicate_of = P3R2-D-01
### P3R2-E-08
- elegance_verdict = REJECT, duplicate_of = P3R2-C-08
### P3R2-E-09
- elegance_verdict = MERGED_INTO_P3R2-A-14, duplicate_of = P3R2-A-14
### P3R2-E-10
- elegance_verdict = MERGED_INTO_P3R2-A-13, duplicate_of = P3R2-A-13
### P3R2-E-11
- elegance_verdict = FIX_APPLIED
### P3R2-E-12
- elegance_verdict = REJECT, duplicate_of = P3R2-D-18
### P3R2-E-13
- elegance_verdict = REJECT, duplicate_of = P3R2-D-11
### P3R2-E-14
- elegance_verdict = PROMOTE

## Coherence check

All edited seeds retain a coherent 2030 contract: TRL unchanged except where fixes hedged claims in text; every FIX seed now carries explicit 2027/2028 gates inside its 2026-2029 pre-company plan; named 2030-2034 triggers were hedged (A-03, B-06, D-08, B-14) rather than deleted; kill dates unchanged except D-11 (2032-12 -> 2033-12 with the stricter imported CE>=4% gate) and C-02/C-21 (fold/re-batch triggers codified). MD files carry per-seed annotations matching the JSON edits.

---

# P3R2 fix-application log — round 2 (wave F + cross-file imports)

Applied 2026-07-13 by the Fable 5/xhigh fix-application agent (claude-fable-5, effort xhigh), implementing `P3R2_ELEGANCE_ADJUDICATION_R2.json` rulings on the 23 wave-F seeds (`P3R2_F_cn_topup.{json,md}`) plus one cross-file import into `P3R2_A_us_pain.{json,md}`. No seed records deleted; rejects and merged seeds remain as audit trail.

## Verdict marking (23 wave-F seeds)

- 3 PROMOTE: F-01, F-02, F-12.
- 15 FIX -> `FIX_APPLIED` (edited in place): F-03, F-04, F-05, F-06, F-07, F-09, F-10, F-11, F-15, F-16, F-17, F-19, F-20, F-22, F-23.
- F-18 -> `MERGED_INTO_P3R2-F-03` (duplicate_of = P3R2-F-03); F-21 -> `MERGED_INTO_P3R2-F-02` (duplicate_of = P3R2-F-02).
- F-08 -> `REJECT` (duplicate_of = P3R2-A-02, import executed); F-13 -> `REJECT`; F-14 -> `REJECT` (import into F-01 executed).
- Every seed carries a dated `adjudication_note`; every FIX seed carries `fix_applied_notes`.
- Post-merge distinct wave-F concepts: 18.

## China-flag changes (honesty rule)

- **P3R2-F-06**: primary_market US+CN -> US, china_beachhead true -> false, per the judge's honesty ruling (State Grid domestic-only; CN revenue "license royalties at best" - the same condition that downgraded C-12/C-21). CN license chapter retained in text; the demand-trigger and plan fields relabel the CN leg as royalty upside, not a market leg. NOT counted toward the CN quota; the judge's 35/36 CN-gate shortfall stands (remedy is micro-wave G or the F-04/F-20 P4-conditional upgrades - not re-flagging).
- **P3R2-F-04** and **P3R2-F-20** remain dual (china_beachhead true) but CONDITIONALLY per the ruling; the conditions (named CN OEM/tender channel in P4, else downgrade/reduce) are now written into their JSON demand/plan fields.
- No CN credibility fabricated to hit quotas.

## Merges and imports

1. **F-21 -> F-02 (entry SKU)**: catalog binary current leads (0.5-20 kA), vacuum-tight instrumented feedthroughs, and certified heat-load datasheets appended to F-02's product; entry-SKU track added to the 2026-2029 plan; end-2031 >=$1M cumulative entry-SKU gate added inside the kill-date field.
2. **F-18 -> F-03 (CN plant-integration/licensing chapter)**: EPC co-bidding memorandum concept, Xinjiang first-set timeline alignment (~2028 completion), rollout-industrialization framing added to F-03's plan; no new source IDs needed (all already cited in F-03).
3. **F-14 -> F-01 (CN-chapter licensing mechanics)**: licensing-with-golden-reference structure (founder retains golden-reference subassemblies, calibration methodology, factory test benches; milestone-based contracts via an HK-structured IP entity) appended to F-01's product and plan; Hengyunchang/Injet buyer evidence already cited.
4. **F-08 -> A-02 (device-strategy workstream, cross-file)**: 2027 SiC interruption-duty die-characterization study (di/dt, avalanche energy, series sharing vs press-pack IGBT baselines) + fail-short press-pack qualification concept inserted into A-02's 2026-2029 plan with a `merge_import_notes` field; A MD annotated.

## Source-ID imports (eligibility-checked against 90_BIBLIOGRAPHY/sources.json)

- P3R2-F-02 demand_source_ids: +L03-052 (accepted, verified_non_india_origin).
- P3R2-F-02 technical_source_ids: +L07-009 (accepted + verified_non_india_origin; the bibliography also carries a stale non-accepted duplicate row for this ID - flagged for the orchestrator's next ledger merge/dedupe).
- P3R2-A-02: no new IDs (imported content cites already-present L08-001/003/004/017). **Eligibility note:** F-08's own demand anchor L08-016 is `accepted: false` in both the bibliography and the L08 ledger; it was NOT imported anywhere. The rejected F-08 record retains it as audit trail only.

## Fix highlights (binding gates written into seed fields)

- Binding pre-company gates added/codified: F-03 (2029 machine-builder co-dev), F-04 (2028 paid OEM evaluation = externalization proof), F-05 (2028 CN export-certification LOI + unsubsidized repower economics), F-06 (2029 OEM/EPC evaluation paired with E-14-class traction), F-07 (CN swap-procurement openness + 2028 charger-OEM co-dev), F-09 (2028 evaluation windows in one named ARDAP rebuild program), F-10 (2028 battery-equipment OEM LOI; POD-at-speed end-2029 binding), F-11 (coil-life >=10,000 shots end-2028 binding; contractualized IP split), F-15 (2028 EPC retrofit study with >=3% gain target), F-16 (paid premium commitment inside the 2028 beta), F-17 (priced option: $150k cap + 2028 one-of-three dated-signal gate), F-19 (2028 colocation pilot + operator LOI), F-20 (two paid OEM evaluations 2028), F-22 (2027 manufacturing-partner route), F-23 (2029 lender-requirement/developer-LOI + OEM design-in).
- P4 pre-promotion requirements written into competition/plan fields: F-02 (OCEM/Danfysik incumbency), F-03 (Calnetix-class + turbine-OEM in-house), F-04 (SKF S2M/Calnetix/Waukesha teardown), F-05 (Danfoss Editron/Dana TM4/BAE teardown), F-06 (Hitachi/ABB optical-CT map), F-07 (Staubli/Phoenix Contact/Huber+Suhner map), F-10 (Tecnar/Evident/Baker Hughes check), F-16 (Nordson MARCH/Panasonic/Samco roadmap), F-20 (full HV competitor map), F-22 (CN vacuum-cap makers + Comet/Jennings verification).
- Overbroad claims corrected in text (JSON + MD): F-02 "nobody productized" restated as the integrated extraction/dump + leads + acceptance-protocol island; F-05 "no standardized kit exists" downgraded to judgment pending teardown; F-20 "one dominant vendor" flagged as judgment requiring the P4 map.
- Stale-source refresh obligations (rule 18) written into F-10 and F-11 (L16-028, 2022 vintage).
- Portfolio pre-agreements codified: F-01+F-22 single RF-components company if both survive P4; L11 concentration cap (C-07/C-22/F-15/F-23, at most two funded); F-20 fold-down into C-09's platform family.

## Coherence check (2030 contract fields)

All edited seeds retain a coherent 2030 contract: TRLs unchanged; every FIX seed carries explicit dated 2027/2028/2029 gates inside `precompany_plan_2026_2029`; `launch_2030_timing_thesis` untouched except where flag changes altered meaning (F-06's CN leg relabeled royalty-upside in the demand-trigger field); kill-date years unchanged (2034) with binding gates added inside the kill-date text for F-02 (entry SKU end-2031), F-03 (co-dev end-2029), F-10 (POD end-2029), and F-11 (coil life end-2028) - all tighten, never loosen, existing triggers; `precompany_validation_by_2029` unchanged. MD sections carry per-seed annotations matching the JSON fields, plus the F-06 header/flag downgrade and the two surgical claim corrections.

Quota state after this application matches the judge's reckoning: 62 distinct concepts across A-F, CN gate 35/36 (FAIL by 1); closure is routed to micro-wave G or the F-04/F-20 P4-conditional upgrades per the adjudication - not to re-flagging F-06 or resurrecting F-13/F-14.

Tooling note: applied by `tools/apply_p3r2_r2_fixes_json.py` and `tools/apply_p3r2_r2_fixes_md.py` (retained for audit; atomic assert-then-write).

---

# P3R2 fix-application log — round 3 (micro-wave G, final)

Applied 2026-07-13 by the Fable 5/xhigh fix-application agent (claude-fable-5, effort xhigh), implementing `P3R2_ELEGANCE_ADJUDICATION_R3.{md,json}` rulings on the 3 wave-G seeds (`P3R2_G_cn_microwave.{json,md}`). Wave-G verdicts: 0 PROMOTE, 3 FIX, 0 REJECT — no merges, no rejects, no records deleted this round. Founder-profile firewall respected.

## Verdict marking (3 wave-G seeds)

### P3R2-G-01
- elegance_verdict = FIX_APPLIED (N7/E7/C6/V6/T5)
- (1) L07-053 "trade bifurcation constrains Western metrology imports" over-read DELETED from painful_job, launch-timing thesis, and competition; INFICON FY2025 figures (Americas -12.4% to $156.4M; APAC +19.2% to $168.6M) retained as market-structure context only — APAC growth evidences continued import availability.
- (2) BINDING 2028 evidence gate added to the 2026-2029 plan: documented facility acceptance requirements imposed on fabricators at delivery (tender technical annex, facility vacuum-acceptance spec, or fabricator quality requirement) — the buyer-existence proof that fabricators, not institutes, own conditioning/acceptance; no 2029 paid pilot without it.
- (3) Multi-tender cadence proof beyond CEPC made a BINDING P4 pre-promotion condition (plan + timing-risk fields): re-date the 2021-vintage L07-045 anchor AND evidence >=2 additional CN chamber-class tenders (HEPS follow-on/CSNS/ASIPP-pattern). NIM-class CN metrology anchor for witness-standard traceability named as a P4 task.
- (4) Judge's primary-source verification incorporated into the evidence notes (painful_job + buyer context): PRC-registration + manufacturer eligibility clause independently confirmed in the primary tender document at ccnta.cn on 2026-07-13; the L07-045 ledger claim_supported/locator repair remains assigned to the orchestrator (freeze condition 2).

### P3R2-G-02
- elegance_verdict = FIX_APPLIED (N6/E6/C6/V6/T6)
- (1) "ISO 11137-1:2025 forces fleet-wide re-qualification" over-claim corrected to a PERMISSIVE energy-limit increase in painful_job, launch-timing thesis, and demand trigger; a second BINDING 2028 evidence gate added: named operators/OEMs actually uprating to 11 MeV/7.5 MeV, else the ISO trigger de-weights to CN consumables + localization demand only.
- (2) Merchant-targetry incumbency map (ARTMS/Comecer-class + IBA's own target business) made PRE-PROMOTION BINDING for the cyclotron-target leg in the competition field, with the pre-agreed re-scope to the e-beam/X-ray window+converter leg if merchant targetry is already served; the "no merchant, certified, cross-platform supplier" claim marked as judgment pending that map.
- (3) Surrogate-heat-flux validity limit DECLARED in first_experiment (validates thermo-mechanics + interlock speed only; NOT radiation-driven foil degradation — embrittlement, blistering); beam-time validation added to the 2028 co-development gate.
- (4) Beam-components portfolio pre-agreement recorded in the competition field: G-02 joins the R2 portfolio evaluation with F-09/F-20 (C-09/D-07 adjacency) at P4 — at most one funded beam-components company.

### P3R2-G-03
- elegance_verdict = FIX_APPLIED (N5/E7/C7/V7/T6)
- (1) The ~12%/78% HVDC-vs-UPS penetration figure demoted to explicitly UNVERIFIED and not load-bearing in painful_job and demand trigger (raw-ledger WebSearch synthesis; not in the verified L02-048 record); P4 must re-source an eligible CN installed-base/penetration figure before final scoring; the 8-12-year refresh-cycle assumption labeled INFERENCE to be evidenced in P4. CN conversion-base logic now rests only on verified anchors (L02-048 Panama deployments, L02-049 Autrans/East-Data-West-Computing, L02-054 architecture churn). Wave-G MD header carries the matching R3 correction.
- (2) The 2029 frame-agreement gate SPLIT per market in plan and kill-date fields: no US frame agreement by end-2029 -> US leg folds to niche lab tooling; no CN integrator frame agreement by end-2029 -> CN leg downgrades to license-only with the honest flag change applied (F-06 precedent). Combined end-2031 kill retained (tightened, not loosened).
- (3) Instrument-major DC-acceptance roadmaps (Keysight/Chroma/Hioki/Fluke) + CN certification institutes (CQC/CEPREI-class service-only testing) made a PRE-PROMOTION BINDING P4 competitor map in the competition field; the third-party-acceptance willingness thesis must survive it.
- Judge's note applied: first_experiment restated to assume loaner/partner 100 kW 800VDC testbed hardware ($300k covers injector/analyzer build and test time, not testbed ownership).

## Source-ID changes

- None. No source IDs added, removed, or substituted in any G seed; all cited IDs remain accepted and verified_non_india_origin / verified_multinational_allowed in `90_BIBLIOGRAPHY/sources.json` (judge-checked this session: zero quarantine intersections, zero rejected-record citations). L02-048 remains cited for its verified content (Panama 240VDC deployments); only the penetration figure formerly attributed to it was demoted.

## Coherence check (2030 contract fields)

All three seeds retain a coherent 2030 contract: TRLs unchanged (4); primary_market flags unchanged (G-01/G-02 CN-primary, G-03 US+CN dual — no CN credibility added or removed); kill-date years unchanged (2034-12-31) with G-03's per-market 2029 downgrade gates added inside the kill-date field (tighten, never loosen); `precompany_validation_by_2029` unchanged; every seed now carries dated BINDING 2028/2029 gates inside `precompany_plan_2026_2029` and BINDING P4 pre-promotion conditions inside competition/plan fields; `launch_2030_timing_thesis` edited only where the corrected claims altered meaning (G-01 bifurcation removal; G-02 permissive-uprating contingency). MD sections carry per-seed "[FIX applied ...]" annotations matching the JSON edits, plus the header R3 correction. JSON re-parsed clean (3 records).

Freeze-condition state after this application: condition 1 (wave-G fix application logged with FIX_APPLIED marks and all required fixes in substantive fields) is SATISFIED by this round. Remaining conditions owned by the orchestrator: L07-045 ledger claim_supported repair; G-03 penetration-figure re-source in P4; rule-18 refreshes (L16-028 for F-10/F-11; L07-045 re-dating for G-01); concentration caps at portfolio selection (incl. beam-components portfolio F-09/F-20/G-02, at most one funded). Judge's reckoning stands: 65 distinct concepts A-G, all longlist gates PASS, CN-gate sensitivity margin +2 with the three named conditional legs to be resolved in P4.
