from db import engine
from sqlalchemy import (Column, Date, ForeignKey, Integer, MetaData, Numeric,
                        String, Table, Text)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()


class User(Base):
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


Base.metadata.create_all(engine)