# Fable adjudication

**Verdict: PASS**  
**Date:** 2026-07-14  
**Requested route:** Fable-class/xhigh independent adjudication  
**Actual runtime model / effort:** `unknown` / `unknown` (not exposed; not inferred)

## Scope

The independent P8 reviewer read the frozen 24-idea selection, all ten deep dives, the full geography brief, all final-portfolio outputs, the canonical ledger, the P2A origin adjudication, and the load-bearing P4/P5 gate artifacts. The final deterministic sample covered 24 accepted sources across 12 lanes and 12 final ideas, plus 12 load-bearing claim checks and all ten deep dives.

The independent proposal is preserved in `P8_INDEPENDENT_ADJUDICATION_PROPOSAL.md` and `.json`. Its final JSON is parse-valid, records `verdict: PASS`, contains no required repairs, and reports zero unresolved source- or claim-level failures.

## Adversarial findings and repairs

The first readback did not pass. It found four real classes of defect:

1. The historical source ledger contained 1,487 rows but only 1,289 unique IDs. One accepted and one stale rejected copy often shared an ID, which made last-row-wins readers disagree.
2. Ten countable sub-$100k experiments were abbreviated in selection and final cards even though their full protocols existed upstream.
3. C-13 incorrectly carried Raycus as a buyer, and CN-03 incorrectly carried a US beachhead.
4. Several final source packs contained adjacent or off-product records, and four source records had inaccurate source-type, tier, or publisher-origin metadata.

The main repair wave closed every item:

- Collapsed all 198 duplicate-ID groups to one authoritative row. No group had multiple accepted records. The ledger is now 1,289 rows / 1,289 unique IDs, with the pre-repair ledger preserved in the run logs.
- Propagated duration, full budget breakdown, preregistration, pass thresholds, and kill thresholds for all ten immediately countable cheap experiments into selection, idea cards, and roadmap.
- Removed Raycus from the C-13 buyer route, conditioned the remaining China buyer on fresh screening, and set CN-03 to `us_beachhead:false` in selection, cards, matrix, and geography.
- Corrected the transcript/news/trade source typing and DefenseScoop publisher attribution; removed off-product associations from D-02, B-01, F-12, and G-01; inserted relevant accepted replacements; and reran every source quota.
- Retained conservative $120k planning envelopes for both selected China round-two experiments because their lower public estimates lack signed access and project-specific quotes.

## Literal G1 adjudication

The reviewer initially treated absence of a future merchant order as a G1 failure for several pre-company concepts. After applying the binding rubric, those objections were withdrawn. G1 does not require a purchase order for a startup product that does not exist. Host-system evidence may support G1 only when the proposed job is a tight, necessary acceptance or operation function—protection, matching, cooling, sensing, qualification, power conversion, or outgassing acceptance in the reviewed cases.

Merchant separability, willingness to outsource, and a paid evaluation remain real uncertainties, but they belong in G4, G7, and the decisive experiment. The final cards and roadmap preserve those risks and their 2029 kill rules; no future engagement is represented as current fact.

## Final readback

- Canonical sources: 1,289 reviewed unique records; 1,182 accepted; 482 peer-reviewed; 298 primary-demand.
- Portfolio: exactly 24 ideas; exactly 10 deep dives; 12 lanes; maximum three per lane.
- Roles/archetypes: five diagnostics, 19 direct-value products, 12 industrial, four scientific/big-physics, eight infrastructure/utility/transport.
- Geography: 20 US, 18 China, 14 dual; false beachheads remain explicit.
- Experiments: 11 decisive sub-$100k protocols; conditional lower estimates receive no quota credit.
- Deep dives: exact ten; every report 2,500-4,000 words and at least 20 accepted / 7 peer-reviewed / 5 primary sources.
- Founder fit: exactly 2/100 and last on all 24 cards.
- Excluded-market scan: PASS across selection, geography, and final market files.
- Mechanical audit: PASS.

No unresolved substantive defect remains. **Fable adjudication: PASS.**
