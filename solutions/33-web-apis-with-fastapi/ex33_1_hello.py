"""Reference solution for exercise 33-1 (Web APIs with FastAPI)."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    return {"id": item_id, "name": "Lamp"}


@app.post("/items", status_code=201)
def create_item(item: Item) -> Item:
    return item


@app.get("/hello/{name}")
def hello(name: str) -> dict[str, str]:
    """Add GET /hello/{name} that returns {"message": "Hello, Ada"}, then try it in
    /docs.

    Register this function as a route with @app.get(...). To try it in the
    browser, run the app from this folder:

        uv run fastapi dev ex33_1_hello.py

    and open http://127.0.0.1:8000/docs.
    """
    return {"message": f"Hello, {name}"}
