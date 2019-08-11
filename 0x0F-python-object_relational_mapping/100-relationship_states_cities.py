#!/usr/bin/python3
"""State Model"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    MetaData().create_all(engine)
    session = sessionmaker(bind=engine)()
    state = State("California", [City("San Francisco")])
    session.add(state)
    session.commit()
