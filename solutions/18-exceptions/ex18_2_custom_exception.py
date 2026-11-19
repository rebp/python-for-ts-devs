"""Reference solution for exercise 18-2 (Exceptions)."""


class InsufficientFunds(Exception):
    def __init__(self, missing: float) -> None:
        super().__init__(f"missing {missing:.2f}")
        self.missing = missing


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
        if amount > self._balance:
            raise InsufficientFunds(amount - self._balance)
        self._balance -= amount
