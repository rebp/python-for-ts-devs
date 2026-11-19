"""Reference solution for exercise 06-1 (Mutable and immutable)."""


def shallow_copy_with_tag(original: dict, tag: str) -> dict:
    """Make a shallow copy of {"title": "Draft", "tags": ["a"]}, append "b" to the
    copy's tags, and print the original. Explain what you see.

    shallow_copy_with_tag(original, tag) makes a shallow copy of the dict,
    appends tag to the copy's "tags" list and returns the copy. The tests then
    look at the original: it changed too. Why?
    """
    shallow = original.copy()
    shallow["tags"].append(tag)
    # The original changes too: a shallow copy only duplicates the outer dict,
    # so both dicts point to the same tags list.
    return shallow
