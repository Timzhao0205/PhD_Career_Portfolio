"""Merge P2A india-origin batch audit files into canonical + lane ledgers.

- Validates that every queued ID received exactly one valid verdict.
- Pass verdicts (verified_non_india_origin / verified_multinational_allowed):
  writes india_origin_audit onto the accepted record in canonical and lane
  ledgers, in the shape validate_sources.py requires.
- discovery_only verdicts: quarantines using the same pattern as the
  2026-07-12 prefilter (accepted=False, source_type=discovery_only,
  rejection_reason=india_origin_exclusion, audit status=excluded_india_origin).
- Prints per-lane and gate-relevant deltas; writes a machine summary to
  05_STATE/P2A_MERGE_SUMMARY.json for the orchestrator.

Run only after all 12 batch audit files exist.
"""
import datetime
import glob
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASS_VERDICTS = {'verified_non_india_origin', 'verified_multinational_allowed'}
QUARANTINE_NOTE = ('Quarantined by 2026-07 India-origin rule; may be used only to '
                   'discover an independent eligible source.')
RULE_TEXT = ('Entirely India-origin sources are ineligible; multinational academic '
             'coauthorship is allowed when a non-Indian affiliation is verified.')


def load(path):
    with open(path, encoding='utf-8-sig') as f:
        return json.load(f)


def save(path, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')


def main() -> int:
    queue = load(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json'))
    queued = {sid for b in queue['batches'] for sid in b['source_ids']}

    entries = {}
    problems = []
    for b in queue['batches']:
        path = os.path.join(ROOT, f"05_STATE/P2A_BATCHES/{b['batch_id']}_audit.json")
        if not os.path.exists(path):
            problems.append(f"missing audit file for {b['batch_id']}")
            continue
        audit = load(path)
        batch_ids = set(b['source_ids'])
        seen = set()
        for e in audit.get('entries', []):
            sid = e.get('id')
            v = e.get('verdict')
            if sid not in batch_ids:
                problems.append(f"{b['batch_id']}: unexpected id {sid}")
                continue
            if sid in seen:
                problems.append(f"{b['batch_id']}: duplicate id {sid}")
                continue
            seen.add(sid)
            if v not in PASS_VERDICTS and v != 'discovery_only':
                problems.append(f"{b['batch_id']}: {sid} invalid verdict {v}")
                continue
            if v in PASS_VERDICTS and not e.get('evidence_urls'):
                problems.append(f"{b['batch_id']}: {sid} pass verdict lacks evidence_urls")
                continue
            if (v == 'verified_multinational_allowed'
                    and int(e.get('non_indian_affiliation_count') or 0) < 1):
                problems.append(f"{b['batch_id']}: {sid} multinational lacks non-Indian count")
                continue
            e['audited_at'] = e.get('audited_at') or audit.get('audited_at') \
                or datetime.datetime.now(datetime.timezone.utc).isoformat()
            entries[sid] = e
        for sid in batch_ids - seen:
            problems.append(f"{b['batch_id']}: no verdict for {sid}")

    if problems:
        print('P2A MERGE BLOCKED')
        for p in problems[:60]:
            print('-', p)
        return 1
    assert set(entries) == queued

    def apply_to(rec):
        e = entries[rec['id']]
        v = e['verdict']
        if v in PASS_VERDICTS:
            rec['india_origin_audit'] = {
                'status': v,
                'audited_at': e['audited_at'],
                'methods': [e.get('method') or 'unspecified'],
                'institutions': e.get('institutions') or [],
                'non_indian_affiliation_count': int(e.get('non_indian_affiliation_count') or 0),
                'evidence_urls': e.get('evidence_urls') or [],
                'rule': RULE_TEXT,
                'notes': e.get('notes') or '',
            }
        else:
            rec['india_origin_audit'] = {
                'status': 'excluded_india_origin',
                'audited_at': e['audited_at'],
                'methods': [e.get('method') or 'unspecified'],
                'institutions': e.get('institutions') or [],
                'non_indian_affiliation_count': int(e.get('non_indian_affiliation_count') or 0),
                'evidence_urls': e.get('evidence_urls') or [],
                'rule': RULE_TEXT,
                'original_source_type': rec.get('source_type'),
                'useful_lead': e.get('useful_lead') or '',
                'notes': e.get('notes') or '',
            }
            rec['accepted'] = False
            rec['source_type'] = 'discovery_only'
            rec['rejection_reason'] = ('india_origin_exclusion: confirmed India-origin or '
                                       'India-only source; discovery/search lead only')
            notes = str(rec.get('notes') or '').strip()
            if QUARANTINE_NOTE not in notes:
                rec['notes'] = (notes + ' | ' if notes else '') + QUARANTINE_NOTE

    # canonical ledger: apply only to the accepted instance of each queued id
    canon_path = os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json')
    canon = load(canon_path)
    n_canon = 0
    for rec in canon:
        if rec.get('id') in entries and rec.get('accepted') is True:
            apply_to(rec)
            n_canon += 1

    # lane ledgers
    lane_files = sorted(glob.glob(os.path.join(ROOT, '10_SOURCE_ATLAS', '*verified_sources*.json')))
    n_lane = 0
    for lf in lane_files:
        lane = load(lf)
        lst = lane['sources'] if isinstance(lane, dict) and 'sources' in lane else lane
        changed = False
        for rec in lst:
            if rec.get('id') in entries and rec.get('accepted') is True:
                apply_to(rec)
                n_lane += 1
                changed = True
        if changed:
            save(lf, lane)

    save(canon_path, canon)

    verdicts = Counter(e['verdict'] for e in entries.values())
    accepted = [r for r in canon if r.get('accepted') is True]
    lane_counts = {f'L{i:02d}': sum(f'L{i:02d}' in (r.get('lane_ids') or []) for r in accepted)
                   for i in range(1, 17)}
    summary = {
        'merged_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'audited': len(entries),
        'verdicts': dict(verdicts),
        'canonical_records_updated': n_canon,
        'lane_records_updated': n_lane,
        'accepted_after': len(accepted),
        'lane_counts_after': lane_counts,
        'quarantined_ids': sorted(sid for sid, e in entries.items()
                                  if e['verdict'] == 'discovery_only'),
        'multinational_ids': sorted(sid for sid, e in entries.items()
                                    if e['verdict'] == 'verified_multinational_allowed'),
    }
    save(os.path.join(ROOT, '05_STATE/P2A_MERGE_SUMMARY.json'), summary)
    print('P2A MERGE OK', json.dumps(summary['verdicts']),
          'accepted_after=', len(accepted), 'canon_updated=', n_canon, 'lane_updated=', n_lane)
    return 0


if __name__ == '__main__':
    sys.exit(main())
