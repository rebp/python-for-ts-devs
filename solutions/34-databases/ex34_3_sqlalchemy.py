"""Reference solution for exercise 34-3 (Databases)."""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]


def save_and_list_notes_orm(url: str, texts: list[str]) -> list[tuple[int, str]]:
    """Rewrite the notes task with a SQLAlchemy Note model.

    Note is a mapped class with __tablename__ = "notes", an int id primary key
    and a str text. save_and_list_notes_orm(url, texts) creates the table if
    needed, adds one Note per text in a Session, commits, and returns all notes
    as (id, text) tuples ordered by id, like exercise 1.

    The url looks like "sqlite:///notes_orm.db". Call engine.dispose() at the
    end so the database file is closed.
    """
    engine = create_engine(url)
    try:
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            session.add_all([Note(text=text) for text in texts])
            session.commit()
            notes = session.scalars(select(Note).order_by(Note.id))
            return [(note.id, note.text) for note in notes]
    finally:
        engine.dispose()
