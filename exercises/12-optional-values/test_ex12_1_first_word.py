"""Tests for exercise 12-1 (Optional values).

Edit: ex12_1_first_word.py::first_word
"""

from ex12_1_first_word import first_word


def test_first_word():
    assert first_word("hello world") == "hello"
    assert first_word("  padded   text ") == "padded"


def test_blank_text_is_none():
    assert first_word("") is None
    assert first_word("   ") is None
