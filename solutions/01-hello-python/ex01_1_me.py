"""Reference solution for exercise 01-1 (Hello, Python)."""


def introduce(name: str, language: str) -> None:
    """Print your name on one line and your favorite language on the next.

    In the course this is a script, me.py. Here it's a function so a test can
    check it: introduce("Ada", "TypeScript") must print

        Ada
        TypeScript
    """
    print(name)
    print(language)
