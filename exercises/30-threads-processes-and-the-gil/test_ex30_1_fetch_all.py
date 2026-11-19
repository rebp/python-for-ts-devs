"""Tests for exercise 30-1 (Threads, processes and the GIL).

Edit: ex30_1_fetch_all.py::fetch_all
"""

import time

from ex30_1_fetch_all import fetch_all

URLS = [f"https://example.com/{n}" for n in range(6)]


def test_returns_pages_in_order():
    assert fetch_all(URLS) == [f"<page {url}>" for url in URLS]


def test_runs_in_parallel():
    start = time.perf_counter()
    fetch_all(URLS)
    elapsed = time.perf_counter() - start
    # One after the other would take 1.8 s. In parallel it's about 0.3 s.
    assert elapsed < 1.0, f"took {elapsed:.2f}s: are the downloads overlapping?"


def test_empty_list():
    assert fetch_all([]) == []
