"""Tests for exercise 02-2 (Variables and types).

Edit: ex02_2_convert.py::add_eight
"""

from ex02_2_convert import add_eight


def test_adds_eight_to_the_number():
    result = add_eight("42")
    assert result == 50
    assert type(result) is int


def test_negative_numbers():
    assert add_eight("-8") == 0
