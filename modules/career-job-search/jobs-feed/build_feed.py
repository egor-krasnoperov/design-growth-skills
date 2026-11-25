"""Daily list of digital design vacancies for Job Finder.

Reads the open job dataset by Stapply (https://github.com/kalil0321/ats-scrapers, data under CC0 1.0),
keeps digital design roles, adds the place, work mode, level and requirement tags for the quick match,
and writes small JSON files by region and country. Posting texts are read only to find tags; they are
never written out. Every vacancy links to the employer's own posting.

Usage:
  python build_feed.py OUT_DIR                     # download from the dataset, then build
  python build_feed.py OUT_DIR --from candidates.parquet   # build from an earlier download
"""
import collections, datetime, hashlib, json, os, re, sys, time

DATASET = 'https://storage.stapply.ai/jobs/v1/all.parquet'
MANIFEST = 'https://storage.stapply.ai/jobs/v1/manifest.json'
MAX_ROWS = 150  # rows per file, so that a chat assistant can read one file at a time

low = lambda x: (x or '').lower() if isinstance(x, str) else ''

# --- Which titles are digital design roles -------------------------------------------------------
EXCL_TITLE = re.compile(
    r"graphic|motion|brand|interior|industrial|mechanical|hardware|packaging|fashion|apparel|footwear|garment|textile|softgoods|harness|"
    r"\bgame|level design|narrative|instructional|learning|curriculum|course|sound|lighting|\bcad\b|civil|electrical|electronic|pcb|chip|asic|circuit|\brf\b|rfic|mmic|"
    r"verification|physical design|analog|landscape|jewel|print|merchand|kitchen|floral|structural|hvac|piping|tooling|mold|cabinet|signage|exhibit|set design|costume|"
    r"furniture|retail design|store design|silicon|\bsoc\b|fpga|layout|solutions? design|network design|database design|test design|offer design|clinical|trial design|"
    r"pricing|data ?cent|architect|security design|optical|photonic|antenna|thermal|rtl|vehicle|automotive|process design|tool design|pipeline|bridge|road|water|drainage|"
    r"geotech|hydraul|substation|protection|cable|fib(er|re)|telecom|wireless|instrumentation|public realm|\bbim\b|mep\b|cdm|façade|facade|bathroom|"
    r"content design|ux writ|research|intern\b|internship|working student|apprentice|trainee|\[test|test ns|banco de talent|talent (pool|community|network)|"
    r"general application|open application|expression of interest|spontaneous|freelance pool|ai trainer|tutor|annotat|lettering|tattoo|nail|hair|makeup|cake|wedding|event|"
    r"electric|high voltage|\bav designer|audio|creative designer|communication designer|multimedia|social media|media designer|marketing designer|presentation|"
    r"web ?site designer|webdesigner|web designer|framer website|concept design|accessor|sport concept|eyewear|composite|urban|traffic|building|construction|cnc|"
    r"packag|ceramic|toy|watch|exterior|color ?& ?material|cmf\b|combat|gameplay|quest\b")
CLEAR = re.compile(r"product design|ux ?/ ?ui|ui ?/ ?ux|ux ?& ?ui|ui ?& ?ux|\bux designer|\bui designer|\bux design (lead|manager|director)|user experience designer|"
                   r"user interface designer|interaction designer|product designer|head of product design|director of product design|vp,? (of )?product design")
AMBIG = re.compile(r"design engineer|design technologist|\bdesigner\b|design (lead|manager|director)|head of (ux |experience |digital )?design|director,? (of )?design|"
                   r"vp,? (of )?design|vice president,? (of )?design|digital design|web design|experience design|service design")
STRONG = re.compile(r"figma|\bsketch\b|user research|usability|wireframe|design system|user experience|\bux\b|\bui\b|interaction design|saas|mobile app|web app|"
                    r"front-?end|user interface|user flows?|\bapp\b|platform|software|digital product")
DIGITAL = re.compile(r"figma|\bsketch\b|user research|usability|wireframe|prototyp|design system|user experience|\bux\b|\bui\b|interaction design|product design|"
                     r"saas|mobile app|web app|front-?end|react|typescript|\bcss\b|user interface|user journeys?|user flows?")
