"""Reference solution for exercise 03-1 (Functions)."""


def area(width: float, height: float = 1) -> float:
    """Write area(width, height=1) and call it once positionally and once with
    keyword arguments in reverse order.

    area(3, 4) and area(height=4, width=3) both return 12, and area(5) returns 5.
    """
    return width * height
