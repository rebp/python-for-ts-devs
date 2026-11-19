"""Tests for exercise 10-3 (Dataclasses).

Edit: ex10_3_frozen.py::Point
"""

import dataclasses

import pytest
from ex10_3_frozen import Point


def test_cannot_assign():
    p = Point(1, 2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 5


def test_points_are_hashable():
    visited = {Point(1, 2), Point(1, 2), Point(3, 4)}
    assert len(visited) == 2
