import csv

EXPECTED_HEADER = ["source_id","citation","title","authors","year","venue","doi","url","source_type","peer_review_status","quality_tier","topic_tags","claims_supported","verification_basis","access_level","notes"]

path = 'evidence/10A_GAN_WBG_SOURCES.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data_rows = rows[1:]

errors = []
if header != EXPECTED_HEADER:
    errors.append('HEADER MISMATCH: ' + str(header))
else:
    print('Header: EXACT MATCH to SOURCE_POLICY.md (16 columns)')

print('Total data rows:', len(data_rows))

for r in data_rows:
    if len(r) != len(EXPECTED_HEADER):
        errors.append('Column count mismatch in row: ' + str(r[:2]))

dicts = [dict(zip(header, r)) for r in data_rows]

# uniqueness checks
sids = [d['source_id'] for d in dicts]
dois = [d['doi'] for d in dicts]
titles = [d['title'].strip().lower() for d in dicts]

def dupes(lst):
    seen = set(); dup = set()
    for x in lst:
        if x in seen:
            dup.add(x)
        seen.add(x)
    return dup

d_sid = dupes(sids)
d_doi = dupes(dois)
d_title = dupes(titles)
if d_sid: errors.append('Duplicate source_id: ' + str(d_sid))
if d_doi: errors.append('Duplicate doi: ' + str(d_doi))
if d_title: errors.append('Duplicate title: ' + str(d_title))
print('Duplicate source_id count:', len(d_sid))
print('Duplicate doi count:', len(d_doi))
print('Duplicate title count:', len(d_title))

# sequential source_id check
expected_ids = ['A' + str(i).zfill(4) for i in range(1, len(dicts)+1)]
if sids != expected_ids:
    errors.append('source_id not sequential A0001..A' + str(len(dicts)).zfill(4))
else:
    print('source_id sequential: A0001 - ' + sids[-1])

# required non-blank fields
required = ['citation','title','authors','year','venue','doi','url','source_type','peer_review_status','quality_tier','topic_tags','claims_supported','verification_basis','access_level']
blank_report = {}
for field in required:
    blanks = [d['source_id'] for d in dicts if not d[field].strip()]
    if blanks:
        blank_report[field] = blanks
        errors.append('Blank ' + field + ' in: ' + str(blanks))
print('Blank required-field report:', blank_report if blank_report else 'none')

# controlled vocab checks
bad_peer = [d['source_id'] for d in dicts if d['peer_review_status'] != 'verified_peer_reviewed']
bad_tier = [d['source_id'] for d in dicts if d['quality_tier'] not in ('A','B','C')]
bad_access = [d['source_id'] for d in dicts if d['access_level'] not in ('full_text','abstract_metadata','metadata_only')]
bad_url = [d['source_id'] for d in dicts if not d['url'].startswith('https://doi.org/')]
bad_doi_case = [d['source_id'] for d in dicts if d['doi'] != d['doi'].lower()]
bad_doi_url_match = [d['source_id'] for d in dicts if d['url'] != 'https://doi.org/' + d['doi']]

if bad_peer: errors.append('Bad peer_review_status: ' + str(bad_peer))
if bad_tier: errors.append('Bad quality_tier: ' + str(bad_tier))
if bad_access: errors.append('Bad access_level: ' + str(bad_access))
if bad_url: errors.append('Bad url prefix: ' + str(bad_url))
if bad_doi_case: errors.append('DOI not lowercase: ' + str(bad_doi_case))
if bad_doi_url_match: errors.append('URL does not match doi: ' + str(bad_doi_url_match))

print('peer_review_status all verified_peer_reviewed:', len(bad_peer) == 0)
print('quality_tier all in {A,B,C}:', len(bad_tier) == 0)
print('access_level all in {full_text,abstract_metadata,metadata_only}:', len(bad_access) == 0)
print('url all https://doi.org/ prefixed:', len(bad_url) == 0)
print('doi all lowercase:', len(bad_doi_case) == 0)
print('url matches https://doi.org/<doi> exactly:', len(bad_doi_url_match) == 0)

# year sanity check (numeric, plausible range)
bad_year = [d['source_id'] for d in dicts if not (d['year'].isdigit() and 1900 <= int(d['year']) <= 2026)]
if bad_year: errors.append('Bad year: ' + str(bad_year))
print('year numeric & in [1900,2026]:', len(bad_year) == 0)

print()
if errors:
    print('=== VALIDATION FAILED ===')
    for e in errors:
        print(' -', e)
else:
    print('=== VALIDATION PASSED: 0 errors ===')

print()
print('Row count:', len(dicts), '(floor=55, aim=65)')
print('PASS FLOOR:', len(dicts) >= 55)
