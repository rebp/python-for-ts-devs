"""Tests for exercise 34-2 (Databases).

Edit: ex34_2_transaction.py::transfer
"""

import pytest
from ex34_2_transaction import balances, create_bank, transfer


def test_transfer_moves_money():
    conn = create_bank()
    transfer(conn, "ada", "linus", 30)
    assert balances(conn) == {"ada": 70, "linus": 30}


def test_failed_transfer_changes_nothing():
    conn = create_bank()
    with pytest.raises(RuntimeError):
        transfer(conn, "ada", "linus", 50, fail_midway=True)
    assert balances(conn) == {"ada": 100, "linus": 0}


def test_a_later_transfer_still_works():
    conn = create_bank()
    with pytest.raises(RuntimeError):
        transfer(conn, "ada", "linus", 50, fail_midway=True)
    transfer(conn, "ada", "linus", 10)
    assert balances(conn) == {"ada": 90, "linus": 10}
