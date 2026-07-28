"""Diagnose queue-vs-ledger accepted mismatch before P2A dispatch."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8') as f:
    data = json.load(f)
recs = data['sources'] if isinstance(data, dict) and 'sources' in data else data
by_id = {r['id']: r for r in recs}

with open(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json'), encoding='utf-8') as f:
    queue = json.load(f)
queued = [sid for b in queue['batches'] for sid in b['source_ids']]

acc = [r for r in recs if r.get('accepted') is True]
print('ledger total:', len(recs))
print('ledger accepted:', len(acc))
print('queued:', len(queued))

qset = set(queued)
acc_ids = {r['id'] for r in acc}
print('accepted but not queued:', sorted(acc_ids - qset)[:30], '... n =', len(acc_ids - qset))
print('queued but not accepted: n =', len(qset - acc_ids))

r = by_id['L01-008']
print(json.dumps({k: r.get(k) for k in ['id', 'accepted', 'rejection_reason', 'notes',
                                        'canonical_key', 'title']},
                 ensure_ascii=False, indent=1)[:1200])
# check for duplicate canonical keys covering these ids
ck = {}
for rec in recs:
    ck.setdefault(rec.get('canonical_key'), []).append((rec['id'], rec.get('accepted')))
dups = [v for v in ck.values() if len(v) > 1]
print('canonical keys with >1 record:', len(dups), dups[:5])
