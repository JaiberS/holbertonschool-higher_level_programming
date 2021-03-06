#!/usr/bin/python3
"""State Model"""

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from relationship_state import Base


class City(Base):
    """Model State"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('seq_reg_id', start=1, increment=1),
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
