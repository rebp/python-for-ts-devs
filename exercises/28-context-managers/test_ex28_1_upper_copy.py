"""Tests for exercise 28-1 (Context managers).

Edit: ex28_1_upper_copy.py::upper_copy
"""

import ast

from ex28_1_upper_copy import upper_copy

from course_helpers import source_tree, uses_node


def test_copies_in_uppercase(tmp_path):
    src = tmp_path / "input.txt"
    dst = tmp_path / "output.txt"
    src.write_text("hello\nwörld\n", encoding="utf-8")
    upper_copy(str(src), str(dst))
    assert dst.read_text(encoding="utf-8") == "HELLO\nWÖRLD\n"


def test_one_with_statement_for_both_files():
    assert uses_node(upper_copy, ast.With)
    withs = [
        node for node in ast.walk(source_tree(upper_copy)) if isinstance(node, ast.With)
    ]
    assert len(withs) == 1 and len(withs[0].items) == 2, (
        "open both files in a single with statement"
    )
