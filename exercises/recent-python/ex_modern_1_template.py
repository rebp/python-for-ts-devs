"""Lesson 13.3 · What's new in Python 3.13–3.15 · exercise 1.

Check your work with: uv run course.py 13.3-1
"""

from string.templatelib import Template


def render_html(template: Template) -> str:
    """Render a trusted HTML-text template, escaping each interpolated value.

    Apply an interpolation's conversion and format specification before
    escaping it. Literal text is trusted. This is not a sanitizer for URLs,
    JavaScript, CSS, or arbitrary untrusted template literals.
    """
    raise NotImplementedError("Your code here")
