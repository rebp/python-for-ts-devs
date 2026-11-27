"""Lesson 12.3 · Calling LLM APIs · exercise 2.

Check your work with: uv run course.py 12.3-2
"""

from openai import AsyncOpenAI


async def collect_text(client: AsyncOpenAI, prompt: str) -> str:
    """Collect streamed text from a completed Responses API request.

    Use model ``gpt-5.5`` and close the stream. Raise RuntimeError for a
    refusal, a failed or incomplete response, a stream ending before
    completion, or a completed response with no text. Let SDK errors propagate.
    """
    raise NotImplementedError("Your code here")
