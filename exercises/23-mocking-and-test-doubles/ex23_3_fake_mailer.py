"""Lesson 23 · Mocking and test doubles · exercise 3.

Check your work with: uv run course.py
"""

from collections.abc import Iterable
from typing import Protocol


class MailError(Exception):
    """Raised when an email can't be delivered."""


class Mailer(Protocol):
    def send(self, to: str, subject: str) -> None: ...


def send_welcome_emails(addresses: list[str], mailer: Mailer) -> list[str]:
    """Send a welcome email to every address and return the ones that failed."""
    failed = []
    for address in addresses:
        try:
            mailer.send(address, "Welcome!")
        except MailError:
            failed.append(address)
    return failed


class FakeMailer:
    """Write a fake mailer: a small, working stand-in for the real one that
    tests can pass to send_welcome_emails instead of a Mock.

    - FakeMailer() starts with an empty `sent` list.
    - send(to, subject) appends the tuple (to, subject) to `sent`.
    - FakeMailer(fail_for=["bob@example.com"]) makes send raise MailError for
      those addresses, without recording them in `sent`.

    A fake has real behaviour, so tests check the result (what's in `sent`)
    instead of which methods were called. It's the kind of object you'd hand
    to app.dependency_overrides in lesson 36.
    """

    def __init__(self, fail_for: Iterable[str] = ()) -> None:
        raise NotImplementedError("Your code here")

    def send(self, to: str, subject: str) -> None:
        raise NotImplementedError("Your code here")
