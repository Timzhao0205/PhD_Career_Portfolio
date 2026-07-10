# Fable-5 Gate Record — CF-7 "Conduction-Cooled Lead/Termination Co-Qual"

**models=GATE:fable-5** (intended, all three gates) · effort=high · date=2026-07-10
**Candidate:** current-lead + termination assembly for a cryogen-free (cryocooler-only)
HTS magnet that ships "born-qualified": each production unit carries an integrated,
matched acceptance-test record co-verifying heat-leak (W) AND joint/contact resistance
(Ω / nΩ·cm²) as one unit-specific record.

> **Drafting/analysis aid only — registered patent attorney review required before any
> filing, disclosure, or reliance. This record authorizes nothing.**

---

## Hard-rule screens (CLAUDE.md Rules 1–3)

- **Prong-a (Rule 1):** CF-7's core is current-lead/termination thermal+electrical
  acceptance testing for conduction-cooled magnets. No overlap with HSX plasma
  diagnostics, GaN/AlGaN Hall devices, or battery magnetic imaging. **Hall-sensing
  adjacency check: NONE** — the instrumented-lead embodiments discussed below use
  voltage taps and thermometry, not magnetic/Hall sensing. Constraint recorded: if any
  future embodiment adds magnetic-field sensing to the lead, re-screen before drafting.
- **Rule 2 (no GaN):** clean.
- **Rule 3 (no "stellarator"):** clean. ITER/fusion references in the IDS_pool are
  third-party art and permissible; patent-facing framing stays "conduction-cooled /
  cryogen-free HTS magnet current leads."

---

## G-PHYS — Physics correctness

**Verdict: PASS**, with two binding conditions carried forward.

**Reasoning.** CF-7 claims no new physical effect; it is an engineering/manufacturing-
process concept resting entirely on established measurement physics:

1. Conductive heat leak of a current lead into a cryocooler-anchored cold mass is a
   standard, well-modeled quantity (Wiedemann–Franz-limited optimization; benchmark
   figures ~47 W/kA at 4.2 K for optimized conduction-cooled leads per Ballarino,
   ledger T3-4; numerical models per T3-5, T3-7). Measurable per unit by calorimetry
   or by temperature-gradient inference at a calibrated thermal anchor.
2. Joint/contact resistance at nΩ-class levels is routinely measured per unit
   (four-wire under transport current; ledger T3-8, T3-9, T3-10, US7,394,024).
3. The two quantities are physically coupled, which *strengthens* rather than
   undermines the co-verification rationale: joint Joule heating (I²·Rj) lands in the
   same cryocooler lift budget as conductive heat leak, so in a cryogen-free system
   the total per-lead thermal burden is only known when both are measured on the same
   physical unit. No sign, units, conservation, or boundary-condition incoherence.
   The CF-1 starter's known tau↔Rc inversion is irrelevant here (no shared code path;
   no CF-7 sim exists at all).

**One real physical subtlety (must be resolved in drafting, not a KILL):** the two
measurements interfere. Joint-resistance measurement requires transport current, whose
self-heating perturbs a simultaneous heat-leak measurement. A "co-verified as one
unit" record is only coherent if the record's schema defines the measurement states —
e.g., (a) zero-current conductive heat leak, (b) joint resistance at rated current,
(c) optionally total heat load under rated current, with (c) ≈ (a) + I²·Rj as an
internal consistency check. This is enabling detail, and the (c)-vs-(a)+(b) closure
check is itself a physically meaningful co-verification feature.

**Binding conditions:**
- **C1 (W2 gap, logged):** No dedicated CF-7 simulation was built in W2. None is
  required for the process/article claim to pass G-PHYS — the physics is textbook.
  HOWEVER: any prophetic numeric example in the W4 disclosure, and ANY parameter-
  window claim (design-around ladder rung 5), REQUIRES a minimal lead model first
  (1-D conduction-cooled lead heat-load model per T3-5/T3-7, plus the I²·Rj closure
  budget vs. cryocooler load line). This is a REVISE-condition on those specific
  outputs, not on the candidate. Do not fabricate numbers without it.
- **C2:** The disclosure must specify the measurement states per C1's subtlety above
  (zero-current vs. under-load), with units and traceability, per Rule 6.

---

## G-NOVEL — Novelty across US + CN + JP + KR + EU

**Verdict: NARROW-NOVEL.**

**What is old (the genus is dead):**

