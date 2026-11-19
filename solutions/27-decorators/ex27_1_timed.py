"""Reference solution for exercise 27-1 (Decorators)."""

import functools
import time


def timed(fn):
    """Write a @timed decorator that prints how long the function took.

    The message looks like "add took 0.0001s" (4 decimals), the decorated
    function still returns its result, and functools.wraps keeps its name.
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {time.perf_counter() - start:.4f}s")
        return result

    return wrapper
