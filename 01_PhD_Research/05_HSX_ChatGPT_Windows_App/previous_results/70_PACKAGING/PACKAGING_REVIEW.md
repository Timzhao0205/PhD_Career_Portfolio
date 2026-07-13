# ST7 — PACKAGING REVIEW: AlGaN/GaN Hall die → Spectrum LCC02046 (Q7)

Reviewer: packaging-wirebond-specialist · 2026-07-10 · effort HIGH (in-vessel hardware)
Scope: comment on the user's wire-bond + one-side routing strategy, per QUESTIONS Q7 /
MISSION_BRIEF ST7. Red-team pass pending before synthesis.

---

## 1. BLUF — verdict: **ADJUST (two corrections), intent is sound**

| # | User's strategy element | Verdict | Correction |
|---|---|---|---|
| 1 | "Wire-bond to the four **corners** of the chip carrier" | **ADJUST** | Bond to the **middle pad of each side** (pads 1, 6, 11, 16 in JEDEC-style numbering), not corners. An LCC-20 has 5 pads per side and **no pads at the exact corners** (one corner is the index chamfer). Mid-side pads sit directly opposite the die's N/E/S/W pads → shortest, radial, **non-crossing** bonds. |
| 2 | "Guide the signal to one side through external connections using the bondpad" | **ADJUST (relocate the idea)** | The carrier **cannot** re-route: each castellation connects a cavity **shelf pad to the outer/bottom pad of the same number only** — there is no pad-to-pad routing inside or on the carrier. "All signals on one side" is achieved at the **mount/socket level (ST8)**, where the spring/pogo contacts on pads 1/6/11/16 are wired into one harness exit. Do **not** add solder jumpers on the carrier (outgassing, magnetic solder risk, rework damage on a brittle body). |
| 3 | (implied) hermetic lid CL-30010 | **REJECT the standard lid** | Spectrum's recommended combo lid CL-30010 is **Kovar/Alloy 42 with Ni plating — ferromagnetic**. It would corrupt the Hall measurement and waste the non-magnetic/no-Ni carrier you specifically bought. Run **open-cavity** in-vessel (also avoids UHV virtual leaks). |

