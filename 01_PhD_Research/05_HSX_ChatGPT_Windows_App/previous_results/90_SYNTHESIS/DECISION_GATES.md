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

## GATE 2 — Feedthrough purchase (~$1,145; hard to undo once the port is committed) — REVISED 2026-07-10

**Recommendation (revised): Accu-Glass 19C-275, P/N 110210** (19-pin, single-shell MIL-C-26482
circular, **2.75″ CF** — keeps the existing port) + 110230 pre-terminated vacuum-side PEEK/Kapton
assembly + 110232 shielded air-side assembly. `50_FLANGE/FLANGE_SELECTION.md` §9 (2026-07-10
addendum) — supersedes the prior 9C2-275 recommendation below it in the same file.

Found in a user follow-up: a third connector family (MIL-C-26482) also fits the existing 2.75″ CF
port, in a **single shell** (19 pins vs. the 9C2-275's 18 split across two shells), for **$427
less** system cost, with **one more spare pin**. The single shell removes the A/B mis-mate risk
that the prior pick (9C2-275) needed a dedicated FMEA/labeling plan to manage — it doesn't
mitigate that risk better, it has no such risk to mitigate.

**Two preconditions — BOTH must clear before the PO:**
1. **UW-Madison confirms the probe port is 2.75″ CF** (assumption A1 — one email: port size,
   whether a 4.5″ alternative exists, bakeout plan, in-vessel temperature at the probe, and
   whether the Ø31.75 mm envelope derives from the port bore).
2. **Accu-Glass confirms (a) the 110230/110240 contacts accept the harness's 24–26 AWG gauge and
   (b) the 19C-275's single-shell protrusion height** above the vacuum-side flange face — neither
   is stated on the fetched product pages. This single-shell height must still clear ST8's
   probe-head standoff budget (prior ledger capped it at **8.2 mm** against the *dual-tower*
   9C2-275 stack; a single shell is expected to need less, but the ST8 height ledger has **not
   been rerun** for a single-shell geometry — do not assume it clears without doing so).

**Fallback order if precondition 2 fails for the 19C-275:**
1. **Accu-Glass 9C2-275, P/N 100012** (18-pin, 2× 9-pin Sub-C, 2.75″ CF, system ≈ $1,572) — the
   prior primary; its own precondition (Sub-C tower protrusion height, same unread spec PDF) is
   still open and still needed if this fallback is used. `WIRING_PLAN.md`'s existing swap-tolerant
   pin map and anti-swap labeling plan apply here, not to the 19C-275.
2. **15D-450** (single 15-pin Sub-D, **4.5″ CF**, system ≈ $952) if UW-Madison confirms a 4.5″
   port is available/preferred; 25D-450 (+$32, 13 spare pins for guards) is the better buy if the
   port change happens anyway.

- **Flip condition:** precondition 1 returns "4.5″ available/preferred" → 15D-450/25D-450,
  regardless of the 2.75″-path outcome. Precondition 2 fails for the 19C-275 → 9C2-275 (whose own
  protrusion precondition then re-applies).
- **Reconciliation debt (new):** `WIRING_PLAN.md` (ST6, per-connector pin grouping + A/B swap
  FMEA) and `PACKAGING_3D_DESIGN.md` (ST8, height ledger, standoff design) were both built around
  the 9C2-275's dual-tower geometry and have **not** been re-derived for the 19C-275's single
  shell. This is cheap-desk-fix scale work (no new CAD, mostly deletion of the swap-risk
  machinery + a height-ledger substitution) but is not yet done — treat as open before the
  19C-275 path is signed off as final, not just before the PO.
- **Failure mode if wrong:** feedthrough arrives and either doesn't fit the port (precondition 1
  skipped), can't take the harness gauge or leaves no height for the probe head (precondition 2
  skipped) — $434–1,572 + weeks depending on which pick was ordered.

**Sign-off: ☐ approve 19C-275 PO after both preconditions ☐ fall back to 9C2-275 ☐ switch to 15D-450/25D-450**

---

## GATE 3 — Probe-head geometry freeze + ceramics/insert PO (in-vessel, custom parts)

**Recommendation: Concept B "SpringClamp Cube"** — 15 mm monolithic zirconia cube, per-face
drop-in pockets, PEEK inserts with 4 gold-plated BeCu (no-Ni) leaf springs on LCC pads
1/6/11/16, Ti picture-frame clamps; glue-free, reusable carriers, ~2-min swap.
`80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` (+ renders/STEP in `concept_B_springclamp_cube/`).
Runner-up: **Concept D "TriPlate"** (same contact interface on 3 flat plates — cheaper to make).

**Preconditions before the RFQ/PO (red-team wave 2 — all cheap desk fixes):**
1. **RT-16:** height ledger updated with the mated-connector stack + the Gate-2 protrusion answer
   (until then, standoff budget is 8.2 mm, not "~10 mm"). **Note (2026-07-10): GATE 2's primary
   pick changed to the single-shell 19C-275** (`FLANGE_SELECTION.md` §9) — the 8.2 mm figure was
   computed against the old dual-tower 9C2-275 stack and has not been recomputed for a single
   shell; recompute once the 19C-275 protrusion height is known, don't reuse 8.2 mm as-is.
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
