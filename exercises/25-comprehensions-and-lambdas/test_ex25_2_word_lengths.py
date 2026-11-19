"""Tests for exercise 25-2 (Comprehensions and lambdas).

Edit: ex25_2_word_lengths.py::word_lengths
"""

import ast

from ex25_2_word_lengths import word_lengths

from course_helpers import uses_node


def test_sentence():
    result = word_lengths("the quick brown fox jumps over the lazy dog")
    assert result == {"quick": 5, "brown": 5, "jumps": 5, "over": 4, "lazy": 4}


def test_short_words_only():
    assert word_lengths("a bb ccc") == {}


def test_uses_a_dict_comprehension():
    assert uses_node(word_lengths, ast.DictComp)
