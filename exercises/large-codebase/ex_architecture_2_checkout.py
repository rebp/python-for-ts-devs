"""Lesson 13.2 · Structuring a large codebase · exercise 2.

Check your work with: uv run course.py 13.2-2
"""

from collections.abc import Callable


def checkout(prices: list[int], save_total: Callable[[int], None]) -> int:
    """Validate prices, persist the total through the supplied function, and return it.

    An empty list or a negative price raises ValueError before saving.
    Call save_total once on success and let storage errors propagate.
    """
    raise NotImplementedError("Your code here")
