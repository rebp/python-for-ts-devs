"""Tests for exercise 16-2 (Strings in depth).

Edit: ex16_2_vowels.py::count_vowels
"""

from ex16_2_vowels import count_vowels


def test_sentence():
    assert count_vowels("Python for TypeScript developers") == 8


def test_ignores_case():
    assert count_vowels("AEIOU aeiou") == 10


def test_no_vowels():
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
