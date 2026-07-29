# One-shot post-freeze founder-fit annotator (rule 3). Fills founder_fit_note on all 65
# frozen longlist ideas and appends the notes section to LONGLIST.md. No other field is
# modified; a built-in diff check enforces that.
import copy
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOTES = {
    "P3R2-A-02": "Founder circuits, controls, and embedded-systems skills transfer to the breaker's sensing, relaying, and trigger electronics, but medium-voltage kA-class power hardware, the mechanical ultra-fast disconnect, and certification programs lie outside the profile.",
    "P3R2-A-03": "Automated test sequencing, data acquisition, and controls experience transfer to the event-playback and evidence-grade reporting layer, while MW-class back-to-back converter design and trailerized power integration are outside the profile.",
    "P3R2-A-05": "Low direct fit: certified outgassing metrology draws on instrumentation and data-acquisition skills, but the core sputter-coating, vacuum-firing, and surface-chemistry process line is outside the founder's electrical-engineering profile.",
    "P3R2-A-10": "Strong transfer: the RF-immune ion-energy sensor, signal-derived estimation, and closed-loop waveform bias controller map directly onto founder sensors/instrumentation, circuits, controls, and electromagnetics skills.",
    "P3R2-A-11": "Strong transfer: pressure-based sensing, model-predictive valve control, and inline transient metrology sit squarely in founder instrumentation, controls, and data-acquisition skills, with only the fluidic/valve mechanics outside the profile.",
    "P3R2-A-13": "Power-stage circuit design, standardized telemetry, and control interfaces draw on founder circuits and embedded-systems skills, but radiation-effects qualification and space-flight hardware processes are outside the profile.",
    "P3R2-A-14": "Strong transfer on the mixed-signal instrumentation front-ends, data-acquisition chain, and reference logging module, which are core founder skills; the high-temperature packaging and die-attach materials work that gates the product is outside the profile.",
    "P3R2-A-16": "Low direct fit: this is a materials/metallurgy and process-licensing play, with founder skills contributing only peripherally via instrumentation for power-cycling and accelerated-reliability test rigs.",
    "P3R2-A-21": "Controls, sequencing software, and embedded fleet-API integration transfer from the founder profile, but multi-megawatt conversion stacks, liquid-cooled dispensing hardware, and heavy-industrial site deployment are outside it.",
    "P3R2-A-22": "The nanosecond-pulsed power supply and destruction-verification instrumentation align with founder circuits, electromagnetics, and instrumentation skills, while plasma-process chemistry, fluoride handling, and regulatory validation are outside the profile.",
    "P3R2-B-01": "Vacuum-setpoint control, vacuum-decay leak-detection instrumentation, and the loop control unit fit founder controls and sensing skills, but the governing two-phase thermal-fluid and evaporator/manifold design work is outside the profile.",
    "P3R2-B-06": "Strong transfer: the HV programmable clamp supply, leakage-current-based force estimation, declamp sequencing, and multi-zone mK-class thermal control are direct applications of founder circuits, controls, instrumentation, and embedded-systems skills.",
    "P3R2-B-14": "Modular converter control, protocol/interlock firmware, and qualification test design draw on founder circuits, embedded, and controls skills, but megawatt-class power hardware engineering and dual-market certification logistics are outside the profile.",
    "P3R2-B-22": "Strong transfer: synchronous-demodulation ripple sensing, hotspot thermal estimation, and physics-of-failure remaining-useful-life modeling map directly onto founder instrumentation, circuits/signal-processing, embedded, and numerical-analysis skills.",
    "P3R2-C-01": "Strong transfer: fast fault-clearing circuits, arc-signature detection, precharge/IMD/hot-swap sequencing, and fleet telemetry sit within founder circuits, embedded-systems, controls, and data-acquisition skills at a rack-scale power class amenable to founder prototyping.",
    "P3R2-C-02": "Strong transfer: the partial-power bidirectional converter, active bus-damping control, and capacitor-prognostics telemetry are circuits, controls, and embedded work at a prototypable rack scale within the founder profile.",
    "P3R2-C-03": "Converter cell control and telemetry transfer from founder circuits/controls skills, but medium-voltage insulation coordination, high-frequency transformer design, and MW-class certification work are outside the profile.",
    "P3R2-C-04": "Fluid-property auto-identification, vacuum-decay detection, and loop control electronics fit founder sensing/controls skills, while the core two-phase cold-plate, micro-pump, and fluid-qualification work is thermal-fluids and chemistry outside the profile.",
    "P3R2-C-05": "Strong transfer: programmable thermal test vehicles, calorimetry benches with tight energy-balance closure, and traceable acceptance protocols are instrumentation, data-acquisition, controls, and numerical-analysis products in the founder's core skill set.",
    "P3R2-C-07": "Ripple/harmonic control design and measurement-and-verification telemetry draw on founder controls, instrumentation, and data-acquisition skills, but 5-50 MW rectifier hardware, plant integration, and electrochemical process knowledge are outside the profile.",
    "P3R2-C-08": "Low direct fit: diffusion-bonded heat-exchanger cores are a materials and thermo-mechanical product, with founder skills applying only peripherally to test-loop instrumentation and creep/fatigue data acquisition.",
    "P3R2-C-09": "Pulse-module control, digital droop correction, and standardized digital interfaces fit founder circuits, controls, and embedded skills, while 10-100 kV kA-class high-voltage packaging and insulation engineering sit at the edge of the profile.",
    "P3R2-C-12": "Low direct fit: gas-bearing turbomachinery and cryogenic engineering dominate the product, with founder skills transferring only to the turboalternator drive electronics, sensing, and health telemetry.",
    "P3R2-C-13": "Strong transfer: multi-channel nanosecond-edge current-drive circuits, safety interlocks, and diode-health telemetry are direct founder-profile circuits, embedded-systems, and instrumentation work.",
    "P3R2-C-19": "Low direct fit: gas-foil bearings and face seals are mechanical/tribological components, with founder skills applying only peripherally to life-test instrumentation and data acquisition.",
    "P3R2-C-21": "Protection-coordination logic and inter-port fault-isolation control align with founder controls and embedded skills, but MW-class multiport converter hardware and EPC-facing deployment are outside the profile.",
    "P3R2-C-22": "Strong transfer: programmable ripple synthesis, renewable-profile playback, impedance diagnostics, and degradation-data pipelines are test-and-measurement engineering within founder instrumentation, controls, and data-acquisition skills, with stack electrochemistry interpretation as the main outside dependency.",
    "P3R2-D-01": "Strong transfer: distributed fiber-optic sensing readout, multi-channel fusion in a deterministic FPGA trigger, and qualified energy-extraction electronics map directly onto founder instrumentation, embedded-systems, circuits, and data-acquisition skills.",
    "P3R2-D-02": "Strong transfer: Hall-array magnetic sensing, lock-in thermal imaging, and line-speed data acquisition with calibrated reporting are core founder sensors/instrumentation, electromagnetics, and numerical-analysis work.",
    "P3R2-D-07": "Electron-optics simulation and drive-waveform electronics draw on founder electromagnetics, numerical-analysis, and circuits skills, but vacuum-tube fabrication, collector thermal design, and rebuild-shop integration are outside the profile.",
    "P3R2-D-08": "Solid-state RF drive, dose-mapping automation, and machine controls fit founder circuits, controls, and instrumentation skills, while accelerator physics, radiation shielding, and sterilization regulatory validation are outside the profile.",
    "P3R2-D-09": "Strong transfer: cavity-resonator charge measurement, Faraday/calorimetric cross-calibration, and metrology-grade uncertainty budgets are precision instrumentation and electromagnetics work at the center of the founder profile.",
    "P3R2-D-10": "Strong transfer: per-channel electro-optic modulation, deterministic sub-microsecond FPGA control loops, and interferometric feedback are founder controls, embedded-systems, circuits, and signal-processing territory.",
    "P3R2-D-11": "Low direct fit: kilowatt-class thulium/holmium laser-chain development is laser physics and photonic-materials engineering, with founder skills applying mainly to drive electronics, timing, and diagnostics instrumentation.",
    "P3R2-D-12": "The high-voltage EHD pump drive, per-channel flow modulation, and hotspot-map feedback control fit founder electromagnetics, circuits, and controls skills, but microchannel two-phase thermal design and fluid qualification are outside the profile.",
    "P3R2-D-13": "Low direct fit: the product is phase-change materials and two-phase thermo-mechanical engineering, with founder skills contributing only the thermal state-of-charge telemetry and test instrumentation.",
    "P3R2-D-16": "kV-class PMAD, high-speed alternator drive, and telemetry draw on founder circuits, controls, and electromagnetics skills, but He-Xe turbomachinery, foil bearings, and space-flight qualification dominate the product and are outside the profile.",
    "P3R2-D-18": "Strong transfer: varactor-tuned metasurface unit cells, RF-chain design, aperture calibration, and beam-control software are direct applications of founder electromagnetics, RF circuits, numerical-analysis, and embedded skills.",
    "P3R2-D-19": "Active-magnetic-bearing control, inverter coupling, and millisecond-response electronics fit founder controls, electromagnetics, and circuits skills, while composite-rotor mechanics and containerized multi-megawatt string integration are outside the profile.",
    "P3R2-D-20": "Low direct fit: 1,400-2,400 C refractory pumps, valves, and seals are extreme-materials mechanical engineering, with founder skills applying only peripherally to level/flow instrumentation in a harsh environment.",
    "P3R2-E-02": "Strong transfer: capacitive/ultrasonic vapor-quality sensing, dryout-margin observers, and model-predictive pump/expansion control are founder sensors, controls, embedded, and numerical-analysis work, with two-phase fluid modeling as the main outside dependency.",
    "P3R2-E-04": "Strong transfer on the cryo-CMOS multiplexing, LNA readout chain, and channels-per-watt instrumentation engineering, which sit in founder circuits/RF and instrumentation skills; cryogenic materials and flex-laminate fabrication are outside the profile.",
    "P3R2-E-11": "Micro-TEC regulation electronics and sub-degree control loops fit founder controls and circuits skills, but the lid-integrated two-phase spreader, TIM stack, and package-materials qualification are outside the profile.",
    "P3R2-E-14": "Strong transfer: traveling-wave fault-discrimination algorithms, sub-millisecond relay firmware, and hardware-in-the-loop qualification suites are founder signal-processing, embedded-systems, controls, and numerical-analysis territory.",
    "P3R2-F-01": "Strong transfer: switched-capacitor RF matching arrays, sub-10-microsecond re-tune control, pulse-synchronous tuning tables, and health telemetry map directly onto founder RF circuits, controls, and embedded skills.",
    "P3R2-F-02": "Precision converter control, magnet-aware dump sequencing, and acceptance-test protocols draw on founder circuits, controls, and instrumentation skills, but kA-class power hardware, current leads, and busbar/thermal engineering are outside the profile.",
    "P3R2-F-03": "Active front-end converter control, bearing-drive electronics, and grid-code compliance testing fit founder circuits and controls skills, while high-speed permanent-magnet machine design and turbomachinery integration are outside the profile.",
    "P3R2-F-04": "Strong transfer: five-axis magnetic-bearing position sensing, adaptive control, drive electronics, and fleet health telemetry form a controls/electromagnetics/embedded product squarely within the founder profile, with rotordynamics modeling supported by numerical-analysis skills.",
    "P3R2-F-05": "Traction-inverter control, vehicle-control-unit firmware, and charge-interface electronics draw on founder circuits, embedded, and controls skills, but vehicle-level mechanical integration and multi-market certification programs are outside the profile.",
    "P3R2-F-06": "Strong transfer: fiber-optic current transducers, zero-flux hybrid sensing from DC to 1 MHz, and published accuracy test protocols are precision electromagnetics and instrumentation work at the core of the founder profile.",
    "P3R2-F-07": "Low direct fit: liquid-cooled megawatt cable/connector and swap-coupler hardware is thermo-mechanical contact engineering, with founder skills applying mainly to contact-resistance health sensing and telemetry.",
    "P3R2-F-09": "Low direct fit: brazed-ceramic vacuum windows and couplers are a materials/joining product, with founder skills applying peripherally to the integrated arc/temperature diagnostics and acceptance-test instrumentation.",
    "P3R2-F-10": "Strong transfer: interferometric/EMAT detection, laser-ultrasound signal chains, and real-time phased-array reconstruction combine founder sensors/instrumentation, electromagnetics, signal-processing, and numerical-analysis skills.",
    "P3R2-F-11": "Pulsed capacitor-bank electronics, per-shot energy control, and field-shaper coil electromagnetics fit founder circuits and electromagnetics skills, but welding metallurgy, process-window development, and production-line integration are outside the profile.",
    "P3R2-F-12": "String protection, insulation monitoring, and pack-interface electronics fit founder circuits and embedded skills, but classification-society type approval, shipyard integration, and the required CN joint-venture structure are outside the profile.",
    "P3R2-F-15": "Per-stack isolation control, current-share balancing, stray-current mitigation, and telemetry draw on founder circuits, controls, and electromagnetics skills, with plant-scale DC switchgear hardware and EPC delivery outside the profile.",
    "P3R2-F-16": "Inline surface-energy/residue metrology and closed-loop recipe control fit founder instrumentation and controls skills, while plasma-source hardware, process chemistry, and CN direct-sales operations are outside the profile.",
    "P3R2-F-17": "Strong transfer: return-path and capacitive body-proximity sensing with a sub-millisecond certified beam-disable chain is a compact sensing and embedded-safety-electronics product within founder instrumentation and circuits skills.",
    "P3R2-F-19": "The multi-parameter sensing skid, telemetry, and automated dosing control fit founder instrumentation, embedded, and controls skills, but coolant chemistry, bio-fouling science, and consumables formulation are outside the profile.",
    "P3R2-F-20": "Active ripple cancellation, arc-quench control, and HV telemetry draw on founder circuits and controls skills, but 50-300 kV insulation design and high-voltage packaging craft sit largely outside the profile.",
    "P3R2-F-22": "Low direct fit: vacuum variable capacitors are a precision brazing/bellows manufacturing product, with founder skills applying mainly to RF characterization and acceptance-test instrumentation.",
    "P3R2-F-23": "Strong transfer: the embedded envelope-enforcement controller, ramp/ripple stress shaping, and tamper-evident logging are founder embedded-systems, controls, and data-acquisition work, with stack electrochemistry degradation models as the main outside dependency.",
    "P3R2-G-01": "Model-based bakeout endpoint control, outgassing/RGA acceptance metrology, and certification data systems fit founder controls, instrumentation, and data-acquisition skills, while vacuum-furnace hardware and surface-chemistry process expertise are outside the profile.",
    "P3R2-G-02": "Low direct fit: titanium-foil exit windows and cooled conversion targets are thermo-mechanical/materials consumables, with founder skills applying mainly to the foil-health monitoring and interlock instrumentation.",
    "P3R2-G-03": "Strong transfer: swept-impedance stability analysis, insulation/ground-fault characterization, high-fidelity transient capture, and automated signed test sequences form a portable test-and-measurement product at the center of founder instrumentation, circuits, and data-acquisition skills.",
}


