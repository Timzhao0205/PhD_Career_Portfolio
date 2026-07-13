# P3R2 round-2 fix application (JSON side).
# Applies P3R2_ELEGANCE_ADJUDICATION_R2.json rulings to P3R2_F_cn_topup.json and
# the F-08 import to P3R2_A_us_pain.json. Atomic: all edits asserted in memory
# before any file is written. Run from project root.
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FP = "20_OPPORTUNITY_POOL/P3R2_F_cn_topup.json"
AP = "20_OPPORTUNITY_POOL/P3R2_A_us_pain.json"
fseeds = json.load(open(FP, encoding="utf-8"))
aseeds = json.load(open(AP, encoding="utf-8"))
F = {r["idea_id"]: r for r in fseeds}
A = {r["idea_id"]: r for r in aseeds}
assert len(F) == 23


def repl(rec, field, old, new):
    v = rec[field]
    assert old in v, f"{rec['idea_id']}.{field}: anchor not found: {old[:60]}"
    rec[field] = v.replace(old, new, 1)


def app(rec, field, extra):
    rec[field] = rec[field].rstrip() + " " + extra


# ---------------- F-01 PROMOTE (absorb F-14 mechanics) ----------------
r = F["P3R2-F-01"]
app(r, "product", "CN chapter delivered as licensing-with-golden-reference (absorbed from F-14): the CN licensee manufactures under milestone-based contracts while the founder retains golden-reference subassemblies, calibration methodology, and factory test benches - certification power stays with the licensor (HK-structured IP entity).")
app(r, "precompany_plan_2026_2029", "CN-chapter licensing mechanics (from F-14): HK-structured IP entity and milestone-based license contracts scoped 2028, know-how held in calibration/test assets.")
r["merge_import_notes"] = "2026-07-13 R2: absorbed P3R2-F-14 (REJECT) as the CN chapter's IP mechanics - licensing-with-golden-reference structure (founder retains golden-reference subassemblies, calibration methodology, and factory test benches; milestone-based contracts via an HK-structured IP entity) and the Hengyunchang/Injet buyer evidence (L06-042/043/044, already cited). F-14's standalone license-into-China model was rejected on the B-12 precedent; imported here only as mechanics subordinate to F-01's hardware business."
r["elegance_verdict"] = "PROMOTE"
r["adjudication_note"] = "2026-07-13 R2 adjudication (PROMOTE, N6/E7/C7/V7/T7): strongest new dual seed; genuinely non-obvious by the convergence test (matching documented unresolved in atlas, absent from all 100 prior seeds); clean complement to A-10 (impedance delivery vs process control); CN leg eligible and country-specific (<12% localization L06-054, named buyers, mature-node scope, 2027 export gate). Absorb F-14's licensing-with-golden-reference mechanics as CN-chapter IP structure. Comet Synertia absorption risk covered by kill trigger; 60 MHz voltage/Q parity is the honest key uncertainty."

# ---------------- F-02 PROMOTE (absorb F-21, restate white space) ----------------
r = F["P3R2-F-02"]
app(r, "product", "Entry SKU (absorbed from F-21): catalog binary current leads (0.5-20 kA classes) and vacuum-tight instrumented feedthroughs with published, certified heat-load and quench-tolerance datasheets.")
repl(r, "competition_outlook_2030",
     "OCEM/Danfysik-class magnet-PSU specialists (judgment; to be mapped in P4), converter groups inside national labs, CN institute in-house builds; CFS vertical integration is the ceiling on the US side.",
     "OCEM/Danfysik-class magnet-PSU specialists - precision magnet converters are catalog items, so the white space is the integrated extraction/dump + leads + acceptance-protocol island, not converter novelty (P4 incumbency map is a pre-promotion requirement); converter groups inside national labs, CN institute in-house builds; CFS vertical integration/bundling remains the named ceiling on the US side (monitor).")
app(r, "precompany_plan_2026_2029", "Entry-SKU track (from F-21): 5 kA instrumented binary-lead prototype with a university magnet group 2027-28; certified heat-load datasheet methodology and first lab purchase orders 2029.")
repl(r, "commercial_readiness_kill_date",
     "2034 (kill if by end-2033 there is no paid drive-and-dump order from a merchant magnet buyer or lab)",
     "2034 (kill if by end-2033 there is no paid drive-and-dump order from a merchant magnet buyer or lab; entry-SKU gate: >=$1M cumulative lead/feedthrough orders by end-2031, else the entry line folds to catalog-support only)")
