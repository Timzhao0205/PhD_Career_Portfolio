# 3D PACKAGING DATA — envelope, constraints, user's idea (for ST8). Data + criteria only; ST8 designs.

The user wants a few good mechanical concepts for the 3-axis probe head that holds three
packaged sensors, with visuals. This file is the design brief and the hard constraints. ST8
produces the options, the criticism of the user's idea, and the CAD/visuals — not this file.

## A. Hard constraints (non-negotiable)

- **Envelope:** the ENTIRE added package (cube/frame + stands + everything) must fit inside a
  virtual **cylinder Ø 1.25 in (31.75 mm) × height 2.75 cm (27.5 mm)**, sitting **on top of the
  flange**. Nothing may protrude past this cylinder. (Derived: a cube standing axis-aligned in
  the cylinder can be at most **~22.4 mm edge** before its cross-section corners hit the wall;
  height budget 27.5 mm. See `envelope_reference.png`.)
- **No epoxy / glue in the 3D package.** Retention of each chip carrier into the structure must
  be **purely mechanical and reversible** (slots, clips, springs, set screws, clamps) so the
  carriers + sensors are **removable and reusable**. Epoxy is used ONLY inside each individual
  sensor↔carrier subassembly (EPO-TEK 353ND), which is out of scope for the 3D structure.
- **Three sensors** = three LCC02046 carriers on (ideally) mutually **orthogonal faces** to give
  a 3-axis vector (per rsi plan §2.2). A 2-axis fallback is acceptable if 3 won't fit/retain.
- **Material — DECIDED: the 3D package is ZIRCONIA ceramic** (yttria-stabilized zirconia, ZrO₂).
  ST8 designs the structure **in zirconia** — it does NOT pick the base material. Zirconia is
  non-magnetic and UHV-compatible (both required — this is a Hall probe inside the vessel; no
  ferromagnetic/high-conductivity material near the plates), and it is the **toughest technical
  ceramic** (fracture toughness ~5–10 MPa·m^0.5, far above alumina/Macor), so thin slot/lip
  features are more viable than in a brittle ceramic. Design consequence ST8 must handle:
  zirconia is **hard to machine after sintering** (diamond grinding) — favor green-machine-then-
  sinter or simple, grindable geometry, and account for **sintering shrinkage (~20–25%)** in
  tolerances. Any fasteners/spring contacts remain the only material choice, and must also be
  **non-magnetic + UHV** (BeCu springs, PEEK/Ti/brass hardware) — ST8 selects those with a cite.

## B. Component sizes (verify against datasheets; see PACKAGING_LCC02046.md)

- LCC02046 carrier: **0.350 in = 8.89 mm square**, ~**1.65 mm (0.065 in) thick**, 20 castellated
  edge pads. The sensor die sits in the carrier cavity; the wire-bonds and any lid add height.
- Feedthrough / flange: baseline 2.75″ CF (9D-275); may change per ST5. The head sits on it via
  a stand; harness (12 conductors) routes from the carriers down to the feedthrough pins.

## C. The user's stated idea (ST8 must CRITIQUE this, with reasons + alternatives)

