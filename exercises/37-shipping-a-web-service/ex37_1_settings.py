"""Lesson 37 · Shipping a web service · exercise 1.

Check your work with: uv run course.py
"""

from pydantic_settings import BaseSettings, SettingsConfigDict  # noqa: F401


class Settings(BaseSettings):
    """Read the service's settings from environment variables that start with
    NOTES_, the way you'd parse process.env with Zod.

    | Field           | Type      | Default | Environment variable  |
    | --------------- | --------- | ------- | --------------------- |
    | database_url    | str       | none    | NOTES_DATABASE_URL    |
    | debug           | bool      | False   | NOTES_DEBUG           |
    | port            | int       | 8000    | NOTES_PORT            |
    | allowed_origins | list[str] | []      | NOTES_ALLOWED_ORIGINS |

    database_url is required: Settings() must raise a ValidationError without it.
    The values are converted for you: NOTES_DEBUG=true gives True, NOTES_PORT=9000
    gives the int 9000, and a list is written as JSON:
    NOTES_ALLOWED_ORIGINS='["http://localhost:5173"]'.

    Hint: set model_config = SettingsConfigDict(env_prefix="NOTES_").
    """

    # TODO: add model_config and the four fields