PHYSICAL = re.compile(r"revit|autocad|\bbim\b|construction site|civil engineer|solidworks|catia|\bcreo\b|ansys|altium|\bfea\b|gd&t|asme|piping|hvac|"
                      r"architectural design|interior design|landscape|tekla|garment|textile|apparel|footwear|fashion design|merchandis|packaging design|"
                      r"mechanical engineering|electrical engineering|schematic|enclosure|injection mold|tolerance analysis|cnc|machining|sheet metal")
# Sites that repost other companies' vacancies; recruiters on Manatal are left out by platform.
REPOSTERS = {'jobgether', 'urban ridge supplies', 'hirehire'}
RECRUITER = re.compile(r"recruit|staffing|talents?\b|headhunt|appointments|\bsearch\b|personalberatung|rekrytering|\bva\b|virtual assist", re.I)


def is_design_role(title, company, ats, desc):
    t, d = low(title), low(desc)
    if EXCL_TITLE.search(t) or not company or low(company) in REPOSTERS or ats == 'manatal':
        return False
    if CLEAR.search(t):
        if re.search(r'\bux\b|\bui\b|user experience|user interface|interaction', t):
            return True
        if len(d) > 300 and not STRONG.search(d):
            return False
        return len(set(PHYSICAL.findall(d))) < 2
    if AMBIG.search(t) and d:
        return len(set(DIGITAL.findall(d))) >= 2 and not PHYSICAL.search(d)
    return False


def role_of(title):
    t = low(title)
    if 'head of' in t: return 'head-of-design'
    if re.search(r'director|\bvp\b|vice president', t): return 'design-director'
    if 'manager' in t: return 'design-manager'
    if re.search(r'design engineer|design technologist', t): return 'design-engineer'
    if re.search(r'\bux\b|\bui\b|user experience|user interface|interaction|web design|digital design|experience design|service design', t) and 'product' not in t:
        return 'ux-ui-designer'
    return 'product-designer'


def level_of(title, role):
    t = low(title)
    if role in ('design-manager', 'head-of-design', 'design-director'): return 'leadership'
    if 'senior associate' in t: return 'middle'
    if re.search(r'junior|\bjr\b|associate|entry|graduate', t): return 'junior'
    if re.search(r'senior|\bsr\b|staff|principal|lead|founding|\biii\b|\biv\b|expert', t): return 'senior'
    if re.search(r'\bmid|\bii\b|intermediate', t): return 'middle'
    return None


# --- Place ----------------------------------------------------------------------------------------
COUNTRY = {'US': 'United States', 'CA': 'Canada', 'GB': 'United Kingdom', 'PT': 'Portugal', 'ES': 'Spain', 'FR': 'France', 'DE': 'Germany',
           'NL': 'Netherlands', 'BE': 'Belgium', 'IE': 'Ireland', 'IT': 'Italy', 'PL': 'Poland', 'CZ': 'Czechia', 'AT': 'Austria', 'CH': 'Switzerland',
           'SE': 'Sweden', 'DK': 'Denmark', 'NO': 'Norway', 'FI': 'Finland', 'EE': 'Estonia', 'LV': 'Latvia', 'LT': 'Lithuania', 'GR': 'Greece',
           'RO': 'Romania', 'HU': 'Hungary', 'BG': 'Bulgaria', 'HR': 'Croatia', 'RS': 'Serbia', 'UA': 'Ukraine', 'CY': 'Cyprus', 'MT': 'Malta',
           'LU': 'Luxembourg', 'SK': 'Slovakia', 'SI': 'Slovenia', 'IS': 'Iceland', 'MX': 'Mexico', 'BR': 'Brazil', 'AR': 'Argentina', 'CO': 'Colombia',
           'CL': 'Chile', 'PE': 'Peru', 'UY': 'Uruguay', 'CR': 'Costa Rica', 'EC': 'Ecuador', 'PA': 'Panama', 'DO': 'Dominican Republic',
           'GT': 'Guatemala', 'AE': 'United Arab Emirates', 'SA': 'Saudi Arabia', 'QA': 'Qatar', 'KW': 'Kuwait', 'BH': 'Bahrain', 'OM': 'Oman',
           'EG': 'Egypt', 'IL': 'Israel', 'JO': 'Jordan', 'LB': 'Lebanon', 'MA': 'Morocco', 'TN': 'Tunisia', 'TR': 'Türkiye', 'IN': 'India',
           'SG': 'Singapore', 'AU': 'Australia', 'NZ': 'New Zealand', 'JP': 'Japan', 'KR': 'South Korea', 'PH': 'Philippines', 'ZA': 'South Africa'}
