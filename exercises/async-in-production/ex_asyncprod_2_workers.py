"""Lesson 8.2 · Async in production · exercise 2.

Check your work with: uv run course.py 8.2-2
"""

from collections.abc import Awaitable, Callable


async def run_workers(
    items: list[str], worker_count: int, handle: Callable[[str], Awaitable[None]]
) -> None:
    """Process every item using a bounded queue and worker_count workers.

    Reject worker_count below one with ValueError. Finish all items on
    success; if a handler fails, cancel the other workers and propagate
    the error. Shut down the queue after producing the items.
    """
    raise NotImplementedError("Your code here")
