import json, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
RULE = 'Entirely India-origin sources are ineligible; multinational academic coauthorship is allowed when a non-Indian affiliation is verified.'
NOW = '2026-07-13T02:55:00+00:00'

SPECS = {
 'L01-013': dict(
    lane='10_SOURCE_ATLAS/L01_verified_sources.json',
    inst=[{'name': 'Huazhong University of Science and Technology', 'country': 'CN'},
          {'name': 'Ruhr University Bochum', 'country': 'DE'},
          {'name': 'Wuhan University of Technology', 'country': 'CN'}],
    n=8,
    evid=['https://api.openalex.org/works?filter=doi:10.1063/5.0226790&select=doi,title,authorships'],
    note=('Fable-5 P2A adjudication (2026-07-13): this lane record (accepted=true, doi:10.1063/5.0226790) '
          'was never merged into the canonical ledger as accepted (canonical holds only the earlier '
          'non-accepted URL-keyed draft) and therefore fell outside the 833-record P2A audit population. '
          'Origin now verified: all 8 authors resolve to CN (HUST x7, Wuhan UT) and DE (Ruhr Bochum, '
          'J. Schulze) institutions via OpenAlex; no Indian affiliation. This adjudication verifies '
          'origin only; canonical acceptance/count changes remain an orchestrator decision.')),
 'L06-030': dict(
    lane='10_SOURCE_ATLAS/L06_verified_sources.json',
    inst=[{'name': 'Advanced Research Center for Nanolithography (ARCNL) / Vrije Universiteit Amsterdam', 'country': 'NL'},
          {'name': 'University of Groningen', 'country': 'NL'}],
    n=5,
    evid=['https://api.openalex.org/works?filter=doi:10.1088/2040-8986/ac5a7e&select=doi,title,authorships'],
    note=('Fable-5 P2A adjudication (2026-07-13): this lane record (accepted=true, doi:10.1088/2040-8986/ac5a7e) '
          'is absent from the canonical ledger entirely and therefore fell outside the 833-record P2A audit '
          'population. Origin now verified: all 5 authors (Versolato, Sheil, Witte, Ubachs, Hoekstra) resolve '
          'to Dutch institutions (ARCNL/VU Amsterdam/Groningen) via OpenAlex; no Indian affiliation. This '
          'adjudication verifies origin only; canonical acceptance/count changes remain an orchestrator decision.')),
}

recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
for key in ['doi:10.1063/5.0226790', 'doi:10.1088/2040-8986/ac5a7e']:
    hits = [(r['id'], r.get('accepted')) for r in recs if str(r.get('canonical_key','')).lower() == key]
    print('canonical rows with key', key, '->', hits if hits else 'none')

for rid, spec in SPECS.items():
    data = json.load(open(spec['lane'], encoding='utf-8-sig'))
    done = False
    for r in data:
        if r.get('id') == rid and r.get('india_origin_audit') is None:
            r['india_origin_audit'] = {
                'status': 'verified_non_india_origin',
                'audited_at': NOW,
                'methods': ['openalex_affiliations'],
                'institutions': spec['inst'],
                'non_indian_affiliation_count': spec['n'],
                'evidence_urls': spec['evid'],
                'rule': RULE,
                'notes': spec['note'],
            }
            done = True
    open(spec['lane'], 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(rid, 'lane audit object written:', done)
