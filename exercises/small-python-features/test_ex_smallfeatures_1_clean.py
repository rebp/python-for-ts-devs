"""Tests for exercise 4.4-1.

Edit: ex_smallfeatures_1_clean.py::clean_lines
"""

import ast

from ex_smallfeatures_1_clean import clean_lines

from course_helpers import uses_node


def test_strips_and_filters_a_generator() -> None:
    lines = (line for line in ["  Ada ", "", " \t ", "0", " Lin"])
    assert clean_lines(lines) == ["Ada", "0", "Lin"]


def test_empty_input_and_assignment_expression() -> None:
    assert clean_lines([]) == []
    assert uses_node(clean_lines, ast.NamedExpr)
