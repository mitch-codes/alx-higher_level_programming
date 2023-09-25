#!/usr/bin/python3
"""connect to database python using sqlalchemy"""
import sys
from sqlalchemy import create_engine
from base_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(mysql://"+sys.argv[1]":"+sys.argv[2]+"@localhost/"+sys.argv[3])
    session = sessionmaker(bind=engine)

    myStates = session.query(State).order_by(State.id)
    for row in myStates:
        print("%s: %s"% (row.id, row.name))

