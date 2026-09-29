# Chapter 3: set up the desk, then score two models

The desk itself is the [Start here](../../README.md#start-here) steps. This folder is the head-to-head: one memo request in two products, scored on five lines you check yourself. "The model never grades itself."

1. Note your stock's newest 10-Q or 10-K and its filing date on EDGAR. That's the answer key for "current."
2. Paste this request, with your ticker, into a Research Desk chat. In the other product (ChatGPT's free plan works), paste your memo template first, then the same request.

   ```
   Write a one-page memo on [TICKER] using memo-template.
   Use the company's most recent 10-Q or 10-K. For every number,
   give form, filing date, section and period, and cite the source.
   Include a real bear case built from facts, not a disclaimer.
   Do not predict the price or tell me to buy or sell.
   If you can't find something, write NOT FOUND.
   ```

3. Score both on [`model-scorecard.txt`](model-scorecard.txt). A half-right line is a zero.
4. Add one sentence naming your pick and the line that decided it, and save it to Research Desk as `model-scorecard`.

The four follow-ups (Tag it, Which period?, Quote it, Argue with it) close out [`research-questions.txt`](../../research-desk/knowledge/research-questions.txt), so the desk knows them by name.

> Your Research Desk project lists your three files when asked, repeats the tag rule back, and returns a memo in your template's six-field shape on a stock you own. Your scorecard has a number in every cell and one sentence naming the deciding line.

Your list runs past three files if you uploaded all of `knowledge/`. Rerun the scorecard when a new model ships.
