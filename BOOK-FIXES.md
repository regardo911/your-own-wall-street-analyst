# Book fixes

Where running the book's own text showed a problem, and what this repo does about it.

## Appendix B6: the margin can mix two periods

What the book prints: `latest()` picks revenue and gross profit separately, and the margin line divides one by the other. The appendix warns that the script "can also finish without an error and still mix periods" and says to "Check that the two period lines match before you trust the margin."

What happens when you run it: the book's script, changed only in its User-Agent line, on General Mills (`python3 latest_numbers.py 40704`), exit code 0:

```
GENERAL MILLS, INC.
Revenue           4,389,500,000  10-Q filed 2026-09-23  period 2026-06-01..2026-08-30  accn 0001628280-26-063201
Gross profit      1,603,500,000  10-K filed 2026-07-01  period 2026-02-23..2026-05-31
Gross margin 36.5%  (computed here from the two lines above)
Shares out          534,687,144  as of 2026-09-16  10-Q filed 2026-09-23
```

General Mills tags gross profit only in its 10-K, so that 36.5% divides one quarter's revenue by an earlier quarter's gross profit, silently.

What the repo does: [`appendix-b/latest_numbers.py`](appendix-b/latest_numbers.py) checks the two periods after the margin line and, when they differ, prints:

```
WARNING: revenue and gross profit are from different periods, so the margin above mixes them. Don't use it.
```

On Apple the periods match, so the output is still exactly the five lines Appendix B6 prints.
