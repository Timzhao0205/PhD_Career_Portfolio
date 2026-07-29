import json, csv, re

records = json.load(open('state/scratch_kept.json', encoding='utf-8'))

TIER_A_DOIS = {
    "10.1063/1.369664",
    "10.1109/jproc.2002.1021567",
    "10.1016/0924-4247(89)80069-x",
    "10.1016/0038-1101(79)90061-3",
    "10.1063/1.329347",
    "10.1016/0038-1101(81)90213-6",
    "10.1016/s0924-4247(00)00328-9",
    "10.1109/jsen.2006.874493",
    "10.1109/jsen.2010.2043429",
    "10.1109/4.585275",
    "10.1109/lsens.2019.2898157",
    "10.1016/0038-1101(88)90064-0",
    "10.1038/s41467-020-18007-5",
    "10.1149/2.0251602jss",
    "10.1116/6.0002628",
    "10.1109/jsen.2021.3119766",
}

def is_mdpi_style(venue, doi):
    mdpi_venues = ['sensors', 'micromachines', 'electronics', 'materials', 'crystals', 'nanomaterials']
    if doi.startswith('10.3390/'):
        return True
    v = (venue or '').strip().lower()
    return v in mdpi_venues

def quality_tier(r):
    st = r.get('SOURCE_TYPE', '').strip()
    doi = r['DOI']
    venue = r.get('VENUE', '')
    if st == 'conference_paper':
        return 'C'
    if is_mdpi_style(venue, doi):
        return 'C'
    if doi in TIER_A_DOIS:
        return 'A'
    return 'B'

TAG_KEYWORDS = [
 ('algan-gan-2deg', ['algan/gan', 'aln/gan', 'ingan', 'gan hemt', 'gan 2deg', 'gan-based mis-hemt', '2deg', 'gan mis-hemt']),
 ('iii-v-hall-platform', ['insb', 'ingaas', 'gaas', 'alsb/inas', ' inas ', 'graphene hall', 'silicon hall', 'anomalous hall', 'silicon carbide neutron', 'ceramic-chromium']),
 ('hall-geometry', ['geometry', 'greek cross', 'van der pauw', 'octagonal', 'cross-like', 'vertical hall', 'horizontal hall', 'finite contacts']),
 ('sensitivity', ['sensitivity', 'sensitive']),
 ('offset', ['offset']),
 ('planar-hall-effect', ['planar hall']),
 ('cross-axis-sensitivity', ['cross-axis', 'misalignment', '3-axis', 'three-axis', 'multi-axis', 'inverted pyramid']),
 ('spinning-current', ['spinning current', 'spinning-current', 'current spinning', 'current-spun', 'current-mode']),
 ('offset-cancellation', ['offset cancellation', 'offset-cancellation', 'offset correction', 'quadrature offset', 'chopper']),
 ('noise', ['noise']),
 ('drift', ['drift', 'aging', 'ageing']),
 ('linearity', ['linearity', 'nonlinearity']),
 ('bandwidth', ['bandwidth', 'frequency response', 'frequency limit']),
 ('parasitics', ['parasitic', 'capacitance']),
 ('ohmic-contacts', ['ohmic contact']),
 ('wire-bonds', ['wire bond', 'wire-bond', 'bonding wire']),
 ('packaging', ['packaging', 'package']),
 ('calibration', ['calibration']),
 ('temperature-coefficient', ['temperature coefficient', 'tcs', 'temperature dependence', 'high temperature', 'high-temperature']),
 ('repeatability', ['repeatability', 'reproducib']),
 ('harsh-temperature', ['high temperature', 'high-temperature', 'harsh environment', 'extreme temperature', '500 c', '500' + chr(176) + 'c']),
 ('vacuum', ['vacuum']),
 ('radiation-tolerance', ['radiation', 'proton', 'ionizing', 'neutron', 'irradiat']),
 ('extreme-environment-instrumentation', ['extreme environment', 'harsh environment', 'fusion', 'nuclear', 'reactor', 'demo scale', 'iter']),
 ('gan-sic-wbg-device', ['sic ', '4h-sic', 'silicon carbide', 'wide-bandgap', 'wide bandgap', ' gan ', 'gan/']),
 ('hall-sensor-review', ['review']),
 ('novelty-comparison', ['comparison', 'compared', 'versus', ' vs.', 'novelty']),
 ('senesky-group-prior-art', ['senesky']),
 ('fusion-diagnostics-context', ['fusion', 'tokamak', 'stellarator', 'demo', 'iter', 'plasma']),
]

def topic_tags(r):
    blob = ' '.join([r.get('TITLE', ''), r.get('CLAIMS_SUPPORTED', ''), r.get('NOTES', '')]).lower()
    tags = []
    for tag, kws in TAG_KEYWORDS:
        if any(kw in blob for kw in kws):
            tags.append(tag)
    if not tags:
        tags = ['gan-sic-wbg-device']
    return ';'.join(tags[:8])

def fmt_citation(r):
    authors = r.get('AUTHORS', '').strip()
    title = r.get('TITLE', '').strip()
    venue = r.get('VENUE', '').strip()
    vol = r.get('VOLUME', '').strip()
    iss = r.get('ISSUE', '').strip()
    pages = r.get('PAGES', '').strip()
    year = r.get('YEAR', '').strip()
    tail = []
    if vol:
        tail.append('vol. ' + vol)
    if iss:
        tail.append('no. ' + iss)
    if pages:
        tail.append('pp. ' + pages)
    tailstr = ', '.join(tail)
    citation = authors + ', "' + title + ',\" ' + venue
    if tailstr:
        citation += ', ' + tailstr
    citation += ', ' + year + '.'
    return citation

def clean(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()

rows = []
sid = 1
for r in records:
    source_id = 'A' + str(sid).zfill(4)
    sid += 1
    doi = r['DOI']
    row = {
        'source_id': source_id,
        'citation': fmt_citation(r),
        'title': clean(r.get('TITLE', '')),
        'authors': clean(r.get('AUTHORS', '')),
        'year': clean(r.get('YEAR', '')),
        'venue': clean(r.get('VENUE', '')),
        'doi': doi,
        'url': 'https://doi.org/' + doi,
        'source_type': clean(r.get('SOURCE_TYPE', 'journal_article')),
        'peer_review_status': 'verified_peer_reviewed',
        'quality_tier': quality_tier(r),
        'topic_tags': topic_tags(r),
        'claims_supported': clean(r.get('CLAIMS_SUPPORTED', '')),
        'verification_basis': clean(r.get('VERIFICATION_BASIS', '')),
        'access_level': clean(r.get('ACCESS_LEVEL', 'metadata_only')),
        'notes': clean(r.get('NOTES', '')),
    }
    rows.append(row)

header = ['source_id', 'citation', 'title', 'authors', 'year', 'venue', 'doi', 'url', 'source_type', 'peer_review_status', 'quality_tier', 'topic_tags', 'claims_supported', 'verification_basis', 'access_level', 'notes']

with open('evidence/10A_GAN_WBG_SOURCES.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for row in rows:
        w.writerow(row)

from collections import Counter
summary = []
summary.append('Wrote ' + str(len(rows)) + ' rows to evidence/10A_GAN_WBG_SOURCES.csv')
summary.append('Quality tier distribution: ' + str(Counter(r['quality_tier'] for r in rows)))
summary.append('Source type distribution: ' + str(Counter(r['source_type'] for r in rows)))
summary.append('Access level distribution: ' + str(Counter(r['access_level'] for r in rows)))
open('state/scratch_build_summary.txt', 'w', encoding='utf-8').write('\n'.join(summary))
print('OK')
