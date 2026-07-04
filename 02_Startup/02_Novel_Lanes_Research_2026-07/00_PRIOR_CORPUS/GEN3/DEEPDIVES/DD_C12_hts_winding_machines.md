# DD_C12 — Automated NI/MI-HTS Coil Winding & Jointing Cells (Capital Equipment + Process Software)

**Candidate:** C12 · **Analyst prefix:** DD-C12 · **Date:** 2026-07-03 · **Sources:** 31 (see `DD_C12_sources.json`)
**Red-team status:** REDTEAM_C12.md objections (1) incumbent vendors, (2) vertical integration of top buyers, (3) job-shop vs venture scale are addressed explicitly in §4, §5, and §8/§10. The one-pager's claim that "no third-party vendor exists" is **retracted** in this deep dive; the thesis is restated on corrected facts.

---

## 1. Problem & who has it

No-insulation (NI) and metal-insulation (MI) REBCO coils are the winding architecture behind essentially every record HTS magnet: NHMFL's 45.5 T world record used an NI REBCO insert [DD-C12-03]; ASIPP's 24.1 T all-REBCO magnet used a combined NI + MI scheme with co-wound high-modulus metal tape [DD-C12-14]. The physics that makes NI attractive (self-protecting turn-to-turn current sharing) is created **during winding**: MIT's foundational measurements show the coil's characteristic resistance comes almost entirely from turn-to-turn contacts, is set by winding tension held constant during fabrication (~71 μΩ·cm² contact surface resistivity in their builds), and directly determines charging delay and quench behavior [DD-C12-02]. In other words, for NI coils the winding machine's tension/placement recipe **is** the electromagnetic design. Get it wrong and you get unpredictable charging constants, screening-current strain, or delamination — failure modes serious enough that FSU patented active feedback control just to fight NI charging delay (850 s → 0.4 s) [DD-C12-06].

Who feels this pain in 2026–2031:

- **Second-wave fusion magnet programs.** 53 private fusion companies (FIA 2025 census), cumulative funding $9.77 B [DD-C12-25]; supply chain spend $434 M (2024) → $538 M (2025) → $681 M projected 2026 [DD-C12-26][DD-C12-27]. In FIA's 2024 supply-chain survey, 7 of 20 fusion companies named magnets as critical [DD-C12-23]; 31% flagged precision-engineering supplier availability as a current concern, rising to 63% for future needs [DD-C12-26].
- **Labs and universities building NI coils by hand or on self-built rigs.** KIT assembled its own two-robot ABB cell with a custom tension-controlled end-effector to wind non-planar NI coils — published December 2025, i.e., a top EU lab still had to build its own machine last year [DD-C12-01]. CAS Hefei patented its own winding-line subsystems (US11581133B2, inter-layer transition former for large SC coils) [DD-C12-05]. HFIPS/CAS runs regular public tenders for magnet prototype fabrication [DD-C12-15].
- **Chinese industrial HTS coil producers scaling volume**: 联创超导 plans to grow HTS induction-heater output from 27 units (2025) toward a reported 81 units/yr in 2026 (brokerage-reported plan, snippet-verified) [DD-C12-31]; 健信超导 is tooling a 600-unit/yr helium-free superconducting MRI magnet line and treats its proprietary **dry winding process (干式绕线工艺)** as core IP [DD-C12-29].

The archetypal buyer: a magnet program lead with $5–50 M, 5–30 staff, a coil design, tape on order — and no winding line, no tension-vs-Rc database, and no in-house machine-building team.

## 2. Product definition & the extreme-performance edge

**Product:** a turnkey **NI/MI coil production cell** — not a bare winding lathe:

