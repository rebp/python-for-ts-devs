"""Tests for exercise 39-3 (Data work with pandas).

Edit: ex39_3_report.py::revenue_by_region
"""

import pytest
from ex39_3_report import revenue_by_region

CSV = """order_id,region,product,price,qty
1,EU,Lamp,24.5,3
2,US,Desk,150,1
3,EU,Chair,75,4
4,APAC,Lamp,24.5,10
5,US,Lamp,24.5,2
"""


@pytest.fixture
def csv_path(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(CSV, encoding="utf-8")
    return str(path)


def test_totals_per_region(csv_path):
    result = revenue_by_region(csv_path)
    assert result == pytest.approx({"EU": 373.5, "APAC": 245.0, "US": 199.0})


def test_highest_first(csv_path):
    assert list(revenue_by_region(csv_path)) == ["EU", "APAC", "US"]


def test_returns_a_plain_dict(csv_path):
    assert type(revenue_by_region(csv_path)) is dict
