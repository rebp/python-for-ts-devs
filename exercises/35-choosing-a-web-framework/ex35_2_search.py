"""Lesson 35 · Choosing a web framework · exercise 2.

Check your work with: uv run course.py
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


ITEMS = [
    Item(name="Desk lamp", price=24.5),
    Item(name="Floor lamp", price=89.0),
    Item(name="Lamp shade", price=12.0),
    Item(name="Desk", price=150.0),
    Item(name="Chair", price=75.0),
]


def search_items(q: str) -> list[Item]:
    """Translate this Express handler into a FastAPI route:

        app.get("/items/search", (req, res) => {
          const q = String(req.query.q ?? "");
          const limit = Number(req.query.limit ?? 10);
          const maxPrice = req.query.max_price ? Number(req.query.max_price) : undefined;
          ...
        });

    GET /items/search?q=lamp&limit=2&max_price=50 returns the ITEMS whose name
    contains q (ignoring case), cheaper than or equal to max_price when it's
    given, and at most limit of them, in their original order.

    - q is required: without it FastAPI answers 422.
    - limit defaults to 10 and must be between 1 and 50 (422 otherwise).
    - max_price is optional.

    Register the function with @app.get and add the limit and max_price
    parameters.

    Hint: any function parameter that isn't in the path is a query parameter.
    Use Annotated[int, Query(ge=1, le=50)] for the limits.
    """
    raise NotImplementedError("Your code here")
