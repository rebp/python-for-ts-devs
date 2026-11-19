"""Reference solution for exercise 26-3 (Iterators and generators)."""

from collections.abc import Iterator
from itertools import islice


def fibonacci() -> Iterator[int]:
    """Write an infinite Fibonacci generator and print the first 10 numbers with
    itertools.islice.

    fibonacci() yields 0, 1, 1, 2, 3, 5… forever. first_fibonacci(n) (below)
    returns the first n of them as a list, using islice.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def first_fibonacci(n: int) -> list[int]:
    """The first n Fibonacci numbers, taken from fibonacci() with itertools.islice."""
    return list(islice(fibonacci(), n))