REGION_OF = {}
for _r, _cs in {'NA': 'US CA', 'UK': 'GB', 'LATAM': 'MX BR AR CO CL PE UY CR EC PA DO GT BO PY VE SV HN NI PR JM TT',
                'MENA': 'AE SA QA KW BH OM EG IL JO LB MA TN DZ IQ LY PS YE TR',
                'EUROPE': 'AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE NO CH IS LI UA RS BA ME MK AL MD XK GE AM AD MC'}.items():
    for _c in _cs.split():
        REGION_OF[_c] = _r
CITY = {'london': 'GB', 'manchester': 'GB', 'edinburgh': 'GB', 'bristol': 'GB', 'new york': 'US', 'nyc': 'US', 'san francisco': 'US', 'seattle': 'US',
        'austin': 'US', 'boston': 'US', 'chicago': 'US', 'los angeles': 'US', 'denver': 'US', 'atlanta': 'US', 'miami': 'US', 'toronto': 'CA',
        'vancouver': 'CA', 'montreal': 'CA', 'lisbon': 'PT', 'lisboa': 'PT', 'berlin': 'DE', 'munich': 'DE', 'hamburg': 'DE', 'paris': 'FR',
        'madrid': 'ES', 'barcelona': 'ES', 'amsterdam': 'NL', 'dublin': 'IE', 'warsaw': 'PL', 'krakow': 'PL', 'stockholm': 'SE', 'copenhagen': 'DK',
        'helsinki': 'FI', 'tallinn': 'EE', 'prague': 'CZ', 'vienna': 'AT', 'zurich': 'CH', 'dubai': 'AE', 'abu dhabi': 'AE', 'riyadh': 'SA',
        'tel aviv': 'IL', 'cairo': 'EG', 'mexico city': 'MX', 'cdmx': 'MX', 'são paulo': 'BR', 'sao paulo': 'BR', 'buenos aires': 'AR',
        'bogotá': 'CO', 'bogota': 'CO', 'medellín': 'CO', 'medellin': 'CO', 'lima': 'PE', 'montevideo': 'UY', 'doha': 'QA', 'istanbul': 'TR'}
NAME_TO_CC = {v.lower(): k for k, v in COUNTRY.items()}
NAME_TO_CC.update({'uk': 'GB', 'england': 'GB', 'scotland': 'GB', 'usa': 'US', 'united states of america': 'US', 'uae': 'AE', 'turkey': 'TR',
                   'czech republic': 'CZ', 'brasil': 'BR', 'méxico': 'MX', 'deutschland': 'DE', 'españa': 'ES'})


def country_of(cc, location):
    cc = (cc or '').upper()
    if cc:
        return cc
    loc = low(location)
    for name, code in NAME_TO_CC.items():
        if re.search(r'\b' + re.escape(name) + r'\b', loc):
            return code
    for city, code in CITY.items():
        if city in loc:
            return code
    return None


def region_of(cc):
    return REGION_OF.get(cc, 'OTHER') if cc else None


def work_mode(workplace_type, is_remote, location):
    w, loc = low(workplace_type), low(location)
    if 'hybrid' in w or 'hybrid' in loc: return 'hybrid'
    if 'remote' in w or is_remote is True or 'remote' in loc: return 'remote'
    if w in ('onsite', 'on-site', 'on_site', 'office') or 'on-site' in loc or 'onsite' in loc: return 'onsite'
    return None


