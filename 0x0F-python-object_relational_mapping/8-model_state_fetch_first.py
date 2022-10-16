#!/usr/bin/python3
""""
display all the records of
a database table"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
                            "mysql+mysqldb://{}:{}@localhost/{}"
                            .format(
                                    sys.argv[1],
                                    sys.argv[2],
                                    sys.argv[3]
                                        ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    for state in session.query(State).order_by(State.id).first():
        print("{}: {}".format(state.id, state.name))
    session.close()
