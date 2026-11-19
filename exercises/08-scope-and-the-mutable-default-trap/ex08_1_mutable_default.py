"""Lesson 08 · Scope and the mutable default trap · exercise 1.

Check your work with: uv run course.py
"""


def add_tag(tag, tags=[]):  # noqa: B006  the bug! (ruff spots it too)
    """Reproduce the add_tag bug from the example, then fix it with a None default.

    This function has the bug from the lesson. Call it twice without tags in the
    REPL to see it, then fix it:

        add_tag("a")  ->  ['a']
        add_tag("b")  ->  ['b']     (not ['a', 'b'])

    Passing your own list still appends to that list and returns it.
    """
    tags.append(tag)
    return tags
