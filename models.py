
"""
Model definiotions.

Use new sqlalchemy style:
https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#whatsnew-20-orm-declarative-typing
"""


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)


class Base(DeclarativeBase):
	pass


class User(Base):
	__tablename__ = "users"
	id = mapped_column(Integer, primary_key=True)
	email = mapped_column(String(255), nullable=False)


class URL(Base):
	__tablename__ = "urls"
	id = mapped_column(Integer, primary_key=True)
	short = mapped_column(String(255), nullable=False)
	long = mapped_column(String(255), nullable=False)
	user_id = mapped_column(Integer, ForeignKey("users.id"))
