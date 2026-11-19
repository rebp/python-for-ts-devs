"""Tests for exercise 17-2 (Dicts and sets).

Edit: ex17_2_group.py::group_by_first_letter
"""

from ex17_2_group import group_by_first_letter


def test_groups():
    result = group_by_first_letter(
        ["apple", "avocado", "banana", "blueberry", "cherry"]
    )
    assert result == {
        "a": ["apple", "avocado"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"],
    }


def test_returns_a_plain_dict():
    assert type(group_by_first_letter(["kiwi"])) is dict


def test_empty_list():
    assert group_by_first_letter([]) == {}
