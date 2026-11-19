"""Reference solution for exercise 38-2 (Command-line tools with Typer)."""

import typer

app = typer.Typer()


@app.command()
def add(a: float, b: float) -> None:
    """Build a calculator with two subcommands, like git commit and git push:

        python ex38_2_calc.py add 2 3        prints 5
        python ex38_2_calc.py divide 7 2     prints 3.5
        python ex38_2_calc.py divide 1 0     prints an error, exit code 1

    - Format results with :g, so 5.0 prints as 5 and 2.75 as 2.75.
    - Dividing by zero prints "Error: can't divide by zero" to stderr
      (typer.echo(..., err=True)) and exits with code 1 (raise typer.Exit(code=1)).

    Register both functions with @app.command(). With two commands, Typer
    makes the command name required.
    """
    typer.echo(f"{a + b:g}")


@app.command()
def divide(a: float, b: float) -> None:
    """Print a / b, or an error and exit code 1 when b is 0."""
    if b == 0:
        typer.echo("Error: can't divide by zero", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"{a / b:g}")


if __name__ == "__main__":
    app()
