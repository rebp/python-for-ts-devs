"""Tests for exercise 02-1 (Variables and types).

Edit: ex02_1_total.py::order_line
"""

from ex02_1_total import order_line


def test_desk_lamp():
    assert order_line("Desk lamp", 24.5, 3) == "Desk lamp: 73.50"


def test_always_two_decimals():
    assert order_line("Chair", 10, 1) == "Chair: 10.00"
    assert order_line("Pen", 1.5, 3) == "Pen: 4.50"


def test_rounds_to_two_decimals():
    assert order_line("Bolt", 0.333, 3) == "Bolt: 1.00"
