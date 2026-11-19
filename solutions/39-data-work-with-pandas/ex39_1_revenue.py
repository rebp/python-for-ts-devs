"""Reference solution for exercise 39-1 (Data work with pandas)."""

import pandas as pd


def add_revenue(orders: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of orders with a new revenue column: price * qty.

    The DataFrame passed in must not change, so don't assign to
    orders["revenue"]. Use orders.assign(revenue=...), which returns a new
    DataFrame, like {...obj, revenue} in TypeScript.

    Don't loop over the rows: orders["price"] * orders["qty"] multiplies the
    whole columns at once.
    """
    return orders.assign(revenue=orders["price"] * orders["qty"])
