"""Reference solution for exercise 07-1 (Truthiness, None and equality)."""


def describe(value: object) -> str:
    """Write describe(value) that returns "empty" for falsy values and "has value"
    otherwise. Try it with 0, "", [], [0] and None.
    """
    return "has value" if value else "empty"
