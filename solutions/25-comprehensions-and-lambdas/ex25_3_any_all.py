"""Reference solution for exercise 25-3 (Comprehensions and lambdas)."""


def someone_failed(scores: list[int]) -> bool:
    """Given scores = [72, 95, 48, 88], use any() to check whether someone failed
    (below 50) and all() to check that every score is below 100.

    someone_failed(scores) uses any(); all_below_100(scores) (below) uses all().
    Both return True for [72, 95, 48, 88].
    """
    return any(s < 50 for s in scores)


def all_below_100(scores: list[int]) -> bool:
    """True when every score is below 100. Use all()."""
    return all(s < 100 for s in scores)
