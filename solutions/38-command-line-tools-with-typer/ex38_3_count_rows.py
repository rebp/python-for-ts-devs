"""Reference solution for exercise 38-3 (Command-line tools with Typer)."""

import csv
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def count_rows(
    path: Annotated[Path, typer.Argument(exists=True, dir_okay=False)],
    column: str | None = None,
) -> None:
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
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        headers = reader.fieldnames or []
    if column is None:
        typer.echo(f"{len(rows)} row" + ("" if len(rows) == 1 else "s"))
        return
    if column not in headers:
        typer.echo(f"Error: no column named {column}", err=True)
        raise typer.Exit(code=1)
    distinct = {row[column] for row in rows}
    typer.echo(f"{len(distinct)} distinct values in {column}")


if __name__ == "__main__":
    app()
