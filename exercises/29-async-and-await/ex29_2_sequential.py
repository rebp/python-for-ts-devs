"""Lesson 29 · Async and await · exercise 2.

Check your work with: uv run course.py
"""

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)


async def run_one_by_one(seconds: float = 1.0) -> float:
    """Now await the three calls one after another instead of using gather. How
    long does it take?

    run_one_by_one(seconds) awaits say_after("a", seconds), then "b", then
    "c", and returns the elapsed seconds (import time and use time.perf_counter()).
    Write your answer to "how long?" as a
    comment.
    """
    raise NotImplementedError("Your code here")
