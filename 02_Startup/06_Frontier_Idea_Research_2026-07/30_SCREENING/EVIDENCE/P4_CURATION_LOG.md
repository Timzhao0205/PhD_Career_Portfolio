# P4 Source-Ledger Curation Log

Analyst: P4 curation agent (Sonnet 5, high effort). Date: 2026-07-13.
Scope: the 13 P4 group ledgers (`30_SCREENING/EVIDENCE/P4-G01..G13_sources.json`) only. No pre-P4
atlas record (`Lxx-xxx`) was touched.

## Method note (read before the line items)

Before editing, every one of the 63 P4 idea evidence files (`30_SCREENING/EVIDENCE/P3R2-*.md`) was
read in full and cross-referenced against the 30 Step-2 tier-upgrade candidates and 185 Step-3
context-citation candidates identified by a scripted scan of the 13 ledgers. The honest finding:
these evidence files were authored with each source cited once for a specific, distinct micro-fact
(a named competitor's spec, a unique risk finding, a specific corroborating number) rather than with
redundant/duplicate citations. Under the task's own KEEP test (sole support for a claim, OR
competitor-primary source, OR one of the idea's two 2030-timing sources), the large majority of the
185 Step-3 candidates clear KEEP honestly. Only four records were found to be genuinely
contextual/duplicative under the DEMOTE test as literally specified (co-supported by a T1 source for
the same claim, or a vendor-marketing/trade-press restatement of a fact established elsewhere). This
is reported plainly in the final status rather than forced to a target count.

## Step 1 — fetch repair (8 records, in P4-G01 and P4-G05)

- `P3R2-A-05-S03` (DOE Build America Buy America page): WebFetched successfully; page fully supports
  the recorded domestic-content/waiver claim. Set `fetched: true`; locator updated to cite the
  specific fetched sentences (55% threshold, waiver review process). Tier T1 unchanged, accepted.
- `P3R2-A-10-S02` (Baker McKenzie blog on the Dec 2024 BIS rule): WebFetched successfully; page
  confirms the "140 new entities" and AMEC/CSMC/HHGrace VEU-removal facts but does **not** itself
  name NAURA or Piotech (two further targeted re-fetches confirmed no such text on the page). Set
  `fetched: true`, claim_supported narrowed to only what this page actually supports. Also demoted in
  Step 3 (see below) as duplicative of T1 source `P3R2-A-10-S01` (Federal Register, 89 FR 96830) for
  the same Entity List/VEU event.
- `P3R2-A-10-S03` (EE Times, VEU-revocation article): three independent WebFetch attempts all timed
  out (60s each). Per the fetch-repair rule, set `accepted: false`, `rejection_reason: "inaccessible;
  cannot verify -- logged as rejected per claim discipline"`. Removed one record from the P4 accepted
  count (300 -> 299 before Step 3).
- `P3R2-A-10-S04` (Impedans Semion RFEA datasheet): WebFetched successfully; page confirms the
  multi-sensor RFEA/ion-flux claim verbatim. Set `fetched: true`; locator updated.
- `P3R2-A-11-S02` (HORIBA D700MG product page): WebFetched successfully, but the page contradicts the
  originally recorded claim -- it advertises "100ms Step-up Response," not the "~1 second settling"
  figure the record attributed to it (that figure likely belongs to a different HORIBA product page,
  SEC-Z700X/Z500X, not this URL). Set `fetched: true`; claim_supported rewritten to state only what
  this specific page shows, and flagged that the idea's "~10x gap vs. HORIBA" competitive claim needs
  independent re-verification against the correct product line before being relied on for scoring.
- `P3R2-A-11-S03` (Brooks Instrument AMF Series press release): WebFetched successfully; confirms
  launch date, footprint, 1000:1 turndown, and EtherNet/IP diagnostics, but the page does **not** state
  the "+/-0.6% accuracy" figure previously recorded. Set `fetched: true`; claim narrowed to drop the
  unconfirmed accuracy number.
- `P3R2-A-11-S04` (Ichor Systems Talon gas-delivery page): WebFetched successfully; confirms Ichor is
  a real gas-panel-integrator company and describes seal-configuration/footprint benefits, but does
  **not** itemize the MFC/valve/manifold/sensor/control-electronics bundle previously attributed to it.
  Set `fetched: true`; claim narrowed accordingly (the Lam+AMAT=76%-of-sales figure remains correctly
  sourced to atlas `L07-049`, not this page).
- `P3R2-C-09-S03` (ScandiNova PR Newswire release): WebFetched successfully; the release states "over
  200 customers in more than 50 countries" and the 3,000th-unit milestone -- it does **not** state
  "150 customers and 2,000+ modulators installed historically" as previously recorded. Set
  `fetched: true`; claim corrected to the actually-supported figures.

Net Step 1: 7 of 8 records fixed (fetched:true, several claims corrected for accuracy); 1 rejected as
inaccessible (`P3R2-A-10-S03`).

## Step 2 — definitional tier corrections

Full scan of all 13 ledgers found 30 candidate records (definitional-T1-type T2/T3, or company_filing
T2). Each was checked against SOURCE_STANDARDS.md's T1 test ("official agency page, tender document,
statute/standard text, official program page" / "audited filing or official filing document").

Upgraded to T1 (3):
- `P3R2-C-12-S03` (P4-G05): Chinese Academy of Sciences institute page (cas.cn) describing CAS-IOP/IET's
  own cryogenic technology and its 2016 commercialization spinoff -- an official national-academy
  primary record. T2 -> T1.
- `P3R2-D-08-S02` (P4-G07): US Small Business Administration Office of Advocacy page (advocacy.sba.gov)
  quantifying the EPA EtO-rule rollback's cost impact -- an official federal-agency primary economic
  record. T2 -> T1.
- `P3R2-F-07-S04` (P4-G11): Guangdong Tower Energy battery-swap-cabinet tender notice, directly
  fetched from the bid-hosting platform -- a buyer tender/procurement document, the literal T1
  definition. T2 -> T1.

Not upgraded (examined and rejected for upgrade, with reason):
- `P3R2-C-13-S01`, `P3R2-F-15-S06/S07/S08`, `P3R2-F-20-S03` (all "regulator" T2, all OpenSanctions
  search results): OpenSanctions is a private third-party compliance aggregator, not an official
  government record -- fails the T1 "official law/regulation/standard; government... primary record"
  test regardless of source_type label. Left at T2.
- `P3R2-C-02-S03` ("standard" T3, ODCC white paper): the fetch was OCR-limited (content not fully
  machine-readable); upgrading tier on a document whose full text could not be confirmed would
  overstate confidence. Left at T3.
- All 21 `company_filing` T2 candidates (e.g., `P3R2-A-02-S02/S03`, `P3R2-A-11-S03`, `P3R2-A-14-S01`,
  `P3R2-A-21-S06/S07`, `P3R2-C-01-S01`, `P3R2-C-13-S05`, `P3R2-D-08-S03/S04`, `P3R2-D-13-S03`, etc.):
  each is a press release, funding announcement, product-launch release, or an earnings-call/summary
  write-up rather than an audited filing (10-K/20-F/annual report/8-K/official exchange disclosure).
  Per the binding rule ("investor-relations blurbs and press releases stay T2"), none were upgraded.

## Step 3 — atlas curation of context citations

Full scan found 185 candidate records (T2/T3, source_type in {trade_press, vendor_datasheet,
market_industry}). All 63 evidence files were read to check each candidate against the KEEP test
(sole support for a claim / competitor-primary / one of two 2030-timing sources) versus the DEMOTE
test (co-supported by a T1 source for the same claim / purely contextual-duplicative, e.g., a second
write-up of a funding round already covered, or generic vendor-marketing color).

Demoted (4):
- `P3R2-A-03-S03` (P4-G01, Elevate Energy blog): the evidence file's own text shows this restates the
  same "model-based PRC-029-1 compliance is sufficient" conclusion already established by T1 primary
  source `P3R2-A-03-S01` (Texas RE) and independently corroborated by `P3R2-A-03-S02` (which adds a
  unique fact -- named SEL compliance hardware -- that S03 does not). No new fact; demoted.
- `P3R2-A-10-S02` (P4-G01, Baker McKenzie blog): duplicates the Entity-List/VEU event already
  established by T1 source `P3R2-A-10-S01` (Federal Register), and (per the Step-1 fetch correction)
  does not independently confirm the more specific NAURA/Piotech-naming claim it was cited for.
  Demoted.
- `P3R2-C-09-S02` (P4-G05, NextBeam facility-gap article): the evidence file itself labels this
  "vendor-adjacent analysis, not independent customer evidence... used only as directional
  market-structure context" -- the analyst's own characterization matches the DEMOTE test for generic
  context. Demoted.
- `P3R2-E-02-S06` (P4-G09, 2013 Asetek/Data Center Knowledge article): a 13-year-old vendor-marketing
  write-up used only to note an absence (no EU two-phase competitor found), not to establish a
  specific competitive fact. Matches the "vendor marketing summaries" DEMOTE example. Demoted.

Kept accepted:true (the remaining ~181 candidates): in every evidence file reviewed, each T2/T3
trade_press/vendor_datasheet/market_industry record was independently verified to be either (a) the
sole documentation of a named competitor's product/capability (e.g., Comet Synertia, Calnetix IPM,
HORIBA D700MG, LEM zero-flux sensors, Danfysik, OCEM, Spellman, Advanced Energy UltraVolt, John Crane,
Bmax, PSTproducts, Guoli Electronics, NR Electric PCS-series, Recodeal, ASE FOEB, Mikros Technologies,
Sungrow SMS1000, Ecolab/Nalco+CoolIT, Dober, etc.), (b) one of the idea's two required 2030-timing
sources, or (c) the sole support for a specific, distinct demand/risk/competitive finding not
duplicated by any other source in the same file (e.g., the BIS Entity List findings for NAURA/Piotech/
CGN/CSSC/Raycus/CGN Dasheng, the CARB/EPA rollback findings, the Ecolab/CoolIT and Heron Power
competitive-timeline corrections, the Kuqa ALK-vs-PEM technology mismatch, etc.). These were judged
load-bearing per the task's own KEEP criteria and left unchanged.

