#!/usr/bin/python3
"""State Model"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).order_by(State.id)
    for i in result:
        name = i.name
        if 'a' in name:
            session.delete(i)
            session.commit()
