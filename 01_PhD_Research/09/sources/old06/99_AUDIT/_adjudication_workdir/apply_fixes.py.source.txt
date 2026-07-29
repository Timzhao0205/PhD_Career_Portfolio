import json, os, io, sys, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

NOW = '2026-07-13T02:30:00+00:00'
RULE = 'Entirely India-origin sources are ineligible; multinational academic coauthorship is allowed when a non-Indian affiliation is verified.'
REJ = 'india_origin_exclusion: confirmed India-origin or India-only underlying technical claim; discovery/search lead only'
NOTE_SUFFIX = ' | Quarantined by 2026-07 India-origin rule; may be used only to discover an independent eligible source.'
ADJ = 'Encoded during Fable-5 P2A origin adjudication (2026-07-13): the 2026-07-12 prefilter flipped accepted=false but never recorded the quarantine encoding; origin independently verified by the adjudicator. '

FIX_A = ['L01-041','L01-042','L01-054','L04-105','L06-047','L08-028','L09-035','L11-036','L14-052']

FIX_B = {
 'L01-010': dict(
    methods=['openalex_affiliations'],
    institutions=[{'name': 'Indian Institute of Technology Hyderabad', 'country': 'IN'}],
    evidence_urls=['https://api.openalex.org/works?filter=doi:10.1016/j.ces.2022.118376&select=doi,authorships',
                   'https://api.crossref.org/works/10.1016/j.ces.2022.118376'],
    detail='All 6 authors (Rao, Bhargavi, Chawdhury, Ray, Vanjari, Subrahmanyam) resolve to IIT Hyderabad (IN) per OpenAlex raw affiliation strings. DOI 10.1016/j.ces.2022.118376 identified via Crossref bibliographic title search (record itself carried only ScienceDirect PII S0009250922009617).'),
 'L02-008': dict(
    methods=['openalex_affiliations'],
    institutions=[{'name': 'Indian Institute of Technology Ropar', 'country': 'IN'}],
    evidence_urls=['https://api.openalex.org/works?filter=doi:10.1016/j.mtcomm.2022.104244&select=doi,authorships',
                   'https://api.crossref.org/works/10.1016/j.mtcomm.2022.104244'],
    detail='All 4 authors (Shivani, Kaur, Ghosh, Kumar) carry the raw affiliation "FREM Laboratory, Department of Physics, Indian Institute of Technology Ropar, Punjab, India" per OpenAlex. DOI 10.1016/j.mtcomm.2022.104244; Crossref registers the container as Materials Today Communications (the ledger\'s "e-Prime journal" attribution was inaccurate).'),
 'L03-054': dict(
    methods=['org_identity_page'],
    institutions=[{'name': 'Institute for Plasma Research / Variable Energy Cyclotron Centre, Department of Atomic Energy, Government of India', 'country': 'IN'}],
    evidence_urls=['https://www.vecc.gov.in/sites/default/files/2023-06/SST-1_VECC_Jan22_15%20(1).pdf'],
    detail='Document is hosted on the Government of India vecc.gov.in domain and is produced by Indian national laboratories (IPR/VECC, DAE) about India\'s SST-1 tokamak; entirely India-origin on its face.'),
 'L04-024': dict(
    methods=['crossref_affiliations'],
    institutions=[{'name': 'Indira Gandhi Centre for Atomic Research (IGCAR), Kalpakkam', 'country': 'IN'}],
    evidence_urls=['https://api.crossref.org/works/10.1115/gtindia2019-2455'],
    detail='All 4 authors (Joseph, Kumar, Vasal, Theivarajan) carry the Crossref affiliation string "IGCAR Kalpakkam, Chennai, India". DOI 10.1115/gtindia2019-2455 identified via Crossref bibliographic search (record carried no DOI).'),
 'L05-025': dict(
    methods=['openalex_affiliations'],
    institutions=[{'name': 'Bhabha Atomic Research Centre (BARC), Mumbai', 'country': 'IN'}],
    evidence_urls=['https://api.openalex.org/works?filter=doi:10.1016/j.nima.2014.05.125&select=doi,authorships',
                   'https://api.crossref.org/works/10.1016/j.nima.2014.05.125'],
    detail='All 4 authors (Mishra, Ramarao, Pande, Singh) carry the raw affiliation "Ion Accelerator Development Division, Bhabha Atomic Research Centre, Mumbai, India" per OpenAlex. DOI 10.1016/j.nima.2014.05.125 identified via Crossref title search. Note: the record\'s org field said RRCAT; actual affiliation is BARC (both India-origin, verdict unchanged).'),
 'L05-051': dict(
    methods=['publisher_page'],
    institutions=[{'name': 'Raja Ramanna Centre for Advanced Technology (RRCAT), Indore', 'country': 'IN'}],
    evidence_urls=['https://www.cambridge.org/core/journals/international-journal-of-microwave-and-wireless-technologies/article/abs/design-and-characterization-of-50-kw-solidstate-rf-amplifier/D5F9E1B01EA1BB6CE561238369CE6377'],
    detail='Cambridge Core article page lists all 9 authors (Jain, Hannurkar, Sharma, Gupta, Tiwari, Lad, Kumar, Gupta, Pathak) at RRCAT Indore, India; amplifier designed for RRCAT\'s Indus-2 synchrotron. Record\'s "multinational" geography tag was wrong: source is entirely India-origin.'),
 'L08-023': dict(
    methods=['openalex_affiliations'],
    institutions=[{'name': 'Indian Institute of Technology Bombay', 'country': 'IN'}],
    evidence_urls=['https://api.openalex.org/works?filter=doi:10.1109/tpel.2023.3263004&select=doi,authorships'],
    detail='Both authors (G. A. Reddy, A. Shukla) resolve to IIT Bombay (IN) per OpenAlex. DOI 10.1109/tpel.2023.3263004 (IEEE Trans. Power Electronics 2023) identified via OpenAlex title search (record carried only the IEEE Xplore document number 10086620).'),
}
LANE_FILE = {
 'L01-010': '10_SOURCE_ATLAS/L01_verified_sources.json',
 'L02-008': '10_SOURCE_ATLAS/L02_verified_sources.json',
 'L03-054': '10_SOURCE_ATLAS/L03_verified_sources.json',
 'L04-024': '10_SOURCE_ATLAS/L04_verified_sources.json',
 'L05-025': '10_SOURCE_ATLAS/L05_verified_sources.json',
 'L05-051': '10_SOURCE_ATLAS/L05_verified_sources.json',
 'L08-023': '10_SOURCE_ATLAS/L08_verified_sources.json',
 'L16-045': '10_SOURCE_ATLAS/L16_verified_sources.json',
 'L15-010': '10_SOURCE_ATLAS/L15_verified_sources.json',
}

