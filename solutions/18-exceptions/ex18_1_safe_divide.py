"""Reference solution for exercise 18-1 (Exceptions)."""


def safe_divide(a: float, b: float) -> float | None:
    """Write safe_divide(a, b) that returns None instead of crashing when b is 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
