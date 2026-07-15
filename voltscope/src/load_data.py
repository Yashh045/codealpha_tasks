"""Data loading and preprocessing utilities."""

from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "global_energy_consumption.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "energy_enriched.csv"


def load_raw_data(path: Path | None = None) -> pd.DataFrame:
    """Load the raw energy consumption dataset."""
    data_path = path or RAW_DATA_PATH
    df = pd.read_csv(data_path)
    df["year"] = df["year"].astype(int)
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Enrich raw data with derived metrics for analysis."""
    enriched = df.copy()

    enriched["renewable_twh"] = (
        enriched["solar_twh"] + enriched["wind_twh"] + enriched["hydro_twh"]
    )
    enriched["per_capita_consumption_kwh"] = (
        enriched["total_consumption_twh"] * 1_000_000 / enriched["population_millions"]
    )
    enriched["co2_intensity"] = (
        enriched["co2_emissions_mt"] / enriched["total_consumption_twh"]
    )
    enriched["renewable_growth_index"] = enriched.groupby("country")[
        "renewable_share_pct"
    ].transform(lambda s: (s / s.iloc[0]) * 100)

    return enriched


def load_processed_data() -> pd.DataFrame:
    """Load raw data, preprocess, and optionally cache to disk."""
    df = load_raw_data()
    processed = preprocess(df)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    processed.to_csv(PROCESSED_DATA_PATH, index=False)

    return processed
