import json, glob

files = sorted(glob.glob('30_SCREENING/EVIDENCE/P4-G*_sources.json'))
step2_candidates = []
step3_candidates = []
for fp in files:
    with open(fp, encoding='utf-8-sig') as f:
        data = json.load(f)
    recs = data if isinstance(data, list) else data.get('sources', [])
    for r in recs:
        if not r.get('accepted'):
            continue
        st = r.get('source_type')
        tier = r.get('tier')
        if st in {'buyer_procurement','government','national_lab','standard','regulator'} and tier != 'T1':
            step2_candidates.append((fp, r))
        elif st == 'company_filing' and tier == 'T2':
            step2_candidates.append((fp, r))
        elif tier in ('T2','T3') and st in {'trade_press','vendor_datasheet','market_industry'}:
            step3_candidates.append((fp, r))

print("STEP2 candidates:", len(step2_candidates))
for fp, r in step2_candidates:
    print(f"  {r['id']:20s} {fp:45s} type={r.get('source_type'):18s} tier={r.get('tier')} fetched={r.get('fetched')} idea={r.get('idea_ids')}")

print()
print("STEP3 candidates:", len(step3_candidates))
for fp, r in step3_candidates:
    print(f"  {r['id']:20s} {fp[-25:]:25s} type={r.get('source_type'):16s} tier={r.get('tier')} idea={r.get('idea_ids')}")
