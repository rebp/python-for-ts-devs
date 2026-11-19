"""Reference solution for exercise 37-1 (Shipping a web service)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(env_prefix="NOTES_")

    database_url: str
    debug: bool = False
    port: int = 8000
    allowed_origins: list[str] = []
