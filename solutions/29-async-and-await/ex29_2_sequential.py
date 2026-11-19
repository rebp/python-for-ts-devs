"""Reference solution for exercise 29-2 (Async and await)."""

import asyncio
import time


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
    start = time.perf_counter()
    await say_after("a", seconds)
    await say_after("b", seconds)
    await say_after("c", seconds)
    # About 3 * seconds: each await waits for the previous call to finish.
    return time.perf_counter() - start


if __name__ == "__main__":
    print(asyncio.run(run_one_by_one(1)))
