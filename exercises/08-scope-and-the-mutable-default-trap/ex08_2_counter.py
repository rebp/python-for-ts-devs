"""Lesson 08 · Scope and the mutable default trap · exercise 2.

Check your work with: uv run course.py
"""

from collections.abc import Callable


def make_counter() -> Callable[[], int]:
    """Write make_counter() that returns a function. Each call of that function
    returns the next number: 1, 2, 3…

    Each counter is independent: a second make_counter() starts again at 1.

    Hint: the inner function needs nonlocal to update the outer variable.
    """
    raise NotImplementedError("Your code here")
