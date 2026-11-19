"""Tests for exercise 05-3 (Names and objects).

Edit: ex05_3_equality.py::compare
"""

from ex05_3_equality import compare


def test_two_separate_lists_with_the_same_contents():
    assert compare([1, 2], [1, 2]) == (True, False)


def test_the_same_list_twice():
    x = [1, 2]
    y = x
    assert compare(x, y) == (True, True)


def test_different_contents():
    assert compare([1, 2], [2, 1]) == (False, False)
