from sqlalchemy import (
    Column, Boolean, Integer, MetaData, String, Table,)

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