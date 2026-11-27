"""Tests for exercise 8.2-1.

Edit: ex_asyncprod_1_bounded.py::bounded_map
"""

import asyncio

import pytest
from ex_asyncprod_1_bounded import bounded_map


def test_empty_input() -> None:
    async def work(value: int) -> int:
        return value * 2

    assert asyncio.run(bounded_map([], 2, work)) == []


def test_limits_concurrency_and_preserves_input_order() -> None:
    async def scenario() -> None:
        release = asyncio.Event()
        two_started = asyncio.Event()
        active = 0
        peak = 0

        async def work(value: int) -> int:
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            if active == 2:
                two_started.set()
            try:
                await release.wait()
                return value * 2
            finally:
                active -= 1

        task = asyncio.create_task(bounded_map([3, 1, 4], 2, work))
        await asyncio.sleep(0)
        if task.done():
            await task
        try:
            await asyncio.wait_for(two_started.wait(), timeout=2)
            assert peak == 2
        finally:
            release.set()
        assert await asyncio.wait_for(task, timeout=2) == [6, 2, 8]
        assert peak == 2

    asyncio.run(scenario())


@pytest.mark.parametrize("limit", [0, -1])
def test_rejects_nonpositive_limit(limit: int) -> None:
    async def work(value: int) -> int:
        return value

    with pytest.raises(ValueError):
        asyncio.run(bounded_map([1], limit, work))


def test_failure_cancels_a_running_sibling() -> None:
    async def scenario() -> None:
        started = asyncio.Event()
        cleaned = asyncio.Event()

        async def work(value: int) -> int:
            if value == 0:
                await started.wait()
                raise ValueError("failed")
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                cleaned.set()
            return value

        with pytest.raises(ExceptionGroup) as error:
            await asyncio.wait_for(bounded_map([1, 0], 2, work), timeout=2)
        assert any(isinstance(exc, ValueError) for exc in error.value.exceptions)
        assert cleaned.is_set()

    asyncio.run(scenario())