## Result and honest shortfall

After Steps 1-3: total accepted = 1,112 (817 pre-P4 unchanged + 295 P4 records: 300 - 1 rejected - 4
demoted). Total T1 = 682 (593 pre-P4 unchanged + 89 P4: 86 original + 3 upgraded). T1 share = 682 /
1,112 = **61.3%**, versus the >=70% validator gate (>=70.5% target). All other validator gates pass
(peer=470/360, demand=284/120, gov=190/60, industry=308/60, US=454/150, CN=248/100, JP/TW/KR=128/40,
Asia=363/80, local_asia=162/40, T1+T2=97.5%, all 16 lanes >=35 accepted).

**This falls well short of the 70/70.5% T1-share target, and the shortfall is not closeable through
further honest per-record demotion.** The P4 evidence corpus, as authored, contains very little
duplicate or purely-contextual citation of the kind the DEMOTE test targets -- a full read of all 63
evidence files against all 185 Step-3 candidates found only 4 qualifying demotions, not the ~100-130
the task's target range assumed. Forcing additional demotions past this point would require either
(a) demoting records that are the sole documentation of a named competitor or a required 2030-timing
source -- which would violate the per-idea minimum-source and dual-timing-source requirements in
SOURCE_STANDARDS.md -- or (b) reclassifying tiers/acceptance without a genuine basis, which the task
explicitly prohibits ("never change a record's substance to game a gate"). Per the task's own
instruction, this shortfall is reported rather than forced.
