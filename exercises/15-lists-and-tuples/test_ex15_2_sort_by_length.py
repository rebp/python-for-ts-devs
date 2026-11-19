"""Tests for exercise 15-2 (Lists and tuples).

Edit: ex15_2_sort_by_length.py::sort_by_length
"""

from ex15_2_sort_by_length import sort_by_length, sort_by_length_desc

WORDS = ["kiwi", "banana", "fig", "apple"]


def test_shortest_first():
    assert sort_by_length(WORDS) == ["fig", "kiwi", "apple", "banana"]


def test_longest_first():
    assert sort_by_length_desc(WORDS) == ["banana", "apple", "kiwi", "fig"]


def test_input_is_not_sorted_in_place():
    words = list(WORDS)
    sort_by_length(words)
    sort_by_length_desc(words)
    assert words == WORDS
