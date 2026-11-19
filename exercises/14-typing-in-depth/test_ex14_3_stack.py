"""Tests for exercise 14-3 (Typing in depth).

Edit: ex14_3_stack.py::Stack
"""

import pytest
from ex14_3_stack import Stack

from course_helpers import type_check_strict

MODULE = "ex14_3_stack"

USAGE = """
from typing import assert_type

from ex14_3_stack import Stack

numbers = Stack[int]().push(1).push(2)
assert_type(numbers, Stack[int])
assert_type(numbers.pop(), int)
assert_type(numbers.peek(), int | None)
assert_type(len(numbers), int)
numbers.push("three")  # type: ignore[arg-type]
"""


def test_push_and_pop():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_push_chains():
    stack = Stack[str]().push("a").push("b")
    assert isinstance(stack, Stack)
    assert len(stack) == 2
    assert stack.peek() == "b"


def test_peek_does_not_remove():
    stack = Stack[int]().push(7)
    assert stack.peek() == 7
    assert len(stack) == 1


def test_empty_stack():
    stack = Stack[int]()
    assert len(stack) == 0
    assert stack.peek() is None
    with pytest.raises(IndexError):
        stack.pop()


def test_passes_mypy_strict(lesson_dir, tmp_path):
    ok, output = type_check_strict(lesson_dir / f"{MODULE}.py", USAGE, tmp_path)
    assert ok, "mypy --strict found problems:\n" + output
