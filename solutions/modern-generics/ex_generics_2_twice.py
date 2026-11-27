"""Reference solution for exercise 3.8-2."""

from collections.abc import Callable
from functools import wraps


def twice[**P, R](function: Callable[P, R]) -> Callable[P, tuple[R, R]]:
    """Call a function twice without losing its parameter types."""

    @wraps(function)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> tuple[R, R]:
        return function(*args, **kwargs), function(*args, **kwargs)

    return wrapped
