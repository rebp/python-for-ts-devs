"""Tests for exercise 26-2 (Iterators and generators).

Edit: ex26_2_read_lines.py::read_lines
"""

import inspect

from ex26_2_read_lines import read_lines


def test_is_a_generator_function():
    assert inspect.isgeneratorfunction(read_lines), "use yield"


def test_strips_and_skips_empty_lines(tmp_path):
    notes = tmp_path / "notes.txt"
    notes.write_text("  first  \n\nsecond\n   \nthird", encoding="utf-8")
    assert list(read_lines(str(notes))) == ["first", "second", "third"]


def test_empty_file(tmp_path):
    empty = tmp_path / "empty.txt"
    empty.write_text("", encoding="utf-8")
    assert list(read_lines(str(empty))) == []
