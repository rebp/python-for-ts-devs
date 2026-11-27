"""Tests for exercise 13.2-2.

Edit: ex_architecture_2_checkout.py::checkout
"""

import pytest
from ex_architecture_2_checkout import checkout


def test_uses_the_supplied_storage_boundary() -> None:
    saved: list[int] = []
    assert checkout([125, 75], saved.append) == 200
    assert saved == [200]


@pytest.mark.parametrize("prices", [[], [10, -1]])
def test_invalid_input_does_not_save(prices: list[int]) -> None:
    saved: list[int] = []
    with pytest.raises(ValueError):
        checkout(prices, saved.append)
    assert saved == []


def test_storage_errors_are_not_hidden() -> None:
    def fail(_total: int) -> None:
        raise OSError("storage unavailable")

    with pytest.raises(OSError, match="storage unavailable"):
        checkout([1], fail)
