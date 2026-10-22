# Assignment 2 — Electricity in Europe

In this assignment, you will analyze how much electricity European countries use, and how that has changed over two decades. The data comes straight from [Eurostat](https://ec.europa.eu/eurostat), the statistical office of the EU, in the format Eurostat publishes it — which means that before you can analyze anything, you have to read and clean a file that was made for people to look at, not for programs to read.

The assignment draws on everything from the course so far: functions, loops and decisions from the first half, and reading, cleaning, combining and summarizing data with pandas from the second.

**Before you start:**

- Set up a folder for the assignment as described in [Your folder](#your-folder). Everything you need is already in the `data` folder you downloaded at the start of the course.
- Work in **one notebook**, and build it in the four parts below, **in order**. Each part builds on the one before it.
- Start each part with a markdown heading, and answer every written question in a markdown cell, in a few sentences of your own.
- Your notebook must run from top to bottom without errors. Check this with **Restart** and **Run All** before you finish.

> 💡 **Tip:** If you use an AI assistant, read the [AI guidelines](../../guides/ai-guidelines.md) first. This assignment is a chance to practice, and you only get the practice by writing the code yourself.

---

## Your folder

Your assignment must be a **self-contained folder**: someone else should be able to take the whole folder, open the notebook on their own computer, and run it. That means the data has to be inside the folder, and every path in your notebook has to be **relative** to it.

Set it up like this:

```
assignment2/
├── assignment2.ipynb
├── data/
│   ├── eurostat.xlsx
│   ├── co2_emissions.csv
│   └── country_info.csv
└── output/
```

- Copy the three data files from the course's `data` folder into the assignment's own `data` folder.
- Your notebook sits next to `data`, so it reads `"data/eurostat.xlsx"` — no `../` in front, and no path that starts with `C:\` or `/Users/`.
- Everything your notebook **creates** goes in `output`, never in `data`. Let the notebook create the folder itself, so it works on a computer where the folder does not exist yet:

  ```python
  import os

  os.makedirs("output", exist_ok=True)
  ```

  `exist_ok=True` tells Python not to complain if the folder is already there, so the cell can be run again.

---

## The data

`eurostat.xlsx` holds Eurostat's table of **electricity available for final consumption**, in gigawatt hours (GWh), for 2001–2023: the electricity that reaches the people, businesses and industries that use it. One GWh is a million kilowatt hours (kWh); a typical household uses a few thousand kWh a year.

The file covers the EU countries, a few other European countries, and two groupings of countries. If you have done the home exercise on reading awkward files, you have already read this file once, and that code is a good starting point for Part 1. If not, open the file in Excel first and look at it before you write any code.

The other two files are the World Bank files from the lectures: `co2_emissions.csv` for population, and `country_info.csv` for each country's income level.

---

## Part 1 — Read and clean

1. Read the data on `Sheet 1` into a DataFrame. Every year in the sheet has **two** columns: the value, and a column of flags beside it. Keep the country column and the value columns only, and make sure Eurostat's symbol for a missing value is read as missing. Every year column should end up **numeric**: check the dtypes.
2. Rename the first column to `country`, and keep only the rows that hold data — not the header row above the names, and not the notes below them. Report how many rows you had before and after.
3. Two of the rows are not countries but groupings of countries. Put them in a separate DataFrame, `aggregates`, and keep the countries in another, `countries`.
4. Count the missing values in every year. Which is the **latest year** with data for nearly every country? Use it as the end year for the rest of the assignment. Then look at the countries with gaps in the earlier years, and say what kinds of gap there are.

**Check:** you should have 43 data rows, of which 2 are aggregates and 41 are countries, with 24 columns.

> 💡 **Tip:** `read_excel` has a parameter for each of the things you need to deal with: which sheet, how many rows to skip, which columns to keep, and which values count as missing. The [`read_excel` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) is long; search it for the words you need rather than reading it.

---

## Part 2 — A function, then the pandas way

1. Write a function `percent_change(old, new)` that returns the change from `old` to `new` in percent of `old`. It must follow these rules:
   - If either value is missing, it returns `np.nan`.
   - If `old` is zero or negative, a percentage change is undefined, so it **raises a `ValueError`** with a message saying what is wrong.

   Give it a docstring saying what it does, what each parameter is, what it returns, and what it raises. Then test it on every case in the table below. For the last two, catch the error with `try`/`except` and print its message.

   | `old` | `new` | Expected |
   | --- | --- | --- |
   | `100` | `150` | `50.0` |
   | `200` | `150` | `-25.0` |
   | `80` | `80` | `0.0` |
   | `100` | `np.nan` | `nan` |
   | `np.nan` | `100` | `nan` |
   | `0` | `50` | `ValueError` |
   | `-10` | `50` | `ValueError` |

2. Use a **loop** and your function to compute each country's percentage change from 2001 to your end year, and store the results in a new column.
3. Compute the same change again **without a loop**, in a single expression on the two columns. Check that the two versions agree, and say in a markdown cell which one you would use, and what the function is still good for.

> 💡 **Tip:** `pd.isna(value)` is `True` if a single value is missing. And be careful when you compare the two versions: `np.nan == np.nan` is `False`, so a plain `==` reports a disagreement wherever both versions are correctly missing. Check that they are missing in the same rows, and that the largest absolute difference between them is (close to) zero. `.abs()` turns every value in a Series into its absolute value, so `(a - b).abs().max()` gives the largest difference in either direction, skipping the missing values.

---

## Part 3 — Classify, rank and check

1. Use `np.select` to add a column `trend` that labels each country's change from 2001 to the end year:

   | Change | `trend` |
   | --- | --- |
   | 20% or more | `strong growth` |
   | 5% or more, but less than 20% | `growth` |
   | more than −5%, but less than 5% | `stable` |
   | −5% or less | `decline` |
   | missing | `no data` |

   Count how many countries have each label.
2. Display the five countries with the largest rise and the five with the largest fall.
3. **A sanity check.** A surprising number can be a discovery or a mistake in the data, and the only way to tell is to look. Use a **loop** over each pair of adjacent years (2001 and 2002, 2002 and 2003, and so on) to find the **largest one-year percentage change** for any country in the whole table. Report the country, the year and the change.

   Is it plausible? Look at that country's figures for the surrounding years, and explain your judgment in a markdown cell. If you conclude that a value is an error, set it to missing, say why, and redo the change and the `trend` column so that the rest of your analysis uses the corrected table. Did it change your answer to question 2?
4. **Does the EU add up?** One of the aggregate rows is the EU's 27 member countries:

   ```python
   eu_members = [
       "Belgium", "Bulgaria", "Czechia", "Denmark", "Germany", "Estonia", "Ireland",
       "Greece", "Spain", "France", "Croatia", "Italy", "Cyprus", "Latvia",
       "Lithuania", "Luxembourg", "Hungary", "Malta", "Netherlands", "Austria",
       "Poland", "Portugal", "Romania", "Slovenia", "Slovakia", "Finland", "Sweden",
   ]
   ```

   Use a loop over the years up to your end year to check whether the EU row equals the sum of its members in every year. Report the largest difference you find, and say what you checked to make sure the comparison is fair.
5. **Export** your cleaned `countries` table, with the change and `trend` columns, to `output/electricity_clean.csv`. Read the file back in and check that it contains what you meant to save.

---

## Part 4 — Merge and summarize

1. **Population.** From `co2_emissions.csv`, take each country's population in your end year. Merge it onto `countries` by country name, with a **left** join, `validate=` set to the shape the merge should have, and `indicator=True`. How many countries matched?

   Some did not, although every one of them is in the World Bank file. Find out why, fix it, and merge again until every country matches. Say in a markdown cell why each one failed.
2. **Income level.** Merge on each country's `incomeLevel` from `country_info.csv`, using the column that matches best, with `validate=` again.
3. **Electricity per person.** Add a column `eu_member` saying whether each country is in the EU, and a column with each country's electricity use in **kWh per person** in the end year. Display the five countries with the highest and the five with the lowest figure.

   Which countries are missing from the ranking? Use the figures you do have to estimate where one of them would rank, and say whether it changes the picture.
4. **A summary table.** Group the countries by **EU membership and income level**, and build a table with one row per group and these columns:
   - the number of countries in the group, and how many of them have a figure for the end year,
   - total electricity use in GWh, and total population,
   - electricity use **per person** for the group as a whole: the group's total electricity divided by its total population,
   - the **average** of the countries' own per-person figures.

   Make sure the totals are computed over the same countries, so that no group is divided by the population of a country whose electricity was not counted. Then **export** the table to `output/electricity_summary.xlsx`, with the groups as ordinary columns rather than as an index.

   In a markdown cell, describe what the table shows in a few sentences. Why do the two per-person columns differ, and which group's figure would you trust least, and why?

**Check:** on the first attempt, 38 of the 41 countries should match the World Bank file. Of the 41 countries, 31 are high income and 10 upper middle income.

> 💡 **Tip:** Merging and grouping are covered in the [lecture on summarizing and combining](../../week08/08-summarizing-and-combining.ipynb), including how to find the rows a merge failed to match. Grouping on two columns at once works exactly like grouping on one: pass a list.

---

## Organizing your notebook

A notebook of this size is much easier to write, read and fix when every part follows the same pattern: a markdown cell saying what the next step does, a code cell that does it, and the output that shows it worked. Keep each code cell to one step. Load and clean the data **once**, at the top, and build every later part on the same DataFrames rather than reading the files again.

Functions are welcome anywhere they make the notebook clearer, but the only one the assignment requires is `percent_change`.
