"""The Account class from lessons 09 and 18. Exercises 22-2 and 22-3 test it."""


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def total(self) -> float:
        return self._balance
