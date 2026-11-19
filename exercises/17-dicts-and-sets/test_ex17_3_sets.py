"""Tests for exercise 17-3 (Dicts and sets).

Edit: ex17_3_sets.py::compare_weeks
"""

from ex17_3_sets import compare_weeks


def test_compare_weeks():
    both, only_first, either = compare_weeks([1, 2, 3, 5, 8], [2, 3, 4, 8, 9])
    assert both == {2, 3, 8}
    assert only_first == {1, 5}
    assert either == {1, 2, 3, 4, 5, 8, 9}


def test_returns_sets_without_duplicates():
    both, only_first, either = compare_weeks([1, 1, 2], [2, 2])
    assert (both, only_first, either) == ({2}, {1}, {1, 2})
    assert all(type(s) is set for s in (both, only_first, either))
