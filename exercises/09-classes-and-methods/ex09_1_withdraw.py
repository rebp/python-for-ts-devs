"""Lesson 09 · Classes and methods · exercise 1.

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

    def withdraw(self, amount: float) -> None:
        """Add withdraw(amount) to Account. It raises ValueError when the balance is
        too low.

        Withdrawing exactly the whole balance is fine and leaves 0. A failed
        withdrawal leaves the balance unchanged.
        """
        raise NotImplementedError("Your code here")
