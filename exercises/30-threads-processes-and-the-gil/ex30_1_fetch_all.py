"""Lesson 30 · Threads, processes and the GIL · exercise 1.

Check your work with: uv run course.py
"""

import time


def fetch(url: str) -> str:
    """A slow, blocking download (it just sleeps). Don't change it."""
    time.sleep(0.3)
    return f"<page {url}>"


def fetch_all(urls: list[str]) -> list[str]:
    """Download every URL with fetch(), in parallel threads, and return the
    pages in the same order as urls.

    fetch() blocks for 0.3 seconds, so six URLs one after the other take
    1.8 seconds. With a thread pool they overlap and take about 0.3 seconds:
    while one thread sleeps (or waits for the network), the others run.

    Use concurrent.futures.ThreadPoolExecutor in a with block, and pool.map,
    which returns results in input order, like Promise.all.
    An empty list returns [].
    """
    raise NotImplementedError("Your code here")
