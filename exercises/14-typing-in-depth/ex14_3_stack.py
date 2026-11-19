"""Lesson 14 · Typing in depth · exercise 3.

Check your work with: uv run course.py
"""

from typing import Self  # noqa: F401


class Stack:
    """Make Stack a generic class, the Python version of class Stack<T>.

    - Stack[int]() holds ints, Stack[str]() holds strings.
    - push(item) adds an item and returns the stack itself, so calls chain:
      Stack[int]().push(1).push(2). Annotate the return type as Self.
    - pop() removes and returns the last item, or raises IndexError when the
      stack is empty.
    - peek() returns the last item without removing it, or None when empty.
    - len(stack) is the number of items (define __len__).

    The tests run mypy --strict, and check that Stack[int]().push("three") is
    a type error and that pop() on a Stack[int] is an int.
    """

    def __init__(self) -> None:
        raise NotImplementedError("Your code here")
