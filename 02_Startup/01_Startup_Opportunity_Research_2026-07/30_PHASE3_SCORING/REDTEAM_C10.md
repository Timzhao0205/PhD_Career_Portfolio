# RED TEAM — C10: Precision GaN/SiC magnet & scientific power converter line

Reviewer stance: adversarial. Current score 88.4 (rank 2). Verdict: overrated.

## Strongest bear case

The one-pager assumes a whitespace that does not exist. "Catalog ppm-class magnet supplies with fast lead time" is already a shipping product category (CAENels FAST-PS family; Danfysik's standard high-stability line, 60 years in market [RT-C10-01][RT-C10-02]), and the fat fusion budget line — pulsed CS/PF converters — is utility-scale thyristor work owned by Jema Energy (ITER, JET, MAST-U TFPS) and China's Rongxin Huike [RT-C10-04][RT-C10-05]. Meanwhile CFS is selling *fully integrated* magnet systems "including power" to other fusion companies (Realta deal), vertically absorbing exactly this product [RT-C10-09]. A solo founder launching v1 in 2029–2030 arrives after the DOE-milestone PDR wave (2027–2029, per the candidate's own [S058]) has been spec'd and sourced. Most likely 2031 outcome: a fine engineering demo competing on price against six incumbents and three Chinese listed companies for a handful of tenders a year.

## Hidden competition (missed by the one-pager)

- **Danfysik** (DK): standard + custom high-stability supplies, W-to-MW, accelerator installed base worldwide [RT-C10-01].
- **CAENels** (IT): FAST-PS/FAST-PS-M — digital, Ethernet-controlled, catalog precision supplies at 10 kHz update — this *is* the claimed product [RT-C10-02].
- **CERN Knowledge Transfer** licenses in-house converter designs; big labs largely self-design [RT-C10-03].
- **Jema Energy** (ES): ITER coil/heating supplies since project start; JET NBI HV; MAST-U toroidal field converter [RT-C10-04].
- **Magna-Power** (US, NJ): programmable DC to 10 kA/unit, 54 kA systems, explicitly marketed for tokamak field coils — the cheap-and-cheerful option US fusion startups actually buy [RT-C10-08].
- **荣信汇科 (Rongxin Huike)**: ITER ELM-PS contract (27 converter sets, signed Jan 2026 with SWIP), VS1/VS3, EAST, HL-3, CFQS-T stellarator; STAR-board IPO in progress [RT-C10-05].
- **英杰电气 (Injet Electric)**: full fusion line — magnet, heating, control power [RT-C10-06]; BEST tenders are being fought over by multiple domestic listed firms [RT-C10-06a].
- **爱科赛博 (Actionpower, 688719)**: magnet + NBI/wave-heating supplies; claims domestically leading ripple at MA-class current [RT-C10-07].

The beachhead's China half ([S052] ¥1.3B CAS tenders) is precisely what these three domestic firms are winning. A US founder will not win a CAS institute tender; fusion power systems also carry dual-use export-control friction in both directions.

## Physics/engineering reality check

ppm stability lives in the DCCT, voltage reference, and thermal drift of the feedback chain — not in the switch. GaN/SiC buys switching frequency and density but injects EMI/common-mode noise that directly fights a ppm noise floor and nearby beam diagnostics. At kA class, GaN is irrelevant and SiC means massive paralleling/interleaving; after DCCTs, output filters, dump circuitry, and water cooling, "10x volumetric density" degrades to maybe 2–3x at system level — and converter-hall floor space is not a purchase criterion at any national lab. The "magnets are 28–40% of tokamak capex" framing [S054] is a bait-and-switch: converters are a single-digit-percent slice of that.

## Market skepticism

DOE milestone awardees are pre-revenue companies splitting a $46M program [S058]; they buy lowest-bid or in-house, in single-digit unit counts. US accelerator labs replace converters on decade cycles via FAR procurement requiring past performance. Nobody has evidenced willingness to pay a premium for "weeks not years" — labs' binding constraint is budget cycles, not lead time.

## Founder-fit doubts

Solo founder vs. a product needing a kA-class safety-rated test floor (water-cooled loads, HV interlocks — capital-intensive before first revenue), NRTL/CE/EMC compliance, magnetics manufacturing, and 12–36-month government sales cycles. The stellarator credibility is diagnostics-side, not converter-procurement-side. The China channel is unusable for him specifically.

## Score adjustments (rubric criteria)

- **#2 Extreme edge: 4 → 3** — CAENels/Danfysik catalogs already exist; WBG doesn't move ppm.
- **#7 Whitespace/moat: 4 → 3** — nine named competitors incl. three Chinese listed firms.
- **#8 China+US: 5 → 4** — CAS tender pipeline is inaccessible to a US solo founder.
- **#3 Beachhead: 5 → 4** — cash-poor DOE awardees, tiny unit volumes, tender procurement.
- No upward adjustments warranted. Implied retotal ≈ 80, out of the top tier.

## Steelman rebuttal

A believer answers: incumbents are slow, custom-quote, and pre-digital, while private fusion companies buy commercially and fast and desperately want modern telemetry-rich converters — Magna-Power's crude catalog winning fusion sockets proves labs will buy standard product. Ride 2–3 fusion startups as design partner in 2029, and own the "modern scientific converter" brand as the industry scales 10x; the Chinese firms' order books prove the category's revenue is real, not hypothetical.
