# Chapter 4: connect the clerk

The clerk fetches three numbers from a filing and tags each one. You check them against the filing yourself: Apple first, where the answers are known, then a stock you own.

## Give the desk a source

Start with the filing drop: save the filing from EDGAR, or print the pages you need to PDF, and upload it to Research Desk. For the calibration run, that's Apple's 10-Q for the quarter ended June 27, 2026:

```
https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm
```

Then add one connector: go to **Customize > Connectors**, click **"+"**, choose **"Add custom connector"**, paste the service's address, open Advanced settings only if the service gave you sign-in details, and click **"Add"**. The free Claude plan gets one custom connector. The book picks Equibles (`https://mcp.equibles.com/mcp`), the only free tier whose vendor page says it includes the earnings-call transcripts Chapter 6 needs. Financial Modeling Prep (FMP) is in Claude's own directory. edgar.tools' free tier can't pass the test below. Plans change, so check the vendor's page before you pay.

In any chat where the clerk fetches, set the connector to **"Always available"** under "+" > Connectors > Tool access.

## Block the order tools first

> Not "Needs approval." Blocked. An approval prompt at the end of a long session is a button you'll eventually click without reading.
>
> Apply the same check to any connector you ever add: open Tool permissions and read the list before the first chat. If a tool's name starts with place, modify, cancel, delete, buy, sell or transfer, it gets Blocked.

Equibles' portfolio tools (`CreateMyPortfolio`, `AddPortfolioLot`) go to Blocked as well. Skip Zerodha's Kite connector. Your desk doesn't need your holdings to read filings.

## The three-number test

[`desk-pull.txt`](../../research-desk/knowledge/desk-pull.txt) is already in your desk. In a new chat in the project:

```
desk-pull AAPL · 10-Q filed 2026-07-31 · three months ended June 27, 2026
```

Check the answers on the top table of [`tag-check.txt`](tag-check.txt), whose "Filing says" column is the book's Apple key. Two traps wait. $364,357M next to "Total net sales" is nine months, not the quarter, and 14,608,963 thousand shares is the balance sheet as of June 27, not the cover page as of July 17. If it returns either one, don't fix it yourself. Ask, and note which trap it fell into:

```
Which period is that?
```

Then run the same request on your own stock and its newest 10-Q or 10-K. On the bottom table you fill in "Filing says" yourself. Finish with [`data-source-card.txt`](data-source-card.txt), saved to Research Desk as `data-source-card`.

Chapter 4's checkpoint:

> Three numbers on your own stock (revenue, gross margin, share count) come back from the desk with a filing name and a date, and all four lines of your tag-check table match when you open the filing yourself (gross margin counts twice: once in dollars, once as a percent). Apple matched first, on all four lines, including the gross margin percentage. No connector on your desk has an order tool set to anything but Blocked.
