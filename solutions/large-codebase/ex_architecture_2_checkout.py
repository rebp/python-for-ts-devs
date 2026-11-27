"""Reference solution for exercise 13.2-2."""

from collections.abc import Callable


def checkout(prices: list[int], save_total: Callable[[int], None]) -> int:
    """Validate before using the injected storage function."""
    if not prices or any(price < 0 for price in prices):
        raise ValueError("prices must be nonempty and nonnegative")
    total = sum(prices)
    save_total(total)
    return total
