"""Tests for exercise 12.3-2.

Edit: ex_llm_2_stream.py::collect_text
"""

import asyncio
import json
from collections.abc import Sequence

import httpx2
import pytest
from ex_llm_2_stream import collect_text
from openai import AsyncOpenAI


def delta(text: str) -> dict[str, object]:
    return {
        "type": "response.output_text.delta",
        "delta": text,
        "item_id": "message-test",
        "output_index": 0,
        "content_index": 0,
        "sequence_number": 1,
    }


def completed() -> dict[str, object]:
    return {
        "type": "response.completed",
        "sequence_number": 2,
        "response": {
            "id": "response-test",
            "object": "response",
            "created_at": 0,
            "model": "gpt-5.5",
            "status": "completed",
            "output": [],
        },
    }


def make_client(events: Sequence[dict[str, object]]) -> AsyncOpenAI:
    payload = (
        "".join(f"data: {json.dumps(event)}\n\n" for event in events)
        + "data: [DONE]\n\n"
    )

    def handler(request: httpx2.Request) -> httpx2.Response:
        body = json.loads(request.content)
        assert request.url.path == "/v1/responses"
        assert body["stream"] is True
        assert body["model"] == "gpt-5.5"
        return httpx2.Response(
            200, headers={"content-type": "text/event-stream"}, text=payload
        )

    return AsyncOpenAI(
        api_key="test-only",
        base_url="https://invalid.local/v1",
        max_retries=0,
        http_client=httpx2.AsyncClient(transport=httpx2.MockTransport(handler)),
    )


def test_collects_text_only_after_completion() -> None:
    async def scenario() -> None:
        async with make_client([delta("Hello"), delta("!"), completed()]) as client:
            assert await collect_text(client, "Say hello") == "Hello!"

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "events",
    [
        [delta("partial")],
        [completed()],
        [delta(""), completed()],
        [{"type": "response.refusal.delta", "delta": "No", "sequence_number": 1}],
        [{"type": "response.refusal.done", "refusal": "No", "sequence_number": 1}],
        [
            {
                "type": "response.failed",
                "sequence_number": 1,
                "response": {
                    "id": "response-test",
                    "object": "response",
                    "created_at": 0,
                    "model": "gpt-5.5",
                    "status": "failed",
                    "output": [],
                },
            }
        ],
    ],
)
def test_does_not_return_partial_or_refused_output(
    events: list[dict[str, object]],
) -> None:
    async def scenario() -> None:
        async with make_client(events) as client:
            with pytest.raises(RuntimeError) as error:
                await collect_text(client, "Say hello")
            assert not isinstance(error.value, NotImplementedError)

    asyncio.run(scenario())
