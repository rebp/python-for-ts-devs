"""Reference solution for exercise 22-2 (Testing with pytest)."""

import pytest
from bank import Account


@pytest.fixture
def account() -> Account:
    acct = Account("Ada")
    acct.deposit(100)
    return acct


def test_deposit(account):
    account.deposit(50)
    assert account.total == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.total == 70
