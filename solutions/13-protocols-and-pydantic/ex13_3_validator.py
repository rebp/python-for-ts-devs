"""Reference solution for exercise 13-3 (Protocols and Pydantic)."""

from pydantic import BaseModel, field_validator


class Product(BaseModel):
    """Add a validator to Product that rejects negative prices.

    Hint: use @field_validator("price") on a classmethod that returns the value
    or raises ValueError. A price of 0 is allowed.
    """

    name: str
    price: float

    @field_validator("price")
    @classmethod
    def price_not_negative(cls, value: float) -> float:
        if value < 0:
            raise ValueError("price must be 0 or more")
        return value
