# ST5 — Vacuum feedthrough / flange selection (Q5)

**Date:** 2026-07-10 · **Status:** DECISION_GATE (spends money, changes mechanical fit)
**Scope:** replace the Accu-Glass 9D-275 (9-pin, 2.75″ CF) with a ≥12-conductor feedthrough at
≥ baseline ratings (500 VDC, 5 A/pin, ≤1×10⁻¹⁰ Torr, −200…250 °C), compatible with the
Ø31.75 × 27.5 mm probe-head envelope sitting on the vacuum side of this flange.

---

## BLUF — UPDATED 2026-07-10 (post-run addendum, see §9)

| | Pick | Why in one line |
|---|---|---|
| **Primary (revised)** | **Accu-Glass 19C-275, P/N 110210** — 19-pin **MIL-C-26482 circular**, **single connector**, on **2.75″ CF**, $434.00 [19C-275 page] | **Strictly dominates the prior pick**: same 2.75″ CF port (zero HSX mechanical change), same 1.45″ bore, same 500 VDC/5 A/pin/−200…250 °C/1×10⁻¹⁰ Torr ratings, **one shell instead of two** (mis-mate risk = zero by construction, not by procedure), **7 spare pins** (vs 6), and **$427 cheaper system cost** (§4a). Two items remain UNVERIFIED (contact AWG, single-shell protrusion height, §7) — same class of gap the prior pick carried, not a new risk. |
| **Alternate (2.75″, prior primary)** | **Accu-Glass 9C2-275, P/N 100012** — 18-pin (2 × 9-pin Sub-C) on **2.75″ CF**, $685.00 [9C2-275 page] | Falls back to this **only if** the 19C-275's contact size can't take the harness gauge, or its protrusion height is confirmed *worse* than the dual Sub-C towers. Carries known mis-mate risk (mitigated procedurally in `WIRING_PLAN.md`) that the 19C-275 removes structurally. |
| **Runner-up (4.5″ path)** | **Accu-Glass 15D-450, P/N 100210** — 15-pin Sub-D on **4.5″ CF**, $464.00 [15D-450 page] | Single connector, cheapest parts list (~$950), pre-terminated UHV ribbon available — **but requires a 4.5″ CF port** (2.75″→4.5″ change). For **+$32**, the **25D-450 (100220, $496)** gives 13 spare pins for guard/shield — the better 4.5″ choice if the port change happens anyway. |
| **Flip condition** | 19C-275 → 9C2-275 if the 19C contact/AWG or protrusion check fails (§7/§9). Either 2.75″ pick → **15D-450/25D-450** if UW-Madison confirms the port is (or can be) **4.5″ CF**. |
| **Hard dependency** | **UW-Madison must confirm the HSX port CF size** before purchase. Everything below branches on it. **New dependency (§9): Accu-Glass must confirm 19C-275 contact wire-gauge capacity and single-shell protrusion height** before it can clear the primary slot outright. |

There is **no Sub-D option ≥12 pins on 2.75″ CF**: `…/cf-feedthroughs/15d-275` returns HTTP 404, and the Sub-D family offers "9, 15, 25, or 50-pin" with 15+ pins only on 4.5″ CF [Sub-D landing page; family search]. The Sub-D path to 2.75″ CF does not exist. Originally the 2.75″-CF path was thought to exist only via the **Sub-C (circular) family** (9C2-275) — **§9 found a third family, MIL-C-26482 (circular, bayonet-style), that also offers 2.75″ CF and beats it on cost, pin count, and mis-mate risk.**

---

## 1. Candidate comparison — all ratings (fetched 2026-07-10; 19C-275 added 2026-07-10 in §9)

