# Exercise 40-3: Read real Python (answer)

Some of what you'll find, depending on the library you picked:

- **`fastapi/routing.py`**: `APIRouter` and `APIRoute` are classes with long,
  fully typed `__init__` methods. The `get`, `post` and other methods return
  decorators (lesson 27), which is exactly why `@router.get("/")` works.
- **`fastapi/params.py` and `fastapi/param_functions.py`**: `Query`,
  `Header` and `Depends` are small classes that only store metadata. FastAPI
  reads them back from your `Annotated[...]` hints.
- **`typer/main.py`**: Typer inspects your function's signature with the
  `inspect` module and builds a Click command from it. That's how a default
  value turns into an `--option`.
- **`pydantic_settings/main.py`**: `BaseSettings` is a Pydantic `BaseModel`
  subclass that collects values from several sources (init arguments,
  environment variables, `.env` files and secrets) in a fixed priority order.
- **`sqlalchemy/orm/session.py`**: `Session` defines `__enter__` and
  `__exit__` (lesson 28), which is why lesson 34 writes
  `with Session(engine) as session:` and the session is closed for you.

Things you may have met that the course didn't cover: `typing.overload`,
`__slots__`, `functools.wraps`, `contextvars`, `typing.TypeVar` and
`ParamSpec`, and `TYPE_CHECKING` imports. All are in the Python docs.

A good next step is to pick one library your team uses and read its main
module once a week.
