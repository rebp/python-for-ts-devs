"""Lesson 29 · Async and await · exercise 1.

Check your work with: uv run course.py
"""


async def say_after(text: str, seconds: float) -> None:
    """Write async def say_after(text, seconds) that sleeps and then prints. Run
    three of them at once with gather and time the total.

    run_together(seconds) (below) runs say_after("a", seconds),
    say_after("b", seconds) and say_after("c", seconds) at the same time and
    returns how many seconds that took in total (use time.perf_counter()).
    With seconds=1 it takes about 1 second, not 3.

    Try it: asyncio.run(run_together(1)).
    """
    raise NotImplementedError("Your code here")


async def run_together(seconds: float = 1.0) -> float:
    """Run three say_after calls at once with asyncio.gather; return the elapsed seconds."""
    raise NotImplementedError("Your code here")
