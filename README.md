# Web Scraping Collection

A practical Python scraping toolkit with category-wise scrapers, CSV exports, and a lightweight CLI to discover and run scripts quickly.

## Highlights

- Organized scraper library across e-commerce, jobs, education, social media, content, and misc sites.
- Fresh CLI workflow via `main.py` (`--list` and `--run`).
- Improved IMDb scraper with resilient selectors, argparse support, and cleaner output handling.
- Output-first design: each scraper writes CSV files to `output/`.

## Quick Start

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

Or with `pyproject.toml`:

```bash
pip install .
```

### 2) Discover available scrapers

```bash
python main.py --list
```

### 3) Run a scraper

```bash
python main.py --run content/imdb
```

Direct script execution still works:

```bash
python scrapers/content/imdb.py --limit 25 --output imdb_top25.csv
```

## Updated IMDb Scraper

The IMDb scraper (`scrapers/content/imdb.py`) now includes:

- safer HTTP requests (timeout + headers)
- CSS selector-based extraction for modern IMDb markup
- explicit model with `dataclass`
- argument flags for `--limit` and `--output`

Output example:

```csv
Rank,Name,Year,Rating,Link,Director
1,The Shawshank Redemption,1994,9.2,https://www.imdb.com/title/tt0111161/,Frank Darabont
```

## Project Structure

```text
web-scrapping-master/
├── main.py
├── pyproject.toml
├── requirements.txt
├── scrapers/
│   ├── content/
│   ├── ecommerce/
│   ├── educational/
│   ├── job_boards/
│   ├── misc/
│   ├── social_media/
│   └── utils/
└── output/
```

## Notes

- Respect `robots.txt`, site terms, and responsible request frequency.
- Website HTML changes over time; selectors may need occasional updates.
- Keep generated CSV files in `output/` for easier tracking and cleanup.

## License

MIT License. See `LICENSE`.
