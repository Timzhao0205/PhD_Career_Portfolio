import json, glob

files = sorted(glob.glob('30_SCREENING/EVIDENCE/P4-G*_sources.json'))
targets = {
 'P3R2-A-05-S03','P3R2-A-10-S02','P3R2-A-10-S03','P3R2-A-10-S04',
 'P3R2-A-11-S02','P3R2-A-11-S03','P3R2-A-11-S04','P3R2-C-09-S03',
 'P3R2-C-12-S03','P3R2-D-08-S02','P3R2-F-07-S04',
 'P3R2-A-03-S03','P3R2-C-09-S02','P3R2-E-02-S06'
}
for fp in files:
    with open(fp, encoding='utf-8-sig') as f:
        data = json.load(f)
    recs = data if isinstance(data, list) else data.get('sources', [])
    hits = [r['id'] for r in recs if r.get('id') in targets]
    if hits:
        print(fp, '->', hits)
