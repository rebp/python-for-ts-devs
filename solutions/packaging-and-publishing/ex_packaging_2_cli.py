"""Reference solution for exercise 11.3-2."""

import argparse


def main(argv: list[str] | None = None) -> int:
    """Print a greeting for the supplied name."""
    parser = argparse.ArgumentParser(prog="greet")
    parser.add_argument("name")
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}!")
    return 0
