# Career and Job Search

**For AI assistants.** Before you use a skill from this repository, read its files in full. If your page-reading tool gives you only a summary, clone the repository with git (`git clone --depth 1 https://github.com/egor-krasnoperov/design-growth-skills.git`) and read the files from the clone. Don't ask the user to download anything.

These skills help Product, UX, and UI designers and design leaders prepare their application materials and look for work. They evaluate what the materials and vacancies show, not the person's actual professional level or their chances of being hired.

| Skill | Main question | What to provide |
| --- | --- | --- |
| [Portfolio Checker](portfolio-checker/SKILL.md) | How might my portfolio come across in an initial review for my target role? | Your target role, portfolio homepage, and up to three separately identified cases. |
| [Resume Checker](resume-checker/SKILL.md) | What does my resume communicate, and what could make it clearer and more effective? | Your existing resume and any relevant role context. |
| [Job Finder](job-finder/SKILL.md) *(beta)* | Which current vacancies fit what I'm looking for? | Your CV, a portfolio or website link if you have one, and a few answers about the roles, level, location and work format you want. |
| [Job Matcher](job-matcher/SKILL.md) *(beta)* | How well does my CV match this specific vacancy? | Your CV, your portfolio or website if you like, and the vacancy text or link. |

## Personal Job Board *(beta)*

Job Finder collects the vacancies it finds on your own [Personal Job Board](personal-job-board/README.md). It's a private page where you filter and save vacancies, mark where you've applied and get a deep analysis of any of them. Each card shows Job match, how well your CV and portfolio fit the job.

- In Claude on a paid plan, the board is a private artifact in your own chat. It holds your personal base of vacancies, your saved vacancies, statuses and reports.
- On the free plan, Claude shows the 10 best vacancies as a list in the chat. In other assistants, you get the list and reports in the chat too.
- You can download the board as an HTML file and keep working with it in a browser.

Tailoring your CV for a vacancy and exporting it as a PDF is coming next.

## Getting started

1. Open a new chat in Claude. The board needs a paid plan.
2. Send the link to this repository or to the [Job Finder](job-finder/SKILL.md) skill and attach your CV. If you have a portfolio or website, add its link too.
3. Answer a few short questions about the roles, level, places and work format you want, about your Claude plan, and whether you want a board or a list in the chat.
4. Check the profile Claude shows you and reply yes.
5. Wait 20 to 30 minutes. Claude puts together your base, creates the board and analyses the 20 best vacancies. The board fills up as it goes.
6. For a deep analysis, open a vacancy and press Get deep analysis. Claude asks in its own window whether the board may send it a message. Press Send.

There is nothing to install. In ChatGPT and other assistants you can send the same link and get the vacancies in the chat.

The [Job Finder guide](job-finder/GUIDE.md) walks you through the first run step by step, shows how the board works and answers common questions.

## How Job Finder works

