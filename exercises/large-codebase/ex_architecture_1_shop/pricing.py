"""Calculate prices."""

from .inventory import Product


def total(products: list[Product]) -> int:
    return sum(product.price for product in products)
