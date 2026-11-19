"""Reference solution for exercise 26-1 (Iterators and generators)."""

from collections.abc import Iterator


def evens(limit: int) -> Iterator[int]:
    """Write a generator evens(limit) that yields 0, 2, 4… up to and including limit.

    list(evens(10)) is [0, 2, 4, 6, 8, 10]. Use yield.
    """
    n = 0
    while n <= limit:
        yield n
        n += 2
