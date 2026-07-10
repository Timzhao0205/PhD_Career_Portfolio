# QUESTIONS — the six things to answer (verbatim intent + the crisp version)

These are the user's questions. Each maps to a subtask in MISSION_BRIEF.md. Answer all six,
nothing more.

## Q1 → ST1 · Component selection
> "Verify if my component selection is optimal (or should I modify better option)."
Scope: the whole signal chain of `hsx_2026_v2` — bias mux (ADG1209), sense mux (ADG1209),
chopper (ADG5236), in-amp (AD8429), rails (RS6-2415D), and the passives that set gain,
loading, and sensing (R_G, 2.2 kΩ returns, 100 Ω sense). For each: **keep or change**, with a
datasheet-cited reason, *under the locked ambient / ≤20 kHz / spun constraints*. If "change,"
name the specific alternative part (package + datasheet link). Note the unplaced ADA4898-2 in
the library and say whether it should be placed and for what.

## Q2 → ST2 · Connection correctness
> "Verify if my connections are correct."
Scope: the netlist/pinout, with special attention to the **updated Amphenol DSUB-9
(D09S33E6GX00LF, J1)** — confirm its pin numbering/gender matches the sensor pinout
(p1=1, p3=2, p2=6, p4=7) and the twisted-pair harness convention, and that nothing regressed
vs v1 in the swap. Also sanity-check EN pulldown, the missing J3 ground, bias-loop
sense-resistor placement, and the output network.

## Q3 → ST3 · 3-axis board architecture
> "If I am considering a board for 3D (3 sets of components), would you recommend a larger
> board, or more layers (6 layers), or three individual boards connected through wires and
> stacked like a tower?"
Deliver a trade study of the three options (single large board / 6-layer board / 3 stacked
single-axis boards) against: channel isolation & crosstalk, ground integrity, hand-assembly
& rework, cost, mechanical fit to the cube-probe geometry, schedule risk, and reuse of the
existing single-axis design. Give a recommendation with the runner-up and the condition that
would flip it.

## Q4 → ST4 · Raspberry Pi fan-out
> "Would the Raspberry Pi connection change (need more signal power)?"
One Pico drives shared a0/a1/a2/EN into **3×** the CMOS mux/chopper inputs now. Determine
whether that needs buffering / series termination / level considerations / extra current or
power, and whether sync/ground distribution changes. Quantify the load (input capacitance ×
3, edge rate, cable length) and give a keep-or-add-buffer call.

## Q5 → ST5 · Vacuum feedthrough / flange
> "For 3 sensors (3×4 = 12 wires) I need to adjust the flange. Currently Accu-Glass 9D-275.
> Which flange should I move to that meets the same requirement?"
From the Accu-Glass sub-D CF feedthrough family (menu in REFERENCE_DATA), select the
option(s) that carry **≥12 conductors** while meeting or exceeding the 9D-275 ratings
(500 VDC, 5 A/pin, ≤10⁻¹⁰ Torr, −200…250 °C, 2.75″ CF baseline). Compare a single
higher-count feedthrough vs per-sensor grouping; note CF size change and mating-connector
implications. Cite every part.

## Q6 → ST6 · Multi-sensor wiring & short-circuit safety (the top worry)
> "My biggest concern when making connections for multiple sensors is wiring and short
> circuit."
Produce a concrete harness + pinout + isolation plan for 3 sensors through one feedthrough:
per-plate twisted pairs, pin assignment that keeps bias and sense pairs separated, shielding/
drain strategy, keying/labeling to prevent mis-mating, and the specific short-circuit failure
modes (pin-to-pin at the feedthrough, chafing in the hot zone, shared-return sneak paths) with
mitigations and a pre-power continuity/insulation test procedure.

## Q7 → ST7 · Hall-die packaging / wire-bond strategy
> "For the packaging of the Hall-effect sensor I purchased LCC02046 (Spectrum ceramic chip
> carrier). I assume I need to wire-bond to the four corners of the chip carrier. My
> understanding is that I can guide the signal to one side through external connections using
> the bondpad. Comment my strategy."
Scope: comment on the die→LCC02046 wire-bond + one-side signal-routing plan. Data is in
`01_MISSION/REFERENCE/PACKAGING_LCC02046.md` (20-pad .350″ LCC; octagonal Hall die with 4
corner contacts p1–p4). Deliver: which LCC pads carry p1–p4, whether one-side routing via the
castellations is sound, bond-wire length/loop/crossing assessment, the die-contact → LCC-pad →
DSUB-9-pin mapping (must reconcile with p1=1/p3=2/p2=6/p4=7), ground/shield strategy, packaging
gotchas (353ND attach, 150 °C vacuum bake, hermeticity, vertical-face bonding for the cube), and
a keep/adjust verdict with an alternative pad map if needed. Comment on the strategy — do not
just restate it.

## Q8 → ST8 · 3D probe-head packaging design (with visuals)
> "For the 3D packaging design side, provide a few options you consider good. The entire added
> package (stands and everything) must fit inside a virtual cylinder — height 2.75 cm, diameter
> 1.25 in — on top of the flange. My idea: a cube with slots on each face to insert and secure
> my chip carrier with sensors on top. No epoxy/glue for the 3D package (I'll epoxy each
> individual sensor + carrier); I want the carriers reusable. Add suggestions and criticize my
> idea. Use generation tools to create visual explanations."
Scope + data + the validated CAD pipeline: `01_MISSION/REFERENCE/PACKAGING_3D_ENVELOPE.md`,
`envelope_reference.png`, `REFERENCE/cad/*.stp` (his idea + old 1D mount), `tools/cad/`.
Deliver 3–4 buildable, glue-free concepts (his slotted cube refined + alternatives), a point-by-
point critique of his idea, per-concept CAD renders (iso/top/front/section) + STEP/STL, a
weighted decision matrix, and a recommendation. Hard limits: Ø31.75×27.5 mm envelope, mechanical
reversible retention, non-magnetic + UHV material, 3 carriers on orthogonal faces.
**Update (user):** he is willing to replace his idea — so ST8 should actively recommend the
design it considers OPTIMAL, not just present neutral options. **Every concept must be verified
compatible with the LCC02046 specifically** (leadless SMT carrier: 20 castellated pads — the mount
must connect them without solder/glue, e.g. socket/spring/pogo, and must not chip the brittle
8.89 mm body). See `PACKAGING_3D_ENVELOPE.md §F` for the compatibility gate + seed directions.

## Global asks that ride on every answer
- Keep the single-axis board bootable for the Aug 2026 HSX campaign — don't recommend changes
  that block that.
- Distinguish "needed now (3-axis)" from "nice-to-have (rev-B)".
- Flag anything that spends money or is hard to undo into `90_SYNTHESIS/DECISION_GATES.md`.