def remote_scope(mode, cc, location, desc):
    if mode != 'remote':
        return None
    text = low(location) + ' ' + low(desc)[:4000]
    if re.search(r'worldwide|anywhere in the world|work from anywhere|\bglobal(ly)? remote|remote[- ]first,? (anywhere|global)', text): return 'worldwide'
    if re.search(r'anywhere in (europe|the eu)|(within|across|from) (europe|the eu)|eu[- ]based|european time ?zones?|\bcet\b|\bemea\b|remote[^.]{0,40}europe|europe[^.]{0,40}remote', text): return 'EUROPE'
    if re.search(r'latam|latin america|south america', text): return 'LATAM'
    if re.search(r'(us|united states) (or|and) canada|north america', text): return 'NA'
    return cc  # remote within one country, or unknown when no country is known


def clean_place(location, cc, mode):
    raw = re.sub(r'(?i)\b(fully )?remote\b|\bjobs?\b|\bhybrid\b|\bon-?site\b|[()]', ' ', location or '')
    parts = [p.strip(' -–,') for p in re.split(r'[;|/]| or ', raw) if p.strip(' -–,')]
    cities = []
    for p in parts:
        first = re.split(r',', p)[0].strip()
        if first and not re.search(r'\d', first) and len(first) > 2 and low(first) not in NAME_TO_CC and first.upper() not in COUNTRY:
            if first not in cities:
                cities.append(first)
    country = COUNTRY.get(cc or '', cc or '')
    if not cities:
        return country or None
    place = cities[0] + (', ' + country if country and country != cities[0] else '')
    return place + (f' and {len(cities) - 1} more' if len(cities) > 1 else '')


# --- Requirement tags for the quick match ---------------------------------------------------------
SKILLS = {
    'figma': r'figma', 'design systems': r'design systems?|component librar', 'prototyping': r'prototyp',
    'usability testing': r'usability|user testing', 'user research': r'user research|user interviews|qualitative research|discovery research',
    'interaction design': r'interaction design|user flows?|user journeys?', 'ui design': r'visual design|ui design|interface design|pixel[- ]perfect',
    'mobile': r'mobile app|\bios\b|android|native app', 'web': r'web app|web application|responsive',
    'analytics and experiments': r'a/b test|experimentation|data[- ]informed|data[- ]driven|analytics|amplitude|mixpanel',
    'html and css': r'\bhtml\b|\bcss\b|front-?end (code|development)|\breact\b|coding', 'accessibility': r'accessibility|wcag|a11y',
    'workshops': r'workshops?|facilitat', 'motion': r'motion design|animation', 'ai products': r'\bllms?\b|generative ai|\bgenai\b|ai[- ]native|ai agents?|machine learning',
    'mentoring': r'mentor', 'end-to-end': r'end[- ]to[- ]end',
}
DOMAINS = {
    'fintech': r'fintech|banking|payments?\b|financial services|lending|neobank', 'e-commerce': r'e-?commerce|checkout|online retail',
    'consumer': r'\bb2c\b|consumer', 'b2b saas': r'\bb2b\b|saas|enterprise software', 'healthcare': r'health ?care|medical|clinical|patients?',
    'developer tools': r'developer tools|devtools|developers? experience|\bapis?\b', 'security': r'cyber ?security|security product',
    'marketplace': r'marketplace', 'travel': r'travel|hospitality', 'data products': r'data visuali[sz]ation|dashboards?',
    'crypto': r'crypto|blockchain|web3', 'education': r'edtech|education', 'gaming': r'\bgaming\b|video games?',
}
LANGS = ['german', 'french', 'spanish', 'portuguese', 'dutch', 'italian', 'polish', 'arabic', 'hebrew', 'swedish', 'danish', 'norwegian', 'finnish',
         'czech', 'japanese', 'mandarin']
YEARS = re.compile(r'(\d{1,2})\s*\+?\s*(?:-|–|to)?\s*(?:\d{1,2}\s*)?\+?\s*years?', re.I)


