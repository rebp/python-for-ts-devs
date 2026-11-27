"""Tests for exercise 12.2-1.

Edit: ex_arrays_1_scale.py::scale_nonnegative
"""

import ast

import numpy as np
from ex_arrays_1_scale import scale_nonnegative

from course_helpers import uses_node


def test_scales_without_mutating_the_input() -> None:
    values = np.array([-2.0, 0.0, 3.0])
    np.testing.assert_array_equal(scale_nonnegative(values, 2.0), [0.0, 0.0, 6.0])
    np.testing.assert_array_equal(values, [-2.0, 0.0, 3.0])
    np.testing.assert_array_equal(scale_nonnegative(values, -1.0), [2.0, 0.0, 0.0])


def test_empty_array_and_vectorized_implementation() -> None:
    assert scale_nonnegative(np.array([], dtype=np.float64), 2.0).size == 0
    assert not uses_node(scale_nonnegative, ast.For)
    assert not uses_node(scale_nonnegative, ast.While)
    assert not uses_node(scale_nonnegative, ast.ListComp)
