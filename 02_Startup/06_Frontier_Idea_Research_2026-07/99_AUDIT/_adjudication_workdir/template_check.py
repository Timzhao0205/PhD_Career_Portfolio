import json, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
first = {}
for r in recs:
    first.setdefault(r['id'], r)
print(json.dumps(first['L05-001'], indent=1)[:2800])
print()
r = first['L08-029']
print('L08-029 geo:', r.get('geography'), '| demand_evidence_type:', r.get('demand_evidence_type'), '| type:', r.get('source_type'))
print('L08-029 claim:', (r.get('claim_supported') or '')[:300])
print()
# lane-ledger copy of a correctly encoded prefilter quarantine, for lane-file template
lane = json.load(open('10_SOURCE_ATLAS/L01_verified_sources.json', encoding='utf-8-sig'))
if isinstance(lane, dict): lane = lane.get('sources', [])
for x in lane:
    if x.get('id') == 'L01-006':
        print(json.dumps(x, indent=1)[:2400])
        break
