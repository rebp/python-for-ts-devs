"""Lesson 23 · Mocking and test doubles · exercise 1.

Test checkout() from ex23_checkout.py without a real payment gateway: pass it
a unittest.mock.Mock instead, the way you'd pass a jest.fn() object.

Write at least two tests:

- A successful payment: set gateway.charge.return_value to a transaction id,
  check what checkout(19.99, gateway) returns, and check that charge was
  called exactly once with the amount in cents (1999), using
  assert_called_once_with.
- A declined card: make charge raise PaymentDeclined with side_effect, and
  check that checkout returns "declined".

How it's checked: your tests must pass against ex23_checkout.py, and fail
against broken versions of it. Run them yourself with:

    uv run pytest exercises/23-mocking-and-test-doubles/ex23_1_checkout_tests.py

Check your work with: uv run course.py
"""

from unittest.mock import Mock  # noqa: F401  (delete this comment once you use Mock)

import pytest
from ex23_checkout import PaymentDeclined, checkout  # noqa: F401


def test_placeholder():
    pytest.fail("Replace this placeholder with your tests")
