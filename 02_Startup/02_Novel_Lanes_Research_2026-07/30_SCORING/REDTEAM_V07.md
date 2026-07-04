# RED TEAM — V07 Vendor-agnostic laser-power-beaming receiver module (lane G05)

Date 2026-07-03 · Raw 84.4 · Sources: `30_SCORING/REDTEAM_V07_sources.json` (RT-V07-01..21)

## 1. Novelty verification (G7-NOVEL)

Nearest ledger neighbors checked: **C29** (smallsat EP PPU/PCDU), **C26/C28** (rad-characterized space WBG / rad-tolerant DC-DC), **RID-100** (photonic active-alignment assembly cell), **W-AYAR** (CPO interconnect), **C05** (DoD pulsed-power for directed energy — transmit-side electronics), **N04** (subsea inductive WPT — different medium/buyer). No ledger entry sells terrestrial/airborne optical-power *receive* conversion to beaming primes/UAS OEMs; buyer segment AND product category are new. Not a re-parameterization: PPU/PCDU manage satellite buses; this converts free-space photons. **Verdict: NOVEL — G7 passes.** The kill case below is competitive/market, not novelty.

## 2. Strongest bear case

The merchant slot V07 targets is being foreclosed in real time. PowerLight unveiled its **end-to-end** PTROL-UAS system in Jan 2026 with its **own ~6 lb receiver** (laser power converters + embedded telemetry/control) [RT-V07-01], and flew it operationally at Shaw AFB Apr 2026 (the very demo the one-pager cites as beachhead evidence — both ends were PowerLight's) [RT-V07-02, RT-V07-19]. DARPA's receiver mandate is already held by **Teravec Technologies** (PRAD record receiver, w/ Packet Digital + RIT), which markets "modular, scalable 10–100 kW" receivers [RT-V07-03/04/05]. By 2031 V07 is the third merchant receiver vendor in a market with zero commercial revenue and single-digit annual DoD demo procurements.

## 3. Hidden competition (missed by the one-pager)

Above: **PowerLight** (vertical, in-house receiver), **Teravec + Packet Digital** (DARPA incumbent), **Aetherflux** (builds its own PV ground stations; $60M, 2026 orbital demo) [RT-V07-14]. Below, the cell layer — where the efficiency IP actually lives — is a catalog business: **Broadcom** AFBR-POC multi-junction photonic power converters (800–830/960–990/1500–1600 nm) [RT-V07-06], **Lumentum** PPC-6E (790–850 nm) [RT-V07-08], **MH GoPower** Si-VMJ cells (915–980 nm, stable >100 W/cm², sells *turnkey* PoF/power-beaming solutions itself) [RT-V07-07]. China: **长光华芯 Everbright Photonics** ships laser-battery chips (70.1% cell claim, 179 W/20 m demo) [RT-V07-10]; 西安电子科技大学's 逐日工程 SSPS chain is **microwave**, not laser (kW @ 100 m, MW orbital ~2030) [RT-V07-12/13] — the Chinese state track partly bypasses laser receivers entirely.

## 4. Physics/engineering reality check (the 2x claim)

2x DARPA's >20% is cell-physics-plausible: Fraunhofer hit 68.9% at 858 nm monochromatic [RT-V07-09], so ~40–50% module-level is credible. But (a) that efficiency is epitaxy IP owned by cell vendors and equally purchasable by every prime — the integrator adds MPPT and packaging, not the 2x; (b) wavelength-matching **contradicts vendor-agnosticism**: cells are band-specific (see the three Broadcom bands vs. MH GoPower's 915–980 vs. HELSTF's ~1 µm source), so V07 is either matched (per-transmitter SKUs, bespoke again) or broadband (silicon-class efficiency, no 2x). You cannot ship both claims in one module; (c) at 40% efficiency, 60% of multi-kW flux is heat — active cooling mass erodes the W/kg pitch against PowerLight's existing 6-lb/kW-class in-house benchmark; beam-profile nonuniformity forces per-string MPPT; safety interlocks must speak each transmitter's proprietary beacon protocol (ANSI Z136.6 / FAA AC 70-1B ops approvals are transmitter-operator-led, pulling the interlock design prime-ward) [RT-V07-15/16].

## 5. Willingness-to-pay skepticism

There is no commercial power-beaming revenue anywhere; the "market" is DARPA POWER (Phase 2 subscale relay demo 2026 at HELSTF; Phase 3 is a *decision gate*, not a commitment) [RT-V07-17], CENTCOM-sponsored demos, and OECIF/OEPF prototype funds — no program of record as of mid-2026 [RT-V07-18]. Receiver specs in POWER flow to the relay/receiver contractors already inside the program, not to a merchant catalog. The China angle ("sell instrumentation-grade receivers into Chinese research programs") is export-control-dead both directions: dual-use directed-energy adjacency outbound; III-V feedstock whipsaw inbound (gallium banned Dec 2024, +150% price, suspension expires Nov 2026) [RT-V07-20/21].

## 6. Founder-fit doubts

Not PhD-lane, but C1=4 overstates fit: the value stack is III-V cell array engineering, concentrator/stray-light optics, and kW-class thermal — none demonstrated by the founder. The genuinely matched pieces (MPPT/power conditioning, FPGA telemetry) are the commodity 30% of the module. "Optics-adjacent motion/alignment" is not receiver photonics.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 4→3 | No optics/III-V/thermal track record; matched skills are the commodity layer |
| 2 | 5→4 | 2x lives in purchasable cells; 2x XOR vendor-agnostic |
| 3 | 4→3 | Beachhead buyers build in-house (PowerLight) or are taken (Teravec) |
| 4 | 5→4 | Space/commercial expansion owned by vertically integrated players |
| 5 | 5→4 | Phase-3 is a decision gate; no PoR; timing single-threaded on DARPA |
| 6 | 4→4 | kW receiver buildable — proven by competitors (that is the problem) |
| 7 | 4→3 | Squeezed: cell IP above, prime integration below, Teravec beside |
| 8 | 3→2 | China sales blocked; China has own cell champion + microwave track |
| 9 | 3→2 | Dual-use both ways + Z136.6/FAA ops burden + gallium whipsaw |
| 10 | 4→3 | Demo-trickle revenue; single-digit units/yr through ~2030 |
| 11 | 5→4 | Useless without someone's transmitter; ecosystem-contingent |

**Adjusted total: 66.4** (was 84.4; −18.0).

## 8. Steelman

DARPA explicitly wants an industrial base, Teravec is tiny, and a 2027–28 receiver-spec standardization moment could create exactly one merchant slot; the founder's MPPT + safety-telemetry firmware could win the power-conditioning brick *inside* every receiver rather than the whole module. If Aetherflux-class constellations scale, qualified ground-station arrays become a real volume market. That is a subsystem/wait-and-see thesis, not the scored 2029 module thesis.

**Recommendation: KILL (foreclosed merchant slot + no non-DoD market + internal claim contradiction). Kill-probability 80%. Do not advance; pull a reserve seed.**
