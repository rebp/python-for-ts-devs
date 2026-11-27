"""Reference solution for exercise 13.3-2."""

import annotationlib
from collections.abc import Callable


def unresolved_annotations(function: Callable[..., object]) -> list[str]:
    """Find top-level annotations that are unresolved forward references."""
    annotations = annotationlib.get_annotations(
        function, format=annotationlib.Format.FORWARDREF
    )
    return [
        name
        for name, value in annotations.items()
        if name != "return" and isinstance(value, annotationlib.ForwardRef)
    ]
