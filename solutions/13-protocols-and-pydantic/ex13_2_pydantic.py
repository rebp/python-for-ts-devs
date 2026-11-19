"""Reference solution for exercise 13-2 (Protocols and Pydantic)."""

from pydantic import BaseModel, ValidationError


class Product(BaseModel):
    name: str
    price: float
    tags: list[str] = []  # safe in Pydantic: each instance gets its own copy


def load_product(data: dict) -> Product | None:
    """Create a Pydantic Product with name, price and tags (default empty). Validate
    one good dict and one with "price": "cheap", and print the error.

    load_product(data) validates data with Product.model_validate. When the data
    is valid it returns the Product. When it isn't, it prints the
    ValidationError (import it from pydantic) and returns None.
    """
    try:
        return Product.model_validate(data)
    except ValidationError as err:
        print(err)
        return None
