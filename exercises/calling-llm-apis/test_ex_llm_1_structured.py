"""Tests for exercise 12.3-1.

Edit: ex_llm_1_structured.py::summarize
"""

import json
from collections.abc import Callable

import httpx2
import pytest
from ex_llm_1_structured import Summary, summarize
from openai import APITimeoutError, OpenAI
from pydantic import ValidationError


def response_body(
    content: list[dict[str, object]], status: str = "completed"
) -> dict[str, object]:
    return {
        "id": "response-test",
        "object": "response",
        "created_at": 0,
        "status": status,
        "model": "gpt-5.5",
        "output": [
            {
                "id": "message-test",
                "type": "message",
                "role": "assistant",
                "status": "completed",
                "content": content,
            }
        ],
    }


def client_for(handler: Callable[[httpx2.Request], httpx2.Response]) -> OpenAI:
    return OpenAI(
        api_key="test-only",
        base_url="https://invalid.local/v1",
        max_retries=0,
        timeout=1.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(handler)),
    )


def test_sends_schema_and_parses_the_response() -> None:
    requests: list[dict[str, object]] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        assert request.url.path == "/v1/responses"
        requests.append(json.loads(request.content))
        return httpx2.Response(
            200,
            json=response_body(
                [
                    {
                        "type": "output_text",
                        "text": '{"topic":"Python","keywords":["async"]}',
                        "annotations": [],
                    }
                ]
            ),
        )

    with client_for(handler) as client:
        result = summarize(client, "Summarize this")
    assert result == Summary(topic="Python", keywords=["async"])
    assert requests[0]["input"] == "Summarize this"
    assert requests[0]["model"] == "gpt-5.5"
    text = requests[0]["text"]
    assert isinstance(text, dict)
    format_config = text["format"]
    assert isinstance(format_config, dict)
    assert format_config["type"] == "json_schema"


@pytest.mark.parametrize(
    "body",
    [
        response_body([{"type": "refusal", "refusal": "Cannot answer"}]),
        response_body(
            [
                {
                    "type": "output_text",
                    "text": '{"topic":"Python","keywords":[]}',
                    "annotations": [],
                }
            ],
            status="incomplete",
        ),
    ],
)
def test_refusal_and_incomplete_output_are_not_success(body: dict[str, object]) -> None:
    with (
        client_for(lambda _request: httpx2.Response(200, json=body)) as client,
        pytest.raises(ValueError),
    ):
        summarize(client, "Summarize this")


def test_timeout_is_not_swallowed() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        raise httpx2.ReadTimeout("simulated timeout", request=request)

    with client_for(handler) as client, pytest.raises(APITimeoutError):
        summarize(client, "Summarize this")


def test_invalid_structured_data_is_reported() -> None:
    body = response_body(
        [
            {
                "type": "output_text",
                "text": '{"topic":42,"keywords":[]}',
                "annotations": [],
            }
        ]
    )
    with (
        client_for(lambda _request: httpx2.Response(200, json=body)) as client,
        pytest.raises(ValidationError),
    ):
        summarize(client, "Summarize this")