**Failure mode if the original strategy were executed as stated:** bonding four wires toward
one side/corner region forces the far die pad's wire to ~4+ mm sweeping over the die and over
other wires → wire-to-wire short or wire-to-mesa short (exactly the user's #1 fear), plus low
pull-strength long Al wedge bonds; a solder-jumpered "one-side" carrier adds fluxed, magnetic
(Sn-Pb/Ni) material into UHV next to the Hall plate.

---

## 2. Verified carrier facts (LCC02046)

| Fact | Value | Source / status |
|---|---|---|
| Part / type | LCC02046, 20-pad leadless ceramic chip carrier, alumina | **Verified** — Spectrum product page [1] |
| Body | 0.350″ × 0.350″ (8.89 mm sq) | **Verified** [1]; matches user drawing (+.010/−.005 tol from drawing) |
| Pad count / layout | 20 pads, 5 per side | **Verified** [1] ("Body configuration 5×5") |
| Pad pitch | 0.050″ on center (pad width ~0.025″ typ) | Pitch **verified** [1]; pad width **user-drawing only** |
| Cavity (die-attach floor) | 0.160″ × 0.160″ (4.06 mm sq) | **Verified** [1] ("Cavity 0.16 × 0.16″"); user drawing adds cavity **opening 0.240″ sq** at shelf level — *interpretation: 0.160″ is the floor, 0.240″ the opening above the bond shelf; consistent two-tier cavity* |
| Seal ring | OD 0.314″ sq / ID 0.254″ sq | **Verified** [1]; user drawing's "metallized area 0.314″" agrees |
| Thickness | ~0.065″ (1.65 mm) | **User-drawing only** (UNVERIFIED online) |
| Finish | Gold, **no nickel**, non-magnetic ("NON-MAGNETIC / NO NI") | **Verified** [1]; ≥20 µin Au thickness is **user-drawing note 1** (UNVERIFIED online — page quotes Au thickness only for a different P/N) |
| Mfg drawing | PB-CA8272-B | **Verified** [1] |
| Recommended lid | CL-30010 combo lid | **Verified** [1]; combo lids are **Kovar/Alloy 42, Ni+Au plated** per Spectrum/Materion combo-lid pages [2][3] → **ferromagnetic, do not use** |
| Pad numbering direction / pin-1 location | Pin-1 index chamfer per user drawing. JEDEC MS-004-style convention: terminal 1 = **middle pad of the index side**, numbering **counterclockwise viewed from the top (cavity up)** → mid-side pads are 1, 6, 11, 16 | **UNVERIFIED online** — the Spectrum PDF datasheet [4] is image-only (not machine-readable) and the ADI LCC-20 cross-reference [5] was unreachable (ECONNRESET, 2 attempts). Marked ENGINEERING JUDGMENT; see mitigation below |
| Cross-check geometry | TopLine LCC20 0.35″ sq, 0.050″ pitch, 0.160″ sq cavity, castellations standard, Al₂O₃ | **Verified** (independent second source) [6] |

**Mitigation for the numbering uncertainty:** every instruction below is stated physically —
"**the middle pad of each side, identified relative to the pin-1 chamfer**" — which is correct
regardless of whether Spectrum numbers CW or CCW. The assembler must confirm pad numbers
against drawing PB-CA8272-B (in hand with the purchased parts) before bonding, and the numbers
in §4 must be updated if the drawing numbers CW. **The die→DSUB mapping is unaffected** (it is
fixed by which *physical side* each die terminal faces, not by the printed pad number).

---

## 3. Die facts and orientation assumption

| Item | Value | Status |
|---|---|---|
| Die | AlGaN/GaN octagonal Hall plate, 4 square bond pads at N/E/S/W via tapered arms; terminals p1–p4; opposite pairs (p1,p2), (p3,p4) | User GDS description (PACKAGING_LCC02046.md §B) — **GDS image not in pack** |
| Die size | "a few mm" — **assumed 2–3 mm sq**, fits the 4.06 mm cavity floor with ≥0.5 mm clearance | ASSUMPTION (die outline not provided) |
| Pad metallization | **Assumed Au-topped** (typical AlGaN/GaN ohmic/overlay stack) | ASSUMPTION — confirm from fab runsheet; changes the intermetallic assessment in §6 |
| Orientation | **Assumed p1 = N, p2 = S, p3 = E, p4 = W** with die alignment marks used to fix rotation | ASSUMPTION — must be pinned to the GDS labels before first bond; a 90° rotation swaps bias/sense pairs downstream (detectable but confusing), a 180° rotation flips signs |

---

## 4. Recommended pad map — die contact → LCC pad → harness → DSUB-9

Convention preserved exactly as HARDWARE_DATA §3 (p1=1, p3=2, p2=6, p4=7; twisted pairs
(1,2) and (6,7)). No change to the board or harness convention is needed — the carrier pad
choice is invisible to the board because the ST8 mount does the pad→harness dressing.

| Die terminal | Die pad location (assumed §3) | LCC pad # (JEDEC-style; = **middle pad of side**) | Carrier side (chamfer = datum, cavity up, pin-1 side = "N") | Harness wire / twisted pair | DSUB-9 pin (J1) |
|---|---|---|---|---|---|
| **p1** | N | **1** | N (index side) | Pair A, wire 1 | **1** |
| **p3** | E | **16** | E | Pair A, wire 2 | **2** |
| **p2** | S | **11** | S | Pair B, wire 1 | **6** |
| **p4** | W | **6** | W | Pair B, wire 2 | **7** |

Mnemonic: **p1 lands on pad 1** (the index-side middle pad) — self-documenting during assembly.

Notes:
- Under 8-phase spinning the (1,2) and (6,7) pairs alternate bias/sense roles per phase (the
  muxes rotate the roles); the *pairing* is fixed at the harness, the *role* is not. The table
  above is the wiring truth; don't relabel wires "bias"/"sense" permanently on the harness.
- Note the DSUB pairs (p1,p3) and (p2,p4) are **adjacent** (90°-apart) die terminals, not the
  geometric opposite pairs — that is the established board convention (HARDWARE_DATA §3);
  keep it, it's already validated on the bench.
- Remaining 16 pads: leave **unbonded and unconnected** inside the cavity. At the ST8 mount,
  optionally land shield/drain on **pads 3, 8, 13, 18** (the other mid-flank pads, one per
  side) to form a guard ring around each signal pad — the castellation itself provides ~0.050″
  creepage between the signal pad and its neighbors. ENGINEERING JUDGMENT; only worthwhile if
  ST6's shield plan wants a per-carrier drain point. Do **not** bond guard wires in the cavity
  (added crossing risk, no benefit at 100 µA / mV levels).
- If the seal ring metallization is electrically floating, tying it to the harness shield at
  the mount (spring contact on the top metallization) removes a floating conductor next to the
  plate — optional, ENGINEERING JUDGMENT, coordinate with ST6.

---

## 5. Point-by-point comment on the user's strategy

### (a) "Bond to the four corners" — right instinct, wrong target
The die's four pads are at **mid-sides** (N/E/S/W), not corners; and the LCC-20 has **no
corner pads** (5 per side, the corners are bare ceramic, one carrying the index chamfer).
The geometrically correct move is the one his instinct is reaching for: **four radial bonds,
one per side, to the middle pad of each side (1/6/11/16)**. This gives:
- equal bond lengths (~1.5–2 mm, see §5c) — matched parasitics on all four terminals, which
  spinning likes;
- 90° separation between wires — **zero crossing risk**;
- maximum distance from each wire to its neighbors' pads.
Bonding to corner-adjacent pads (e.g., 3/8/13/18) would skew each wire ~2 pads sideways
(~2.5 mm lateral), lengthening wires ~40–60% and angling wedge feet — worse, no benefit.

### (b) "Guide all signals to one side" — right requirement, wrong layer
What the carrier **can** do: each of the 20 castellations ties its **shelf pad ↔ edge ↔
bottom pad, same number**. What it **cannot** do: route pad m to pad n. There are no
internal traces. So the four signals *necessarily* exit on four sides if bonded per §4.
Three ways to still get a one-side harness:
1. **(REJECT)** Bond all four die pads to one side's pads (e.g., 4–8): the far (opposite)
   die pad's wire becomes ~4–4.5 mm and must fly **over the die and over the other wires**
   — crossing + sag-short risk, and long Al wedge bonds at low loop are weak. Kills the
   symmetric parasitics too.
2. **(REJECT)** External jumpers (soldered wires pad-to-pad around the body): solder + flux
   residue in UHV, Sn/Ni magnetic contamination next to a Hall plate, thermal-cycling joints
   on a brittle 8.89 mm body, and it makes the carrier non-reusable — contradicts ST8's
   glue-free reusable-carrier requirement.
3. **(ADOPT)** Do it **in the ST8 mount**: the socket/spring seat contacts pads 1/6/11/16
   wherever they physically are and its internal wiring dresses all four conductors (as the
   two twisted pairs) to a single harness exit per face. One-side harness achieved, carrier
   stays standard and reusable. **This is where "guide the signal to one side" belongs — flag
   to ST8 as an interface requirement: contacts at the mid-side pads of each face, one
   harness exit per carrier.**

### (c) Bond-wire assessment (Al wedge, 25 µm / 1-mil assumed)

| Parameter | Value | Basis |
|---|---|---|
| Bond span, die pad → mid-side shelf pad | ~1.5–2.0 mm horizontal (die half-width ~1.0–1.5 mm from center; shelf pad inner edge ~3.0 mm from center) + shelf step ~0.4–0.5 mm up from floor | ENGINEERING JUDGMENT from drawing dims (floor 4.06 mm, opening 6.10 mm); shelf step height UNVERIFIED |
| Wire length | ~2.0–2.5 mm — comfortably inside routine Al-wedge range (≤ ~3–4 mm) | judgment |
| Loop height | Wedge bonds are inherently low-loop: keep **150–300 µm** above the die surface; die-side bond first (first bond on the die pad, second on the shelf) so the loop rises away from the mesa edge | standard wedge practice, judgment |
| Crossings | **None** with the §4 radial map — the four wires point at 90° to each other | geometric fact |
| Wire resistance | 25 µm Al: ~0.054 Ω/mm → ~0.13 Ω per bond — negligible vs the ~1 kΩ plate; and residual mismatch is cancelled by spinning | one-line calc (ρ_Al = 2.65 µΩ·cm, A = 4.9×10⁻⁶ cm²) |
| Metallurgy | Al wedge on **Au shelf pads** (and Au die pads if §3 assumption holds) → Au–Al intermetallic couple at both feet. Benign at 150 °C×1 h bake; grows with long hot exposure (§6). Carrier's **no-Ni thin-Au over refractory** metallization is a *good* Al-wedge surface | judgment + verified finish [1] |
| Bond pull qual | Do a destructive pull-test coupon (same carrier type) before committing real dies; MIL-STD-883 Method 2011 thresholds (≥2.5 gf for 1-mil wire) | standard practice |

Gen-2 enlarged die pads (rsi plan §2.1) directly raise wedge placement tolerance — keep them.

### (d) DSUB-9 convention — **preserved**
Because the mount does the routing, the §4 map lands exactly on p1=1, p3=2, p2=6, p4=7 with
pairs (1,2)/(6,7) twisted from the mount contacts onward. **No end-to-end convention change is
needed or recommended** — the convention is already bench-validated on `hsx_2026_v2`, and
changing it would touch ST2 (netlist), ST5 (feedthrough pin plan) and ST6 (harness) for zero
gain. Keep bias-pair and sense-pair conductors twisted separately and separated at the
feedthrough per ST6.

### (e) Ground / shield on the carrier
The Hall plate is fully differential and floats on a 100 µA source — there is **no ground
terminal on the die**, and none should be bonded. Shielding is a harness/mount function:
guard-ring option on pads 3/8/13/18 and optional seal-ring drain per §4 notes. Keeping the
two pairs on opposite side-pairs of the carrier (N/E vs S/W) plus twisting from the contacts
onward is sufficient at these signal levels and ≤20 kHz. ENGINEERING JUDGMENT.

### (f) Vertical faces on the 3-axis cube
**You cannot wire-bond on a vertical face** — wedge bonders need the bond plane horizontal
(within a few degrees) and clear tool access. The LCC-per-face architecture is exactly what
makes the cube buildable: **bond and qualify every die flat in its own carrier on the bench,
then mount finished carriers on the orthogonal faces.** Never plan any bonding after cube
assembly. This is a genuine strength of the user's overall architecture — say so. The gen-2
enlarged pads further de-risk the (bench, horizontal) bonding yield; they are *not* a license
to bond on the cube.

---

## 6. Packaging gotchas

| # | Item | Assessment | Failure mode if ignored |
|---|---|---|---|
| G1 | **EPO-TEK 353ND die attach** | Heat-cure epoxy, typical cure **150 °C / 1 h**; **electrically insulating**; passes **NASA ASTM E595** (TML 0.76%, CVCM 0.01% per distributor listing [7] — TML/CVCM figures UNVERIFIED against the official TDS, which redirects to Meridian [8] without numbers). Insulating attach is correct — the die needs no backside contact. Cure **fully before** the vacuum bake; keep the fillet minimal (less outgassing surface, no wicking up to the shelf pads). Note Tg of 353ND is ~90 °C (commonly quoted — **UNVERIFIED**): above Tg the epoxy is rubbery with higher CTE; acceptable for a small die at these stakes, but log it | Under-cured epoxy outgasses in the vessel; epoxy on a shelf pad ruins the wedge bond |
| G2 | **150 °C vacuum bake, 1 h** | Fine for alumina + Au + cured 353ND (353ND is marketed as a high-temperature epoxy [8]). Au–Al intermetallic growth in 1 h at 150 °C is negligible | — |
| G3 | **Au–Al couple (purple plague)** | Al wedge on Au at both feet. Slow at ≤150 °C; becomes a life issue with long hot in-vessel dwell. **If a Au ball/wedge bonder is accessible, prefer Au wire** (monometallic both ends if die pads are Au) — mark as *nice-to-have, rev-B*; Al wedge is acceptable **now** with pull-test qual + visual after bake | Kirkendall voiding → open bond mid-campaign (one open kills the axis) |
| G4 | **Hermeticity / lid** | No lid is specified in the plan — and that is the **right call**: (i) a sealed 1-atm cavity inside UHV is a virtual-leak / lid-deflection liability; (ii) the recommended CL-30010 combo lid is **Kovar/Alloy 42 + Ni plating = ferromagnetic** [2][3] — disqualifying next to a Hall plate. Run **open cavity**; the "hermetic" carrier property is irrelevant in-vessel. Cost: exposed bonds → handling discipline (G6) and plasma-facing exposure. If the HSX port geometry exposes the die to direct plasma light/particles, a **non-magnetic ceramic (alumina) lid attached with 353ND, unsealed (vented)** is the fallback — UNVERIFIED whether needed; defer to the HSX-side collaborators | Kovar lid: field distortion at the measurement point — silently wrong B data. Sealed lid: virtual leak flagged by HSX vacuum QA |
| G5 | **Carrier in-vessel survivability** | Alumina + Au, no organics except the 353ND bond line: compatible with UHV and −200…250 °C class environments (same materials class as the feedthrough ceramics). Verified materials, judgment on the conclusion | — |
| G6 | **Brittle 8.89 mm body handling** | Vacuum pickup or carbon/ESD tweezers on the bare ceramic edges only; never grip castellations (Au pad peel) or corners (chips destroy the index datum). Store bonded carriers in waffle trays; bonds are unencapsulated (no glob-top — it would add outgassing and block cube clearance) | Chipped castellation → open circuit discovered after cube assembly |
| G7 | **ST8 interface handoff** | The mount must contact the **mid-side pads** (1/6/11/16) at minimum, must not press on bond wires or overhang the open cavity, and provides the one-side harness exit (§5b). Feed this to ST8 as a hard interface requirement | Mount contacts wrong pads → open/short at first power-up |

---

## 7. Verdict summary

| Recommendation | Keep / adjust | Failure mode if wrong |
|---|---|---|
| Bond p1–p4 radially to the **mid-side pads 1/16/11/6** (physically: middle pad of each side, chamfer as datum) | **Adjust** (from "corners") | Corner/one-side bonding → long crossing wires → intermittent shorts, low pull strength |
| One-side harness exit implemented **in the ST8 mount**, not on the carrier | **Adjust** (relocate) | Jumpered carrier → UHV contamination, magnetic solder, non-reusable carrier |
| Keep DSUB-9 convention p1=1, p3=2, p2=6, p4=7; pairs (1,2)/(6,7) | **Keep** | Convention change ripples through ST2/ST5/ST6 and invites the exact miswiring the user fears |
| Open cavity, **no CL-30010 lid** | **Adjust** (reject the catalog lid) | Ferromagnetic lid corrupts B measurement; sealed cavity = virtual leak |
| Al wedge now (with pull-test qual); consider Au wire rev-B | **Keep (qualified)** | Unqualified long-term Au–Al → open bond mid-campaign |
| Bond flat on the bench, then mount; never bond on the assembled cube | **Keep (make explicit)** | Attempted vertical-face bonding → near-zero yield, scrapped dies |

**Alternative pad map (only if the ST8 mount design ends up unable to contact all four
mid-side pads):** shift every bond by **one pad in the same rotational direction** — i.e.,
p1→pad 2, p4→pad 7, p2→pad 12, p3→pad 17 (each the pad adjacent to the mid-side pad).
Bond lengths grow ~20–30% (still ≤2.5 mm) and the four wires remain crossing-free because
the shift is uniform. Do **not** go further off-axis than ±1 pad, and prefer fixing the
mount geometry instead of the bond map.

---

## 8. Assumptions made (orchestrator to log in 05_STATE/ASSUMPTIONS.md — ST7 does not write 05_STATE)

1. Die outline 2–3 mm sq, pads at N/E/S/W near the die edges (GDS image not in pack).
2. Die terminal labels: p1=N, p2=S, p3=E, p4=W — **must be confirmed against the GDS before
   first bond**; the §4 table's die-side column moves with this.
3. Die pad metallization is Au-topped (drives the G3 intermetallic assessment).
4. LCC pad numbering: JEDEC MS-004-style (pin 1 = mid-pad of index side, CCW viewed cavity-up).
   Physical instructions are numbering-agnostic; confirm numbers on drawing PB-CA8272-B.
5. Bond shelf step height ~0.4–0.5 mm (typical two-tier LCC; not on the readable sources).
6. Wire: 25 µm (1-mil) Al, wedge-wedge, per the stated assembly process.

## 9. Requests to the orchestrator

- **Attach `LCC02046_datasheet.pdf` (drawing PB-CA8272-B)** to the pack — the online PDF [4]
  is image-only and could not be machine-read; pad numbering direction and shelf step height
  need it (or a 5-minute look by the user at the paper drawing shipped with the parts).
- **Attach the die GDS image ("C1")** — needed to pin p1–p4 to physical N/E/S/W and close
  assumption 2 before anyone bonds.
- Log assumptions §8 into `05_STATE/ASSUMPTIONS.md` and route this file to `red-team-critic`.

## Sources

1. Spectrum Semiconductor Materials — Leadless Chip Carrier product table (LCC02046 row: 20
   pads, 0.35″ sq, cavity 0.16″ sq, 0.050″ pitch, S/R OD 0.314″ / ID 0.254″, lid CL-30010,
   "NON-MAGNETIC / NO NI", drawing PB-CA8272-B):
   https://www.spectrum-semi.com/products/leadless-chip-carrier (fetched 2026-07-10)
2. Spectrum Semiconductor Materials — Combo Lids (square): Kovar/Alloy 42, Ni+Au plating:
   https://www.spectrum-semi.com/products/combo-lid-square
3. Materion — Combo Lids (construction: Kovar/Alloy 42, Ni/Au):
   https://materion.com/products/microelectronics-packaging-materials/hermetic-packaging-lids/combo-lids
4. Spectrum LCC02046 datasheet PDF (fetched; image-only, not machine-readable):
   https://www.spectrum-semi.com/sites/default/files/pdfs/LCC02046.pdf
5. ADI LCC-20 .350″ outline (cross-reference; UNREACHABLE during run — ECONNRESET ×2):
   https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-lcc/LCC_20_05-08-1260.pdf
6. TopLine LCC20 (independent geometry cross-check: 0.35″ sq, 0.050″ pitch, 0.160″ sq cavity,
   Al₂O₃, castellations standard): https://www.topline.tv/lcc.html
7. Fiber Optic Center — EPO-TEK 353ND listing (cure 150 °C/1 h typ; NASA ASTM E595; TML
   0.76% / CVCM 0.01%): https://focenter.com/epo-tekr-et353nd-heat-cure-epoxy-8oz-9939
8. Meridian Adhesives (EPO-TEK) — 353ND product page (high-Tg, electrically insulating,
   passes NASA ASTM E595): https://meridianadhesives.com/products/epo-tek-353nd/
   (official TDS at epotek.com/docs/en/Datasheet/353ND.pdf now 301-redirects here; exact Tg
   and operating-temperature numbers therefore **UNVERIFIED** this run)
9. JEDEC MS-004 (leadless chip carrier, .050″ centers, Type C) — standard referenced for the
   numbering convention; document access-restricted:
   https://www.jedec.org/standards-documents/docs/ms-004-b
10. Internal: `01_MISSION/REFERENCE/PACKAGING_LCC02046.md` (user drawing readout + strategy);
    `01_MISSION/HARDWARE_DATA.md` §3 (DSUB-9 convention), §4 (locked constraints);
    `01_MISSION/REFERENCE/PACKAGING_3D_ENVELOPE.md` (ST8 interface, zirconia cube).
