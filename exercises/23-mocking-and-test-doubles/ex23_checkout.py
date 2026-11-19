"""The checkout code that exercise 23-1 tests. You don't need to change it."""


class PaymentDeclined(Exception):
    """Raised by a payment gateway when the card is declined."""


class PaymentGateway:
    """The real gateway talks to a payment provider over the network."""

    def charge(self, amount_cents: int) -> str:
        """Charge the card and return a transaction id."""
        raise RuntimeError("the real gateway needs the network: use a mock in tests")


def checkout(total: float, gateway: PaymentGateway) -> str:
    """Charge `total` euros through the gateway, converted to cents.

    Returns "paid <transaction id>", or "declined" when the gateway raises
    PaymentDeclined.
    """
    try:
        transaction_id = gateway.charge(round(total * 100))
    except PaymentDeclined:
        return "declined"
    return f"paid {transaction_id}"
