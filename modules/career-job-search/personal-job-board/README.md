# Personal Job Board

*Your own board for the vacancies Job Finder finds for you*

Personal Job Board is a private page where you review vacancies, save the interesting ones, hide the rest and track where you've applied. For any vacancy you can run Match and read the report right on the board.

## How you get a board

1. Share this repository or the [Job Finder](../job-finder/SKILL.md) skill with Claude and add your CV.
2. Answer a few short questions about the work you're looking for.
3. Claude searches for vacancies, checks each one on the employer's live page and creates the board in your chat. This usually takes about 25 minutes.

The board is created for you personally. Nobody else sees it or its data unless you share it.

## What you can do on the board

- Filter by work format and level, and sort by date, salary or best match.
- Save vacancies, hide the ones you don't need and see which ones are new.
- Mark your progress with Applied, In progress or Rejected.
- Open a vacancy and press Match. Claude asks in its own window whether the board may send it the request. Press Send, and the report appears on the board in a minute or two.
- Download the board as an HTML file.

Each vacancy shows a short summary of the posting, where it was found, when it was checked and a link to the original. The summary is written by Claude. The full text stays on the employer's page.

## Where your data is

- In Claude, the vacancies, reports and your choices are stored in the board's own storage, private to your account.
- Your CV stays in the chat. The board keeps only short quotes from it inside match reports.
- A downloaded HTML file contains the vacancies, the reports and your choices. Keep that in mind before you send it to someone.
- Opened outside Claude, the board keeps your changes in this browser only.

## Limits

- The board shows what Job Finder found and checked at a given moment. Vacancies close and change, so open the original link before you apply.
- Match compares your CV with one vacancy. It isn't a hiring prediction.
- The board works best in Claude on a paid plan. Other assistants give you the same list and reports in the chat.
- So far the board has been tested in Claude on the web. See [what was tested in this beta](../README.md#what-was-tested-in-this-beta).

## For AI assistants

Follow [board-integration.md](board-integration.md) to create the board, write data to it and handle its requests. The board template is [personal-job-board.html](personal-job-board.html).
