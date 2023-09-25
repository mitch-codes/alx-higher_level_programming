#!/usr/bin/python3
"""create a base fro the table state"""
from sqlalchemy.ext.declarative import declarative_Base
form sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """State class represents table states"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name= Column(String(128), nullable=False)
    
