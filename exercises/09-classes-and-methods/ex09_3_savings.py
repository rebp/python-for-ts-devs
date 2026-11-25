"""Lesson 09 · Classes and methods · exercise 3.

Check your work with: uv run course.py
"""


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount

    @property
    def total(self) -> float:
        return self._balance


class SavingsAccount:
    """Create SavingsAccount(Account) with an add_interest(rate) method, where 0.05
    means 5%.

    A SavingsAccount("Ada") with 100 deposited has 105.0 after add_interest(0.05).

    Reuse Account's total property and deposit method. There's no extra state,
    so you can inherit __init__ without redefining it.
    """

    # TODO: inherit from Account and add the add_interest(self, rate) method
