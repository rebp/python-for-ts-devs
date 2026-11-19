"""Tests for exercise 02-3 (Variables and types).

Edit: ex02_3_minutes.py::format_minutes
"""

import ast

import pytest
from ex02_3_minutes import format_minutes

from course_helpers import uses_node


@pytest.mark.parametrize(
    "minutes, expected",
    [(135, "2 h 15 min"), (60, "1 h 0 min"), (59, "0 h 59 min"), (0, "0 h 0 min")],
)
def test_format(minutes, expected):
    assert format_minutes(minutes) == expected


def test_uses_floor_division_and_modulo():
    assert uses_node(format_minutes, ast.FloorDiv), "use // for the hours"
    assert uses_node(format_minutes, ast.Mod), "use % for the minutes"
