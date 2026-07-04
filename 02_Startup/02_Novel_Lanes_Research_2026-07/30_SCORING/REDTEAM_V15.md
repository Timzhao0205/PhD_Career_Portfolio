# RED TEAM — V15 Vendor-agnostic battery-buffer retrofit kit for RTG cranes (lane G08)

Date 2026-07-03 · Raw 76.0 · Sources: `30_SCORING/REDTEAM_V15_sources.json` (RT-V15-01..25)

## 1. Novelty verification (G7-NOVEL)

Nearest ledger neighbors checked: **C08** (GPU transient buffer / facility ride-through), **RID-002**/PWR-03/CL-03 (rack/AI-load DC buffers), **C09**/RID-004 (SST blocks), **C38** (GFM PCS, compute microgrids), plus C04 (MCS charging) and C40/RID-016 (pack grading). The functional guts — a DC-bus battery buffer that peak-shaves a bursty load to shrink required grid feed — rhyme with the C08/RID-002 family, but buyer segment (terminal operators, not datacenter/colo), duty (hoist regen on a mobile diesel-hybrid platform), and category (crane drive-bus retrofit kit with genset coordination, no SST stage) all differ materially. Not a re-parameterized ledger variant. **Verdict: NOVEL — G7 passes.** The duplication problem is with the *commercial market*, not the ledger — and it is severe (below).

## 2. Strongest bear case

Both load-bearing whitespace claims are already false. "Konecranes retrofits only its own fleet": Konecranes launched Battery-RTG/E-Hybrid **refits "both on its own cranes and other brands" in May 2026** [RT-V15-01,03]. "ZPMC sells new cranes": **ZPMC North America delivered DP World Prince Rupert's hybrid RTG retrofit in June 2026** [RT-V15-02], and ZPMC signed a 12-RTG diesel-to-lithium retrofit for Thailand's LCMT [RT-V15-07]. The category itself is ~18 years old (Vycon flywheel 2008; EPA-verified EcoCrane, 56% fuel economy, ~2010; Corvus batteries already in 186+ hybrid RTGs) [RT-V15-12,14,18]. By 2031 V15 is an unreferenced integrator bidding against OEM service arms holding warranty control, spares networks, and fleet data — after the 2025–27 retrofit wave was contracted.

## 3. Hidden competition (the one-pager missed the whole roster)

Konecranes multi-brand refit line + Hybrid Power Pack + 200+ fielded hybrid RTGs, 30-crane E-Hybrid fleet order in India [RT-V15-01,03,04,05,06]; ZPMC NA + CCCCSEE + **Corvus** (25 battery-hybrid RTGs at South Carolina Ports, 65% fuel cut) [RT-V15-02,17,18]; **Conductix-Wampfler** hybrid battery systems and FE-RTG battery packs "also in ones already in use" [RT-V15-09]; **TMEIC** E-Tanker (May 2026) — containerized mobile charging + FMS that electrifies mixed fleets with *zero* drive-bus surgery, and TMEIC/ABB/Siemens already own the drives inside most RTG brands, making them the natural "vendor-agnostic" integrators [RT-V15-10,11]; **Kalmar** Hybrid RTG + electrification retrofit services [RT-V15-16]; **Mi-Jack/MJ EcoPower** EcoCrane (EPA-verified) [RT-V15-12,13]; **Vycon** REGEN (CARB-listed) [RT-V15-15]; **VAHLE** eRTG [RT-V15-22]. China: 油改电 is commodity practice — INVT and Veichi sell RTG hybrid/energy-feedback retrofit kits off the shelf; provincial programs run through SOE port groups [RT-V15-19,20,21,25]. Correction to tasking tip: MJR Power & Automation is vessel/marine-only, no RTG line [RT-V15-24]. Patent estate: crane regen-ESS patents date to 2009 (US 7,554,278) — dense prior art cuts both ways: old claims expire, but Konecranes/ZPMC hold fresh ones (ZPMC RTG battery-swap patent, July 2025) [RT-V15-08,23].

## 4. Engineering reality check

Nothing extreme: ~600–750 VDC crane bus, 200–600 kWh LFP at ≤2–3C, brake-chopper tap — catalog parts, which is why a dozen vendors ship it. The declaration's "1–4 MW peaks" overstates RTG duty 2–10x: Konecranes' own grid-peak figure for a full-electric RTG is 400 kW [RT-V15-05]; 4 MW is STS-class. Regen is real but bounded (~37% of hoist energy, HPH data 2008 [RT-V15-14]) and every incumbent hybrid captures it. The hard part is per-OEM drive integration, safety interlocks, and liability on a live $1.9M asset — a warranty/certification wall favoring OEMs, not a physics wall a startup wins.

## 5. Willingness-to-pay skepticism

WTP is real (50–74% fuel cuts documented since 2008–2010) — and therefore already monetized. Actual buyers procure from OEM service arms or crane-drive OEMs: DP World via ZPMC NA, SC Ports via CCCCSEE/ZPMC, Indian terminal via Konecranes. Gdynia's EUR 10.9M NPV was an EU-funded, EPC-delivered 15 kV conductor-rail conversion — a different architecture that bypasses buffers entirely. No evidence any terminal buys safety-critical drive-bus surgery from a seed-stage vendor; EPA Clean Ports/CARB money flows to EPA/CARB-verified equipment (EcoCrane, Vycon listed).

## 6. Founder-fit doubts

Not PhD-lane, but C1=4 is pattern-matching "power electronics × battery." The kit monetizes none of the founder's extreme-edge capabilities (density, kHz FPGA control, beyond-marine-grade packaging); it is LFP racks + catalog bidirectional DC-DC + PLC integration — any competent integrator's job, and ten are already doing it.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 4→3 | Commodity integration; capability graph unused |
| 2 | 3→2 | Replicates Konecranes' published numbers; EPA-verified category since ~2010; "1–4 MW" inflated |
| 3 | 4→3 | Named beachhead already served (ZPMC NA at DP World; Konecranes any-brand refits) |
| 4 | 4→3 | Reach-stacker/straddle expansion owned by same OEM arms; fleet software contested by TMEIC FMS |
| 5 | 4→3 | Inflection is 2025–26 and being captured now; 2029 arrival is post-window |
| 6 | 4→4 | Genuinely buildable (that is the problem) |
| 7 | 3→2 | Whitespace empirically false; ≥10 named shipping competitors |
| 8 | 4→3 | China SOE-locked (ZPMC/CCCCSEE/port groups); US channel verified-vendor-locked |
| 9 | 4→4 | No added regulatory risk |
| 10 | 4→3 | Live-terminal pilots + per-OEM warranty negotiation are slow |
| 11 | 4→4 | Kit has standalone value |

**Adjusted total: 60.0** (was 76.0; −16.0).

## 8. Steelman

Thousands of diesel RTGs will never make OEM refit queues, the Corvus/Conductix component chain is open to anyone, and a regional integrator with a standardized kit plus better fleet-energy software could profitably serve secondary ports the giants ignore. TMEIC's E-Tanker proves demand for non-invasive electrification paths. But that is a regional systems-integration services business with OEM-set price ceilings — not a venture-scale extreme-performance product.

**Recommendation: KILL (market-crowding + false premise, not ledger novelty). Kill-probability 90%. Do not advance; pull a reserve seed.**
