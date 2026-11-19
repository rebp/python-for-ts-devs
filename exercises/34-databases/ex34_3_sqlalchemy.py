"""Lesson 34 · Databases · exercise 3.

Check your work with: uv run course.py
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Note:
    """TODO: make this a mapped class: subclass Base, set __tablename__, add id and text."""


def save_and_list_notes_orm(url: str, texts: list[str]) -> list[tuple[int, str]]:
    """Rewrite the notes task with a SQLAlchemy Note model.

    Note is a mapped class with __tablename__ = "notes", an int id primary key
    and a str text. save_and_list_notes_orm(url, texts) creates the table if
    needed, adds one Note per text in a Session, commits, and returns all notes
    as (id, text) tuples ordered by id, like exercise 1.

    The url looks like "sqlite:///notes_orm.db". Call engine.dispose() at the
    end so the database file is closed.
    """
    raise NotImplementedError("Your code here")
