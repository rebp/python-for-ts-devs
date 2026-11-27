# Exercise 8.2-3: Reason about cancellation

A coroutine awaits `asyncio.to_thread(blocking_call)`, and its enclosing
`asyncio.timeout()` expires after the thread has started. Explain what happens
to the waiting coroutine and to the running thread. How would the blocking
function stop early?

Hint: cancelling an await does not safely terminate an operating-system thread.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/async-in-production/ex_asyncprod_3_cancellation.md`.
