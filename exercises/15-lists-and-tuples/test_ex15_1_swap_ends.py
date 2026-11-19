"""Tests for exercise 15-1 (Lists and tuples).

Edit: ex15_1_swap_ends.py::swap_ends
"""

from ex15_1_swap_ends import swap_ends


def test_swaps_first_and_last():
    assert swap_ends([1, 2, 3, 4]) == [4, 2, 3, 1]
    assert swap_ends(["a", "b"]) == ["b", "a"]


def test_input_does_not_change():
    items = [1, 2, 3]
    swap_ends(items)
    assert items == [1, 2, 3]


def test_short_lists_return_a_copy():
    one = [5]
    result = swap_ends(one)
    assert result == [5]
    assert result is not one
    assert swap_ends([]) == []
