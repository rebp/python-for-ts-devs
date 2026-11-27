"""Reference solution for exercise 12.2-2."""

import polars as pl


def totals_by_category(frame: pl.LazyFrame) -> pl.LazyFrame:
    """Build, but do not execute, a grouped query."""
    return (
        frame.filter(pl.col("amount") > 0)
        .group_by("category")
        .agg(pl.col("amount").sum().alias("total"))
        .sort("category")
    )
