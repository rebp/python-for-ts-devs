"""Reference solution for exercise 8.2-2."""

import asyncio
from collections.abc import Awaitable, Callable


async def run_workers(
    items: list[str], worker_count: int, handle: Callable[[str], Awaitable[None]]
) -> None:
    """Process items with a bounded queue and structured worker tasks."""
    if worker_count < 1:
        raise ValueError("worker_count must be at least one")
    queue: asyncio.Queue[str] = asyncio.Queue(maxsize=worker_count)

    async def worker() -> None:
        while True:
            try:
                item = await queue.get()
            except asyncio.QueueShutDown:
                return
            try:
                await handle(item)
            finally:
                queue.task_done()

    async with asyncio.TaskGroup() as group:
        for _ in range(worker_count):
            group.create_task(worker())
        for item in items:
            await queue.put(item)
        queue.shutdown()
        await queue.join()
