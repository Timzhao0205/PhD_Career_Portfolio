# RED TEAM — C13: HTS current leads & low-resistance joint/splice modules

Reviewer stance: adversarial. Currently ranked #10 (77.6). Both halves of the product are weaker than the one-pager admits: one half is a decades-old commodity, the other half may not be a purchasable component at all.

## Strongest bear case

The business splits into (a) current leads — a mature, crowded, slow market — and (b) joints — which are largely **not outsourceable**. Pancake-to-pancake bridge joints, splices over tape defects, and terminations are fabricated *in situ* during coil winding and assembly, from the customer's own conductor lot, in the customer's geometry [RT-C13-05][S091]. You cannot ship a "joint module" the way you ship a connector; you can only ship a recipe, a jig, or an engineer — a consulting business, not a component business. Meanwhile the leads market that *is* purchasable was worth ~$123M globally in 2024, growing at 4.2% CAGR to ~$164M by 2031 [RT-C13-03] — sub-venture-scale and already divided among seven-plus named vendors. A 2030 entrant with zero fielded reliability history, in a market that buys on decade-long track records, most likely dies as a job shop.

## Hidden competition (the one-pager names no incumbent; there are many)

- **HTS-110 (NZ)**: CryoSaver leads, 150A–2000A catalog, "over a thousand leads in the field" for more than a decade, distributed in North America through GMW Associates with published price lists [RT-C13-01][RT-C13-02]. This is exactly the beachhead product, already commoditized to catalog-and-distributor form.
- **Named market leaders**: Hall Scientific, Energy to Power Solutions (E2P), DABS, Furukawa Electric, Solid Material Solutions, Brookhaven Technology Group, CAN Superconductors [RT-C13-03]. Sumitomo commercialized BSCCO MRI leads years ago; Cryomagnetics bundles HTS leads with its magnet systems [RT-C13-08]; ASG Superconductors publishes its own BSCCO lead optimization — integrators making, not buying [RT-C13-07].
- **China**: the largest HTS leads ever procured — ITER's 68 kA TF leads — were designed, built, and tested by **ASIPP (中科院等离子体所)**, a state lab, since 2007 [RT-C13-04]; 上海超导/上创超导 anchor a full-chain domestic HTS industry [RT-C13-06]; SAMRI (上海超导材料研究院 / Jiangsu Etern) and SuNAM (Korea) are conductor makers moving downstream. Leads are the easiest HTS component to clone domestically.
- **MRI joints**: persistent-current PbBi/NbTi joints are guarded in-house IP at Siemens/GE/Philips with a 40-year patent thicket [RT-C13-09] — that door is closed.

## Physics/engineering reality check

Lap-splice resistance in REBCO is dominated by the tape's own architecture — interface resistance and stabilizer plating quality — i.e., by the *conductor vendor's* product, not the joiner's skill; reduction techniques reaching few-nΩ are already published in the open literature [RT-C13-05]. True superconducting REBCO joints remain unreproducible at any vendor [RT-C13-10], so the "extreme edge" is either a published solder recipe (no moat) or an unsolved research problem (no product). Every joint must additionally be qualified in the customer's field/temperature/strain state — each sale is NRE.

## Market skepticism

No cited source shows anyone *buying* joints as components; S054 documents that splices fail, not that a procurement line-item exists. The one purchasable SKU (leads) has hard market-size data: $123M, 4.2% growth [RT-C13-03] — flagged by nobody in the one-pager. Big buyers (ITER, national labs, CFS-class fusion firms) demonstrably self-supply [RT-C13-04].

## Founder-fit doubts

A solo 2029 PhD selling $5–50K parts against distributor-backed incumbents needs a catalog, a 10 kA-class cryogenic test stand (expensive), long lab-procurement cycles, and field-failure liability — with the thinnest software content in the portfolio (the G2 flag is fatal for venture financing). No channel, no certifications, no service network.

## Score adjustments

- **extreme_edge 4 → 3**: splice recipes are published; resistance is set by tape architecture.
- **whitespace_moat 4 → 3**: HTS-110 + six named vendors; catalog commodity.
- **beachhead 3 → 2**: joints not procurable as components; leads TAM $123M and crowded.
- **why_2029 4 → 3**: 4.2% CAGR market — no discontinuity a new entrant rides.
- **standalone_value 3 → 2**: only coherent as a C12 attach/consumable.

Net: ~66–68, bottom quartile.

## Steelman rebuttal

The incumbents are BSCCO-era lead makers; fusion's REBCO wave creates a genuinely new category — high-current REBCO terminations, demountable joints, and qualified splice kits — that none of them serve, and second-wave magnet builders without CFS-scale in-house teams will pay to de-risk their named worst failure mode [S054]. Bundled with C12 machines as qualified consumables and tooling, C13 becomes recurring attach revenue rather than a standalone parts catalog.

---
**Kill-probability estimate: 75%. Biggest objection: the joint "component" cannot actually be shipped — joints are made in situ from the customer's conductor during coil assembly — leaving only a $123M, 4.2%-growth commodity leads market already owned by HTS-110, CAN Superconductors, Furukawa, and state labs like ASIPP.**
