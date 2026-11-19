"""Prices and discounts for the shop (lesson 19).

Check your work with: uv run course.py
"""


def apply_discount(price: float, percent: float) -> float:
    """Exercise 19-1: create the shop package from the diagram with an
    apply_discount(price, percent) function, and call it from main.py.

    apply_discount(80, 25) returns 60.0. Round the result to 2 decimals.
    Then finish main.py so that `uv run main.py` (run it from this folder)
    prints the result of apply_discount(80, 25).
    """
    raise NotImplementedError("Your code here")


def demo() -> None:
    """Exercise 19-2: add an if __name__ == "__main__": demo to pricing.py.
    Run the file directly, then run main.py, and check when the demo prints.

    demo() prints "demo: 90.0", the result of apply_discount(100, 10).
    Below this function, call demo() only when the file is run directly:

        uv run python -m shop.pricing   -> prints the demo
        uv run main.py                  -> doesn't
    """
    raise NotImplementedError("Your code here")
