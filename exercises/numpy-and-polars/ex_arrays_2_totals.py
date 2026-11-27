"""Lesson 12.2 · NumPy and Polars · exercise 2.

Check your work with: uv run course.py 12.2-2
"""

import polars as pl


def totals_by_category(frame: pl.LazyFrame) -> pl.LazyFrame:
    """Return a lazy query summing positive amounts by category.

    Ignore zero, negative and null amounts. Return columns ``category`` and
    ``total``, sorted by category. Do not collect inside the function.
    """
    raise NotImplementedError("Your code here")
