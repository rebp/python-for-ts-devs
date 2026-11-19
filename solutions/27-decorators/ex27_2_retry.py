"""Reference solution for exercise 27-2 (Decorators)."""

import functools


def retry(times: int = 3):
    """Write @retry(times=3) that calls the function again when it raises, up to
    times attempts, and re-raises the last error.

    Hint: you need three levels: retry(times) returns decorator(fn), which
    returns wrapper(*args, **kwargs).
    """

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
                    print(f"attempt {attempt} failed, retrying")

        return wrapper

    return decorator
