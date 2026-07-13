import json, os, io, sys, glob, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
first = {}
for r in recs:
    first.setdefault(r['id'], r)

prefx = ['L01-006','L01-010','L01-026','L01-041','L01-042','L01-054','L02-003','L02-008','L03-054','L04-024','L04-037','L04-105','L05-025','L05-051','L06-047','L07-033','L07-048','L08-023','L08-028','L09-035','L11-036','L11-053','L12-043','L13-034','L13-051','L14-052','L16-021']
fullq = ['L01-051','L01-052','L03-047','L03-049','L05-001','L06-053','L07-038','L07-039','L13-050','L14-011','L14-017','L14-023','L15-045','L16-008','L16-012']
excl = prefx + fullq

bad = []
for i in excl:
    r = first.get(i)
    ia = (r or {}).get('india_origin_audit') or {}
    if r is None: bad.append((i, 'missing')); continue
    if r.get('accepted') is not False: bad.append((i, 'accepted'))
    if r.get('source_type') != 'discovery_only': bad.append((i, 'type=' + str(r.get('source_type'))))
    if ia.get('status') != 'excluded_india_origin': bad.append((i, 'ia=' + str(ia.get('status'))))
    if not (r.get('rejection_reason') or '').strip(): bad.append((i, 'no rejection_reason'))
    if not ia.get('evidence_urls'): bad.append((i, 'no ia evidence_urls'))
print('CANONICAL 42-exclusion encoding problems:', bad if bad else 'NONE — all 42 fully encoded')

acc = [r for r in recs if r.get('accepted')]
noia = [r['id'] for r in acc if (r.get('india_origin_audit') or {}).get('status') != 'verified_non_india_origin']
print('canonical accepted:', len(acc), '| accepted lacking verified audit:', noia if noia else 'none')

# Lane ledgers: accepted records must carry completed audits; quarantined must be encoded.
lane_problems = []
lane_acc_total = 0
for lf in sorted(glob.glob('10_SOURCE_ATLAS/*verified_sources.json')):
    data = json.load(open(lf, encoding='utf-8-sig'))
    if isinstance(data, dict): data = data.get('sources', [])
    for r in data:
        rid = r.get('id')
        ia = r.get('india_origin_audit') or {}
        if r.get('accepted'):
            lane_acc_total += 1
            if ia.get('status') not in ('verified_non_india_origin', 'verified_multinational_allowed'):
                lane_problems.append((lf, rid, 'accepted without completed audit'))
        if rid in excl:
            if r.get('accepted') is not False: lane_problems.append((lf, rid, 'excluded but accepted'))
            if r.get('source_type') != 'discovery_only': lane_problems.append((lf, rid, 'excluded type=' + str(r.get('source_type'))))
            if ia.get('status') != 'excluded_india_origin': lane_problems.append((lf, rid, 'excluded ia=' + str(ia.get('status'))))
print('lane accepted records:', lane_acc_total)
print('lane problems:', lane_problems[:30] if lane_problems else 'NONE')

# L15-010 / L16-045 spot check
for rid in ['L15-010', 'L16-045']:
    r = first[rid]
    ia = r.get('india_origin_audit') or {}
    print(rid, '| url:', r.get('url'))
    print('   methods:', ia.get('methods'), '| inst:', [(x['name'][:45], x['country']) for x in ia.get('institutions', [])])
    print('   authors_or_org:', (r.get('authors_or_org') or '')[:110])
