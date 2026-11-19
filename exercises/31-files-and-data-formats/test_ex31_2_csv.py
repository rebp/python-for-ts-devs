"""Tests for exercise 31-2 (Files and data formats).

Edit: ex31_2_csv.py::csv_to_json
"""

import json

from ex31_2_csv import csv_to_json


def test_converts_and_casts_ages(tmp_path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text('name,age\nAda,36\nGrace,85\n"Hopper, Grace",85\n', encoding="utf-8")
    csv_to_json(str(src), str(dst))
    assert json.loads(dst.read_text(encoding="utf-8")) == [
        {"name": "Ada", "age": 36},
        {"name": "Grace", "age": 85},
        {"name": "Hopper, Grace", "age": 85},
    ]