def tags_of(desc):
    d = low(desc)
    out = {'skills': sorted(k for k, p in SKILLS.items() if re.search(p, d)),
           'domains': sorted(k for k, p in DOMAINS.items() if re.search(p, d))}
    langs = []
    for lang in LANGS:
        for m in re.finditer(lang, d):
            ctx = d[max(0, m.start() - 80): m.end() + 80]
            if re.search(r'fluent|native|proficien|required|must|professional|business[- ]level|\bc1\b|\bc2\b|written and spoken', ctx):
                langs.append(lang); break
    out['languages'] = langs
    years = [int(m.group(1)) for m in YEARS.finditer(d)
             if 1 <= int(m.group(1)) <= 15 and re.search(r'experience|design|product', d[m.start(): m.end() + 60])]
    out['yearsMin'] = min(years) if years else None
    return out


# --- Build ----------------------------------------------------------------------------------------
def download(path):
    import duckdb
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute(f"""COPY (
        SELECT url, apply_url, title, company, ats_type, location, country_iso, is_remote, workplace_type,
               salary_min, salary_max, salary_currency, salary_period, posted_at, description
        FROM '{DATASET}'
        WHERE regexp_matches(lower(title), 'design') AND coalesce(is_stale, false) = false
    ) TO '{path}' (FORMAT parquet)""")


def snapshot_date():
    try:
        import urllib.request
        with urllib.request.urlopen(MANIFEST, timeout=30) as r:
            return json.load(r).get('generated_at')
    except Exception:
        return None


