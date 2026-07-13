import json, os, io, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
pos = collections.defaultdict(list)
for idx, r in enumerate(recs): pos[r['id']].append(idx)

prefx = ['L01-006','L01-010','L01-026','L01-041','L01-042','L01-054','L02-003','L02-008','L03-054','L04-024','L04-037','L04-105','L05-025','L05-051','L06-047','L07-033','L07-048','L08-023','L08-028','L09-035','L11-036','L11-053','L12-043','L13-034','L13-051','L14-052','L16-021']
for i in prefx:
    r = recs[pos[i][0]]
    ia = r.get('india_origin_audit') or {}
    print('='*90)
    print(i, '|', r.get('source_type'), '| ia:', ia.get('status'))
    print(' title:', (r.get('title') or '')[:130])
    print(' org:  ', (r.get('authors_or_org') or '')[:140])
    print(' url:  ', r.get('url'))
    print(' doi:  ', r.get('doi'))
    print(' geo:  ', r.get('geography'), '| year:', r.get('year'))
    print(' ia_inst:', ia.get('institutions'))
    print(' ia_evid:', ia.get('evidence_urls'))
    print(' ia_notes:', (ia.get('notes') or '')[:300])
    print(' claim:', (r.get('claim_supported') or '')[:180])
    print(' notes:', (r.get('notes') or '')[:300])
