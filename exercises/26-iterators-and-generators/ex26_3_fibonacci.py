"""Lesson 26 · Iterators and generators · exercise 3.

Check your work with: uv run course.py
"""

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Write an infinite Fibonacci generator and print the first 10 numbers with
    itertools.islice.

    fibonacci() yields 0, 1, 1, 2, 3, 5… forever. first_fibonacci(n) (below)
    returns the first n of them as a list, using islice.
    """
    raise NotImplementedError("Your code here")


def first_fibonacci(n: int) -> list[int]:
    """The first n Fibonacci numbers, taken from fibonacci() with itertools.islice."""
    raise NotImplementedError("Your code here")
