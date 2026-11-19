"""Reference solution for exercise 15-1 (Lists and tuples)."""


def swap_ends(items: list) -> list:
    """Write swap_ends(items) that returns a new list with the first and last items
    swapped. The input must not change.

    swap_ends([1, 2, 3, 4]) returns [4, 2, 3, 1]. Lists with fewer than two items
    come back as a copy.
    """
    if len(items) < 2:
        return items[:]
    return [items[-1], *items[1:-1], items[0]]
