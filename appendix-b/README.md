# Appendix B6: latest_numbers.py (optional)

The book's one script, for readers who write a little code. Give it a CIK and it prints a company's latest quarterly revenue, gross profit, gross margin and share count from the SEC's free JSON, each with its form, filing date and period.

It needs python3 and the internet. First put your own name and email on the `HEADERS` line: the SEC wants both in the User-Agent, and asks you to stay under 10 requests a second.

```
python3 latest_numbers.py 320193
```

That's Apple, where it prints the five lines Appendix B6 shows. Other companies can label their numbers differently ("some use a different revenue tag, some have no gross profit line"), and then it stops with a KeyError until you change the tag names.

One addition to the book's version: a WARNING under the margin when revenue and gross profit come from different periods. [BOOK-FIXES.md](../BOOK-FIXES.md) has the run behind it.
