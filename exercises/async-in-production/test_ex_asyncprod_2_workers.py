"""Tests for exercise 8.2-2.

Edit: ex_asyncprod_2_workers.py::run_workers
"""

import asyncio

import pytest
from ex_asyncprod_2_workers import run_workers


def test_processes_every_item_with_bounded_workers() -> None:
    async def scenario() -> None:
        seen: list[str] = []
        active = 0
        peak = 0

        async def handle(item: str) -> None:
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            try:
                await asyncio.sleep(0)
                seen.append(item)
            finally:
                active -= 1

        await asyncio.wait_for(run_workers(["a", "b", "a", "c"], 2, handle), 2)
        assert sorted(seen) == ["a", "a", "b", "c"]
        assert 1 <= peak <= 2

    asyncio.run(scenario())


def test_empty_input_finishes() -> None:
    async def handle(_item: str) -> None:
        raise AssertionError("no items should be handled")

    asyncio.run(asyncio.wait_for(run_workers([], 1, handle), 2))


@pytest.mark.parametrize("worker_count", [0, -1])
def test_rejects_nonpositive_worker_count(worker_count: int) -> None:
    async def handle(_item: str) -> None:
        pass

    with pytest.raises(ValueError):
        asyncio.run(run_workers(["a"], worker_count, handle))


def test_handler_failure_cancels_other_workers() -> None:
    async def scenario() -> None:
        started = asyncio.Event()
        cleaned = asyncio.Event()

        async def handle(item: str) -> None:
            if item == "fail":
                await started.wait()
                raise RuntimeError("failed")
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                cleaned.set()

        with pytest.raises(ExceptionGroup) as error:
            await asyncio.wait_for(run_workers(["slow", "fail"], 2, handle), 2)
        assert any(isinstance(exc, RuntimeError) for exc in error.value.exceptions)
        assert cleaned.is_set()

    asyncio.run(scenario())
