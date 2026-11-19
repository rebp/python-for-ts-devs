"""Lesson 31 · Files and data formats · exercise 2.

Check your work with: uv run course.py
"""


def csv_to_json(src: str, dst: str) -> None:
    """Convert people.csv (columns name, age) to people.json, turning ages into
    integers.

    csv_to_json(src, dst) reads the CSV file src and writes a JSON list like
    [{"name": "Ada", "age": 36}, ...] to dst.

    Hint: csv.DictReader gives you one dict per row; open the CSV with
    newline="".
    """
    raise NotImplementedError("Your code here")
