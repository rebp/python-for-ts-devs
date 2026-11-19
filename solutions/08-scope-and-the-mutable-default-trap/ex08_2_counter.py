"""Reference solution for exercise 08-2 (Scope and the mutable default trap)."""

from collections.abc import Callable


def make_counter() -> Callable[[], int]:
    """Write make_counter() that returns a function. Each call of that function
    returns the next number: 1, 2, 3…

    Each counter is independent: a second make_counter() starts again at 1.

    Hint: the inner function needs nonlocal to update the outer variable.
    """
    count = 0

    def next_number() -> int:
        nonlocal count
        count += 1
        return count

    return next_number
