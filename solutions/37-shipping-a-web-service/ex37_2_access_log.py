"""Reference solution for exercise 37-2 (Shipping a web service)."""

import logging
import time
from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response

VERSION = "1.4.0"

logger = logging.getLogger("notes.access")

app = FastAPI()


@app.middleware("http")
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
    start = time.perf_counter()
    response = await call_next(request)
    elapsed_ms = (time.perf_counter() - start) * 1000
    logger.info(
        "%s %s %d %.1fms",
        request.method,
        request.url.path,
        response.status_code,
        elapsed_ms,
    )
    return response


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": VERSION}
