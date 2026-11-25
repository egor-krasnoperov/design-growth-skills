# Jobs feed

The program that builds the daily list of digital design vacancies for Job Finder. The list itself lives in the [`jobs-feed` branch](https://github.com/egor-krasnoperov/design-growth-skills/tree/jobs-feed).

- `build_feed.py` reads the open job dataset by [Stapply](https://github.com/kalil0321/ats-scrapers) (data under CC0 1.0), keeps digital design roles, adds the place, work mode, level and requirement keywords, and writes small JSON files by region and country. Posting texts are read only to find the keywords and are never written out.
- `.github/workflows/jobs-feed.yml` runs it every morning and publishes the result.
- `FEED_README.md` becomes the README of the `jobs-feed` branch.

To build the list on your own computer, install `duckdb` and run `python build_feed.py OUT_DIR`.
