"""Reference solution for exercise 15-3 (Lists and tuples)."""


def stats(nums: list[float]) -> tuple[float, float, float]:
    """Write stats(nums) that returns a tuple (minimum, maximum, average), and
    unpack the result into three variables.

    stats([4, 8, 15, 16, 23, 42]) returns (4, 42, 18.0).
    """
    return min(nums), max(nums), sum(nums) / len(nums)


if __name__ == "__main__":
    low, high, avg = stats([4, 8, 15, 16, 23, 42])
    print(low, high, avg)  # 4 42 18.0
