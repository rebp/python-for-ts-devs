"""Tests for exercise 3.8-2.

Edit: ex_generics_2_twice.py::twice
"""

from pathlib import Path

import pytest
from ex_generics_2_twice import twice

from course_helpers import type_check_strict

USAGE = """
from typing import assert_type
from ex_generics_2_twice import twice

def label(prefix: str, *, count: int) -> str:
    return prefix * count

wrapped = twice(label)
assert_type(wrapped("a", count=2), tuple[str, str])
wrapped(1, count=2)  # type: ignore[arg-type]
wrapped("a")  # type: ignore[call-arg]
"""


def test_calls_twice_with_positional_and_keyword_arguments() -> None:
    calls: list[tuple[str, int]] = []

    def label(prefix: str, *, count: int) -> str:
        calls.append((prefix, count))
        return prefix * count

    wrapped = twice(label)
    assert wrapped("a", count=2) == ("aa", "aa")
    assert calls == [("a", 2), ("a", 2)]
    assert wrapped.__name__ == "label"


def test_propagates_errors() -> None:
    def fail() -> int:
        raise ValueError("failed")

    with pytest.raises(ValueError, match="failed"):
        twice(fail)()


def test_preserves_the_callable_signature(lesson_dir: Path, tmp_path: Path) -> None:
    ok, output = type_check_strict(
        lesson_dir / "ex_generics_2_twice.py", USAGE, tmp_path
    )
    assert ok, output
