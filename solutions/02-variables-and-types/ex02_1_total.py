"""Reference solution for exercise 02-1 (Variables and types)."""


def order_line(name: str, price: float, quantity: int) -> str:
    """Create variables for a product name, a price and a quantity. Print the total
    with exactly two decimals.

    Here the three values arrive as parameters, and you return the text:
    order_line("Desk lamp", 24.5, 3) returns "Desk lamp: 73.50".

    Hint: inside an f-string, {value:.2f} formats a float with two decimals.
    """
    total = price * quantity
    return f"{name}: {total:.2f}"
