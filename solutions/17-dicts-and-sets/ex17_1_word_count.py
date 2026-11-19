"""Reference solution for exercise 17-1 (Dicts and sets)."""

from collections import Counter


def count_words(sentence: str) -> dict[str, int]:
    """Count how often each word appears in a sentence, first with a plain dict,
    then with Counter.

    count_words(sentence) uses a plain dict (no imports) and returns it.
    top_words(sentence, n) (below) uses collections.Counter and returns the n
    most common words as (word, count) pairs.
    """
    counts: dict[str, int] = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(sentence: str, n: int) -> list[tuple[str, int]]:
    """The n most common words, using Counter and its most_common() method."""
    return Counter(sentence.split()).most_common(n)
