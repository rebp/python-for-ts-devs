"""Reference solution for exercise 23-1 (Mocking and test doubles)."""

from unittest.mock import Mock, create_autospec

from ex23_checkout import PaymentDeclined, PaymentGateway, checkout


def test_successful_payment():
    gateway = Mock()
    gateway.charge.return_value = "tx_123"

    assert checkout(19.99, gateway) == "paid tx_123"
    gateway.charge.assert_called_once_with(1999)


def test_declined_card():
    gateway = Mock()
    gateway.charge.side_effect = PaymentDeclined()

    assert checkout(19.99, gateway) == "declined"


def test_with_autospec():
    # create_autospec copies PaymentGateway's real methods and signatures, so
    # calling a method that doesn't exist, or with the wrong arguments, fails.
    gateway = create_autospec(PaymentGateway, instance=True)
    gateway.charge.return_value = "tx_456"

    assert checkout(5, gateway) == "paid tx_456"
    gateway.charge.assert_called_once_with(500)
