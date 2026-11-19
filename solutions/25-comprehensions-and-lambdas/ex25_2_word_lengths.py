"""Reference solution for exercise 25-2 (Comprehensions and lambdas)."""


def word_lengths(sentence: str) -> dict[str, int]:
    """From a sentence, build a dict of word → length, keeping only words longer
    than 3 letters.

    word_lengths("the quick brown fox jumps over the lazy dog") returns
    {'quick': 5, 'brown': 5, 'jumps': 5, 'over': 4, 'lazy': 4}.
    Use a dict comprehension.
    """
    return {word: len(word) for word in sentence.split() if len(word) > 3}
