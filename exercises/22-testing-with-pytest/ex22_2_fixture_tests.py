"""Lesson 22 · Testing with pytest · exercise 2.

Write an account fixture that returns an Account with 100 deposited, and two
tests that use it.

Account is imported from bank.py in this folder. Name the fixture `account`.
Write one test for deposit and one for withdraw, and check the balance with
`account.total` in each.

How it's checked: your tests must pass against bank.py, and fail against
broken versions of it. Run them yourself with:

    uv run pytest exercises/22-testing-with-pytest/ex22_2_fixture_tests.py

Check your work with: uv run course.py
"""

import pytest
from bank import Account  # noqa: F401  (delete this comment once you use Account)


def test_placeholder():
    pytest.fail("Replace this placeholder with your fixture and tests")
