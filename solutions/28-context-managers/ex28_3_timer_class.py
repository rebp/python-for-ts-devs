"""Reference solution for exercise 28-3 (Context managers)."""

import time
from typing import Self


class Timer:
    """Write the timer example as a class with __enter__ and __exit__ instead of a
    generator.

    `with Timer("load"):` prints something like "load: 0.201s" (3 decimals) when
    the block ends, also when it raises. __enter__ returns the Timer itself, and
    exceptions from the block are not swallowed.
    """

    def __init__(self, label: str) -> None:
        self.label = label

    def __enter__(self) -> Self:
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        print(f"{self.label}: {time.perf_counter() - self.start:.3f}s")
