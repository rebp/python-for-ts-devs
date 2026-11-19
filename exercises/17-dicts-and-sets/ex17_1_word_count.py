"""Lesson 17 · Dicts and sets · exercise 1.

Check your work with: uv run course.py
"""


def count_words(sentence: str) -> dict[str, int]:
    """Count how often each word appears in a sentence, first with a plain dict,
    then with Counter.

    count_words(sentence) uses a plain dict (no imports) and returns it.
    top_words(sentence, n) (below) uses collections.Counter and returns the n
    most common words as (word, count) pairs.
    """
    raise NotImplementedError("Your code here")


def top_words(sentence: str, n: int) -> list[tuple[str, int]]:
    """The n most common words, using Counter and its most_common() method."""
    raise NotImplementedError("Your code here")
