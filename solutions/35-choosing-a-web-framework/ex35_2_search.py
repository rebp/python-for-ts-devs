"""Reference solution for exercise 35-2 (Choosing a web framework)."""

from typing import Annotated

from fastapi import FastAPI, Query
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


@app.get("/items/search")
def search_items(
    q: str,
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
    max_price: float | None = None,
) -> list[Item]:
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

    Hint: any function parameter that isn't in the path is a query parameter.
    Use Annotated[int, Query(ge=1, le=50)] for the limits.
    """
    matches = [item for item in ITEMS if q.lower() in item.name.lower()]
    if max_price is not None:
        matches = [item for item in matches if item.price <= max_price]
    return matches[:limit]
