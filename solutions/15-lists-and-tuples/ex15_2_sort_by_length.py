"""Reference solution for exercise 15-2 (Lists and tuples)."""


def sort_by_length(words: list[str]) -> list[str]:
    """Sort ["kiwi", "banana", "fig", "apple"] by length, then by length from longest
    to shortest.

    sort_by_length(words) returns ['fig', 'kiwi', 'apple', 'banana'] and
    sort_by_length_desc(words) (below) returns ['banana', 'apple', 'kiwi', 'fig'].
    Both return new lists and leave the input alone.
    """
    return sorted(words, key=len)


def sort_by_length_desc(words: list[str]) -> list[str]:
    """Longest first."""
    return sorted(words, key=len, reverse=True)
