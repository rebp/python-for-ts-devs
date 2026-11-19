"""Tests for exercise 31-1 (Files and data formats).

Edit: ex31_1_json.py::filter_expensive
"""

import json

from ex31_1_json import filter_expensive

PRODUCTS = [
    {"name": "Lamp", "price": 19.9},
    {"name": "Desk", "price": 249},
    {"name": "Mug", "price": 20},
    {"name": "Chair", "price": 89.5},
]


def test_writes_only_expensive_products(tmp_path):
    src = tmp_path / "products.json"
    dst = tmp_path / "expensive.json"
    src.write_text(json.dumps(PRODUCTS), encoding="utf-8")
    filter_expensive(str(src), str(dst))
    assert json.loads(dst.read_text(encoding="utf-8")) == [
        {"name": "Desk", "price": 249},
        {"name": "Chair", "price": 89.5},
    ]


def test_nothing_expensive(tmp_path):
    src = tmp_path / "products.json"
    dst = tmp_path / "expensive.json"
    src.write_text(json.dumps([{"name": "Pen", "price": 1.5}]), encoding="utf-8")
    filter_expensive(str(src), str(dst))
    assert json.loads(dst.read_text(encoding="utf-8")) == []
