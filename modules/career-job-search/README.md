# Career and Job Search

These skills help Product, UX, and UI designers and design leaders prepare their application materials and look for work. They evaluate what the materials and vacancies show, not the person's actual professional level or their chances of being hired.

| Skill | Main question | What to provide |
| --- | --- | --- |
| [Portfolio Checker](portfolio-checker/SKILL.md) | How might my portfolio come across in an initial review for my target role? | Your target role, portfolio homepage, and up to three separately identified cases. |
| [Resume Checker](resume-checker/SKILL.md) | What does my resume communicate, and what could make it clearer and more effective? | Your existing resume and any relevant role context. |
| [Job Finder](job-finder/SKILL.md) *(beta)* | Which current vacancies fit what I'm looking for? | Your CV and a few answers about the roles, level, location and work format you want. |
| [Job Matcher](job-matcher/SKILL.md) *(beta)* | How well does my CV match this specific vacancy? | Your CV and the vacancy text or link. |

## Personal Job Board *(beta)*

Job Finder can collect the vacancies it finds on your own [Personal Job Board](personal-job-board/README.md). It's a private page where you filter and save vacancies, mark where you've applied and run Match on any of them. The match report appears right on the board.

- In Claude on a paid plan, the board is a private artifact in your own chat, and your saved vacancies, statuses and reports are stored in it.
- In other assistants and on free plans, you get the same list and reports in the chat.
- You can download the board as an HTML file and keep working with it in a browser.

Tailoring your CV for a vacancy and exporting it as a PDF is coming next.

## How Job Finder works

1. You share your CV and answer two to four short questions about roles, level, location and work format.
2. Job Finder searches job boards, employer career pages and job platforms such as Greenhouse, Lever, Ashby and Workable. Search results are treated as leads only, because many of them point to vacancies that have already closed.
3. Every vacancy is checked on a fresh copy of the employer's own posting. If the posting is closed, gone or can't be read, the vacancy doesn't go on the board, and the chat says which ones were left out.
4. Each vacancy on the board has a short summary of the posting, the source, the date it was checked and a link to the original. Claude doesn't copy the employer's full text, so the original link is always there.
5. The board gets every checked vacancy that fits, up to 30. If there are fewer than 15, Job Finder explains why and suggests how to widen the search.

## How Match works

1. You press Match on a vacancy. Claude reads the full posting again from its live page, so the report is based on the current text and you know if the vacancy has closed in the meantime.
2. It lists the vacancy's requirements, keeping required and preferred apart.
3. For each requirement it looks for evidence in your CV and marks it as supported, partly supported, not evidenced or unclear.
4. The percentage is calculated from that table. Required items count twice, preferred ones once, and unclear ones are left out. It maps to a level from High to Below average.
5. The report on the board shows the evidence, strengths, gaps, questions for you and what could be clearer in your CV.

The percentage shows how much of the vacancy your CV currently supports. It isn't an ATS score or a chance of getting an interview, and a missing line in a CV doesn't mean you lack the skill.

## What was tested in this beta

Job Finder, Job Matcher and Personal Job Board were built and tested in Claude first. In November 2026 I ran the full flow in Claude on the web, on a paid plan, with a fictional CV of a Product Designer based in Lisbon and real vacancies.

- In the last two runs every vacancy link on the board opened a live posting (16 of 16 and 14 of 14). The links were checked by a script outside Claude.
- Match reports appeared on the board, and their percentages matched the formula.
- A search took about 25 minutes. For this profile the board had 14 to 16 vacancies, because most search results had already closed.

## Known limits

- Some career sites don't let assistants read them. Vacancies there are skipped and mentioned in the chat.
- The board shows a summary of each posting, not the full text.
- When you press Match, Claude asks in its own window whether the board may send it a message. Press Send.
- Free and Pro plans, the Claude desktop and mobile apps, ChatGPT and other assistants, roles beyond Product, UX and UI design, and regions outside Europe haven't been tested yet.

If something doesn't work as described, I'd like to hear about it.

## How to use

Open a `SKILL.md` file and give it to your AI assistant along with the relevant materials. The assistant's ability to open links, read files, and generate documents depends on the tools available to it. If it cannot inspect part of a source, that limitation should be reflected in the review.

Each skill can be used independently. Their reviews are approximations based on the available evidence, not hiring decisions or guarantees.
