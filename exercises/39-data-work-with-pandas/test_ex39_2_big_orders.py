"""Tests for exercise 39-2 (Data work with pandas).

Edit: ex39_2_big_orders.py::big_orders
"""

import pandas as pd
import pytest
from ex39_2_big_orders import big_orders


@pytest.fixture
def orders():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "region": ["EU", "US", "EU", "APAC", "US"],
            "qty": [3, 1, 4, 10, 2],
        }
    )


def ids(frame):
    return frame["order_id"].tolist()


def test_filters_on_both_conditions(orders):
    assert ids(big_orders(orders, "EU", 3)) == [1, 3]


def test_min_qty_is_inclusive(orders):
    assert ids(big_orders(orders, "EU", 4)) == [3]


def test_other_region(orders):
    assert ids(big_orders(orders, "US", 2)) == [5]


def test_no_matches_gives_an_empty_frame(orders):
    result = big_orders(orders, "US", 5)
    assert isinstance(result, pd.DataFrame)
    assert result.empty
