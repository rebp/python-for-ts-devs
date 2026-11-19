"""Lesson 09 · Classes and methods · exercise 2.

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

    def __repr__(self) -> str:
        """Add a __repr__ so that print(acct) shows Account(owner='Ada', balance=50.0).

        Hint: inside an f-string, {value!r} uses the value's own repr, which adds
        quotes around strings.
        """
        raise NotImplementedError("Your code here")
