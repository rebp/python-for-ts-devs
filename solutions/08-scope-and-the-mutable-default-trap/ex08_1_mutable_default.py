"""Reference solution for exercise 08-1 (Scope and the mutable default trap)."""


def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    """Reproduce the add_tag bug from the example, then fix it with a None default.

    This function has the bug from the lesson. Call it twice without tags in the
    REPL to see it, then fix it:

        add_tag("a")  ->  ['a']
        add_tag("b")  ->  ['b']     (not ['a', 'b'])

    Passing your own list still appends to that list and returns it.
    """
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