assert "L03-052" not in r["demand_source_ids"]
r["demand_source_ids"].append("L03-052")
assert "L07-009" not in r["technical_source_ids"]
r["technical_source_ids"].append("L07-009")
r["merge_import_notes"] = "2026-07-13 R2: absorbed P3R2-F-21 (MERGED_INTO_P3R2-F-02) as the entry SKU - catalog binary current leads (0.5-20 kA), vacuum-tight instrumented feedthroughs, certified heat-load datasheets, end-2031 <$1M entry-SKU gate. Source imports: demand +L03-052, technical +L07-009 (both accepted + verified_non_india_origin in 90_BIBLIOGRAPHY/sources.json). Promote-conditions applied: white space restated (extraction/dump + leads + acceptance-protocol island, not converter novelty) with P4 OCEM/Danfysik incumbency map pre-promotion; CFS bundling stays the named US ceiling."
r["elegance_verdict"] = "PROMOTE"
r["adjudication_note"] = "2026-07-13 R2 adjudication (PROMOTE, N5/E7/C7/V7/T7): merchant-magnet commerce (L03-035) is a real structural change; ASIPP tenders (L01-037/038) are dated CN evidence with honest big-science-only access; D-01 complement split mirrors the endorsed A-02/E-14 pattern. Promote-conditions: P4 OCEM/Danfysik-class incumbency map; white space restated as the integrated extraction/dump + leads + acceptance-protocol island; CFS bundling the named US ceiling; absorb F-21 as entry SKU."

# ---------------- F-03 FIX (absorb F-18) ----------------
r = F["P3R2-F-03"]
r["precompany_plan_2026_2029"] = "2026-27 requirements interviews with 5+ machine builders (US/EU/KR) - the $900k drive-stand experiment is staged behind these findings (no build until interviews confirm the cartridge specification); 2027-28 build 250 kW/30 krpm generator + AFE prototype on a drive rig with representative load transients; 2029 one co-development agreement with an ORC or sCO2 integrator - BINDING GATE; CN plant-integration/licensing chapter (absorbed from F-18) scoped with counsel in 2028: EPC co-bidding memorandum and electrical-island package v1 aligned to Xinjiang first-set completion (~2028, L04-051)."
repl(r, "competition_outlook_2030",
     "Calnetix-class high-speed machine specialists (judgment; P4 to map), turbine OEM in-house (Turboden/Hanwha, L04-047/055), CN institute-affiliated suppliers (CAS-IET/SMDERI ecosystem, L04-102/106).",
     "Calnetix-class merchant high-speed PM+converter specialists sell exactly this pairing for ORC - P4 incumbent map centered on Calnetix-class and turbine-OEM in-house (Turboden/Hanwha, L04-047/055) is a PRE-PROMOTION requirement the white-space claim must survive; CN institute-affiliated suppliers (CAS-IET/SMDERI ecosystem, L04-102/106).")
app(r, "demand_trigger_2030_2034", "CN retrofit TAM is single-source (L04-051): triangulation from eligible sources is a pre-scale gate - no scale assumption before it.")
r["commercial_readiness_kill_date"] = "2034 (kill if no machine-builder design win by end-2033; BINDING GATE: signed machine-builder co-development agreement by end-2029)"
r["merge_import_notes"] = "2026-07-13 R2: absorbed P3R2-F-18 (MERGED_INTO_P3R2-F-03) as the CN plant-integration/licensing chapter - EPC co-bidding memorandum concept, Xinjiang first-set timeline alignment (~2028 completion), rollout-industrialization framing. No new source IDs required (F-18's L04-048/051 and L04-102/106/111/113 already cited here)."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: (1) P4 incumbent map (Calnetix-class merchant high-speed PM+converter + turbine-OEM in-house) made a pre-promotion requirement; (2) 2029 machine-builder co-development agreement made a binding gate; (3) single-source CN retrofit TAM (L04-051) given a pre-scale triangulation gate; (4) F-18 absorbed as the CN plant-integration/licensing chapter; (5) $900k drive-stand experiment staged behind the 2026-27 requirements-interview findings."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E6/C5/V7/T6): fills a real in-pool gap (electrical half of heat-to-power machines) with dual dated anchors (Fervo-Turboden; Chaotan One + first-set); merchant white-space claim must survive Calnetix-class incumbency; CN TAM single-source."

