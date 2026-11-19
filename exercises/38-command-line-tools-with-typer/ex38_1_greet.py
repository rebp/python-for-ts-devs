"""Lesson 38 · Command-line tools with Typer · exercise 1.

Check your work with: uv run course.py
"""

import typer

app = typer.Typer()


def greet(name: str, shout: bool = False, times: int = 1) -> None:
    """Turn greet into a command: python ex38_1_greet.py Ada --shout --times 2

    - NAME is a required argument, and the command prints "Hello, Ada!".
    - --shout prints it in capitals: "HELLO, ADA!".
    - --times N prints it N times, one per line (1 by default).

    Register the function with @app.command() and print with typer.echo().
    The type hints and defaults are all Typer needs: a parameter without a
    default becomes an argument, one with a default becomes an --option, and a
    bool becomes a flag. Typer also generates --help and rejects --times abc.
    """
    raise NotImplementedError("Your code here")


if __name__ == "__main__":
    app()