1. **Laser-aligned precision winding head** for 4–12 mm REBCO tape: closed-loop tension (±0.1 N class vs the ~24 N setpoints used at KIT [DD-C12-01]), turn placement metrology, co-winding of stainless/copper tape for MI variants [DD-C12-14].
2. **Inline process QC**: continuous turn-to-turn contact-resistance estimation during winding (exploiting the tension→Rc relationship established in the NI literature [DD-C12-02]), tape defect-map-aware feed (slowing/flagging at low-Ic segments from the supplier's Ic-vs-position data), and per-coil digital traceability records.
3. **Joint station**: fixtured soldered-joint fabrication with in-situ nΩ-class verification — the industry benchmark is 1.3–5.5 nΩ for VIPER cable joints [DD-C12-04].
4. **Recipe software**: parametric winding programs (planar pancakes → D-shaped → non-planar per winding-angle optimization methods [DD-C12-07]), predicted charging constant per coil, fleet analytics. Sold as subscription.

**The edge, quantified against what incumbents ship:** Broomfield markets tokamak coil winders in NbTi/Nb₃Sn wire terms with tension/breakage/layer monitoring — no REBCO-tape, NI, or contact-resistance capability advertised [DD-C12-17]. Ridgway's catalog is taping/insulation-wrapping lines, 2D/3D winders and cable lines with PLC/dancer tension control — its named work (ITER CS/PF/TF wrapping, CERN, GA, PSI) is insulated-conductor-era; nothing NI-specific [DD-C12-18]. Supertek (BOW group) builds custom HTS **cable** winding machines [DD-C12-20]. None sells a machine whose output spec is "coil with predicted Rc ± 20% and logged joint resistance." That spec — machine + process physics + QC data — is the 10x claim: first-pass coil yield and per-coil qualification data, replacing wind-then-test-then-scrap iteration. It is honest to say (per the red team) this is **recipes-on-precision-motion, not ASML physics**; the defense is speed, data accumulation, and vendor neutrality (§4), not a physical moat.

## 3. Technical feasibility & TRL path to a sellable unit (2029–2031)

- **What exists:** the founder has personally built a laser-aligned automated NI-HTS winding machine (UIUC/Hinetics) — a working v0. KIT's published cell proves the architecture works with COTS robots + custom end-effector + PID tension via force feedback [DD-C12-01]. TRL of the machine concept: 4–6.
- **BOM sketch (v1 planar-pancake cell, ~$180–300K COGS):** granite/steel base, direct-drive rotary stage, 2–3 servo axes, laser line sensors + machine vision, load-cell tension arm, tape pay-off with defect-map sync, solder joint fixture + micro-ohmmeter (nV-class), industrial PC + custom control stack. All purchasable; the built parts are the end-effector, the recipe software, and the QC electronics — squarely inside the founder's power-electronics/precision-instrumentation/embedded skill set.
- **Hard parts:** (a) kilometer-length tape handling without Ic degradation (spool logistics, twist/camber control); (b) joint yield at nΩ under production conditions [DD-C12-04]; (c) non-planar geometry — a 6-axis-robot option pack, de-risked by KIT's published trajectories [DD-C12-01] and winding-angle math [DD-C12-07]; (d) customer conductor diversity (bare tape vs stacks vs cable) — mitigated by declaring v1 scope = single-tape/co-wound NI/MI pancakes and double-pancakes, which covers most current NI practice [DD-C12-02][DD-C12-14].
- **Cleanroom dependence: none.** A 200–400 m² light-industrial bay suffices.
- **Timeline:** v1 sellable cell in 12–18 months from company start (2029 → first delivery 2030); the personal prior build plus 2026–2028 PhD-side validation (§10) is what makes this credible for a solo founder.

## 4. Competitive landscape — global and China

**Red-team objection #1 (incumbents exist — "whitespace is fictional"): conceded and reframed.** The corrected map:

| Player | What they sell | NI/MI-HTS gap | Note |
|---|---|---|---|
| Broomfield (US) [DD-C12-17] | Tokamak SC coil winders (NbTi/Nb₃Sn framing), tension/layer monitoring | No REBCO/NI process layer advertised | Transformer-winding heritage firm |
| Ridgway Machines (UK) [DD-C12-18][DD-C12-21] | Taping/insulation wrap lines, 2D/3D coil winders, HTS cable lines; ITER, CERN, GA, PSI; multimillion-pound contracts | Insulation-era product line; no NI QC | **Acquired by Tokamak Energy, Sept 2025** [DD-C12-19] |
| Supertek/BOW (DE) [DD-C12-20] | Custom HTS cable winding machines | Cable, not NI coil process | Bespoke machine shop |
| CFS (US) [DD-C12-22][DD-C12-23] | **Magnets**, not machines (WHAM 17 T; Realta; Type One license) | Sells the output, not the tool | The real strategic competitor: makes "buy coils" an alternative to "buy machines" |
| KIT-style self-builds [DD-C12-01]; CAS winding-line patents [DD-C12-05] | In-house robot cells | — | Proves both feasibility and the self-build alternative |

The genuinely new fact vs the red-team file: **Ridgway is no longer neutral.** Tokamak Energy bought it to feed TE Magnetics' own scale-up [DD-C12-19]. A fusion startup buying its coil line from a direct competitor's subsidiary has an obvious information-leakage problem. From late 2025 there is **no vendor-neutral, HTS/NI-native winding-equipment specialist in the West** — Broomfield is LTS-centric, Supertek is a small custom shop. That is a real (if narrower and time-limited) opening, and it is the corrected version of the one-pager's false "no vendor exists" claim.

**China landscape (Chinese-language research).** Magnet manufacturing is treated as strategic and is vertically integrated at the leaders: Energy Singularity developed 绕制/绝缘/浸渍/组装 processes in-house for the 26-magnet all-HTS tokamak 洪荒70 (>96% localization, nΩ joints named among the conquered challenges) [DD-C12-08]; CRAFT's TF magnet passed acceptance with a "full-chain domestically controlled" narrative, magnets ≈53% of experimental-device value [DD-C12-28]; BEST's 6,000-ton assembly including the superconducting magnet system started May 2025 at Hefei [DD-C12-09]. Equipment-side: CAS Hefei patents its own winding-line machinery [DD-C12-05], and procurement flows through institutional 招标 channels [DD-C12-15]. Industrial coil producers (联创超导 induction heaters scaling 27→~81 units/yr [DD-C12-31]; 健信超导's 600-set/yr magnet lines with proprietary dry-winding [DD-C12-29]) build or closely control their winding capability as differentiating IP. Conclusion for C12: **China is a fast-follower threat and a hard sales territory, not a beachhead** — domestic toolmakers (motion + tension control is home turf) will clone an NI cell within ~2 years of seeing one, and the state ecosystem prefers 国产 equipment.

## 5. Market: beachhead sizing (bottom-up), expansion, TAM/SAM/SOM

**Red-team objection #2 (top buyers vertically integrate — who actually buys?): counted.**

Vertically integrated non-buyers: CFS, Tokamak Energy/TE Magnetics(+Ridgway), Proxima (ordered its own in-house cable line, Sept 2025 [DD-C12-24]), Energy Singularity [DD-C12-08], and CFS-ecosystem companies that buy **coils** instead of machines (Realta, Type One, WHAM-class projects) [DD-C12-22][DD-C12-23]. That removes the largest ~8–10 budgets. Remaining machine buyers, 2027–2031:

- **A. Second-wave fusion companies** building first coil labs without machine teams: of 53 FIA companies [DD-C12-25], magnetic-confinement designs needing HTS coils and not in the integrated set ≈ 15–25; realistic equippers in window ≈ **10–16 orgs × 1–3 machines = 15–35 machines**.
- **B. National labs / universities** (NHMFL, ORNL, PSFC, KIT, CERN test stands, KFE, QST, UKAEA, Columbia/UW/Tsinghua/SJTU-class programs; ex-China ~15–20 credible buyers given 招标/self-build leakage): ≈ **10–15 machines**.
- **C. Industrial HTS coil producers outside fusion** (motors — Hinetics-class; induction heating; benchtop NMR; SMES; MRI adjacency where NI is relevant): ex-China ≈ 8–12 orgs → **10–20 machines** (higher-volume lines, 2–4 cells each at maturity).

**Bottom-up beachhead:** 35–70 machines cumulatively over ~2027–2031 ex-China, i.e., **~10–18 machines/yr globally** at steady state. At ASP $400K–$1.2M (bespoke SC winding lines transact in "multimillion-pound" project sizes at the top end [DD-C12-21]; take $700K average): **served annual market ≈ $7–13M/yr in machines**, plus 20–30% attach in recipes-software subscriptions, joint stations, acceptance service ≈ **$9–17M/yr total SAM**. A winning specialist taking 30–40% of the NI-native segment: **SOM ≈ $3–6M/yr by 2032; $8–12M/yr in the bull case** (fusion Series B/C wave converts to coil-line capex faster, category C industrializes).

**Top-down triangulation:** fusion supply-chain spend $538M (2025) [DD-C12-27]; magnets are the single largest value block (~half of experimental-device value in Chinese accounting [DD-C12-28]), so magnet-related spend plausibly $100–250M/yr, of which production **equipment** capex is typically a 3–8% slice → $5–20M/yr — consistent with the bottom-up figure. Tape-side growth supports direction: ~15 vendors, >5,000 km/yr capacity, single prototypes consuming ~10,000 km-4mm [DD-C12-10][DD-C12-23], and China's project pipeline alone is projected at ~RMB 146.5B over coming years [DD-C12-30].

**Honest verdict on size: the red team is right that machines-only is a $3–8M/yr business — below venture scale.** The expansion logic that could change that: (i) recipe/QC software + per-coil data subscription across the installed base; (ii) leasing/"winding-cell-as-a-service" for startups that cannot justify capex before their Series B; (iii) forward-integration into **contract coil manufacturing** on the founder's own cells (a cell producing 100–300 qualified pancakes/yr at $3–15K value-add each yields $0.5–4M/yr per cell — better economics than selling the cell); (iv) adjacent tape-handling equipment (rewinding, Ic mapping, cabling). Even so, the credible 2035 outcome is a $20–60M/yr niche equipment+services firm, not an ASML.

## 6. Go-to-market: China-first vs US-first

**US/EU-first, China-deferred. This is one of the few candidates in the portfolio where the China angle is structurally weak rather than an asset (see §7).**

- **US/EU sequence (recommended):** (1) 2029: land one lighthouse lab (NHMFL/university stellarator program) via a subsidized first cell + publication; scientific buyers procure openly and reference loudly [DD-C12-15 analog, DD-C12-01]. (2) 2030: convert 2–3 second-wave fusion startups (category A) with the "vendor-neutral alternative to buying from your competitor's subsidiary (Ridgway/TE) or your competitor's coils (CFS)" pitch [DD-C12-19][DD-C12-22]. (3) 2031: category C industrial lines + software attach. Channel: direct founder-led sales; MT/ASC conference presence; acceptance-test partnerships with tape vendors (defect-map integration makes tape suppliers natural allies).
- **China sequence (if pursued):** only via a software/recipe licensing or JV structure, targeting industrial (non-fusion) coil producers (感应加热, 电机, MRI adjacency) where end-use is civil and documentable — e.g., the 联创-class induction-heating scale-up [DD-C12-31] and MRI magnet lines [DD-C12-29]. Direct machine exports into CAS/fusion-linked programs (BEST, CRAFT ecosystem) should be treated as unlicensable-by-default for planning purposes (§7). The founder's China network is better spent on supply chain (servo/granite/vision components at ~60–70% of Western cost) than on China revenue.

## 7. Regulatory & geopolitical exposure — **PROVISIONAL** (POLICY_BRIEF.md not yet available; to be reconciled in Phase 5)

- **The machines themselves are probably EAR99.** No CCL entry found covering conductor/coil winding machines (1B201 filament-winding controls fibrous/composite winding, not conductor coils) — provisional, snippet-level verification [DD-C12-13][DD-C12-16].
- **The machine's outputs are controlled.** Superconducting solenoidal electromagnets above NSG-derived thresholds (>2 T, L/ID>2, ID>300 mm, homogeneity <1%; NMR-system exclusion) sit in 3A201/3A001.e.3, with an April 2024 rule tying high-performance variants to 3A090-linked license requirements [DD-C12-13]. Selling **equipment and process technology whose purpose is producing controlled magnets** to Chinese fusion-linked end users triggers EAR end-use/end-user catch-alls and Entity List screening even if the tool is EAR99 — a per-deal BIS licensing exercise a solo founder should not build a revenue plan on (provisional; core of the red team's China critique, accepted).
- **China-side controls cut the other way too:** HTS wire/film manufacturing technology appears in China's Catalogue of Technologies Prohibited or Restricted from Export (reported thresholds: Tc>77 K, length>100 m, Jc>10⁴ A/cm² — snippet-verified) [DD-C12-12], and the 2026 dual-use license catalog regime (MOFCOM/GACC Announcement 91 of 2025, effective 2026-01-01) is expanding [DD-C12-11]. A China-based engineering team would complicate moving winding process tech **out** of China as much as US rules complicate moving it in.
- **Certification burden:** CE/UL machine safety only — light. No medical/nuclear certification attaches to the equipment itself.
- **Net:** structurally **US/EU-market company with Chinese component sourcing**; parallel-entry and China-first sequences are disfavored. Deemed-export exposure for hiring is low if the stack stays EAR99 (provisional).

## 8. Capital & milestones (2029 → 2032)

**Red-team objection #3 (job shop vs venture; WIP drag): accepted and designed around.** The plan below is deliberately fundable-as-a-business, not fundable-as-a-rocketship:

- **2029 H1 (found, $2.5–3.5M seed):** team of 3–4 (founder + controls engineer + mechatronics + apps engineer). Build demo cell in-house; publish tension→Rc reproducibility benchmark.
- **2029 H2–2030 H1:** 2 customer builds under **milestone-payment contracts (30/40/30)** so customer cash funds WIP (~$350–500K/machine) — the standard bespoke-machinery model [DD-C12-21]; first revenue ~9–12 months post-founding, $1.0–1.6M recognized 2030.
- **2030 H2–2031:** 4–6 cells/yr + software subscriptions ($30–60K/yr/cell) + joint stations; open a leased "coil service bay" running one in-house cell for paid pilot winding (validates foundry pivot). Revenue 2031: $3.5–5.5M, roughly breakeven at 8–10 staff.
- **2032 decision gate:** either (a) Series A ($8–15M) **only if** software/QC attach >20% of revenue and the coil-foundry bay is oversubscribed — thesis then is "coil manufacturing platform," or (b) stay bootstrapped as a profitable niche equipment firm. Both are acceptable outcomes; only (a) is venture.

Burn floor is modest: no cleanroom, ~$60–80K equipment bay fit-out, biggest cash risks are WIP timing and 12–18 month capex sales cycles (mitigated but not eliminated by milestone contracts).

## 9. Risks & kill criteria

**Risks (ranked):**
1. **Demand thinness / build-vs-buy culture** — labs self-build (KIT [DD-C12-01]), leaders integrate (Proxima [DD-C12-24]), CFS sells coils so customers skip machines entirely [DD-C12-22]. Highest-probability failure mode.
2. **Incumbent response:** Broomfield adds a REBCO/NI package; or TE/Ridgway sells externally anyway at fusion-major scale [DD-C12-19].
3. **Chinese clones** compress ASP within ~2 years of first delivery (motion+tension is commodity there; CAS already patents winding machinery [DD-C12-05]).
4. **Process fragmentation:** each customer's conductor (bare tape, MI co-wind, VIPER-class cable [DD-C12-04]) demands NRE, eroding standardization economics.
5. **Solo-founder capital-equipment shape:** field service, acceptance travel, enterprise sales — needs an ops/service co-founder by first customer build.
6. **Export-control drag** on any China revenue (§7).

**Kill criteria (pre-commitment):**
- **K1 (demand):** fewer than 3 paid commitments/LOIs from distinct non-integrated magnet builders by **mid-2030** → stop; fold skills into a magnet-maker job or pivot to C13/C33-adjacent products.
- **K2 (attach):** software+QC+service <15% of revenue by end-2031 → it is a job shop; stop raising, run for cash or sell to Broomfield/an integrator.
- **K3 (competition):** CFS/TE begin selling winding cells or per-coil manufacturing services to third parties at scale before first delivery → differentiation window closed.
- **K4 (clone price):** credible Chinese NI cell offered at <50% of ASP before 5th unit ships → exit equipment, keep software/foundry only.

## 10. Verdict

**Conviction: MEDIUM** (as a company thesis; HIGH as a founder-fit wedge). The red team's core factual attack stands — incumbents exist and the biggest buyers integrate — but two 2025–2026 developments partially rehabilitate the idea: Tokamak Energy's purchase of Ridgway removed the West's main neutral vendor [DD-C12-19], and fusion supply-chain spend keeps compounding (~$681M projected 2026) with precision-manufacturing capacity the top stated worry [DD-C12-26][DD-C12-27]. Honestly sized, this is a **$3–8M/yr equipment business with a plausible path to $20–60M/yr as an equipment+software+coil-services platform** — a strong, low-downside first company that banks the founder's rarest asset, but venture-scale only if the foundry/software layer proves out. It should rank behind pure-product candidates on upside, ahead of most on probability of reaching profitable revenue by 2031.

**Cheapest validation experiments (2026–2028, during the PhD):**
1. **Build-vs-buy interview sprint (~$3K):** 15+ structured interviews at ASC 2026 / MT-29 with magnet leads from category A/B orgs (Columbia, UW, Thea-class startups, NHMFL, KIT). Success metric: ≥3 written "would buy at $500–800K" signals. Directly tests K1 two years early.
2. **Tabletop NI benchmark rig (<$15K, no Stanford IP):** re-implement a personal winding head with inline turn-to-turn resistance estimation; wind repeated test pancakes from tape offcuts showing Rc control/predictability; publish in SUST/IEEE TAS. Establishes the "NI process control" flag the incumbents lack [DD-C12-02][DD-C12-17].
3. **Sell the software layer first ($0 hardware):** license a winding-recipe/QC data tool to 1–2 robot-cell labs (KIT-style [DD-C12-01]) as a $10–25K paid pilot. If labs won't pay even for the process layer, the bundle thesis — the only venture path — dies cheaply.

**Kill criteria:** K1–K4 above, with K1 (three paid commitments by mid-2030) as the governing gate.
