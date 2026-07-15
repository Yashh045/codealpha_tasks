"""VoltScope Analytics — shared visualization styling."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

# Cohesive portfolio palette — deep teal-navy with warm energy accents
COLORS = {
    "primary": "#0F2D3D",
    "secondary": "#1A5276",
    "accent": "#148F8B",
    "highlight": "#00B894",
    "warning": "#E17055",
    "danger": "#D63031",
    "neutral": "#636E72",
    "light": "#F5F6FA",
    "solar": "#F9CA24",
    "wind": "#4ECDC4",
    "hydro": "#3A86FF",
    "fossil": "#636E72",
}

PALETTE = [
    COLORS["primary"],
    COLORS["accent"],
    COLORS["highlight"],
    COLORS["warning"],
    COLORS["danger"],
    COLORS["secondary"],
    COLORS["solar"],
    COLORS["wind"],
]

REGION_COLORS = {
    "North America": "#0F2D3D",
    "Europe": "#1A5276",
    "Asia": "#00B894",
    "South America": "#F9CA24",
    "Africa": "#E17055",
    "Oceania": "#4ECDC4",
    "Middle East": "#9B59B6",
}


def apply_theme() -> None:
    """Apply consistent matplotlib/seaborn styling across all figures."""
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        font_scale=1.05,
        rc={
            "figure.facecolor": COLORS["light"],
            "axes.facecolor": "white",
            "axes.edgecolor": COLORS["neutral"],
            "axes.labelcolor": COLORS["primary"],
            "axes.titleweight": "bold",
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "xtick.color": COLORS["primary"],
            "ytick.color": COLORS["primary"],
            "grid.alpha": 0.35,
            "legend.framealpha": 0.92,
            "font.family": "sans-serif",
            "font.sans-serif": ["Segoe UI", "Helvetica Neue", "Arial", "DejaVu Sans"],
        },
    )


def save_figure(fig: plt.Figure, filename: str, output_dir: Path) -> Path:
    """Save figure at publication-ready resolution."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / filename
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return path


def add_source_note(ax: plt.Axes, note: str = "Source: VoltScope curated dataset (2015–2024)") -> None:
    """Add a subtle data source attribution."""
    ax.text(
        0.0,
        -0.14,
        note,
        transform=ax.transAxes,
        fontsize=8,
        color=COLORS["neutral"],
        style="italic",
    )
