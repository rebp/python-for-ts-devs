"""Lesson 39 · Data work with pandas · exercise 3.

Check your work with: uv run course.py
"""


def revenue_by_region(csv_path: str) -> dict[str, float]:
    """Read an orders CSV (columns order_id, region, product, price, qty) and
    return the total revenue (price * qty) per region, highest first.

    For a file where EU sold 373.5, APAC 245 and US 199, the result is
    {"EU": 373.5, "APAC": 245.0, "US": 199.0}, in that order.

    Hint: pd.read_csv, then groupby("region")[...].sum(), sort_values and
    to_dict(). A Series turns into a dict with .to_dict().
    """
    raise NotImplementedError("Your code here")
