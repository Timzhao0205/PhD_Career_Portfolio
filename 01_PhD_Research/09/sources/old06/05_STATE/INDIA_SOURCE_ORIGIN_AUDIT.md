# India source-origin audit — P2A completion report

Written: 2026-07-13T00:54:28.564496+00:00

## Scope and rule

All 833 provisionally accepted canonical records (post-prefilter) were individually
audited in 12 batches by Sonnet-5 auditor agents. Academic papers: author affiliations
resolved from OpenAlex/Crossref structured metadata with publisher-page/PDF enumeration
whenever any Indian or unresolved affiliation appeared; affiliations were never inferred
from names. Non-academic sources: producing-organization location verified from official
identity/about/contact pages or registries, including checks for India-registered
consultancies operating behind US/UK virtual-office branding.

## Results

- Full-audit verdicts: {'verified_non_india_origin': 818, 'discovery_only': 15}
- Newly quarantined (discovery_only): 15 — L01-051, L01-052, L03-047, L03-049, L05-001, L06-053, L07-038, L07-039, L13-050, L14-011, L14-017, L14-023, L15-045, L16-008, L16-012
- Multinational exceptions used: 0 (none arose)
- Prefilter quarantines (2026-07-12): 27
- Total excluded IDs: 42
- Accepted after audit: 818

## Quarantined records and their leads (must be independently re-sourced before reuse)

