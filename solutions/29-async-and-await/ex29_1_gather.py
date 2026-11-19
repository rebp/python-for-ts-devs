"""Reference solution for exercise 29-1 (Async and await)."""

import asyncio
import time


async def say_after(text: str, seconds: float) -> None:
    """Write async def say_after(text, seconds) that sleeps and then prints. Run
    three of them at once with gather and time the total.

    run_together(seconds) (below) runs say_after("a", seconds),
    say_after("b", seconds) and say_after("c", seconds) at the same time and
    returns how many seconds that took in total (use time.perf_counter()).
    With seconds=1 it takes about 1 second, not 3.

    Try it: asyncio.run(run_together(1)).
    """
    await asyncio.sleep(seconds)
    print(text)


async def run_together(seconds: float = 1.0) -> float:
    """Run three say_after calls at once with asyncio.gather; return the elapsed seconds."""
    start = time.perf_counter()
    await asyncio.gather(
        say_after("a", seconds), say_after("b", seconds), say_after("c", seconds)
    )
    return time.perf_counter() - start
