# CONTEXT_PRIMER — what this project is, so your review lands in the right frame

**Owner:** Yiming "Tim" Zhao, Stanford EE PhD (Senesky group). **Collaboration:** UW-Madison
HSX stellarator (Goodman, Gallenberger, Geiger).

**One-line:** a calibrated, offset-free AlGaN/GaN Hall-effect magnetic-field readout for
in-vessel fusion diagnostics, being scaled from one axis to a 2–3 axis vector probe.

## Trajectory (frame every answer against this)

1. **2023 (published, IEEE Sensors Letters):** packaged AlGaN/GaN Hall sensor survived 68
   in-vessel HSX shots; voltage-biased, uncalibrated. Future work it named: absolute
   calibration, offset stability, lower-noise readout.
2. **2026 — the board under review (`hsx_2026_v2`, single axis):** 100 µA current bias +
   4-phase spinning-current with polarity chopping (kills plate + amp offsets), AD8429
   readout; HSX install target ~Aug 2026. This is bench-validated now (see HARDWARE_DATA §5).
3. **2026–27 — the scale-up this review is FOR:** 2–3 axis vector probe (gen-2 dies with
   larger pads, LCCs on orthogonal faces of a ceramic cube), 2nd HSX campaign, paper to
   **Review of Scientific Instruments** (~Mar 2027).

## Decisions already fixed upstream (don't relitigate; build on them)

- Readout scales by **replicating the single-axis board ×3** from the existing design (not a
  new multichannel board rev). Hand assembly.
- **One Raspberry Pi Pico 2** fans out shared a0/a1/a2/EN to all three boards → synchronized
  spinning; per-board **floating 100 µA** sources; one sync line timestamps all three demods.
- DAQ: 4-channel scope = v_x, v_y, v_z + sync.
- **Scope rule (hard):** plasma + magnetic-field measurement only. No neutron/gamma radiation
  work here. Don't introduce radiation-hardness requirements.

## What "optimal" means for THIS review (the locked lens)

Because the readout sits **outside the vessel at ~ambient** and only needs **10–20 kHz**
demodulated bandwidth, the earlier high-temperature / 1-MHz concerns are **out of scope**.
"Optimal" here means: right parts and connections for a **calibrated, low-noise, offset-free,
~ambient, ≤20 kHz, 3-channel synchronized** measurement that is **easy to wire without shorts**
across three sensors and one vacuum feedthrough — at low bench cost and hand-assemblable.

## The open item that gates electrical claims

There is an **unresolved bench anomaly** (measured output ~100× below prediction). Its
surviving cause includes "in-operation gain isn't ~100×." So: **do not conclude anything
about component adequacy from measured amplitudes** until the ΔV gain check closes it.
Base ST1 reasoning on datasheets and first principles; explicitly note where the anomaly,
if real, would change a conclusion.
