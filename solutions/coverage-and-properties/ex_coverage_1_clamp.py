"""Reference solution for exercise 6.3-1."""


def clamp(value: int, lower: int, upper: int) -> int:
    """Keep value within the inclusive bounds."""
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
