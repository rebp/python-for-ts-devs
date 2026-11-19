"""Reference solution for exercise 34-1 (Databases)."""

import sqlite3


def save_and_list_notes(db_path: str, texts: list[str]) -> list[tuple[int, str]]:
    """Create a notes table with id and text, insert three notes, and print them all.

    save_and_list_notes(db_path, texts) connects to the SQLite file db_path,
    creates the table if it doesn't exist yet (id INTEGER PRIMARY KEY, text TEXT),
    inserts one note per text, commits, and returns every row as (id, text)
    tuples, ordered by id.

    Use ? placeholders for the values, never f-strings: a note like
    "Ada's list" must work.
    """
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)"
        )
        with conn:
            conn.executemany(
                "INSERT INTO notes (text) VALUES (?)", [(text,) for text in texts]
            )
        return conn.execute("SELECT id, text FROM notes ORDER BY id").fetchall()
    finally:
        conn.close()
