from sqlalchemy import (Column, Date, ForeignKey, Integer, MetaData, Numeric,
                        String, Table, Text)
from sqlalchemy.ext.declarative import declarative_base

from db import engine


Base = declarative_base()
metadata = MetaData()


class User(Base):
    """
    Models User:
    Attributes:
        - id: pk
        - email: unique email
        - username: unique username
        - password: hashed password
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(
        String(128), 
        unique=True, 
        nullable=False,)
    username = Column(
        String(128), 
        unique=True, 
        nullable=False,)
    password_hash = Column(
        String(128),
        nullable=False,)


# class Film(Base):
#     """
#     Model Film:
#     Attributes:
#         -
#         -
#     """
#     __tablename__ = 'films'


# class Serial(Base):
#     """
#     Model Serial:
#     Attributes:
#         -
#         -
#     """
#     __tablename__ = 'serials'



Base.metadata.create_all(engine)