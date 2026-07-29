# P5-USSCI2-S01 — Diamond Transmission-Dynode Cartridge for Hybrid MCP-PMTs

<!-- SOURCE_IDS: P5-USSCI2-D01 P5-USSCI2-D02 P5-USSCI2-D03 P5-USSCI2-D04 P5-USSCI2-D05 P5-USSCI2-D06 P5-USSCI2-D07 P5-USSCI2-D08 P5-USSCI2-D09 P5-USSCI2-D10 P5-USSCI2-D11 P5-USSCI2-D12 P5-USSCI2-D13 P5-USSCI2-D14 P5-USSCI2-D15 P3R2-A-05-S01 L13-009 L13-014 L07-001 L07-002 L07-009 L07-023 -->

**Frozen selection status:** rank 6 of 24; top-10 deep dive; revised score **58.2/100**; confidence **medium-low**; TRL **3**. Frozen gates are recorded as pass in the authoritative selection, with the final adjudication retaining marginal competition, experiment-budget, and timing conditions. This document preserves that score and analyzes the conditions; it does not rescore the idea.

## Thesis

The product is a qualified diamond transmission-dynode membrane and integration cartridge sold to US hybrid microchannel-plate photomultiplier-tube developers. It is not a complete photodetector. The cartridge combines a thickness-controlled conductive CVD diamond membrane, a vacuum-stable negative-electron-affinity surface, electrodes and a guarded mechanical mount, serialized electron-yield and leakage maps, bake and dose records, and an acceptance dossier for a tube integrator.

The underlying detector job is real. A conventional MCP-PMT converts a photon at the photocathode, accelerates the released photoelectron toward a microchannel plate, and multiplies charge through repeated wall collisions. Photoelectrons that land on the solid area between the first plate’s pores may be lost. Raising photocathode quantum efficiency does not eliminate that collection loss, while demanding more gain from the MCP increases voltage and accumulated-charge stress. Brookhaven’s 2026 documentation explicitly identifies the open-area loss and a live photon-detection-efficiency effort [P5-USSCI2-D03]. A diamond transmission dynode placed before the MCP could turn one photoelectron into several transmitted electrons, relaxing the multiplication demanded from the plate.

The unusually strong part of the thesis is the buyer-job match. Brookhaven National Laboratory’s RFI 479547 asks outside organizations to procure and process thin diamond films, reduce thickness by laser or reactive-ion etching, create negative-electron-affinity surfaces, measure secondary-electron yield, and consider doping or coating for LDRD-26-055 [P5-USSCI2-D01]. That is almost the proposed v1 work package. It validates an external-capability need, not a future startup purchase order.

The timing thesis is strictly **upgrade-only**. Base ePIC photosensor procurement freezes too early and is excluded from the commercial case. A 2030 launch is countable only if a funded EIC Detector II, a post-freeze upgrade or replacement package, or an adjacent US fast-photon program adopts externally supplied dynode hardware. Brookhaven’s FY2027 LDRD agenda names the hybrid MCP-PMT/Timepix4 project for EIC Detector II [P5-USSCI2-D02], but Detector II construction funding is not committed. The company thesis dies on **2029-12-31** unless a US laboratory or tube maker pays for qualification or writes the cartridge into a funded design. Research interest alone is not a pass.

## Exact buyer, job, and product boundary

The first buyer is a US national-laboratory detector group or a US-serving MCP-PMT tube integrator responsible for turning a promising transmission-gain mechanism into repeatable vacuum hardware. The buyer’s painful job has six parts: source film with controlled thickness and conductivity; thin it without cracks or unacceptable roughness; create and preserve an emitting surface; integrate electrodes and a mount that survive handling and sealing; demonstrate yield, dark-current, timing, bake, and accumulated-charge behavior; and deliver traceable units with data a detector review can accept.

The BNL RFI is exact evidence for the first four tasks [P5-USSCI2-D01]. The broader EIC detector plan adds the system constraints: cost, pixel size, magnetic-field tolerance, common-photosensor procurement, and collaboration with large-area MCP developers [P5-USSCI2-D15]. Those requirements prevent a materials-only pitch. A high-yield membrane that contaminates a photocathode, cannot survive a tube bake, charges destructively, or creates unacceptable transit-time spread has no product value.

The cartridge boundary should therefore include:

1. incoming CVD diamond specification and metrology;
2. controlled thinning, edge definition, cleaning, and surface preparation;
3. two qualified surface-termination families and a documented air-transfer or vacuum-transfer procedure;
4. front and back electrode geometry, bias connection, and a guarded low-leakage mount;
5. serialized reflection and transmission electron-yield maps, dark-current data, dimensional inspection, and defect images;
6. a 200 °C bake record, accelerated input-charge exposure, helium-leak acceptance, and timing contribution; and
7. an interface-control document and lot-level acceptance dossier.

