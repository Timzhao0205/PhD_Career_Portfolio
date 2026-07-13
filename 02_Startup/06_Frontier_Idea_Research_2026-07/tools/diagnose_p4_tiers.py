"""Diagnose tier distribution of P4-added sources vs SOURCE_STANDARDS tier definitions."""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8-sig') as f:
    recs = json.load(f)

acc = [r for r in recs if r.get('accepted') is True]
p4 = [r for r in acc if str(r.get('id', '')).startswith('P3R2-')]
old = [r for r in acc if not str(r.get('id', '')).startswith('P3R2-')]

print('accepted total:', len(acc), '| P4-added:', len(p4), '| pre-P4:', len(old))
t1_old = sum(r.get('tier') == 'T1' for r in old)
t1_p4 = sum(r.get('tier') == 'T1' for r in p4)
print(f'pre-P4 T1: {t1_old}/{len(old)} = {t1_old/len(old):.1%}')
print(f'P4 T1: {t1_p4}/{len(p4)} = {t1_p4/len(p4):.1%}')

print('\nP4 source_type x tier:')
ct = Counter((r.get('source_type'), r.get('tier')) for r in p4)
for (st, t), n in sorted(ct.items()):
    print(f'  {st:25s} {t}: {n}')

# candidates for definitional T1 upgrade
T1_TYPES = {'buyer_procurement', 'government', 'national_lab', 'standard', 'regulator',
            'company_filing'}
upgradable = [r for r in p4 if r.get('source_type') in T1_TYPES and r.get('tier') != 'T1'
              and r.get('fetched') is True]
print('\nP4 records of definitional-T1 types currently tiered T2/T3:', len(upgradable))

# what-if: after upgrade
t1_after = t1_old + t1_p4 + len(upgradable)
print(f'T1 share after definitional upgrade: {t1_after}/{len(acc)} = {t1_after/len(acc):.1%}')

t3 = sum(r.get('tier') == 'T3' for r in acc)
print(f'T3 share: {t3}/{len(acc)} = {t3/len(acc):.1%} (max 15%)')

unfetched = [r['id'] for r in acc if not r.get('fetched')]
print('\naccepted but unfetched:', unfetched)

# peer-reviewed accepted with unverified status among p4
bad_peer = [r['id'] for r in p4 if r.get('source_type') == 'academic_peer_reviewed'
            and r.get('peer_review_status') != 'verified']
print('P4 academic with unverified peer review:', bad_peer)
