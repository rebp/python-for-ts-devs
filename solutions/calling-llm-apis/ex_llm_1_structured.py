"""Reference solution for exercise 12.3-1."""

from openai import OpenAI
from pydantic import BaseModel


class Summary(BaseModel):
    topic: str
    keywords: list[str]


def summarize(client: OpenAI, text: str) -> Summary:
    """Parse a completed structured response or report its absence."""
    response = client.responses.parse(model="gpt-5.5", input=text, text_format=Summary)
    if response.status != "completed" or response.output_parsed is None:
        raise ValueError("response was incomplete or contained no parsed result")
    return response.output_parsed
