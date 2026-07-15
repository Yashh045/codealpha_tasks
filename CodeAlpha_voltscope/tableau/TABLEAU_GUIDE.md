# Tableau Public Workbook Guide

Recreate the **VoltScope Executive Dashboard** in Tableau Public using the exported CSV files.

---

## Step 1 — Export data

From the project root:

```bash
python scripts/export_tableau_data.py
```

This creates three files in `tableau/data/`:

| File | Use for |
|------|---------|
| `voltscope_energy_full.csv` | Time-series, correlations, country comparisons |
| `voltscope_energy_2024_snapshot.csv` | KPI cards, rankings, donut charts |
| `voltscope_yearly_regional.csv` | Regional trend lines, stacked areas |

---

## Step 2 — Install Tableau Public

Download free at: https://public.tableau.com/

---

## Step 3 — Connect to data

1. Open Tableau Public → **Connect** → **Text file**
2. Select `tableau/data/voltscope_energy_full.csv`
3. Drag the table to the canvas → **Sheet 1**

---

## Step 4 — Build four views

### View A: Renewable Share Trend (Line Chart)

- **Sheet name:** `Renewable Trend`
- **Columns:** `year` (continuous)
- **Rows:** `renewable_share_pct` (average)
- **Color:** `country`
- **Filter:** Top 7 countries by 2024 renewable share
- **Chart type:** Line

### View B: Country Ranking 2024 (Bar Chart)

- **Data source:** `voltscope_energy_2024_snapshot.csv`
- **Sheet name:** `Country Ranking`
- **Columns:** `renewable_share_pct`
- **Rows:** `country` (sort descending)
- **Color:** `renewable_share_pct` (gradient: teal)
- **Chart type:** Horizontal bar

### View C: GDP vs Renewable (Scatter)

- **Data source:** `voltscope_energy_2024_snapshot.csv`
- **Sheet name:** `GDP Scatter`
- **Columns:** `gdp_per_capita_usd`
- **Rows:** `renewable_share_pct`
- **Size:** `total_consumption_twh`
- **Color:** `region`
- **Label:** `country`
- **Chart type:** Circle (scatter)

### View D: Regional Renewable Mix (Stacked Area)

- **Data source:** `voltscope_yearly_regional.csv`
- **Sheet name:** `Renewable Mix`
- Pivot or use:
  - **Columns:** `year`
  - **Rows:** `solar_twh`, `wind_twh`, `hydro_twh` (measure names / values)
- **Chart type:** Area (stacked)

---

## Step 5 — Assemble dashboard

1. **Dashboard** → **New Dashboard** → size **Desktop (1000 x 800)**
2. Title: **VoltScope Executive Dashboard — Global Energy Transition**
3. Add a **Text** object with KPIs from 2024 snapshot:
   - Avg renewable share
   - Total CO₂ emissions
   - Solar growth since 2015
4. Drag all four sheets into a 2×2 grid
5. Add a **Filter** for `region` that applies to all sheets

---

## Step 6 — Publish

1. **Server** → **Tableau Public** → **Save to Tableau Public**
2. Sign in and publish
3. Copy the public URL into your `README.md` and LinkedIn

---

## Color palette (match Python charts)

| Element | Hex |
|---------|-----|
| Primary | `#0F2D3D` |
| Accent | `#148F8B` |
| Highlight | `#00B894` |
| Solar | `#F9CA24` |
| Wind | `#4ECDC4` |
| Hydro | `#3A86FF` |
| Warning | `#E17055` |

In Tableau: **Format** → **Colors** → **Custom** → paste hex codes.

---

## Tips for portfolio polish

- Use **consistent fonts** (Tableau Book / Arial)
- Add **data source footnote**: "VoltScope curated dataset, 2015–2024"
- Enable **tooltips** with country, year, and renewable %
- Export dashboard as **image** for resume if embed isn't possible
