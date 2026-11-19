"""Reference solution for exercise 34-2 (Databases)."""

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
    with conn:
        conn.execute(
            "UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender)
        )
        if fail_midway:
            raise RuntimeError("crash in the middle")
        conn.execute(
            "UPDATE accounts SET balance = balance + ? WHERE name = ?",
            (amount, receiver),
        )


if __name__ == "__main__":
    bank = create_bank()
    try:
        transfer(bank, "ada", "linus", 50, fail_midway=True)
    except RuntimeError:
        pass
    print(balances(bank))  # {'ada': 100, 'linus': 0}
