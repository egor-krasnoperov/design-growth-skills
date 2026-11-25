# Personal Job Board

*Your own board for the vacancies Job Finder finds for you*

Personal Job Board is a private page where you review vacancies, save the interesting ones, hide the rest and track where you've applied. For any vacancy you can get a deep analysis and read the report right on the board.

## How you get a board

1. Share this repository or the [Job Finder](../job-finder/SKILL.md) skill with Claude and add your CV.
2. Answer a few short questions about the work you're looking for.
3. Claude picks vacancies from the daily list, checks the best ones on the employer's live page and creates the board in your chat. This takes a few minutes.

The board is created for you personally. Nobody else sees it or its data unless you share it.

## What you can do on the board

- Filter by place, work format, role, level, salary and publication date, and sort by date, salary or best match.
- See Job match on every card, how well your CV fits the job. It's a quick estimate until you get a deep analysis.
- Save vacancies, hide the ones you don't need and see which ones are new.
- Mark your progress with Applied, In progress or Rejected.
- Open a vacancy and press Get deep analysis. Claude asks in its own window whether the board may send it the request. Press Send, and the report appears in the chat and on the board in a minute or two.
- Press Refresh to add new vacancies from the latest daily list.
- Download the board as an HTML file.

The best vacancies, checked on the employer's live page, show a short summary of the posting written by Claude. The others show the key requirements found in the posting and the date of the list. Every vacancy has a link to the original, and the full text stays on the employer's page.

## Where your data is

- In Claude, the vacancies, reports and your choices are stored in the board's own storage, private to your account.
- Your search conditions and a short profile from your CV (years of experience, skills, domains and languages) are stored on the board too, without your contacts.
- Your CV stays in the chat. The board keeps only short quotes from it inside match reports.
- A downloaded HTML file contains the vacancies, the reports and your choices. Keep that in mind before you send it to someone.
- Opened outside Claude, the board keeps your changes in this browser only.

## Limits

- The board shows what Job Finder found and checked at a given moment. Vacancies close and change, so open the original link before you apply.
- The deep analysis compares your CV with one vacancy. It isn't a hiring prediction.
- The board works best in Claude on a paid plan. Other assistants give you the same list and reports in the chat.
- So far the board has been tested in Claude on the web. See [what was tested in this beta](../README.md#what-was-tested-in-this-beta).

## For AI assistants

Follow [board-integration.md](board-integration.md) to create the board, write data to it and handle its requests. The board template is [personal-job-board.html](personal-job-board.html).
