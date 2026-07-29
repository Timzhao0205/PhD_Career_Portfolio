# CONNECTION_CHECK — ST2 / Q2 · netlist & pinout verification

Source of truth parsed: **live netlist** `01_MISSION/REFERENCE/hsx_2026_v2.net` (KiCad
E-format, Eeschema 10.0.3, exported 2026-07-09T17:17:50) + `hsx_2026_v2_bom.csv`. All 40
components in the BOM are present in the netlist `(components)` block (10×C, 7×J, 10×R,
8×TP, 5×U — counts reconcile exactly). All 36 nets in the netlist were read and traced by
hand below. Where the netlist and `HARDWARE_DATA.md` disagree, both are reported.

## Bottom line up front: **PASS-with-flags**

No wiring defect, short, or mis-numbered pin was found. The bias→chopper→plate→sense→in-amp
signal path is topologically correct and — on close inspection of the mux/chopper channel
assignment — correctly implements the documented 8-phase spin table (a1 rotates the bias/sense
diagonal, a0 flips sense polarity for amplifier-offset cancellation, a2 flips bias polarity via
the chopper). J1 (Amphenol D09S33E6GX00LF) is confirmed the correct gender/pinout and its
schematic-net-to-physical-pin mapping matches `HARDWARE_DATA` §3 exactly. Flags below are all
low-severity: one net-naming inconsistency (cosmetic), one operational caution (bias mux goes
open when EN=0), one item that could not be verified from the files in this pack (custom
footprint pad geometry — no `.kicad_mod` was supplied), and the v1→v2 regression check is based
on the documented design intent rather than an actual v1-netlist diff (no v1 file exists in this
pack).

---

## 1. J1 verification — Amphenol D09S33E6GX00LF

