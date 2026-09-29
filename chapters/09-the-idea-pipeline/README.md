# Chapter 9: the idea pipeline

From a screen to three candidates, each with a cited memo, a bear case and a buy zone your own spreadsheet computed.

## Screen, cut, run the team

This is the author's screen (small market cap, gross margin over 40%, quarterly sales growth over 20%). "You'll choose yours."

```
https://finviz.com/screener.ashx?v=111&f=cap_small,fa_grossmargin_o40,fa_salesqoq_o20
```

Cut to about twenty with rules you'd defend. The book's four:

1. **Profitable, or clearly close.** Positive operating income in the latest quarter, or losses shrinking for three quarters running.
2. **Not printing shares.** Cover-page share count up less than about 5% over the past year. (Chapter 7 showed you where to look.)
3. **No going-concern language.** A 10-second EDGAR full-text search for "going concern" on the company's latest 10-Q.
4. **A business you can explain in one sentence.** If you can't say what it sells and to whom, skip it for now.

Pick five and write a candidate card for each, before the desk sees them: the blank is the second card in [`thesis-cards.txt`](../02-write-the-desks-brief/thesis-cards.txt), filed in your `thesis-cards` under a CANDIDATES heading. Run `desk-memo` and `desk-bear` on each, and drop any with a thesis-breaker you can't answer from the filings.

## The sheet does the math

For each survivor, run [`desk-inputs`](../../research-desk/knowledge/desk-inputs.txt), check two inputs against the filing, and fill in [`value-range-sheet.xlsx`](value-range-sheet.xlsx):

- **Your stock**: tagged inputs in B2:B5 (tags in column E), and your low, base and high assumptions in B8:D11, set before you look at the price. Until then, the formula cells show zeros and #DIV/0!.
- **Company X (example)**: the book's invented company, landing on $7.26 / $15.71 / $29.72 and a buy zone of $11.78.

Rows 14-17 are the book's formulas, copied across to C and D. Row 19's buy zone uses the book's 25% cushion: "The 25% is my choice, not a law. Pick your own cushion and write it on the card." Yours goes in place of the 0.75 in C19.

Rank the three on [`idea-list.txt`](idea-list.txt), saved as `ideas-[date]`.

> Three new candidates, each with a cited memo, a bear case with three breakers, and a value range and buy zone that your spreadsheet computed from tagged inputs and your written assumptions. No value, range or buy zone anywhere on the list came from the model.
