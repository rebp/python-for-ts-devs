"""Tests for exercise 18-1 (Exceptions).

Edit: ex18_1_safe_divide.py::safe_divide
"""

from ex18_1_safe_divide import safe_divide


def test_divides():
    assert safe_divide(10, 4) == 2.5


def test_divide_by_zero_returns_none():
    assert safe_divide(1, 0) is None


def test_zero_result_is_not_none():
    assert safe_divide(0, 5) == 0
    assert safe_divide(0, 5) is not None
