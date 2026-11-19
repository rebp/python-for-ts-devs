"""Tests for exercise 11-3 (Enums and match).

Edit: ex11_3_priority.py::days_to_respond
"""

import ast

from ex11_3_priority import Priority, days_to_respond

from course_helpers import uses_node


def test_members_and_values():
    assert [p.name for p in Priority] == ["LOW", "MEDIUM", "HIGH"]
    assert Priority("medium") is Priority.MEDIUM


def test_days_to_respond():
    assert days_to_respond(Priority.LOW) == 5
    assert days_to_respond(Priority.MEDIUM) == 2
    assert days_to_respond(Priority.HIGH) == 0


def test_from_a_string():
    assert days_to_respond(Priority("high")) == 0


def test_uses_match():
    assert uses_node(days_to_respond, ast.Match)