| Check | Finding | Verdict |
|---|---|---|
| Gender | Digi-Key spec table: **"Receptacle, Female Sockets"** [1]. Amphenol P/N decode: `D`=D-Sub, `09`=9-position, **`S`=Socket (female)** (confirmed against sibling parts `D09P...`=Plug/male vs `D09S...`=Socket/female in the same family) [2]. BOM/netlist schematic symbol is `Conn_01x09_Socket` [3] — **gender label agrees on all three sources.** | PASS |
| Positions / rows | 9 positions, 2 rows (5+4) [1]. Netlist declares 9 pins (1–9), pins 3/4/5/8/9 unconnected — consistent with a standard DE-9 shell. | PASS |
| Mount / termination | Through-hole, right-angle, solder [1]; BOM footprint name `DSUB-9_Pins_Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm` — "Horizontal"+"EdgePinOffset" is consistent with a right-angle THT edge-mount D-sub. | PASS |
| Footprint identity | Netlist footprint field: `D09S33E6GX00LF:AMPHENOL_D09S33E6GX00LF` [3] — a **dedicated footprint library named after the exact MPN**, not a generic DSUB-9 stand-in. Good practice signal. | PASS (see caveat) |
| Pad-level geometry | The actual `.kicad_mod` footprint file is **not included** in this review pack (only the `.net`/BOM were supplied) — pad-to-physical-pin-number correspondence inside that footprint could not be independently opened and inspected. | **UNVERIFIED** — recommend a first-article continuity check (schematic net → physical J1 pin, ohmmeter) before first power-up; this is naturally covered by ST6's pre-power continuity procedure. |
| Standard D-sub numbering / "solder-cup mirror" caution | J1 is a **through-hole, right-angle, solder-terminal PCB receptacle**, not a solder-cup cable connector — so the classic "solder-cup rear-view mirrors the front-view pin order" trap does not apply to J1 itself (its pin-1 index is molded into the shell and the footprint is fixed once soldered). The caution **does** apply to the **mating cable connector** on the sensor-harness side (whoever hand-wires that solder-cup plug must work from the correct face). This is industry-standard D-sub practice per DIN 41652/MIL-DTL-24308 (referenced, full text not fetchable — see Sources); flagged for ST6's harness assembly procedure, not a defect in this board. | Engineering judgment — flagged for ST6, not a J1 defect |
| Sensor pin convention (p1=1, p3=2, p2=6, p4=7) | Netlist nets: `/pin1`→J1.1, `/pin2`→J1.6, `/pin3`→J1.2, `/pin4`→J1.7. Cross-checked against plate labels via the mux wiring (§2 below): net `/pin1` carries plate **p1**, `/pin2` carries plate **p2**, `/pin3` carries plate **p3**, `/pin4` carries plate **p4**. → **pin1=p1, pin6=p2, pin2=p3, pin7=p4 — exact match to `HARDWARE_DATA` §3.** | PASS |
| Twisted-pair convention (1,2)=p1&p3 bias, (6,7)=p2&p4 sense | Confirmed by trace (§2): the bias mux (U1) only ever drives the (p1,p3) diagonal or the (p2,p4) diagonal — never a mixed pair — so grouping DSUB pins (1,2) and (6,7) as the two harness twisted pairs is electrically sound (each twisted pair always carries one complete diagonal's current-loop, not a cross-diagonal mix). | PASS |
| Spare pins | J1 pins 3,4,5,8,9 are all `unconnected-(J1-Pin_N-PadN)` in the netlist — matches `HARDWARE_DATA` "Pins 3/4/5/8/9 spare." | PASS |

**Sources for J1:** [1] Digi-Key product page, D09S33E6GX00LF, Amphenol ICC (FCI) —
https://www.digikey.com/en/products/detail/amphenol-cs-fci/D09S33E6GX00LF/1539664 (fetched
2026-07-10; spec table: Positions=9, Rows=2, Gender="Female Sockets (Receptacle)", Mounting
Type="Through Hole, Right Angle with Board Lock and Mounting Brackets", Termination="Solder",
Shell Size="1 (DE, E)"). Direct fetch of the Amphenol-hosted datasheet PDF
(`cdn.amphenol-cs.com/.../io_dsub_brochure.pdf`) and product page
(`amphenol-cs.com/product/d09s33e6gx00lf.html`) both returned HTTP 403 from this environment;
Digi-Key's vendor page (an accepted primary source per `SOURCE_STANDARDS.md` §1) was used
instead and is internally consistent with the Amphenol part-number-decode pattern seen across
the D09Sxxx/D09Pxxx family [2]. [2] Amphenol/FCI Delta-D part-number pattern
(`D`+2-digit-position-count+`S`|`P` for socket/plug), corroborated across multiple listed
part numbers (e.g. `D09P33E6GX00LF` = plug/male counterpart of the same shell) — Digi-Key/
Mouser/Newark listings, search 2026-07-10. [3] `hsx_2026_v2.net` lines 597–671 (J1 `comp`
block: value `Conn_01x09_Socket`, footprint `D09S33E6GX00LF:AMPHENOL_D09S33E6GX00LF`).

---

## 2. Full signal-path trace (net-by-net)

### 2a. Mux/chopper channel-assignment logic (the part that actually determines correctness)

The ADG1209 (U1, U2) is a 4:1 **differential** mux: address bits A1 (MSB) and A0 (LSB) select
one of 4 switch-pairs onto common output DA/DB; **EN=0 forces all switches off (Hi-Z)**, and
A1=0/A0={0,1} select switch-pair {1,2}, A1=1/A0={0,1} select switch-pair {3,4} [4]. Reading the
netlist's node lists for each of the four plate nets:

| Net (plate) | J1 pin | U1 (bias mux) nodes tied here | U2 (sense mux) nodes tied here |
|---|---|---|---|
| `/pin1` (p1) | 1 | S1A(4), S2A(5) | S3B(11), S4A(7) |
| `/pin2` (p2) | 6 | S3A(6), S4A(7) | S2B(12), S1A(4) |
| `/pin3` (p3) | 2 | S2B(12), S1B(13) | S4B(10), S3A(6) |
| `/pin4` (p4) | 7 | S4B(10), S3B(11) | S1B(13), S2A(5) |

