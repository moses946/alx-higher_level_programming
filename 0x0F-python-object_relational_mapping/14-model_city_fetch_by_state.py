#!/usr/bin/python3

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as a


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
