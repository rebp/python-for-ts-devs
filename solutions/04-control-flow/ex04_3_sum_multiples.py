"""Reference solution for exercise 04-3 (Control flow)."""


def sum_multiples_while(limit: int = 100) -> int:
    """Sum the numbers from 1 to 100 that are divisible by 3 or 5, first with a
    while loop, then with for and range.

    Write it twice: sum_multiples_while(limit) with a while loop, and
    sum_multiples_for(limit) (below) with for and range. Both include limit
    itself, and both return 2418 for 100.
    """
    total, n = 0, 1
    while n <= limit:
        if n % 3 == 0 or n % 5 == 0:
            total += n
        n += 1
    return total


def sum_multiples_for(limit: int = 100) -> int:
    """Same result as sum_multiples_while, written with for and range()."""
    total = 0
    for n in range(1, limit + 1):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total
