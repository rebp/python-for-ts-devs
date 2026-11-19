"""Tests for exercise 32-3 (Dates and times).

Edit: ex32_3_business_days.py::add_business_days
"""

from datetime import date

import pytest
from ex32_3_business_days import add_business_days

FRIDAY = date(2026, 11, 20)


def test_friday_plus_one_is_monday():
    assert add_business_days(FRIDAY, 1) == date(2026, 11, 23)


def test_a_full_week():
    assert add_business_days(FRIDAY, 5) == date(2026, 11, 27)


def test_midweek():
    assert add_business_days(date(2026, 11, 17), 2) == date(2026, 11, 19)


def test_zero_days():
    assert add_business_days(FRIDAY, 0) == FRIDAY


def test_starting_on_saturday():
    assert add_business_days(date(2026, 11, 21), 1) == date(2026, 11, 23)


def test_across_a_month_end():
    assert add_business_days(date(2026, 11, 27), 3) == date(2026, 12, 2)


def test_negative_days():
    with pytest.raises(ValueError):
        add_business_days(FRIDAY, -1)