Consequence for **U1 (bias)**: channel-1 and channel-2 (A1=0) are wired **identically** —
both connect DA→p1, DB→p3. Channel-3 and channel-4 (A1=1) are also wired identically — both
connect DA→p2, DB→p4. **So for U1, a0 has no electrical effect; only a1 matters**, and it
toggles the bias diagonal between (p1,p3) and (p2,p4).

Consequence for **U2 (sense)**: channel-1=(DA=p2,DB=p4), channel-2=(DA=p4,DB=p2) — a
**polarity-swapped repeat** of channel 1, not identical. Channel-3=(DA=p3,DB=p1),
channel-4=(DA=p1,DB=p3) — likewise polarity-swapped. **So for U2, a1 selects the sense
diagonal (always the diagonal orthogonal to whatever U1 is biasing) and a0 swaps sense
polarity.**

This exactly reproduces `SPECS.md`'s stated phase-table intent — *"Plate offset cancels
across a1 pairs, amplifier offset across a0 pairs, and the a2 (chopper) reversal removes
second-order residuals"* — **without needing to trust that prose**: a1 is confirmed (by the
netlist's own wiring, independent of the phase-table doc) to be the bit that moves the bias/
sense role between the two orthogonal diagonals, and a0 is confirmed to be a pure sense-side
polarity flip with zero effect on the bias side. **PASS — this is a non-trivial, previously
undocumented cross-check and it comes out correct.**

**U3 (ADG5236 chopper)** — pin function labels in the netlist (IN1@1, S1A@2, D1@3, S1B@4,
VSS@5, GND@6, NC@7/8, IN2@9, S2A@10, D2@11, S2B@12, VDD@13, NC@14/15/16) **match the ADG5236
TSSOP-16 pinout exactly**, pin-for-pin, against the Analog Devices datasheet [5]. Both control
inputs IN1 and IN2 are tied to the same net `/a2`, so both SPDT switches move together. The
throw wiring is cross-complementary: S1A and S2B are tied together (net `/ibout`), S1A and
S2A are on *different* physical nets (`/ibout` vs `/ibin`) even though both are "A" throws —
so toggling a2 always lands D1/D2 on **opposite** nodes of the (ibin, ibout) pair, i.e. it is
a true bias-polarity flip and **can never short ibin to ibout** through the chopper.
**PASS.**

