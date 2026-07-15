"""Regional and cross-country comparison visualizations."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.style import COLORS, REGION_COLORS, add_source_note, apply_theme, save_figure


def plot_regional_renewable_boxplot(df: pd.DataFrame, output_dir: Path) -> Path:
    """Box plot: distribution of renewable share by region (2024 snapshot)."""
    apply_theme()

    latest = df[df["year"] == 2024].copy()
    region_order = (
        latest.groupby("region")["renewable_share_pct"]
        .median()
        .sort_values(ascending=False)
        .index.tolist()
    )

    fig, ax = plt.subplots(figsize=(11, 6))

    sns.boxplot(
        data=latest,
        x="region",
        y="renewable_share_pct",
        hue="region",
        order=region_order,
        palette=REGION_COLORS,
        width=0.55,
        ax=ax,
        fliersize=4,
        legend=False,
    )
    sns.stripplot(
        data=latest,
        x="region",
        y="renewable_share_pct",
        order=region_order,
        color=COLORS["primary"],
        size=6,
        alpha=0.7,
        ax=ax,
    )

    ax.set_title("Renewable Share Varies Widely Across Regions (2024)")
    ax.set_xlabel("")
    ax.set_ylabel("Renewable Share (%)")
    ax.set_xticks(range(len(region_order)))
    ax.set_xticklabels(region_order, rotation=25, ha="right")
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "03_regional_renewable_distribution.png", output_dir)


def plot_country_ranking_bar(df: pd.DataFrame, output_dir: Path) -> Path:
    """Horizontal bar chart: 2024 renewable leaders and laggards."""
    apply_theme()

    latest = df[df["year"] == 2024].sort_values("renewable_share_pct")

    fig, ax = plt.subplots(figsize=(10, 7))

    colors = [
        COLORS["highlight"] if v >= 50 else COLORS["accent"] if v >= 25 else COLORS["warning"]
        for v in latest["renewable_share_pct"]
    ]

    bars = ax.barh(latest["country"], latest["renewable_share_pct"], color=colors, edgecolor="white")

    for bar, val in zip(bars, latest["renewable_share_pct"]):
        ax.text(
            bar.get_width() + 1.2,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%",
            va="center",
            fontsize=9,
            color=COLORS["primary"],
        )

    ax.set_title("Country Ranking: Renewable Electricity Share in 2024")
    ax.set_xlabel("Renewable Share (%)")
    ax.set_xlim(0, 110)
    ax.axvline(50, color=COLORS["highlight"], linestyle="--", alpha=0.5)
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "04_country_renewable_ranking.png", output_dir)


def plot_gdp_vs_renewable_scatter(df: pd.DataFrame, output_dir: Path) -> Path:
    """Scatter plot: wealth vs. clean energy adoption (2024)."""
    apply_theme()

    latest = df[df["year"] == 2024].copy()

    fig, ax = plt.subplots(figsize=(11, 7))

    scatter = sns.scatterplot(
        data=latest,
        x="gdp_per_capita_usd",
        y="renewable_share_pct",
        hue="region",
        size="total_consumption_twh",
        sizes=(80, 600),
        palette=REGION_COLORS,
        alpha=0.85,
        edgecolor="white",
        linewidth=0.8,
        ax=ax,
    )

    for _, row in latest.iterrows():
        ax.annotate(
            row["country"],
            (row["gdp_per_capita_usd"], row["renewable_share_pct"]),
            textcoords="offset points",
            xytext=(6, 4),
            fontsize=8,
            color=COLORS["primary"],
        )

    ax.set_title("Wealth Alone Doesn't Predict Clean Power — Policy & Geography Matter")
    ax.set_xlabel("GDP per Capita (USD)")
    ax.set_ylabel("Renewable Share (%)")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.legend(title="Region", bbox_to_anchor=(1.02, 1), loc="upper left")
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "05_gdp_vs_renewable_scatter.png", output_dir)
