# Your Own Wall Street Analyst

**Your research desk in Claude: a clerk, an analyst, a bear and a morning run. Every command and card from the book, ready to upload instead of retyped.**

Companion to the book *Build Your Own Wall Street Analyst with Claude* · [youcanbuildthings.com](https://youcanbuildthings.com)

[![ci](https://github.com/regardo911/your-own-wall-street-analyst/actions/workflows/ci.yml/badge.svg)](https://github.com/regardo911/your-own-wall-street-analyst/actions/workflows/ci.yml) [![license: MIT](https://img.shields.io/badge/license-MIT-111111.svg)](LICENSE) [![not investment advice](https://img.shields.io/badge/not%20investment%20advice-read%20first-E4572E.svg)](DISCLAIMER.md)

![Headline: Wall Street has an analyst on every stock. Now you do too. One research desk seen from above: the clerk (desk-pull) and the analyst (desk-memo) on one side, the bear (desk-bear) and the morning run (desk-morning) on the other, and you in orange at the head of the desk, labelled You decide. Footer: Nobody on the team touches an order.](docs/images/hero.png)

The book's prompts and forms, as plain-text files you drop into a Claude project. Once your three thesis cards are written, the uploading takes minutes. Two words to know. **Research Desk** is the Claude project you make in Chapter 3 ([folder](chapters/03-score-two-models/)). A **tag** is the `form · filing date · section · period` label from Chapter 2 that goes on every number ([folder](chapters/02-write-the-desks-brief/)). Pick your line below.

## Start here

### "I'm setting up my desk" (Chapters 2 and 3)

1. Click **Code → Download ZIP** at the top of this page and unzip it.
2. Open [`thesis-cards.txt`](chapters/02-write-the-desks-brief/thesis-cards.txt) and fill in one thesis card for each of the three stocks you own the most of. By hand, before any AI sees them. Save it as `thesis-cards`.
3. In Claude, go to **Projects** and create a project named **Research Desk**. Create it in the app, not from a folder on your computer.
4. Upload the nine files in [`research-desk/knowledge/`](research-desk/knowledge/) and your `thesis-cards` into the project's knowledge.
5. Paste [`research-desk/project-instructions.txt`](research-desk/project-instructions.txt) into the project instructions.
6. Start a chat in the project and type the book's setup test:

   ```
   List the files you can see in this project and repeat rule 2 back to me.
   ```

   You should get your file names and the tag rule back. If a file is missing, the upload didn't finish; add it again.

Next: [Chapter 3's head-to-head](chapters/03-score-two-models/), then [Chapter 4](chapters/04-connect-the-clerk/) for real filings.

### "My desk is running and I want one command"

Open [`research-desk/knowledge/`](research-desk/knowledge/), open the command, click **Copy raw file**, and save it in your project under the same name. Rule 8 in your instructions runs it when you type its name.

### "I'm on Chapter 8"

Go to [`bear-desk/`](bear-desk/): a second project, the bear's rules, one command.

### "I want the spreadsheet"

[`value-range-sheet.xlsx`](chapters/09-the-idea-pipeline/value-range-sheet.xlsx) carries the book's formulas with your assumption cells empty, and the book's made-up Company X on a second tab.

Two ways to get files: **Code → Download ZIP** for everything, or open any one file and use **Copy raw file**.

## The copy table

The table starts at Chapter 2, the first build step. "Research Desk" and "Bear Desk" mean that project's knowledge (its file area) unless the row says instructions.

| Ch | File in this repo | Where it goes |
|---|---|---|
| 2 | [memo-template.txt](research-desk/knowledge/memo-template.txt), [research-questions.txt](research-desk/knowledge/research-questions.txt) | Research Desk |
| 2 | [thesis-cards.txt](chapters/02-write-the-desks-brief/thesis-cards.txt) | Filled in by hand, Research Desk as `thesis-cards` |
| 3 | [project-instructions.txt](research-desk/project-instructions.txt) | Research Desk instructions |
| 3 | The head-to-head request, in [chapter 3's README](chapters/03-score-two-models/) | A Research Desk chat, and one other product |
| 3 | [model-scorecard.txt](chapters/03-score-two-models/model-scorecard.txt) | Filled in, Research Desk as `model-scorecard` |
| 4 | [desk-pull.txt](research-desk/knowledge/desk-pull.txt) | Research Desk |
| 4 | [tag-check.txt](chapters/04-connect-the-clerk/tag-check.txt) | Paper or a notes file |
| 4 | [data-source-card.txt](chapters/04-connect-the-clerk/data-source-card.txt) | Filled in, Research Desk as `data-source-card` |
| 5 | [desk-memo.txt](research-desk/knowledge/desk-memo.txt) | Research Desk |
| 5 | [desk-memo/SKILL.md](chapters/05-your-first-memo/desk-memo/SKILL.md) | Optional: zipped, uploaded as a skill |
| 5 | [five-source-check.txt](chapters/05-your-first-memo/five-source-check.txt), [example-memo-aapl.txt](chapters/05-your-first-memo/example-memo-aapl.txt) | Paper or a notes file |
| 6 | [desk-calls.txt](research-desk/knowledge/desk-calls.txt) | Research Desk |
| 6 | The earnings-season roll-up, in [chapter 6's README](chapters/06-read-every-earnings-call/) | One chat, after four `desk-calls` runs |
| 7 | [desk-changes.txt](research-desk/knowledge/desk-changes.txt) | Research Desk |
| 7 | [filing-change-report.txt](chapters/07-find-what-changed/filing-change-report.txt) | Filled in, Research Desk as `changes-[TICKER]` |
| 8 | [project-instructions.txt](bear-desk/project-instructions.txt) | Bear Desk instructions |
| 8 | [desk-bear.txt](bear-desk/knowledge/desk-bear.txt) | Bear Desk |
| 8 | [what-the-bear-sees.txt](chapters/08-the-bear/what-the-bear-sees.txt) | Paper: a checklist for every Bear Desk upload |
| 9 | [desk-inputs.txt](research-desk/knowledge/desk-inputs.txt) | Research Desk |
| 9 | [value-range-sheet.xlsx](chapters/09-the-idea-pipeline/value-range-sheet.xlsx) | Your spreadsheet app |
| 9 | [idea-list.txt](chapters/09-the-idea-pipeline/idea-list.txt) | Filled in, saved as `ideas-[date]` |
| 10 | [desk-morning.txt](research-desk/knowledge/desk-morning.txt), [trigger-list.txt](research-desk/knowledge/trigger-list.txt) | Research Desk |
| 10 | [cost-log.txt](chapters/10-the-morning-run/cost-log.txt), [before-a-ticker-joins.txt](chapters/10-the-morning-run/before-a-ticker-joins.txt) | Paper or a notes file |
| 11 | [weekly-check.txt](chapters/11-the-weekly-check/weekly-check.txt), [error-log.txt](chapters/11-the-weekly-check/error-log.txt), [what-my-desk-sees.txt](chapters/11-the-weekly-check/what-my-desk-sees.txt) | Filled in, Research Desk (the map is the book's filled example) |
| 12 | [framework.txt](chapters/12-framework-scorecard-calendar/framework.txt) | Filled in, Research Desk as `framework` |
| 12 | [scorecard.csv](chapters/12-framework-scorecard-calendar/scorecard.csv) | Your spreadsheet app, as `scorecard` |
| 12 | [next-30-days.txt](chapters/12-framework-scorecard-calendar/next-30-days.txt) | Your calendar |
| 12 | [monthly-review.txt](chapters/12-framework-scorecard-calendar/monthly-review.txt) | Paper or a notes file |
| B | [latest_numbers.py](appendix-b/latest_numbers.py) | Optional, your computer |

## Two projects, one wall

![Headline: Two projects. One wall. The bear never sees your thesis. Research Desk holds your instructions, cards, desk- commands, memos and breakers. Bear Desk holds the bear's rules, desk-bear, filings, transcripts, stripped-[TICKER] and asked-[TICKER]. Only stripped-[TICKER] crosses the wall, and only 3 thesis-breakers come back. Never in the bear's project: your thesis cards, memo fields 1, 2, 4, 6, and share counts, cost basis, position sizes.](docs/images/two-projects.png)

The Research Desk holds your cards and your commands. The Bear Desk holds the filings and a stripped copy of each memo, so the bear builds the case against each stock without ever seeing why you own it.

## What it needs

A browser and a Claude account: the free plan runs Chapters 2 through 9, and Chapter 10's scheduled morning run needs Claude Pro or higher. Any spreadsheet app opens the sheet and the scorecard. The optional script in [`appendix-b/`](appendix-b/) needs python3 and the internet.

## Real money stays with you

Before your first chat with any connector, open its **Tool permissions** under **Customize > Connectors** and set every order tool to **Blocked**. Not "Needs approval." Blocked. Skip Zerodha's Kite connector altogether: your desk doesn't need your holdings to read filings. The first line of your project instructions settles the rest: "You research; I decide."

## Contributing

Found a file that differs from the book, or a broken link? Open an issue or a pull request and name the chapter; every file maps to one. [BOOK-FIXES.md](BOOK-FIXES.md) covers the one change made after running the book's script. Offline checks: `python -m unittest discover -s tests`.

## License

MIT. See [LICENSE](LICENSE).

*Educational material that goes with the book. Not investment advice.*
