"""Reference solution for exercise 16-2 (Strings in depth)."""


def count_vowels(text: str) -> int:
    """Count the vowels in a sentence, ignoring case.

    count_vowels("Python for TypeScript developers") returns 8. Only a, e, i, o
    and u count as vowels.
    """
    return sum(1 for ch in text.lower() if ch in "aeiou")
