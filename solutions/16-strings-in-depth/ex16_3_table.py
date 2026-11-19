"""Reference solution for exercise 16-3 (Strings in depth)."""


def print_table(items: list[tuple[str, float]]) -> None:
    """Print a small table: names left-aligned in 10 characters, prices
    right-aligned in 8 characters with 2 decimals.

    print_table([("Lamp", 19.9), ("Desk", 249), ("Pen", 1.5)]) prints:

        Lamp         19.90
        Desk        249.00
        Pen           1.50

    Hint: format specs go after a colon in an f-string: < left-aligns,
    > right-aligns.
    """
    for name, price in items:
        print(f"{name:<10}{price:>8.2f}")
