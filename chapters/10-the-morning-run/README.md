# Chapter 10: the morning run

![Headline: Every name gets checked. Only what changed reaches you. For one ticker: anything filed since the memo's data line? If not, UNCHANGED. Did one of the six triggers fire? If not, UNCHANGED. If so, the analyst quotes what changed, the bear marks FIRED or NOT FIRED, shared exposure is listed, and the name is FLAGGED in your brief. A side panel lists the six triggers.](../../docs/images/morning-run.png)

Your whole list, checked every weekday by a scheduled task; only changed names reach you. This step needs **Claude Pro or higher**.

## Get the desk ready

- The run reads what Chapters 2-9 put in Research Desk (every `memo-[TICKER]` and `breakers` included), plus this chapter's [`desk-morning.txt`](../../research-desk/knowledge/desk-morning.txt) and [`trigger-list.txt`](../../research-desk/knowledge/trigger-list.txt).
- In **Tool permissions**, set the clerk's read tools to **Always allow** so a 6 a.m. run doesn't wait for a click, and check that every order tool is still **Blocked**.
- If your data-source card shows your route can't see new 8-Ks or Form 4s, add this line to `trigger-list`:

  ```
  If you can't see this ticker's 8-Ks or Form 4s, write NOT COVERED beside it.
  ```

- Run it by hand once. Open the sources for two flagged names, and check one UNCHANGED name on EDGAR yourself.

## Schedule it

In the combined Claude, describe it in the project, answer Claude's questions, and click **"Schedule"**:

```
Run desk-morning every weekday at 6 a.m. and send me the brief
```

With a separate Cowork mode: **"Scheduled"** > **"New task"** > **"Create with Claude"** or **"Set up manually"**, frequency **on weekdays**, and the folder field left empty. "A task tied to a folder on your computer only runs locally."

Find out two things on day one:

- "One thing I haven't confirmed, and you should know it: whether a scheduled task can edit a file in your project in place." Ask the run to save its update blocks to a file. If no file appears, fold the blocks into each memo by hand on Friday.
- Whether the phone notice comes: "confirm on day one that the notification arrives for your scheduled run." For email, the book has the run write a Gmail draft you open, or you approve each send.

## Every morning

One dated line per flagged name goes in a file called `decisions`: NOTHING, UPDATE THE CARD, RE-RUN THE BEAR or ZONE CHECK. [`cost-log.txt`](cost-log.txt) records each run as the percent of your five-hour and weekly limits it used (Settings > Usage, before and after). A new name joins once every box on [`before-a-ticker-joins.txt`](before-a-ticker-joins.txt) is ticked.

> The first scheduled brief arrives on its own (not a run you started) and flags only names with a changed filing, call, Form 4, watch item or card condition, each with a source you can open. The cost log has its first row: the percent of your five-hour and weekly limits the run used, and that figure divided by the number of names.