**AD8429 (U4)** pin roles from the netlist (−IN@1, RG@2, RG@3, +IN@4, −VS@5, REF@6, OUT@7,
+VS@8) match the ADI datasheet pin table exactly [6]. REF (pin 6) is tied to GND1 — correct,
sets output common-mode reference. R1 bridges RG(2)–RG(3), setting gain (value/verification is
ST1's scope; connectivity here is correct). **PASS.**

### 2b. End-to-end path (bias source → output)

```
J2.1 ∥ J7.1 → R9(100Ω, sense) → node "ibin" → U3 S1B/S2A
J2.2 ∥ J7.2 → R10(100Ω, sense) → node "ibout" → U3 S1A/S2B
U3 D1/D2 (chopped, polarity set by a2) → U1 DA/DB (/ib_p, /ib_n)
U1 (channel set by a1; a0 don't-care) → J1 plate diagonal (p1,p3) or (p2,p4)
   [orthogonal diagonal] → U2 (channel set by a1+a0) → U2 DA/DB (/in+, /in-)
U2 DA/DB → U4 (AD8429) +IN/−IN, with R2/R3 (2.2 kΩ each) → GND1 as bias-return
U4 OUT (pin 7) → R4 (10 kΩ, to GND1) ∥ J4.1 (SMA center) → scope
J4.2, J4.3 (SMA shield) → GND1
```

All of the above is directly read from netlist nodes; **PASS** end-to-end, no missing links,
no unexpected node merges.

### 2c. Pass/flag table — every net

| Net | Members | Function | Verdict |
|---|---|---|---|
| `+15V` | C2,C5,C6,C7(→GND1), U1.14, U2.14, U3.13, U4.8, U5.6 | Positive rail, 4× decoupling caps, one per IC | PASS |
| `-15V` | C1,C3,C4,C8(→GND1), U1.3, U2.3, U3.5, U4.5, U5.8 | Negative rail, symmetric decoupling | PASS |
| `+36V` | C9,C10(→GND), J5.1, J6.1, U5.2(+VIN) | Raw DC input to the isolated DC/DC | **FLAG (naming)** — see §4 |
| `GND` | C9,C10, J5.2, J6.2, U5.1(−VIN) | DC/DC **primary-side** return | PASS (intentionally separate from GND1 — isolated converter) |
| `GND1` | C1–C8, J4.2/3, R2.1, R3.2, R4.1, R5–R8.1, U1.15, U2.15, U3.6, U4.6(REF), U5.7(COM) | **Secondary-side / analog** ground, everything downstream of the DC/DC bonds here | PASS |
| `/a0` | J3.3, R6.2(pulldown), TP3, U1.1, U2.1 | Shared address bit 0 → both muxes only | PASS |
| `/a1` | J3.2, R7.2(pulldown), TP2, U1.16, U2.16 | Shared address bit 1 → both muxes only | PASS |
| `/a2` | J3.1, R5.2(pulldown), TP1, U3.1(IN1), U3.9(IN2) | Chopper polarity bit → both SPDT control inputs | PASS |
| `/en` | J3.4, R8.2(pulldown), TP4, U1.2, U2.2 | Enable, both muxes; **chopper U3 has no EN pin (TSSOP package)** | PASS, see FLAG in §4 (EN=0 opens bias loop) |
| `/ib_p`, `/ib_n` | U1.8/9(DA/DB) ↔ U3.3/11(D1/D2) | Chopper output → bias-mux common port | PASS |
| `/ibin`, `/ibout` | R9.2/TP5/U3.4,10 ; R10.2/TP7/U3.2,12 | Sense-resistor node → chopper throws | PASS, no shorts (§2a) |
| `/in+`, `/in-` | R2.2/U2.8/U4.4 ; R3.1/U2.9/U4.1 | Sense-mux common port → in-amp inputs | PASS |
| `/pin1`–`/pin4` | J1.1/6/2/7 ↔ U1,U2 switch throws | Plate connections, diagonal-correct (§2a) | PASS |
| `Net-(J2-Pin_1/2)` | J2, J7, R9/R10.1, TP6/TP8 | External bias loop in, J2∥J7 redundant access points | PASS (redundant by design, not a defect) |
| `Net-(J4-Pin_1)` | J4.1, R4.2, U4.7(OUT) | Output node | PASS |
| `Net-(R1-Pad1/2)` | R1, U4.2/3(RG) | Gain-set resistor | PASS |
| `unconnected-(J1-Pin_3/4/5/8/9)` | J1 only | Spare sensor-connector pins | PASS (matches HARDWARE_DATA) |
| `unconnected-(U3-NC-Pad7/8/14/15/16)` | U3 only | Manufacturer NC pins (confirmed against ADG5236 datasheet pin table [5]) | PASS |
| `unconnected-(U5-CTRL-Pad3)` | U5 only | RS6-2415D remote on/off, left floating | Engineering judgment — flag for ST1 (confirm floating = enabled per RECOM datasheet); not a wiring defect |
| `unconnected-(U5-NC-Pad5)` | U5 only | Manufacturer NC pin | PASS |

No net was found connected to only a single *functional* pin (the "unconnected-(...)" nets above
are all deliberate spares/NC, matching either HARDWARE_DATA or the manufacturer pinout) and no
two nets that should be isolated were found merged.

---

## 3. Integration items (per MISSION_BRIEF §3)

| Item | Netlist finding | Verdict |
|---|---|---|
| EN pulldown on J3.4 | R8 (0805) ties net `/en` (=J3.4) to GND1. Confirmed. | PASS |
| J3 has no ground pin | J3 is a 1×04 header; its 4 pins are fully consumed by a2/a1/a0/en (pins 1–4 respectively, matching HARDWARE_DATA's J3 map exactly). No 5th position exists on the physical part for a ground pin. | PASS — confirms HARDWARE_DATA's caution that logic ground must be bonded to GND1 by a separate external wire (Pico GND → GND1, per HARDWARE_DATA §3); this bond is **external to the board schematic** and cannot be checked from the netlist — it is an assembly/integration step that must be verified physically (recommend ST6/bring-up continuity step). |
| R9 = R10 = 100 Ω in the bias loop | Confirmed in series with the external bias loop, feeding the chopper throws (§2b). Values (100 Ω) are asserted in HARDWARE_DATA as DMM-confirmed as-built; the netlist's generic `R` symbols carry no engineering value field, so the 100 Ω figure itself is **not independently re-derivable from the netlist** — this is expected (KiCad passive symbols here don't carry annotated values) and is not a discrepancy. | PASS (connectivity); value trust deferred to HARDWARE_DATA/DMM per pack convention |
| 2.2 kΩ returns (R2, R3) | Confirmed: R2 from `/in+` to GND1, R3 from `/in-` to GND1 — correct bias-return topology for the in-amp inputs. | PASS |

---

## 4. Flags and recommendations

| # | Flag | Severity | Detail | Recommendation |
|---|---|---|---|---|
| F1 | Net name `+36V` vs documented 24 V nominal input | Low (cosmetic/documentation) | The raw input rail feeding U5's +VIN (via J5/J6) is schematic-labeled `+36V`, but HARDWARE_DATA/SPECS state the input is "24 V" on J5. Wiring itself is correct (J5.1/J6.1 → U5.2, unambiguous); this is a **net-label**, not a connectivity, issue. RS6-2415D "24" nominally denotes a 24 V-input family, which for RECOM RS6 modules typically tolerates a wide input range (commonly quoted up to ~36 V max on some 24 V-nominal iso-DC/DC families) — that is likely the origin of the label, but it should be confirmed against the RS6-2415D datasheet (ST1 scope) and the net renamed to something like `+24V_IN` or `+VIN_RAW` to avoid a future engineer assuming 36 V is the intended operating input. | Rename net for clarity; cross-check actual RS6-2415D input voltage rating in ST1. Failure mode if ignored: none electrical (label doesn't affect fab/assembly), but risks a future engineer mis-specifying the external 24 V supply as 36 V. |
| F2 | Bias mux opens when EN = 0 | Low–Medium (operational, not wiring) | U1/U2 go full Hi-Z when EN=0 (ADG1209 truth table [4]). Because U1's DA/DB feed straight back to the chopper and then to the external 100 µA current-source loop (via R9/R10/J2/J7), driving EN low (the board's documented "dead"/default-safe state, per the R8 pulldown) **opens the bias-current path**. If the external current source is a true constant-current source without open-circuit protection, this can force its compliance voltage to the rail while EN=0 (e.g., at power-up before the Pico drives EN high, or if EN is dropped mid-run). This is a function of how the external 100 µA source is built, not of this board, but it is exactly the kind of "net doesn't land where function requires" case the review is meant to catch. | Confirm the external current source (existing bench emulator / eventual per-channel floating 100 µA source, per REFERENCE_DATA §D) tolerates or clamps an open-circuit/high-compliance condition, or add a bleed resistor across the loop input if not. Failure mode if ignored: current-source output could rail or degrade during EN=0 dwell (power-up sequencing, fault states). |
| F3 | J1 footprint pad geometry not independently verifiable from this pack | Low (verification gap, not a found defect) | Only the `.net`/BOM were supplied; the referenced footprint library `D09S33E6GX00LF:AMPHENOL_D09S33E6GX00LF` (a custom, MPN-named footprint — a good sign) could not be opened to confirm pad-1-to-physical-pin-1 correspondence. | Do a first-article continuity check: with the harness disconnected, verify each `/pin1`–`/pin4` schematic net actually appears on the *correct physical* J1 pin (1, 6, 2, 7) with an ohmmeter before mating the sensor harness. This is naturally covered by ST6's pre-power continuity/insulation procedure — cross-reference it there explicitly. |
| F4 | v1→v2 regression check has no v1 netlist to diff against | Low (documentation gap) | No `v1` KiCad project/netlist file exists anywhere in this pack (checked). The "topologically identical to v1 except J1 changed" claim and the "pin convention preserved from v1" claim (HARDWARE_DATA, REFERENCE_DATA §B) are **asserted**, not independently diffed here. | If a v1 netlist/schematic still exists in the KiCad project history or a prior export, diff it against v2 as a cheap confirmation. Given the datasheet-confirmed gender/pinout of the new Amphenol part and the fully self-consistent v2 wiring found above, risk is judged low, but this is the one regression claim taken on faith rather than verified by diff. |
| F5 | U5 CTRL pin (RS6-2415D remote on/off) left floating | Low (adjacent to ST1) | Net `unconnected-(U5-CTRL-Pad3)` — CTRL is not tied to GND or VIN. Most RECOM CTRL pins default to "on" when floating, but this should be confirmed against the RS6-2415D datasheet rather than assumed. | Cross-reference with ST1's RS6-2415D datasheet pull; not a wiring defect, just an unconfirmed default-state assumption. |

