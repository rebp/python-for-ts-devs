"""Tests for exercise 36-1 (A real FastAPI service).

Edit: ex36_1_api_key.py::require_api_key
"""

from ex36_1_api_key import API_KEY, app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_public_needs_no_key():
    assert client.get("/public").status_code == 200


def test_private_without_key_is_401():
    assert client.get("/private").status_code == 401


def test_private_with_wrong_key_is_401():
    assert client.get("/private", headers={"X-API-Key": "guess"}).status_code == 401


def test_private_with_right_key():
    response = client.get("/private", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert response.json() == {"message": "you have the key"}


def test_header_name_is_case_insensitive():
    assert client.get("/private", headers={"x-api-key": API_KEY}).status_code == 200
