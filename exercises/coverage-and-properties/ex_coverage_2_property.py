"""Lesson 6.3 · Coverage and property-based tests · exercise 2.

Write a Hypothesis property for normalize: words separated by arbitrary
whitespace should become the same words separated by single spaces. The
runner checks your property against working and deliberately broken code.
"""

from ex_coverage_words import normalize  # noqa: F401  (use it in the property)
from hypothesis import given, settings
from hypothesis import strategies as st


@settings(derandomize=True, database=None, deadline=None)
@given(st.lists(st.text(alphabet="abc", min_size=1, max_size=5), max_size=5))
def test_words(words: list[str]) -> None:
    """Check that normalization preserves the words and their order."""
    raise NotImplementedError("Your code here")
