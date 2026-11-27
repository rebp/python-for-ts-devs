"""Tests for exercise 4.4-2.

Edit: ex_smallfeatures_2_find.py::find_index
"""

import ast

from ex_smallfeatures_2_find import find_index

from course_helpers import source_tree


def test_first_match_and_missing_values() -> None:
    assert find_index(iter(["a", "b", "b"]), "b") == 1
    assert find_index(["", "a"], "") == 0
    assert find_index([], "a") is None
    assert find_index(["a"], "b") is None


def test_has_a_loop_else() -> None:
    assert any(
        isinstance(node, ast.For) and node.orelse
        for node in ast.walk(source_tree(find_index))
    )
