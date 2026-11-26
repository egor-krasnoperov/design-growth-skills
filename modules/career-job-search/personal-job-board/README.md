# Personal Job Board

*Your own board for the vacancies Job Finder finds for you*

Personal Job Board is a private page where you review vacancies, save the interesting ones, hide the rest and track where you've applied. For any vacancy you can get a deep analysis and read the report right on the board.

## How you get a board

1. Share this repository or the [Job Finder](../job-finder/SKILL.md) skill with Claude and add your CV and, if you have one, a link to your portfolio or website.
2. Answer a few short questions about the work you're looking for.
3. Check the profile Claude shows you and reply yes.
4. Claude puts together your personal base of vacancies from the daily list, creates the board in your chat and analyses the 20 best vacancies on the employers' live pages. This takes about 20 minutes, and the board fills up as it goes.

The board is created for you personally. Nobody else sees it or its data unless you share it.

## What you can do on the board

- Filter by place, work format, role, level, salary and publication date. The filters work across your whole base.
- Sort by best match, date or salary. The board opens on Best match, with the analysed vacancies at the top.
- See Job match on every card, how well your CV and portfolio fit the job. For the analysed vacancies it's based on the full posting, for the others it's a quick estimate from keywords, marked with ≈.
- Save vacancies, hide the ones you don't need and see which ones are new.
- Mark your progress with Applied, In progress or Rejected.
- Press Analyse 20 more to have Claude analyse the next 20 vacancies.
- Open a vacancy and press Get deep analysis. Claude asks in its own window whether the board may send it the request. Press Send, and the report appears in the chat and on the board in a minute or two.
- Press Refresh to add new vacancies from the latest daily list to your base. Claude analyses the best of them too.
- Download the board as an HTML file.

An analysed vacancy shows a summary of the posting, its requirements with their status, what matches, what's missing and what to check. The others show About this job, the facts from the list next to your profile, and the date of the list. Vacancies from sites Claude can't read at the moment are marked. Every vacancy has a link to the original, and the full text stays on the employer's page.

## Where your data is

- In Claude, your personal base is a file next to the board. The analyses, reports and your choices are stored in the board's own storage, private to your account.
- Your search conditions and a short profile from your CV and portfolio (years of experience, skills, domains and languages) are stored on the board too, without your contacts.
- Your CV stays in the chat, and the board doesn't store your portfolio link. The board keeps only short quotes from them inside match reports.
- A downloaded HTML file contains the base, the reports and your choices. Keep that in mind before you send it to someone.
- Opened outside Claude, the board keeps your changes in this browser only.

## Limits

- The board shows what Job Finder found and checked at a given moment. Vacancies close and change, so open the original link before you apply.
- The deep analysis compares your CV and portfolio with one vacancy. It isn't a hiring prediction.
- The board works best in Claude on a paid plan. Other assistants give you the same list and reports in the chat.
- So far the board has been tested in Claude on the web. See [what was tested in this beta](../README.md#what-was-tested-in-this-beta).

## For AI assistants

Follow [board-integration.md](board-integration.md) to create the board, write data to it and handle its requests. The board template is [personal-job-board.html](personal-job-board.html).
