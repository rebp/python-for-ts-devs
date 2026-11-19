"""Tests for exercise 07-1 (Truthiness, None and equality).

Edit: ex07_1_describe.py::describe
"""

import pytest
from ex07_1_describe import describe


@pytest.mark.parametrize("value", [0, 0.0, "", [], {}, set(), None, False])
def test_falsy_values_are_empty(value):
    assert describe(value) == "empty"


@pytest.mark.parametrize("value", [[0], "0", " ", 1, -1, {"a": None}, True])
def test_truthy_values_have_a_value(value):
    assert describe(value) == "has value"
