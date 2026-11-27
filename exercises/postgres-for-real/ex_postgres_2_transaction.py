"""Lesson 10.3 · Postgres for real · exercise 2.

Check your work with: uv run course.py 10.3-2
"""

from collections.abc import Awaitable, Callable

from sqlalchemy.ext.asyncio import AsyncSession


async def in_transaction[T](
    session: AsyncSession, operation: Callable[[AsyncSession], Awaitable[T]]
) -> T:
    """Run an operation inside one session transaction and return its result.

    Let the transaction context commit on success and roll back on error.
    Do not swallow the operation's exception.
    """
    raise NotImplementedError("Your code here")
