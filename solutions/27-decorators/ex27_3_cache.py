"""Reference solution for exercise 27-3 (Decorators)."""

import functools


@functools.cache
def fib(n: int) -> int:
    """Write a naive recursive fib(n), time fib(32), then add @functools.cache and
    time it again.

    fib(0) is 0, fib(1) is 1, and fib(n) is fib(n - 1) + fib(n - 2). Time a call
    with time.perf_counter() before and after it. The tests check the cached
    version, so leave @functools.cache on when you're done.
    """
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(fib(32), f"{time.perf_counter() - start:.4f}s")  # instant with the cache
