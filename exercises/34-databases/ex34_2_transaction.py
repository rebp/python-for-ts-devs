"""Lesson 34 · Databases · exercise 2.

Check your work with: uv run course.py
"""

import sqlite3


def create_bank() -> sqlite3.Connection:
    """An in-memory database with two accounts: ada (100) and linus (0)."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance INT)")
    with conn:
        conn.executemany(
            "INSERT INTO accounts VALUES (?, ?)", [("ada", 100), ("linus", 0)]
        )
    return conn


def balances(conn: sqlite3.Connection) -> dict[str, int]:
    return dict(conn.execute("SELECT name, balance FROM accounts"))


def transfer(
    conn: sqlite3.Connection,
    sender: str,
    receiver: str,
    amount: int,
    fail_midway: bool = False,
) -> None:
    """Transfer money between two accounts inside one transaction. Raise an error
    between the debit and the credit and confirm that neither change was saved.

    transfer(conn, sender, receiver, amount) subtracts amount from sender and
    adds it to receiver, both inside one `with conn:` block. With
    fail_midway=True it raises RuntimeError("crash in the middle") right after
    the debit; the transaction must then leave both balances unchanged.

    create_bank() and balances() are ready for you to try it.
    """
    raise NotImplementedError("Your code here")
