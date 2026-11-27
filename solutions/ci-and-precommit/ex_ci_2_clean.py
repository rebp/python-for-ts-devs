"""Reference solution for exercise 11.2-2."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
