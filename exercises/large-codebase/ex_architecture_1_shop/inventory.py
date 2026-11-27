"""Represent products and calculate inventory value."""

from dataclasses import dataclass

from .pricing import total


@dataclass(frozen=True)
class Product:
    name: str
    price: int


def inventory_value(products: list[Product]) -> int:
    return total(products)
