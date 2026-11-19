"""Tests for exercise 03-1 (Functions).

Edit: ex03_1_area.py::area
"""

import inspect

from ex03_1_area import area


def test_positional():
    assert area(3, 4) == 12


def test_keywords_in_reverse_order():
    assert area(height=4, width=3) == 12


def test_height_defaults_to_one():
    assert inspect.signature(area).parameters["height"].default == 1
    assert area(5) == 5
