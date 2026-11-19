"""Tests for exercise 24-3 (Debugging).

Edit: ex24_3_log_failures.py::run_job
"""

import logging

import pytest
from ex24_3_log_failures import run_job


def broken():
    raise ValueError("disk full")


@pytest.fixture
def job_log(caplog):
    caplog.set_level(logging.INFO, logger="jobs")
    return caplog


def records(caplog):
    return [r for r in caplog.records if r.name == "jobs"]


def test_success_returns_true_and_logs_nothing(job_log):
    assert run_job("backup", lambda: 42) is True
    assert records(job_log) == []


def test_failure_returns_false(job_log):
    assert run_job("backup", broken) is False


def test_failure_is_logged_as_an_error_with_message(job_log):
    run_job("backup", broken)
    [record] = records(job_log)
    assert record.levelno == logging.ERROR
    assert record.getMessage() == "job backup failed"


def test_log_contains_the_traceback(job_log):
    run_job("backup", broken)
    [record] = records(job_log)
    assert record.exc_info is not None, "use logger.exception, not logger.error"
    assert record.exc_info[0] is ValueError
    assert "disk full" in job_log.text
    assert "in broken" in job_log.text


def test_keyboard_interrupt_is_not_swallowed(job_log):
    def interrupted():
        raise KeyboardInterrupt

    with pytest.raises(KeyboardInterrupt):
        run_job("backup", interrupted)
