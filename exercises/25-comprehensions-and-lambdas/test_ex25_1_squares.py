"""Tests for exercise 25-1 (Comprehensions and lambdas).

Edit: ex25_1_squares.py::even_squares
"""

import ast

from ex25_1_squares import even_squares

from course_helpers import uses_node


def test_one_to_twenty():
    assert even_squares() == [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


def test_custom_limit():
    assert even_squares(6) == [4, 16, 36]
    assert even_squares(1) == []


def test_uses_a_list_comprehension():
    assert uses_node(even_squares, ast.ListComp)
