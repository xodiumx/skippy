from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Models User:
    Attributes:
        - id: pk
        - email: unique email
        - username: unique username
        - password: hashed password
        - is_active: account is active
        - is_superuser: account is superuser
        - is_verified: account is verified
    """
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(128), unique=True, nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(length=128), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=128), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
