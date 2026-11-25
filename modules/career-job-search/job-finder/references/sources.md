# Candidate vacancy sources

The source list below was compiled on 2026-11-19 from design job boards collected by the author and additional research. Entries are candidates, not integrations or a promise of access, freshness, completeness, or permission to scrape. Recheck each source when used.

| Source | Checked direct address |
| --- | --- |
| Woody Jobs | [https://www.woodyjobs.com/](https://www.woodyjobs.com/) |
| Wellfound (AngelList) | [https://wellfound.com/jobs](https://wellfound.com/jobs) |
| Design Jobs Board | [https://www.designjobsboard.com/](https://www.designjobsboard.com/) |
| DesignX Jobs | [https://designx.community/jobs](https://designx.community/jobs) |
| EU Remote Jobs | [https://euremotejobs.com/](https://euremotejobs.com/) |
| Get on Board | [https://getonbrd.com/](https://getonbrd.com/) |
| NoDesk | [https://nodesk.co/remote-jobs/](https://nodesk.co/remote-jobs/) |
| WeLoveProduct | [https://weloveproduct.co/](https://weloveproduct.co/) |
| Startup Jobs | [https://startup.jobs/](https://startup.jobs/) |
| TopStartups | [https://topstartups.io/jobs/](https://topstartups.io/jobs/) |
| UI/UX Jobs Board | [https://uiuxjobsboard.com/](https://uiuxjobsboard.com/) |
| Uxcel Jobs | [https://app.uxcel.com/jobs](https://app.uxcel.com/jobs) |
| JobFluent | [https://www.jobfluent.com/](https://www.jobfluent.com/) |
| Work in Startups | [https://workinstartups.com/](https://workinstartups.com/) |
| Working Nomads | [https://www.workingnomads.com/jobs](https://www.workingnomads.com/jobs) |
| Y Combinator Jobs | [https://www.ycombinator.com/jobs/](https://www.ycombinator.com/jobs/) |
| Design Engineer Jobs | [https://designengineer.io/](https://designengineer.io/) |
| Design Code Jobs | [https://designcodejobs.com/](https://designcodejobs.com/) |
| Dribbble Jobs | [https://dribbble.com/jobs](https://dribbble.com/jobs) |
| Remotive | [https://remotive.com/remote-jobs/design](https://remotive.com/remote-jobs/design) |
| We Work Remotely | [https://weworkremotely.com/categories/remote-design-jobs](https://weworkremotely.com/categories/remote-design-jobs) |
| Himalayas | [https://himalayas.app/jobs/design](https://himalayas.app/jobs/design) |
| Accel Job Board | [https://jobs.accel.com/jobs](https://jobs.accel.com/jobs) |
| Khosla Ventures Job Board | [https://jobs.khoslaventures.com/jobs](https://jobs.khoslaventures.com/jobs) |
| DesignerJobs | [https://designerjobs.co/](https://designerjobs.co/) |
| Authentic Jobs | [https://authenticjobs.com/](https://authenticjobs.com/) |
| UX Jobs Board | [https://www.uxjobsboard.com/](https://www.uxjobsboard.com/) |

Additional channels: employer career pages and the public job platform addresses below, for identified employers, not global searches. Use each source only within its current access and usage conditions.

At the last check in November 2026 DesignX returned an empty accessible view, Work in Startups required a human check, and Woody Jobs and Personio career pages refused the reading tool in claude.ai. Remote geography, individual vacancy freshness and the original employer posting still need verification.

## Checking a posting on its job platform

Many employers publish vacancies through Greenhouse, Lever, Workable or Ashby. Each has a public address that returns the posting as data, without a browser. It is the most reliable way to check that a vacancy is still open and to read its full text. These addresses were checked in November 2026; they are public read-only endpoints, not integrations, and may change.

Find the platform from the posting link (or from the employer's "Apply" link on an aggregator), take the company name and posting id from it, and read the address yourself.

**Always add a unique check string** such as `check=20261125-1` to these addresses (`?check=…`, or `&check=…` after an existing `?`), with a new value in each search. Without it the page-reading tool may return an old saved copy. In November 2026 it showed a Greenhouse posting as open with data from June, although the posting had been closed for months. All addresses below accept the extra string, but some page-reading tools refuse any address that has one (ChatGPT's did in November 2026); then read the same address in a work environment with internet access, which returns the live page without the string (Job Finder, live check rules). Never keep it in links shown to the user.

| Platform | Posting link looks like | All postings of the employer (start here) | One posting |
| --- | --- | --- | --- |
| Greenhouse | `job-boards.greenhouse.io/{board}/jobs/{id}`, `boards.greenhouse.io/{board}/jobs/{id}`, or a career page with `gh_jid={id}` | `https://boards-api.greenhouse.io/v1/boards/{board}/jobs` (titles, places, dates; add `content=true` for the full texts) | `https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{id}?pay_transparency=true` |
| Lever | `jobs.lever.co/{company}/{id}`; in Europe `jobs.eu.lever.co/{company}/{id}` | `https://api.lever.co/v0/postings/{company}?mode=json`; in Europe `https://api.eu.lever.co/v0/postings/{company}?mode=json` (large; `&limit=50&skip=0` reads it in parts) | `https://api.lever.co/v0/postings/{company}/{id}` (Europe: `api.eu.lever.co`) |
| Workable | `apply.workable.com/{account}/j/{shortcode}` | `https://apply.workable.com/api/v1/widget/accounts/{account}` | `https://apply.workable.com/api/v2/accounts/{account}/jobs/{shortcode}` |
| Ashby | `jobs.ashbyhq.com/{org}/{id}` | `https://api.ashbyhq.com/posting-api/job-board/{org}?includeCompensation=true` (full texts of all postings; a large employer comes in several parts) | No public address for one posting, and the posting page shows no text without JavaScript. Use the list: a posting in it is open. |
| Recruitee | `{company}.recruitee.com/o/{slug}` or a career site on Recruitee | `https://{company}.recruitee.com/api/offers/` | Open the posting page itself |
| SmartRecruiters | `jobs.smartrecruiters.com/{company}/{id}` | `https://api.smartrecruiters.com/v1/companies/{company}/postings` (large employers come in parts with `limit` and `offset`). In November 2026 these addresses refused the reading tool in claude.ai, so there the posting page itself may be the only way. | `https://api.smartrecruiters.com/v1/companies/{company}/postings/{id}` |

How to read the answer:

- **The posting is in the employer's live list, or comes back on its own.** The vacancy is open. Take the title, location, work mode, an explicit publication date and a disclosed salary from it.
- **An error comes back for one posting** (the reading tool may show only `client_error`, or 404, 410), **a page redirects to the general list** (Greenhouse adds `?error=true`), **or the posting is missing from the employer's live list.** The vacancy is closed or removed. Drop it. Do not treat this as "blocked" or "not verified".
- **The whole platform address fails** (for example the company name is wrong, or the employer has moved to another platform and its list is empty). Open the posting page itself, with a check string, and judge it by its content.
- **Rate limited.** Platforms limit fast reading, Greenhouse most of all. Read one address of a site at a time. For Greenhouse read one list per employer (with `content=true` it has the texts of all postings) instead of single postings. If the list address is limited, try the employer's board page `https://job-boards.greenhouse.io/{board}?check=…`, which shows the same open postings. If a read is still limited, go on with other employers and come back to it at the end of the search, before you decide what goes on the board.
- **A very long list.** Large employers on Ashby or Lever have lists too long to read in full. On Lever read the single posting instead. On Ashby open the posting page with a check string: a 404 means closed, and the page title shows the posting when it is open. Then read the list in parts only until you reach that posting's text.

Where the fields are:

| Platform | Full description | Publication date | Salary | Place and format |
| --- | --- | --- | --- | --- |
| Greenhouse | `content`: escaped HTML. Decode it and turn it into plain text with line breaks; keep every sentence. | `first_published` | `pay_input_ranges`: `min_cents`, `max_cents` (divide by 100), `currency_type`. Several entries are separate ranges. | `location.name`, `offices` |
| Lever | `descriptionPlain`, then each of `lists` (heading and items), then `additionalPlain` | not stated (`createdAt` is not a publication date) | `salaryRange` when present | `categories.location`, `workplaceType` |
| Workable | `description`, `requirements`, `benefits` (HTML) | `published` | `salary_from`, `salary_to`, `salary_currency_iso_code`, `salary_frequency` | `location`, `locations`, `workplace`, `remote` |
| Ashby | `descriptionPlain` | `publishedAt` | `compensation`: use one tier only; a summary such as "Multiple Ranges" or several tiers are separate ranges | `location`, `secondaryLocations`, `workplaceType`, `isRemote` |
| SmartRecruiters | `jobAd.sections` (`jobDescription`, `qualifications`, `additionalInformation`) | `releasedDate` | rarely given | `location.city`, `location.remote`, `location.hybrid`; `active: true` means open |

To find more vacancies on these platforms, search the platform domains directly with the role and region, for example `site:job-boards.greenhouse.io "Product Designer" remote Europe`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`, `site:apply.workable.com`. Search results are leads only; check each one as above. Once an employer's list is open, look there for other postings that fit the user's roles too.