The company should not build the photocathode, MCP stack, Timepix4 ASIC, complete vacuum envelope, high-voltage supply, or detector readout. Production readout chips in other particle-detector programs already face extreme radiation, hit-rate, and multi-gigabit-output constraints [L13-009], while even a different single-photon technology requires tightly co-designed, picosecond-class readout [L13-014]. Those records are adjacent engineering evidence: they show why the cartridge must publish electrical and timing interfaces, not why it should absorb the electronics business.

This narrow boundary is strategically important. It turns BNL’s requested external work into a supplier product and leaves the mature tube and ASIC layers to organizations that already own them. It also creates a clean failure rule: if integrators will accept diamond processing only as fee-for-service research while retaining the design, data package, and production method in-house, there is no defensible cartridge company.

## Physics and technical plausibility

The mechanism does not require new physics. An incoming electron deposits energy in diamond, creating mobile carriers. With suitable electric field, thickness, transport quality, and surface electron affinity, carriers can reach the exit surface and emit into vacuum. Negative electron affinity lowers the escape barrier. Conductivity and electrode geometry must remove charge quickly enough to prevent field distortion, while the membrane must remain thin enough for carriers to reach the emitting surface and mechanically robust enough to handle.

The literature clears the mechanism gate but not the manufacturing gate. A peer-reviewed review surveys secondary-emission materials, transmission-dynode yield requirements, and integration tradeoffs [P5-USSCI2-D06]. Direct diamond experiments measure transmitted yield as a function of CVD film thickness, doping, and incident energy [P5-USSCI2-D07]. Earlier work reports strong secondary emission from negative-electron-affinity CVD diamond [P5-USSCI2-D08], while related measurements connect impact ionization, carrier transport, surface condition, transmitted intensity, and emitted-electron energy distribution [P5-USSCI2-D09]. A particularly relevant result reports transmission yield above ten at 1 keV from porous boron-doped diamond membranes [P5-USSCI2-D10]. Diamond dynodes have also been studied explicitly in photomultiplier reflection and transmission configurations [P5-USSCI2-D11].

These papers establish that a target transmission yield of at least eight at 1–3 keV is physically credible. They do not prove four repeatable, sealable cartridges from a small lot. Decades-old point demonstrations can hide the exact problems a company must own: pinholes, thickness gradients, edge damage, surface aging, adsorbates, contact resistance, local charging, membrane bow, and unit-to-unit variation after bake and air exposure. The v1 is valuable only if it converts a best-device result into a lot acceptance process.

The simplest gain arithmetic explains the “10x” aspiration. If one photoelectron produces a validated transmission yield of eight, then an equal downstream pulse can, in principle, use roughly one-eighth the subsequent MCP gain. A yield above ten would cross a literal order-of-magnitude ratio at that operating point [P5-USSCI2-D10]. This is not automatically a 10x lifetime improvement: MCP aging depends on total extracted charge, materials, bias distribution, rate, pulse spectrum, and required output signal. The decisive 10x claim is therefore narrower—approximately an order-of-magnitude reduction in required MCP multiplication for equal downstream signal, with no more than 50 ps added timing spread and acceptable dose stability.

That last condition is severe because current EIC-oriented HRPPDs report 15–20 ps single-photon timing and peak quantum efficiency above 30% [P5-USSCI2-D12]. A dynode that adds 50 ps would already be a material system penalty, even if the gain target passes. The cartridge must be evaluated as a coupled gain-timing-lifetime component, not as a yield coupon.

## Incumbents, in-house absorption, and the bear case

The competitor set is strong. Incom has received DOE small-business funding for EIC-oriented large-area multi-anode MCP-PMTs, with requirements including 3 mm pixels, high rate, and multi-tesla magnetic-field operation [P5-USSCI2-D05]. Brookhaven’s 2026 record says six DC-coupled HRPPDs are being ordered from Incom and describes a separate photon-detection-efficiency contract [P5-USSCI2-D03]. Those are base-program activities and are not startup revenue, but they show that an incumbent detector supply chain is active.

Hamamatsu sells catalog MCP-PMTs with picosecond response, photon-counting and gated options, and typical gain up to 10^6 [P5-USSCI2-D13]. Exosens/Photonis advertises PhotonPix at under 30 ps FWHM, above 30% quantum efficiency, high-rate operation, and collection efficiency approaching 100% [P5-USSCI2-D14]. If an incumbent reaches adequate collection efficiency and lifetime without an extra dynode, the cartridge becomes avoidable complexity. A tube maker can also license or reproduce the process, while BNL can internalize the method after its LDRD.

