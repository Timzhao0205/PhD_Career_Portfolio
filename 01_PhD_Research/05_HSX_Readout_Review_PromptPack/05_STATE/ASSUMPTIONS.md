# ASSUMPTIONS (write every gap-filling assumption here, with a date; proceed, don't ask)

Seed assumptions carried into the review (challenge and update as you verify):

- The HSX vacuum port that currently takes the 2.75" CF (9D-275) can accommodate a larger CF
  (e.g., 4.5") OR an adapter is available — CONFIRM with the mechanical drawing / UW team; this
  gates ST5. [unconfirmed]
- Per-axis board connector stays a DSUB-9 (as on hsx_2026_v2 J1); the feedthrough choice must
  reconcile 3× DSUB-9 board side with whatever conductor grouping the flange provides. [design intent]
- The 3-axis readout keeps 100 uA per-plate current bias and 40 kHz-class spin (→ ~1-2 kHz per
  demod, well inside the 10-20 kHz budget). [from RSI plan]
- Sensor/module max temperature and the in-vessel harness length are not yet fixed here; if a
  spec is needed, log the assumed value and flag it. [open]

Run assumptions (2026-07-10):

- 2026-07-10 — `LCC02046_datasheet.pdf` and the die image are NOT in `01_MISSION/REFERENCE/`.
  ST7 proceeds on `PACKAGING_LCC02046.md` (user's mechanical-drawing readout) + the Spectrum
  web page; geometry numbers not confirmable online are marked UNVERIFIED against the paper
  drawing. [logged per kickoff instruction]
- 2026-07-10 — Housekeeping (state/log file edits) is done inline by the Fable 5 orchestrator
  instead of Haiku subagents: each edit is a one-line write, and spawning an agent costs more
  tokens than the edit itself. Deviation from MODEL_EFFORT_POLICY housekeeping row, logged in
  MODEL_EFFORT_LOG.md. [cost-motivated fallback]
- 2026-07-10 — ST7 assumptions (full list in 70_PACKAGING/PACKAGING_REVIEW.md §8; close before
  first bond): die ~2–3 mm sq with p1=N/p2=S/p3=E/p4=W (GDS image not in pack — orientation must
  be pinned to actual GDS labels); die pads Au-topped; JEDEC-style CCW pad numbering with pin 1 =
  mid-pad of index side (drawing-only, Spectrum PDF image-only/unreadable); shelf step ~0.4–0.5 mm;
  25 µm Al wedge wire. ST7 instructions written physically (chamfer as datum) to survive a
  numbering-direction surprise. [ST7]
- 2026-07-10 — ST4 assumptions: ADG1209/ADG5236 logic C_IN ≈ 5 pF/pin (conservative EJ; ADI PDFs
  unreachable); RP2350 GPIO electricals taken from RP2040 precedent; R5–R8 pulldowns treated as
  ~10 kΩ class (value not in HARDWARE_DATA); a2→ADG5236 IN1+IN2 direct (no inverter) inferred from
  the 8-phase encoding — ST2 to cross-check in netlist. [ST4]
- 2026-07-10 — ST5 assumption A1: the HSX probe port is 2.75″ CF (gates the 9C2-275 pick); plus
  Sub-C tower protrusion dims, stock/lead times, per-page VDC UNVERIFIED — see
  50_FLANGE/FLANGE_SELECTION.md. [ST5]
- 2026-07-10 — ST1 assumptions: R5–R8 = 10–100 kΩ class (values absent from HARDWARE_DATA and
  netlist parts list); ~450 Ω symmetric per-input source for i_n calc; 50–100 pF/m logic cable;
  295 K Johnson noise; ADG1209 Q_inj at family-standard test condition. UNVERIFIED: RS6-2415D
  switching freq/ripple (PDF text-locked) + isolation 1.6 kV (Digi-Key) vs 2 kV (TME) discrepancy;
  AD8429 I_B typ; ADG5236 numeric JESD78 rating; RP2350 drive strengths from secondary RPi docs.
  ADI specs verified from full-text mirrors of Rev E/B/A PDFs (analog.com direct timed out). [ST1]
- 2026-07-10 — ST6 assumptions A5–A12 (full list in 60_WIRING_SHORTS/WIRING_PLAN.md §13): bias
  compliance ≤18 V; J1 spares N/C (CONFIRMED by red-team netlist check); LCC pads per ST7 with
  PB-CA8272-B numbering caveat; ≤0.5 m in-vessel run. UNVERIFIED: Sub-C insert pin adjacency;
  die voltage/ESD withstand; cable wire colors. [ST6]
- 2026-07-10 — ST8 assumptions A1–A8 (full list in 80_3D_PACKAGING/PACKAGING_3D_DESIGN.md):
  A1 envelope centered on port axis; A2 Sub-C tower protrusion ≤~6.5 mm (UNVERIFIED — standoff
  adjustable, flip if >~10 mm); A3 heritage ±12.5 mm mount pattern; A4–A5 leaf-spring contact
  force 0.3–0.6 N + stiffness (EJ pending photo-etch prototype); A6 head ≤~200 °C (else fuzz
  buttons replace BeCu leafs); A7 LCC bottom-pad flat area confirm on physical part; A8 generic
  socket dims in concept C. UNVERIFIED: tower protrusion, BeCu relaxation limit, HSX in-vessel
  temp at probe. [ST8]