1. **Combined thermal + electrical qualification testing of one HTS current-lead unit
   is anticipated by NPL.** ASIPP/CASIPP: the 68 kA ITER lead cold-performance
   campaigns (T3-1/T3-2/T3-3, Fusion Eng. Design / Cryogenics, CN institution,
   worldwide printed-publication effect) and, decisively, the 13 kA lead paper
   (S2-11, Cryogenics 2022) reporting a Nov-2020 acceptance-test sequence on ONE
   physical unit combining steady-state thermal, LOFA, joint-resistance, pulse, and
   insulation tests. A method claim on "test both heat leak and joint resistance on
   the same current lead before acceptance" is anticipated or at minimum hopelessly
   obvious over these. **Blocking refs: S2-11 + T3-1 (NPL, CN-origin, blocks in all
   five jurisdictions as prior art).**
2. **The electrical half alone:** US7,394,024 B2 (Chubu/Dowa, US, expired) —
   quantified per-lead contact-resistance acceptance measurement (0.28 Ω @ 77 K,
   0.2 Ω @ 4.2 K, to 1060 A). Blocks patentability of that half; being expired, no FTO
   issue. Joint-resistance QC as an institutionalized discipline: SELFIE (T3-10,
   CEA/EU), soldered-joint QC (T3-9).
3. **The thermal half alone:** CN101409127B (CN) — numeric heat-leak spec
   (<0.2 W/kA to 5 K) engineered into an HTS lead shunt; plus decades of heat-leak-
   specified lead design (US4,394,634; US4,930,318; US5,742,217; T3-4).

**The claimed distinction, adjudicated honestly.** "Research campaign runs both tests
on a prototype/mock-up" vs. "every production unit SHIPS with a matched per-unit
co-verified acceptance record" is a REAL factual distinction (ITER qualified mock-ups
to release a series-production process; nothing found discloses a per-shipped-unit
matched thermal+electrical record as a product feature). But **standing alone it is a
distinction without legal teeth**, for two reasons:
- *Obviousness (all five jurisdictions):* per-unit factory acceptance testing (FAT)
  is universal manufacturing practice; applying the ASIPP combined test protocol to
  each production unit instead of one prototype is the sort of routine-QC scaling an
  examiner (and CNIPA in particular, with its strict inventive-step practice) will
  reject as obvious with no technical problem solved.
- *Printed-matter / non-technical-feature doctrine:* "ships with a record" is
  informational content with no functional relationship to the article. US printed-
  matter doctrine, EPO non-technical-feature analysis, and CN Art. 22.3 all discount
  it unless the record does something.

