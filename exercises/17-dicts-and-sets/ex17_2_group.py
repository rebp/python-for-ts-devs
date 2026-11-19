"""Lesson 17 · Dicts and sets · exercise 2.

Check your work with: uv run course.py
"""


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group ["apple", "avocado", "banana", "blueberry", "cherry"] by first letter.

    group_by_first_letter(words) returns a plain dict:
    {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}

    Hint: collections.defaultdict(list) saves you the "is the key there yet?"
    check. Convert it with dict(...) before returning.
    """
    raise NotImplementedError("Your code here")
