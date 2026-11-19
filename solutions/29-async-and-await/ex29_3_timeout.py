"""Reference solution for exercise 29-3 (Async and await)."""

import asyncio
import time


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
    try:
        await asyncio.wait_for(say_after("slow", seconds), timeout=timeout)
    except TimeoutError:
        print(f"gave up after {timeout:g} second{'' if timeout == 1 else 's'}")
        return False
    return True


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(slow_with_timeout())
    print(f"took {time.perf_counter() - start:.1f}s")
