# Chapter 7: find what changed

Rule 9 and the longer data line are already in your desk, in [`project-instructions.txt`](../../research-desk/project-instructions.txt) and [`memo-template.txt`](../../research-desk/knowledge/memo-template.txt).

Pick a stock you own. Cut Item 1A out of this year's 10-K and last year's, and save each as a text file (`TICKER-1A-2025`, `TICKER-1A-2024`, or your fiscal years). Attach both to a new chat and run [`desk-changes`](../../research-desk/knowledge/desk-changes.txt) the way the book does on Apple:

```
desk-changes AAPL · NEW = 10-K filed 2025-10-31, Item 1A · OLD = 10-K filed 2024-11-01, Item 1A
```

Then the three hand checks: the cover-page share counts, the 8-Ks since the last report, and the Form 4s. Here's Apple's Form 4 list; swap in your company's 10-digit CIK:

```
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=4&dateb=&owner=include&count=40
```

Write it up on [`filing-change-report.txt`](filing-change-report.txt), saved as `changes-[TICKER]`. The checkpoint: "Every flagged change in your report quotes both versions and names its section and filing. Your memo's data line shows the newest filing the desk used, and it matches the newest 10-Q or 10-K on EDGAR for that company."
