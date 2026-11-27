"""Reference solution for exercise 10.3-2."""

from collections.abc import Awaitable, Callable

from sqlalchemy.ext.asyncio import AsyncSession


async def in_transaction[T](
    session: AsyncSession, operation: Callable[[AsyncSession], Awaitable[T]]
) -> T:
    """Commit on success and roll back on failure."""
    async with session.begin():
        return await operation(session)
