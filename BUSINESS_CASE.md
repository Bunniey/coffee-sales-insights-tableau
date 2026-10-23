# From dashboard to operating decisions

## Context and objective
A coffee vending-machine operator needs to decide which drinks to keep available, when to replenish and service the machine, and how to interpret sales changes. Saksham Chauhan's Tableau dashboard addresses these questions through product revenue, monthly revenue, hourly cups and daily time-slot revenue views.

This is an educational analysis for Analyst Club's Friday Challenge. The stakeholder roles and proposed operating measures below are analytical framing, not evidence of a stakeholder engagement or implemented project.

## 1. Product mix: distinguish value from volume
The product revenue chart puts Latte first (27,866.30), followed by Americano with Milk (25,269.12) and Cappuccino (18,034.14). Latte contributes 24.14% of revenue. The top two drinks together contribute 46.03%.

Source verification adds a useful distinction: Americano with Milk sells 824 cups versus Latte's 782. Replenishment should consider units and ingredient recipes, while commercial prioritisation should consider revenue and margins. Espresso's 2,814.28 revenue alone is insufficient grounds to remove it.

**Proposed action:** review ingredient coverage for leading drinks before peak periods. **Measure:** stockout minutes by drink, ingredient waste and contribution margin, once collected. **Decision condition:** increase replenishment only where service improvement justifies added waste and servicing cost.

## 2. Hourly demand: make the machine ready before the peak
The hourly chart peaks at 349 cups between 10:00 and 10:59, or 9.60% of all cups. The next busiest slots are 11:00 (294) and 16:00 (283). These are accumulated totals over the dataset, not daily demand forecasts.

**Proposed action:** pilot a pre-peak refill check and a second inventory assessment before 16:00. Schedule maintenance using both demand and actual operating hours. **Measure:** peak-window availability, stockouts and replenishment visits. **Additional evidence:** capacity, downtime, recipes, operating schedule and daily variability.

## 3. Monthly trends: investigate peaks without assuming a cause
October 2024 generates 13,891.16 from 426 cups, ahead of February 2025 at 13,215.48 from 423 cups. January 2025 generates 6,398.86. The dashboard reveals variation but cannot attribute it to seasonality, promotions or changing footfall.

**Proposed action:** investigate prices, operating days, location events and outages. Compare revenue and cups per operating day once the schedule is available. March 2025 ends on 23 March and must be labelled partial; a raw full-month comparison would be misleading.

## 4. Time slots: translate the extra dashboard view into service planning
The Tableau calculation defines Morning as 06:00–12:59, Afternoon as 13:00–16:59, Evening as 17:00–18:59 and Night as all other hours. Verified revenue shares are 39.03%, 27.19%, 13.13% and 20.65%, respectively.

The daily stacked area chart helps locate variation over time, but the time bands have different lengths. Their total shares do not establish which band has the greatest revenue intensity per hour. The hourly view is better suited to specific refill timing.

## 5. Payment reliability: interpret the denominator correctly
Card revenue is 112,245.58 (97.24%); cash revenue is 3,186.00 (2.76%). Card-paid cups represent 97.55% of all cups. These are different metrics, and neither directly measures customer preference.

**Proposed action:** monitor terminal availability and failed payments, while assessing cash-service requirements before changing payment options. **Measure:** failed-payment rate and terminal downtime. The dataset contains successful sales, not failed attempts.

## Scope and evidence
All numerical results use the supplied Excel snapshot (1 March 2024–23 March 2025), with the existing Tableau views as the presentation framework. No costs, margins, stock levels, failed transactions, operating calendar or intervention results are available. No profit improvement, revenue uplift or causal impact is claimed.
