from sqlalchemy import (
    Column, Date, Integer, MetaData, String, Table,)

metadata = MetaData()


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