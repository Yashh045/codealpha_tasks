"""
VoltScope Analytics — generate all portfolio visualizations.

Usage:
    python main.py
"""

from pathlib import Path

from src.load_data import load_processed_data
from src.visualizations.correlation_analysis import plot_correlation_heatmap
from src.visualizations.dashboard import plot_executive_dashboard
from src.visualizations.regional_comparison import (
    plot_country_ranking_bar,
    plot_gdp_vs_renewable_scatter,
    plot_regional_renewable_boxplot,
)
from src.visualizations.renewable_mix import plot_energy_composition_donut, plot_renewable_mix_stacked
from src.visualizations.trend_analysis import plot_co2_decline, plot_renewable_trends

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs" / "figures"


def main() -> None:
    print("VoltScope Analytics — Loading and preprocessing data...")
    df = load_processed_data()
    print(f"  -> {len(df)} records across {df['country'].nunique()} countries")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generators = [
        ("Renewable share trends", lambda: plot_renewable_trends(df, OUTPUT_DIR)),
        ("CO2 emissions trends", lambda: plot_co2_decline(df, OUTPUT_DIR)),
        ("Regional distribution", lambda: plot_regional_renewable_boxplot(df, OUTPUT_DIR)),
        ("Country ranking", lambda: plot_country_ranking_bar(df, OUTPUT_DIR)),
        ("GDP vs renewable scatter", lambda: plot_gdp_vs_renewable_scatter(df, OUTPUT_DIR)),
        ("Correlation heatmap", lambda: plot_correlation_heatmap(df, OUTPUT_DIR)),
        ("Renewable mix stacked area", lambda: plot_renewable_mix_stacked(df, OUTPUT_DIR)),
        ("Germany energy mix donut", lambda: plot_energy_composition_donut(df, OUTPUT_DIR, "Germany")),
        ("India energy mix donut", lambda: plot_energy_composition_donut(df, OUTPUT_DIR, "India")),
        ("Executive dashboard", lambda: plot_executive_dashboard(df, OUTPUT_DIR)),
    ]

    print("\nGenerating visualizations...")
    for name, gen in generators:
        path = gen()
        print(f"  [ok] {name}: {path.name}")

    print(f"\nDone! {len(generators)} figures saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
