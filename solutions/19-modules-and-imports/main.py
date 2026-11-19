"""Exercise 19-1, second half: import apply_discount and print apply_discount(80, 25)."""

from shop import (
    apply_discount,  # works after exercise 19-3; before that: from shop.pricing import ...
)

print(apply_discount(80, 25))
