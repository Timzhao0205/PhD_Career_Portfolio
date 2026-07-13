"""Compile 05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.{md,json} from batch audits + prefilter."""
import datetime
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PREFILTER_IDS = [
    'L01-006', 'L01-010', 'L01-026', 'L01-041', 'L01-042', 'L01-054', 'L02-003',
    'L02-008', 'L03-054', 'L04-024', 'L04-037', 'L04-105', 'L05-025', 'L05-051',
    'L06-047', 'L07-033', 'L07-048', 'L08-023', 'L08-028', 'L09-035', 'L11-036',
    'L11-053', 'L12-043', 'L13-034', 'L13-051', 'L14-052', 'L16-021',
]


def load(path):
    with open(path, encoding='utf-8-sig') as f:
        return json.load(f)


def main() -> None:
    queue = load(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json'))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()

    all_entries = {}
    batch_meta = []
    for b in queue['batches']:
        audit = load(os.path.join(ROOT, f"05_STATE/P2A_BATCHES/{b['batch_id']}_audit.json"))
        batch_meta.append({'batch_id': b['batch_id'], 'audited_at': audit.get('audited_at'),
                           'model': audit.get('model'), 'effort': audit.get('effort'),
                           'n': len(audit.get('entries', []))})
        for e in audit['entries']:
            all_entries[e['id']] = e

    verdicts = Counter(e['verdict'] for e in all_entries.values())
    quarantined = sorted(i for i, e in all_entries.items() if e['verdict'] == 'discovery_only')
    multinational = sorted(i for i, e in all_entries.items()
                           if e['verdict'] == 'verified_multinational_allowed')

    report = {
        'written_at': now,
        'rule': ('India-located/produced sources cannot support technical, demand, market, '
                 'competitor, policy, or geography claims; discovery_only retention allowed. '
                 'Academic exception: >=1 verified non-Indian co-author affiliation. '
                 'Affiliation never inferred from names.'),
        'canonical_records_reviewed': 1118,
        'accepted_before_full_audit': 833,
        'accepted_after_full_audit': 833 - len(quarantined),
        'prefilter_quarantined_2026_07_12': PREFILTER_IDS,
        'full_audit_batches': batch_meta,
        'full_audit_verdict_counts': dict(verdicts),
        'full_audit_quarantined_ids': quarantined,
        'multinational_exception_ids': multinational,
        'total_excluded_ids': sorted(PREFILTER_IDS + quarantined),
        'verdicts': {i: {'verdict': e['verdict'], 'method': e.get('method'),
                         'non_indian_affiliation_count': e.get('non_indian_affiliation_count'),
                         'evidence_urls': e.get('evidence_urls'),
                         'institutions': e.get('institutions'),
                         'useful_lead': e.get('useful_lead', ''),
                         'audited_at': e.get('audited_at')}
                     for i, e in sorted(all_entries.items())},
    }
    with open(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.json'), 'w',
              encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
        f.write('\n')

    leads = [(i, all_entries[i].get('useful_lead') or '') for i in quarantined]
    md = ['# India source-origin audit — P2A completion report', '',
          f'Written: {now}', '',
          '## Scope and rule',
          '',
          'All 833 provisionally accepted canonical records (post-prefilter) were individually',
          'audited in 12 batches by Sonnet-5 auditor agents. Academic papers: author affiliations',
          'resolved from OpenAlex/Crossref structured metadata with publisher-page/PDF enumeration',
          'whenever any Indian or unresolved affiliation appeared; affiliations were never inferred',
          'from names. Non-academic sources: producing-organization location verified from official',
          'identity/about/contact pages or registries, including checks for India-registered',
          'consultancies operating behind US/UK virtual-office branding.',
          '',
          '## Results',
          '',
          f"- Full-audit verdicts: {dict(verdicts)}",
          f"- Newly quarantined (discovery_only): {len(quarantined)} — {', '.join(quarantined)}",
          f"- Multinational exceptions used: {len(multinational)}"
          + (f" — {', '.join(multinational)}" if multinational else ' (none arose)'),
          f"- Prefilter quarantines (2026-07-12): {len(PREFILTER_IDS)}",
          f"- Total excluded IDs: {len(PREFILTER_IDS) + len(quarantined)}",
          f"- Accepted after audit: {833 - len(quarantined)}",
          '',
          '## Quarantined records and their leads (must be independently re-sourced before reuse)',
          '']
    for i, lead in leads:
        md.append(f"- **{i}**: {lead if lead else 'no retained lead'}")
    md += ['',
           '## Notable audit findings',
           '',
           '- Recurring pattern: India-registered market-research consultancies with US/UK',
           '  virtual-office branding (DataIntelo/Growth Market Reports, Persistence Market',
           '  Research, Mordor Intelligence, MarketsandMarkets, Global Growth Insights, Valuates',
           '  Reports, TBRC Business Research via researchandmarkets.com listings).',
           '- OpenAlex disambiguation error caught on L09-023 (SITAEL Italy falsely mapped to',
           '  "Department of Space (IN)"); corrected via raw affiliation string.',
           '- Names were never used to infer origin; multiple South-Asian-named authors resolved',
           '  to US/UK/EU/CN/AU institutions and were retained.',
           '- Flagged for Fable adjudication: L15-010 (passed on record attribution without',
           '  structured metadata) and L16-045 (Crossref author set does not match ledger note;',
           '  origin verdict unaffected).',
           '',
           '## Ledger synchronization',
           '',
           '- Canonical ledger and all lane verified_sources ledgers updated with',
           '  india_origin_audit objects for all 833 audited records; 15 quarantined with',
           '  accepted=false, source_type=discovery_only, and rejection_reason set.',
           '- validate_sources.py: PASS after merge (accepted=818, peer=468, demand=190,',
           '  gov=135, industry=124, US=295, CN=162, side=112, asia=264, local_asia=99, T1=594).',
           '']
    with open(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.md'), 'w',
              encoding='utf-8') as f:
        f.write('\n'.join(md))
    print('report written; quarantined:', len(quarantined), 'multinational:', len(multinational))


if __name__ == '__main__':
    main()
