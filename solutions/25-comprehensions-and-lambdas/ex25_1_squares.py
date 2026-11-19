"""Reference solution for exercise 25-1 (Comprehensions and lambdas)."""


def even_squares(limit: int = 20) -> list[int]:
    """Build a list of the squares of the even numbers from 1 to 20.

    even_squares() returns [4, 16, 36, ..., 400]; even_squares(6) returns
    [4, 16, 36]. Use a list comprehension.
    """
    return [n * n for n in range(1, limit + 1) if n % 2 == 0]
