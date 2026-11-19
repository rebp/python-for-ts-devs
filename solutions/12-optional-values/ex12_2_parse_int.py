"""Reference solution for exercise 12-2 (Optional values)."""


def parse_int(s: str) -> int | None:
    """Write parse_int(s: str) -> int | None that returns None instead of raising
    when the text isn't a number.
    """
    try:
        return int(s)
    except ValueError:
        return None
