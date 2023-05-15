from sqlalchemy import (
    Column, Date, Boolean, Integer, MetaData, Numeric,
    String, Table, Text,)

metadata = MetaData()


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column(
        'email', String(128), unique=True, nullable=False, index=True,),
    Column(
        'username', String(128), unique=True, nullable=False,),
    Column(
        'hashed_password', String(128), nullable=False,
        ),
    Column(
        'is_active', Boolean, default=True, nullable=False,
    ),
    Column(
        'is_superuser', Boolean, default=False, nullable=False,
    ),
    Column(
        'is_verified', Boolean, default=False, nullable=False,
    )
)

# class Film(Base):
#     """
#     Model Film:
#     Attributes:
#         - name: название
#         - description: описание
#         - image: постер
#         - release_date: дата выхода
#         - urls: ссылки
#     """
# # __tablename__ = 'films'

film = Table(
    'film',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(128),  nullable=False,),
    Column('description', String(250), nullable=False,
    ),
    #image = None
    Column('release_date', Date),
)

# class Serial(Base):
#     """
#     Model Serial:
#     Attributes:
#         -
#         -
#     """
#     __tablename__ = 'serials'
