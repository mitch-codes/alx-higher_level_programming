#!/usr/bin/python3
"""create a base fro the table state"""
from sqlalchemy.ext.declarative import declarative_Base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """State class represents table states
    
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name= Column(String(128), nullable=False)
    
