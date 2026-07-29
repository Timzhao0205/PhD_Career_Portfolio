# P3R2 round-2 fix application (MD side).
# Mirrors the JSON edits in P3R2_F_cn_topup.md and P3R2_A_us_pain.md.
# Atomic: all anchors asserted before writing. Run from project root.
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FMD = "20_OPPORTUNITY_POOL/P3R2_F_cn_topup.md"
AMD = "20_OPPORTUNITY_POOL/P3R2_A_us_pain.md"
text = open(FMD, encoding="utf-8").read()
atext = open(AMD, encoding="utf-8").read()


def sub1(s, old, new):
    assert old in s, "anchor not found: " + old[:80]
    assert s.count(old) == 1, "anchor not unique: " + old[:80]
    return s.replace(old, new, 1)


# 1. Header blockquote
text = sub1(text, "secondary markets.\n\n---",
            "secondary markets.\n\n"
            "> **Adjudication R2 applied 2026-07-13:** the second-pass verdicts\n"
            "> (`P3R2_ELEGANCE_ADJUDICATION_R2.md`) have been applied to all 23 seeds - 3 PROMOTE\n"
            "> (F-01, F-02, F-12), 15 FIX_APPLIED, 5 REJECT/MERGED (F-08 REJECT with import to A-02;\n"
            "> F-13 REJECT; F-14 REJECT with import to F-01; F-18 merged into F-03; F-21 merged into\n"
            "> F-02). F-06 downgraded to US-primary (china_beachhead false) per the honesty ruling.\n"
            "> Post-merge distinct wave-F concepts: 18. Annotations at the end of each seed section\n"
            "> match the JSON `elegance_verdict`/`fix_applied_notes` fields. See\n"
            "> `P3R2_FIX_APPLICATION_LOG.md` (round-2 section).\n\n---")

# 2. F-06 header downgrade
text = sub1(text,
            "## P3R2-F-06 — Precision wideband DC sensing platform for HVDC, electrolysis, magnets (dual US+CN)",
            "## P3R2-F-06 — Precision wideband DC sensing platform for HVDC, electrolysis, magnets (US-primary; CN license chapter only — downgraded 2026-07-13)")

# 3. F-02 white-space restatement
text = sub1(text,
            "- **Why incumbents miss it:** magnet PSU work is trapped between national-lab in-house\n"
            "  builds and one-off vendor projects; nobody has productized the skid because until\n"
            "  merchant magnet sales (2024–26) there was no serial buyer.",
            "- **Why incumbents miss it:** magnet PSU work is trapped between national-lab in-house\n"
            "  builds and one-off vendor projects; precision converters themselves are catalog items\n"
            "  (OCEM/Danfysik-class), so the unproductized white space is the integrated\n"
            "  extraction/dump + leads + acceptance-protocol island — not converter novelty (P4\n"
            "  incumbency map required pre-promotion).")

# 4. F-02 product entry SKU
text = sub1(text,
            "clean interface to third-party quench\n  detection.\n",
            "clean interface to third-party quench\n  detection. Entry SKU (absorbed from F-21): catalog binary current leads (0.5–20 kA)\n"
            "  and vacuum-tight instrumented feedthroughs with certified heat-load datasheets.\n")

# 5. F-05 kit-claim hedge
text = sub1(text,
            "affordable path but no standardized kit exists; E-hybrid",
            "affordable path but off-highway repower electrics remain per-project engineering ('no\n"
            "  standardized kit' downgraded to judgment pending the P4 teardown); E-hybrid")

