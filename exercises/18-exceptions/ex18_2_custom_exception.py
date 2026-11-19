"""Lesson 18 · Exceptions · exercise 2.

Check your work with: uv run course.py
"""


class InsufficientFunds(Exception):
    """TODO: take the missing amount, store it as self.missing, and set the message."""


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount

    @property
    def total(self) -> float:
        return self._balance

    def withdraw(self, amount: float) -> None:
        """Create an InsufficientFunds exception that stores the missing amount, and
        raise it from Account.withdraw.

        With 50 in the account, withdraw(70) raises InsufficientFunds whose
        .missing is 20 and whose message (str(err)) is "missing 20.00".
        """
        raise NotImplementedError("Your code here")
