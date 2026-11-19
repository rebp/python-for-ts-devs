"""Tests for exercise 33-1 (Web APIs with FastAPI).

Edit: ex33_1_hello.py::hello
"""

from ex33_1_hello import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_hello():
    response = client.get("/hello/Ada")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Ada"}


def test_hello_someone_else():
    assert client.get("/hello/Grace").json() == {"message": "Hello, Grace"}


def test_lesson_routes_still_work():
    assert client.get("/items/3").json() == {"id": 3, "name": "Lamp"}
