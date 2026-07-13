# PACKAGING DATA — Hall die → Spectrum LCC02046 (for ST7). Data + user strategy only; no verdict here.

The user has PURCHASED the carrier; the open question is the wire-bond / signal-routing
strategy inside it. Re-verify every geometry number against the Spectrum datasheet before use.

## A. The carrier — Spectrum Semiconductor Materials LCC02046

20-pad **leadless ceramic chip carrier (LCC-20)**, hermetic alumina, gold-plated. Facts read
from the user's mechanical drawing (confirm on the Spectrum datasheet):

- Body: **0.350″ sq** (+.010/−.005); metallized area 0.314″ sq; cavity 0.240″ sq; die-attach
  cavity floor **0.160″ sq**.
- **20 castellated edge pads**, 5 per side, numbered **1–20** with a **pin-1 index** (chamfer).
  Feature pitch ~0.050″ (0.025″ typ). Edge-metallized castellations tie each cavity bond-shelf
  pad to the outer/bottom pad of the same number.
- Finish: all exposed metallization **gold, ≥20 µin, no nickel** (per drawing note 1).
- Thickness ~0.065″.
- Industry-standard .350″ 20-pin LCC geometry (cf. ADI "LS" 20-pin .350″ hermetic LCC).
- Datasheet / vendor: https://www.spectrum-semi.com/products/leadless-chip-carrier

## B. The die — AlGaN/GaN Hall plate (from the user's GDS layout "C1")

- Central **octagonal Hall plate** (2DEG mesa), with **four contacts** brought out to **four
  square bond pads** at the N/E/S/W sides, each joined to the octagon by a short tapered arm.
  These are the four Hall terminals: p1, p2, p3, p4 (opposite pairs (p1,p2) and (p3,p4);
  diagonals p1–p3 and p2–p4 are the bias/sense pairs — see SPECS.md phase table).
- Additional small pads / alignment-mark structures appear on the left; cross-hair alignment
  marks around the field.
- Gen-2 dies have **enlarged bond pads** (per rsi plan §2.1) to improve wirebond yield —
  relevant to which carrier pads are reachable and to non-horizontal-face bonding on the cube.

## C. The user's stated strategy (verbatim intent — ST7 must COMMENT on this, not restate it)

> "I purchased LCC02046. I assume I need to **wire-bond to the four corners** of the chip
> carrier [i.e., bond the die's four corner contacts to carrier pads]. My understanding is that
> I can **guide the signal to one side** through external connections using the bondpad [route
> all four signals to pads on one side of the carrier via the castellations, so the harness
> connects on one side]."

## D. Downstream constraints ST7 must respect

- The board expects the sensor on **J1 (DSUB-9)** with the convention **p1=1, p3=2, p2=6,
  p4=7**, twisted pairs (1,2)=bias, (6,7)=sense (HARDWARE_DATA §3). Whatever carrier pads are
  chosen, the die→carrier→harness mapping must land on that convention (or the change must be
  documented end-to-end).
- Assembly process (from SPECS / bring-up plan): Al wedge bonds, **EPO-TEK 353ND** die attach,
  **150 °C vacuum bake 1 h**, hermetic. Only the die + LCC are inside the vessel (hot); the
  carrier must survive the in-vessel environment.
- 3-axis future: the cube mounts **2–3 LCCs on orthogonal faces** — bonding on vertical faces
  is a yield risk the enlarged pads exist to mitigate. ST7 should note the one-die case now and
  the cube implication.

## E. What ST7 should verify/produce (see MISSION_BRIEF ST7 for the full prompt)
Confirm pad geometry/pitch from the Spectrum datasheet; recommend the specific carrier pads for
p1–p4 and any ground/shield pads; assess bond-wire length/loop/crossing and the one-side routing
idea; keep or remap the DSUB convention; flag packaging gotchas. Provide the pinout mapping table
die-contact → LCC pad → DSUB-9 pin.

Sources: user drawing (LCC02046); user GDS ("C1" Hall die); https://www.spectrum-semi.com/products/leadless-chip-carrier ; ADI LS 20-pin .350″ LCC reference https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-lcc/LCC_20_05-08-1260.pdf