The wedge is therefore not “a better MCP-PMT.” It is a qualified upstream gain membrane that a tube integrator can insert without building a diamond thin-film and surface-chemistry line. The data moat would be process recipes linked to yield maps, bake history, accumulated-charge decay, timing contribution, and failure analysis across lots. The operating moat would be transfer, contamination, and mounting discipline. Neither moat exists yet.

The strongest bear case is that the 2026 RFI is a one-off capability search for a laboratory project. An established research contractor completes the work; BNL retains the architecture; Detector II is not funded; incumbents improve first-plate collection; and adjacent US programs stay with catalog sensors. Under that scenario the science succeeds and the company fails. The frozen score of 58.2 correctly reflects that distinction.

## Decisive nine-month experiment: $94,000

The first experiment should test repeatability and integrator relevance, not optimize one heroic membrane. It runs in 2027–2028 for nine months and uses at least 12 CVD diamond films spanning a prespecified thickness and doping matrix. The frozen budget is:

- **$18,000** — diamond films and incoming metrology;
- **$23,000** — laser and reactive-ion-etch thinning;
- **$16,000** — surface termination and electrodes;
- **$22,000** — UHV secondary-yield and pulsed-electron test access;
- **$9,000** — mounts, bake, and lifetime fixtures; and
- **$6,000** — contingency.

Total: **$94,000**. These are planning allowances, not supplier quotes. Before spending, replace them with written quotations and a laboratory safety scope. No facility access, partner commitment, or purchase order is assumed.

Apply two negative-electron-affinity treatments and two electrode schemes. Map reflection and transmission yield in UHV, leakage versus bias, spatial uniformity, and pulsed-electron timing. Repeat after a 200 °C bake and an accelerated accumulated-input-charge dose. The experiment passes only if four independent membranes achieve all of the following: transmission yield at least 8 at no more than 3 keV; within-wafer yield coefficient of variation no more than 15%; dark current no more than 10 nA at operating bias; no more than 10% yield loss after bake; and no more than 20% loss after the charge dose.

Kill the technical thesis on destructive charging, uncontrolled surface loss during the defined transfer process, or more than 50 ps timing spread attributable to the dynode. Kill the cartridge boundary if two independent tube integrators state in writing that the mount cannot be sealed or that the acceptance data would not support qualification. Four passing coupons without a credible tube interface do not pass.

Vacuum practice must be part of the experiment. Accelerator work shows how getter coatings, clean assembly, and outgassing control support extreme-high-vacuum systems [L07-001] [L07-002]. Medium-temperature treatment can reduce stainless-steel hydrogen outgassing dramatically [L07-009], and sensitive helium-leak methods can exceed ordinary detector limits [L07-023]. These sources do not specify the final cartridge acceptance number; they justify treating material history, bake, clean assembly, and leak testing as controlled variables rather than late packaging chores.

## Bottom-up commercial arithmetic

No accepted source validates a market price or unit forecast for the cartridge, so this section uses explicit scenarios. Assume an early qualification cartridge plus data dossier sells for **$35,000–$60,000**, falling to **$15,000–$30,000** for a qualified small production lot. Assume one cartridge per hybrid tube and a 45% contribution margin after diamond processing, outsourced UHV testing, yield loss, and documentation. All are diligence inputs.

A paid 12-unit qualification lot at a midpoint $45,000 produces **$540,000 revenue** and about **$243,000 contribution**. A 50-unit instrument lot at a midpoint $22,500 produces **$1.125 million revenue** and about **$506,000 contribution**. Three such programs or upgrade lots produce **$3.375 million revenue** and roughly **$1.52 million contribution**. At 200 production units, revenue is **$4.5 million** and contribution roughly **$2.0 million**.

The proposed v1 capitalization range is $1.8–$4.5 million before a scaled production line. The arithmetic therefore rejects a one-program company. Even 200 units may not repay development capital plus staff and overhead. A viable business needs paid non-recurring engineering, multiple US detector programs, repeat or replacement lots, and a high-value qualification dossier. It should not cite the EIC’s overall construction budget as addressable market. DOE’s 2026 CD-3B decision authorized about $67 million of long-lead EIC procurement and moved the project forward [P3R2-A-05-S01], but that spend does not imply any allocation to dynode cartridges.

The commercial pass is consequently more demanding than technical yield. By end-2029 there must be a paid qualification, funded work package, or signed design-in. By end-2032, require either one production order above $750,000 or two funded US programs. By end-2034, kill or convert the activity to a small research-service line if cumulative paid production and NRE remain below $3 million or no repeat order appears. These are management thresholds, not sourced forecasts.

## US route and non-countable China route

**2026:** respond to the exact capability category represented by the BNL RFI, reproduce published yield measurements on commercial coupons, obtain processing and UHV-test quotes, and draft an interface-control document. **2027:** execute the 12-film matrix and freeze process travelers, contamination controls, and serialized data fields. **2028:** deliver four passing cartridges for independent measurement only after written test terms; collect bake, timing, charge-dose, and sealability feedback. **2029:** require paid qualification or funded design-in. Without it, stop the commercial thesis.

