"""Tests for exercise 17-1 (Dicts and sets).

Edit: ex17_1_word_count.py::count_words
"""

from ex17_1_word_count import count_words, top_words

from course_helpers import calls_name

SENTENCE = "the cat and the hat and the bat"


def test_count_words():
    result = count_words(SENTENCE)
    assert result == {"the": 3, "cat": 1, "and": 2, "hat": 1, "bat": 1}
    assert type(result) is dict, "use a plain dict here, Counter comes next"


def test_top_words():
    assert top_words(SENTENCE, 2) == [("the", 3), ("and", 2)]


def test_top_words_uses_counter():
    assert calls_name(top_words, "Counter")
