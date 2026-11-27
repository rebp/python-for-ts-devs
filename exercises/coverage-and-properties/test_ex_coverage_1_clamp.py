"""Tests for exercise 6.3-1.

Edit: ex_coverage_1_clamp.py::clamp
"""

import pytest
from ex_coverage_1_clamp import clamp
from hypothesis import given, settings
from hypothesis import strategies as st


def test_examples_that_miss_the_bug() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0


@settings(derandomize=True, database=None, deadline=None)
@given(value=st.integers(), lower=st.integers(), width=st.integers(0, 100))
def test_result_stays_in_range(value: int, lower: int, width: int) -> None:
    upper = lower + width
    result = clamp(value, lower, upper)
    assert lower <= result <= upper
    if lower <= value <= upper:
        assert result == value


def test_reversed_bounds_are_rejected() -> None:
    with pytest.raises(ValueError):
        clamp(1, 3, 2)
