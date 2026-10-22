# Week 08 — Home exercises

Work through these before the next lecture. They cover everything from [`08-summarizing-and-combining.ipynb`](08-summarizing-and-combining.ipynb): grouping and aggregating, the index of a grouped result, transforming within groups, dates, `resample`, `concat`, duplicates, and `merge` together with the checks that tell you it worked.

Work in a **notebook**, as last time. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: import what you need, load your own data, and make sure the whole thing runs from top to bottom before you call it finished.

---

## Before you start

One thing the lecture did not cover, and exercise 4 needs it.

### Asking Python what is in a folder

So far every file you have opened, you have named yourself. That stops working the moment a folder holds ten files, or a hundred, or a number that changes every month. `os.listdir` hands you the names.

```python
import os

files = os.listdir("../data/stocks")
print(files)
```

Three habits worth building around that one line.

**Filter to the files you actually want.** A folder is rarely as tidy as you hope: `.ipynb_checkpoints`, a stray `notes.txt`, a `.DS_Store` that macOS put there without telling you. Handing any of those to `read_csv` gives you an error at best.

```python
files = [f for f in os.listdir("../data/stocks") if f.endswith(".csv")]
```

**Sort it.** `os.listdir` makes no promise about order, and an analysis whose output depends on the order the operating system happened to return files in is not reproducible. `sorted()` returns a list in order and costs nothing.

**Join the folder onto the name.** `listdir` gives you `"AAPL.csv"`, not `"../data/stocks/AAPL.csv"`. `os.path.join` builds the full path with the right separator for whichever computer is running the code — which matters, because Windows and macOS disagree about which way the slash leans.

```python
for name in sorted(files):
    path = os.path.join("../data/stocks", name)
    df = pd.read_csv(path)
```

The filename itself is often data. `"AAPL.csv"` tells you which company the rows belong to, and nothing inside the file does — so you take it apart with the string methods you already know: `name.split(".")[0]` gives `"AAPL"`.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out the rule that explains the real answer — that is the whole point of the exercise. Every one of these runs without an error, and most of them are wrong in a way nothing warns you about.

**a)**

```python
import pandas as pd

sales = pd.DataFrame({
    "shop": ["A", "B", "A", "B"],
    "day":  [1, 1, 2, 2],
    "sold": [10, 20, 30, 40],
})

result = sales.groupby("shop")["sold"].sum()

print(type(result))
print(result)
print(result["A"])
```

**b)**

```python
print(sales.groupby("shop")["sold"].mean().shape)
print(sales.groupby("shop")["sold"].transform("mean").shape)
```

**c)**

```python
staff = pd.DataFrame({
    "team":  ["red", "blue", None, "red"],
    "hours": [10, 20, 30, 40],
})

print(staff.groupby("team")["hours"].sum())
print(staff["hours"].sum())
```

**d)**

```python
survey = pd.DataFrame({
    "group": ["x", "x", "y", "y", "y"],
    "score": [4, None, 3, None, None],
})

print(survey.groupby("group").size())
print(survey.groupby("group")["score"].count())
print(survey.groupby("group")["score"].mean())
```

**e)**

```python
prices = pd.DataFrame({"item": ["tea", "coffee"], "value": [30, 45]})
sold = pd.DataFrame({"item": ["tea", "coffee", "tea"], "value": [2, 1, 4]})

both = sold.merge(prices, on="item", how="left")

print(both.columns.tolist())
print(both)
```

**f)**

```python
panel = pd.DataFrame({
    "country": ["A", "B", "A", "B", "A"],
    "year":    [2021, 2020, 2020, 2021, 2022],
    "value":   [2.0, 100.0, 1.0, 101.0, 4.0],
})

panel["change"] = panel.groupby("country")["value"].diff()

print(panel)
```

**g)**

```python
dates = pd.DataFrame({
    "date":  ["10/01/2021", "02/11/2020", "05/06/2022"],
    "value": [1, 2, 3],
})

print(dates["date"].dtype)
print(dates.sort_values("date"))
print(dates["date"].max())
```

### Then: two broken snippets

Each of the two below does not do what its comment says. Say what is wrong, and write a corrected version.

```python
# 1 - meant to give each country's share of world emissions in 2023, in percent
co2 = pd.read_csv("../data/co2_emissions.csv")

year_2023 = co2[co2["year"] == 2023].copy()
year_2023["share"] = 100 * year_2023["co2_total"] / year_2023["co2_total"].sum()

print(year_2023.sort_values("share", ascending=False)[["country", "share"]].head())
```

```python
# 2 - meant to give each country's most recent renewable energy figure
co2 = pd.read_csv("../data/co2_emissions.csv")

latest = co2.dropna(subset=["renew_energy"]).drop_duplicates(subset="country")

print(latest[latest["country"] == "Norway"][["country", "year", "renew_energy"]])
```

---

## 📚 Exercise 2: Summarizing the panel

Start from the lecture's `load_emissions` — copy it into your notebook — and load `../data/co2_emissions.csv` with it.

