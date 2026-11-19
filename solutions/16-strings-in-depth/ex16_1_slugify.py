"""Reference solution for exercise 16-1 (Strings in depth)."""


def slugify(text: str) -> str:
    """Write slugify(text) so that slugify("Hello World, Python!") returns
    "hello-world-python".

    Lowercase everything, drop punctuation, keep letters and digits, and join
    the words with single hyphens.

    Hint: keep characters where ch.isalnum() or ch.isspace(), then split() and
    join with hyphens.
    """
    cleaned = "".join(ch for ch in text.lower() if ch.isalnum() or ch.isspace())
    return "-".join(cleaned.split())
