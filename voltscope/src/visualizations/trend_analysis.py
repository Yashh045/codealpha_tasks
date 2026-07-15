"""Global renewable energy adoption trends over time."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.style import COLORS, add_source_note, apply_theme, save_figure


def plot_renewable_trends(df: pd.DataFrame, output_dir: Path) -> Path:
    """Line chart: renewable share evolution for selected economies (2015–2024)."""
    apply_theme()

    focus_countries = [
        "United States",
        "Germany",
        "India",
        "China",
        "United Kingdom",
        "Australia",
        "Norway",
    ]
    subset = df[df["country"].isin(focus_countries)]

    fig, ax = plt.subplots(figsize=(12, 6.5))

    sns.lineplot(
        data=subset,
        x="year",
        y="renewable_share_pct",
        hue="country",
        marker="o",
        linewidth=2.2,
        markersize=5,
        ax=ax,
        palette="husl",
    )

    ax.set_title(
        "Renewable Electricity Share Is Accelerating — But Progress Is Uneven",
        pad=16,
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Renewable Share of Electricity (%)")
    ax.set_xticks(range(2015, 2025))
    ax.axhline(50, color=COLORS["highlight"], linestyle="--", alpha=0.6, linewidth=1.2)
    ax.text(2015.2, 51.5, "50% benchmark", color=COLORS["highlight"], fontsize=9)

    ax.annotate(
        "Norway leads at ~99%",
        xy=(2024, 99),
        xytext=(2020, 88),
        arrowprops=dict(arrowstyle="->", color=COLORS["neutral"]),
        fontsize=9,
        color=COLORS["primary"],
    )
    ax.annotate(
        "India: fastest large-economy climb",
        xy=(2024, 31),
        xytext=(2018, 42),
        arrowprops=dict(arrowstyle="->", color=COLORS["warning"]),
        fontsize=9,
        color=COLORS["primary"],
    )

    ax.legend(title="Country", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True)
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "01_renewable_share_trends.png", output_dir)


def plot_co2_decline(df: pd.DataFrame, output_dir: Path) -> Path:
    """Area chart: CO₂ emissions trajectory for top emitters."""
    apply_theme()

    top_emitters = (
        df[df["year"] == 2024]
        .nlargest(5, "co2_emissions_mt")["country"]
        .tolist()
    )
    subset = df[df["country"].isin(top_emitters)]

    fig, ax = plt.subplots(figsize=(11, 6))

    for country in top_emitters:
        country_data = subset[subset["country"] == country].sort_values("year")
        ax.fill_between(
            country_data["year"],
            country_data["co2_emissions_mt"],
            alpha=0.15,
        )
        ax.plot(
            country_data["year"],
            country_data["co2_emissions_mt"],
            label=country,
            linewidth=2.5,
            marker="s",
            markersize=4,
        )

    ax.set_title("Power Sector CO₂ Emissions — Diverging Paths Among Major Economies")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂ Emissions (Million Tonnes)")
    ax.set_xticks(range(2015, 2025))
    ax.legend(title="Country", loc="upper right")
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "02_co2_emissions_trends.png", output_dir)
