"""Deterministic builder for outputs/04_APPLICATION_SCORECARD.csv (stage 40).

Reusable: edit ROWS and re-run to regenerate the scorecard without
hand-editing CSV quoting. Mirrors the stage-20/30 precedent
(tools/build_02_estimator_csv.py, tools/build_03_risk_register.py).

Scoring rubric (full explanation in outputs/04_COLLABORATION_STRATEGY.md):
each of hybrid_value, identifiability_path, radiation_fit, experimental_access,
publication_value, collaboration_leverage is scored 0-5 (5 = most favorable).
prototype_cost and thesis_dilution_risk are scored 0-5 with 5 = LEAST
favorable (highest cost / highest risk) and are inverted before averaging
into strategic_score. technical_score = mean(hybrid_value,
identifiability_path, radiation_fit). strategic_score = mean(
experimental_access, publication_value, collaboration_leverage,
5-prototype_cost, 5-thesis_dilution_risk). Vetoes per DECISION_FRAMEWORK.md
override any score.
"""
import csv
import os

HEADER = [
    "application", "problem", "incumbent_diagnostic", "hybrid_value",
    "identifiability_path", "radiation_fit", "experimental_access",
    "publication_value", "collaboration_leverage", "prototype_cost",
    "thesis_dilution_risk", "technical_score", "strategic_score", "veto",
    "evidence_ids", "rank", "recommendation", "next_gate",
]

