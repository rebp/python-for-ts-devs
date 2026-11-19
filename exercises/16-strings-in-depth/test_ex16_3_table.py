"""Tests for exercise 16-3 (Strings in depth).

Edit: ex16_3_table.py::print_table
"""

from ex16_3_table import print_table


def test_table(capsys):
    print_table([("Lamp", 19.9), ("Desk", 249), ("Pen", 1.5)])
    assert capsys.readouterr().out.splitlines() == [
        "Lamp         19.90",
        "Desk        249.00",
        "Pen           1.50",
    ]


def test_every_line_is_18_characters(capsys):
    print_table([("Notebook", 3), ("Chair", 1234.5)])
    lines = capsys.readouterr().out.splitlines()
    assert [len(line) for line in lines] == [18, 18]
    assert lines[1] == "Chair      1234.50"