# ---------------- F-04 FIX ----------------
r = F["P3R2-F-04"]
r["precompany_plan_2026_2029"] = "2026-27 retrofit a commercial maglev turbopump rotor with an open controller; publish shock-ride-through and touchdown-life results; 2027 teardown of SKF S2M/Calnetix/Waukesha merchant controllers against the semiconductor-grade duty claim (P4 requirement - the wedge must survive it); 2028 paid evaluation with one pump or compressor OEM - BINDING GATE: a paying OEM is the proof that pump OEMs will externalize AMB electronics (the thesis's stated key uncertainty); 2029 second vertical (sCO2 rig or flywheel) demo."
app(r, "demand_trigger_2030_2034", "CN leg CONDITIONAL: a named CN pump/tool-OEM design-in channel must be evidenced in P4 or primary_market downgrades to US (INFICON APAC revenue attribution, L07-053, is not buyer evidence).")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: 2028 paid OEM evaluation made the binding proof that pump OEMs will externalize AMB electronics; 2027 teardown of SKF S2M/Calnetix/Waukesha merchant controllers vs the semiconductor-grade duty claim scoped as a P4 requirement; CN leg made conditional (named CN pump/tool-OEM design-in channel in P4 or primary_market downgrades to US - INFICON APAC revenue attribution is not buyer evidence); 2032 internal kill retained."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E6/C6/V6/T6): real 30-year documented reliability gap (L07-010..013); thesis lives or dies on OEM externalization; thinnest CN leg among surviving dual seeds - counted dual-conditional in quota."

# ---------------- F-05 FIX ----------------
r = F["P3R2-F-05"]
repl(r, "painful_job",
     "but no standardized heavy-duty repower electronics kit exists.",
     "but off-highway repower electrics remain per-project engineering (the stronger 'no standardized heavy-duty repower kit exists' claim is downgraded to judgment pending the P4 competitive teardown).")
app(r, "product", "The dual-standard interface personality is bought as a module (B-14-class), not rebuilt - the defensible core is the UL/IEC/GB certification matrix plus the dual-personality interface, not kit existence.")
repl(r, "precompany_plan_2026_2029",
     "2028 one grant-funded pilot repower with a terminal operator plus one CN OEM export-certification engagement; 2029",
     "2028 one grant-funded pilot repower with a terminal operator plus one CN OEM export-certification engagement LOI (BINDING GATE) and an unsubsidized repower economics model (EPA grants mostly fund new equipment - the repower inference must be evidenced, not assumed); 2029")
repl(r, "competition_outlook_2030",
     "Dana TM4, BAE Systems, Danfoss Editron, ZF (judgment names; P4 to source);",
     "Dana TM4, BAE Systems, Danfoss Editron, ZF - P4 competitive teardown REQUIRED against these off-highway electrics lines, with the defensible core restated as the certification matrix + dual-personality interface;")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: defensible core restated as the UL/IEC/GB certification matrix + dual-personality interface (kit-existence claim downgraded to judgment pending P4 teardown vs Danfoss Editron/Dana TM4/BAE); 2028 CN OEM export-certification LOI made binding; unsubsidized repower economics model due 2028 (EPA grants mostly fund new equipment); B-14 interface personality bought as a module, not rebuilt."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E5/C6/V6/T6): US 'no standardized kit' claim likely overstated; CN certification-demand leg (Western-cert competence sold to XCMG-class exporters) is honest and distinctive."

# ---------------- F-06 FIX + flag change ----------------
r = F["P3R2-F-06"]
assert r["primary_market"] == "US+CN" and r["china_beachhead"] is True
r["primary_market"] = "US"
r["china_beachhead"] = False
repl(r, "precompany_plan_2026_2029",
     "2029 one protection-OEM or EPC evaluation agreement; CN license-out term sheet scoped 2029.",
     "2029 one protection-OEM or EPC evaluation agreement - BINDING GATE, go/no-go paired with evidence of E-14-class third-party protection winning sockets (the merchant sensing layer exists only if that layer wins); CN license-out term sheet scoped 2029 (royalty upside only; not a market leg).")
repl(r, "demand_trigger_2030_2034",
     "CN: State Grid annual UHV equipment tender batches (L08-034 pattern) via a licensed CN manufacturer.",
     "CN (license-royalty upside only, not a counted market leg - State Grid procurement is domestic-only): State Grid annual UHV equipment tender batches (L08-034 pattern) via a licensed CN manufacturer.")
