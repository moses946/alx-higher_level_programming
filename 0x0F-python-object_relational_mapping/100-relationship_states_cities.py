#!/usr/bin/python3
"""Module that Creates a state with a city.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State
from sys import argv as a

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add_all([new_city, new_state])
    session.commit()
    session.close()
