"""Lesson 13 · Protocols and Pydantic · exercise 1.

Check your work with: uv run course.py
"""

from typing import Protocol


class Sized(Protocol):
    """Anything with a size() -> int method."""

    # TODO: declare the method. In a Protocol, its body is just: ...


class Folder:
    """TODO: give it a size() method. Don't inherit from Sized."""


class Photo:
    """TODO: give it a size() method. Don't inherit from Sized."""


def total_size(items: list[Sized]) -> int:
    """Define a Protocol called Sized with a size(self) -> int method, and two
    unrelated classes that satisfy it without inheriting from it.

    Folder() and Photo() take no arguments and each has a size() method that
    returns an int. total_size(items) adds up the sizes of anything that has a
    size() method.
    """
    raise NotImplementedError("Your code here")
