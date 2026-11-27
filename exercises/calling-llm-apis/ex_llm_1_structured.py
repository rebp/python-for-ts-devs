"""Lesson 12.3 · Calling LLM APIs · exercise 1.

Check your work with: uv run course.py 12.3-1
"""

from openai import OpenAI
from pydantic import BaseModel


class Summary(BaseModel):
    topic: str
    keywords: list[str]


def summarize(client: OpenAI, text: str) -> Summary:
    """Request a structured Summary with the Responses API.

    Use model ``gpt-5.5`` and the supplied client. Reject incomplete responses
    and responses with no parsed result. Let API and validation errors propagate.
    """
    raise NotImplementedError("Your code here")
