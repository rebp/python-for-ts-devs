"""Reference solution for exercise 06-2 (Mutable and immutable)."""

import copy


def deep_copy_with_tag(original: dict, tag: str) -> dict:
    """Repeat the task with copy.deepcopy and confirm the original no longer changes.

    deep_copy_with_tag(original, tag) works like exercise 1, but the original
    must stay exactly as it was.
    """
    deep = copy.deepcopy(original)
    deep["tags"].append(tag)
    return deep
