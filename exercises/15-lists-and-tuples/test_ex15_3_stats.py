"""Tests for exercise 15-3 (Lists and tuples).

Edit: ex15_3_stats.py::stats
"""

from ex15_3_stats import stats


def test_returns_a_tuple():
    assert stats([4, 8, 15, 16, 23, 42]) == (4, 42, 18.0)
    assert type(stats([1])) is tuple


def test_unpacking():
    low, high, avg = stats([3, 1, 2])
    assert (low, high, avg) == (1, 3, 2.0)
