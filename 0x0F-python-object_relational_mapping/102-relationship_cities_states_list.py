#!/usr/bin/python3
"""Module that lists all cities and their states.
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv as a
from relationship_city import City, Base
from relationship_state import State


if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
