"""Reference solution for exercise 04-2 (Control flow)."""


def print_ranking(scores: list[int]) -> None:
    """Given scores = [72, 95, 48, 88], print each score with its position,
    starting at 1: "1. 72", "2. 95"…

    print_ranking([72, 95, 48, 88]) prints four lines, starting with "1. 72".

    Hint: enumerate() takes a start argument.
    """
    for position, score in enumerate(scores, start=1):
        print(f"{position}. {score}")
