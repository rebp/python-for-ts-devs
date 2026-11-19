"""Reference solution for exercise 33-3 (Web APIs with FastAPI)."""

from ex33_2_todo_api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_and_list():
    response = client.post("/todos", json={"title": "Learn Python"})
    assert response.status_code == 201
    assert client.get("/todos").json()[-1]["title"] == "Learn Python"


def test_delete_unknown():
    assert client.delete("/todos/999").status_code == 404
