# MISSION_BRIEF — the six subtasks + how to run them

You are the orchestrator. Execute ST1–ST8 then the synthesis. Follow `MODEL_EFFORT_POLICY.md`
for which model/effort each subtask uses, and LOG every model/effort switch (see CLAUDE.md §Logging). Each subtask: read its inputs,
do the work with the named subagent, write the specified output file, update `05_STATE`.
Independent subtasks may run in parallel; the synthesis runs last.

Global inputs for every subtask: `CONTEXT_PRIMER.md`, `HARDWARE_DATA.md` (esp. §4 locked
constraints + §5 open anomaly), `SOURCE_STANDARDS.md`. Global output rule: decision tables,
cited numbers, a "failure mode if wrong" line per recommendation, and a `red-team-critic` pass
before anything enters `90_SYNTHESIS`.

---

### ST1 — Component selection (Q1) · agent: `component-selection-reviewer`
Output: `10_COMPONENTS/COMPONENT_REVIEW.md` + `10_COMPONENTS/bom_verdict.csv`.
Method: pull each datasheet (REFERENCE_DATA §C). Build a table: Ref · Part · role · key spec
that matters here · **keep/change** · alternative (if change) + datasheet link · reason ·
failure-mode-if-wrong. Judge under the *ambient, ≤20 kHz, spun, low-noise, hand-assembled*
lens — not high-T, not wideband. Explicitly address: is ADG1209 the right mux (charge
injection vs R_on trade), is AD8429 right vs AD8421 at ambient with this source impedance,
is the ADA4898-2 needed (place or leave), are R_G / 2.2 kΩ / 100 Ω values right for the
target operating point. End with a "needed-now vs rev-B" split. Do NOT lean on measured
amplitudes (see anomaly).

### ST2 — Connection correctness (Q2) · agent: `netlist-connection-checker`
Output: `20_CONNECTIONS/CONNECTION_CHECK.md`.
Method: if the live `hsx_2026_v2.net` is available, parse it; else use HARDWARE_DATA §1/§3.
Verify J1 = Amphenol D09S33E6GX00LF pin numbering/gender against the sensor pinout and harness
convention; trace bias mux → chopper → plate → sense mux → in-amp → J4; confirm EN pulldown,
J3-has-no-ground, R9/R10 placement, output network. Produce a net-by-net pass/flag table and a
short "regressions introduced by the v1→v2 connector swap?" verdict.

### ST3 — 3-axis board architecture (Q3) · agent: `mechanical-vacuum-analyst` (+ high effort)
Output: `30_3AXIS_ARCH/ARCHITECTURE_TRADE.md`.
Method: score {single large board · 6-layer board · 3 stacked single-axis boards (tower)}
against the criteria in QUESTIONS Q3. Include a weighted matrix, a recommendation, the
runner-up, and the flip condition. Tie back to the fixed upstream decision (replicate ×3) and
the cube-probe geometry. This is a DECISION_GATE item.

### ST4 — Pico fan-out (Q4) · agent: `component-selection-reviewer`
Output: `40_PI_FANOUT/PI_FANOUT.md`.
Method: quantify the shared-line load driving 3 boards (3 × mux/chopper C_in, edge rate,
cable length, DC current ≈ 0 for CMOS). Decide: does it need a buffer (e.g., 74LVC-class),
series termination, or a re-clock; does EN need more drive; does sync/ground distribution
change; any power delta. Keep-or-add verdict with the threshold (cable length / capacitance)
that would force a buffer.

### ST5 — Flange (Q5) · agent: `mechanical-vacuum-analyst`
Output: `50_FLANGE/FLANGE_SELECTION.md`.
Method: from REFERENCE_DATA §A, select the feedthrough(s) that carry ≥12 conductors at ≥
9D-275 ratings; compare single-vs-grouped; verify CF size vs the HSX port and matching
cables/connectors; cite every part. This is a DECISION_GATE item (it spends money + changes
mechanical fit).

### ST6 — Wiring & short-circuit plan (Q6) · agent: `mechanical-vacuum-analyst` + `red-team-critic`
Output: `60_WIRING_SHORTS/WIRING_PLAN.md`.
Method: full 3-sensor harness + pin-assignment + isolation plan (per QUESTIONS Q6), a labeled
pinout table (board DSUB-9 ×3 ↔ feedthrough pins ↔ sensor plates), short-circuit FMEA
(pin-to-pin, chafing, shared-return sneak paths), and a **pre-power continuity + insulation-
resistance test procedure**. Red-team it hard — this is the user's #1 worry.

### ST7 — Hall-die packaging / wire-bond strategy (Q7) · agent: `packaging-wirebond-specialist`
Output: `70_PACKAGING/PACKAGING_REVIEW.md`.
Method: read `01_MISSION/REFERENCE/PACKAGING_LCC02046.md`. Datasheet-verify the LCC02046 pad
geometry, then **comment on the user's strategy** (bond the die's 4 corner contacts; route all
signals to one side via castellations). Produce the die-contact → LCC-pad → DSUB-9-pin mapping
table (reconcile with p1=1/p3=2/p2=6/p4=7), assess bond-wire length/loop/crossing and the
one-side idea, cover ground/shield and packaging gotchas (353ND, 150 °C vacuum bake, hermeticity,
vertical-face bonding for the cube), and give a keep/adjust verdict + alternative pad map. This
touches the in-vessel hardware, so `red-team-critic` reviews it (a bad bond map or lost
hermeticity is expensive).

### ST8 — 3D probe-head packaging design + visuals (Q8) · agent: `packaging-3d-designer` (Fable 5, high effort)
Output: `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` + per-concept CAD/renders under
`80_3D_PACKAGING/<concept>/`.
Method: read `PACKAGING_3D_ENVELOPE.md` (incl. **§F LCC02046 compatibility gate + seed directions
S1–S4**); load his STEP (`REFERENCE/cad/*.stp`) in a real CAD kernel to measure + critique;
produce 3–4 glue-free concepts + a point-by-point critique of his slotted-cube idea; **be
opinionated and recommend the OPTIMAL design (the user will adjust his)**; generate iso/top/front/
section renders + STEP/STL via `tools/cad/`. Enforce the hard limits (Ø31.75×27.5 mm, reversible
mechanical retention, non-magnetic/UHV, 3 orthogonal faces) AND the LCC02046 gate — every concept
must make the electrical connection to the 20 castellated pads without solder/glue (socket/spring/
pogo) and not chip the brittle body. Weighted matrix + recommendation + runner-up + flip condition.
This is the most generative subtask and an in-vessel DECISION_GATE — `red-team-critic` reviews it.

---

### Synthesis (last)
Outputs:
- `90_SYNTHESIS/RECOMMENDATIONS.md` — one table: question · answer · keep/change · confidence ·
  cost/effort · source. Plus a "3-axis build order of operations."
- `90_SYNTHESIS/DECISION_GATES.md` — the 2–3 choices needing the user's sign-off (board
  architecture, flange P/N, any part swap that costs money or blocks the Aug build).
- `90_SYNTHESIS/RED_TEAM.md` — the critic's surviving objections and what evidence would settle
  each.
Set `MASTER_STATE.json.mission = "COMPLETE"` only when DELIVERABLES_SPEC's checklist passes.
