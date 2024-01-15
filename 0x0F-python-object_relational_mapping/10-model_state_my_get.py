#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as a


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id).filter(State.name == a[4])

    if result.count() == 0:
        print("Not found")
    else:
        print(result[0].id)
