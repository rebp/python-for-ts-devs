"""A small function to test with generated inputs."""


def normalize(text: str) -> str:
    """Join whitespace-separated words with single spaces."""
    return " ".join(text.split())
