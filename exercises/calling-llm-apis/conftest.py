"""Prevent real HTTP transports from being used by this lesson's tests."""

from typing import NoReturn

import httpx2
import pytest


@pytest.fixture(autouse=True)
def forbid_network(monkeypatch: pytest.MonkeyPatch) -> None:
    def deny_sync(_self: httpx2.HTTPTransport, _request: httpx2.Request) -> NoReturn:
        raise AssertionError("real network access is disabled")

    async def deny_async(
        _self: httpx2.AsyncHTTPTransport, _request: httpx2.Request
    ) -> NoReturn:
        raise AssertionError("real network access is disabled")

    monkeypatch.setattr(httpx2.HTTPTransport, "handle_request", deny_sync)
    monkeypatch.setattr(httpx2.AsyncHTTPTransport, "handle_async_request", deny_async)
