"""Lesson 13 · Protocols and Pydantic · exercise 3.

Check your work with: uv run course.py
"""

from pydantic import BaseModel


class Product(BaseModel):
    """Add a validator to Product that rejects negative prices.

    Hint: use @field_validator("price") on a classmethod that returns the value
    or raises ValueError. A price of 0 is allowed.
    """

    name: str
    price: float
