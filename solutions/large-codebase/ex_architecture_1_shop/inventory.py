"""Calculate inventory value."""

from .models import Product
from .pricing import total


def inventory_value(products: list[Product]) -> int:
    return total(products)
