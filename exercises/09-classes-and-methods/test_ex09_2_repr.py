"""Tests for exercise 09-2 (Classes and methods).

Edit: ex09_2_repr.py::Account.__repr__
"""

from ex09_2_repr import Account


def test_repr_after_a_deposit():
    acct = Account("Ada")
    acct.deposit(50)
    assert repr(acct) == "Account(owner='Ada', balance=50.0)"


def test_print_uses_repr(capsys):
    acct = Account("Grace")
    print(acct)
    assert capsys.readouterr().out == "Account(owner='Grace', balance=0.0)\n"
