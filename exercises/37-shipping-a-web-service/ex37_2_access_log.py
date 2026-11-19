"""Lesson 37 · Shipping a web service · exercise 2.

Check your work with: uv run course.py
"""

import logging
from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response

VERSION = "1.4.0"

logger = logging.getLogger("notes.access")

app = FastAPI()


async def log_requests(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Add an access log and a health check to the service.

    1. Register this function with @app.middleware("http"). For every request,
       await call_next(request) to get the response, then log one INFO line on
       `logger` in this format and return the response:

           GET /health 200 1.3ms

       That's the method, the path, the status code and the time in
       milliseconds with one decimal. Use time.perf_counter() for the timing.

    2. Add GET /health that returns {"status": "ok", "version": VERSION}, the
       endpoint a load balancer or Kubernetes polls.

    Hint: log with placeholders, logger.info("%s %s %d %.1fms", ...), not with
    an f-string, so the message is only built when the line is really written.
    """
    raise NotImplementedError("Your code here")
