"""Tests for exercise 37-1 (Shipping a web service).

Edit: ex37_1_settings.py::Settings
"""

import pytest
from ex37_1_settings import Settings
from pydantic import ValidationError

VARIABLES = [
    "NOTES_DATABASE_URL",
    "NOTES_DEBUG",
    "NOTES_PORT",
    "NOTES_ALLOWED_ORIGINS",
    "DATABASE_URL",
]


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch):
    for name in VARIABLES:
        monkeypatch.delenv(name, raising=False)


def test_reads_database_url_and_uses_defaults(monkeypatch):
    monkeypatch.setenv("NOTES_DATABASE_URL", "sqlite:///notes.db")
    settings = Settings()
    assert settings.database_url == "sqlite:///notes.db"
    assert settings.debug is False
    assert settings.port == 8000
    assert settings.allowed_origins == []


def test_converts_types(monkeypatch):
    monkeypatch.setenv("NOTES_DATABASE_URL", "sqlite:///notes.db")
    monkeypatch.setenv("NOTES_DEBUG", "true")
    monkeypatch.setenv("NOTES_PORT", "9000")
    monkeypatch.setenv("NOTES_ALLOWED_ORIGINS", '["http://localhost:5173"]')
    settings = Settings()
    assert settings.debug is True
    assert settings.port == 9000
    assert settings.allowed_origins == ["http://localhost:5173"]


def test_database_url_is_required():
    with pytest.raises(ValidationError):
        Settings()


def test_variables_need_the_prefix(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///notes.db")
    with pytest.raises(ValidationError):
        Settings()


def test_bad_values_are_rejected(monkeypatch):
    monkeypatch.setenv("NOTES_DATABASE_URL", "sqlite:///notes.db")
    monkeypatch.setenv("NOTES_PORT", "eighty")
    with pytest.raises(ValidationError):
        Settings()
