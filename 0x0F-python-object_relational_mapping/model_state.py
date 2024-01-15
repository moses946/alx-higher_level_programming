#!/usr/bin/python3
"""Module containing definition of a State using ORM"""


from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Class definition of a State
    Attrs:
        id(Int): Auto-generated, Unique, Not Null, PKey
        name(String): Name of state
    """
    __tablename__ = "states"

    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement='auto')
    name = Column(String(128), nullable=False)
