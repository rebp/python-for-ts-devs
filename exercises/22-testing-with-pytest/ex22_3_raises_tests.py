"""Lesson 22 · Testing with pytest · exercise 3.

Test that withdrawing more than the balance raises an error, and check the
error message too.

Account.withdraw raises ValueError("insufficient funds"). Use pytest.raises
with match=. You can copy the account fixture from exercise 2.

How it's checked: your tests must pass against bank.py, and fail against
versions that don't raise, raise a different exception type, or use a
different message. Run them yourself with:

    uv run pytest exercises/22-testing-with-pytest/ex22_3_raises_tests.py

Check your work with: uv run course.py
"""

import pytest
from bank import Account  # noqa: F401  (delete this comment once you use Account)


def test_placeholder():
    pytest.fail("Replace this placeholder with your fixture and test")
