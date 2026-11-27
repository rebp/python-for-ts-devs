"""Lesson 8.2 · Async in production · exercise 1.

Check your work with: uv run course.py 8.2-1
"""

from collections.abc import Awaitable, Callable


async def bounded_map(
    items: list[int], limit: int, work: Callable[[int], Awaitable[int]]
) -> list[int]:
    """Run work concurrently, with at most limit calls active at once.

    Return results in input order. Reject a limit below one with ValueError.
    If one call fails, cancel its siblings and propagate the failure.
    """
    raise NotImplementedError("Your code here")