- **L01-051**: Report claims global plasma surface treatment system market at $4.5B (2025) growing to $8.2B by 2034 (6.8% CAGR); Asia Pacific >$1.7B in 2025 (7.6% CAGR). Independently confirm via a non-India-based market-research or trade-association source before citing.
- **L01-052**: Report claims plasma surface treatment equipment market at $2.6B (2025) growing to $3.9B by 2032 (5.8% CAGR); typical equipment price USD 5,000-8,000/unit; Europe 34% share; semiconductor/electronics 26.1% share. Independently confirm via a non-India-based market-research or trade-association source before citing.
- **L03-047**: Global cryocooler market estimated at USD 2.81 billion (2026) growing to USD 5.26 billion by 2031 (13.37% CAGR), with named leading vendors Sumitomo Heavy Industries, Northrop Grumman, Cryomech/Bluefors, Thales, and Sunpower/AMETEK -- worth independently re-sourcing from a non-India market-research firm before use as demand/market evidence.
- **L03-049**: Global superconducting wire market estimated to grow from USD 1.32 billion (2025) to USD 2.19 billion (2030), 10.6% CAGR, with named leaders Sumitomo Electric, Fujikura, Furukawa Electric, Bruker, and American Superconductor -- worth independently re-sourcing from a non-India market-research firm before use as demand/market evidence.
- **L05-001**: RRCAT (India) reports a 34-section, 100 kV/20 A, 1 ms solid-state Marx modulator prototype for klystron drive using IGBT-based 3 kV main modules with a 24-module droop-correction scheme. If this specific design point is needed, seek an independent non-Indian source (e.g., another lab's citation/replication) before treating it as load-bearing; do not cite this record directly for technical, demand, market, or geography claims.
- **L06-053**: MFC-for-semiconductor market-size estimate (USD 1.05B in 2025 -> USD 2B by 2035, 6.5% CAGR) and vendor share list (HORIBA 17%, MKS 14%, Fujikin, Sevenstar, Hitachi Metals, Pivotal Systems, Bronkhorst, Brooks, Sensirion) is worth independently re-sourcing from a non-Indian consultancy (e.g., a competing Fortune Business Insights or Yole report) before use in market sizing.
- **L07-038**: Global vacuum pump market size claim (~USD 7.56B 2025 -> USD 10.81B 2030, 7.41% CAGR) originates from Mordor Intelligence, headquartered at Rajapushpa Summit, Financial District, Gachibowli, Hyderabad, Telangana, India (confirmed via the firm's own contact-us page, which lists only the Hyderabad office, and its ROC-Hyderabad company registration). Needs independent confirmation from a non-Indian market-research firm or trade association before use in market sizing.
- **L07-039**: Semiconductor dry vacuum pump market TAM figures and vendor-concentration claim (Atlas Copco/Edwards, Ebara, Pfeiffer, Kashiyama, ULVAC among ~15 named vendors, informal 'top-6 = 62% share') originate from Valuates Reports/MarketGrowthReports, headquartered at Balaraj's Arcade, Whitefield, Bangalore, Karnataka, India (confirmed via the firm's own contact page, which lists only the Bangalore office and an India phone number alongside a US toll-free forwarding line). Needs independent non-Indian confirmation before use in market sizing or competitive-structure claims; the named-vendor list itself may be separately corroborable from vendor-side sources.
- **L13-050**: Dilution-refrigerator-for-quantum-computing market estimated at roughly US$72.6M (2024) growing to US$193M by 2031 (~15% CAGR); lists 9 major vendors (Bluefors, ULVAC, Oxford Instruments, Cryoconcept, FormFactor, Maybell Quantum, Zero Point Cryogenics, Benyuan Quantum Computing/Hefei, Hefei QuantumCTek). Independently confirm market-size/vendor-share figures via a non-India-based market-research source (e.g., a QYResearch report published/sold directly by QYResearch's own US entity, or vendor-disclosed figures from Bluefors/Oxford Instruments) before use in demand or market-size claims.
- **L14-011**: This is a critical review of nanofluid impinging-jet cooling for advanced electronic cooling; the underlying technical claim (nanofluid impinging jets as a viable next-gen cooling approach) could be independently corroborated via other non-Indian review literature already in this lane (e.g., L14-013 general jet-impingement review) rather than relying on this source.
- **L14-017**: This is a general review of thermal interface materials (TIM tradeoffs among bulk conductivity, bond-line resistance, mechanical compliance); the general technical claim could be independently corroborated via other non-Indian TIM reviews already in this lane (e.g., L14-018, European Polymer Journal) rather than relying on this source.
- **L14-023**: The paper's core technical claim (loop-heat-pipe architecture and use in spacecraft/high-reliability thermal control) is a well-established topic; independently confirm via non-Indian primary sources such as NASA/ESA loop-heat-pipe technical literature if this specific claim is needed for the brief.
- **L15-045**: Global downhole tools market claimed at $5.79B (2025) rising to $6.07B (2026) and $7.33B by 2030 (4.7-4.8% CAGR); independently confirm via a non-Indian-origin market-research firm, oilfield-services trade association, or public-company investor materials before citing any downhole-tools market-size figure.
- **L16-008**: Review of ionic-wind (corona-discharge EHD) thermal-management research through 2020; if this survey's technical summary is useful, independently confirm the underlying claims via the primary papers it cites or an equivalent non-Indian-authored review.
- **L16-012**: Review of metamaterial-based RF/microwave absorber design approaches; if useful for the RCS/stealth-metamaterials thread, cross-check its claims against the batch's other already-accepted non-Indian metamaterial-RCS academic sources (e.g., L16-010, L16-011) rather than citing this record directly.

## Notable audit findings

- Recurring pattern: India-registered market-research consultancies with US/UK
  virtual-office branding (DataIntelo/Growth Market Reports, Persistence Market
  Research, Mordor Intelligence, MarketsandMarkets, Global Growth Insights, Valuates
  Reports, TBRC Business Research via researchandmarkets.com listings).
- OpenAlex disambiguation error caught on L09-023 (SITAEL Italy falsely mapped to
  "Department of Space (IN)"); corrected via raw affiliation string.
- Names were never used to infer origin; multiple South-Asian-named authors resolved
  to US/UK/EU/CN/AU institutions and were retained.
- Flagged for Fable adjudication: L15-010 (passed on record attribution without
  structured metadata) and L16-045 (Crossref author set does not match ledger note;
  origin verdict unaffected).

## Ledger synchronization

- Canonical ledger and all lane verified_sources ledgers updated with
  india_origin_audit objects for all 833 audited records; 15 quarantined with
  accepted=false, source_type=discovery_only, and rejection_reason set.
- validate_sources.py: PASS after merge (accepted=818, peer=468, demand=190,
  gov=135, industry=124, US=295, CN=162, side=112, asia=264, local_asia=99, T1=594).
