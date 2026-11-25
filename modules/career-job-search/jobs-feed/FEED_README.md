# Design jobs list

A daily list of open digital design vacancies for [Job Finder](https://github.com/egor-krasnoperov/design-growth-skills/tree/main/modules/career-job-search). It is rebuilt every morning by a GitHub Action, and this branch keeps the last three days.

Start with `latest.json`. It names the folder of the latest day, and that folder's `index.json` lists every file with its region, country and number of vacancies, and explains each field.

## Where the vacancies come from

The vacancies come from the open job dataset by [Stapply](https://github.com/kalil0321/ats-scrapers), which collects them every day from job platforms such as Greenhouse, Lever, Ashby and Workable. The dataset is published under CC0 1.0. Thank you, Stapply.

Each vacancy belongs to its employer. This list keeps only short facts (title, company, place, work mode, salary when stated, dates) and requirement keywords used for a quick match. It never keeps the text of a posting. Open the link to read the posting itself.

## Limits

- The list covers companies that publish on the job platforms in the dataset. Some companies and job boards are not in it.
- A vacancy can close between the daily update and the moment you open it.
- Roles are selected by rules from titles and descriptions. A few non-digital design roles may slip in, and a few digital ones may be missed.
