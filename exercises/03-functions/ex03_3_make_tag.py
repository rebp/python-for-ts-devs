"""Lesson 03 · Functions · exercise 3.

Check your work with: uv run course.py
"""


def make_tag(tag: str, text: str, **attrs: str) -> str:
    """Write make_tag(tag, text, **attrs) so that make_tag("a", "Home", href="/")
    returns <a href="/">Home</a>.

    Attributes appear in the order they were passed, each as key="value" with a
    space before it. Without attributes, make_tag("p", "Hi") returns <p>Hi</p>.

    Hint: loop over attrs.items() to build each key="value" pair, then join them.
    """
    raise NotImplementedError("Your code here")
