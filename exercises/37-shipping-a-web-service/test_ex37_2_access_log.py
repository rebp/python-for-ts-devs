"""Tests for exercise 37-2 (Shipping a web service).

Edit: ex37_2_access_log.py::log_requests
"""

import logging
import re

import pytest
from ex37_2_access_log import VERSION, app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture
def access_log(caplog):
    caplog.set_level(logging.INFO, logger="notes.access")
    return caplog


def lines(caplog):
    return [
        record.getMessage()
        for record in caplog.records
        if record.name == "notes.access" and record.levelno == logging.INFO
    ]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": VERSION}


def test_logs_one_line_per_request(access_log):
    client.get("/health")
    logged = lines(access_log)
    assert len(logged) == 1
    assert re.fullmatch(r"GET /health 200 \d+\.\dms", logged[0]), logged[0]


def test_logs_errors_too(access_log):
    client.post("/nope")
    logged = lines(access_log)
    assert len(logged) == 1
    assert re.fullmatch(r"POST /nope 404 \d+\.\dms", logged[0]), logged[0]
