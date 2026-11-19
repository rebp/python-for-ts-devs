"""Tests for exercise 12-2 (Optional values).

Edit: ex12_2_parse_int.py::parse_int
"""

import pytest
from ex12_2_parse_int import parse_int


@pytest.mark.parametrize(
    "text, expected", [("42", 42), ("-7", -7), (" 8 ", 8), ("0", 0)]
)
def test_numbers(text, expected):
    assert parse_int(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "4.5", "12px"])
def test_not_numbers(text):
    assert parse_int(text) is None
