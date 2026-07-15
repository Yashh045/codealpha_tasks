"""Renewable energy mix and composition charts."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.style import COLORS, add_source_note, apply_theme, save_figure


def plot_renewable_mix_stacked(df: pd.DataFrame, output_dir: Path) -> Path:
    """Stacked area chart: solar, wind, hydro contribution over time (global aggregate)."""
    apply_theme()

    yearly = (
        df.groupby("year")[["solar_twh", "wind_twh", "hydro_twh"]]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(
        yearly["year"],
        yearly["solar_twh"],
        yearly["wind_twh"],
        yearly["hydro_twh"],
        labels=["Solar", "Wind", "Hydro"],
        colors=[COLORS["solar"], COLORS["wind"], COLORS["hydro"]],
        alpha=0.85,
    )

    ax.set_title("Global Renewable Generation Mix — Wind & Solar Are Driving Growth")
    ax.set_xlabel("Year")
    ax.set_ylabel("Generation (TWh)")
    ax.set_xticks(range(2015, 2025))
    ax.legend(loc="upper left", title="Source")
    add_source_note(ax)
    fig.tight_layout()

    return save_figure(fig, "07_renewable_mix_stacked.png", output_dir)


def plot_energy_composition_donut(df: pd.DataFrame, output_dir: Path, country: str = "Germany") -> Path:
    """Donut chart: energy source breakdown for a single country in 2024."""
    apply_theme()

    row = df[(df["country"] == country) & (df["year"] == 2024)].iloc[0]

    sources = ["Solar", "Wind", "Hydro", "Fossil & Other"]
    values = [
        row["solar_twh"],
        row["wind_twh"],
        row["hydro_twh"],
        row["fossil_twh"],
    ]
    colors = [COLORS["solar"], COLORS["wind"], COLORS["hydro"], COLORS["fossil"]]

    fig, ax = plt.subplots(figsize=(8, 8))

    wedges, texts, autotexts = ax.pie(
        values,
        labels=sources,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.78,
        wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2),
        textprops=dict(color=COLORS["primary"], fontsize=10),
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.text(
        0,
        0,
        f"{row['renewable_share_pct']:.0f}%\nRenewable",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=COLORS["primary"],
    )

    ax.set_title(f"{country} Electricity Mix — 2024", pad=20)
    add_source_note(ax)
    fig.tight_layout()

    slug = country.lower().replace(" ", "_")
    return save_figure(fig, f"08_energy_mix_donut_{slug}.png", output_dir)