def encode_b(rec):
    rid = rec['id']
    spec = FIX_B[rid]
    orig_type = rec.get('source_type')
    rec['source_type'] = 'discovery_only'
    rec['accepted'] = False
    rec['rejection_reason'] = REJ
    notes = (rec.get('notes') or '').rstrip()
    if 'Quarantined by 2026-07 India-origin rule' not in notes:
        rec['notes'] = notes + NOTE_SUFFIX
    rec['india_origin_audit'] = {
        'status': 'excluded_india_origin',
        'audited_at': NOW,
        'methods': spec['methods'],
        'institutions': spec['institutions'],
        'non_indian_affiliation_count': 0,
        'evidence_urls': spec['evidence_urls'],
        'rule': RULE,
        'original_source_type': orig_type,
        'notes': ADJ + spec['detail'],
    }

def fix_l16045(rec):
    rec['authors_or_org'] = ('Yunda Wang; Ziyang Zhang; Tomoyasu Usui; Michael Benedict; Sakyo Hirose; '
        'Joseph Lee; Jamie Kalb; David Schwartz (PARC, A Xerox Company, Palo Alto, US; '
        'Murata Manufacturing Co., Ltd., Kyoto, JP)')
    cs = rec.get('claim_supported') or ''
    rec['claim_supported'] = cs.replace('(UCLA)', '(PARC, A Xerox Company + Murata Manufacturing)')
    rec['notes'] = (rec.get('notes') or '').rstrip() + (
        ' | P2A adjudication correction (2026-07-13): Crossref and OpenAlex both register DOI '
        '10.1126/science.aba2648 with authors Wang, Zhang, Usui, Benedict, Hirose, Lee, Kalb, '
        'Schwartz (PARC, A Xerox Company, US + Murata Manufacturing, JP). The prior '
        "'Qian, Suxin et al. (UCLA-affiliated)' attribution was a conflation with other "
        'caloric-cooling literature and has been corrected. Origin verdict unaffected (US/JP).')

