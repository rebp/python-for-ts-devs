"""Tests for exercise 01-1 (Hello, Python).

Edit: ex01_1_me.py::introduce
"""

from ex01_1_me import introduce


def test_prints_name_then_language(capsys):
    introduce("Ada", "TypeScript")
    assert capsys.readouterr().out == "Ada\nTypeScript\n"


def test_works_with_other_values(capsys):
    introduce("Grace", "COBOL")
    assert capsys.readouterr().out.splitlines() == ["Grace", "COBOL"]
