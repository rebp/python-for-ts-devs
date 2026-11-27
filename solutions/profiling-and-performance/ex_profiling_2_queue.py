"""Reference solution for exercise 6.5-2."""

from collections import deque
from collections.abc import Iterable


def drain_queue(items: Iterable[int]) -> list[int]:
    """Drain a FIFO queue efficiently."""
    queue = deque(items)
    result: list[int] = []
    while queue:
        result.append(queue.popleft())
    return result
