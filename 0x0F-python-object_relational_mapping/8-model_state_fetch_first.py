#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql://"+sys.argv[1]+":"+sys.argv[2]+"@localhost:3306/"+sys.argv[3])
    session = sessionmaker()
    myrow = session.query(State.id, State.name).order_by(State.id).first()
    for row in myrow:
        print("%s: %s" % (row.id, row.name))
