"""Reference solution for exercise 22-3 (Testing with pytest)."""

import pytest
from bank import Account


@pytest.fixture
def account() -> Account:
    acct = Account("Ada")
    acct.deposit(100)
    return acct


def test_withdraw_too_much(account):
    with pytest.raises(ValueError, match="insufficient"):
        account.withdraw(1000)
