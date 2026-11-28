# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright>=1.50"]
# ///
"""Run every runnable Python example on the course site in a real browser.

uv run scripts/check_in_browser.py

Opens index.html in Chrome (or Playwright's Chromium), clicks Run on every
example marked data-run and checks the result: data-run="error" examples must
show a traceback, all others must print something without one. Needs network
access for Pyodide. Run it after adding examples or upgrading Pyodide.
"""

from __future__ import annotations

import functools
import http.server
import re
import sys
import threading
from pathlib import Path

from playwright.sync_api import Browser, Error, Page, Playwright, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PORT = 8799
UNCAUGHT = re.compile(r"^[\w.]*(Error|Exception|Interrupt)\b")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def serve() -> http.server.ThreadingHTTPServer:
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def launch(playwright: Playwright) -> Browser:
    try:
        return playwright.chromium.launch(channel="chrome")
    except Error:
        return playwright.chromium.launch()


def lessons() -> list[str]:
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    return re.findall(r'<template class="lesson" data-n="([^"]+)"', page)


def check_lesson(page: Page, lesson: str) -> list[str]:
    page.goto(f"http://127.0.0.1:{PORT}/index.html#lesson-{lesson}")
    page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
    problems = []
    boxes = page.locator(".runnable:has(.run-go)")
    for index in range(boxes.count()):
        box = boxes.nth(index)
        mode = box.locator("code").get_attribute("data-run") or ""
        source = box.locator("code").text_content() or ""
        first_line = (source.splitlines() or [""])[0]
        box.locator(".run-go").click()
        box.locator('.run-go[aria-busy="false"]').wait_for(timeout=180_000)
        output = box.locator(".run-output").inner_text()
        # An uncaught exception ends the output with its "SomeError: message" line.
        lines = [line for line in output.splitlines() if line.strip()]
        failed = bool(lines) and bool(UNCAUGHT.match(lines[-1]))
        if mode == "error":
            ok = failed
        else:
            ok = not failed and "(no output)" not in output and "Couldn’t" not in output
        status = "ok  " if ok else "FAIL"
        print(f"{status} {lesson:<14} {mode or 'run':<6} {first_line[:60]}")
        if not ok:
            problems.append(f"{lesson}: {first_line}\n{output}")
    return problems


def main() -> int:
    server = serve()
    problems: list[str] = []
    with sync_playwright() as playwright:
        browser = launch(playwright)
        page = browser.new_page()
        for lesson in lessons():
            problems += check_lesson(page, lesson)
        browser.close()
    server.shutdown()
    print()
    if problems:
        print(f"{len(problems)} example(s) failed in the browser:\n")
        print("\n\n".join(problems))
        return 1
    print("Every runnable example works in the browser.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
