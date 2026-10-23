# Validation and Tableau opening notes

## What was checked
- Read the existing Tableau workbook's XML, chart definitions, calculated fields and connection metadata, and inspected the supplied dashboard screenshot.
- Recomputed full-period metrics and chart aggregates from the supplied Excel data.
- Confirmed 3,636 rows, 8 drinks, no exact duplicate rows, positive sales amounts, matching date/datetime dates, and no missing values outside the card identifier field.
- All 89 missing card IDs correspond to cash payments, as expected by the guide. No rows were deleted.
- Supporting results are in `the included CSV and JSON files (or results/ after rerunning the script)`; rerun `validate.py` to reproduce them.

## Existing dashboard scope
The screenshot shows KPI panels with 944 cups, 30.7K revenue, 100% Card Share and 32.5 Money. These do not reconcile to the complete source dataset, while the chart panels span March 2024–March 2025. The extension cards show comparison-period labels, but their exact runtime aggregation, filter scope and data refresh state have not been verified. The discrepancy must be investigated in Tableau rather than assigned to a presumed quarter. Do not present those cards as all-period KPIs.

The complete dataset baseline is 3,636 cups, 115,431.58 revenue, 31.75 average price and 97.24% card revenue share. The screenshot is retained as originally provided, not relabelled or retouched.

## Card Share definition
The workbook uses a row-level flag `If [cash_type]='Card' THEN 1 ELSE 0 END`, then divides its sum by `COUNT([date])`. That measures the share of cups paid by card (97.55% across the source), not the guide's revenue share (97.24%). Source payment values are lowercase; normalise casing explicitly when revising.

For a future Tableau revision, use:

```text
IF SUM([money]) = 0 THEN 0
ELSE SUM(IF LOWER([cash_type]) = 'card' THEN [money] ELSE 0 END) / SUM([money])
END
```

Format as a percentage and label it **Card Revenue Share**. It should show 0% with Cash selected and 100% with Card selected. The packaged original workbook has not been modified.

## Opening the original workbook
The `.twb` contains definitions, not a bundled data extract. It references an Excel path on the author's Windows machine and a temporary Hyper extract that was not attached. Reconnect Excel to the repository's `Coffee_Sales_Dataset.xlsx`, then recreate the extract if requested. The original source build is Tableau 2026.2.3.

The dashboard uses an Infotopics Power KPIs extension. Its availability and rendering depend on Tableau and extension settings. Desktop execution, filter behaviour and extension loading could not be tested here.

## Challenge alignment and next checks
The guide is an Excel/PivotTable walkthrough; this portfolio is a Tableau adaptation. Product revenue, monthly revenue and hourly cups are visible, plus the additional time-slot chart. Do not claim the Excel slicers or PivotTables were built in this project.

Before a refreshed public dashboard export:
1. Align the four KPI panels with the intended date scope and clearly label any quarterly comparison.
2. Use the revenue-based Card Share definition and label Money as Average Price per Cup.
3. Confirm coffee, payment and month filters update every relevant view; test Latte then Cash, and clear filters.
4. If strict brief compliance is required, add/verify a payment-revenue share chart; it is not visible in the supplied screenshot.
5. Check the clipped Latte revenue label and export a new screenshot after extensions finish loading.
6. Keep March 2025 marked as partial.

These are documented follow-up checks, not claims of completed changes.
