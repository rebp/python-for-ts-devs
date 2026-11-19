"""Lesson 34 · Databases · exercise 1.

Check your work with: uv run course.py
"""


def save_and_list_notes(db_path: str, texts: list[str]) -> list[tuple[int, str]]:
    """Create a notes table with id and text, insert three notes, and print them all.

    save_and_list_notes(db_path, texts) connects to the SQLite file db_path,
    creates the table if it doesn't exist yet (id INTEGER PRIMARY KEY, text TEXT),
    inserts one note per text, commits, and returns every row as (id, text)
    tuples, ordered by id.

    Use ? placeholders for the values, never f-strings: a note like
    "Ada's list" must work.
    """
    raise NotImplementedError("Your code here")
