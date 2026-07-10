# DECISION_GATES — the three sign-offs this run needs from you (Tim)

Everything else in this review is reversible or free. These three spend money and/or are hard
to undo. Each gate lists the recommendation, the live options, the preconditions that must
clear **before** the money moves, and what flips the call. Supporting analysis: the parent
deliverable + `RED_TEAM.md` (finding IDs cited).

---

## GATE 1 — 3-axis board architecture (commit before ordering boards/parts)

**Recommendation: Option C — replicate `hsx_2026_v2` ×3, racked side-by-side on one baseplate
with insulating standoffs** (not a face-to-face stack). `30_3AXIS_ARCH/ARCHITECTURE_TRADE.md`.

| Option | Score /500 | One-line case | One-line risk |
|---|---|---|---|
| **C — 3 replicated boards (rack)** | **475** | Zero layout work; bit-identical to the Campaign-#1 board; physical channel isolation; blown channel = board swap | Harness dressing ×3 needs discipline (mitigated by `WIRING_PLAN.md`) |
| A — single larger 2/4-layer board | 310 | One clean board, natural rev-B | New layout voids bench heritage; a routing mistake before Nov 2026 machine time is unrecoverable |
| B — 6-layer multichannel | 275 | Best copper/planes | Maximum respin + new-stackup risk for a problem C solves physically |

- **Cost:** ~$30/set PCBs (existing gerbers) + ~2× component sets (~low $100s). All parts
  confirmed active/orderable (`10_COMPONENTS/bom_verdict.csv`).
- **Precondition:** none — this can be signed and ordered today. Suggested sequencing (from
  ST3): order boards+parts in July, hold assembly of boards 2–3 until the ΔV anomaly closes
  and Campaign #1 debriefs.
- **Flip condition:** the ΔV gain anomaly (or Campaign #1) forces a layout respin anyway →
  heritage is void → switch to A.
- **Failure mode if wrong:** three-board rack proves mechanically awkward at the flange — cost
  is a baseplate re-machine, not a board respin (that asymmetry is why C wins).

**Sign-off: ☐ approve C ☐ choose A ☐ choose B**

---

## GATE 2 — Feedthrough purchase (~$1,572; hard to undo once the port is committed)

**Recommendation: Accu-Glass 9C2-275, P/N 100012** (18-pin, 2× 9-pin Sub-C, **2.75″ CF** —
keeps the existing port) + 2× 100040 vacuum-side PEEK/Kapton assemblies + 2× 100020 shielded
air-side assemblies. `50_FLANGE/FLANGE_SELECTION.md` (+ its 2026-07-10 addendum).

**Two preconditions — BOTH must clear before the PO (red-team RT-01/RT-16):**
1. **UW-Madison confirms the probe port is 2.75″ CF** (assumption A1 — one email: port size,
   whether a 4.5″ alternative exists, bakeout plan, in-vessel temperature at the probe, and
   whether the Ø31.75 mm envelope derives from the port bore).
2. **Accu-Glass confirms the Sub-C tower protrusion height** above the vacuum-side flange face
   (spec PDF unreadable this run; catalog gave 0.750″ tower centers but not height). ST8's
   height ledger caps the probe-head standoff at **8.2 mm** with the mated 100040 connector
   stack included; towers >~10–15 mm breach the Ø31.75×27.5 mm envelope by 1.8–6.8 mm →
   **this one phone call gates BOTH the feedthrough PO and the Gate-3 ceramics PO.**

- **Runner-up:** 15D-450 (single 15-pin Sub-D, **4.5″ CF**, system ≈ $952); if the port changes
  anyway, 25D-450 (+$32, 13 spare pins for guards) is the better buy.
- **Flip condition:** precondition 1 returns "4.5″ available/preferred," or precondition 2
  returns a tower height the envelope can't absorb → runner-up.
- Also note: connectors may be factory-unmarked A/B — `WIRING_PLAN.md`'s pin map is
  swap-tolerant by construction, and adds labeling; no extra risk carried.
- **Failure mode if wrong:** feedthrough arrives and either doesn't fit the port (precondition
  1 skipped) or leaves no height for the probe head (precondition 2 skipped) — $1,572 + weeks.

**Sign-off: ☐ approve 9C2-275 PO after both preconditions ☐ switch to 15D-450/25D-450**

---

## GATE 3 — Probe-head geometry freeze + ceramics/insert PO (in-vessel, custom parts)

**Recommendation: Concept B "SpringClamp Cube"** — 15 mm monolithic zirconia cube, per-face
drop-in pockets, PEEK inserts with 4 gold-plated BeCu (no-Ni) leaf springs on LCC pads
1/6/11/16, Ti picture-frame clamps; glue-free, reusable carriers, ~2-min swap.
`80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` (+ renders/STEP in `concept_B_springclamp_cube/`).
Runner-up: **Concept D "TriPlate"** (same contact interface on 3 flat plates — cheaper to make).

**Preconditions before the RFQ/PO (red-team wave 2 — all cheap desk fixes):**
1. **RT-16:** height ledger updated with the mated-connector stack + the Gate-2 tower answer
   (until then, standoff budget is 8.2 mm, not "~10 mm").
2. **RT-17:** preload tolerance chain computed end-to-end; worst-case ±0.3 mm stack-up exits
   the 0.2–0.5 mm spring working band → mandate the pocket-floor lapping step (or lengthen the
   spring finger) in the drawing package. Zirconia "±1 % as-sintered" had no vendor backing —
   quote must state achieved tolerance.
3. **RT-18:** add a green-machined **corner key** so a carrier cannot seat 90°/180° rotated
   (square pocket + symmetric contacts currently allows a silent axis/sign flip guarded only
   by procedure).

**Bond-blocking sub-gate (no money, but irreversible — RT-02, before FIRST bond):**
- Verify LCC02046 pad-numbering direction on a physical carrier against drawing PB-CA8272-B
  (chamfer as datum), and pin die p1–p4 orientation to the GDS labels. The pad map
  (p1→1, p3→16, p2→11, p4→6 → DSUB 1/2/6/7) is written chamfer-relative and survives a
  numbering-direction surprise, but the *printed artifacts* must be corrected if it flips.

- **Flip conditions:** monolithic cube quote >2–3× the TriPlate set, unachievable tolerance, or
  lead time past the ceramics deadline → Concept D. Sustained in-vessel temperature >~200 °C →
  keep the geometry, swap BeCu leafs for Au/BeCu fuzz buttons (and revisit PEEK insert
  material — PEEK Tg is 143 °C; red-team RT-series notes it's acceptable below ~200 °C but
  the HSX probe temperature is still UNVERIFIED, same UW email as Gate 2).
- **Failure mode if wrong:** a seated-but-rotated or intermittent-contact carrier in the vessel
  = a silently wrong vector component for a whole campaign — this is why RT-17/18 are
  mandatory, not advisory.

**Sign-off: ☐ freeze B geometry after RT-16/17/18 fixes ☐ switch to D ☐ request another concept**

---

## Not gated (proceed without sign-off)
Keyed J2/J5 housings (~$10s, prevents the #1 die-killer); star-ground fan-out wiring; 2× PCB
reorder ($30/set, reversible); LCC/die verification steps; all rev-B items (deferred anyway).
