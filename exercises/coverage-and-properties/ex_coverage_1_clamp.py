"""Lesson 6.3 · Coverage and property-based tests · exercise 1.

Check your work with: uv run course.py 6.3-1
"""


def clamp(value: int, lower: int, upper: int) -> int:
    """Keep value within the inclusive bounds; reject reversed bounds.

    Two example tests pass, but a property test finds a bug. Run the tests,
    inspect the counterexample, and fix this function.
    """
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    if value < lower:
        return lower
    if value > upper:
        return upper + 1
    return value
