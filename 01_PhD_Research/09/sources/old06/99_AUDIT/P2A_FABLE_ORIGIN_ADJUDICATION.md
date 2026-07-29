# P2A India source-origin audit — Fable 5/xhigh adjudication

- Adjudicator: Fable 5 (claude-fable-5), xhigh effort, independent of the P2A auditor agents
- Date: 2026-07-13
- Working artifacts (scripts + extracts): `99_AUDIT/_adjudication_workdir/`
- Inputs reviewed: `05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.json` (+ `.md`),
  `05_STATE/INDIA_SOURCE_ORIGIN_PREFILTER.md` (+ `.json`), all 12 `05_STATE/P2A_BATCHES/P2A-*_audit.json`
  headers, `90_BIBLIOGRAPHY/sources.json`, all 20 `10_SOURCE_ATLAS/*verified_sources.json`,
  lane briefs + `ATLAS.md`, `tools/validate_sources.py`, `tools/merge_sources.py`.

## 1. Methodology

1. Parsed the canonical ledger (1,118 rows) and the audit report (833 verdicts: 818
   `verified_non_india_origin`, 15 `discovery_only`). Cross-checked coverage: every canonical
   accepted record carries a completed audit object; zero accepted records lack one.
2. Stratified sample of 80 accepted records (5 per lane, L01–L16): the five lowest accepted IDs
   per lane, with the lane's first non-academic accepted record swapped into position 5 whenever
   the first five were all academic (triggered in 13 of 16 lanes). Desk-checked all 80 for
   verdict, method, institutions, and evidence URLs; WebFetch-verified 13 of the 80 end-to-end.
3. Independently web-verified the two flagged records (L15-010, L16-045), 6 exclusions whose
   India-origin evidence was absent from the ledger, 2 lane-ledger strays, and the large-author
   multinational plausibility set — 24 live web verifications in total (OpenAlex, Crossref, PMC,
   Cambridge Core, publisher/organization pages).
4. Reviewed all 42 excluded IDs (27 prefilter + 15 full-audit) copy-by-copy in the canonical and
   lane ledgers, including duplicate-row analysis.
5. Read 3 repaired lane briefs (L01, L07, L14) plus ATLAS.md in full at the repair sections, and
   programmatically scanned all 16 briefs + ATLAS.md for any excluded-ID or quarantined-consultancy
   mention outside the repair-log sections.
6. Ran `tools/validate_sources.py` before and after fixes.

## 2. Sampled ID list (80)

- L01: 001, 002, 003, 004, 030 — L02: 001, 002, 004, 005, 025 — L03: 001, 002, 003, 004, 030
- L04: 001, 002, 003, 004, 020 — L05: 002, 003, 004, 005, 028 — L06: 001, 002, 003, 004, 032
- L07: 001, 002, 003, 004, 028 — L08: 001, 003, 004, 005, 029 — L09: 001, 002, 003, 004, 009
- L10: 001, 002, 003, 004, 009 — L11: 001, 002, 003, 004, 032 — L12: 001, 002, 003, 004, 031
- L13: 001, 002, 003, 004, 026 — L14: 001, 002, 003, 004, 030 — L15: 001, 002, 003, 004, 026
- L16: 001, 002, 003, 004, 009

Desk result: all 80 have `verified_non_india_origin` with an appropriate method
(`openalex_affiliations`, `publisher_page`, `org_identity_page`, or `other` with justification),
plausible named institutions, and at least one evidence URL. No gaps.

Web-verified end-to-end (13 of the 80): L01-001 (Southeast Univ. CN), L02-001 (Virginia Tech US),
L03-003 (RU/US/JP/CH/NZ, 28 authorships), L04-001 (MIT/NREL US), L05-004 (Dongnam Inst. KR),
L06-032 (NIST US-gov page), L08-029 (GE Vernova, Cambridge MA US), L09-009 (Busek, Natick MA US),
L12-031 (DefenseScoop/Scoop News Group, US), L13-003 (229 authorships, CN-only country set),
L14-001 (Zhejiang Univ. CN), L15-026 (DARPA US-gov page), L16-004 (Univ. of Guilan/Mazandaran IR).
Every fetch matched the recorded verdict; zero Indian affiliations found.

## 3. Per-check findings

### 3.1 Zero multinational exceptions — plausible, not an artifact

The auditors demonstrably enumerated affiliations rather than sampling first authors:

- L13-003 (229 authorships) and L13-009 (151 authorships): full lists checked programmatically;
  I re-fetched both OpenAlex records — country sets match the audit notes exactly (CN-only;
  IT/FR/ES/CH/GB/DE/US/NL/GR/NO/CN/CZ). No IN.
