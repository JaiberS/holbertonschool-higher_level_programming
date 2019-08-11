#!/usr/bin/python3
"""State Model"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for i in result:
        print(i[1].name + ": (" + str(i[0].id) + ") " + i[0].name)
