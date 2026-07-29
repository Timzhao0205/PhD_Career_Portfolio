import json, collections, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
WD = os.path.join(ROOT, '99_AUDIT', '_adjudication_workdir')

recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
byid = {r['id']: r for r in recs}
audit = json.load(open('05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.json', encoding='utf-8'))
verdicts = audit['verdicts']
print('audit meta:', {k: audit[k] for k in ['canonical_records_reviewed','accepted_before_full_audit','accepted_after_full_audit','full_audit_verdict_counts','multinational_exception_ids','total_excluded_ids'] if k in audit})
print('n verdict entries:', len(verdicts))
vk = list(verdicts.items())[0] if isinstance(verdicts, dict) else verdicts[0]
print('verdict sample:', json.dumps(vk)[:400])

lanes = sorted({r['id'].split('-')[0] for r in recs})
print('lanes:', lanes)

accepted = [r for r in recs if r.get('accepted')]
print('accepted count:', len(accepted))

ACADEMIC = {'academic_peer_reviewed'}
sample = {}
for lane in lanes:
    lane_acc = sorted([r for r in accepted if r['id'].startswith(lane + '-')], key=lambda r: r['id'])
    first5 = lane_acc[:5]
    types = [r.get('source_type') for r in first5]
    if all(t in ACADEMIC for t in types):
        nonac = next((r for r in lane_acc if r.get('source_type') not in ACADEMIC), None)
        if nonac:
            first5 = first5[:4] + [nonac]
    sample[lane] = [r['id'] for r in first5]

total = sum(len(v) for v in sample.values())
print('sample size:', total)
for lane, ids in sample.items():
    print(lane, ids)

out = {}
for lane, ids in sample.items():
    for i in ids:
        r = byid[i]
        ia = r.get('india_origin_audit', {})
        out[i] = {
            'title': r.get('title','')[:110],
            'source_type': r.get('source_type'),
            'url': r.get('url'),
            'doi': r.get('doi'),
            'authors_or_org': r.get('authors_or_org','')[:120],
            'audit': ia,
        }
json.dump(out, open(os.path.join(WD,'sample80.json'),'w', encoding='utf-8'), indent=1)
print('wrote sample80.json')

prefx = ['L01-006','L01-010','L01-026','L01-041','L01-042','L01-054','L02-003','L02-008','L03-054','L04-024','L04-037','L04-105','L05-025','L05-051','L06-047','L07-033','L07-048','L08-023','L08-028','L09-035','L11-036','L11-053','L12-043','L13-034','L13-051','L14-052','L16-021']
fullq = ['L01-051','L01-052','L03-047','L03-049','L05-001','L06-053','L07-038','L07-039','L13-050','L14-011','L14-017','L14-023','L15-045','L16-008','L16-012']
excl = prefx + fullq
print('n excluded:', len(excl))
exc_out = {}
for i in excl:
    r = byid.get(i)
    if r is None:
        exc_out[i] = 'MISSING FROM LEDGER'
        continue
    ia = r.get('india_origin_audit', {})
    exc_out[i] = {
        'accepted': r.get('accepted'),
        'source_type': r.get('source_type'),
        'ia_status': ia.get('status'),
        'rejection_reason': (r.get('rejection_reason') or '')[:220],
        'title': r.get('title','')[:90],
        'authors_or_org': r.get('authors_or_org','')[:110],
        'url': r.get('url'),
        'ia_institutions': ia.get('institutions'),
        'ia_evidence': ia.get('evidence_urls'),
        'ia_notes': (ia.get('notes') or '')[:280],
    }
json.dump(exc_out, open(os.path.join(WD,'excluded42.json'),'w', encoding='utf-8'), indent=1)
print('wrote excluded42.json')

for fid in ['L15-010','L16-045']:
    r = byid.get(fid)
    print('\n=== ', fid, ' ===')
    print(json.dumps(r, indent=1)[:3200])

big = []
for r in accepted:
    ia = r.get('india_origin_audit', {})
    n = ia.get('non_indian_affiliation_count')
    if r.get('source_type') in ACADEMIC and isinstance(n, int) and n >= 8:
        big.append((r['id'], n, r.get('doi'), (ia.get('notes') or '')[:150]))
big.sort(key=lambda x: -x[1])
print('\nbig author lists (top 15):')
for b in big[:15]: print(b)

bad = [r['id'] for r in accepted if r.get('india_origin_audit',{}).get('status') != 'verified_non_india_origin']
print('\naccepted without verified status:', bad[:20], 'count', len(bad))
ver_not_acc = [r['id'] for r in recs if r.get('india_origin_audit',{}).get('status')=='verified_non_india_origin' and not r.get('accepted')]
print('verified but not accepted (other-reason rejects):', len(ver_not_acc), ver_not_acc[:10])
enc_bad = []
for i in excl:
    r = byid.get(i)
    if not r: enc_bad.append((i,'missing')); continue
    ia = r.get('india_origin_audit', {})
    if r.get('accepted') is not False: enc_bad.append((i,'accepted!=False'))
    if r.get('source_type') != 'discovery_only': enc_bad.append((i,'source_type='+str(r.get('source_type'))))
    if ia.get('status') != 'excluded_india_origin': enc_bad.append((i,'ia_status='+str(ia.get('status'))))
    if not (r.get('rejection_reason') or '').strip(): enc_bad.append((i,'empty rejection_reason'))
print('\nencoding problems in 42 excluded:', enc_bad if enc_bad else 'NONE')

# audited coverage: all 833 have india_origin_audit?
no_audit = [r['id'] for r in recs if r.get('india_origin_audit') is None]
print('\nrecords with no india_origin_audit object:', len(no_audit))
statuses = collections.Counter((r.get('india_origin_audit') or {}).get('status') for r in recs)
print('status distribution across ledger:', dict(statuses))