- L07-020: two authors with Indian names and no OpenAlex institution (Puneet Sharma, Lavanya
  Iyer) were resolved via a direct PMC affiliation-list fetch — I re-fetched PMC8575750 and
  confirmed Genentech (US) and BMS (US). Names were resolved, never inferred.
- L11-010 (21 authors, 18 resolved) and L03-026 (32 authors, 20 resolved + documented handling of
  the unresolved JT-60SA/F4E cohort): partial-resolution cases were documented rather than waved
  through.
- The same OpenAlex query pattern demonstrably catches India when present (L05-001's RRCAT
  exclusion came from the identical batch query that passed L05-004).

Zero exceptions is consistent with a corpus whose scouts were already India-avoidant post-directive:
the India-linked papers that slipped through were India-ONLY (all quarantined), and the two
near-miss mixed-name cases resolved to US institutions. Finding: **plausible and evidenced**.

### 3.2 All 42 exclusions reviewed

- India-origin evidence is specific for every exclusion I could trace, and I affirmatively
  re-verified 7 end-to-end this session (see 3.3). Specific bases include: Government-of-India
  domains (barc.gov.in, isro.gov.in, rrcat.gov.in, vecc.gov.in, digitalindia.gov.in, iterindia.in),
  Indian companies' own pages (Tata Electronics, Larsen & Toubro, INOX India), publisher-registered
  Indian institutional affiliations (IIT Bombay/Hyderabad/Ropar/Kanpur, IGCAR, BARC, RRCAT,
  Kumaraguru College), India-based outlets (pv magazine India, Mercom India, SolarQuarter,
  The Better India), and — for the consultancy quarantines — registry/contact-page evidence
  (Mordor Intelligence: Hyderabad HQ + ROC-Hyderabad registration; Valuates/MarketGrowthReports:
  Bangalore contact page with India phone number behind a US toll-free forward).
- **No exclusion rests on a person's name alone.** All 42 rest on institutional affiliation,
  organizational registry/domain, or India-only content; the corpus retains multiple
  South-Asian-named authors at US/UK/EU/CN institutions (L07-020 verified live).
- Two quarantines are over-broad but in the permitted conservative direction: L01-042
  (CleanTechnica, US outlet) and L01-054 (AII, US non-profit) were excluded for India-tied
  content clusters although their producers are US-based and (for L01-054) most of the content
  concerns UK/US/Japan failures. No action required; if the plasma-gasification failure evidence
  is needed for red-teaming, these two may be re-audited for reinstatement or re-sourced — the
  L01 brief already flags the claims as "needs re-sourcing".
- **Encoding defect found and fixed (pre-existing, now closed):** 16 of the 27 prefilter
  quarantines were not correctly encoded in the canonical ledger. 7 (L01-010, L02-008, L03-054,
  L04-024, L05-025, L05-051, L08-023) had only `accepted:false` with **no** rejection_reason, no
  `discovery_only` retype, and no `india_origin_audit` object anywhere (canonical or lane) — a
  silent, unexplained rejection that a later agent could have re-promoted. 9 more (L01-041,
  L01-042, L01-054, L04-105, L06-047, L08-028, L09-035, L11-036, L14-052) were fully encoded in
  their lane ledgers but retained their original `source_type` in the canonical copy. All 15
  full-audit quarantines were correctly encoded on their authoritative canonical rows.
  Post-fix check: **all 42 now satisfy accepted=false + source_type=discovery_only +
  india_origin_audit.status=excluded_india_origin + non-empty rejection_reason + evidence URLs**
  in the canonical ledger, and the 7 repaired records are likewise encoded in their lane ledgers.

### 3.3 Origin verification performed for the 7 silently-rejected exclusions

I did not encode any exclusion without independently verifying India origin first:

| ID | Verified origin | Evidence |
|----|-----------------|----------|
| L01-010 | IIT Hyderabad (all 6 authors) | OpenAlex, DOI 10.1016/j.ces.2022.118376 (found via Crossref title search) |
| L02-008 | IIT Ropar (all 4 authors) | OpenAlex, DOI 10.1016/j.mtcomm.2022.104244 (journal is Materials Today Communications, not "e-Prime" as the ledger said) |
| L03-054 | IPR/VECC, DAE, Government of India | Document hosted on vecc.gov.in (self-evident national-lab origin) |
| L04-024 | IGCAR Kalpakkam (all 4 authors) | Crossref affiliation strings, DOI 10.1115/gtindia2019-2455 |
| L05-025 | BARC Mumbai (all 4 authors; ledger said RRCAT — both Indian) | OpenAlex, DOI 10.1016/j.nima.2014.05.125 |
| L05-051 | RRCAT Indore (all 9 authors; ledger geography "multinational" was wrong) | Cambridge Core article page |
| L08-023 | IIT Bombay (both authors) | OpenAlex, DOI 10.1109/tpel.2023.3263004 |

