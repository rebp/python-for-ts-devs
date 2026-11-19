"""Tests for exercise 34-1 (Databases).

Edit: ex34_1_sqlite.py::save_and_list_notes
"""

import sqlite3

from ex34_1_sqlite import save_and_list_notes

NOTES = ["Buy milk", "Learn match", "Call Grace"]


def test_inserts_and_lists(tmp_path):
    db = str(tmp_path / "notes.db")
    assert save_and_list_notes(db, NOTES) == [
        (1, "Buy milk"),
        (2, "Learn match"),
        (3, "Call Grace"),
    ]


def test_data_is_committed(tmp_path):
    db = str(tmp_path / "notes.db")
    save_and_list_notes(db, NOTES)
    conn = sqlite3.connect(db)
    assert conn.execute("SELECT COUNT(*) FROM notes").fetchone() == (3,)
    conn.close()


def test_second_call_adds_to_the_table(tmp_path):
    db = str(tmp_path / "notes.db")
    save_and_list_notes(db, NOTES)
    rows = save_and_list_notes(db, ["Ada's list"])
    assert len(rows) == 4
    assert rows[-1] == (4, "Ada's list")