ROWS = [
    ["Tokamak long-pulse/plasma magnetic diagnostics (ITER/WEST/JT-60SA/EAST/DEMO)",
     "Long-pulse/steady-state tokamak operation needs non-inductive DC field sensing because Mirnov/Rogowski/flux-loop integrators drift unboundedly as pulse length grows (now ~1000 s at WEST, hours targeted at ITER/DEMO); DEMO's antimony-Hall program states inductive sensors 'require supplementation,' not merely improvement (C33, H065, P004, P009).",
     "Mirnov/pickup coils, Rogowski coils, flux/diamagnetic loops; ITER's outer-vessel steady-state sensor set (OVSS) already runs a system-level architecture pairing bismuth Hall sensors with inductive sensors specifically to correct coil drift (P003, C27).",
     "4/5 -- strongest documented fit of any lane: the only application where the DC-Hall-corrects-coil-drift half of the hybrid is hardware-proven at machine scale (C02, C27). OVSS is a system-level pairing of separate sensor heads, not a co-located hybrid, and the reverse direction (coil identifies Hall drift) is untested on any tokamak (C06) -- the genuine open contribution, not a re-derivation of OVSS.",
     "4/5 -- stage-20 CASE D (machine-current + validated vacuum field model, rank 4/4) is directly available via logged PF-coil currents and cross-machine-validated field models (P010, JT-60SA to ITER); zero-field/between-shot epochs (CASE C2) resolve offset. Bounded by Theorem-1 common-mode blindness between anchor epochs -- an honest, stated limit, not a defect unique to this lane.",
     "4/5 -- this is the one lane where the architecture's radiation-compensation value proposition is squarely relevant: DEMO in-vessel coils are qualified to intense neutron/gamma loads (P009), and the JET radiation-hard-Hall (RHP) 11.5-year/>19,000-pulse record including a D-T campaign is the strongest operational radiation precedent in the entire evidence base (C05, H003/H007). JT-60SA's cited 200 degC/9 MGy figures (P006) remain full-text-unconfirmed.",
     "2/5 hardware, 4/5 algorithm -- direct in-vessel deployment on ITER/DEMO is inaccessible within 24 months; WEST/JT-60SA/EAST are operating now and cross-machine algorithm validation is already a live practice (P010). Realistic near-term access is to validate the CASE-D estimator against public tokamak current-log/field-model data or the user's own HSX data, not to install new hardware in a tokamak vessel.",
     "5/5 -- directly targets the mission's sharpest documented gap (C06; C36a-b: no source jointly proves the reverse-calibration direction or demonstrates in-situ radiation-aware Hall recalibration in any fusion environment); sits inside the user's existing RSI-track trajectory and the exact venues (Nuclear Fusion, Fusion Engineering and Design, RSI) that already carry this literature.",
     "4/5 -- a small, mature, actively publishing, collaborative community (Prague/Lviv/Italy JET-RHP line; KFE/KAIST 2025 Kalman-fusion paper, H001/H002) working on precisely this problem class, not a cold-call target -- genuine technical overlap exists on both sides.",
     "2/5 low-moderate -- near-term validation (T0 simulation, T1 bench) needs no tokamak-specific new hardware; reuses the existing GaN Hall + wound coil + machine-current-log architecture already being built for HSX (stage-30 MVD).",
     "2/5 low-moderate -- consistent generalization of the user's own HSX trajectory (project 02/03) rather than a new domain; risk is scope creep toward ITER/DEMO-scale radiation claims, which root CLAUDE.md and MISSION.md explicitly exclude from the user's first-author experimental work (T3 stays collaborator-led, stage-30 section 9.4).",
     "4.0/5 (mean of hybrid_value, identifiability_path, radiation_fit = [4,4,4])",
     "3.4/5 (mean of experimental_access[hardware]=2, publication_value=5, collaboration_leverage=4, cost-inverted=3, dilution-inverted=3)",
     "None. Caveat only: the reverse-direction (coil-informs-Hall) claim and any in-vessel radiation demonstration remain unproven (C06) and must not be asserted as already solved.",
     "C02;C05;C06;C27;C33;C36;H001;H002;H003;H007;H065;P003;P004;P006;P009;P010",
     "2", "approach-after-bench-proof",
     "Stage-30 G1 (bench truth: anchored-hybrid calibration repeatable across >=3 cycles within T0-predicted uncertainty; alpha_S, beta_b characterized) -- ideally demonstrated first on HSX or public tokamak current-log data before any approach to IPP-Prague/KFE. G4/G5 (environmental qualification) remain T3, collaborator-led, and are explicitly NOT a prerequisite for this recommendation (stage-30 section 9.4)."],

    ["Stellarator field mapping, alignment/error-field correction, and coil-current/field validation (W7-X/LHD/TJ-II/HSX-class)",
     "Vacuum field verification during commissioning is essential (error fields, trim-coil correction) but the incumbent method (e-beam/fluorescent-screen mapping) cannot coexist with plasma and runs only during infrequent commissioning windows (C32); no literature has ever proposed a Hall+coil hybrid for this lane (C32, systematic absence after documented search).",
     "Electron-beam/fluorescent-screen vacuum flux-surface mapping (P018-P020) plus trim-coil correction informed by it (P012-P014); W7-X design criterion is ~1e-4 relative coil-current accuracy (P016).",
     "3/5 -- the pair adds nothing once plasma is present (same DC/quasi-static blindness as any lane, CASE F), but during vacuum-shot commissioning windows the field is exactly known from machine coil currents plus a validated model -- precisely stage-20's CASE D anchor condition, realized in its purest form because the user already operates the machine.",
     "5/5 -- the strongest identifiability access of any lane precisely because it is the user's own facility: CASE D (machine current + validated vacuum field model, rank 4/4) is directly available at HSX with logged coil currents and an existing field model, requiring no new external reference chain.",
     "3/5 not applicable by design, neutral -- no environmental-qualification literature exists for stellarator field mapping (a gap, not a finding either way); commissioning-era measurements are low-radiation, and root CLAUDE.md/MISSION.md explicitly state no neutron/gamma experiment is planned for the user's HSX work, so absence of radiation content here is consistent with mission scope, not a weakness.",
     "5/5 -- this is the user's own facility with an established UW-Madison collaboration (Goodman, Gallenberger, Geiger) and an HSX hardware install already targeted for August 2026 (project 02/03); no external access barrier exists.",
     "4/5 -- a genuinely open, evidence-free niche (C32) gives clean novelty, and this work directly is the planned RSI (~Mar 2027) vector-probe paper (project 03); it is a narrower contribution than the tokamak radiation angle but the one with the fastest, most certain path to a result.",
     "2/5 external -- the primary execution partner is the user's own existing HSX collaboration, not a new external group; W7-X (IPP Greifswald, MHD Research Unit) is the one genuine new-collaboration angle for cross-machine benchmarking or algorithm comparison, scored moderate rather than high because no shared measurement problem has yet been defined with them.",
     "1/5 lowest -- this is the already-funded, already-planned project 02/03 hardware; no new spend attributable to this stage's recommendation.",
     "0/5 lowest -- not dilution; this lane is the thesis trajectory itself (HSX vector-probe RSI paper) and is the necessary T1/T2 validation venue that the tokamak and every other lane's recommendation depends on.",
     "3.7/5 (mean of hybrid_value, identifiability_path, radiation_fit[neutral] = [3,5,3])",
     "4.0/5 (mean of experimental_access=5, publication_value=4, collaboration_leverage=2, cost-inverted=4, dilution-inverted=5)",
     "None.",
     "C32;P012;P013;P014;P016;P018;P019;P020",
     "1", "approach-now (internal -- no outreach required; the W7-X benchmarking recommendation is monitor, see 04_COLLABORATOR_CANDIDATES.csv)",
     "Stage-30 G0 (T0 simulation, in progress this mission) then G1 (T1 bench truth = HSX MVD hardware install, Aug 2026 target; anchored-hybrid calibration repeatable across >=3 cycles). This gate sequence is a prerequisite feeding every other lane's recommendation, not a separate outreach question."],

    ["Z-pinch/pulsed-power current and field measurements (Sandia Z/MAGPIE/gas-puff, LTDs)",
     "Need robust current/field measurement in extreme EMI/blast/debris environments at ns-us timescales with dI/dt to ~200 kA/ns (P021, P023); no persistent DC baseline exists within a single shot.",
     "B-dot probes and Rogowski coils, cross-calibrated against a current-viewing resistor; the community's own 'sensor fusion' precedent (P025) deliberately fuses two inductive sensors (B-dot + Rogowski, +/-13-15% error), bypassing Hall sensors entirely.",
     "1/5 -- direct documented counter-evidence: the field already solved its redundancy need without Hall (C30), and Hall-effect current sensors are independently documented as EMI-susceptible to tangential RF E-fields (P028) -- an extrapolation from power-electronics testing, but the direction of the evidence is unfavorable, not merely absent.",
     "1/5 -- no persistent field/DC content exists within a single ns-us shot for CASE-D-style anchoring, and between shots the field returns to near-zero; the stage-30 estimator architecture has no engineered anchor that applies at this timescale.",
     "1/5 -- radiation here is a brief single-shot burst, not the cumulative-fluence drift the compensation architecture (stage 30) is built to track; the mission's radiation-compensation value proposition does not transfer to this stressor class.",
     "1/5 -- Sandia Z is a large, expensive, single-shot national-lab facility; not a realistic 24-month access target for an outside PhD student with no current tie to the program.",
     "1/5 -- would be arguing against an entrenched, already-optimized, well-evidenced incumbent choice with no identified theoretical opening.",
     "2/5 -- Sandia's MIF/pulsed-power program (Mykonos) is active and publishes openly, but no shared measurement problem exists where a Hall+coil hybrid adds value over the community's own inductive-fusion solution.",
     "4/5 high -- surviving blast/debris/ns-bandwidth EMI would require substantial new hardware and qualification unrelated to any HSX asset.",
     "4/5 high -- would require building expertise in an entirely different pulsed-power diagnostics domain, unrelated to HSX plasma work.",
     "1.0/5 (mean of hybrid_value, identifiability_path, radiation_fit = [1,1,1])",
     "1.2/5 (mean of experimental_access=1, publication_value=1, collaboration_leverage=2, cost-inverted=1, dilution-inverted=1)",
     "Yes -- 'no credible advantage over a simpler single-sensor solution' (DECISION_FRAMEWORK.md): the community already fused two inductive sensors bypassing Hall (C30); and 'no identifiable calibration path' (no persistent DC baseline within a shot for any stage-20 anchor case).",
     "C30;P021;P022;P023;P025;P028",
     "6", "do-not-prioritize",
     "None -- vetoed at the architecture level (C30); no stage-30 gate applies."],

    ["Magneto-inertial fusion/plasma-jet experiments (MagLIF, PLX, ZaP, Zap Energy Century)",
     "Need current/field diagnostics through severe EMI/thermal/blast stress in single-shot liner-implosion or plasma-jet experiments (P029, P034); in the highest-stress regions the field has already abandoned magnetic probes.",
     "Multi-axis B-dot (Mirnov-style) coil arrays at boundary/electrode locations; where probes cannot physically survive, the field uses optical PDV (P031) or Zeeman spectroscopy (P032) instead of any magnetic sensor.",
     "1/5 -- where the environment already forced abandonment of magnetic probes entirely (C35), a Hall+coil hybrid adds no survivability. A boundary/wall-location niche at lower-field, single-shot devices is conceivable but wholly undemonstrated (Unknown, not inferred favorably).",
     "1/5 -- mostly single-shot with no persistent field for within-shot anchoring; a stable pre-shot calibration reference for a boundary niche is speculative and absent from the evidence base.",
     "2/5 -- MagLIF has a real, documented D-T neutron yield (~1e12, P030) -- a genuine radiation environment exists -- but PLX/ZaP are low-yield/non-fusion and must not be merged with MagLIF's radiation context (C35 caveat); no source quantifies drift at a boundary-probe location specifically.",
     "1/5 -- Sandia MagLIF and LANL's plasma-jet/MIF program (P-24 Thermonuclear Plasma Physics) are not broadly accessible testbeds for an outside stellarator-focused PhD student; Zap Energy's repetitive Century platform (0.2 Hz, P037) is a possible access outlier but its technical details are bibliographic-only, unconfirmed.",
     "2/5 -- an undemonstrated niche could be novel but is speculative without a concretely defined measurement problem; no direct-prior-art gap was identified with confidence.",
     "1/5 -- no clear shared measurement problem has been identified with any group in this lane.",
     "4/5 high -- a boundary-sensor package surviving liner-implosion/plasma-jet conditions differs substantially from any HSX-class hardware.",
     "5/5 highest -- furthest domain from HSX plasma diagnostics of any lane evaluated.",
     "1.3/5 (mean of hybrid_value, identifiability_path, radiation_fit = [1,1,2])",
     "1.0/5 (mean of experimental_access=1, publication_value=2, collaboration_leverage=1, cost-inverted=1, dilution-inverted=0)",
     "Partial -- 'no credible advantage over a simpler single-sensor solution' applies to the core/high-stress region where probes are already abandoned (C35); the boundary niche is not formally vetoed but is entirely unevidenced (Unknown), so it cannot be scored as an opportunity either.",
     "C35;P029;P030;P031;P032;P034;P037",
     "5", "do-not-prioritize",
     "None -- no gate applies; if the boundary-probe niche is ever revisited it needs its own dedicated G0-equivalent simulation feasibility study, not inheritance from the stellarator/tokamak MVD plan."],

    ["Superconducting magnets, HTS rotating machinery, motors/generators (trapped-field magnets, quench detection, field poles)",
     "Need field mapping/monitoring of persistent-mode trapped fields and quench detection in HTS magnets and machines (P038-P051).",
     "Scanning/fixed Hall-probe arrays for the static/persistent state (P047, P048); pick-up/search coils only during the brief (de)magnetization transient (P049); NMR as the field's own accepted precision cross-check for the persistent state (P042).",
     "1/5 -- structurally poor fit: a coil is blind to a static trapped field once magnetization completes (no dB/dt) -- the clearest single-sentence veto condition in the whole evidence base (C28).",
     "1/5 -- the coil contributes nothing during the dominant (persistent/DC) operating mode; only during the ms-scale magnetization pulse does dB/dt exist, and even there NMR, not a coil, is the accepted reference (C28).",
     "3/5 not applicable, neutral -- temperature (cryogenic, 4-77 K), not radiation, is the dominant stressor; documented Hall temperature-coefficient behavior to 0.001%/K by doping (P050, P051) is directly reusable as literature input to the stage-30 alpha_S characterization task without requiring this application to be pursued.",
     "2/5 -- Cambridge's Bulk Superconductivity Group is active and well-published, but no shared measurement problem exists for the hybrid architecture specifically.",
     "2/5 -- low for a hybrid-architecture paper (the architecture does not apply in the dominant regime); the only reusable value is the temperature-coefficient literature already cited into stage 30 without needing this application pursued.",
     "2/5 -- low as an application target; the P050/P051 cryogenic Hall data is already usable via citation, with no outreach needed.",
     "3/5 moderate -- not being pursued as an application; would require cryogenic infrastructure far outside current HSX hardware if it ever were.",
     "4/5 high if pursued -- requires motor/generator and cryogenic-magnet domain expertise unrelated to HSX plasma diagnostics.",
     "1.7/5 (mean of hybrid_value, identifiability_path, radiation_fit[neutral] = [1,1,3])",
     "1.8/5 (mean of experimental_access=2, publication_value=2, collaboration_leverage=2, cost-inverted=2, dilution-inverted=1)",
     "Yes -- structural 'no credible advantage over a simpler single-sensor solution' in the persistent-mode operating regime (C28): a coil is blind to a static trapped field, and NMR is the accepted reference, not the coil. The brief magnetization-transient sub-case already uses coils today (P039, P049) without needing a novel hybrid.",
     "C28;P038;P039;P040;P041;P042;P043;P045;P047;P048;P049;P050;P051",
     "4", "do-not-prioritize (as a hybrid-architecture application); monitor (Cambridge Bulk Superconductivity Group, for cryogenic Hall temperature-coefficient literature reuse only -- no shared measurement problem, no outreach ask)",
     "None -- vetoed for structural fit (C28); the P050/P051 data is already absorbed into stage-30 section 2.1 alpha_S characterization without requiring any gate specific to this application."],

    ["Accelerator magnets -- precision field mapping and calibration (CERN/FNAL/HIAF)",
     "Need multi-T, ppm-level field mapping and calibration during controlled magnet test campaigns (P052-P058).",
     "Hall probes + rotating/fixed coils + NMR, already combined as decades-old, production-scale practice (P052, P054, P057, P058), including in-situ calibration of rotating coils against a reference magnet (P057).",
     "1/5 -- the architecture-level 'Hall+coil hybrid' is not novel here at all (C29); the most direct novelty veto in the entire scorecard, not merely a weak fit.",
     "3/5 mature, not novel -- paradoxically the strongest demonstrated identifiability path of any lane (in-situ rotating-coil self-calibration against a reference magnet is routine, P057; NMR absolute reference is routine, P058) -- but this only confirms prior art already solved the problem, it does not open a gap for the user.",
     "1/5 -- radiation is background context only at accelerator test benches, not a qualification driver (10C review); poor fit for the mission's specific radiation-compensation contribution.",
     "2/5 -- CERN/FNAL/HIAF are world-class facilities generally not readily accessible to an outside PhD student without a pre-existing tie.",
     "2/5 -- blocked on architecture novelty (C29); a paper here would need a narrow, unevidenced angle (e.g. in-situ radiation-tolerant embedded calibration for the minority of accelerator magnets sitting in beamline radiation backgrounds) that is currently speculative.",
     "3/5 -- CERN's magnetic-measurements group (rotating-coil/Hall-probe field mapping) is active, technically excellent, and methodologically close to stage 30's embedded-calibration-winding design (section 5.4-5.5 triangle-closure test is directly inspired by this literature) -- worth monitoring for technique-borrowing even though it is not a novel application target.",
     "3/5 -- not pursuing as an application; the in-situ rotating-coil self-calibration technique itself is free to borrow from the literature, already reflected in stage 30.",
     "3/5 moderate if pursued as a beamline-magnet-mapping project; low if only the published technique is borrowed, which is what has already happened.",
     "1.7/5 (mean of hybrid_value, identifiability_path, radiation_fit = [1,3,1])",
     "2.2/5 (mean of experimental_access=2, publication_value=2, collaboration_leverage=3, cost-inverted=2, dilution-inverted=2)",
     "Yes -- direct prior-art novelty veto (DECISION_FRAMEWORK.md: 'direct prior art that removes the proposed novelty'); C29 states architecture-level Hall+coil+NMR fusion is mature, decades-old production practice at CERN/FNAL/HIAF.",
     "C29;C36;P052;P053;P054;P055;P056;P057;P058;P075",
     "3", "do-not-prioritize (as application target); monitor (CERN magnetic-measurements group methodology -- technique already absorbed into stage-30 section 5.4-5.5 via literature, no outreach needed)",
     "None -- vetoed for novelty (C29); no stage-30 gate applies."],
]


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    out_path = os.path.join(out_dir, "04_APPLICATION_SCORECARD.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        for row in ROWS:
            assert len(row) == len(HEADER), f"row length {len(row)} != header length {len(HEADER)}: {row[0]}"
            w.writerow(row)
    print(f"Wrote {out_path} with {len(ROWS)} data rows.")


if __name__ == "__main__":
    main()
