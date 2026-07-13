"""Analyze the elegance adjudication: surviving distinct concepts by market/lane."""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, '20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION.json'),
          encoding='utf-8-sig') as f:
    adj = json.load(f)
if isinstance(adj, dict):
    adj = adj.get('entries') or adj.get('seeds') or list(adj.values())[0]

seeds = {}
for tag, rel in [('A', 'P3R2_A_us_pain.json'), ('B', 'P3R2_B_china_pain.json'),
                 ('C', 'P3R2_C_dual_us_cn.json'), ('D', 'P3R2_D_wildcards.json'),
                 ('E', 'P3R2_E_jptwkr_side.json')]:
    with open(os.path.join(ROOT, '20_OPPORTUNITY_POOL', rel), encoding='utf-8-sig') as f:
        for s in json.load(f):
            seeds[s['idea_id']] = s

verdicts = Counter(e.get('verdict') for e in adj)
print('verdict counts:', dict(verdicts))

# Build duplicate clusters: map each seed to its canonical (duplicate_of or self)
canon_of = {}
for e in adj:
    i = e['idea_id']
    d = e.get('duplicate_of')
    canon_of[i] = d if d else i

survivors = [e for e in adj if e.get('verdict') in ('PROMOTE', 'FIX')]
# distinct concepts among survivors: collapse by canonical id
clusters = {}
for e in survivors:
    key = canon_of[e['idea_id']] or e['idea_id']
    clusters.setdefault(key, []).append(e['idea_id'])

print('surviving seeds:', len(survivors), '| distinct surviving concepts:', len(clusters))

mk = Counter()
lanes = Counter()
for key, members in clusters.items():
    # representative: the canonical if it survived, else first member
    rep = key if key in seeds and any(m == key for m in members) else members[0]
    s = seeds.get(rep) or seeds.get(members[0])
    mk[s.get('primary_market')] += 1
    lanes[s.get('primary_lane')] += 1

print('distinct survivors by market:', dict(mk))
print('distinct survivors by lane:', dict(sorted(lanes.items())))
us_cred = mk.get('US', 0) + mk.get('US+CN', 0)
cn_cred = mk.get('CN', 0) + mk.get('US+CN', 0)
print(f'credible US={us_cred} (need 36) | credible CN={cn_cred} (need 36) | '
      f'dual={mk.get("US+CN",0)} (need 24) | total={len(clusters)} (need 48) | '
      f'lanes={len(lanes)} (need 14)')

rejected_dupes = [e['idea_id'] for e in adj if e.get('verdict') == 'REJECT'
                  and canon_of[e['idea_id']] != e['idea_id']]
print('rejects that are duplicates of survivors:', len(rejected_dupes))
