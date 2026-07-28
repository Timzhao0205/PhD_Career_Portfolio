import json, os, io, sys, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
for rid in ['L01-013', 'L06-030']:
    copies = [r for r in recs if r['id'] == rid]
    print('===', rid, '| canonical copies:', len(copies))
    for r in copies:
        ia = r.get('india_origin_audit') or {}
        print('  accepted:', r.get('accepted'), '| type:', r.get('source_type'), '| ia:', ia.get('status'),
              '| rej:', (r.get('rejection_reason') or '')[:100])
        print('  title:', (r.get('title') or '')[:100])
        print('  key:', r.get('canonical_key'))

# lane copies
for lf, rid in [('10_SOURCE_ATLAS/L01_verified_sources.json', 'L01-013'),
                ('10_SOURCE_ATLAS/L06_verified_sources.json', 'L06-030')]:
    data = json.load(open(lf, encoding='utf-8-sig'))
    for r in data:
        if r.get('id') == rid:
            ia = r.get('india_origin_audit') or {}
            print('LANE', lf, rid, '| accepted:', r.get('accepted'), '| ia:', ia.get('status'),
                  '| key:', r.get('canonical_key'))
            print('  title:', (r.get('title') or '')[:100])
            print('  notes:', (r.get('notes') or '')[:220])

# was the id audited at all? check audit json verdicts
audit = json.load(open('05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.json', encoding='utf-8'))
v = audit['verdicts']
for rid in ['L01-013', 'L06-030']:
    print(rid, 'in audit verdicts:', rid in v, v.get(rid, {}).get('verdict') if rid in v else '')