# 6. Per-seed annotation bullets
ann = {
    1: "- **[Adjudication 2026-07-13 R2 - PROMOTE]:** strongest new dual seed (N6/E7/C7/V7/T7); non-obvious by the convergence test; clean A-10 complement. Absorbed F-14's licensing-with-golden-reference mechanics (milestone-based contracts via an HK-structured IP entity; founder retains golden references, calibration methodology, and factory test benches) as the CN chapter's IP structure; Hengyunchang/Injet buyer evidence already cited (L06-042/043/044). Comet-Synertia absorption risk covered by the kill trigger.",
    2: "- **[Adjudication 2026-07-13 R2 - PROMOTE]:** (N5/E7/C7/V7/T7). Promote-conditions applied: white space restated as the integrated extraction/dump + leads + acceptance-protocol island (precision converters are catalog items - P4 OCEM/Danfysik incumbency map required pre-promotion); CFS bundling stays the named US ceiling. Absorbed F-21 as entry SKU: catalog binary leads/instrumented feedthroughs, certified heat-load datasheets, end-2031 <$1M entry-SKU gate (source imports +L03-052, +L07-009).",
    3: "- **[FIX applied 2026-07-13 R2]:** P4 Calnetix-class/turbine-OEM in-house incumbent map made a pre-promotion requirement; 2029 machine-builder co-development agreement made a binding gate; single-source CN TAM (L04-051) now carries a pre-scale triangulation gate; $900k experiment staged behind the requirements interviews; absorbed F-18 as the CN plant-integration/licensing chapter (EPC co-bidding memorandum, Xinjiang first-set alignment, rollout-industrialization framing).",
    4: "- **[FIX applied 2026-07-13 R2]:** 2028 paid OEM evaluation made the binding externalization proof; 2027/P4 teardown of SKF S2M/Calnetix/Waukesha vs the semiconductor-duty claim; CN leg conditional - a named CN pump/tool-OEM design-in channel must be evidenced in P4 or primary_market downgrades to US (INFICON APAC attribution is not buyer evidence); 2032 internal kill retained. Counted dual-conditional in the judge's quota.",
    5: "- **[FIX applied 2026-07-13 R2]:** defensible core restated as the UL/IEC/GB certification matrix + dual-personality interface (kit-existence claim downgraded to judgment pending P4 teardown vs Danfoss Editron/Dana TM4/BAE); 2028 CN OEM export-certification LOI made binding; unsubsidized repower economics model due 2028; B-14 interface personality bought as a module, not rebuilt.",
    6: "- **[FIX applied 2026-07-13 R2 - flags downgraded]:** primary_market US+CN -> US, china_beachhead -> false (honesty ruling: State Grid domestic-only, CN revenue 'license royalties at best' - the C-12/C-21 condition; CN license chapter retained in text, not counted toward CN quota). 2029 OEM/EPC evaluation agreement made binding and paired with E-14-class third-party protection traction; P4 Hitachi/ABB optical-CT incumbency map required - the wedge is the demonstrated round-robin result, not an assertion.",
    7: "- **[FIX applied 2026-07-13 R2]:** CN-leg binding gate added (P4 confirmation that CN swap-equipment component procurement is open to licensed outsiders); 2028 charger-OEM co-development made binding; P4 connector-major incumbent map (Staubli/Phoenix Contact/Huber+Suhner) with the 10,000-mate-cycle duty dataset as wedge proof; sequencing fixed: port/mining (funded) before trucking (MCS volume risk).",
    8: "- **[Adjudication 2026-07-13 R2 - REJECT]:** double contingency - component supplier into the atlas's documented unconverged meshed-MVDC showstopper, one level below A-02 without its productization wedge; the offered demand anchors do not hold (GEV orders are not MVDC-protection procurement; State Grid valves license-out only); press-pack incumbents absorb the socket if meshed DC arrives. Die-characterization workstream imported into P3R2-A-02 (see the A batch). Record retained as audit trail.",
    9: "- **[FIX applied 2026-07-13 R2]:** 2028 evaluation windows inside one NAMED rebuild program (ARDAP channel) made the binding gate; P4 evidence on prime merchant-buy behavior (negative -> re-scope to lab spares/aftermarket and re-size); two-paying-customers-by-2032 kill retained; P4 evaluates a beam-components portfolio company with C-09/D-07 adjacency.",
    10: "- **[FIX applied 2026-07-13 R2]:** CN demand bridge made binding (battery-equipment OEM co-development/design-in LOI by 2028); US pipeline leg de-weighted until a named operator/NDT-service evaluation exists by 2028; POD-at-speed end-2029 kill made binding; L16-028 (2022) refresh required before final scoring; P4 incumbent check extended to Tecnar-class laser-UT and Evident/Baker Hughes production NDT.",
    11: "- **[FIX applied 2026-07-13 R2]:** coil-life gate (>=10,000 shots at spec by end-2028) made binding - the engineering thesis; 2028 CN integrator co-development with a contractualized IP split (founder retains pulsed power + recipes; integrator sells); 2028 cost-per-joint/line-rate model vs ultrasonic AND laser (laser is the real substitute); L16-028 refresh required before final scoring.",
    12: "- **[Adjudication 2026-07-13 R2 - PROMOTE]:** best CN-primary seed of the wave (N6/E6/C7/V6/T7): dated CCS 2025-edition trigger, type-approval-dossier moat, honest JV structure, $300k class-design-appraisal experiment, named CATL-bundling kill. P4: confirm the non-CATL integrator/shipyard share, map CSSC-affiliated suppliers, scope the DNV/ABS export hedge.",
    13: "- **[Adjudication 2026-07-13 R2 - REJECT]:** demand real and dated (Baogang, July 2026) but structurally captured: Huawei-ecosystem integrators self-supply, CRRC-class suppliers replicate fast (no hard physics), foreign content in SOE mine-safety chains politically fragile (self-flagged), RMB3.75M tender scale implies project-shaped thin-margin revenue, thin atlas technical base. Demand without a defendable technical wedge in the hardest-access market. Record retained as audit trail.",
    14: "- **[Adjudication 2026-07-13 R2 - REJECT]:** B-12 precedent applies in full - in license-into-China know-how models the licensee is the accumulating asset; the seed names its own mechanism as the kill risk and golden-reference retention does not survive its own 2032 absorption horizon. Licensing mechanics + Hengyunchang/Injet buyer evidence imported into P3R2-F-01's CN chapter. Record retained as audit trail.",
    15: "- **[FIX applied 2026-07-13 R2]:** 2028 EPC retrofit-study partnership made the binding demand gate (measured park losses must justify skid cost, >=3% gain target); Sungrow/LONGi verticalization kill retained; P4 must evidence a licensed JV winning park-management retrofit scope at one named SOE park; boundary coordination with C-07/F-23 codified - one L11 power story, at most two funded.",
    16: "- **[FIX applied 2026-07-13 R2]:** 2028 beta must carry a PAID premium commitment (>=30% premium thesis tested before the 2030 gate, not at it); 2027 experiment must validate inline surface-energy proxy robustness at line rate; P4 Nordson MARCH/Panasonic/Samco roadmap check (closed-loop treat-to-spec is absorbable by the incumbent premium tier).",
    17: "- **[FIX applied 2026-07-13 R2]:** held as a priced option - pre-company spend capped at the $150k prototype until a dated signal exists; 2028 gate: documented ISO/IEC revision work-item, EU/US market-surveillance action on handheld Class-4 welders, or insurer/OEM requirement (one of three, else kill at end-2030); P4 chases European welding-association handheld-laser safety materials for an eligible dated anchor; OEM design-in LOI remains the second gate.",
    18: "- **[Adjudication 2026-07-13 R2 - MERGED INTO P3R2-F-03]:** self-flagged CN-primary licensing variant of F-03's cartridge (same CNNC ecosystem, same single-source TAM). EPC co-bidding memorandum, Xinjiang first-set alignment, and rollout-industrialization framing imported into F-03's CN chapter. Record retained as audit trail; not independently promotable.",
    19: "- **[FIX applied 2026-07-13 R2]:** P4 must source operator incident/warranty data (pain evidence is inference from spec structure + fleet scale); 2028 colocation pilot + operator LOI made binding; the 12-month aging study must produce the failure-signature dataset that IS the moat (else a CDU-vendor feature - bundling kill stands); C-05 boundary confirmed: pair commercially, do not merge prematurely. Counted 1/4 against the datacenter cap.",
    20: "- **[FIX applied 2026-07-13 R2]:** P4 competitor map made a pre-promotion requirement (Spellman AND Advanced Energy HiTek/UltraVolt, AMETEK/Glassman, Matsusada, iseg, Heinzinger, Technix, XP Power, CN HV makers) - the one-dominant-vendor thesis must survive it; two PAID OEM evaluations by 2028 binding; CN chapter reduced pending a named CN OEM/tender channel in P4 (else license notes); pre-agreed fold-down into C-09's platform family if OEM appetite fails. Counted dual-conditional.",
    21: "- **[Adjudication 2026-07-13 R2 - MERGED INTO P3R2-F-02]:** self-flagged fold. Catalog binary-lead SKU, instrumented feedthroughs, certified heat-load datasheets, and the end-2031 <$1M standalone milestone imported into F-02 as its entry SKU + gate. Record retained as audit trail; not independently promotable.",
    22: "- **[FIX applied 2026-07-13 R2]:** vacuum-components manufacturing-partner route made a binding 2027 gate (the $450k experiment does not make a qualified line); one PAID OEM qualification by 2029; P4 must map CN vacuum-capacitor makers (credible domestic caps collapse the CN licensing leg) and verify the Comet/Jennings supply structure; portfolio pre-agreement: if F-01 and F-22 both survive P4 they merge into one RF-components company.",
    23: "- **[FIX applied 2026-07-13 R2]:** binding 2029 gate added (named H2Hub lender/financier technical requirement or developer LOI referencing instrumented warranty evidence, plus one OEM design-in agreement); the 2,000 h A/B experiment made the binding existence proof (measurable degradation-rate reduction); data-interface pre-agreement with C-22 (no duplicate bench); battery/fuel-cell retarget hedge scoped (not asserted) by 2029.",
}

