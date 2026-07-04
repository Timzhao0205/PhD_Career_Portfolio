# RED TEAM — C23: JEDEC-compliant automated WBG characterization appliance

**Verdict summary: kill probability ~75%. The one-pager's core premise — "no product exists" — is false.**

## Strongest bear case

The category already exists at both ends of the price spectrum, and the JEDEC angle is a software feature, not a product. Keysight has shipped the PD1500A (discretes) since 2019 and the PD1550A (modules) since 2022 — turnkey automated DPT appliances [RT-C23-01][RT-C23-02]. Tektronix's WBG-DPT scope option already performs "automated switching, timing, and diode reverse recovery measurements per JEDEC and IEC standards" [RT-C23-03] — meaning JEP203/204 compliance arrives at incumbents as a firmware update, months before Tim's 2029 v1 ships. The S127 Catapult anecdote proves a UK lab chose to build shared capacity, not that no product exists. By launch, C23 enters a 10-year-old category against entrenched vendors with calibration networks.

## Hidden competition (what the one-pager missed)

- **忱芯科技 (UniSiC, Shanghai, founded 2020)** is essentially C23 already built: SiC/GaN dynamic test, wafer-level dynamic WLR, KGD, static, dynamic-reliability, and bipolar-degradation systems; RMB 200M+ B/B+ round led by state fund 国投创业 (Dec 2024); systems already validated by **Wolfspeed and onsemi** [RT-C23-04][RT-C23-05]. Five-plus years and nine figures of capital ahead of a 2029 solo launch.
- **PE-Systems GmbH (Germany)** sells a fully automated, vendor-agnostic double-pulse tester and demos with Rohde & Schwarz (MXO 5 + RT-ZISO) on 1200 V SiC [RT-C23-06][RT-C23-07].
- **RIGOL (普源精电)** markets a Chinese-price DPT bundle (DG5000 Pro + PIA1000 isolated probe + DHO5000 12-bit scopes) aimed at EV-drive customers [RT-C23-08] — attacking the sub-$150K wedge from below.
- **LEMSYS (Switzerland)**: switching test to 600 A/1500 V and short-circuit test to 2500 A — the "ruggedness" leg is already commercial [RT-C23-09].
- **长川科技**: CTM2100 avalanche module plus PIM solutions at 2000 V/1000 A DC, 1200 A dynamic AC [RT-C23-10]; **华峰测控** is explicitly expanding STS coverage into GaN/SiC/IGBT discretes and modules [RT-C23-11]; **联讯仪器** holds ~43.6% domestic share in SiC burn-in with BYD Semiconductor as customer [RT-C23-12]. **NI/SET** sells dynamic-HTGB and H3TRB reliability testers [RT-C23-13].

## Physics/engineering reality check

The "edge" evaporates at the fixture. DPT accuracy is dominated by layout parasitics, probe deskew, and DUT-specific fixturing — the parts that don't productize; that's why Keysight and PE-Systems sell configured systems, not boxes. A credible GaN dynamic-Ron + SC appliance needs isolated GHz-class probing and clamp circuits (published academic designs, no IP moat) plus arc-safe destructive-test containment. Worse, bundling **HTRB — a 1,000-hour elevated-temperature chamber stress test — into a "bench appliance" is technically incoherent**; it signals scope creep, not focus. Sub-$150K with scope-grade digitizers inside leaves thin margin after CE/UL safety certification of a kV-class pulsed instrument.

## Market skepticism

Nobody cited actually says they'd pay. University/DoE labs (the named beachhead) buy on grant cycles, prize flexibility over appliances, and build DPT rigs with free grad-student labor — Tim is himself the counter-evidence. "Mid-tier device makers" are shrinking, not growing: the 2025 SiC price crash and Wolfspeed's Chapter 11 gutted mid-tier capex. JEP203/204 are *guidelines*, not qualification mandates — no OEM contract requires a compliant instrument. "Hundreds of buyers × $80–150K" is a ~$30–50M SAM contested by six-plus named vendors.

## Founder-fit doubts

Solo founder, first revenue gated on graduating (~2029). T&M is a channel business: demo inventory, field application engineers, calibration/service contracts, CE/UL/CSA compliance — none of which a PhD bench skillset covers. Seed-scale capital cannot fund demo units plus a service network. Running the measurement daily ≠ selling instruments to procurement.

## Score adjustments

- **Extreme edge / whitespace: −1** — Keysight, Tek, PE-Systems, UniSiC already occupy it.
- **Competition/moat: −1** — JEDEC compliance is an incumbent software update.
- **Beachhead willingness-to-pay: −1** — labs self-build; mid-tier capex collapsing.
- **TRL/speed-to-revenue: −1** — 9–12 months to a safety-certified kV appliance, solo, is fantasy; 18–24 realistic.
- **Founder fit: hold** — the technical fit is genuinely strong; the gap is commercial, not technical.

## Steelman rebuttal

A believer would say the incumbents prove demand while pricing at $300K+ leaves a real gap for an integrated sub-$150K unit; UniSiC will face FEOC/export-control headwinds in US/EU labs, creating a "trusted-vendor" niche; and JEDEC standardization historically expands instrument TAM (cf. compliance-test suites in high-speed digital), so a compliance-native, software-first entrant at the right price could still take the long tail Keysight ignores.

---
**Kill probability: 75%.** Biggest objection: the founding premise ("no product exists") is factually wrong — Keysight PD1500A/PD1550A, PE-Systems, and a Wolfspeed/onsemi-validated Chinese startup (忱芯科技) already sell this product.
