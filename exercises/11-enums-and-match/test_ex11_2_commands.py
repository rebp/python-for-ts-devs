"""Tests for exercise 11-2 (Enums and match).

Edit: ex11_2_commands.py::handle
"""

import ast

import pytest
from ex11_2_commands import handle

from course_helpers import uses_node


def test_go():
    assert handle(["go", "north"]) == "Going north"
    assert handle(["go", "west"]) == "Going west"


def test_quit():
    assert handle(["quit"]) == "Bye"


@pytest.mark.parametrize(
    "command", [[], ["go"], ["go", "north", "fast"], ["dance"], ["quit", "now"]]
)
def test_anything_else(command):
    assert handle(command) == "Unknown command"


def test_uses_match():
    assert uses_node(handle, ast.Match)
