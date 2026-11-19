"""Tests for exercise 01-2 (Hello, Python).

Edit: ex01_2_f_string.py::lived_in
"""

import ast

from ex01_2_f_string import lived_in

from course_helpers import uses_node


def test_lisbon():
    assert lived_in("Lisbon", 2019) == "I've lived in Lisbon since 2019"


def test_other_city():
    assert lived_in("Porto", 2023) == "I've lived in Porto since 2023"


def test_uses_an_f_string():
    assert uses_node(lived_in, ast.JoinedStr), (
        'build the sentence with an f-string: f"...{city}..."'
    )