All 7 confirmed entirely India-origin; quarantine encoding applied with this evidence.

### 3.4 Ruling on L15-010

**Finding:** the original verdict basis (the record's own "University of Arkansas" attribution,
because OpenAlex/Crossref carry no affiliation metadata for DOI 10.4071/imaps.527) did **not**
meet the "verified" bar — self-attestation is not verification.

**Independent verification performed:** (a) OpenAlex re-fetched — affiliation arrays confirmed
empty, corroborating the auditor's account; (b) the IMAPS JMEP mirror
(imapsjmep.org/article/39940) confirms the exact article, the six-author list, and JMEP
vol 13(4) pp. 143–154 (2016); (c) Ozark Integrated Circuits, Inc. (Fayetteville, AR, US)
publicly claims the publication and team on its own site; (d) H. A. Mantooth's group is
University of Arkansas (US). No India connection appears anywhere.

**Ruling: verdict `verified_non_india_origin` AFFIRMED**, with the evidence basis upgraded
(methods now include `publisher_page`; Ozark IC added to institutions; two evidence URLs added)
in the canonical and L15 lane ledgers. I also corrected the record's article URL: it pointed to
`jmep/article/15/4/163/36733` (a different article page); the correct page is
`jmep/article/13/4/143/36623`, matching the record's own locator. No quarantine required.

### 3.5 Ruling on L16-045

**Finding confirmed:** Crossref registers DOI 10.1126/science.aba2648 (Science 370(6512):129–133,
2020-10-02) with authors Wang, Zhang, Usui, Benedict, Hirose, Lee, Kalb, Schwartz — PARC, A Xerox
Company (US) + Murata Manufacturing (JP). No "Qian", no UCLA. The ledger's "Qian, Suxin et al.
(UCLA-affiliated)" was a conflation with other caloric-cooling literature (Qian Suxin's work is
elastocaloric, Xi'an Jiaotong; the UCLA electrocaloric Science paper is Ma et al. 2017).

**Ruling: metadata correction REQUIRED and APPLIED** (canonical + L16 lane ledger):
`authors_or_org` replaced with the Crossref-verified list, "(UCLA)" corrected in
`claim_supported`, correction note appended. Origin verdict `verified_non_india_origin`
unaffected (US/JP under either attribution).

### 3.6 Atlas repair quality (L01, L07, L14 briefs + ATLAS.md)

- Repairs are genuine removals, not soft edits: consultancy market sizes, the India named-buyer
  entries, India trigger bullets, and India geography paragraphs are deleted with explicit
  "needs re-sourcing from an eligible provider" annotations; citation lists were trimmed
  ID-by-ID; renumbering documented. ATLAS.md even removed a *derived, uncredited* echo of the
  quarantined L15-045 TAM-disagreement claim — good depth.
- Programmatic scan of all 16 briefs + ATLAS.md: **zero quarantined-consultancy names**
  (Mordor, Valuates, DataIntelo, Persistence, MarketsandMarkets, TBRC, Global Growth Insights,
  QYResearch, researchandmarkets, MarketGrowthReports, Growth Market Reports) survive outside
  repair sections.
- Residual stale bookkeeping found and fixed by me: L13 brief still counted quarantined L13-050
  in its T3 tally; L15 brief still counted L15-045 in its T3 cap and fetch-status list; L16 brief
  still counted L16-008/021 in Asia-coverage and follow-up-priority lines. All now carry explicit
  "[quarantined 2026-07-13]" corrections. The L05 brief's line-6 mention of `L05-001` is a benign
  ID-range span ("L05-001...L05-050"), not a citation — left as is.
- L10's brief lacked the repair section entirely (the repair wave skipped the one lane with no
  exclusions); I appended a factual "no exclusions in this lane" P2A section so every brief now
  carries an explicit disposition.

### 3.7 Ledger / validator coherence

- `validate_sources.py`: **PASS before and after fixes**, identical counters —
  reviewed=1118, accepted=818, peer=468, demand=190, gov=135, industry=124, US=295, CN=162,
  side=112, asia=264, local_asia=99, T1=594 — matching the audit report exactly. My fixes touched
  only non-accepted rows plus metadata/evidence on two accepted rows, so counts are unchanged by
  construction.
- Audit JSON internal consistency: 833 verdicts = 818 verified + 15 excluded; the 42-ID exclusion
  list matches prefilter + full-audit lists exactly; multinational_exception_ids = [].