1. Job Finder writes a short profile from your CV and, if you share it, your portfolio or website, with your years of experience, skills, product domains and languages. It shows the profile to you and starts the search only after you confirm it. Your contacts and the texts of your CV and portfolio don't go into it.
2. It reads a shared list of open design vacancies that is rebuilt every morning. See [where the vacancies come from](#where-the-vacancies-come-from).
3. From the list it puts together your personal base. It holds the vacancies of your roles in your city in any work format, remote vacancies open to your country, your region or the whole world, and vacancies in the countries you'd relocate to. The base is a bit wider than your conditions, so you can widen the board's filters without a new search. It sits on the board as a file.
4. It sorts the vacancies by Job match, a quick estimate of how many of the posting's key requirements your profile covers.
5. It reads the 20 best on the employer's live page and writes a summary and a short analysis of each. The analysis has up to 8 main requirements with their status, a percentage calculated with the same formula as the deep analysis, what matches, what's missing and what to check. It skips the closed vacancies and the ones that don't fit your place or US working hours, and takes the next.
6. You get 20 more analyses with a button on the board. If fewer than 15 vacancies fit, Job Finder also searches the web and checks every vacancy it finds there on the live page.

Refresh on the board reads the latest list, adds the new vacancies to your base, analyses the best of them and marks the ones that have left the list. When the board is ready, Job Finder also gives a few tips on how to search faster.

## How the deep analysis works

1. You open a vacancy and press Get deep analysis. Claude reads the full posting again from its live page, so the report is based on the current text and you know if the vacancy has closed in the meantime.
2. It lists the vacancy's requirements, keeping required and preferred apart.
3. For each requirement it looks for evidence in your CV and portfolio and marks it as supported, partly supported, not evidenced or unclear. A requirement shown only in your portfolio counts as partly supported, with a suggestion to add it to your CV.
4. The percentage is calculated from that table. Required items count twice, preferred ones once, and unclear ones are left out. It maps to a level from High to Below average.
5. The report on the board shows the evidence, strengths, gaps, questions for you and what could be clearer in your CV. Its percentage replaces the quick Job match or the short analysis on the card.

The percentage shows how much of the vacancy your CV and portfolio currently support. It isn't an ATS score or a chance of getting an interview, and a missing line in a CV doesn't mean you lack the skill.

## Where the vacancies come from

The daily list is built from the open job dataset by [Stapply](https://github.com/kalil0321/ats-scrapers), which collects postings from company career pages on Greenhouse, Lever, Ashby, Workable and other job platforms. The data is under CC0 1.0. A [small program](jobs-feed/README.md) in this repository keeps the digital design and UX research roles every morning and adds the place, work format, level and requirement keywords.

Each vacancy belongs to its employer. The list keeps only short facts, requirement keywords and the link to the employer's posting, never the posting text. It holds no personal data.

## What was tested in this beta

Job Finder, Job Matcher and Personal Job Board were built and tested in Claude first, on the web and on a paid plan, with fictional CVs.

- The daily list was first built on 25 November 2026 and had about 5,400 design vacancies.
- With two fictional profiles, a Senior Product Designer in Lisbon and one in London, the selection and the Job match were checked on that list. 115 vacancies fitted the Lisbon profile and 255 the London one.
- In the earlier version, which searched the web, every vacancy link on the board opened a live posting in the last two runs (16 of 16 and 14 of 14), and the deep analysis percentages matched the formula.
- On 26 November 2026 the whole flow ran in Claude on the Max 5x plan with a fictional Product Designer in Lisbon. From confirming the profile to a ready board took about 3.5 minutes, and to 20 analysed vacancies about 19 minutes. It used about 9% of the Max 5x five-hour limit. On Pro that is roughly half of the five-hour limit, by calculation rather than measurement.
- The short analysis gave 59% on average, and the quick estimate for the same vacancies 77%. For half of the analysed vacancies the live posting didn't fit the place or US working hours. So Claude now skips such vacancies. A later run on the same day confirmed the rule. Claude skipped 10 such vacancies, the board's filters hid 8 of them, and only fitting vacancies were at the top. With the skipping, 20 analysed vacancies took about 26 minutes and about 8% of the Max 5x five-hour limit.

## Known limits

- The list has only vacancies from the job platforms in the dataset. Vacancies posted only on LinkedIn or on a company's own site may be missing.
- About half of the vacancies don't state a work format. The board shows "format not stated" for them.
- Job match is a rough estimate from keywords. The deep analysis reads the whole posting.
- Vacancies that weren't checked live may have closed since the list was built. The board shows the date of the list for them.
- Some career sites don't let assistants read them, so not every vacancy can be checked live.
- Claude can't read postings on Workable, Workday, Gem and Welcome to the Jungle at the moment. The board marks them, and they only have the quick estimate. Sometimes it can't read Ashby postings either, for companies with a very long list of vacancies. These keep the quick estimate and the date of the list.
- Some remote vacancies in the list are marked as worldwide but are open to one country or region only. Claude sees this only for the vacancies it reads.
- The board shows a summary of a posting, not the full text.
- Free and Pro plans, the Claude desktop and mobile apps, ChatGPT and other assistants, UX research roles, roles beyond Product, UX and UI design, and regions beyond Lisbon and London haven't been tested yet.

If something doesn't work as described, I'd like to hear about it in [GitHub Issues](https://github.com/egor-krasnoperov/design-growth-skills/issues).

## How to use

Open a `SKILL.md` file and give it to your AI assistant along with the relevant materials. The assistant's ability to open links, read files, and generate documents depends on the tools available to it. If it cannot inspect part of a source, that limitation should be reflected in the review.

Each skill can be used independently. Their reviews are approximations based on the available evidence, not hiring decisions or guarantees.
