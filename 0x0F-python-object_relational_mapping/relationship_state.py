#!/usr/bin/python3
"""State Model"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Model State"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence('seq_reg_id', start=1, increment=1),
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    def __init__(self, name, cities):
        self.name = name
        self.cities = cities
