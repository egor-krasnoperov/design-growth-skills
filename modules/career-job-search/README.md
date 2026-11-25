# Career and Job Search

These skills help Product, UX, and UI designers and design leaders prepare their application materials and look for work. They evaluate what the materials and vacancies show, not the person's actual professional level or their chances of being hired.

| Skill | Main question | What to provide |
| --- | --- | --- |
| [Portfolio Checker](portfolio-checker/SKILL.md) | How might my portfolio come across in an initial review for my target role? | Your target role, portfolio homepage, and up to three separately identified cases. |
| [Resume Checker](resume-checker/SKILL.md) | What does my resume communicate, and what could make it clearer and more effective? | Your existing resume and any relevant role context. |
| [Job Finder](job-finder/SKILL.md) *(beta)* | Which current vacancies fit what I'm looking for? | Your CV and a few answers about the roles, level, location and work format you want. |
| [Job Matcher](job-matcher/SKILL.md) *(beta)* | How well does my CV match this specific vacancy? | Your CV and the vacancy text or link. |

## Personal Job Board *(beta)*

Job Finder collects the vacancies it finds on your own [Personal Job Board](personal-job-board/README.md). It's a private page where you filter and save vacancies, mark where you've applied and get a deep analysis of any of them. Each card shows Job match, how well your CV fits the job.

- In Claude on a paid plan, the board is a private artifact in your own chat, and your saved vacancies, statuses and reports are stored in it.
- In other assistants and on free plans, you get the same list and reports in the chat.
- You can download the board as an HTML file and keep working with it in a browser.

Tailoring your CV for a vacancy and exporting it as a PDF is coming next.

## Getting started

1. Open a new chat in Claude. The board needs a paid plan.
2. Send the link to this repository or to the [Job Finder](job-finder/SKILL.md) skill and attach your CV.
3. Answer a few short questions about the roles, level, places and work format you want.
4. When the board is ready, open a vacancy and press Get deep analysis. Claude asks in its own window whether the board may send it a message. Press Send.

There is nothing to install. In ChatGPT and other assistants you can send the same link and get the vacancies in the chat.

## How Job Finder works

1. Job Finder writes a short profile from your CV with your years of experience, skills, product domains and languages, and shows it to you so you can correct it. Your contacts and the CV text don't go into it.
2. It reads a shared list of open design vacancies that is rebuilt every morning. See [where the vacancies come from](#where-the-vacancies-come-from).
3. It keeps the vacancies that fit your roles, level, places and work format. Vacancies that don't state a level or a work format stay, marked as not stated.
4. It sorts them by Job match, a quick estimate of how many of the posting's key requirements your profile covers.
5. It opens the 10 best on the employer's live page, drops the closed ones and writes a short summary for each. The other vacancies show the date of the list.
6. The board gets up to 100 vacancies. If fewer than 15 fit, Job Finder also searches the web and checks every vacancy it finds there on the live page.

Refresh on the board reads the latest list, adds the new vacancies that fit and marks the ones that have left the list. When the board is ready, Job Finder also gives a few tips on how to search faster.

## How the deep analysis works

1. You open a vacancy and press Get deep analysis. Claude reads the full posting again from its live page, so the report is based on the current text and you know if the vacancy has closed in the meantime.
2. It lists the vacancy's requirements, keeping required and preferred apart.
3. For each requirement it looks for evidence in your CV and marks it as supported, partly supported, not evidenced or unclear.
4. The percentage is calculated from that table. Required items count twice, preferred ones once, and unclear ones are left out. It maps to a level from High to Below average.
5. The report on the board shows the evidence, strengths, gaps, questions for you and what could be clearer in your CV. Its percentage replaces the quick Job match on the card.

The percentage shows how much of the vacancy your CV currently supports. It isn't an ATS score or a chance of getting an interview, and a missing line in a CV doesn't mean you lack the skill.

## Where the vacancies come from

The daily list is built from the open job dataset by [Stapply](https://github.com/kalil0321/ats-scrapers), which collects postings from company career pages on Greenhouse, Lever, Ashby, Workable and other job platforms. The data is under CC0 1.0. A [small program](jobs-feed/README.md) in this repository keeps the digital design roles every morning and adds the place, work format, level and requirement keywords.

Each vacancy belongs to its employer. The list keeps only short facts, requirement keywords and the link to the employer's posting, never the posting text. It holds no personal data.

## What was tested in this beta

Job Finder, Job Matcher and Personal Job Board were built and tested in Claude first, on the web and on a paid plan, with fictional CVs.

- The daily list was first built on 25 November 2026 and had about 5,400 design vacancies.
- With two fictional profiles, a Senior Product Designer in Lisbon and one in London, the selection and the Job match were checked on that list. 115 vacancies fitted the Lisbon profile and 255 the London one.
- In the earlier version, which searched the web, every vacancy link on the board opened a live posting in the last two runs (16 of 16 and 14 of 14), and the deep analysis percentages matched the formula.

## Known limits

- The list has only vacancies from the job platforms in the dataset. Vacancies posted only on LinkedIn or on a company's own site may be missing.
- About half of the vacancies don't state a work format. The board shows "format not stated" for them.
- Job match is a rough estimate from keywords. The deep analysis reads the whole posting.
- Vacancies that weren't checked live may have closed since the list was built. The board shows the date of the list for them.
- Some career sites don't let assistants read them, so not every vacancy can be checked live.
- The board shows a summary of a posting, not the full text.
- Free and Pro plans, the Claude desktop and mobile apps, ChatGPT and other assistants, roles beyond Product, UX and UI design, and regions beyond Lisbon and London haven't been tested yet.

If something doesn't work as described, I'd like to hear about it.

## How to use

Open a `SKILL.md` file and give it to your AI assistant along with the relevant materials. The assistant's ability to open links, read files, and generate documents depends on the tools available to it. If it cannot inspect part of a source, that limitation should be reflected in the review.

Each skill can be used independently. Their reviews are approximations based on the available evidence, not hiring decisions or guarantees.
