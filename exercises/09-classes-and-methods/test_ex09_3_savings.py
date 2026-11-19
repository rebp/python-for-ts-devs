"""Tests for exercise 09-3 (Classes and methods).

Edit: ex09_3_savings.py::SavingsAccount
"""

import pytest
from ex09_3_savings import Account, SavingsAccount


def test_is_an_account():
    assert issubclass(SavingsAccount, Account)


def test_add_five_percent():
    savings = SavingsAccount("Ada")
    savings.deposit(100)
    savings.add_interest(0.05)
    assert savings.total == pytest.approx(105.0)


def test_interest_compounds():
    savings = SavingsAccount("Ada")
    savings.deposit(100)
    savings.add_interest(0.05)
    savings.add_interest(0.05)
    assert savings.total == pytest.approx(110.25)
