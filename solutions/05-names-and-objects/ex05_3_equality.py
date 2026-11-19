"""Reference solution for exercise 05-3 (Names and objects)."""


def compare(x: list[int], y: list[int]) -> tuple[bool, bool]:
    """Create x = [1, 2] and y = [1, 2]. Compare them with == and is and explain
    the results.

    compare(x, y) returns the pair (x == y, x is y). For two separate lists
    [1, 2] it returns (True, False). Write a comment in your solution that
    explains why.
    """
    # == compares contents; `is` asks "are these the same object?", like === on objects.
    # Two list literals create two separate list objects, so x is y is False.
    return x == y, x is y