app(r, "competition_outlook_2030", "P4 map of Hitachi Energy/ABB optical-CT incumbency is required; the wedge must be the demonstrated combined accuracy+bandwidth+open-protocol result of the published round-robin, not an assertion.")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: HONESTY FLAG CHANGE primary_market US+CN -> US, china_beachhead true -> false (seed's own text: State Grid domestic-only, CN revenue 'license royalties at best' - same condition that downgraded C-12/C-21; CN license chapter retained in text, not counted toward CN quota); 2029 OEM/EPC evaluation agreement made binding with go/no-go paired to E-14-class third-party protection traction; P4 map of Hitachi Energy/ABB optical-CT incumbency required - wedge is the demonstrated combined accuracy+bandwidth+open-protocol round-robin result, not an assertion."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX with flag change, N5/E7/C7/V6/T6): elegant measurement-layer complement to E-14 with a cheap decisive experiment; structurally dependent on third-party protection winning sockets. Honesty ruling applied: primary_market US, china_beachhead false."

# ---------------- F-07 FIX ----------------
r = F["P3R2-F-07"]
r["precompany_plan_2026_2029"] = "2026-27 thermal test bench replicating IEC TS 63379 3,000 A duty with non-PFAS coolants; 2028 co-development agreement with one charger OEM (NREL emulator ecosystem, L10-049) - BINDING; CN leg BINDING GATE: P4 confirmation that CN swap-equipment component procurement is open to licensed outside suppliers before any CN investment (no eligible source documents CN conductive MW-charging demand); 2029 1e5-cycle contact endurance dataset; sequencing: port/mining applications (funded, L10-048) before trucking (MCS volume risk)."
repl(r, "competition_outlook_2030",
     "Staubli, Phoenix Contact, Huber+Suhner on cooled cables (judgment; P4 to source);",
     "Staubli, Phoenix Contact, Huber+Suhner on cooled cables - P4 incumbent map REQUIRED, with the wedge proven by the 10,000-mate-cycle duty dataset, not asserted;")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: CN-leg binding gate added (P4 confirmation that CN swap-equipment component procurement is open to licensed outsiders); 2028 charger-OEM co-development made binding; P4 connector-major incumbent map (Staubli/Phoenix Contact/Huber+Suhner) with the 10,000-mate-cycle duty dataset as wedge proof; sequencing fixed - port/mining (funded) before trucking (MCS volume risk)."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N6/E6/C6/V6/T6): genuine no-man's-land between EVSE OEMs and connector vendors; CN swap evidence country-specific (SPIC, GB/T 45926, CCS); no eligible source documents CN conductive MW-charging demand - CN leg gated."

# ---------------- F-08 REJECT (import -> A-02) ----------------
r = F["P3R2-F-08"]
r["duplicate_of"] = "P3R2-A-02"
r["elegance_verdict"] = "REJECT"
r["adjudication_note"] = "2026-07-13 R2 adjudication (REJECT, N5/E6/C4/V7/T3): double contingency - component supplier to breaker/valve OEMs whose own market (meshed MVDC) is the atlas's documented unconverged showstopper; demand anchors do not hold (GEV datacenter electrification orders are not MVDC-protection procurement; State Grid valves license-out only); Infineon/Hitachi/Fuji press-pack scale absorbs the socket if meshed DC arrives. IMPORT into P3R2-A-02 executed 2026-07-13: 2027 SiC interruption-duty die-characterization study + fail-short press-pack qualification concept (see P3R2_A_us_pain.json merge_import_notes). Record retained as audit trail."

# ---------------- F-09 FIX ----------------
r = F["P3R2-F-09"]
r["precompany_plan_2026_2029"] = "2026-27 ceramic-metal joining and multipactor test capability at a university/lab partner; 2028 supply first evaluation windows into one NAMED rebuild program (ARDAP channel, L05-031/032) - BINDING GATE; 2029 lifetime dataset (thermal cycling + RF conditioning) published; P4: evidence on whether tube primes buy reliability-critical components merchant - if negative, re-scope to lab spares/aftermarket and re-size honestly; P4 also evaluates one beam-components portfolio company pairing F-09 with C-09/D-07 adjacency; CN big-science channel scoped through international procurement counsel."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: 2028 evaluation windows inside one named rebuild program (ARDAP channel) made the binding gate; P4 evidence requirement on prime merchant-buy behavior (if negative, re-scope to lab spares/aftermarket and re-size honestly); two-paying-customers-by-2032 kill retained; P4 evaluation of a beam-components portfolio company with C-09/D-07 adjacency added."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E6/C6/V5/T6): documented failure mode (L05-014), real qualification wedge, honest small-TAM admission; whether tube primes buy reliability-critical 'internal art' merchant is the killer question."

# ---------------- F-10 FIX ----------------
r = F["P3R2-F-10"]
r["precompany_plan_2026_2029"] = "2026-27 lab demonstration on Al-Cu tab welds with destructive-test correlation; 2028 battery-equipment OEM co-development/design-in LOI - BINDING GATE (the CN demand bridge: inline volumetric QC demand is inferential, only the equipment channel is documented); US pipeline leg DE-WEIGHTED until a named operator/NDT-service evaluation exists by 2028 (standards-cycle timing is not a procurement trigger); 2029 standards engagement (ISO 13588 revision cycle) and speed/POD dataset; refresh L16-028 (2022-vintage buyer concentration) with a current filing before final scoring."
r["commercial_readiness_kill_date"] = "2034 (BINDING: kill if POD/speed target unmet by end-2029; kill if no OEM design-in by end-2032)"
repl(r, "competition_outlook_2030",
     "Evident/Olympus, Zetec, Baker Hughes NDT (judgment; P4 to source);",
     "Evident/Olympus, Zetec, Baker Hughes production NDT and Tecnar-class industrial laser-UT - P4 incumbent check REQUIRED;")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: CN demand bridge made binding (battery-equipment OEM co-development/design-in LOI by 2028); US pipeline leg de-weighted until a named operator/NDT-service evaluation exists by 2028; POD-at-speed end-2029 kill made binding; L16-028 (2022-vintage) refresh required before final scoring (rule 18); P4 incumbent check extended to Tecnar-class industrial laser-UT and Evident/Baker Hughes production NDT."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N7/E7/C6/V6/T5): highest-novelty dual seed (first NDT play in the pool); physics risk on thin reflective Al-Cu at line rate honestly named; pipeline standards-cycle timing is too soft to carry demand."

# ---------------- F-11 FIX ----------------
r = F["P3R2-F-11"]
r["precompany_plan_2026_2029"] = "2026-27 university-lab MPW rig: establish Al-Cu weldability windows and coil-life engineering (the known killer); BINDING coil-life gate: >=10,000 shots at spec by end-2028 - the entire engineering thesis; 2028 co-development agreement with one CN equipment integrator with the IP split CONTRACTUALIZED (founder retains pulsed-power hardware + process recipes; integrator sells the machine); 2028 cost-per-joint and line-rate model versus ultrasonic AND laser welding (laser is the real substitute); 2029 pilot cell on a busbar application; refresh L16-028 (2022) with a current filing before final scoring."
r["commercial_readiness_kill_date"] = "2034 (BINDING: kill if coil life <10,000 shots at spec by end-2028; kill if no integrator agreement by end-2030)"
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: coil-life gate (>=10,000 shots at spec by end-2028) made binding; 2028 CN integrator co-development agreement now requires a contractualized IP split (founder retains pulsed power + recipes; integrator sells); 2028 cost-per-joint and line-rate model vs ultrasonic AND laser welding added (laser is the real substitute); L16-028 (2022) refresh required before final scoring."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N7/E7/C6/V6/T5): genuinely non-obvious productization of a 15-year non-productized process; correctly identifies coil economics as blocker-turned-wedge; technology-push honestly gated (no battery maker has asked for MPW)."

# ---------------- F-12 PROMOTE ----------------
r = F["P3R2-F-12"]
r["elegance_verdict"] = "PROMOTE"
r["adjudication_note"] = "2026-07-13 R2 adjudication (PROMOTE, N6/E6/C7/V6/T7): best CN-primary seed of the wave - dated country-specific regulatory trigger (CCS Rules 2025 edition effective 2025-12-31, ~2-year revision cadence), national-benchmark vessel class, type-approval-dossier moat, honest JV structure (concede manufacturing, retain protection IP + type approval), $300k class-design-appraisal experiment, named CATL-bundling kill. P4: confirm non-CATL integrator/shipyard share; map CSSC-affiliated suppliers; scope DNV/ABS export hedge."

# ---------------- F-13 REJECT ----------------
r = F["P3R2-F-13"]
r["elegance_verdict"] = "REJECT"
r["adjudication_note"] = "2026-07-13 R2 adjudication (REJECT, N5/E4/C6/V5/T5): demand real and dated (Baogang tender July 2026) but structurally captured - Huawei-ecosystem integrators self-supply hardware, CRRC-class suppliers replicate the kit fast (no hard physics), foreign content in SOE mine-safety chains politically fragile (self-flagged), RMB3.75M tender scale implies project-shaped thin-margin revenue, atlas technical base admittedly thin. Demand without a defendable technical wedge in the hardest-access market. Record retained as audit trail."

# ---------------- F-14 REJECT (import -> F-01) ----------------
r = F["P3R2-F-14"]
r["elegance_verdict"] = "REJECT"
r["adjudication_note"] = "2026-07-13 R2 adjudication (REJECT, N4/E5/C5/V5/T4): B-12 precedent applies in full - in license-into-China know-how models the licensee is the accumulating asset; the seed names its own central mechanism as the kill risk (licensee R&D, poached teams); Hengyunchang's RMB1.5B IPO proceeds fund in-house capability; golden-reference retention does not survive the seed's own 2032 absorption horizon. IMPORT into P3R2-F-01 executed 2026-07-13: licensing-with-golden-reference/test-bench structure and Hengyunchang/Injet buyer evidence as F-01's CN-chapter mechanics (see F-01 merge_import_notes). Record retained as audit trail."

# ---------------- F-15 FIX ----------------
r = F["P3R2-F-15"]
r["precompany_plan_2026_2029"] = "2026-27 model park-level electrical losses/imbalance with published Kuqa-type data; 2028 EPC retrofit-study partnership (access via engineering-services JV) - BINDING DEMAND GATE: measured park-level imbalance/stray-current losses must justify skid cost (>=3% utilization/specific-energy gain target) before any pilot build; 2029 pilot skid on a 4-stack sub-array at a partner site; P4: evidence that a licensed JV can win park-management retrofit scope at one named SOE park (no such tender exists yet - the audit-pressure trigger is inferential); boundary coordination with C-07 (rectifier) and F-23 (stack envelope) codified: one L11 power story, three sockets, at most two funded; explicitly monitor Sungrow/LONGi verticalization as the kill signal."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: 2028 EPC retrofit-study partnership made the binding demand gate (measured park-level losses must justify skid cost; >=3% gain target); Sungrow/LONGi verticalization kill retained; P4 requirement added - evidence that a licensed JV can win park-management retrofit scope at one named SOE park; C-07/F-23 boundary coordination codified (one L11 power story, at most two funded)."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N6/E7/C6/V6/T5): most elegant CN-primary framing ('string-inverter moment for hydrogen'); respects the L11 stack-overcapacity negative finding; demand mechanism (SOE audits forcing utilization retrofits) is inferential - gated."

# ---------------- F-16 FIX ----------------
r = F["P3R2-F-16"]
r["precompany_plan_2026_2029"] = "2026-27 integrate candidate inline sensors (contact-angle proxies, OES dose models) on a lab plasma cell - the 2027 experiment must validate inline surface-energy proxy robustness AT LINE RATE (the stated key uncertainty); 2028 beta at one CN PCB maker via tender channel (L01-114 shows the procurement route is open) - the beta must carry a PAID premium commitment: the >=30% premium thesis is tested before the 2030 gate, not at it (documented evidence is category procurement, not metrology-premium demand); 2029 yield-correlation dataset that justifies premium pricing."
app(r, "first_experiment", "Must validate proxy robustness at production line rate.")
app(r, "competition_outlook_2030", "P4 roadmap check REQUIRED (Nordson MARCH/Panasonic/Samco): closed-loop treat-to-spec is absorbable by the incumbent premium tier.")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: 2028 beta now requires a paid premium commitment (>=30% premium thesis tested before the 2030 gate, not at it); 2027 experiment scoped to validate inline surface-energy proxy robustness at line rate; P4 Nordson MARCH/Panasonic/Samco roadmap check added (closed-loop treat-to-spec is absorbable by the incumbent premium tier)."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E6/C7/V6/T6): converts the rejected B-15 knife-fight into a treat-to-spec premium position with a documented open procurement channel (L01-114) and durable category (L01-115); documented evidence is category demand, not metrology-premium demand - gated."

# ---------------- F-17 FIX (priced option) ----------------
r = F["P3R2-F-17"]
r["precompany_plan_2026_2029"] = "HELD AS A PRICED OPTION: pre-company spend capped at the $150k prototype until a dated regulatory signal exists. 2026-27 prototype sensing + shutoff chain and human-factors testing; 2028 GATE (one of three, else kill at the existing end-2030 trigger): a documented ISO/IEC revision work-item, an EU/US market-surveillance action on handheld Class-4 welders, or an insurer/OEM requirement; one CN OEM design-in LOI remains the second gate; P4 discovery lead: European welding-association handheld-laser safety materials (judge's external check found safety materials but no dated enforcement action) - chase for an eligible dated anchor; 2029 certification body (TUV-class) assessment of module architecture."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: held as a priced option - pre-company spend capped at the $150k prototype until a dated signal exists; 2028 gate added (documented ISO/IEC revision work-item, EU/US market-surveillance action on handheld Class-4 welders, or insurer/OEM requirement - one of three, else kill at the existing end-2030 trigger); P4 discovery lead added (European welding-association handheld-laser safety materials - chase for an eligible dated anchor); OEM design-in LOI remains the second gate."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX - option, N6/E6/C7/V5/T4): real gap (ISO 11553-2 dated 2007 vs documented export explosion) but the entire demand thesis is an undated regulatory contingency (judge's external check found association safety materials, no dated enforcement); adjudicated as an honest option purchase, D-16-style."

# ---------------- F-18 MERGED -> F-03 ----------------
r = F["P3R2-F-18"]
r["duplicate_of"] = "P3R2-F-03"
r["elegance_verdict"] = "MERGED_INTO_P3R2-F-03"
r["adjudication_note"] = "2026-07-13 R2 adjudication (REJECT - duplicate of P3R2-F-03, self-flagged): CN-primary licensing variant of F-03's cartridge in the same CNNC ecosystem with the same single-source TAM. Imported into F-03: EPC co-bidding memorandum concept, Xinjiang first-set timeline alignment, rollout-industrialization framing. Record retained as audit trail; not independently promotable."

# ---------------- F-19 FIX ----------------
r = F["P3R2-F-19"]
r["precompany_plan_2026_2029"] = "2026-27 accelerated-aging loop studies establishing failure signatures for PG25-class fluids (GS Caltex/OCP context, L14-049/041) - the 12-month aging study must produce the failure-signature dataset that IS the moat (else the concept is a CDU-vendor feature); 2028 pilot skid in one colocation hall plus one operator LOI - BINDING; P4 REQUIREMENT: source operator incident/warranty data (direct pain evidence is currently inference from spec structure + fleet scale); 2029 fleet analytics MVP; C-05 boundary confirmed (lab qualification vs in-service operations + consumables): pair commercially, do not merge prematurely; CN route via licensed manufacture with a domestic thermal vendor (Envicool-class, L14-043)."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: P4 requirement to source operator incident/warranty data; 2028 colocation pilot + one operator LOI made binding; 12-month aging study scoped to produce the failure-signature dataset that IS the moat (existing CDU-bundling kill trigger stands); C-05 boundary confirmed (lab qualification vs in-service operations + consumables) - pair commercially, do not merge prematurely."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N6/E6/C6/V7/T6): water-treatment-industry archetype applied to DLC fleets; only F datacenter-correlated seed (counted 1/4 against the cap), partially downturn-resistant (installed fluid ages regardless); direct pain evidence thin and CDU-vendor absorption the default outcome - gated."

# ---------------- F-20 FIX ----------------
r = F["P3R2-F-20"]
repl(r, "painful_job", "(Spellman, judgment)", "(Spellman, judgment; P4 pre-promotion competitor map required)")
r["precompany_plan_2026_2029"] = "2026-27 100 kV/10 kW prototype with ripple/arc-recovery characterization; 2028 two PAID OEM evaluations (one US tool OEM, one accelerator lab) - BINDING; 2029 reliability database + acceptance-protocol publication; CN chapter REDUCED pending evidence (no eligible source shows CN accelerator OEMs outsourcing precision HV): name a CN OEM/tender channel in P4 or the CN chapter becomes license notes; CN channel scoped via big-science procurement and non-controlled application counsel."
repl(r, "competition_outlook_2030",
     "Spellman (dominant, will defend), Technix/Heinzinger, XP Power/Excelitas lines, CN: Dongwen-class HV makers scaling (judgment names; P4 to map). Wedge must be arc-recovery + telemetry, not price.",
     "Spellman (dominant, will defend) AND Advanced Energy (HiTek/UltraVolt), AMETEK/Glassman, Matsusada, iseg, Heinzinger, Technix, XP Power/Excelitas lines, CN Dongwen-class HV makers scaling - P4 competitor map is a PRE-PROMOTION requirement: the 'effectively one dominant vendor' thesis is held only as judgment and must survive it, or the seed collapses to niche lab supply; pre-agreed fold-down: the DC-HV line folds into C-09's platform family if OEM appetite fails. Wedge must be arc-recovery + telemetry, not price.")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: P4 competitor map made a pre-promotion requirement (Spellman AND Advanced Energy HiTek/UltraVolt, AMETEK/Glassman, Matsusada, iseg, Heinzinger, Technix, XP Power, CN HV makers); two paid OEM evaluations by 2028 made binding; CN chapter reduced pending evidence (name a CN OEM/tender channel in P4 or it becomes license notes); fold-down of the DC-HV line into C-09's platform family pre-agreed if OEM appetite fails."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N4/E5/C6/V5/T5): thesis rests on a competitive claim held only as judgment; highest hidden-commodity risk among surviving F seeds; CN leg reduced pending evidence - counted dual-conditional in quota."

# ---------------- F-21 MERGED -> F-02 ----------------
r = F["P3R2-F-21"]
r["duplicate_of"] = "P3R2-F-02"
r["elegance_verdict"] = "MERGED_INTO_P3R2-F-02"
r["adjudication_note"] = "2026-07-13 R2 adjudication (REJECT - duplicate of P3R2-F-02, self-flagged fold): imported into F-02 as entry SKU - catalog binary-lead SKU, instrumented feedthrough line, certified heat-load datasheets, end-2031 <$1M standalone milestone (now F-02's entry-SKU gate). Record retained as audit trail; not independently promotable."

# ---------------- F-22 FIX ----------------
r = F["P3R2-F-22"]
r["precompany_plan_2026_2029"] = "2026-27 process development (ceramic-metal brazing, bellows) with a vacuum-components partner - BINDING 2027 GATE: signed manufacturing-partner route (precision brazing/bellows craft is both moat and barrier; the $450k experiment does not make a qualified line); 2028 first capacitor family qualified against Comet datasheet specs; 2029 one PAID OEM qualification (gate); P4: map existing CN vacuum-capacitor makers (credible domestic caps collapse the CN licensing leg) and verify the Comet/Jennings supply structure; portfolio pre-agreement: if F-01 and F-22 both survive P4, merge into one RF-components company (two L06 RF-chain startups is one too many); CN licensing scoped with export counsel."
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: vacuum-components manufacturing-partner route made a binding 2027 gate; one paid OEM qualification by 2029 added; P4 must map existing CN vacuum-capacitor makers (credible domestic caps collapse the CN licensing leg) and verify the Comet/Jennings supply structure; portfolio pre-agreement added - if F-01 and F-22 both survive P4, merge into one RF-components company."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N5/E5/C6/V5/T6): single-source arbitrage (Comet 23.8% single-customer concentration, L05-034) with a sensible solid-state dual-track hedge bridging to F-01; craft barrier cuts both ways - manufacturing-partner route gated."

# ---------------- F-23 FIX ----------------
r = F["P3R2-F-23"]
r["precompany_plan_2026_2029"] = "2026-27 codify published stress-degradation maps into envelope algorithms; 2028 bench validation on a short stack with accelerated stress tests; BINDING 2029 GATE: one named H2Hub lender/financier technical requirement or a developer LOI referencing instrumented warranty evidence, PLUS one OEM design-in agreement (the demand mechanism is anticipatory - developers buy only if lenders force it); data-interface pre-agreement with C-22 (its benches calibrate the envelope maps this device enforces - no duplicate bench build); battery/fuel-cell warranty retarget hedge SCOPED (not asserted) by 2029."
app(r, "first_experiment", "BINDING: the A/B result must show a measurable degradation-rate reduction - the product's existence proof.")
r["fix_applied_notes"] = "2026-07-13 R2 FIX applied: binding 2029 gate added (one named H2Hub lender/financier technical requirement or developer LOI referencing instrumented warranty evidence, plus one OEM design-in agreement); 2,000 h A/B experiment made the binding existence proof (measurable degradation-rate reduction); data-interface pre-agreement with C-22 (no duplicate bench build); battery/fuel-cell warranty retarget hedge scoped (not asserted) by 2029."
r["elegance_verdict"] = "FIX_APPLIED"
r["adjudication_note"] = "2026-07-13 R2 adjudication (FIX, N6/E7/C7/V7/T6): most intelligent new L11 seed - converts published stress-degradation science into bankability hardware with genuinely independent US (H2Hub lender exposure) and CN (Kuqa-class utilization audits) legs; demand mechanism is anticipatory - gated on lender forcing."

# ---------------- A-02 import from F-08 ----------------
r = A["P3R2-A-02"]
repl(r, "precompany_plan_2026_2029",
     "track ARPA-E DC-GRIDS cohort results (L02-034). 2028:",
     "track ARPA-E DC-GRIDS cohort results (L02-034). 2027: SiC interruption-duty die-characterization study (di/dt, avalanche energy, series sharing vs press-pack IGBT baselines) and fail-short press-pack qualification concept - device-strategy workstream imported from wave-F seed F-08 (2026-07-13); cheap, publishable, and feeds the module design regardless of breaker-market timing (L08-001/003/004/017). 2028:")
new = {}
for k, v in r.items():
    if k == "elegance_verdict":
        new["merge_import_notes"] = "2026-07-13 R2: imported P3R2-F-08's (wave-F REJECT) device-strategy workstream - 2027 SiC interruption-duty die-characterization study (di/dt, avalanche energy, series sharing vs press-pack IGBT baselines) and fail-short press-pack qualification concept; cheap, publishable, useful regardless of breaker-market timing. No new source IDs: L08-001/003/004/017 already cited and eligible; F-08's L08-016 is not accepted in the ledger and was NOT imported."
    new[k] = v
idx = aseeds.index(r)
aseeds[idx] = new

# verdict tally check
tally = Counter(x["elegance_verdict"] for x in fseeds)
assert tally["PROMOTE"] == 3 and tally["FIX_APPLIED"] == 15 and tally["REJECT"] == 3, tally
assert tally["MERGED_INTO_P3R2-F-02"] == 1 and tally["MERGED_INTO_P3R2-F-03"] == 1
assert F["P3R2-F-06"]["primary_market"] == "US" and F["P3R2-F-06"]["china_beachhead"] is False

with open(FP, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(fseeds, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
with open(AP, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(aseeds, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("JSON edits applied OK:", dict(tally))