| Spec | 9D-275 (baseline) | **19C-275** | 9C2-275 | **15D-450** | 25D-450 | 15D2-450 | 25D-15D-450 | 25D2-450 |
|---|---|---|---|---|---|---|---|---|
| Accu-Glass P/N | 100200 | **110210** | 100012 | **100210** | 100220 | 100212 | 100226 | 100225 |
| Connector family | Sub-D | **MIL-C-26482 (circular)** | Sub-C (circular) | Sub-D | Sub-D | Sub-D | Sub-D | Sub-D |
| Pins (connectors) | 9 (1) | **19 (1)** | 18 (2×9) | **15 (1)** | 25 (1) | 30 (2×15) | 40 (25+15) | 50 (2×25) |
| **CF flange** | **2.75″** | **2.75″** (1.45″ ID) | **2.75″** (1.45″ ID noted) | 4.5″ | 4.5″ | 4.5″ | 4.5″ | 4.5″ |
| Voltage | 500 VDC [9D-275 page] | **500 VDC** [MIL-C-26482 family page] | Product page: not stated → **500 VDC per Sub-C family page** | Product page: not stated → **500 VDC per Sub-D family page** | not stated → 500 VDC (family) | not stated → 500 VDC (family) | not stated → 500 VDC (family) | not stated → 500 VDC (family) |
| Current | 5 A/pin, max 20 % of pins simult. | **5 A/pin, max 20 % simult.** [family page] | 5 A (family: 5 A max) | 5 A/pin, max 20 % simult. | 5 A/pin, max 20 % simult. | 5 A/pin, max 20 % simult. | "5 AMP" | 5 A/pin, max 20 % simult. |
| Temp range / bake | −200…250 °C / 250 °C | **−200…250 °C / 250 °C** | −200…250 °C / 250 °C | −200…250 °C / 250 °C | −200…250 °C / 250 °C | −200…250 °C / 250 °C | −200…250 °C / 250 °C | −200…250 °C / 250 °C |
| Vacuum | 1×10⁻¹⁰ Torr | **1×10⁻¹⁰ Torr** | 1×10⁻¹⁰ Torr | 1×10⁻¹⁰ Torr | 1×10⁻¹⁰ Torr | 1×10⁻¹⁰ Torr | 1×10⁻¹⁰ Torr | 1×10⁻¹⁰ Torr |
| Materials / contacts | SS, glass-ceramic / Ni-Fe Au-plt | **SS, glass-ceramic / Ni-Fe Au-plt** | SS, glass-ceramic / Au-plt pins | SS, glass-ceramic / Ni-Fe Au-plt | SS, glass-ceramic / Ni-Fe Au-plt | SS, glass-ceramic / Ni-Fe Au-plt | SS, glass-ceramic / Ni-Fe Au-plt | SS, glass-ceramic / Ni-Fe Au-plt |
| Gender | Male/Male (straight-through) | **Male/Male** | Male/Male | Male/Male | Male/Male | Male/Male | Male/Male | Male/Male |
| **Price** | $329.00 | **$434.00** | $685.00 | **$464.00** | $496.00 | $950.00 | $1,126.00 | $967.00 |
| Meets 12-signal need | NO (9 < 12) | **YES, +7 spare** | YES, +6 spare | YES, +3 spare | YES, +13 spare | YES (overkill) | YES (overkill) | YES (overkill) |
| Port change needed | — | **NO** | **NO** | **YES 2.75″→4.5″** | YES | YES | YES | YES |
| Connectors on shell | 1 | **1 (zero mis-mate risk)** | 2 (A/B swap risk) | 1 | 1 | 2 | 2 | 2 |
| Stock / lead time | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED | not listed — UNVERIFIED |
| Orderable (live page w/ price) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

All URLs in the Sources block. Every candidate **meets or exceeds every baseline rating**; the
only differentiators are pin count, connector count/style, CF size, and price. The 19C-275 is
the only candidate that is simultaneously single-connector *and* 2.75″ CF.

**Electrical headroom sanity (one-line calc):** worst-case conductor load = the 100 µA bias
pair → margin vs 5 A/pin = 5 / 1×10⁻⁴ = **50,000×**; vs the weakest mating element (2 A on the
Sub-C UHV cable assemblies [100040/100110 pages]) still **20,000×**. Voltage: signals are
±15 V-rail-bounded ≪ 500 VDC. Ratings are a non-issue at this operating point; the decision is
purely mechanical/handling. (Verified from vendor pages; margin arithmetic = engineering judgment.)

---

## 2. Single high-count feedthrough vs per-sensor grouping