If the 2029 gate passes, **2030–2031** is a US launch into the funded post-freeze program, not base ePIC procurement. **2032–2034** is the period to qualify a second US program, reduce lot variation, add a controlled transfer option, and secure repeat production. The EIC master schedule extends procurement, integration, installation, commissioning, and later work through 2035, but its PMT purchasing tasks also demonstrate why a 2030 entrant cannot claim the original photosensor order [P5-USSCI2-D04]. The opportunity is conditional on Detector II, upgrades, replacements, or adjacent US fast-photon programs.

**China is explicitly non-countable.** The selection is US-only: no Chinese buyer solicitation, program-specific design-in, qualification route, or lawful supply-chain plan has been validated for this cartridge. There is no China revenue in the base arithmetic, no China beachhead credit, and no fallback claim that unsuccessful US qualification can be offset there. Any later inquiry would require fresh buyer evidence, classification, end-use review, and a separate adjudication; it is outside this thesis.

## Safety, compliance, and quality

The shipped membrane cartridge is passive, but development is not low risk. The test system combines kilovolt bias, an electron source, UHV hardware, hot surfaces, pulsed signals, laser or reactive-ion-etch processing, thin brittle membranes, and surface-treatment chemicals. The laboratory plan needs interlocked high-voltage and electron-gun enclosures, current limiting, remote operation where appropriate, laser/RIE controls, chemical review, ventilation, vacuum-vessel safeguards, emergency shutdown, and trained operators. A written hazard analysis must precede the $94,000 experiment.

Quality records should include supplier lot, film thickness and doping, process traveler, cleaning and transfer time, electrode lot, dimensional inspection, yield-map coordinates, leakage curve, bake trace, residual-gas or contamination observations where available, accumulated charge, timing result, helium-leak result, nonconformance, and disposition. Detector radiation qualification belongs in the buyer program; the startup must not imply radiation hardness from diamond’s reputation alone.

The US civilian science route still requires classification and restricted-end-use screening before any export or controlled technical-data release. The company should use a US-only base supply chain and avoid promising cross-border delivery. Compliance is not a sales wedge; it is a condition for remaining a credible laboratory supplier.

## Evidence durability and refresh plan

The physics evidence is relatively durable. The peer-reviewed mechanism, thickness/doping tradeoffs, negative-electron-affinity emission, and historical transmission-yield results will not become false because a new product launches [P5-USSCI2-D06; P5-USSCI2-D07; P5-USSCI2-D08; P5-USSCI2-D09; P5-USSCI2-D10; P5-USSCI2-D11]. UHV bake, outgassing, clean-assembly, and leak-control principles are similarly durable [L07-001; L07-002; L07-009; L07-023].

The commercial evidence is refresh-sensitive. The 2026 RFI, FY2027 LDRD agenda, current Incom orders, Exosens and Hamamatsu specifications, EIC schedule, Detector II status, and DOE project approvals can all change [P5-USSCI2-D01; P5-USSCI2-D02; P5-USSCI2-D03; P5-USSCI2-D04; P5-USSCI2-D05; P5-USSCI2-D13; P5-USSCI2-D14; P3R2-A-05-S01]. Refresh those records at least quarterly through the 2029 gate. Specifically track whether the RFI becomes an award, whether external diamond work continues beyond research, whether Detector II gains funded scope, whether an upgrade specification names hybrid tubes, and whether incumbents close the collection-efficiency or lifetime gap without a dynode.

## Risks, kills, and verdict

The load-bearing risks are: surface instability between processing and sealing; poor lot repeatability; charging or leakage; bake and dose degradation; added timing spread; an unsealable mount; incumbent collection-efficiency improvement; BNL process internalization; loss of Detector II funding; and a market too small to support a product company. The experiment kills the first six. The end-2029 paid-qualification/design-in gate kills the commercial timing risk. The 2032 and 2034 revenue gates kill a technically successful but uneconomic niche.

**Verdict: retain as a conditional top-10 deep dive at the frozen 58.2 score.** The exact BNL RFI makes this more than a science-fiction materials idea, and the transmission-gain physics is supported by seven directly relevant peer-reviewed records. The investable thesis is nevertheless narrow: a US qualified cartridge for funded post-freeze detector work. Base ePIC procurement is excluded; China is non-countable; no access or order is assumed. Advance only through the $94,000 lot-reproducibility experiment and stop at end-2029 without paid qualification or a funded design-in.

Founder fit is secondary. Thin-film process control, electrical test, automation, statistical qualification, and data infrastructure transfer well from an EE/CE background. Negative-electron-affinity surface chemistry, UHV tube sealing, and detector qualification require specialist partners from the start.
