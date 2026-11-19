"""Tests for exercise 34-3 (Databases).

Edit: ex34_3_sqlalchemy.py::save_and_list_notes_orm
"""

from ex34_3_sqlalchemy import Base, Note, save_and_list_notes_orm


def test_note_is_a_mapped_class():
    assert issubclass(Note, Base)
    assert Note.__tablename__ == "notes"
    assert set(Note.__table__.columns.keys()) == {"id", "text"}
    assert Note.__table__.columns["id"].primary_key


def test_saves_and_lists(tmp_path):
    url = f"sqlite:///{tmp_path / 'notes_orm.db'}"
    assert save_and_list_notes_orm(url, ["Buy milk", "Learn match"]) == [
        (1, "Buy milk"),
        (2, "Learn match"),
    ]


def test_second_call_adds_to_the_table(tmp_path):
    url = f"sqlite:///{tmp_path / 'notes_orm.db'}"
    save_and_list_notes_orm(url, ["Buy milk"])
    assert save_and_list_notes_orm(url, ["Call Grace"]) == [
        (1, "Buy milk"),
        (2, "Call Grace"),
    ]