1. **What can you actually study?** With one `groupby`, count the non-missing values of every column in every year. Display a handful of years from across the period, and say in a markdown cell which indicators you could use for a study of 2023, and which you could not.

   Then turn the question round: for each entity, count how many years of `gdp_pc` it has. How many entities have the complete 24-year series, and how many have none at all?
2. Build an `income_group` column: use `np.select` on `gdp_pc`, with the bands from last time — below 1 000 is `"low"`, below 10 000 `"lower-middle"`, below 50 000 `"upper-middle"`, and above that `"high"`. Make sure rows with no `gdp_pc` end up as missing rather than `"high"`.

   Restrict to 2023 and build a summary table with one row per income group and three named columns: the number of entities, total emissions, and mean emissions per person. Then check: do the group totals add up to the column total? Explain any difference in a markdown cell.

### Then: a baseline over part of the period

Climate work rarely compares a year against the whole record — it compares it against a fixed **baseline period**. Compute, for each entity, its average `co2_pc` over **2000–2009**, and then an `anomaly` column giving every row's distance from its own entity's baseline.

The baseline is an average over *some* of each entity's rows and has to end up beside *all* of them. `transform("mean")` averages over every row in the group, so on its own it gives you the wrong average. Compute the baseline as its own small table, then bring it back with a merge — and validate that merge.

Display the five entities with the largest anomaly in 2023. One of the five is not a country. Say in a markdown cell how you can tell, and what you would need in order to remove it.

### Finally: your bands against the World Bank's

`../data/country_info.csv` has the World Bank's own classification of every country, in `incomeLevel`. Merge it on, drop the aggregates, and restrict to 2023.

1. Count how many countries fall in each combination of the World Bank's level and your band. How often do the two agree?
2. Find the thresholds the World Bank actually uses (search for "World Bank country income classification"), rebuild your bands with them, and count again. Write a short markdown cell on why your first bands disagreed so badly, and why even the corrected ones cannot agree perfectly.

> 💡 **Tip:** To compare the two classifications row by row they need the same labels. Giving your `np.select` call the World Bank's own labels — `"Low income"`, `"Lower middle income"`, and so on — is the shortest way.

---

## 📚 Exercise 3: The NASDAQ in real terms

Every NASDAQ figure in the lecture was **nominal**: in dollars of the day. But a dollar in 1975 bought far more than a dollar in 2015, so a nominal index mixes two things together — what shares did, and what money did. This exercise separates them.

Load `../data/NASDAQ.csv` and convert `Date` properly, saying the format explicitly.

1. **The worst months.** Resample to monthly closing levels and find the three worst months in the whole series. The worst one is more than fifty years old — look up what happened that month.
2. **Bring in prices.** Resample to annual closing levels, and turn the result into a table with a `year` column. Then load `../data/FRED_annual.xlsx`, which holds annual US macroeconomic series including the consumer price index, `CPI`, and merge `CPI` on by year. Use `validate=` and `indicator=True`, and report which years did not match and why. Decide which kind of join you want, and say why.
3. **Real returns.** Convert the annual closing level into **constant 1999 dollars** — divide by that year's CPI and multiply by 1999's CPI — and compute the yearly percentage change of both the nominal and the real level. Report the five worst years in real terms, and compare them against the nominal ranking. Which decade looks much worse once inflation is taken out?
4. **The lost decade, again.** Report the closing level at the end of 1999 and at the end of 2009, and the percentage change between them, in nominal and in real terms. Then find the first year in which the index closed above its 1999 level again — once in nominal terms and once in real terms.

Write a short markdown cell on what this means for the "shares go up over time" claim — and note that this series is the NASDAQ, which is unusually concentrated in technology companies.

> 💡 **Tip:** `resample` needs the dates as the index and in order — `.set_index("Date").sort_index()`. And `reset_index()` turns the dates back into an ordinary column when you need one to merge on.

---

## 📚 Exercise 4: Ten companies through 2020

The folder `../data/stocks/` holds one CSV per company: daily prices and volume for 2020, ten tickers, same columns in each. The company name appears nowhere inside the files — only in the file name.

**Task 1.** Read all ten into a single DataFrame, using `os.listdir` and a loop as described in "Before you start". Add a `ticker` column taken from the file name, convert `Date` with an explicit format, and combine with `concat`. You should end up with 2 520 rows and 10 tickers.

**Task 2.** Check the combined table before you trust it: how many rows are exact duplicates, and how many `ticker`–`Date` combinations appear more than once? Say in a markdown cell why both checks are worth doing, and what it would mean if the second one found something the first did not.

**Task 3.** Compute the total monthly `Volume` for each ticker in three ways, and confirm all three agree.

1. With a **loop** and no pandas grouping at all: an outer loop over tickers, an inner loop over months, collecting the results into lists and building a DataFrame at the end.
2. With `groupby`.
3. With `resample`.

Then write a paragraph comparing them. Which would you actually write, and what did the loop cost you in lines and in the number of places a mistake could hide?

**Task 4.** The ten share prices are on completely different scales, so compare them the way the financial press does: **rebase** each ticker to 100 on its first trading day, so that 150 means "up 50% since 2 January". Use `Adj Close`, the price adjusted for stock splits and dividends. Report each ticker's lowest rebased level of the year and its level on the last day, sorted by the last.

