"""Tests for exercise 36-3 (A real FastAPI service).

Edit: ex36_3_error_handler.py::note_not_found_handler
"""

from ex36_3_error_handler import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_known_note():
    response = client.get("/notes/1")
    assert response.status_code == 200
    assert response.json() == {"text": "Buy milk"}


def test_unknown_note_is_404_with_error_body():
    response = client.get("/notes/7")
    assert response.status_code == 404
    assert response.json() == {"error": "note_not_found", "note_id": 7}


def test_handler_covers_every_route():
    response = client.get("/notes/42/shout")
    assert response.status_code == 404
    assert response.json() == {"error": "note_not_found", "note_id": 42}
