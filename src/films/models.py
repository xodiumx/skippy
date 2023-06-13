from sqlalchemy import (
    Column, Date, Integer, String, Table,)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from main.db import metadata


film = Table(
    'film',
    metadata,
    Column('id', Integer, primary_key=True,
    ),
    Column('key', String(128), nullable=False, index=True,
    ),
    Column('title', String(128),  nullable=False, index=True,
    ),
    Column('genres', String(256), nullable=False,
    ),
    Column('image', String(256), nullable=False,
    ),
    Column('release_date', Date, nullable=False,
    ),
    Column('trailer', String(256), #nullable=False,
    ),
)


class Base(DeclarativeBase):
    pass


class FilmModel(Base):

    __tablename__ = 'film'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    key: Mapped[str] = mapped_column(
        String(128), unique=True, nullable=False, index=True,
    )
    title: Mapped[str] = mapped_column(
        String(128), nullable=False, index=True,
    )
    genres: Mapped[str] = mapped_column(
        String(256), nullable=False,
    )
    image: Mapped[str] = mapped_column(
        String(256), nullable=False,
    )
    release_date: Mapped[Date] = mapped_column(
        Date, nullable=False,
    )
    trailer: Mapped[str] = mapped_column(
        String(256), #nullable=False,
    )
