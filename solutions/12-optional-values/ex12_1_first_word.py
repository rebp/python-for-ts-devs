"""Reference solution for exercise 12-1 (Optional values)."""


def first_word(text: str) -> str | None:
    """Write first_word(text: str) -> str | None that returns None for blank text.

    first_word("hello world") returns "hello"; first_word("   ") returns None.
    """
    words = text.split()
    return words[0] if words else None
