"""Executive dashboard — multi-panel summary for decision-makers."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import seaborn as sns

from src.style import COLORS, REGION_COLORS, add_source_note, apply_theme, save_figure


def _kpi_card(ax, title: str, value: str, subtitle: str, color: str) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(
        plt.Rectangle(
            (0.02, 0.08),
            0.96,
            0.84,
            facecolor="white",
            edgecolor=color,
            linewidth=2.5,
            transform=ax.transAxes,
            clip_on=False,
        )
    )
    ax.text(0.5, 0.72, value, ha="center", va="center", fontsize=26, fontweight="bold", color=color)
    ax.text(0.5, 0.48, title, ha="center", va="center", fontsize=11, color=COLORS["primary"])
    ax.text(0.5, 0.28, subtitle, ha="center", va="center", fontsize=9, color=COLORS["neutral"])


def plot_executive_dashboard(df: pd.DataFrame, output_dir: Path) -> Path:
    """Four-panel dashboard with KPIs, trends, and regional snapshot."""
    apply_theme()

    latest = df[df["year"] == 2024]
    prev = df[df["year"] == 2015]

    avg_renewable_2024 = latest["renewable_share_pct"].mean()
    avg_renewable_2015 = prev["renewable_share_pct"].mean()
    renewable_delta = avg_renewable_2024 - avg_renewable_2015

    total_co2_2024 = latest["co2_emissions_mt"].sum()
    total_co2_2015 = prev["co2_emissions_mt"].sum()
    co2_change_pct = ((total_co2_2024 - total_co2_2015) / total_co2_2015) * 100

    solar_growth = (
        latest["solar_twh"].sum() / prev["solar_twh"].sum() - 1
    ) * 100

    fig = plt.figure(figsize=(16, 10))
    gs = gridspec.GridSpec(3, 4, figure=fig, height_ratios=[0.9, 1.2, 1.2], hspace=0.45, wspace=0.35)

    # KPI row
    _kpi_card(
        fig.add_subplot(gs[0, 0]),
        "Avg Renewable Share",
        f"{avg_renewable_2024:.1f}%",
        f"+{renewable_delta:.1f} pp since 2015",
        COLORS["highlight"],
    )
    _kpi_card(
        fig.add_subplot(gs[0, 1]),
        "Global CO₂ (Power)",
        f"{total_co2_2024:,.0f} Mt",
        f"{co2_change_pct:+.1f}% vs 2015",
        COLORS["danger"] if co2_change_pct > 0 else COLORS["highlight"],
    )
    _kpi_card(
        fig.add_subplot(gs[0, 2]),
        "Solar Growth",
        f"+{solar_growth:.0f}%",
        "Aggregate generation 2015→2024",
        COLORS["solar"],
    )
    _kpi_card(
        fig.add_subplot(gs[0, 3]),
        "Countries Tracked",
        f"{latest['country'].nunique()}",
        f"{latest['region'].nunique()} regions",
        COLORS["accent"],
    )

    # Trend panel
    ax_trend = fig.add_subplot(gs[1, :2])
    yearly_avg = df.groupby("year")["renewable_share_pct"].mean().reset_index()
    sns.lineplot(data=yearly_avg, x="year", y="renewable_share_pct", marker="o", linewidth=3, color=COLORS["accent"], ax=ax_trend)
    ax_trend.fill_between(yearly_avg["year"], yearly_avg["renewable_share_pct"], alpha=0.2, color=COLORS["accent"])
    ax_trend.set_title("Global Average Renewable Share")
    ax_trend.set_xlabel("Year")
    ax_trend.set_ylabel("%")

    # Regional bar
    ax_region = fig.add_subplot(gs[1, 2:])
    regional = latest.groupby("region")["renewable_share_pct"].mean().sort_values()
    regional.plot(kind="barh", ax=ax_region, color=[REGION_COLORS.get(r, COLORS["neutral"]) for r in regional.index])
    ax_region.set_title("Regional Averages (2024)")
    ax_region.set_xlabel("Renewable %")

    # Top movers
    ax_movers = fig.add_subplot(gs[2, :2])
    movers = (
        df[df["year"].isin([2015, 2024])]
        .pivot_table(index="country", columns="year", values="renewable_share_pct")
        .dropna()
    )
    movers["change"] = movers[2024] - movers[2015]
    movers = movers.sort_values("change", ascending=True).tail(8)
    movers["change"].plot(kind="barh", ax=ax_movers, color=COLORS["highlight"])
    ax_movers.set_title("Biggest Renewable Share Gains (2015–2024)")
    ax_movers.set_xlabel("Percentage Point Change")
    ax_movers.set_ylabel("")

    # CO2 intensity
    ax_intensity = fig.add_subplot(gs[2, 2:])
    intensity_latest = latest.nsmallest(8, "co2_intensity")
    sns.barplot(
        data=intensity_latest,
        y="country",
        x="co2_intensity",
        hue="country",
        palette="Blues_r",
        ax=ax_intensity,
        legend=False,
    )
    ax_intensity.set_title("Lowest CO₂ Intensity — 2024 Leaders")
    ax_intensity.set_xlabel("Mt CO₂ per TWh")
    ax_intensity.set_ylabel("")

    fig.suptitle(
        "VoltScope Executive Dashboard — Global Energy Transition Snapshot",
        fontsize=18,
        fontweight="bold",
        y=0.98,
        color=COLORS["primary"],
    )

    fig.text(
        0.5,
        0.01,
        "Source: VoltScope curated dataset (2015–2024)  |  Built with Matplotlib & Seaborn",
        ha="center",
        fontsize=8,
        color=COLORS["neutral"],
        style="italic",
    )

    return save_figure(fig, "09_executive_dashboard.png", output_dir)
