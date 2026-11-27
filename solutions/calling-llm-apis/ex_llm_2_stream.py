"""Reference solution for exercise 12.3-2."""

from openai import AsyncOpenAI


async def collect_text(client: AsyncOpenAI, prompt: str) -> str:
    """Collect completed output and reject refusal or partial output."""
    stream = await client.responses.create(model="gpt-5.5", input=prompt, stream=True)
    parts: list[str] = []
    completed = False
    async with stream:
        async for event in stream:
            if event.type == "response.output_text.delta":
                parts.append(event.delta)
            elif event.type in ("response.refusal.delta", "response.refusal.done"):
                raise RuntimeError("model refused the request")
            elif event.type in ("response.failed", "response.incomplete"):
                raise RuntimeError("response failed or was incomplete")
            elif event.type == "response.completed":
                completed = event.response.status == "completed"
    text = "".join(parts)
    if not completed or not text:
        raise RuntimeError("stream ended without a completed text response")
    return text
