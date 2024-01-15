#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv as a
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(a[1], a[2], a[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
