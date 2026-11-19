"""Reference solution for exercise 03-2 (Functions)."""


def average(*nums: float) -> float:
    """Write average(*nums) that returns the average, or 0 when called with no
    arguments.

    average(1, 2, 3) returns 2.0 and average() returns 0.

    Hint: nums is a tuple. An empty tuple is falsy, and len() gives its length.
    """
    if not nums:
        return 0
    return sum(nums) / len(nums)