def build(candidates, out_dir, seen_path=None):
    import duckdb
    today = datetime.date.today().isoformat()
    seen = json.load(open(seen_path)) if seen_path and os.path.exists(seen_path) else {}
    cur = duckdb.connect().execute(f"select * from '{candidates}' order by posted_at desc nulls last")  # newest first, so a duplicate keeps the newest
    cols = [c[0] for c in cur.description]
    jobs, keys = [], set()
    for row in cur.fetchall():
        r = dict(zip(cols, row))
        if not is_design_role(r['title'], r['company'], r['ats_type'], r['description']):
            continue
        url = r['url'] or r['apply_url']
        if not url or not url.startswith('https://'):
            continue
        role = role_of(r['title'])
        cc = country_of(r['country_iso'], r['location'])
        mode = work_mode(r['workplace_type'], r['is_remote'], r['location'])
        scope = remote_scope(mode, cc, r['location'], r['description'])
        region = scope if scope in ('EUROPE', 'LATAM', 'NA') else ('WORLDWIDE' if scope == 'worldwide' else region_of(cc) or 'NOT_STATED')
        # The same posting is often published once per office; a remote one open to a region or the world counts once.
        key = (low(r['company']).split()[0] if r['company'] else '', low(r['title']).strip(), scope if scope in ('EUROPE', 'LATAM', 'NA', 'worldwide') else cc)
        if key in keys:
            continue
        keys.add(key)
        jid = hashlib.sha1(url.encode()).hexdigest()[:12]
        seen.setdefault(jid, today)
        salary = None
        if r['salary_min'] and r['salary_currency']:
            salary = {'min': int(r['salary_min']), 'max': int(r['salary_max'] or r['salary_min']), 'currency': r['salary_currency'],
                      'period': {'yearly': 'year', 'annual': 'year', 'monthly': 'month', 'hourly': 'hour'}.get(low(r['salary_period']), low(r['salary_period']) or 'year')}
        published = str(r['posted_at'])[:10] if r['posted_at'] else None
        tags = tags_of(r['description'])
        job = {'id': jid, 'title': r['title'].strip(), 'company': r['company'].strip(), 'place': clean_place(r['location'], cc, mode),
               'country': cc, 'region': region, 'workMode': mode, 'remoteScope': ('country:' + scope) if scope and len(scope) == 2 else
               (('region:' + scope) if scope in ('EUROPE', 'LATAM', 'NA') else scope), 'role': role, 'level': level_of(r['title'], role),
               'salary': salary, 'publishedAt': published, 'firstSeen': seen[jid], 'url': url, 'platform': r['ats_type'],
               'skills': tags['skills'], 'domains': tags['domains'], 'languages': tags['languages'], 'yearsMin': tags['yearsMin']}
        if RECRUITER.search(r['company']):
            job['recruiter'] = True
        jobs.append({k: v for k, v in job.items() if v not in (None, [], '')})
    # Files: one per region and country; remote jobs open to a whole region or the world get their own file.
    groups = collections.defaultdict(list)
    for j in jobs:
        rs = j.get('remoteScope', '')
        if rs.startswith('region:') or rs == 'worldwide':
            groups[(j['region'].lower(), 'remote')].append(j)
        else:
            groups[((j['region'] if j['region'] in ('NA', 'UK', 'EUROPE', 'LATAM', 'MENA') else 'other').lower(), j.get('country') or 'not-stated')].append(j)
    day_dir = os.path.join(out_dir, today)
    files = []
    for (region, key), rows in sorted(groups.items()):
        rows.sort(key=lambda j: j.get('publishedAt') or '', reverse=True)
        chunks = [rows]
        if len(rows) > MAX_ROWS:
            by_role = collections.defaultdict(list)
            for j in rows:
                by_role[j['role']].append(j)
            chunks = [v for _, v in sorted(by_role.items())]
        for chunk in chunks:
            for i in range(0, len(chunk), MAX_ROWS):
                part = chunk[i:i + MAX_ROWS]
                name = key + (('-' + part[0]['role']) if len(chunks) > 1 else '') + (f'-{i // MAX_ROWS + 1}' if len(chunk) > MAX_ROWS else '')
                rel = f'{region}/{name}.json'
                os.makedirs(os.path.join(day_dir, region), exist_ok=True)
                json.dump({'region': region.upper(), 'key': key, 'jobs': part}, open(os.path.join(day_dir, rel), 'w'), ensure_ascii=False, separators=(',', ':'))
                files.append({'path': rel, 'region': region.upper(), 'country': None if key in ('remote', 'not-stated') else key,
                              'remote': key == 'remote', 'role': part[0]['role'] if len(chunks) > 1 else None, 'rows': len(part)})
    index = {'date': today, 'generatedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
             'sourceSnapshot': snapshot_date(), 'jobs': len(jobs),
             'source': 'Open job dataset by Stapply (https://github.com/kalil0321/ats-scrapers), data under CC0 1.0. Each vacancy belongs to its employer; open the url for the posting.',
             'byRegion': dict(collections.Counter(j['region'] for j in jobs).most_common()),
             'fields': {'id': 'stable id from the posting url', 'place': 'city and country as far as known', 'country': 'ISO code',
                        'region': 'NA, UK, EUROPE, LATAM, MENA, WORLDWIDE, OTHER or NOT_STATED', 'workMode': 'remote, hybrid or onsite',
                        'remoteScope': 'where a remote job can be done: country:XX, region:XX or worldwide', 'role': 'role family', 'level': 'junior, middle, senior or leadership',
                        'salary': 'one stated range', 'publishedAt': 'date from the job platform', 'firstSeen': 'first day this list had the vacancy',
                        'skills, domains, languages, yearsMin': 'requirement keywords found in the posting, for the quick match; languages are the ones marked as required',
                        'recruiter': 'true when the poster looks like a recruitment agency'},
             'files': files}
    json.dump(index, open(os.path.join(day_dir, 'index.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({'date': today, 'index': f'{today}/index.json'}, open(os.path.join(out_dir, 'latest.json'), 'w'))
    if seen_path:
        live = {j['id'] for j in jobs}
        json.dump({k: v for k, v in seen.items() if k in live}, open(seen_path, 'w'))
    return index


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    src = sys.argv[sys.argv.index('--from') + 1] if '--from' in sys.argv else os.path.join(out, 'candidates.parquet')
    t = time.time()
    if '--from' not in sys.argv:
        download(src)
    idx = build(src, out, os.path.join(out, 'seen.json'))
    if '--from' not in sys.argv:
        os.remove(src)
    print(json.dumps({'jobs': idx['jobs'], 'files': len(idx['files']), 'byRegion': idx['byRegion'], 'seconds': round(time.time() - t)}))
