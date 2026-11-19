"""Tests for exercise 18-2 (Exceptions).

Edit: ex18_2_custom_exception.py::Account.withdraw
"""

import pytest
from ex18_2_custom_exception import Account, InsufficientFunds


def make_account() -> Account:
    acct = Account("Ada")
    acct.deposit(50)
    return acct


def test_is_an_exception():
    assert issubclass(InsufficientFunds, Exception)


def test_withdraw_within_balance():
    acct = make_account()
    acct.withdraw(30)
    assert acct.total == 20


def test_raises_with_the_missing_amount():
    acct = make_account()
    with pytest.raises(InsufficientFunds) as excinfo:
        acct.withdraw(70)
    assert excinfo.value.missing == 20
    assert str(excinfo.value) == "missing 20.00"
    assert acct.total == 50
