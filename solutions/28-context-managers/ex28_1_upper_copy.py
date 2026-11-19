"""Reference solution for exercise 28-1 (Context managers)."""


def upper_copy(src: str, dst: str) -> None:
    """Copy input.txt to output.txt in uppercase, using a single with statement
    for both files.

    upper_copy(src, dst) reads src and writes its uppercase version to dst.
    Open both files in one with statement, and use encoding="utf-8".
    """
    with (
        open(src, encoding="utf-8") as source,
        open(dst, "w", encoding="utf-8") as target,
    ):
        target.writelines(line.upper() for line in source)
