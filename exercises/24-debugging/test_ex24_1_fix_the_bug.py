"""Tests for exercise 24-1 (Debugging).

Edit: ex24_1_fix_the_bug.py::order_total
"""

from ex24_1_fix_the_bug import order_total, to_cents


def test_order_with_decimal_prices():
    assert order_total("Lamp,24.50,2\nDesk,150,1") == 19900


def test_whole_prices_still_work():
    assert order_total("Desk,150,2") == 30000


def test_cents_are_exact():
    assert to_cents("0.10") == 10
    assert to_cents("19.99") == 1999
    assert isinstance(to_cents("19.99"), int)


def test_empty_order():
    assert order_total("") == 0
