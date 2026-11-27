"""Reference solution for exercise 8.2-1."""

import asyncio
from collections.abc import Awaitable, Callable


async def bounded_map(
    items: list[int], limit: int, work: Callable[[int], Awaitable[int]]
) -> list[int]:
    """Run at most limit calls concurrently and preserve result order."""
    if limit < 1:
        raise ValueError("limit must be at least one")
    semaphore = asyncio.Semaphore(limit)

    async def run_one(item: int) -> int:
        async with semaphore:
            return await work(item)

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(run_one(item)) for item in items]
    return [task.result() for task in tasks]
