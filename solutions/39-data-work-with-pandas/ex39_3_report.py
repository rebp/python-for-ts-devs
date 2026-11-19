"""Reference solution for exercise 39-3 (Data work with pandas)."""

import pandas as pd


def revenue_by_region(csv_path: str) -> dict[str, float]:
    """Read an orders CSV (columns order_id, region, product, price, qty) and
    return the total revenue (price * qty) per region, highest first.

    For a file where EU sold 373.5, APAC 245 and US 199, the result is
    {"EU": 373.5, "APAC": 245.0, "US": 199.0}, in that order.

    Hint: pd.read_csv, then groupby("region")[...].sum(), sort_values and
    to_dict(). A Series turns into a dict with .to_dict().
    """
    orders = pd.read_csv(csv_path).assign(revenue=lambda df: df["price"] * df["qty"])
    totals = orders.groupby("region")["revenue"].sum().sort_values(ascending=False)
    return totals.to_dict()
