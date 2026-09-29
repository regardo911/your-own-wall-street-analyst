# Chapter 6: read every earnings call

Attach this quarter's transcript, last quarter's, and the results release, then run [`desk-calls`](../../research-desk/knowledge/desk-calls.txt) with your own ticker and dates in place of the book's:

```
desk-calls GIS · THIS = Sept. 23 call (fiscal Q1) · LAST = July 1 call (fiscal Q4)
```

Give it only the part of a transcript page headed **Full Conference Call Transcript**, never the summary blocks above it. No transcript for a company? Run it on the last two results releases, with this line added under the command:

```
SOURCE: RELEASES ONLY. THIS and LAST are results releases, not call transcripts, so skip the transcript-section rule, quote the release where a speaker would go, and write NO CALL under ASKED.
```

Run your top four holdings, one chat each, then paste each result's last line and guidance status into one more chat, under this:

```
Combine these four desk-calls results into one earnings-season note.
For each ticker, one block:
- Biggest change (quote THIS and LAST)
- Guidance: MATCHES release / DIFFERS / NO GUIDANCE GIVEN
- One question this raises for my thesis card
Order the tickers by how much the change matters to the thesis card,
most first. No predictions, no buy/sell.
```

Save each stock's ASKED group as `asked-[TICKER]`; the bear reads it in Chapter 8.

Done when:

> Every change in every desk-calls result quotes both transcripts, with speakers. Every guidance number has been matched by you against the company's own results release, and each one is marked MATCHES or DIFFERS. The four-holding note exists and names one thesis-card question per stock.
