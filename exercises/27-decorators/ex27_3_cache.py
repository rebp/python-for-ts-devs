"""Lesson 27 · Decorators · exercise 3.

Check your work with: uv run course.py
"""


def fib(n: int) -> int:
    """Write a naive recursive fib(n), time fib(32), then add @functools.cache and
    time it again.

    fib(0) is 0, fib(1) is 1, and fib(n) is fib(n - 1) + fib(n - 2). Time a call
    with time.perf_counter() before and after it. The tests check the cached
    version, so leave @functools.cache on when you're done.
    """
    raise NotImplementedError("Your code here")
