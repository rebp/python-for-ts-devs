"""Tests for exercise 04-3 (Control flow).

Edit: ex04_3_sum_multiples.py::sum_multiples_while
"""

import ast

import pytest
from ex04_3_sum_multiples import sum_multiples_for, sum_multiples_while

from course_helpers import calls_name, uses_node


@pytest.mark.parametrize("fn", [sum_multiples_while, sum_multiples_for])
def test_one_to_hundred(fn):
    assert fn() == 2418
    assert fn(100) == 2418


@pytest.mark.parametrize("fn", [sum_multiples_while, sum_multiples_for])
def test_limit_is_included(fn):
    assert fn(10) == 3 + 5 + 6 + 9 + 10


def test_while_version_uses_while():
    assert uses_node(sum_multiples_while, ast.While)


def test_for_version_uses_for_and_range():
    assert uses_node(sum_multiples_for, ast.For)
    assert calls_name(sum_multiples_for, "range")
