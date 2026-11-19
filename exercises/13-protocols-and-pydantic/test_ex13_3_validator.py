"""Tests for exercise 13-3 (Protocols and Pydantic).

Edit: ex13_3_validator.py::Product
"""

import pytest
from ex13_3_validator import Product
from pydantic import ValidationError


def test_positive_and_zero_prices_are_fine():
    assert Product(name="Lamp", price=19.9).price == 19.9
    assert Product(name="Sample", price=0).price == 0


def test_negative_price_is_rejected():
    with pytest.raises(ValidationError) as excinfo:
        Product(name="Lamp", price=-1)
    assert "price" in str(excinfo.value)


def test_rejected_through_model_validate_too():
    with pytest.raises(ValidationError):
        Product.model_validate({"name": "Lamp", "price": "-5"})
