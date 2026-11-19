"""Reference solution for exercise 17-2 (Dicts and sets)."""

from collections import defaultdict


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group ["apple", "avocado", "banana", "blueberry", "cherry"] by first letter.

    group_by_first_letter(words) returns a plain dict:
    {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}

    Hint: collections.defaultdict(list) saves you the "is the key there yet?"
    check. Convert it with dict(...) before returning.
    """
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)
