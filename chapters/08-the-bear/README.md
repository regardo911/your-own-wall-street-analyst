# Chapter 8: the bear

A second analyst builds the strongest honest case against each stock you own, from a project that never sees your opinion.

## Build the wall

1. Clear anything about your holdings or opinions out of Claude's global instructions (Settings > General). The bear would see it.
2. Create a second project, **Bear Desk**. Paste [`bear-desk/project-instructions.txt`](../../bear-desk/project-instructions.txt) into its instructions and upload [`desk-bear.txt`](../../bear-desk/knowledge/desk-bear.txt).
3. Per stock, copy `memo-[TICKER]` into `stripped-[TICKER]` and delete fields 1, 2, 4 and 6. Upload it with the stock's filing sections, latest call transcript and `asked-[TICKER]`.

[`what-the-bear-sees.txt`](what-the-bear-sees.txt) is the book's list of what goes in and what never does.

## Prove it's blind, then run it

In a fresh Bear Desk chat:

```
Based only on what's in this project, what do you think I believe about [TICKER], and do I own it?
```

The right answer is some version of "nothing here tells me." If it can describe your thesis, find the leak first. Then, in a new chat, `desk-bear [TICKER]`. A breaker that stays true with another company's name swapped in is boilerplate; send it back:

```
Breaker 2 would be true of any company. Replace it with one only this company's filings support.
```

Open a citation per breaker and strike any that don't hold up; mark the rest NEW or ALREADY ON CARD against your card, by hand. Do every holding, then copy the breakers and watch items into Research Desk as one file, `breakers`, for the morning run.

## The checkpoint

> On at least one holding, the bear names a thesis-breaker that is not on your thesis card, and you opened its citation and found the quoted text in the filing. Every breaker on every holding has a WATCH and a TRIGGER.
