# DELIVERABLES SPEC V3 & ACCEPTANCE CHECKLIST

```
03_C12_C10_Strategy_IP_2026-07/
├── 05_STATE/    MASTER_STATE.json [] COMPLETE · PROGRESS_LOG.md [] per phase/wave ·
│                ASSUMPTIONS.md [] exists · BASELINE.md [] Phase-0 extract
├── 10_COMPETITORS/  [] 8 segment files CS_A..CS_H (4-8 cards each, price signals, weaknesses)
│                    + 8 *_sources.json (>=12 fresh each)
├── 20_UNSOLVED/     [] U_A..U_H fragments · UNSOLVED_REGISTER.md [] 20-40 deduped U-### rows
├── 30_PATENTS/      [] PL_P01..PL_P10 (+ fragments) · patent_ledger.json [] >=150 records,
│                    >=50 CN-family, parses · PATENT_INDEX.md [] human-readable
├── 40_WHITESPACE/   [] WHITESPACE_REGISTER.md 15-25 scored W-## rows with
│                    INVENT/TRADE-SECRET/MONITOR calls; >=10 INVENT selected
├── 50_INVENTIONS/   [] 10-14 ID_nn disclosures (11-part template) · IPRT_nn red-team for
│                    EVERY disclosure · >=6 FILE-CANDIDATE survivors target
├── 60_STRATEGY/     [] 00_EXEC_BRIEF.md · STRATEGY_C12.md · STRATEGY_C10.md ·
│                    CLUSTER_PLAYBOOK.md (incl. ASC-2026 question additions) ·
│                    IP_ROADMAP_2026_2029.md (fee pages fetched, publish/file reconciled)
├── 90_BIBLIOGRAPHY/ [] sources.json >=120 fresh; BIBLIOGRAPHY.md tier-grouped, zh bilingual
└── 99_AUDIT/FINAL_AUDIT.md [] patent re-fetch 15/15 title+assignee match · source re-fetch
                     15 · Stanford-wall table all ID_nn · disclaimer-header check ·
                     Magnefy/HTS-drift scan · quotas · checklist
```

## U-entry schema (20_UNSOLVED)
`U-### | lane C12|C10 | problem (<=30 words) | who suffers (org archetype, named example) |
evidence [S/P refs] | severity 1-5 | why unsolved (technical/economic/incentive, 1 line) |
small-team-exploitable Y/N | linked clusters P##`

## W-entry schema (40_WHITESPACE)
`W-## | gap statement | linked U-### | nearest prior art [P-###] + 1-line distance |
scores D/O/B/M/J (0-5 each, /25) | call INVENT|TRADE-SECRET|MONITOR | 1-line rationale`

## ID_nn disclosure template (50_INVENTIONS; 900-1,600 words; disclaimer header first)
1 Title & field · 2 Problem & demand evidence [U-###, S/P refs] · 3 Inventive concept (what is
new, one paragraph) · 4 Difference vs 3 nearest prior-art patents BY NUMBER [P-###, 1-2 lines
each] · 5 Claim sketch — plain language, 1 independent + 4-6 dependent (drafting aid, not
claims) · 6 Embodiments (2-3, incl. one minimal) · 7 Reduction-to-practice plan: BOM sketch,
budget band <=\$5K / \$5-25K / STRETCH \$25-60K, personal-resources feasibility, timeline in
PhD-evenings terms · 8 Stanford/UIUC wall assessment (4-prong test from IP_GROUND_RULES §1;
verdict PASS / BLOCKED-PENDING-COUNSEL) · 9 Patent-vs-trade-secret call (GROUND RULES §5
rule applied) · 10 Publish/file sequencing + US/CN route (provisional timing, PCT decision
gate, CN utility-model dual-filing note) · 11 Design-around resistance + open counsel
questions

Style: direct, quantitative, units+dates, no filler; every file readable standalone;
disclaimer header on every 40_/50_/60_ file.
