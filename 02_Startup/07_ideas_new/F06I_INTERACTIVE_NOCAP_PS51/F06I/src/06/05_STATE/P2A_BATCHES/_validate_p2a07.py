import json
from collections import Counter

with open('05_STATE/P2A_BATCHES/P2A-07_records.json', encoding='utf-8') as f:
    records = json.load(f)
with open('05_STATE/P2A_BATCHES/P2A-07_audit.json', encoding='utf-8') as f:
    audit = json.load(f)

rec_ids = [r['id'] for r in records['records']]
aud_ids = [e['id'] for e in audit['entries']]

print('records count:', len(rec_ids))
print('audit entries count:', len(aud_ids))
print('unique rec ids:', len(set(rec_ids)))
print('unique aud ids:', len(set(aud_ids)))
print('missing from audit:', set(rec_ids) - set(aud_ids))
print('extra in audit:', set(aud_ids) - set(rec_ids))
dupes = [x for x in aud_ids if aud_ids.count(x) > 1]
print('duplicate ids in audit:', set(dupes))

verdicts = Counter(e['verdict'] for e in audit['entries'])
print('verdict counts:', verdicts)

required = ['id', 'verdict', 'method', 'institutions', 'non_indian_affiliation_count', 'evidence_urls', 'useful_lead', 'notes']
bad = []
for e in audit['entries']:
    for k in required:
        if k not in e:
            bad.append((e.get('id'), k))
print('missing fields:', bad)
