"""Tests for exercise 13-2 (Protocols and Pydantic).

Edit: ex13_2_pydantic.py::load_product
"""

from ex13_2_pydantic import Product, load_product


def test_valid_product_converts_the_price():
    product = load_product({"name": "Lamp", "price": "19.9"})
    assert isinstance(product, Product)
    assert product.name == "Lamp"
    assert product.price == 19.9
    assert product.tags == []


def test_tags_are_not_shared():
    first = Product(name="Lamp", price=1)
    second = Product(name="Desk", price=2)
    first.tags.append("light")
    assert second.tags == []


def test_invalid_price_prints_the_error(capsys):
    assert load_product({"name": "Lamp", "price": "cheap"}) is None
    assert "price" in capsys.readouterr().out


def test_missing_name_is_invalid(capsys):
    assert load_product({"price": 3}) is None
    assert "name" in capsys.readouterr().out
