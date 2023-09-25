#!/usr/bin/python3
"""connect to mysql to retrieve
only one record"""
import sys
from sqlalchemy import create_engine
from base_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(sys.argv[1]+"://"+sys.argv[2]":"+sys.argv[3]+"password@localhost/db")
    session = sessionmaker(bind=engine)

    myStates = session.query(State).order_by(State.id)
    for row in myStates:
        print("%s: %s"% (row.id, row.name))