def fix_l15010(rec):
    rec['url'] = 'https://meridian.allenpress.com/jmep/article/13/4/143/36623/'
    ia = rec.get('india_origin_audit') or {}
    methods = ia.get('methods') or []
    if 'publisher_page' not in methods:
        ia['methods'] = methods + ['publisher_page']
    inst = ia.get('institutions') or []
    if not any('Ozark' in (i.get('name') or '') for i in inst):
        inst.append({'name': 'Ozark Integrated Circuits, Inc., Fayetteville, AR', 'country': 'US'})
    ia['institutions'] = inst
    ev = ia.get('evidence_urls') or []
    for u in ['https://imapsjmep.org/article/39940',
              'https://www.ozarkic.com/2017/01/26/new-publication-extended-high-temperature-operation-of-silicon-carbide-cmos-circuits-for-venus-surface-application/']:
        if u not in ev:
            ev.append(u)
    ia['evidence_urls'] = ev
    ia['notes'] = (ia.get('notes') or '').rstrip() + (
        ' | Fable-5 P2A adjudication (2026-07-13): record-attribution alone did not meet the '
        'verified bar; independently confirmed. IMAPS JMEP mirror (imapsjmep.org/article/39940) '
        'confirms the exact article, author list, and vol 13(4) pp.143-154 (2016); Ozark '
        'Integrated Circuits (Fayetteville, AR, US) publicly claims the publication and team on '
        'its own site; H. A. Mantooth\'s group is University of Arkansas (US). No India '
        'connection in any source. Verdict verified_non_india_origin AFFIRMED with strengthened '
        'evidence. Article URL corrected: previous URL pointed to a different article page '
        '(jmep 15/4/163/36733).')
    rec['india_origin_audit'] = ia
    rec['notes'] = (rec.get('notes') or '').rstrip() + (
        ' | P2A adjudication (2026-07-13): article URL corrected to the JMEP vol 13(4) '
        'pp.143-154 article page; previous URL pointed to jmep/article/15/4/163 (a different '
        'article).')

# ---- canonical ledger ----
path = '90_BIBLIOGRAPHY/sources.json'
recs = json.load(open(path, encoding='utf-8'))
seen = set()
log = []
for rec in recs:
    rid = rec['id']
    if rid in seen:
        continue  # never touch stale duplicate copies
    seen.add(rid)
    if rid in FIX_A:
        ia = rec.get('india_origin_audit') or {}
        if rec.get('source_type') != 'discovery_only':
            if 'original_source_type' not in ia:
                ia['original_source_type'] = rec.get('source_type')
            rec['source_type'] = 'discovery_only'
            rec['india_origin_audit'] = ia
            log.append(f'A {rid}: canonical source_type -> discovery_only (was {ia["original_source_type"]})')
    elif rid in FIX_B:
        encode_b(rec)
        log.append(f'B {rid}: canonical full quarantine encoding applied')
    elif rid == 'L16-045':
        fix_l16045(rec)
        log.append('C L16-045: canonical authorship corrected to PARC/Murata per Crossref')
    elif rid == 'L15-010':
        fix_l15010(rec)
        log.append('D L15-010: canonical evidence strengthened + URL corrected')
open(path, 'w', encoding='utf-8').write(json.dumps(recs, ensure_ascii=False, indent=2) + '\n')

# ---- lane ledgers ----
by_lane = {}
for rid, lf in LANE_FILE.items():
    by_lane.setdefault(lf, []).append(rid)
for lf, rids in by_lane.items():
    data = json.load(open(lf, encoding='utf-8-sig'))
    assert isinstance(data, list)
    for rec in data:
        rid = rec.get('id')
        if rid in rids:
            if rid in FIX_B:
                encode_b(rec)
                log.append(f'B {rid}: lane {lf} encoding applied')
            elif rid == 'L16-045':
                fix_l16045(rec)
                log.append(f'C L16-045: lane {lf} authorship corrected')
            elif rid == 'L15-010':
                fix_l15010(rec)
                log.append(f'D L15-010: lane {lf} evidence strengthened + URL corrected')
    open(lf, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

print('\n'.join(log))
print(f'total fixes logged: {len(log)}')
