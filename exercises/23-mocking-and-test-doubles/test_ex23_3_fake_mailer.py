"""Tests for exercise 23-3 (Mocking and test doubles).

Edit: ex23_3_fake_mailer.py::FakeMailer
"""

import pytest
from ex23_3_fake_mailer import FakeMailer, MailError, send_welcome_emails


def test_starts_empty():
    assert FakeMailer().sent == []


def test_records_sent_messages():
    mailer = FakeMailer()
    mailer.send("ada@example.com", "Hi")
    mailer.send("grace@example.com", "Hello")
    assert mailer.sent == [("ada@example.com", "Hi"), ("grace@example.com", "Hello")]


def test_fails_for_chosen_addresses():
    mailer = FakeMailer(fail_for=["bob@example.com"])
    with pytest.raises(MailError):
        mailer.send("bob@example.com", "Hi")
    assert mailer.sent == []


def test_instances_do_not_share_state():
    first, second = FakeMailer(), FakeMailer()
    first.send("ada@example.com", "Hi")
    assert second.sent == []


def test_works_with_send_welcome_emails():
    mailer = FakeMailer(fail_for={"bob@example.com"})
    failed = send_welcome_emails(
        ["ada@example.com", "bob@example.com", "grace@example.com"], mailer
    )
    assert failed == ["bob@example.com"]
    assert mailer.sent == [
        ("ada@example.com", "Welcome!"),
        ("grace@example.com", "Welcome!"),
    ]
