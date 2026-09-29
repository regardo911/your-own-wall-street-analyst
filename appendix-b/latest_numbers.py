import json, sys, urllib.request
from datetime import date

HEADERS = {"User-Agent": "Your Name your.email@example.com"}  # SEC refuses requests without one

def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.load(r)

cik = sys.argv[1].zfill(10)  # e.g. 320193 -> 0000320193
facts = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
gaap = facts["facts"]["us-gaap"]

def days(x):
    return (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days

def latest(tag, unit="USD"):
    # One 10-Q holds the quarter AND the year-to-date figure, same filing date.
    # Keep only ~3-month periods so the quarter is what comes back.
    rows = [x for x in gaap[tag]["units"][unit]
            if x.get("form") in ("10-Q", "10-K") and "start" in x and 80 <= days(x) <= 100]
    return max(rows, key=lambda x: (x["filed"], x["end"]))

rev = latest("RevenueFromContractWithCustomerExcludingAssessedTax")
gp = latest("GrossProfit")
shares = max(facts["facts"]["dei"]["EntityCommonStockSharesOutstanding"]["units"]["shares"], key=lambda x: x["filed"])
print(f"{facts['entityName']}")
print(f"Revenue      {rev['val']:>18,}  {rev['form']} filed {rev['filed']}  period {rev.get('start')}..{rev['end']}  accn {rev['accn']}")
print(f"Gross profit {gp['val']:>18,}  {gp['form']} filed {gp['filed']}  period {gp.get('start')}..{gp['end']}")
print(f"Gross margin {gp['val']/rev['val']:.1%}  (computed here from the two lines above)")
# added to the book's version: revenue and gross profit are picked separately, so they can come from different periods
if (rev["start"], rev["end"]) != (gp["start"], gp["end"]):
    print("WARNING: revenue and gross profit are from different periods, so the margin above mixes them. Don't use it.")
print(f"Shares out   {shares['val']:>18,}  as of {shares['end']}  {shares['form']} filed {shares['filed']}")
