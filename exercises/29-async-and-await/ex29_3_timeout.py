"""Lesson 29 · Async and await · exercise 3.

Check your work with: uv run course.py
"""

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)


async def slow_with_timeout(seconds: float = 5.0, timeout: float = 1.0) -> bool:
    """Give say_after("slow", 5) a 1-second timeout with asyncio.wait_for and
    handle the timeout.

    slow_with_timeout(seconds, timeout) runs say_after("slow", seconds) with
    the given timeout. It returns True when the call finished in time. When it
    times out, it prints "gave up after 1 second" (with the real timeout) and
    returns False.
    """
    raise NotImplementedError("Your code here")