for n in range(1, 24):
    hdr = f"## P3R2-F-{n:02d} "
    start = text.index(hdr)
    if n < 23:
        p = f"\n\n## P3R2-F-{n + 1:02d} "
        pos = text.find(p, start)
        assert pos != -1, f"next-header anchor missing after F-{n:02d}"
        text = text[:pos] + "\n" + ann[n] + text[pos:]
    else:
        p = "\n\n---\n\nGeneric EE/CE transfer note"
        pos = text.find(p, start)
        assert pos != -1, "terminator anchor missing after F-23"
        text = text[:pos] + "\n" + ann[23] + text[pos:]

# 7. A-02 MD import note
atext = sub1(atext,
             "- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical MVDC hybrid breaker. Documented showstopper niche; MVDC adoption pace and $1.5M pre-company experiment are the honest risks; lean on DC-GRIDS/ORNL facilities.",
             "- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical MVDC hybrid breaker. Documented showstopper niche; MVDC adoption pace and $1.5M pre-company experiment are the honest risks; lean on DC-GRIDS/ORNL facilities.\n"
             "- **[Merge-import 2026-07-13 R2]:** absorbed P3R2-F-08 (wave-F REJECT) as the device-strategy workstream: 2027 SiC interruption-duty die-characterization study (di/dt, avalanche energy, series sharing vs press-pack IGBT baselines) and fail-short press-pack qualification concept - cheap, publishable, useful regardless of breaker-market timing; cited to already-present eligible sources (L08-001/003/004/017); F-08's L08-016 is not accepted in the ledger and was not imported.")

with open(FMD, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
with open(AMD, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(atext)
print("MD edits applied OK (23 annotations + 5 surgical edits + A-02 import note)")
