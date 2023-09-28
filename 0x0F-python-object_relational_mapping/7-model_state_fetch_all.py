#!/usr/bin/python3
"""use sqlalchemy to connect to database"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    myStates = session.query(State).order_by(State.id)
    for row in myStates:
        print("{}: {}".format(row.id, row.name))

