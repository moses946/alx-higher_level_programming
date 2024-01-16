#!/usr/bin/python3
"""Module that prints the first state object.
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)
    if results.count() == 0:
        print("Nothing")
    else:
        print(f"{results[0].id}: {results[0].name}")
