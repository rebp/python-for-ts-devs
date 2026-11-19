"""Tests for exercise 39-1 (Data work with pandas).

Edit: ex39_1_revenue.py::add_revenue
"""

import ast

import pandas as pd
import pytest
from ex39_1_revenue import add_revenue

from course_helpers import uses_node


@pytest.fixture
def orders():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "price": [24.5, 150.0, 75.0],
            "qty": [3, 1, 4],
        }
    )


def test_adds_revenue(orders):
    result = add_revenue(orders)
    assert result["revenue"].tolist() == [73.5, 150.0, 300.0]
    assert result["order_id"].tolist() == [1, 2, 3]


def test_does_not_change_the_input(orders):
    add_revenue(orders)
    assert "revenue" not in orders.columns


def test_no_loops():
    assert not uses_node(add_revenue, ast.For), "use column arithmetic, not a for loop"
