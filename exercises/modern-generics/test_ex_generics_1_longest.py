"""Tests for exercise 3.8-1.

Edit: ex_generics_1_longest.py::longest
"""

from pathlib import Path

import pytest
from ex_generics_1_longest import longest

from course_helpers import type_check_strict

USAGE = """
from typing import assert_type
from ex_generics_1_longest import longest

assert_type(longest(["a", "bbb"]), str)
assert_type(longest([[1], [1, 2]]), list[int])
longest([1, 2])  # type: ignore[type-var]
"""


def test_preserves_values_and_first_tie() -> None:
    assert longest(["a", "two", "six"]) == "two"
    assert longest([[1], [1, 2]]) == [1, 2]
    assert longest(((1,), (2, 3))) == (2, 3)


def test_empty_sequence() -> None:
    with pytest.raises(ValueError):
        longest([])


def test_bound_and_return_type_are_checked(lesson_dir: Path, tmp_path: Path) -> None:
    ok, output = type_check_strict(
        lesson_dir / "ex_generics_1_longest.py", USAGE, tmp_path
    )
    assert ok, output
