"""Reference solution for exercise 11-2 (Enums and match)."""


def handle(command: list[str]) -> str:
    """Write handle(command: list[str]) that returns "Going north" for
    ["go", "north"], "Bye" for ["quit"], and "Unknown command" for anything else.

    Any direction works: ["go", "west"] returns "Going west". Use match with
    sequence patterns.
    """
    match command:
        case ["go", direction]:
            return f"Going {direction}"
        case ["quit"]:
            return "Bye"
        case _:
            return "Unknown command"
