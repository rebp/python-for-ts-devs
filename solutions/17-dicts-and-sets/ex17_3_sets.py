"""Reference solution for exercise 17-3 (Dicts and sets)."""


def compare_weeks(
    week1: list[int], week2: list[int]
) -> tuple[set[int], set[int], set[int]]:
    """Given two lists of user IDs, find the users in both, only in the first, and
    in either.

    compare_weeks(week1, week2) returns three sets: (in_both, only_in_first,
    in_either).
    """
    a, b = set(week1), set(week2)
    return a & b, a - b, a | b
