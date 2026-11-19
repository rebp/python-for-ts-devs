"""Prices and discounts for the shop (lesson 19). Reference solution."""


def apply_discount(price: float, percent: float) -> float:
    """Exercise 19-1: create the shop package from the diagram with an
    apply_discount(price, percent) function, and call it from main.py.
    """
    return round(price * (1 - percent / 100), 2)


def demo() -> None:
    """Exercise 19-2: add an if __name__ == "__main__": demo to pricing.py."""
    print("demo:", apply_discount(100, 10))


if __name__ == "__main__":
    demo()