Context that constrains the trade: **the probe head mounts on the vacuum side of this same
flange** (PACKAGING_3D_ENVELOPE §B — "the head sits on it via a stand; harness routes from the
carriers down to the feedthrough pins"). Therefore **splitting the 12 conductors across two
separate flanges/ports is infeasible** — one probe head, one flange. "Grouping" can only mean
*multiple connectors on one flange* (9C2-275, 15D2-450, …), not multiple 9D-275s on different
HSX ports. (Keeping the existing 9D-275 and adding a second one elsewhere is therefore
**rejected**: it would force an in-vessel harness run across the vessel from the probe head to a
second port — maximal chafing/short exposure in the hot zone, the user's #1 worry.)

| Criterion (weight) | (a) Single high-count connector (15D-450 / 25D-450) | (b) Dual-connector on one flange (9C2-275 / 15D2-450) |
|---|---|---|
| **Mis-mate risk** (high — user's #1 worry) | **Zero** — one plug, one socket, can't be crossed | Two identical connectors per side → A↔B swap is physically possible. Mitigable (ST6): permanent labels, different harness lengths, and a pin assignment where a swap fails safe + pre-power continuity check |
| **Pin-to-pin short concentration** (high) | All 12+ signals in one shell — one bent pin or one conductive sliver can bridge any two circuits; one connector fault takes down all 3 axes | Fault contained to one connector = at most 2 of 3 sensors lost (if grouped per-sensor); 9 pins/shell = fewer adjacent-pin combinations per shell |
| **Signal grouping / crosstalk** (med) | Pairs separated by assignment + 3–13 grounded spare pins as guards (25D-450 best here) | **Physical separation**: bias/sense groups of different sensors in different shells; inter-sensor coupling across shells ≈ nil |
| **CF port impact** (high) | **4.5″ CF required** — port change | **9C2-275: none (2.75″)**; 15D2-450: 4.5″ |
| **Harness build** (med) | One vacuum-side 15/25-way assembly, one air-side cable → fan-out to 3 DSUB-9s | Two 9-way assemblies per side → fan-in to 3 DSUB-9s; slightly more connectorization labor |
| **Cost (system, §4)** (low) | ~$952 (15D) / ~$1,070 (25D) + port-change hardware + UW labor | ~$1,479 (9C2), **no port hardware, no UW machine/vessel work** |

**Verdict (engineering judgment) — SUPERSEDED 2026-07-10, see §9:** this section was written
before the 19C-275 was found and only weighed single-vs-dual connector *within* the options then
known (9C2-275 dual-Sub-C vs 4.5″ single-Sub-D). It no longer reflects the recommended pick.
The 19C-275 removes the tradeoff entirely: it is single-connector (mis-mate risk zero by
construction, no anti-swap keying/labeling needed) **and** stays on the 2.75″ port. The
fault-containment argument for the 9C2-275's dual shells (§ above) is real but is bought at the
cost of *introducing* a swap risk that a single shell never has — a single 19-pin shell fails
closed (any short is contained to the 12 signal + 7 spare pins already in one connector; there
is no second shell for A↔B confusion to trade against). 9C2-275 remains the fallback if the
19C-275 fails its contact-gauge or protrusion check (§7).

**Recommended pin grouping for the 9C2-275 (handoff to ST6):**

| Connector | Pins 1–4 | Pins 5–8 | Pin 9 |
|---|---|---|---|
| A | Sensor X bias pair + sense pair | Sensor Y bias pair + sense pair | Shield/drain (chassis-adjacent return) |
| B | Sensor Z bias pair + sense pair | Returns/guards (grounded spares between groups) | Shield/drain |

A↔B swap with this map puts sensor-Z lines onto X/Y positions — wrong data, but **no
bias-into-sense hard fault** if ST6 mirrors the pair ordering; final map is ST6's to fix with
the FMEA. (Judgment, not vendor data.)

---

## 3. The CF-size change 2.75″ → 4.5″ — mechanical consequences (flag to UW)

- **Different port, not an adapter ring:** a 4.5″ CF flange cannot bolt to a 2.75″ CF port.
  Standard CF geometry: 2.75″ CF = 6-bolt, 4.5″ CF = 8-bolt, larger OD/bolt circle/gasket
  (200810 gasket, $77 [15D-450 page] vs 200760, $47 for 2.75″ [9C2-275 page]). *(Standard CF
  facts — engineering knowledge, not from the fetched pages.)*
- **The only 2.75″-port workaround is a conical reducer/expander nipple** (Accu-Glass markets
  exactly this use: "fitting a 50-pin 4.50-inch CF flange mounted feedthrough using a 2.75-inch
  CF chamber port" [Accu-Glass site text via search]). **Recommend against it here:** the probe
  head is mounted on the feedthrough's vacuum face, so a reducer would **recess the sensors away
  from the port plane by the reducer length**, changing the measurement location and invalidating
  the Ø31.75 × 27.5 mm envelope assumption derived from the current mounting.
- **Envelope note:** the Ø31.75 mm (1.25″) head envelope passes through the 9C2-275's stated
  1.45″ (36.8 mm) ID [9C2-275 page via search] — consistent with the head being inserted through
  the existing 2.75″ port. A 4.5″ port would relax this, but the envelope is a locked constraint
  regardless.
- **Action for UW-Madison (DECISION_GATE):** confirm (i) the CF size of the probe port actually
  assigned for the 2026–27 campaign, (ii) whether a 4.5″ CF port at an equivalent location is
  available, (iii) allowed vacuum-side protrusion above the flange face, (iv) bakeout temperature
  and whether air-side cabling can be removed during bake (the air-side Delrin/PVC assemblies are
  80 °C max [100020 page] — they must be unplugged for any bake; all vacuum-side parts are
  250 °C).

---

## 4. Accessories — matching mating connectors & cables (all Accu-Glass, live pages)

### 4a. Primary path (revised 2026-07-10): 19C-275 (2.75″ CF, 1 × 19-pin MIL-C-26482)

| Item | P/N | Price | Notes |
|---|---|---|---|
| Feedthrough, 19-pin MIL-C-26482 circular, 2.75″ CF | **110210** | $434.00 | Male/male, straight-through, 19 gold-plated Ni-Fe pins [19C-275 page] |
| **Vacuum side:** 19-way female PEEK connector + Kapton ribbon cable, pre-terminated | **110230** | $398.00 | 19″ or 39″, cut to length at the head [19C-275 page] |
| (alt. vacuum side, bare) 19-pin female PEEK connector | 110240 | $229.00 | Contacts likely separate — confirm before ordering [19C-275 page] |
| **Air side:** 19-way shielded cable assembly, Circular Air Side | **110232** | $220.00 | 48″ or 96″ [19C-275 page] |
| (alt. air side, DIY) Air Service Connector, 19-pin straight shell | 110234 | $96.00 | [19C-275 page] |
| Cu gaskets, 2.75″ CF | 200760 | $47.00 | Same P/N as 9C2-275/9D-275 (same 1.45″ ID bore) [19C-275 page] |
| 2.75″ CF fastener kit | 200764 | $46.00 | Same P/N as 9C2-275 [family precedent] |

**System cost (primary, revised):** 434 + 398 + 220 + 47 + 46 ≈ **$1,145** (no HSX port work) —
**$427 cheaper** than the prior 9C2-275 system (§4b) and no A/B keying/labeling hardware needed.

**Open before PO (§7):** contact wire-gauge capacity (AWG) not stated on any fetched page —
confirm the 110230/110240 contacts accept the harness's planned 24–26 AWG before committing;
single-shell protrusion height above the flange face is also UNVERIFIED (likely *less* than the
9C2-275's dual-tower stack since there is only one shell, but not confirmed).

### 4b. Alternate 2.75″ path (prior primary): 9C2-275 (2.75″ CF, 2 × 9-pin Sub-C)

| Item | P/N | Price | Notes |
|---|---|---|---|
| Feedthrough, 18-pin (2×9) Sub-C, 2.75″ CF | **100012** | $685.00 | Male/male, straight-through [9C2-275 page] |
| **Vacuum side:** 9-pin female PEEK connector + Kapton round-wire assembly, pre-terminated, 19″ or 39″ | **100040** ×2 | $243.00 ea | 250 °C, 1×10⁻¹⁰ Torr, 2 A; **cut to length** for the short head-to-pins run — avoids the $1,074 crimp tool [100040 page] |
| (alt. vacuum side) 9-way Kapton **ribbon** + PEEK connector, 19″/39″ | 100110 ×2 | $265.00 ea | Same ratings; ribbon dresses flatter under the head [100110 page] |
| (alt. vacuum side, DIY) bare 9-pin female PEEK connector | 100150 | $162.00 | Contacts NOT included [100150 page] |
| … female crimp contacts, T1, 20–24 AWG | 100180 | $34.00 | 10-pack [100150 page] |
| … high-duty-cycle female contacts | 110908 | $50.00 | For repeated mate/demate [100150 page] |
| … **crimp tool for T1 contacts** | 100190 | **$1,074.00** | **Avoid** by buying 100040/100110 pre-terminated [100150 page] |
| **Air side:** 9-lead shielded cable assembly w/ Delrin female Sub-C connector, 48″ | **100020** (AIR-CP9-48SC) ×2 | $154.00 ea | 9 × 24 AWG, **Al/Mylar foil + drain wire** (good for ST6's shield plan), 4 A, **80 °C max — remove during bake** [100020 page; construction via search] |
| (air side, 96″) | 100021 (AIR-CP9-96SC) | UNVERIFIED price | Same construction [search] |
| (air side, DIY) Delrin female connector | 100160 | UNVERIFIED price | Contacts sold separately [9C2-275/search] |
| Cu gaskets, 2.75″ CF | 200760 | $47.00 | [9C2-275 page] |
| 2.75″ CF fastener kit | 200764 | $46.00 | [9C2-275 page] |

**System cost (primary):** 685 + 2×243 + 2×154 + 47 + 46 ≈ **$1,572** (no HSX port work).

### 4c. Runner-up path (4.5″): 15D-450 (4.5″ CF, 1 × 15-pin Sub-D)

| Item | P/N | Price | Notes |
|---|---|---|---|
| Feedthrough, 15-pin Sub-D, 4.5″ CF | **100210** | $464.00 | [15D-450 page] |
| **Vacuum side:** 15-way female Kapton ribbon cable + PEEK connector | **100350** | $351.00 | Cut to length at the head [15D-450 page] |
| (alt.) 15D female UHV PEEK connector, bare | 100450 | $208.00 | [15D-450 page] |
| **Air side:** air-service cable assembly, 15D | **101050** | $60.00 | [15D-450 page] |
| (alt.) air-service female connector, 15D | 103110 | $17.00 | [15D-450 page] |
| (alt.) HV female connector, 15D | 110003 | $92.00 | [15D-450 page] |
| 15-way extension cable (both ends terminated) | 100890 | $607.00 | If a long air run is wanted [15D-450 page] |
| Cu gaskets, 4.5″ CF | 200810 | $77.00 | [15D-450 page] |

**System cost (runner-up):** 464 + 351 + 60 + 77 ≈ **$952** + 4.5″ port hardware + UW port work.

### 4d. Upgrade within 4.5″ runner-up: 25D-450 (4.5″ CF, 1 × 25-pin Sub-D)

| Item | P/N | Price |
|---|---|---|
| Feedthrough, 25-pin Sub-D, 4.5″ CF | **100220** | $496.00 [25D-450 page] |
| Vacuum side: 25-way female cable assembly | 100370 | $437.00 [25D-450 page] |
| Vacuum side (alt.): 25D female PEEK connector | 100460 | $236.00 [25D-450 page] |
| Air side: air-service cable assembly 25D / connector | 101060 / 103120 | UNVERIFIED / $20.00 [25D-450, 25D2-450 pages] |

+$32 over the 15D-450 buys **13 spare pins** → grounded guard pins between every sensor group
(directly serves the short-circuit/leakage worry). If the port change happens at all, prefer this.

### 4e. Not recommended (verified but rejected)

| Option | P/N | Price | Why rejected |
|---|---|---|---|
| 15D2-450 (30 pins) | 100212 | $950.00 | 4.5″ port change AND dual-connector mis-mate exposure AND 2× the pins needed [15D2-450 page] |
| 25D-15D-450 (40 pins) | 100226 | $1,126.00 | Most expensive; capacity unused [25D-15D-450 page] |
| 25D2-450 (50 pins) | 100225 | $967.00 | Capacity unused; dual-connector [25D2-450 page] |
| 2 × 9D-275 on two ports | 100200 ×2 | $658.00 | Infeasible: one probe head on one flange; cross-vessel in-vessel harness = worst-case chafing/short exposure |
| 4.5″ feedthrough + conical reducer on 2.75″ port | — | — | Recesses the probe head from the port plane; breaks the envelope/measurement-location assumption |
| 9C2-275 as primary (superseded 2026-07-10) | 100012 | $685.00 | Beaten outright by 19C-275 on the same 2.75″ port: $427 more, one fewer spare pin, and carries a structural mis-mate risk the 19C-275 doesn't have. Demoted to alternate (§4b) pending the 19C-275's contact/protrusion check. |

---

## 5. Recommendation block (with failure modes) — REVISED 2026-07-10

| # | Recommendation | Failure mode if wrong |
|---|---|---|
| R0 | **Primary (new):** **Change** flange to **19C-275 (110210)** + 110230 (vacuum) + 110232 (air), **conditional on (a) UW confirming the port is 2.75″ CF and (b) Accu-Glass confirming the 110230/110240 contacts accept 24–26 AWG and the single-shell protrusion height fits the ST8 standoff budget** | If either check fails, we own a $434 feedthrough that can't take the harness gauge or fouls the probe-head stand → fall back to R1 (9C2-275); loss is the $434 + accessories, smaller than an R1-wrong rework since no port work is implicated |
| R1 | **Alternate (2.75″, prior primary):** 9C2-275 (100012) + 2× 100040 (vacuum) + 2× 100020 (air), if R0 fails its contact/protrusion check | Same port-size risk as before, plus the mis-mate exposure R0 was chosen to avoid; if the port is actually larger, a $685 feedthrough under-uses the port → rework ≈ full accessory cost + schedule slip |
| R2 | **Runner-up:** 15D-450 (100210) + 100350 + 101050 if UW offers a 4.5″ CF port; spend +$32 for 25D-450 if guard pins are wanted | If the 4.5″ port never materializes, the part is unusable on the existing port without a reducer that moves the sensors — dead stock + a scramble back to R0/R1 |
| R3 | **Do not** buy the $1,074 Sub-C crimp tool (or any DIY crimp tool); buy pre-terminated assemblies and cut to length | If a lead is cut too short or a re-pin is needed mid-campaign with no tool on hand, a spare pre-terminated assembly is the fix — order **one spare 110230** (or 100040 if on R1) with the initial PO |
| R4 | Air-side cable assemblies are rated 80 °C max and must be **unplugged during any bake**; only PEEK/Kapton parts stay on the flange | Melted air-side connector on the feedthrough pins during a 150–250 °C bake — feedthrough contamination, possible pin damage |
| R5 | **If R0 (19C-275) is adopted, R5 is moot** — single shell has no A/B swap to guard against; `WIRING_PLAN.md`'s anti-swap labeling/keying and swap-tolerant pin map were written for R1 (9C2-275) and are unnecessary complexity under R0, though harmless if kept. **If R1 is adopted** (fallback), ST6's anti-swap labeling + swap-tolerant pin map for the two identical Sub-C connectors still applies | Under R1 only: A↔B swap at power-up cross-connects sensor channels; with a careless pin map it could drive a bias pair into a sense pair |

---

## 6. What UW-Madison / Accu-Glass must confirm (DECISION_GATE inputs — blocking purchase)

1. **UW-Madison — CF size of the assigned probe port** for the 2026–27 vector-probe campaign (is
   the current 9D-275 on a 2.75″ CF port? — assumed yes, A1 below).
2. **Accu-Glass (new, for the 19C-275) — contact wire-gauge capacity** of the 110230/110240
   contacts, and the **single-shell protrusion height** above the flange face (feeds the ST8
   standoff budget the same way the 9C2-275 tower height did).
3. If 2.75″ but the 19C-275 fails check 2: any objection to the **Sub-C (circular) connector
   family** (9C2-275) replacing Sub-D at this port; vacuum-side **protrusion clearance** for two
   connector towers under the probe-head stand.
4. If a **4.5″ CF port** is available at an equivalent measurement location: dimensions,
   orientation, and who does the port work/schedule.
5. **Bakeout plan** (temperature, duration, whether air-side cabling can be removed).
6. Whether the Ø31.75 × 27.5 mm envelope is derived from the port bore (i.e., head inserted
   through the port) — this decides whether a reducer is categorically excluded.

## 7. UNVERIFIED items

| Item | What was needed | Where it should come from |
|---|---|---|
| **19C-275 contact wire-gauge (AWG) rating** | Confirm 110230/110240 contacts accept the planned 24–26 AWG harness | Not on the fetched product/family pages; MIL-C-26482 catalog PDF or Accu-Glass call |
| **19C-275 single-shell protrusion height** above the flange face | Fit-check vs probe-head stand (ST8 standoff budget) | Not on fetched pages; same MIL-C-26482 catalog PDF this run couldn't render, or Accu-Glass call |
| Voltage rating printed on the 9C2-275 / 15D-450 / 25D-450 / 15D2-450 / 25D2-450 **product pages** | Per-product 500 VDC confirmation | Family landing pages state 500 VDC / 5 A for Sub-D, Sub-C, and MIL-C-26482 (19C-275 confirmed at family level); product pages mostly omit it. Confirm on the spec PDF or with Accu-Glass at order time |
| Sub-C connector **protrusion height & tower spacing** on 9C2-275 | Fit-check vs probe-head stand (fallback path only) | `subminiature_c_specifications.pdf` — the PDF would not render in this environment (no PDF text extraction available); must be read before the ST8 stand design freezes if R1 is used |
| Stock / lead time, all P/Ns (both families) | 2026 schedule | Not shown on any fetched page; phone Accu-Glass (661) 607-0250 |
| 100021 (96″ air cable) and 100160 (Delrin connector) prices; 101060 price | Cost roll-up completeness (fallback path) | Pages exist but price not captured |
| Whether 9C2-275's two connectors are factory-marked A/B | ST6 keying plan (fallback path only) | Product page silent — assume unmarked (A2) |

## 8. Assumptions made (per CLAUDE.md rule 5)

- **A1:** The HSX probe port currently carrying the 9D-275 is a **2.75″ CF** and remains the
  assigned port. Basis: baseline part is a 2.75″ CF feedthrough (HARDWARE_DATA §4) and the
  Ø31.75 mm envelope ≈ the 2.75″-CF-class bore. **High confidence, but purchase-blocking — UW
  must confirm.**
- **A2:** The 9C2-275's two connectors are physically identical and unmarked; ST6 must add
  labeling/keying. **Only relevant if R1 (9C2-275) is used instead of R0 (19C-275).**
- **A5 (new, 2026-07-10):** The 19C-275's 110230 pre-terminated vacuum cable and 110240 bare
  connector contacts are assumed to be the same MIL-C-26482 family "circular" pin size used
  across Accu-Glass's 19-pin line, and assumed capable of ≥24 AWG (consistent with the family's
  5 A/pin rating, which requires a contact size larger than typical 26–28 AWG micro-D pins).
  **Medium confidence — purchase-blocking, same tier as A1.** UNVERIFIED until Accu-Glass
  confirms (§7).
- **A3:** Requirement interpreted as 12 signal conductors + ≥3 shield/return conductors
  desirable (REFERENCE_DATA §D contemplated "DB-15 or 2×DSUB-9" — both satisfied here: 15D-450
  is the DB-15 path, 9C2-275 is the 2× 9-way path).
- **A4:** Prices and orderability as displayed 2026-07-10; no stock guarantee.

---

## Sources

- Accu-Glass 9D-275 (100200): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/9d-275
- Accu-Glass Sub-D CF family index: https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs
- Accu-Glass Sub-D landing (family ratings 500 VDC / 5 A / 20 % derating): https://www.accuglassproducts.com/subminiature-d
- Accu-Glass 15D-450 (100210): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d-450
- Accu-Glass 25D-450 (100220): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/25d-450
- Accu-Glass 15D2-450 (100212): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d2-450
- Accu-Glass 25D-15D-450 (100226): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/25d-15d-450
- Accu-Glass 25D2-450 (100225): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/25d2-450
- Accu-Glass 15D-275 (nonexistence check — HTTP 404): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d-275
- Accu-Glass Sub-C CF family (500 VDC / 5 A / −200…250 °C / 1×10⁻¹⁰ Torr): https://www.accuglassproducts.com/subminiature-c/cf-feedthroughs
- Accu-Glass 9C2-275 (100012): https://www.accuglassproducts.com/subminiature-c/cf-feedthroughs/9c2-275
- Accu-Glass 9-pin Sub-C female PEEK connector (100150) + contacts/tool: https://www.accuglassproducts.com/uhv-peek-connector-9c-female
- Accu-Glass 9-pin Sub-C PEEK connector + Kapton round cable (100040): https://www.accuglassproducts.com/subminiature-c/uhv-round-cables/9-pin-female-connector-cable
- Accu-Glass 9-way Kapton ribbon + PEEK C-connector (100110): https://www.accuglassproducts.com/subminiature-c/uhv-ribbon-cables/9-pin-female-connector-cable
- Accu-Glass air-service 9-lead cable assembly (100020/100021): https://www.accuglassproducts.com/subminiature-c/air-cables-components/air-service-connector-cable-female
- Accu-Glass Sub-C air connectors & cables index: https://www.accuglassproducts.com/subminiature-c/sub-c-air-connectors-cables
- Accu-Glass air-service female Sub-C connector (100160): https://www.accuglassproducts.com/subminiature-c/air-cables-components/air-service-connector-female
- Accu-Glass Sub-C specifications PDF (protrusion dims — UNREAD, no PDF extraction in this environment): https://www.accuglassproducts.com/sites/default/files/catalog/subminiature_c_specifications.pdf
- Accu-Glass Sub-D catalog PDF (UNREAD, same limitation): https://www.accuglassproducts.com/sites/default/files/catalog/subminiature_d_feedthroughs.pdf
- Accu-Glass MIL-C-26482 family landing (500 VDC / 5 A / −200…250 °C / 1×10⁻¹⁰ Torr): https://www.accuglassproducts.com/mil-c-26482
- Accu-Glass 19C-275 (110210): https://www.accuglassproducts.com/mil-c-26482/cf-feedthroughs/19c-275
- Accu-Glass 19C-275 UHV components index (110230/110240): https://www.accuglassproducts.com/mil-c-26482/uhv-components
- Accu-Glass 19C-275 UHV ribbon cables index: https://www.accuglassproducts.com/mil-c-26482/uhv-ribbon-cables
- Accu-Glass 19C-275 air cables/components index (110232/110234): https://www.accuglassproducts.com/mil-c-26482/air-cables-components

---

## 9. Post-run addendum (2026-07-10, user-driven follow-up)

The user asked whether Accu-Glass's **19C-275** (MIL-C-26482, 19-pin, 2.75″ CF,
https://www.accuglassproducts.com/mil-c-26482/cf-feedthroughs/19c-275) was a feasible
alternative. **It is, and it is now the primary recommendation.** ST5's original search covered
only the Sub-D and Sub-C families; it did not check MIL-C-26482, a third circular-connector
family Accu-Glass also offers on a 2.75″ CF flange.

**Verified (fetched 2026-07-10):** P/N 110210, $434.00, 19 gold-plated Ni-Fe pins, 2.75″ CF with
the same 1.45″ ID bore as the 9C2-275 (same gasket P/N 200760), 500 VDC / 5 A per pin (≤20 %
simultaneous) / −200…250 °C / 1×10⁻¹⁰ Torr — matching the 9C2-275 on every rating. Mating
accessories exist and are pre-terminated (110230 vacuum, 110232 air) — no crimp-tool dependency,
same as the 9C2-275 path. System cost ≈ **$1,145** vs. $1,572 for 9C2-275.

**Why it wins over the prior primary (9C2-275):** single connector shell vs. two. This removes
the entire A/B mis-mate risk that drove `WIRING_PLAN.md`'s (ST6) anti-swap pin-map and labeling
requirement, at lower cost, with one more spare pin, on the same unmodified 2.75″ CF port.

**What this update did:** rewrote §§ BLUF, 1, 2 (verdict), 4, 5, 6, 7, 8, and Sources above to
make 19C-275 primary and 9C2-275 the 2.75″-path alternate (fallback if the 19C-275 fails its
contact-gauge or protrusion-height check). Also updated `90_SYNTHESIS/DECISION_GATES.md` (GATE
2) and `05_STATE/MASTER_STATE.json`.

**What this update did NOT do — open reconciliation debt:**
- `60_WIRING_SHORTS/WIRING_PLAN.md` (ST6) and `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` (ST8) were
  both written around the 9C2-275's specific dual-tower geometry (0.750″ tower centers, two
  connector shells, the A/B swap FMEA, the height ledger built on "two Sub-C towers"). Neither
  has been re-run against the 19C-275's single-shell geometry. Until the 19C-275's protrusion
  height is confirmed (§7) and, if it clears, ST6/ST8 are reconciled to a single-shell layout,
  **treat those two documents' mechanical specifics (pin grouping across two connectors, tower
  height ledger, A/B swap FMEA) as written for the now-alternate 9C2-275 pick, not the new
  primary.** A single-shell reconciliation is very likely to *simplify* both documents (no
  A/B swap class of fault to design against; a single-tower height budget is a subset of the
  two-tower analysis ST8 already did) — but that simplification has not been done and should not
  be assumed without doing it.
- `90_SYNTHESIS/RED_TEAM.md` and `RECOMMENDATIONS.md` were flagged with a pointer to this
  addendum (see their own follow-up notes) rather than re-run; their ST6/ST8-dependent findings
  carry the same caveat as above.

---

## Orchestrator addendum (2026-07-10, after ST6)

ST6 (`60_WIRING_SHORTS/WIRING_PLAN.md`) successfully read the Accu-Glass Sub-C
specifications catalog PDF that this file marked UNREAD, closing several UNVERIFIED items:

- **500 VDC rating confirmed at family level** for the Sub-C line (was family-page-only here).
- **Keying:** Sub-C connectors mate with a **polarizing screw boss** — positive anti-mis-mate
  keying exists at the connector level.
- **Tower geometry: 0.750″ connector-tower centers** on the dual-connector 9C2-275 —
  feeds the ST8 stand design (protrusion height above the flange face still UNVERIFIED).
- Vacuum-side cable construction: **foil + drain shield** per catalog (informs the ST6
  shield/drain plan).

See WIRING_PLAN.md §Sources for the catalog citation. Remaining open per this file:
protrusion height, stock/lead times, prices for 100021/100160/101060 — call Accu-Glass.
