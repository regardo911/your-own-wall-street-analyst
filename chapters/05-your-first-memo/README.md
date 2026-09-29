# Chapter 5: your first memo

One page on a stock you own, tested against your card, every number tagged to its filing.

## Run it

[`desk-memo.txt`](../../research-desk/knowledge/desk-memo.txt) is already in your Research Desk, and rule 8 runs it by name: the book's Option A, on every plan. With your stock's newest 10-Q or 10-K in the project (or reachable by your connector), open a new chat:

```
desk-memo [TICKER]
```

Scan for gaps first: an `[UNSOURCED]` tag, a number with no tag, a change-my-mind line marked CAN'T TELL. Untagged numbers go back with "Tag it."

## Check five sources

On [`five-source-check.txt`](five-source-check.txt), pick five tagged numbers, one or more of them CALCULATED, and open the filing to each tagged section. "For a CALCULATED number, 'on the page' means both inputs are on the page and your calculator gets the same answer." [`example-memo-aapl.txt`](example-memo-aapl.txt), the book's Apple memo, is the shape to match: six fields, every number tagged, the card test last.

> Five of five numbers match their source when you open it, including the period. The memo contains no number without a tag (every figure is tagged or marked `[UNSOURCED]`). Field 6 has an answer for every condition on your card: TRIPPED, NOT TRIPPED, or CAN'T TELL with the filing it needs.

Save the memo to the project as `memo-[TICKER]`, then run the rest of your cards, one stock per chat.

## Or as a skill (Option B)

[`desk-memo/SKILL.md`](desk-memo/SKILL.md) is the book's skill wrapper with the full command already pasted in. Turn on **Settings > Capabilities > "Code execution and file creation"**, zip the `desk-memo` folder, then **Customize > Skills > "+" > "+ Create skill" > "Upload a skill"**. The book suggests waiting until Chapter 10, where scheduled tasks can use it.
