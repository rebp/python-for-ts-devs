"""Tests for exercise 19-3 (Modules and imports).

Edit: shop/__init__.py::
"""

import shop
import shop.pricing


def test_from_shop_import_apply_discount():
    from shop import apply_discount

    assert apply_discount(80, 25) == 60.0


def test_it_is_the_same_function():
    assert shop.apply_discount is shop.pricing.apply_discount
