"""Reference solution for exercise 31-2 (Files and data formats)."""

import csv
import json


def csv_to_json(src: str, dst: str) -> None:
    """Convert people.csv (columns name, age) to people.json, turning ages into
    integers.

    csv_to_json(src, dst) reads the CSV file src and writes a JSON list like
    [{"name": "Ada", "age": 36}, ...] to dst.

    Hint: csv.DictReader gives you one dict per row; open the CSV with
    newline="".
    """
    with open(src, newline="", encoding="utf-8") as f:
        people = [
            {"name": row["name"], "age": int(row["age"])} for row in csv.DictReader(f)
        ]

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(people, f, indent=2)
