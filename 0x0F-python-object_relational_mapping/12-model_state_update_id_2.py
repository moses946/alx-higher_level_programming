#!/usr/bin/python3
"""Module that updates a state.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as a


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == 2).first()
    update.name = "New Mexico"  # type: ignore
    session.commit()
