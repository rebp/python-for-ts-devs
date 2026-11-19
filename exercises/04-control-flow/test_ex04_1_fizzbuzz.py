"""Tests for exercise 04-1 (Control flow).

Edit: ex04_1_fizzbuzz.py::fizzbuzz
"""

from ex04_1_fizzbuzz import fizzbuzz

EXPECTED_20 = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
    "16",
    "17",
    "Fizz",
    "19",
    "Buzz",
]


def test_one_to_twenty(capsys):
    fizzbuzz()
    assert capsys.readouterr().out.splitlines() == EXPECTED_20


def test_custom_limit(capsys):
    fizzbuzz(5)
    assert capsys.readouterr().out.splitlines() == ["1", "2", "Fizz", "4", "Buzz"]