- **Duplicate-row artifact (documented, not a P2A failure):** the canonical ledger contains 198
  duplicated IDs (1,118 rows / 920 unique). In every pair the authoritative audited copy comes
  first and a stale pre-verifier draft (different `canonical_key`, `accepted:false`, no audit
  object) survives later in the file because `merge_sources.py` dedupes by `canonical_key`, not
  ID. No stale copy is accepted; every accepted row is audited; the validator's
  "accepted-requires-completed-audit" check is an effective backstop against silent re-entry.
  Residual hazard: tools that index the ledger by ID and take the *last* match will read
  pre-audit state (this adjudication initially did exactly that). 30 pairs even differ in title
  (e.g., L03-045 binds two different press items to one ID).
- **Lane-ledger strays closed:** lane ledgers carried 820 accepted rows vs canonical 818. The two
  extras — L01-013 and L06-030 — are cross-lane duplicates of works already accepted *and
  audited* in canonical under other IDs (doi:10.1063/5.0226790 = L06-002; doi:10.1088/2040-8986/ac5a7e
  = L12-008), so no canonical work escaped the audit. Because their lane rows were
  accepted-without-audit (a leak risk for by-lane consumers and future merges), I origin-verified
  both live (HUST CN + Ruhr Bochum DE; ARCNL/VU Amsterdam/Groningen NL — no IN) and wrote audit
  objects into the lane rows with explicit notes that canonical acceptance is not granted here.

## 4. Records re-verdicted or fixed by this adjudication

No verdict among the 833 was overturned. Fixes applied (all verified against live evidence,
validator green after each wave):

1. Full quarantine encoding added, canonical + lane ledgers (7): **L01-010, L02-008, L03-054,
   L04-024, L05-025, L05-051, L08-023** (evidence in §3.3).
2. Canonical `source_type` → `discovery_only` (lane copies were already correct) (9): **L01-041,
   L01-042, L01-054, L04-105, L06-047, L08-028, L09-035, L11-036, L14-052**.
3. **L15-010**: evidence basis upgraded + article URL corrected (canonical + L15 lane).
4. **L16-045**: authorship corrected to the Crossref-verified PARC/Murata list (canonical + L16 lane).
5. Lane-ledger audit objects added for stray accepted duplicates: **L01-013, L06-030**.
6. Brief fixes: stale-count annotations in L13/L15/L16 briefs; missing P2A repair section added
   to the L10 brief.

Outstanding required fixes: **none**.

## 5. Residual risk and recommendations (non-blocking)

1. **Duplicate-ID rows (198)** in the canonical ledger: recommend the orchestrator either purge
   superseded drafts or add ID-level supersession to `merge_sources.py` before P3 consumers read
   the ledger by ID. Also reconcile the 30 title-mismatched pairs (worst: L03-045).
2. **Rule-15 usage leakage (origin-eligible but India-market content):** e.g., L08-029
   (GE Vernova press release on the Adani Khavda VSC-HVDC award; geography ['IN','US'],
   demand_evidence_type=official_project_award) passes the origin rule but must not be used as
   buyer/demand/market evidence in P3 because the buyer and project are Indian. The L13 brief's
   demand-span sentence still names India/Singapore. Recommend a P3-side geography filter on
   `geography`/buyer country, independent of source origin.
3. **ATLAS.md misquotes the founder-fit cap** as "5/100 per CLAUDE.md rule 3"; the binding cap is
   **2/100**. Not an origin matter, so I did not edit it — flagging for the orchestrator to
   correct before P3 scoring.
4. Two conservative over-quarantines (L01-042, L01-054, both US producers) may be revisited if
   the plasma-gasification failure record is wanted for red-teaming; the safe default (leave
   quarantined) stands.
5. OpenAlex institution disambiguation errors occur (the audit itself caught L09-023, SITAEL
   Italy mis-mapped to "Department of Space (IN)"); the audit's practice of falling back to raw
   affiliation strings should be kept mandatory for any future top-up waves.

## 6. Adjudication summary

Sampled 80/818 accepted records across all 16 lanes (13 web-verified end-to-end; 24 live web
verifications overall including flags, exclusions, and strays). Verdict quality is high: methods
are appropriate, evidence is recorded, large author lists were genuinely enumerated, and no
origin call anywhere rests on a person's name. The 15 full-audit quarantines were correctly
evidenced and encoded. The defects found — 16 mis-encoded prefilter quarantines, one
insufficiently-verified pass (L15-010), one authorship conflation (L16-045), two unaudited lane
strays, and stale brief bookkeeping — have all been fixed and re-validated in this session; none
overturned a verdict.

ADJUDICATION: PASS