## 5. Discrepancies: netlist vs. HARDWARE_DATA

None found in pin mapping, connector roles, or the locked design facts (§1–§3 of
HARDWARE_DATA). The only discrepancy is the cosmetic net-name issue (F1, `+36V` label vs. 24 V
documented input) — this is a labeling mismatch inside the schematic/HARDWARE_DATA pairing, not
a netlist-vs-HARDWARE_DATA contradiction about what's *connected*.

## 6. Did the v1→v2 connector swap introduce any regression?

**No regression found**, with the caveat in F4 (no v1 file to diff directly). Specifically:

- **Gender**: confirmed female socket (receptacle) via Digi-Key spec table and the Amphenol
  part-number pattern — matches the schematic symbol `Conn_01x09_Socket` and the documented
  intent (a socket connector on the board mates to a plug on the sensor harness). No gender
  flip.
- **Pin numbering**: standard DE-9 numbering (9 pins, 5-4 rows); netlist's pin-to-plate mapping
  (pin1=p1, pin6=p2, pin2=p3, pin7=p4) matches HARDWARE_DATA §3 exactly and is internally
  self-consistent with the mux/chopper trace (§2a) — i.e., the *board's own logic* only makes
  sense if this mapping is right, and it is right.
- **Mount style**: right-angle THT PCB mount — a mechanical/footprint concern, not a pinout
  regression; footprint name (`D09S33E6GX00LF:AMPHENOL_D09S33E6GX00LF`) is specific to this
  exact MPN, not a generic substitute, reducing (but per F3, not eliminating) the risk of a
  silent footprint mismatch.
