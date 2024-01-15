#!/usr/bin/python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """ Class definition of a city
    Attrs:
        id(int)
        name(string)
        state_id(int)
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement='auto',
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
