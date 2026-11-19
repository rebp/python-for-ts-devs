"""Reference solution for exercise 18-3 (Exceptions)."""


def sum_valid(values: list[str]) -> int:
    """Sum ["1", "x", "3", ""], skipping values that aren't numbers and printing a
    warning for each one.

    sum_valid(["1", "x", "3", ""]) returns 4 and prints:

        skipping 'x'
        skipping ''
    """
    total = 0
    for value in values:
        try:
            total += int(value)
        except ValueError:
            print(f"skipping {value!r}")
    return total
