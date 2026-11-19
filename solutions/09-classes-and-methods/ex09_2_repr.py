"""Reference solution for exercise 09-2 (Classes and methods)."""


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
        return f"Account(owner={self.owner!r}, balance={self._balance})"