def main():
    path = os.path.join(ROOT, "30_SCREENING", "LONGLIST.json")
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    before = copy.deepcopy(d)

    ids = [i["idea_id"] for i in d["ideas"]]
    assert len(ids) == 65 and len(set(ids)) == 65, "idea count mismatch"
    assert set(ids) == set(NOTES), ("id mismatch", set(ids) ^ set(NOTES))

    for i in d["ideas"]:
        i["founder_fit_note"] = NOTES[i["idea_id"]]

    # Verify nothing else changed.
    for a, b in zip(before["ideas"], d["ideas"]):
        for k in a:
            if k != "founder_fit_note":
                assert a[k] == b[k], (a["idea_id"], k)
        assert list(a.keys()) == list(b.keys())
    assert before["frozen_at"] == d["frozen_at"] and before["gates"] == d["gates"]

    with open(path, "w", encoding="utf-8") as f:  # text mode -> CRLF on Windows
        json.dump(d, f, indent=1, ensure_ascii=False)
        f.write("\n")

    mdpath = os.path.join(ROOT, "30_SCREENING", "LONGLIST.md")
    lines = [
        "",
        "## Founder-fit notes (post-freeze)",
        "",
        "Shallow implementation prior only (rule 3); scoring impact capped at 2/100, applied in P4. "
        "Notes describe execution transferability only and do not re-rank or re-frame the frozen list.",
        "",
    ]
    for iid in ids:
        lines.append(f"- {iid}: {NOTES[iid]}")
    lines.append("")
    with open(mdpath, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))

    hi = sum(1 for n in NOTES.values() if n.startswith("Strong transfer"))
    lo = sum(1 for n in NOTES.values() if n.startswith("Low direct fit"))
    print("notes written:", len(NOTES), "| high:", hi, "| low:", lo, "| medium:", 65 - hi - lo)


if __name__ == "__main__":
    main()
