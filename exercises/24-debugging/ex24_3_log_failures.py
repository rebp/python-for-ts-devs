"""Lesson 24 · Debugging · exercise 3.

Check your work with: uv run course.py
"""

import logging
from collections.abc import Callable

logger = logging.getLogger("jobs")


def run_job(name: str, job: Callable[[], object]) -> bool:
    """Run job() and report whether it succeeded, logging any failure with its
    full traceback, the way a worker or a web service should.

    - If job() returns, return True and log nothing.
    - If job() raises an Exception, log it on `logger` with
      logger.exception("job %s failed", name) and return False. The program
      keeps going, and the log contains the whole traceback.
    - Don't catch BaseException: KeyboardInterrupt and SystemExit must still
      stop the program.

    logger.exception() is logger.error() plus the current traceback, so call it
    inside the except block. It's the Python version of console.error(err)
    that keeps err.stack.
    """
    raise NotImplementedError("Your code here")
