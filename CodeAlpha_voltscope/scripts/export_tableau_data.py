"""
Export processed dataset in Tableau-friendly format.

Usage:
    python scripts/export_tableau_data.py
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.load_data import load_processed_data

OUTPUT_DIR = PROJECT_ROOT / "tableau" / "data"


def main() -> None:
    df = load_processed_data()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Full enriched dataset
    full_path = OUTPUT_DIR / "voltscope_energy_full.csv"
    df.to_csv(full_path, index=False)

    # Latest year snapshot for donut/bar dashboards
    snapshot = df[df["year"] == df["year"].max()].copy()
    snapshot_path = OUTPUT_DIR / "voltscope_energy_2024_snapshot.csv"
    snapshot.to_csv(snapshot_path, index=False)

    # Yearly global aggregates for trend charts
    yearly = (
        df.groupby(["year", "region"])
        .agg(
            total_consumption_twh=("total_consumption_twh", "sum"),
            renewable_share_pct=("renewable_share_pct", "mean"),
            solar_twh=("solar_twh", "sum"),
            wind_twh=("wind_twh", "sum"),
            hydro_twh=("hydro_twh", "sum"),
            co2_emissions_mt=("co2_emissions_mt", "sum"),
        )
        .reset_index()
    )
    yearly_path = OUTPUT_DIR / "voltscope_yearly_regional.csv"
    yearly.to_csv(yearly_path, index=False)

    print(f"Exported 3 Tableau-ready files to {OUTPUT_DIR}:")
    print(f"  - {full_path.name} ({len(df)} rows)")
    print(f"  - {snapshot_path.name} ({len(snapshot)} rows)")
    print(f"  - {yearly_path.name} ({len(yearly)} rows)")


if __name__ == "__main__":
    main()