> "My idea is to design a **cube with slots on each face** that can allow me to **insert and
> secure my chip carrier with sensors on top**. I don't want any epoxy/glue for the 3D package
> (I'll use epoxy for each individual sensor + chip carrier). Feel free to add additional
> suggestions and criticize my idea."

His current CAD is provided (his "original idea," assembled + disassembled):
`REFERENCE/cad/new_3d_idea_assembled.stp`, `REFERENCE/cad/new_3d_idea_disassembled.stp`.
His current single-axis mount (heritage reference): `REFERENCE/cad/old_1d_sensor.stp`
(Autodesk Inventor 2026, millimetres). ST8 must **load these in CAD** (real kernel, not
text-parsing — assembly transforms make raw point extents wrong) to extract true dimensions and
fit-check against the envelope, and to critique the existing slot geometry.

## D. What ST8 must deliver (see MISSION_BRIEF ST8 for the full prompt)

- **3–4 distinct concepts** (the user's slotted cube refined + genuinely different alternatives,
  e.g., edge-clip/spring retention, a frame/cage with captured carriers, a kinematic 3-face
  mount, a split-clamshell). Each: how the carrier is retained without glue, how it's inserted/
  removed, envelope fit (with the numeric check), material, machinability/printability,
  wire-bond & harness clearance, thermal/vibration robustness, and assembly/disassembly steps.
- A **criticism of the user's slotted-cube idea** specifically: slot tolerance vs the 8.89 mm
  brittle ceramic carrier (chipping), retention force without glue, how the sensor-on-top and
  wire-bonds survive insertion, harness strain relief, and whether slots on all 6 faces vs 3 is
  right.
- **Visuals for every concept** (isometric + orthographic + section), generated with the CAD
  tooling in `tools/cad/` — export **STEP + STL + PNG** per concept.
- A **weighted decision matrix** and a recommendation with the runner-up and the flip condition.
  This is a DECISION_GATE item.

## F. LCC02046 COMPATIBILITY GATE (every concept must pass) + recommended-direction seeds

**The user is willing to replace his slotted-cube idea — ST8 should put forward the design(s) it
believes are OPTIMAL, with a clear recommendation, not just neutral options.** But every concept
MUST pass this compatibility gate, because the LCC02046 is a **leadless, surface-mount** carrier:
its 20 contacts are **castellated edge/bottom pads**, gold-plated, designed to be **soldered** to
a PCB footprint. That drives two hard requirements a plain friction slot does not satisfy by
itself:

1. **Electrical interface without solder/glue (carriers must stay reusable):** the mount must
   connect the castellation/bottom pads via a **socket or spring/pogo/fuzz-button contacts** — a
   friction slot retains the body but connects nothing. Each concept must state exactly how the
   p1–p4 (+ any ground) pads land on the 12-conductor harness.
2. **Brittle-body handling:** 8.89 mm × 1.65 mm hermetic alumina — retention must not chip the
   ceramic or peel the castellations. Prefer edge/kinematic seating + controlled spring preload
   over a tight interference fit on fragile corners.

Also: minimal, **non-magnetic** metal near the plate (BeCu springs OK; no steel); verify any
socket/plastic is **UHV-compatible** (low outgassing) and survives the in-vessel temperature.

**Recommended-direction SEEDS (author's view of what's likely optimal — ST8 must develop,
visualize, critique, and PICK one):**
- **S1 — custom spring-contact seat ("mini-socket") per face:** the user's face pocket + retention
  lip PLUS gold-plated BeCu spring fingers / pogo / fuzz-button array contacting the LCC pads.
  Marries his slot idea with the electrical reality — reusable, no glue, self-connecting. Likely
  front-runner if UHV-safe contacts can be sourced/made.
- **S2 — clamp-lid + pogo block:** LCC face-up in a shallow ceramic/PEEK pocket; a non-magnetic
  spring-loaded lid presses it onto a pogo/fuzz-button contact block wired to the harness.
  Controlled preload protects the ceramic; clean disassembly.
- **S3 — commercial LCC-20 socket, UHV-screened:** search COTS LCC-20 sockets (Aries, Plastronics,
  Ironwood, Andon, 3M/Textool); instant reusable mechanical + electrical seat, but gate hard on
  non-magnetic + UHV/outgassing + envelope fit (sockets are bulky). Fast fallback if one passes.
- **S4 — refined slotted cube + flying leads:** if reusing the LCC electrically proves too hard,
  hold it in the slot and bring signals out with thin attached leads/flex (carrier reusable
  mechanically, connection semi-permanent). Simplest electrically; the honest baseline.

ST8: verify socket availability + UHV/magnetic suitability by web search, fit-check all against
Ø31.75×27.5 mm for 3 orthogonal faces, and recommend one with the runner-up + flip condition.

Sources: user CAD (new_3d_setup, old_1d_sensor); envelope figure; PACKAGING_LCC02046.md; rsi plan §2.2.
