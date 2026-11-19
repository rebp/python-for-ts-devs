"""Lesson 13 · Protocols and Pydantic · exercise 2.

Check your work with: uv run course.py
"""

from pydantic import BaseModel


class Product(BaseModel):
    """TODO: name (str), price (float) and tags (list of str, empty by default)."""


def load_product(data: dict) -> Product | None:
    """Create a Pydantic Product with name, price and tags (default empty). Validate
    one good dict and one with "price": "cheap", and print the error.

    load_product(data) validates data with Product.model_validate. When the data
    is valid it returns the Product. When it isn't, it prints the
    ValidationError (import it from pydantic) and returns None.
    """
    raise NotImplementedError("Your code here")
