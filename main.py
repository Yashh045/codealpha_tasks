"""CLI entrypoint for the web scraping collection."""

from __future__ import annotations

import argparse
import runpy
from pathlib import Path
from typing import Dict, List

PROJECT_ROOT = Path(__file__).parent
SCRAPERS_DIR = PROJECT_ROOT / "scrapers"

CATEGORIES: Dict[str, str] = {
    "ecommerce": "E-commerce Websites",
    "job_boards": "Job Boards",
    "educational": "Educational Platforms",
    "social_media": "Social Media & Developer Platforms",
    "content": "Content & Media",
    "misc": "Miscellaneous",
}


def discover_scrapers() -> Dict[str, List[str]]:
    """Discover scraper files grouped by category."""
    discovered: Dict[str, List[str]] = {}
    for category in CATEGORIES:
        category_path = SCRAPERS_DIR / category
        if not category_path.exists():
            continue
        scripts = [
            file.stem
            for file in sorted(category_path.glob("*.py"))
            if file.name != "__init__.py"
        ]
        if scripts:
            discovered[category] = scripts
    return discovered


def list_scrapers() -> None:
    """Print all available scrapers."""
    discovered = discover_scrapers()

    print("=" * 64)
    print("Web Scraping Collection")
    print("=" * 64)
    for category, scripts in discovered.items():
        print(f"\n[{category}] {CATEGORIES[category]}")
        for script in scripts:
            print(f"  - {script}")

    print("\nUsage:")
    print("  python main.py --list")
    print("  python main.py --run content/imdb")
    print("=" * 64)


def run_scraper(target: str) -> None:
    """Execute a scraper file by category/name."""
    try:
        category, script_name = target.split("/", maxsplit=1)
    except ValueError as exc:
        raise ValueError("Use --run in format: <category>/<scraper_name>") from exc

    script_path = SCRAPERS_DIR / category / f"{script_name}.py"
    if not script_path.exists():
        raise FileNotFoundError(f"Scraper not found: {target}")

    runpy.run_path(str(script_path), run_name="__main__")


def parse_args() -> argparse.Namespace:
    """Parse command-line args."""
    parser = argparse.ArgumentParser(description="Web Scraping Collection CLI")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available scrapers.",
    )
    parser.add_argument(
        "--run",
        type=str,
        help="Run a scraper in format <category>/<scraper_name>.",
    )
    return parser.parse_args()


def main() -> None:
    """Entrypoint function."""
    args = parse_args()
    if args.list or not args.run:
        list_scrapers()
        return
    run_scraper(args.run)


if __name__ == "__main__":
    main()
