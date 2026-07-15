"""Correlation and relationship heatmaps."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.style import add_source_note, apply_theme, save_figure


def plot_correlation_heatmap(df: pd.DataFrame, output_dir: Path) -> Path:
    """Heatmap: relationships between key energy and economic indicators."""
    apply_theme()

    numeric_cols = [
        "total_consumption_twh",
        "renewable_share_pct",
        "solar_twh",
        "wind_twh",
        "hydro_twh",
        "co2_emissions_mt",
        "gdp_per_capita_usd",
        "co2_intensity",
        "per_capita_consumption_kwh",
    ]

    labels = {
        "total_consumption_twh": "Total Consumption",
        "renewable_share_pct": "Renewable %",
        "solar_twh": "Solar",
        "wind_twh": "Wind",
        "hydro_twh": "Hydro",
        "co2_emissions_mt": "CO₂ Emissions",
        "gdp_per_capita_usd": "GDP/Capita",
        "co2_intensity": "CO₂ Intensity",
        "per_capita_consumption_kwh": "Per-Capita Use",
    }

    corr = df[numeric_cols].corr()
    corr = corr.rename(index=labels, columns=labels)

    fig, ax = plt.subplots(figsize=(10, 8))

    mask = None
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="RdYlGn",
        center=0,
        square=True,
        linewidths=0.8,
        cbar_kws={"shrink": 0.8, "label": "Pearson Correlation"},
        ax=ax,
        mask=mask,
    )

    ax.set_title("What Moves Together? Correlations Across Energy Metrics")
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "06_correlation_heatmap.png", output_dir)
