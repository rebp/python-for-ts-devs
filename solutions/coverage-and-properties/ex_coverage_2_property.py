"""Reference solution for exercise 6.3-2."""

from ex_coverage_words import normalize
from hypothesis import given, settings
from hypothesis import strategies as st


@settings(derandomize=True, database=None, deadline=None)
@given(st.lists(st.text(alphabet="abc", min_size=1, max_size=5), max_size=5))
def test_words(words: list[str]) -> None:
    """Normalization preserves words and separates them with single spaces."""
    assert normalize(" \t".join(words)) == " ".join(words)
