"""Lesson 3.8 · Generics the modern way · exercise 1.

Check your work with: uv run course.py 3.8-1
"""

from collections.abc import Sequence, Sized


def longest[T: Sized](items: Sequence[T]) -> T:
    """Return the longest item, keeping its specific type.

    On ties return the first item. Raise ValueError for an empty sequence.
    The type checker should reject elements that do not support len().
    """
    raise NotImplementedError("Your code here")
