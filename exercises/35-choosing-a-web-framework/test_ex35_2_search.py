"""Tests for exercise 35-2 (Choosing a web framework).

Edit: ex35_2_search.py::search_items
"""

from ex35_2_search import app
from fastapi.testclient import TestClient

client = TestClient(app)


def names(params):
    response = client.get("/items/search", params=params)
    assert response.status_code == 200, response.text
    return [item["name"] for item in response.json()]


def test_matches_names_containing_q():
    assert names({"q": "lamp"}) == ["Desk lamp", "Floor lamp", "Lamp shade"]


def test_ignores_case():
    assert names({"q": "DESK"}) == ["Desk lamp", "Desk"]


def test_limit():
    assert names({"q": "lamp", "limit": 2}) == ["Desk lamp", "Floor lamp"]


def test_max_price():
    assert names({"q": "lamp", "max_price": 30}) == ["Desk lamp", "Lamp shade"]


def test_no_matches_is_an_empty_list():
    assert names({"q": "sofa"}) == []


def test_q_is_required():
    assert client.get("/items/search").status_code == 422


def test_limit_must_be_between_1_and_50():
    assert client.get("/items/search", params={"q": "a", "limit": 0}).status_code == 422
    assert (
        client.get("/items/search", params={"q": "a", "limit": 51}).status_code == 422
    )
    assert (
        client.get("/items/search", params={"q": "a", "limit": 50}).status_code == 200
    )


def test_query_values_are_validated():
    response = client.get("/items/search", params={"q": "a", "max_price": "cheap"})
    assert response.status_code == 422