**Task 5.** The pandemic crash ran from the market peak on **19 February 2020** to the bottom on **23 March 2020**. Filter to those dates and report how far each ticker fell between the first and the last day of the window, from worst to best. Write a sentence on whether the ranking is what you would have guessed.

**Task 6.** A day's traded volume means little on its own — Apple trades more shares on a quiet day than Walmart does on a busy one. Add a column giving each row's volume **relative to its own ticker's median volume**, and display the five days with the most unusual trading. Look up what happened on the top one.

> 💡 **Tip:** For the loop version, `df["Date"].dt.month` gives you the month of every row, so the inner loop can be `for month in range(1, 13)`. For the `resample` version, the lecture resampled a single series; here there are ten in one table. `resample` can follow a `groupby`, exactly like the other methods that must not run across a boundary: `stocks.set_index("Date").groupby("ticker").resample("ME")`.

---

## 📚 Exercise 5: A merge that goes wrong

**This exercise deliberately repeats the lecture.** The diagnosis of a failed merge is the most useful habit this week teaches, and the way to make it a habit is to do it yourself, from an empty notebook, without the lecture open. If you find yourself copying cells across, close the lecture and start again.

Load `../data/co2_emissions.csv` and `../data/country_info.csv`.

1. Merge them with an **inner** join, matching the emissions file's `country` against the lookup file's `name`. Report how many rows you had before and how many you have after.
2. Something is missing. Redo the merge as a **left** join with `indicator=True`, and report how many rows matched and how many did not.
3. Identify the entities that failed to match, and then work out *why* they failed even though they are plainly present in both files. Print the evidence, do not just assert it.
4. Fix it **two ways**, and confirm both give the same row count: once by cleaning the key, and once by choosing a better key. Say in a markdown cell which you would use here and which you would use on a file that had no code column.
5. With the merge fixed, add `validate=` set to the shape you believe the merge has. Then deliberately claim the wrong shape and show the error.

### Then: the other side of the merge

Everything above asked which *emissions* rows found no match. Now ask the opposite: which entities in the *lookup file* match nothing in the emissions file? Use the `how=` that keeps unmatched rows from both sides, with `indicator=True`, and report how many lookup entries are unused and what kind of entity they are. Say in a markdown cell whether they matter for this analysis, and when unused lookup entries *would* matter.

---

## 📚 Exercise 6: A loader you will call more than once

Last time you wrote `load_emissions`, and this week's lecture opened by calling it in one line. This exercise writes its successor — the version that also brings in the country file.

Wrapping loading and cleaning in a function is worth doing for one reason above all: **you run it more than once.** Here that is literal, because the questions below need the table two different ways.

Write `load_panel(emissions_path, info_path, countries_only=True)` that:

1. Reads the emissions file and drops rows with no `co2_total`.
2. Adds `co2_pc`, emissions in tonnes per person.
3. Reads the country file, renames `incomeLevel` to `income_level`, and merges it on, bringing across `region` and `income_level`, using the key that works and `validate=` set to the right shape.
4. Checks that the merge did not change the row count, and **raises a `ValueError` with a useful message** if it did.
5. If `countries_only` is `True`, drops the entities whose region is `"Aggregates"`. If it is `False`, keeps them.
6. Returns the result with a clean index. It should not print anything.

Give it a docstring in the longer format, saying what each parameter does, what comes back, and what it raises.

Then, below the function:

- Call it both ways and confirm you get 4 872 rows with the default and 5 904 with `countries_only=False`.
- **Who emits?** For every year, compute each income level's share of that year's total emissions across the 203 countries, as ordinary columns rather than as an index. Display the shares for 2000, 2010 and 2023, and describe in a sentence what changed.
- **Check yourself against the World Bank.** The aggregates include a `Middle income` entity. Using both of your tables, compare its 2023 emissions against your own total for the lower-middle and upper-middle countries. Report the difference.
- **Per person, two ways.** For 2023, compute each income level's emissions per person — total emissions divided by total population, not the average of its countries' figures. Do it twice: once by writing a function that takes one group's rows and returns the figure, and calling it with `.apply()` on the groupby; and once without a function, by summing the two columns within each group and dividing. Confirm the two agree, and say in a markdown cell which you would write and why.
- Compare that against the plain average of `co2_pc` within each income level, and write a short markdown cell on which level the two disagree about most, and why.

> 💡 **Tip:** Keep the function in its own cell, with the calls that demonstrate it in the cells
below. A function tangled up with the code that uses it is a function you end up rewriting.

> 💡 **Tip:** A check that raises is worth more than a comment saying what should be true.
`if len(after) != len(before): raise ValueError(...)` turns a silent wrong answer into a stack trace,
which is the trade this whole week has been arguing for.

> 💡 **Tip:** `.apply()` on a groupby calls your function once per group and hands it that group's
rows as a DataFrame, so the function can use as many columns as it needs. Select the columns first —
`.groupby("income_level")[["co2_total", "population"]].apply(...)` — so the function sees only what
it uses.