**What survives (the narrow combination):** a conduction-cooled lead/termination
assembly with (i) built-in per-unit verification structures (permanent voltage taps
spanning each joint; thermometric reference stations at each thermal anchor) that make
economical per-unit co-measurement possible, and/or (ii) a system in which the
unit-specific certified heat-leak and joint-resistance values are machine-readable and
CONSUMED by the cryogenic system controller to allocate cryocooler lift budget /
operating margin (functional relationship → defeats printed-matter; composes with
CF-4's ramp governor). Nothing in the 42-citation ledger discloses that combination.

**FTO (distinct from patentability):**
- **US11,961,662 B2 / US12,537,121 B2 (GE Precision Healthcare, ACTIVE, continuation
  granted 2026-01-27, family still in prosecution):** in-force claims on
  additively-manufactured lead heat-exchanger construction. CF-7 embodiments must not
  read on that manufacturing method; design around by claiming test/record/controller
  features, not heat-exchanger fabrication. Watch the open continuation.
- **US10,511,168 (IBM, "intelligent current lead"):** MANDATORY full-text pull before
  any instrumented-lead embodiment is drafted — if it claims integrated sensing/
  monitoring tied to lead operation, it threatens embodiment (i)/(ii) above. This is
  the single largest unresolved risk to the surviving core.
- US7,394,024 and all pre-2006 US art: expired — patentability-blocking only.
- Cross-candidate: US5,260,266 A (GE, expired) overlaps CF-6, not CF-7's core;
  W5 self-collision check stands as flagged in the ledger.

**Reliance caveats:** T3-1/S2-11 were adjudicated from abstracts (full text not
pulled, per ledger Section 6); if their full text shows per-unit series-production
acceptance records rather than prototype-campaign records, the surviving core narrows
to embodiment (ii) only. Harvest used Google-Patents-mirror proxy access (no direct
CNIPA/J-PlatPat/KIPRIS/Espacenet); a direct-database refresh plus the IBM full-text
pull are REQUIRED before filing-relevant reliance on this verdict. Duty of candor:
every reference named here is already in the CF-7 IDS_pool and stays there.

---

## G-CLAIM — Survivability and shaping

**Surviving claim core (one sentence):** A conduction-cooled HTS current-lead/
termination assembly having integrated per-unit verification structures (permanent
joint-spanning voltage taps and calibrated thermal-anchor thermometry) and an
associated unit-specific, machine-readable co-verified heat-leak + joint-resistance
acceptance record whose certified values are consumed by the cryogenic system
controller to allocate the cryocooler's limited lift budget.

**Design-around ladder walk:**

1. **Combination/system (STRONGEST — recommended):** assembly + record + controller
   that ingests the certified per-lead values to set ramp/current/margin limits
   against measured cryocooler headroom. Distinguishes ASIPP (their record went into
   a report, not a control loop) and defeats printed-matter via functional relation.
   Natural CF-4 composition.
2. **Different mechanism:** single-fixture co-measurement in which one calorimetric
   measurement under rated current yields BOTH quantities — joint resistance extracted
   from the Joule component, conductive leak from the zero-current baseline, with the
   (total ≈ leak + I²·Rj) closure as the acceptance criterion. Genuinely different
   from ASIPP's sequential test items; good method claim, but methods are weaker to
   enforce (factory-internal infringement).
3. **Enabling sub-solution:** the built-in tap/thermometry structures that collapse
   per-unit co-qual test time/cost enough to make 100% FAT economical (vs. ASIPP-style
   instrumented one-off rigs). Structural, per-unit, inspectable on the shipped
   article — the best pure-apparatus rung. **Contingent on the IBM US10,511,168
   full-text clearing.**
4. **Architecture/topology:** demountable lead cartridge with a calibrated,
   registration-controlled thermal interface such that the factory-certified heat-leak
   value survives field installation within a stated tolerance. This attacks a real,
   undisclosed engineering gap (factory heat-leak certs are otherwise voided by the
   field-made thermal joint — cf. US4,876,413's interface-conductance sensitivity) and
   may be the strongest actual invention in CF-7; develop as a co-equal independent
   claim in W4.
5. **Parameter windows: BLOCKED** pending G-PHYS condition C1 (no sim, no criticality
   evidence — do not draft).
6. **Application-field:** "cryogen-free / cryocooler-only, no cryogen bath" as a
   dependent limitation everywhere (honest CF relevance + CN utility-model utility);
   too weak to carry an independent claim.

**Recommended adjustment (grant odds × commercial scope):** draft the independent
apparatus claim at rung 3 (integrated verification structures + associated
unit-specific co-verified record) with rung 1's controller-consumption combination as
the lead system claim and rung 4 as a second independent apparatus claim; rungs 2 and
6 as method/dependent fallbacks written into the spec now (no new matter later).
**Cost in scope:** surrenders the broad genus — a competitor may lawfully ship leads
with a co-qual paper certificate but WITHOUT integrated verification structures or
controller consumption of the record. That is the price of the ASIPP art; the retained
scope still covers the C12 leads product's actual differentiator (born-qualified units
whose certs are load-bearing in a lift-budget-limited cryogen-free system).

**Pre-drafting REQUIREMENTS carried to W4:** (a) IBM US10,511,168 full-text pull;
(b) T3-1/S2-11 full-text pull; (c) minimal CF-7 lead model per G-PHYS C1 before any
prophetic example; (d) GE active-family (US11,961,662/US12,537,121) claim charts for
FTO on any heat-exchanger-bearing embodiment.

---

## Model-verification caveat (mandatory)

Intended model for all three gates: **models=GATE:fable-5**, effort=high. The
actually-served model is NOT verifiable from inside this session — Anthropic
safeguards may transparently route some Fable-5 queries to Opus 4.8, and a Fable
self-report is not proof of which model ran. Before any filing-relevant reliance on
these verdicts, confirm the served model against the external transcript at
`%USERPROFILE%\.claude\projects\`.

---

**Summary line:** G-PHYS=PASS (conditions C1/C2) · G-NOVEL=NARROW-NOVEL (genus dead
over ASIPP S2-11/T3-1 + US7,394,024 + CN101409127B; narrow combination survives) ·
G-CLAIM=core survives at rung 3+1 with rung 4 co-equal; parameter windows blocked
pending sim. Registered patent attorney review required; no filing authorized.
