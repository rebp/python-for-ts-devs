"""Reference solution for exercise 03-3 (Functions)."""


def make_tag(tag: str, text: str, **attrs: str) -> str:
    """Write make_tag(tag, text, **attrs) so that make_tag("a", "Home", href="/")
    returns <a href="/">Home</a>.

    Attributes appear in the order they were passed, each as key="value" with a
    space before it. Without attributes, make_tag("p", "Hi") returns <p>Hi</p>.

    Hint: loop over attrs.items() to build each key="value" pair, then join them.
    """
    attr_text = "".join(f' {key}="{value}"' for key, value in attrs.items())
    return f"<{tag}{attr_text}>{text}</{tag}>"
