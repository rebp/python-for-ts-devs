"""Tests for exercise 10.3-2.

Edit: ex_postgres_2_transaction.py::in_transaction
"""

import asyncio
from unittest.mock import MagicMock

import pytest
from ex_postgres_2_transaction import in_transaction
from sqlalchemy.ext.asyncio import AsyncSession


def test_transaction_exits_normally_after_the_operation() -> None:
    session = MagicMock(spec=AsyncSession)

    async def operation(received: AsyncSession) -> int:
        assert received is session
        return 42

    assert asyncio.run(in_transaction(session, operation)) == 42
    session.begin.assert_called_once_with()
    session.begin.return_value.__aenter__.assert_awaited_once()
    session.begin.return_value.__aexit__.assert_awaited_once_with(None, None, None)


def test_transaction_sees_and_propagates_the_error() -> None:
    session = MagicMock(spec=AsyncSession)

    async def operation(_session: AsyncSession) -> int:
        raise ValueError("invalid")

    with pytest.raises(ValueError, match="invalid"):
        asyncio.run(in_transaction(session, operation))
    args = session.begin.return_value.__aexit__.await_args.args
    assert args[0] is ValueError
    assert isinstance(args[1], ValueError)
