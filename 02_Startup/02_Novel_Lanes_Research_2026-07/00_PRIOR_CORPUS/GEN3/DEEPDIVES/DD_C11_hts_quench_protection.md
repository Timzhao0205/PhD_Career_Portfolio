# DD_C11 — Fast Solid-State HTS Quench-Protection Switch & Dump Modules

**Candidate:** C11 · **Phase 3 rank:** 3 (86.8, red-team-adjusted downward) · **Red team kill probability:** ~70%
**Sources:** `DD_C11_sources.json` (24 unique; cited as [DD-C11-##])

> **Scope note (red-team resolution up front).** This deep dive accepts the red team's core physics
> objection and **re-scopes the product**. The as-pitched "sub-millisecond kA-class dump switch" is
> not a coherent product: dump speed is capped by coil insulation voltage (V = L·dI/dt), which is
> why ITER extracts 41 GJ from its TF coils over "about half a minute" through mechanical breakers
> into dump resistors at ≤10 kV [DD-C11-01], and DEMO studies assume τ ≈ 35 s discharges
> [DD-C11-02]. The scarce thing in HTS protection is **detection and decision**, not interruption
> [DD-C11-06]. The honest product is therefore a **detection-integrated magnet protection &
> management unit (MPMU)** for 0.5–20 kA-class HTS systems — multi-modal quench detection frontend,
> decision firmware, and a modest (ms-class, ≤5 kV) hybrid extraction stage — aimed at the
> **non-fusion tier** (industrial magnet OEMs, lab/NMR magnets, dry MRI, SMES pilots) where
> in-house protection teams do not exist. Fusion integrators are treated as a tender-revenue
> adjacency, not the beachhead.

---

## 1. Problem & who has it

**The physics problem.** REBCO HTS magnets quench rarely but catastrophically: normal-zone
propagation is orders of magnitude slower than in LTS (cm/s-class), so a local hotspot can reach
destructive temperature before a measurable resistive voltage appears; Marchevsky's review states
plainly that "traditional voltage-based quench detection schemes may be ineffective" for HTS
[DD-C11-06]. The MIT/CFS/CERN VIPER work at SULTAN was motivated by exactly this: fusion-relevant
environments add electromagnetic noise, inductive coupling, and disruption transients that defeat
voltage taps, pushing the field toward fiber-optic and other non-voltage sensing [DD-C11-07].

**Who actually has the problem, by tier:**

- **Tier A — fusion integrators (CFS, Tokamak Energy, ASIPP/BEST, STEP):** have the problem *and*
  in-house teams plus IP. Tokamak Energy holds granted US patents both on quench protection by
  deliberately quenchable dump sections [DD-C11-08] and on partial-insulation windings with
  built-in diagnostic pickup coils [DD-C11-09]. ASIPP designs and tests its own 100 kA
  quench-protection breakers for CRAFT [DD-C11-13][DD-C11-14]. These are not product customers for
  the safety case — but they **do procure the hardware**: ASIPP issued a public tender in
  September 2025 for a "100 kA 失超保护主开关定型产品" — a *productized* quench-protection main
  switch (bypass switch + vacuum breaker for TF magnet testing) [DD-C11-15]. The buy/build line
  runs between *safety architecture* (kept in-house) and *qualified switching/detection hardware*
  (bought).
- **Tier B — industrial HTS OEMs without protection teams:** 联创超导 (Lianchuang Superconductor,
  Jiangxi) sells MW-class HTS induction heaters and magnet-assisted CZ-silicon furnaces; cumulative
  orders from a single customer (宁夏旭樱) reached ~¥573M (¥95M in 09/2023 + ¥478M in 12/2023,
  100+ units), with magnet capacity planned to grow from ~100/yr toward 1,600/yr by 2027
  [DD-C11-18]. Every unit contains an HTS magnet whose protection/monitoring electronics are not
  the OEM's core competence.
- **Tier C — MRI/NMR/lab magnets:** Ningbo 健信超导 (Jianxin), the world's largest *independent*
  MRI superconducting magnet supplier (global #5, ~4.2% share by installations; 2025 revenue
  ¥577M, +36% YoY; customers include GE, Philips, Siemens, United Imaging) is moving to
  conduction-cooled helium-free magnets [DD-C11-17]; Philips has >2,000 sealed BlueSeal 1.5 T
  magnets installed with only 7 L of enclosed helium [DD-C11-21]. Sealed, helium-free magnets
  cannot vent a quench into boil-off — thermal/energy management during a quench becomes an
  electronics problem, not a plumbing problem.
- **Tier D — the coming 1–20 kA "mid-market":** REBCO tape supply is scaling an order of
  magnitude (Shanghai Superconductor: ~4,000 km/yr today, ¥2.5B new base targeting ≥15,000 km/yr
  within 2–3 years, explicitly citing fusion-driven demand) [DD-C11-19]; fusion supply-chain
  spending hit $434M in 2024, +73% YoY [DD-C11-20]. More tape means more magnets built by teams
  that have never quenched one.

---

## 2. Product definition & the extreme-performance edge

**MPMU — Magnet Protection & Management Unit** (rack or skid, per-magnet):

1. **Detection frontend (the differentiated part):** simultaneous voltage-tap bridge, Hall-array
   current-distribution sensing, and an interrogator channel for fiber (FBG/Rayleigh) sensors;
   fusion-grade common-mode rejection. Detection, not switching, is the acknowledged open problem
   [DD-C11-06][DD-C11-07] — the founder's precision-instrumentation and Hall-sensor background
   attacks exactly this.
2. **Decision firmware:** magnet-specific quench models, current-sharing/contact-resistance
   estimation for NI/MI coils, trip logic with audit logging (the "safety-PLC" layer).
3. **Extraction stage (the commodity part, honestly specified):** hybrid mechanical-bypass +
   solid-state commutation, 0.5–20 kA, ≤5 kV, **millisecond-class opening into a sized dump
   resistor — not sub-ms, not GJ-class**. For comparison: ITER-class FDUs are 70 kA/10 kV
   room-sized systems with counter-pulse vacuum breakers and pyrobreaker backup [DD-C11-01];
   CRAFT's is 100 kA/10 kV with thyristor commutation [DD-C11-13][DD-C11-14]. The MPMU deliberately
   sits two orders of magnitude below, where no packaged product exists.
4. **NI/MI magnet-management mode:** for "self-protecting" coils, the same hardware manages what NI
   coils actually suffer from — long charging delays, ramp losses, screening-current field error,
   and uneven current distribution. The 31.4 T LNI coil study shows NI protection is a *narrow
   engineered window* (contact resistivity 10,000 µΩ·cm² survived at 330 K peak / 718 MPa hoop
   stress; 70 µΩ·cm² would have hit 1,398 MPa — i.e., destruction), "careful engineering… rather
   than inherent immunity" [DD-C11-03]. Managing that window in operation is an electronics and
   estimation problem — a new category, not a dead one.

**Edge claims (quantified, defensible):** detect current-sharing onset 5–10× earlier than voltage
taps via multi-modal fusion (benchmark to be established — this is the PhD-years experiment);
one-box integration at 1/5 the engineering cost of a bespoke lab protection rack; qualified
recipes for NI/MI/insulated coils. **Explicitly renounced claim:** "sub-ms dump of large magnets"
— physics-capped by insulation voltage [DD-C11-01][DD-C11-02].

---

## 3. Technical feasibility & TRL path (2029–2031)

- **Buyable:** press-pack IGBTs/IGCTs and thyristor stacks (commodity — CRAFT's 100 kA/10 kV
  thyristor stack is published engineering, not magic [DD-C11-13]); vacuum interrupters (24 kV /
  20 kA-class interrupters are catalog items; Scibreak's prototype used a 24 kV/1,600 A VI with a
  Thomson-coil actuator opening in <1 ms [DD-C11-12]); fiber interrogators; dump resistors.
- **Must be built:** the analog frontend (µV-class quench signatures on kV common-mode), the
  detection/decision firmware and magnet models, the hybrid commutation control, and the
  qualification data package. No cleanroom anywhere.
- **Hard parts:** (i) proving detection latency claims on real coils — requires access to magnets,
  not a bench; mitigated because the founder can wind small NI test coils himself; (ii) a kA-class
  cryogenic test campaign for the extraction stage — realistically a **partner-lab problem**
  (national lab or OEM co-development), $200–500K of test time, not the $1M+ owned test stand the
  red team priced, *because the extraction stage is de-rated to ≤20 kA/≤5 kV*; (iii) functional
  safety documentation (IEC 61508-informed) — a real cost (~1 engineer-year), but at component
  level the *integrator* owns the system safety case, as with any purchased breaker (ASIPP's
  tender shows precisely this division [DD-C11-15]).
- **TRL path:** bench MPMU with detection on founder-wound NI coils by 2027 (TRL 4); pilot on one
  OEM magnet by 2029 (TRL 6); qualified v1 shipping 2030–31. 24–30 months post-founding to first
  qualified unit — slower than the one-pager's 18–24 months claim.

---

## 4. Competitive landscape (global and China)

**Fast DC interruption (adjacent, above):** Mitsubishi Electric wholly acquired Scibreak (2023) to
commercialize VARC fast DC breakers for HVDC [DD-C11-11]; the technology scales to ±200 kV via
series modules [DD-C11-12]. ABB/Hitachi/Eaton hybrid breakers similarly target grid fault
current, not cryogenic magnet protection with detection integration. They cap any "we'll own fast
DC switching" expansion story; they do not currently sell magnet MPMUs.

**Fusion in-house/IP (above):** Tokamak Energy patents protection methods and partial-insulation
diagnostics [DD-C11-08][DD-C11-09]; Oxford Sigma + STEP Fusion + Strathclyde demonstrated a
magnet-protection "safety valve" for STEP TF coils (announced 2026-02) [DD-C11-10]; ASIPP
publishes its own 100 kA QPS designs and tests [DD-C11-13][DD-C11-14]. Fusion protection
*architecture* is occupied territory.

**Lab-magnet incumbents (below, and the most sobering signal):** Cryomagnetics ships magnets
"fully protected against damage due to quench" and its Model 4G-100 power supply includes
"automatic quench detection and protection" **as a standard built-in feature** [DD-C11-22] —
i.e., in the legacy LTS lab segment, protection is bundled at effectively zero marginal price.
Any MPMU must be sold on HTS-specific capability the bundled logic lacks.

**China (Chinese-language findings):**
- **ASIPP (合肥等离子体所)** is both competitor and customer: in-house QPS R&D
  [DD-C11-13][DD-C11-14], but public tenders for productized 100 kA main switches (09/2025)
  [DD-C11-15] — Chinese switchgear firms win these; award prices were not published in the tender
  document fetched.
- **Chinese patent activity** extends beyond ASIPP: e.g., CN111541222A (南京工程学院, filed 2020,
  granted 2022) claims a hybrid multi-branch quench-protection switch topology for
  CFETR-class magnet power supplies [DD-C11-16] — evidence of an active domestic ecosystem that
  would contest any China-first entry on price.
- **联创超导** integrates magnets into industrial systems and is capacity-constrained on magnets,
  not electronics [DD-C11-18] — a plausible first OEM customer rather than competitor.
- **健信超导 / 辰光医疗 (MRI)** vertically integrate magnet + cryogenics; protection electronics
  are internal today, but the helium-free transition [DD-C11-17][DD-C11-21] reopens the make/buy
  question at exactly MPMU's price point.
- **上海超导** (tape) is upstream, not competing [DD-C11-19].

**Pricing signals:** ITER/CRAFT-class FDU/QPS units are program-priced (single-digit $M per lot,
inferred from system scale [DD-C11-01][DD-C11-13] — no public unit price found; flagged as
uncertainty). Lab-segment bundling implies $0–10K perceived value there [DD-C11-22]. The
defensible MPMU price window is $20–80K/system for industrial/scientific HTS, asserted from
component-cost + value analysis, **not from an observed transaction — this remains the single
weakest number in the thesis.**

---

## 5. Market sizing (bottom-up beachhead, then triangulation)

**Beachhead = protection/management electronics for non-fusion HTS magnet systems, 0.5–20 kA.**

*Segment B — China industrial HTS OEM systems.* Lianchuang alone: ~100 magnets/yr capacity (2024)
→ planned 1,600/yr (2027) [DD-C11-18]. Assume China-wide realized shipments of 300–800 HTS
industrial systems/yr by 2030 (plan-discounted 50–80%) × $15–40K MPMU content =
**$4.5M–32M/yr** (mid ~$13M).

*Segment C — lab/scientific HTS magnets.* Tape supply supports the volume: 15,000 km/yr from one
vendor [DD-C11-19] at 2–20 km/magnet ⇒ capacity for ~750–7,500 magnets/yr; assume 250–500
non-fusion scientific/NMR HTS systems/yr globally by 2030, of which 40–60% are built by teams
without protection capability, × $15–50K = **$1.5M–15M/yr** (mid ~$6M).

*Segment D — dry MRI quench-management content.* If 1,000–3,000 conduction-cooled/sealed magnets
ship per year industry-wide by 2030 (Philips's installed base alone is >2,000 units of BlueSeal
1.5 T accumulated since 2018 [DD-C11-21]; Jianxin is ramping helium-free lines [DD-C11-17]) ×
$3–10K OEM content = **$3M–30M/yr**, gated by 3–5-year OEM design-in cycles.

*Segment A — big-science/fusion tenders.* FIA-surveyed supply-chain spend $434M (2024), +25%
expected 2025 [DD-C11-20]; QPS/switch tenders (ASIPP-style [DD-C11-15]) perhaps 5–15 lots/yr
globally at $0.3–3M = **$3M–20M/yr**, incumbent- and guanxi-dominated.

**Bottom-up TAM 2030 ≈ $12M–97M/yr (mid ~$45M/yr).** Top-down check: protection/management
electronics ≈ 2–5% of HTS magnet-system value; if global HTS magnet systems reach $1.5–3B/yr by
2030 (consistent with tape scaling [DD-C11-19] and fusion supply-chain trajectory [DD-C11-20]),
TAM = $30–150M/yr — the two methods agree on a **sub-$150M/yr category**. SAM (non-fusion,
addressable by a small vendor) ≈ $15–40M/yr; **SOM 2032 ≈ $1.5–4M revenue** (20–40 industrial/lab
units + 1–2 tender wins). This is a product line, not a venture-scale company — the honest
number, stated plainly.

---

## 6. Go-to-market

**China-first sequence:** OEM co-development with a Lianchuang-class industrial integrator
(protection/monitoring as their spec differentiator; they carry the system safety case); then bid
ASIPP/CRAFT/BEST component tenders — the 2025 tender proves the procurement channel exists
[DD-C11-15] — then MRI OEM design-ins (Jianxin et al. [DD-C11-17]). Risk: domestic patent/vendor
ecosystem [DD-C11-16] plus price competition compress margins; a US-person founder selling
protection electronics into Chinese *fusion* programs sits near dual-use tripwires (§7).

**US sequence:** start with national-lab and university magnet groups (MDP-adjacent) as reference
users of the detection frontend; sell MPMUs to the second wave of US HTS entrants (motor, SMES,
compact-NMR startups) who have no protection staff; stay out of CFS/TE's architecture lane and
sell them, at most, qualified hardware.

**Which leads:** **US-led, China-parallel-via-OEM** — inverted from the one-pager. Rationale: the
differentiated layer (detection instrumentation + firmware) earns reference credibility in US/EU
labs, while China is where the unit volume (industrial magnets) lives; a China-first safety
product from a solo US-trained founder faces both trust and export-control friction. Channel:
direct + co-development contracts; the realistic analogy is a qualified Tier-2 component supplier
in big science, not a category-owning platform.

---

## 7. Regulatory & geopolitical exposure — **provisional (no Phase 5 brief available at write time)**

- **US export controls:** superconducting electromagnets fall under ECCN 3A001.e.3 / 3A201 (NP/AT
  reasons; MRI-embedded magnets carved out), and superconductive composite conductors >100 m under
  1C005 (NS/AT) [DD-C11-23]. Protection *electronics* per se are likely EAR99 or 3A001-adjacent,
  but anything marketed for fusion magnets sold into China invites case-by-case scrutiny, and
  ASIPP-affiliated entities have appeared in US restricted-party actions in recent years (status
  must be re-verified at Phase 5 — **do not rely on this sentence**).
- **Deemed export / US-person issues:** firmware and designs shared with a Chinese OEM
  co-development team may constitute controlled technology transfer; structure China activity as
  sale of finished goods, not engineering services, pending Phase 5.
- **Certification burden:** industrial (CE/GB) manageable; MRI OEM content drags the product into
  IEC 60601 supplier-quality territory (12–24 months); functional-safety expectations
  (IEC 61508-informed) add ~1 engineer-year of documentation.
- **China direction:** superconducting materials/applications enjoy plan-level support (tape
  expansion is government-celebrated [DD-C11-19]), meaning import substitution will be *fast* —
  a foreign-flavored vendor's window in China closes within a few years of proving the category.

---

## 8. Capital & milestones (2029→2032)

- **2029 H2 (found, pre-seed $0.75–1.5M):** MPMU detection frontend + firmware on founder-wound NI
  coils; publish latency benchmark vs voltage taps; 2 paid pilot agreements. Burn ~$45K/mo
  (founder + 1 engineer + parts).
- **2030 (seed $2.5–4M):** hybrid extraction stage validated at partner lab (≤10 kA, ≤5 kV);
  first industrial OEM pilot install (China via OEM or US lab); functional-safety file v1.
  **First revenue 2030 H2: pilots $100–300K.**
- **2031:** qualified v1; 8–15 units + 1 tender win; revenue $0.8–1.5M; team of 5–6.
- **2032 (Series A only if category expands):** $2.5–4M revenue. **Honest fork:** at this scale a
  standalone MPMU company does not clear venture thresholds; the natural move is merging the line
  into a broader HTS magnet-electronics/equipment play (C10 power supplies / C12 winding
  machines), where MPMU becomes the margin-rich attach product. Total capital to the fork:
  $4–6M — inside deep-tech seed norms.

---

## 9. Risks & kill criteria

**Risks (ranked):**
1. **No standalone buyer** — protection stays bundled (lab segment already bundles it free
   [DD-C11-22]) or in-house (fusion [DD-C11-08][DD-C11-13]); MPMU collapses into a feature of
   someone else's power supply. *Likelihood: high. This is the top risk.*
2. **Category ceiling** — even at full success, TAM < $150M/yr (§5); venture-scale requires the
   C10/C12 merger, at which point C11 was never really a company.
3. **NI/MI absorption** — if NI magnet management proves to be pure firmware on existing PSU
   hardware, the hardware ASP evaporates; conversely Tokamak-Energy-style patents [DD-C11-08]
   [DD-C11-09] fence the cleverest methods.
4. **Qualification drag** — safety-adjacent sales cycles (12–36 months) outlast a solo founder's
   runway; a credible functional-safety co-founder/hire is effectively mandatory.
5. **China squeeze** — domestic patents [DD-C11-16] + tender localization close the China channel
   faster than OEM relationships open it; export-control friction (§7) works the other direction.

**Kill criteria (binding):**
- By **end-2027**: fewer than 2 non-fusion HTS OEMs/labs express concrete willingness to pay
  ≥$20K for a third-party detection+protection unit (LOI or paid pilot) → kill standalone thesis.
- By **end-2028**: detection benchmark shows <3× latency advantage over tuned voltage-tap bridges
  on NI/MI coils → the differentiated layer is not differentiated; kill.
- Any point: an incumbent PSU vendor (Cryomagnetics-class, or a Chinese equivalent) ships
  HTS-specific multi-modal quench management as a bundled feature → kill; or Mitsubishi/ABB
  announces a magnet-class protection product line → kill.
- 2029 gate: no partner lab secured for kA-class extraction-stage validation at <$500K → descope
  to detection-only instrument (which then belongs to the capped diagnostics quota, weakening
  portfolio fit).

---

## 10. Verdict

**Conviction: LOW as pitched; MEDIUM-LOW after re-scoping.** The red team's objections mostly
stand: sub-ms GJ dumps are physics theater [DD-C11-01][DD-C11-02]; fusion integrators own
protection architecture as IP [DD-C11-08][DD-C11-10][DD-C11-13]; fast DC interruption belongs to
Mitsubishi/Scibreak-class incumbents [DD-C11-11][DD-C11-12]. What survives is real but small: a
detection-first magnet protection & management unit for the non-fusion 0.5–20 kA HTS wave, with
the ASIPP tender [DD-C11-15] proving hardware does get bought and NI physics [DD-C11-03] proving
"self-protecting" coils still need management electronics. But bottom-up sizing caps the category
under ~$150M/yr — **C11 should not be Tim's company; it should be a product line inside C10/C12**
(HTS magnet electronics / winding equipment), where it adds margin and customer lock-in.

**Cheapest validation experiments (2026–2028, during the PhD):**
1. **WTP probe (~$3K, conference travel):** 10 structured conversations at ASC/MT/EUCAS with
   non-fusion HTS OEMs and lab magnet groups (Lianchuang-type, Jianxin-type, AMI/Cryomagnetics,
   university NMR): "would you pay $20–80K for qualified third-party quench detection +
   extraction?" Count LOIs, not compliments.
2. **Detection benchmark (~$15–25K, fits PhD lab access):** wind two small NI REBCO coils (he owns
   this skill), instrument with voltage taps + Hall array + fiber, induce controlled quenches at
   77 K, publish detection-latency comparison. This de-risks the only differentiated claim and is
   publishable regardless of the startup decision.
3. **Tender forensics (~$0):** track ASIPP/CRAFT/BEST 招标/中标 records for 12 months
   [DD-C11-15]-style; extract winners, award prices, and spec drift — turns the asserted ASP into
   an observed one and maps the Chinese competitor set for free.
