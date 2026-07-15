# The Energy Transition in Numbers

**A data story by VoltScope Analytics**

---

## The Question

The world committed to accelerating the shift away from fossil-fueled electricity. But *who* is actually moving, *how fast*, and *what should policymakers prioritize next*?

This analysis tracks **12 economies across 7 regions** from 2015 to 2024 — transforming raw energy consumption data into visuals that support real decisions.

---

## Chapter 1: The Pace of Change

![Renewable Share Trends](outputs/figures/01_renewable_share_trends.png)

**Key insight:** Renewable electricity share is climbing almost everywhere, but the starting line and speed differ dramatically.

- **Norway** remains the benchmark at ~99% — hydro-dominated from the start.
- **Germany** crossed 50% in 2023, driven by deliberate wind and solar policy.
- **India** shows the steepest climb among large economies — from 16% to 31% in a decade.
- The **United States** improved steadily but still trails European leaders.

> **Decision takeaway:** Universal targets mask uneven progress. Incentive design should be region-specific.

---

## Chapter 2: Emissions Aren't Falling Everywhere

![CO₂ Emissions Trends](outputs/figures/02_co2_emissions_trends.png)

**Key insight:** Lower renewable share doesn't always mean rising emissions — total demand matters.

China's emissions peaked and began declining despite massive absolute consumption, as renewables scaled. India's emissions rose with electrification and industrial growth, even as clean share improved.

> **Decision takeaway:** Track both **carbon intensity** and **absolute emissions** when evaluating policy impact.

---

## Chapter 3: Regional Divides

![Regional Distribution](outputs/figures/03_regional_renewable_distribution.png)

Europe and South America lead the median renewable share. The Middle East and Africa remain at the lower end — but Africa's trajectory (South Africa: 8.5% → 18.5%) shows policy can move the needle.

![Country Ranking](outputs/figures/04_country_renewable_ranking.png)

The gap between Norway (99%) and UAE (15%) in 2024 illustrates how geography, policy, and fossil reliance interact.

---

## Chapter 4: Wealth Isn't Destiny

![GDP vs Renewable](outputs/figures/05_gdp_vs_renewable_scatter.png)

Higher GDP per capita does **not** guarantee a greener grid. Brazil outperforms many wealthier nations thanks to hydro resources. Germany and the UK punch above their economic weight through policy.

Bubble size = total electricity consumption — showing that the largest grids (China, US) carry the highest decarbonization leverage.

> **Decision takeaway:** Investment should follow **impact potential** (TWh shifted), not just per-capita income.

---

## Chapter 5: What Correlates — and What Doesn't

![Correlation Heatmap](outputs/figures/06_correlation_heatmap.png)

- Solar and wind growth correlate positively with rising renewable share.
- CO₂ intensity inversely tracks renewable adoption.
- GDP per capita has a **weak** correlation with renewable share — reinforcing that policy beats prosperity alone.

---

## Chapter 6: The Mix Matters

![Renewable Mix](outputs/figures/07_renewable_mix_stacked.png)

Globally, **wind and solar** are the growth engines. Hydro provides a stable base but isn't expanding at the same rate.

![Germany Donut](outputs/figures/08_energy_mix_donut_germany.png)

Germany's 2024 mix — over half renewable — shows how wind has become the backbone of a diversified clean portfolio.

![India Donut](outputs/figures/08_energy_mix_donut_india.png)

India's mix is still fossil-heavy, but solar is scaling fast — a signal of where the next decade of growth will come from.

---

## Executive Summary Dashboard

![Dashboard](outputs/figures/09_executive_dashboard.png)

| Metric | 2024 Value | Trend |
|--------|-----------|-------|
| Avg renewable share (12 countries) | ~38% | +15 pp since 2015 |
| Solar generation growth | +350% aggregate | Fastest-growing source |
| Lowest CO₂ intensity | Norway, Brazil | Hydro advantage |

---

## Recommendations for Decision-Makers

1. **Prioritize solar + wind deployment** in high-consumption grids (China, US, India) for maximum absolute impact.
2. **Pair renewable targets with demand-side strategy** — growing economies can green the share while emissions still rise.
3. **Learn from regional leaders** — Germany's policy model and Brazil's hydro foundation offer different playbooks.
4. **Track intensity metrics**, not just percentage targets, when reporting progress to stakeholders.

---

*Built with Python, Pandas, Matplotlib, and Seaborn. Data: VoltScope curated global energy dataset (2015–2024).*
