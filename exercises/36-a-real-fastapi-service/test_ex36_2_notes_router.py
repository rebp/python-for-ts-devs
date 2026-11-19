"""Tests for exercise 36-2 (A real FastAPI service).

Edit: ex36_2_notes_router.py::list_notes
"""

import pytest
from ex36_2_notes_router import NotesStore, app, get_store
from fastapi.testclient import TestClient


@pytest.fixture
def store():
    """A fresh store for each test, injected in place of the real one."""
    fresh = NotesStore()
    app.dependency_overrides[get_store] = lambda: fresh
    yield fresh
    app.dependency_overrides.clear()


@pytest.fixture
def client(store):
    return TestClient(app)


def test_create_returns_201_and_the_note(client):
    response = client.post("/notes", json={"text": "Buy milk"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "text": "Buy milk"}


def test_create_uses_the_injected_store(client, store):
    client.post("/notes", json={"text": "Buy milk"})
    assert [note.text for note in store.all()] == ["Buy milk"]


def test_list_reads_from_the_injected_store(client, store):
    store.add("Written by the test")
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "text": "Written by the test"}]


def test_get_one(client, store):
    store.add("First")
    store.add("Second")
    assert client.get("/notes/2").json() == {"id": 2, "text": "Second"}


def test_get_unknown_is_404(client):
    assert client.get("/notes/99").status_code == 404


def test_text_is_required(client):
    assert client.post("/notes", json={}).status_code == 422
