"""Check for duplicate record IDs in the canonical ledger."""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8') as f:
    data = json.load(f)
recs = data['sources'] if isinstance(data, dict) and 'sources' in data else data

c = Counter(r['id'] for r in recs)
dups = {k: v for k, v in c.items() if v > 1}
print('total records:', len(recs), 'unique ids:', len(c), 'dup ids:', len(dups))
for k in list(dups)[:10]:
    print('---', k)
    for r in recs:
        if r['id'] == k:
            print('  accepted=', r.get('accepted'), '| ck=', r.get('canonical_key'),
                  '| title=', (r.get('title') or '')[:60])
