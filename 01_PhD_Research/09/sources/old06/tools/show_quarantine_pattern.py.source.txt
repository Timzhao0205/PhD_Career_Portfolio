"""Show how prefilter-quarantined records are encoded in canonical + lane ledgers."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8') as f:
    recs = json.load(f)

for rid in ['L01-006', 'L02-003']:
    for r in recs:
        if r['id'] == rid:
            print('=== canonical', rid, 'accepted=', r.get('accepted'))
            print(json.dumps({k: r.get(k) for k in
                              ['source_type', 'rejection_reason', 'india_origin_audit', 'notes']},
                             ensure_ascii=False, indent=1)[:1500])

with open(os.path.join(ROOT, '10_SOURCE_ATLAS/L01_verified_sources.json'), encoding='utf-8') as f:
    lane = json.load(f)
lane_recs = lane['sources'] if isinstance(lane, dict) and 'sources' in lane else lane
print('lane file type:', type(lane), 'records:', len(lane_recs))
for r in lane_recs:
    if r.get('id') == 'L01-006':
        print('=== lane L01-006 accepted=', r.get('accepted'))
        print(json.dumps({k: r.get(k) for k in
                          ['source_type', 'rejection_reason', 'india_origin_audit']},
                         ensure_ascii=False, indent=1)[:1200])
# how many lane records have audit field already
n_aud = sum(1 for r in lane_recs if r.get('india_origin_audit'))
print('L01 lane records with india_origin_audit:', n_aud)
