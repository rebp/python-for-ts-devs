"""Reference solution for exercise 09-3 (Classes and methods)."""


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount

    @property
    def total(self) -> float:
        return self._balance


class SavingsAccount(Account):
    """Create SavingsAccount(Account) with an add_interest(rate) method, where 0.05
    means 5%.

    A SavingsAccount("Ada") with 100 deposited has 105.0 after add_interest(0.05).
    """

    def add_interest(self, rate: float) -> None:
        self.deposit(self.total * rate)
