"""Reference solution for exercise 31-1 (Files and data formats)."""

import json
from pathlib import Path


def filter_expensive(src: str, dst: str) -> None:
    """Read a JSON list of products (each with name and price) and write the ones
    over 20 to expensive.json.

    filter_expensive(src, dst) reads the products from the file src and writes
    the ones with a price over 20 (not equal) to the file dst, as JSON.
    """
    products = json.loads(Path(src).read_text(encoding="utf-8"))
    expensive = [p for p in products if p["price"] > 20]
    Path(dst).write_text(json.dumps(expensive, indent=2), encoding="utf-8")