- **Solder-cup mirror trap**: does not apply to J1 itself (PCB right-angle receptacle, not a
  solder-cup part); it is relevant to the *mating cable connector* on the harness side and
  should be carried forward as an explicit caution into ST6's harness/continuity procedure.
- **Twisted-pair harness convention**: (1,2)=p1&p3, (6,7)=p2&p4 remains electrically valid post-
  swap because each such pair always carries one complete bias/sense diagonal current loop, per
  the mux trace in §2a — the convention wasn't broken by changing which physical part sits at
  J1.

---

## Assumptions made

- Treated the Digi-Key vendor product page as an acceptable primary source for J1's gender/
  mechanical facts per `SOURCE_STANDARDS.md` §1, since direct fetches to Amphenol-hosted URLs
  (product page and datasheet PDF) returned HTTP 403 in this environment after repeated
  attempts.
- Assumed the ADG1209/ADG5236/AD8429 pin-function labels embedded in the netlist's own
  `pinfunction` fields (auto-generated by KiCad from the schematic symbol) are trustworthy
  enough to trace logic *within* this review, but cross-checked them against the actual
  manufacturer datasheets anyway (§2a) rather than taking them on faith — all matched exactly.
- Did not attempt to verify RS6-2415D input voltage range or CTRL pin default behavior
  (F1, F5) — flagged as adjacent to ST1 (component-spec verification), not re-derived here to
  stay in ST2's connection-correctness scope.
