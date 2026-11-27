"""Lesson 6.5 · Profiling and performance · exercise 2.

Check your work with: uv run course.py 6.5-2
"""

from collections.abc import Iterable


def drain_queue(items: Iterable[int]) -> list[int]:
    """Return items in FIFO order using deque.popleft, not list.pop(0)."""
    raise NotImplementedError("Your code here")
