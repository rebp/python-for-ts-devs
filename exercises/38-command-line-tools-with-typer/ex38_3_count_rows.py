"""Lesson 38 · Command-line tools with Typer · exercise 3.

Check your work with: uv run course.py
"""

from pathlib import Path

import typer

app = typer.Typer()


def count_rows(path: Path, column: str | None = None) -> None:
    """Write a command that counts the rows of a CSV file with a header line:

        python ex38_3_count_rows.py orders.csv                  prints "3 rows"
        python ex38_3_count_rows.py orders.csv --column region  prints "2 distinct values in region"

    - The header line isn't a row. Print "1 row" for a single row.
    - --column NAME prints how many different values that column has instead.
      An unknown column prints "Error: no column named NAME" to stderr and
      exits with code 1.
    - A path that doesn't exist, or is a folder, is rejected by Typer before
      your code runs (exit code 2). Declare the argument as
      Annotated[Path, typer.Argument(exists=True, dir_okay=False)].

    Hint: csv.DictReader (lesson 31) gives you each row as a dict.
    """
    raise NotImplementedError("Your code here")


if __name__ == "__main__":
    app()
