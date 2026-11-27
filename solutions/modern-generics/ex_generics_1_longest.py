"""Reference solution for exercise 3.8-1."""

from collections.abc import Sequence, Sized


def longest[T: Sized](items: Sequence[T]) -> T:
    """Return the first longest item."""
    return max(items, key=len)
