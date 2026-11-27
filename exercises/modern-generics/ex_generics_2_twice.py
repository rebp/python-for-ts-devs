"""Lesson 3.8 · Generics the modern way · exercise 2.

Check your work with: uv run course.py 3.8-2
"""

from collections.abc import Callable


def twice[**P, R](function: Callable[P, R]) -> Callable[P, tuple[R, R]]:
    """Return a wrapper that calls function twice with the same arguments.

    Preserve the original callable's parameter types and metadata. Return
    both results in a tuple and let exceptions propagate.
    """
    raise NotImplementedError("Your code here")
