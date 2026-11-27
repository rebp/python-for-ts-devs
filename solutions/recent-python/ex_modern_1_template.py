"""Reference solution for exercise 13.3-1."""

from html import escape
from string.templatelib import Template, convert


def render_html(template: Template) -> str:
    """Escape interpolations for HTML text in a trusted template."""
    parts: list[str] = []
    for part in template:
        if isinstance(part, str):
            parts.append(part)
        else:
            value = convert(part.value, part.conversion)
            parts.append(escape(format(value, part.format_spec), quote=True))
    return "".join(parts)
