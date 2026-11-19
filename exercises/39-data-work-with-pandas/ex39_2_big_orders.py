"""Lesson 39 · Data work with pandas · exercise 2.

Check your work with: uv run course.py
"""

import pandas as pd


def big_orders(orders: pd.DataFrame, region: str, min_qty: int) -> pd.DataFrame:
    """Return the rows of orders in `region` with a qty of at least `min_qty`.

    big_orders(orders, "EU", 3) is the pandas version of
    orders.filter(o => o.region === "EU" && o.qty >= 3).

    Build a boolean mask for each condition and combine them with &, with
    parentheses around each comparison: orders[(...) & (...)]. Python's `and`
    doesn't work on whole columns.
    """
    raise NotImplementedError("Your code here")