- No v1 netlist exists in this pack to diff (confirmed via filesystem search); the v1→v2
  regression verdict (§6) is therefore based on datasheet verification of the v2 part plus
  internal self-consistency of the v2 design, not a literal diff (flagged as F4).

## UNVERIFIED items

- **J1 footprint pad-level geometry** (pad-1-to-physical-pin-1 correspondence inside the
  `.kicad_mod` file) — the footprint file itself was not included in this review pack (F3).
- **Amphenol manufacturer-hosted datasheet/product page** — direct fetch blocked (HTTP 403);
  relied on Digi-Key's vendor page instead (itself an accepted primary source per this pack's
  rules).
- **RS6-2415D actual input voltage range** and **CTRL-pin floating default** (F1, F5) — left to
  ST1.

---

## Sources

1. Digi-Key, D09S33E6GX00LF product page (Amphenol ICC/FCI) —
   https://www.digikey.com/en/products/detail/amphenol-cs-fci/D09S33E6GX00LF/1539664
   (fetched 2026-07-10).
2. Amphenol/FCI D-Sub part-number family cross-reference (D09P33E6GX00LF plug counterpart,
   etc.) — Digi-Key/Mouser/Newark listings (search, 2026-07-10); Amphenol D-Subminiature
   catalog (fetch of the hosted PDF returned HTTP 403 from this environment) —
   https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/datasheet/inputoutput/io_dsub_brochure.pdf
3. `01_MISSION/REFERENCE/hsx_2026_v2.net` (live KiCad netlist, this project) — all pin/net
   citations in this document are to this file.
4. Analog Devices, ADG1208/ADG1209 datasheet (4-/8-channel iCMOS multiplexers), truth table —
   https://www.analog.com/media/en/technical-documentation/data-sheets/adg1208_1209.pdf
5. Analog Devices, ADG5236 datasheet (dual SPDT, latch-up-proof), TSSOP-16 pin table —
   https://www.analog.com/media/en/technical-documentation/data-sheets/adg5236.pdf
6. Analog Devices, AD8429 datasheet, 8-pin pin configuration —
   https://www.analog.com/media/en/technical-documentation/data-sheets/ad8429.pdf
7. `01_MISSION/HARDWARE_DATA.md` §1/§3 (authoritative design facts, this pack).
8. `01_MISSION/REFERENCE/SPECS.md` and `01_MISSION/REFERENCE/PACKAGING_LCC02046.md` (used to
   resolve the "opposite plate pairs (p1,p2)/(p3,p4)" vs. "diagonal bias/sense pairs p1-p3/
   p2-p4" terminology — PACKAGING_LCC02046.md §B explicitly states the die's opposite
   (N/S or E/W) contact pairs are (p1,p2) and (p3,p4), while the bias/sense *current-path*
   diagonals are p1-p3 and p2-p4, which is what the mux trace in §2a of this document confirms
   is actually wired).
