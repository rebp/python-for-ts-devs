"""Tests for exercise 14-1 (Typing in depth).

Edit: ex14_1_group_by.py::group_by
"""

from ex14_1_group_by import group_by

from course_helpers import type_check_strict

MODULE = "ex14_1_group_by"

USAGE = """
from typing import assert_type

from ex14_1_group_by import group_by

by_letter = group_by(["apple", "banana"], lambda word: word[0])
assert_type(by_letter, dict[str, list[str]])

by_length = group_by(["a", "bb"], len)
assert_type(by_length, dict[int, list[str]])

by_parity = group_by((n for n in range(5)), lambda n: n % 2 == 0)
assert_type(by_parity, dict[bool, list[int]])
"""


def test_groups_in_order():
    assert group_by(["apple", "avocado", "banana"], lambda word: word[0]) == {
        "a": ["apple", "avocado"],
        "b": ["banana"],
    }


def test_key_can_be_any_function():
    assert group_by(["a", "bb", "cc", "d"], len) == {1: ["a", "d"], 2: ["bb", "cc"]}


def test_accepts_any_iterable():
    assert group_by((n for n in range(5)), lambda n: n % 2 == 0) == {
        True: [0, 2, 4],
        False: [1, 3],
    }


def test_empty():
    assert group_by([], len) == {}


def test_passes_mypy_strict(lesson_dir, tmp_path):
    ok, output = type_check_strict(lesson_dir / f"{MODULE}.py", USAGE, tmp_path)
    assert ok, "mypy --strict found problems:\n" + output
