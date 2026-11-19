"""Tests for exercise 33-2 (Web APIs with FastAPI).

Edit: ex33_2_todo_api.py::create_todo
"""

from ex33_2_todo_api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def create(title):
    response = client.post("/todos", json={"title": title})
    assert response.status_code == 201
    return response.json()


def test_create_returns_the_todo():
    todo = create("Learn Python")
    assert todo["title"] == "Learn Python"
    assert isinstance(todo["id"], int)


def test_list_includes_created_todos():
    todo = create("Write tests")
    response = client.get("/todos")
    assert response.status_code == 200
    assert todo in response.json()


def test_ids_are_unique():
    assert create("one")["id"] != create("two")["id"]


def test_delete():
    todo = create("Temporary")
    assert client.delete(f"/todos/{todo['id']}").status_code == 204
    assert todo not in client.get("/todos").json()
    assert client.delete(f"/todos/{todo['id']}").status_code == 404


def test_delete_unknown_is_404():
    assert client.delete("/todos/999999").status_code == 404


def test_title_is_required():
    assert client.post("/todos", json={}).status_code == 422
