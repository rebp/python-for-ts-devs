"""Tests for exercise 11-1 (Enums and match).

Edit: ex11_1_triangle.py::Triangle
"""

import math
from dataclasses import is_dataclass

import pytest
from ex11_1_triangle import Circle, Rect, Triangle, area


def test_triangle_is_a_dataclass():
    assert is_dataclass(Triangle)


def test_triangle_area():
    assert area(Triangle(base=3, height=4)) == 6
    assert area(Triangle(5, 2)) == 5


def test_other_shapes_still_work():
    assert area(Circle(1)) == pytest.approx(math.pi)
    assert area(Rect(2, 3)) == 6


def test_unknown_shape_raises():
    with pytest.raises(TypeError):
        area("square")
