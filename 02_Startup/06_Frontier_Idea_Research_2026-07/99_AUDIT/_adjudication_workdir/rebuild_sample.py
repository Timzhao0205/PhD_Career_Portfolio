import json, os, io, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
first = {}
for r in recs:
    if r['id'] not in first:
        first[r['id']] = r  # authoritative copy is always first occurrence

sample = json.load(open('99_AUDIT/_adjudication_workdir/sample80.json', encoding='utf-8'))
out = {}
for sid in sample:
    r = first[sid]
    ia = r.get('india_origin_audit') or {}
    out[sid] = {
        'title': (r.get('title') or '')[:100],
        'type': r.get('source_type'),
        'doi': r.get('doi'),
        'url': r.get('url'),
        'method': ia.get('methods'),
        'status': ia.get('status'),
        'inst': [(i.get('name','')[:60], i.get('country')) for i in (ia.get('institutions') or [])],
        'n_nonIN': ia.get('non_indian_affiliation_count'),
        'evid': ia.get('evidence_urls'),
        'ia_notes': (ia.get('notes') or '')[:220],
    }
json.dump(out, open('99_AUDIT/_adjudication_workdir/sample80_authoritative.json', 'w', encoding='utf-8'), indent=1)

# Compact review print
issues = []
for sid, v in out.items():
    ok_status = v['status'] == 'verified_non_india_origin'
    has_method = bool(v['method'])
    has_evid = bool(v['evid'])
    has_inst = bool(v['inst'])
    flagline = []
    if not ok_status: flagline.append('BAD_STATUS')
    if not has_method: flagline.append('NO_METHOD')
    if not has_evid: flagline.append('NO_EVIDENCE_URL')
    if not has_inst: flagline.append('NO_INSTITUTIONS')
    if flagline: issues.append((sid, flagline))
    print(sid, '|', ','.join(v['method'] or ['-']), '|', v['status'], '| inst:', v['inst'][:3], '| evid:', len(v['evid'] or []))
print('\nISSUES:', issues if issues else 'none — all 80 have status+method+evidence')

# Full notes for specific records of interest
for sid in ['L07-020','L11-010','L03-026','L10-019','L13-009','L13-003']:
    r = first.get(sid)
    if not r: continue
    ia = r.get('india_origin_audit') or {}
    print('\n###', sid, (r.get('title') or '')[:80])
    print('doi:', r.get('doi'))
    print('methods:', ia.get('methods'), '| n_nonIN:', ia.get('non_indian_affiliation_count'))
    print('notes:', ia.get('notes'))
    print('evid:', ia.get('evidence_urls'))

# The 7 unencoded quarantines: print search keys
print('\n--- 7 unencoded quarantines search keys ---')
for sid in ['L01-010','L02-008','L03-054','L04-024','L05-025','L05-051','L08-023']:
    r = first[sid]
    print(sid, '|', (r.get('title') or '')[:120], '|', r.get('url'))
