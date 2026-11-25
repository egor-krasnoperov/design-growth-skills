# Daily jobs list

A list of open digital design vacancies, rebuilt every morning from the open job dataset by [Stapply](https://github.com/kalil0321/ats-scrapers) (data under CC0 1.0) by the program in [`../../jobs-feed`](../../jobs-feed). Each vacancy belongs to its employer. The list keeps only short facts, requirement keywords and the link to the employer's posting, never the posting text.

## Reading the list

Base address: `https://raw.githubusercontent.com/egor-krasnoperov/design-growth-skills/jobs-feed/`

1. Read `latest.json` at the base address. It gives `date` (the day of the list) and `index`, the path of that day's index, for example `2026-11-25/index.json`.
2. Read the index. It has `jobs` (the total), `byRegion`, `fields` (a short description of each field) and `files`, a list of `{path, region, country, remote, role, rows}`. A file's address is the base address, the date folder and its `path`, for example `…/jobs-feed/2026-11-25/uk/GB-product-designer-1.json`.
3. Each file is `{region, key, jobs}` with up to 150 vacancies, newest first, and up to about 75 KB.

Folders are `na` (US and Canada), `latam`, `europe`, `uk`, `mena`, `worldwide` and `other` (every other country, and vacancies with no stated place).

- A country has one file, `<folder>/<COUNTRY>.json`. A large country has one file per role, `<COUNTRY>-<role>.json`, split into `-1`, `-2` and so on when a role has more than 150 vacancies. The first part of a role holds its newest vacancies.
- Remote vacancies open to a whole region are in `<folder>/remote.json`, those open anywhere in `worldwide/remote.json`. Remote vacancies limited to one country stay in that country's files. Not every region has a `remote.json`.
- Skip `other/not-stated-*.json`: their place is unknown.

**Which files to read for a place**

| The user's place | Files |
| --- | --- |
| A country | That country's files, its region's `remote.json` and `worldwide/remote.json` |
| A city | The country's files, keeping only vacancies whose `place` names the city, plus remote vacancies open to the country, its region or the world |
| A region | The files of the countries the user is open to, the region's `remote.json` and `worldwide/remote.json`. Ask which countries when the region is large |
| The UK | Also `europe/remote.json`. Those vacancies are open across Europe or EMEA; mark them as "check that the UK is included" |

For a large country, read only the files of the selected roles. Read one file at a time. In a chat without a work environment, read at most about four files (up to 600 vacancies), starting with the first part of each selected role and the remote files. Say which files were not read. With a work environment that has internet access, download all the needed files there and select and rank them in code.

## Fields of a vacancy

Empty fields are left out.

| Field | Meaning |
| --- | --- |
| `id` | Stable id made from the posting address (12 characters). Use it as the board's vacancy id |
| `title`, `company` | As on the job platform |
| `place` | City and country in English, as far as known, for example `London, United Kingdom` or `Berlin, Germany and 2 more` |
| `country` | ISO code |
| `region` | `NA`, `UK`, `EUROPE`, `LATAM`, `MENA`, `WORLDWIDE`, `OTHER` or `NOT_STATED` |
| `workMode` | `remote`, `hybrid` or `onsite`. Missing for about half of the vacancies; then the format is not stated |
| `remoteScope` | Only for remote vacancies: `country:XX`, `region:EUROPE` (also `LATAM`, `NA`) or `worldwide` |
| `role` | `product-designer`, `ux-ui-designer`, `design-engineer`, `design-manager`, `head-of-design`, `design-director` |
| `level` | `junior`, `middle`, `senior` or `leadership`, from the title. Missing when the title states no level |
| `salary` | `{min, max, currency, period}`, one stated range, when the platform gives one |
| `publishedAt` | Date from the job platform |
| `firstSeen` | First day the list had the vacancy |
| `url` | The employer's posting on its job platform |
| `platform` | `greenhouse`, `lever`, `ashby`, `workable` and others |
| `skills`, `domains` | Requirement keywords found in the posting, from the lists below |
| `languages` | Languages the posting marks as required (fluent, native, required and similar) |
| `yearsMin` | The smallest number of years of experience the posting asks for |
| `recruiter` | `true` when the poster looks like a recruitment agency |

The keywords are found by simple rules in the posting text. They miss things and sometimes catch words from the company description, so treat them as a rough picture of the requirements, not a reading of the posting.

## The profile

Write the profile from the CV with the same keyword names, so it can be compared with the vacancies. Add a keyword only when the CV shows it.

- **skills** — `figma`, `design systems`, `prototyping`, `usability testing`, `user research`, `interaction design`, `ui design`, `mobile`, `web`, `analytics and experiments`, `html and css`, `accessibility`, `workshops`, `motion`, `ai products`, `mentoring`, `end-to-end`.
- **domains** — `fintech`, `e-commerce`, `consumer`, `b2b saas`, `healthcare`, `developer tools`, `security`, `marketplace`, `travel`, `data products`, `crypto`, `education`, `gaming`.
- **languages** — the languages the person speaks at a working level, in English and lower case, for example `portuguese`. Required languages in the list come from `german`, `french`, `spanish`, `portuguese`, `dutch`, `italian`, `polish`, `arabic`, `hebrew`, `swedish`, `danish`, `norwegian`, `finnish`, `czech`, `japanese`, `mandarin`.
- **years** — years of experience in design roles, from the dates in the CV.
- The target roles, levels, places and work modes the user chose.

## Quick match

An approximate estimate of how many of the vacancy's requirement keywords the profile covers. It never replaces Match, which reads the whole posting.

Each requirement gets a weight and a credit.

| Requirement | Weight | Credit |
| --- | --- | --- |
| Skill `figma`, `prototyping`, `end-to-end`, `ui design`, `interaction design` or `web` (almost every posting names them) | 0.5 | full when the profile has it |
| Any other skill | 1 | full when the profile has it |
| Domain | 1 | full when the profile has it |
| Required language | 3 | full when the profile has it |
| `yearsMin` | 2 | full when the profile's years are enough, half when they are 1–2 years short, otherwise none |
| Level | 2 | full, or half when the title says Staff, Principal, Lead, Expert or Founding (a step above Senior), or Junior, Jr, Associate, Entry or Graduate. Always full for Design Manager, Head of Design and Design Director, where the role sets the level |

Quick match = credits ÷ weights × 100, rounded. Keep what matched, what matched partly and what is missing, to show next to the number.

- When a vacancy has fewer than four requirements (skills, domains, required languages and years together), mark it as having little data and put it after the others. Its number says little.
- Put recruiter postings after employer postings.
- Between equal numbers, put the newer `publishedAt` first.

For an assistant that can run code, the same rule in Python.

```python
import re

COMMON = {'figma', 'prototyping', 'end-to-end', 'ui design', 'interaction design', 'web'}
STEP = re.compile(r'\b(staff|principal|lead|expert|founding|junior|jr|associate|entry|graduate)\b', re.I)
LEADERSHIP = {'design-manager', 'head-of-design', 'design-director'}


def quick_match(job, profile):
    """job: one vacancy from the list. profile: {'skills', 'domains', 'languages', 'years'}."""
    items = []  # (label, weight, credit)
    for s in job.get('skills', []):
        w = 0.5 if s in COMMON else 1
        items.append((s, w, w if s in profile['skills'] else 0))
    for d in job.get('domains', []):
        items.append((d, 1, 1 if d in profile['domains'] else 0))
    for lang in job.get('languages', []):
        items.append((lang + ' (required)', 3, 3 if lang in profile['languages'] else 0))
    if job.get('yearsMin') is not None:
        gap = job['yearsMin'] - profile['years']
        items.append((f"{job['yearsMin']}+ years", 2, 2 if gap <= 0 else 1 if gap <= 2 else 0))
    requirements = len(items)
    step = job.get('role') not in LEADERSHIP and STEP.search(job['title'])
    items.append(('level', 2, 1 if step else 2))
    score = round(100 * sum(c for _, _, c in items) / sum(w for _, w, _ in items))
    return {
        'score': score,
        'lowData': requirements < 4,
        'matched': [l for l, w, c in items if l != 'level' and c == w],
        'partial': [l for l, w, c in items if l != 'level' and 0 < c < w],
        'missing': [l for l, w, c in items if l != 'level' and c == 0],
    }
```

Personal Job Board must use the same rule, so that its numbers match the chat.
