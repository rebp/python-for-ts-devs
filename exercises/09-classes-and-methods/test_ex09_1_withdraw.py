"""Tests for exercise 09-1 (Classes and methods).

Edit: ex09_1_withdraw.py::Account.withdraw
"""

import pytest
from ex09_1_withdraw import Account


def make_account(balance: float) -> Account:
    acct = Account("Ada")
    acct.deposit(balance)
    return acct


def test_withdraw_reduces_the_balance():
    acct = make_account(50)
    acct.withdraw(20)
    assert acct.total == 30


def test_withdraw_everything():
    acct = make_account(50)
    acct.withdraw(50)
    assert acct.total == 0


def test_too_much_raises_value_error():
    acct = make_account(50)
    with pytest.raises(ValueError):
        acct.withdraw(100)
    assert acct.total == 50, "a failed withdrawal must not change the balance"
