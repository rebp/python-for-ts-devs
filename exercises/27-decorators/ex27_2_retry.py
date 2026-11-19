"""Lesson 27 · Decorators · exercise 2.

Check your work with: uv run course.py
"""


def retry(times: int = 3):
    """Write @retry(times=3) that calls the function again when it raises, up to
    times attempts, and re-raises the last error.

    Hint: you need three levels: retry(times) returns decorator(fn), which
    returns wrapper(*args, **kwargs).
    """
    raise NotImplementedError("Your code here")
