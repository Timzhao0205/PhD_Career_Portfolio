import json, glob, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

PROBLEM = ['L01-010','L01-041','L01-042','L01-054','L02-008','L03-054','L04-024','L04-105',
           'L05-025','L05-051','L06-047','L08-023','L08-028','L09-035','L11-036','L14-052']
OK_PREF = ['L01-006','L01-026','L02-003','L04-037','L07-033','L07-048','L11-053','L12-043','L13-034','L13-051','L16-021']

lane_files = sorted(glob.glob('10_SOURCE_ATLAS/*verified_sources.json'))
print('lane files:', lane_files)

found = {}
for lf in lane_files:
    try:
        data = json.load(open(lf, encoding='utf-8-sig'))
    except Exception as e:
        print('ERR', lf, e); continue
    if isinstance(data, dict): data = data.get('sources', [])
    for r in data:
        rid = r.get('id')
        if rid in PROBLEM or rid in OK_PREF:
            ia = r.get('india_origin_audit') or {}
            found.setdefault(rid, []).append({
                'file': lf,
                'accepted': r.get('accepted'),
                'type': r.get('source_type'),
                'ia': ia.get('status'),
                'rej': (r.get('rejection_reason') or '')[:120],
                'notes_tail': (r.get('notes') or '')[-160:],
            })

for rid in PROBLEM:
    print('\n[PROBLEM]', rid)
    for s in found.get(rid, [{'file': 'NOT FOUND IN ANY LANE LEDGER'}]):
        print('  ', s)
for rid in OK_PREF:
    entries = found.get(rid, [])
    summ = [(s['file'], s['accepted'], s['type'], s['ia']) for s in entries]
    print('[OKPREF]', rid, summ if summ else 'NOT FOUND')
