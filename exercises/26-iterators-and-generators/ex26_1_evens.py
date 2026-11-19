"""Lesson 26 · Iterators and generators · exercise 1.

Check your work with: uv run course.py
"""

from collections.abc import Iterator


def evens(limit: int) -> Iterator[int]:
    """Write a generator evens(limit) that yields 0, 2, 4… up to and including limit.

    list(evens(10)) is [0, 2, 4, 6, 8, 10]. Use yield.
    """
    raise NotImplementedError("Your code here")
