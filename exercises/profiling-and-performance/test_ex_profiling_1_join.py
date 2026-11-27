"""Tests for exercise 6.5-1.

Edit: ex_profiling_1_join.py::join_fragments
"""

from ex_profiling_1_join import join_fragments

from course_helpers import calls_name


def test_joins_once_in_order() -> None:
    assert join_fragments(part for part in ["a", "", "b"]) == "ab"
    assert join_fragments([]) == ""


def test_uses_join() -> None:
    assert calls_name(join_fragments, "join")
