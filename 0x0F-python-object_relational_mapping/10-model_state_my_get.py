#!/usr/bin/python3
"""this is crazy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    myrows = session.query(State).filter(State.name == sys.argv[4])
    if myrows.count() > 0:
        print(myrows[0].id)
    else:
        print("Not found")
