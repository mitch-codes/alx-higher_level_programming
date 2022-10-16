#!/usr/bin/python3
""""
display all the records of
a database table"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine()
    Base.metadata.createall(
                            "mysql+mysqldb://{}:{}@localhost/{}"
                            .format(
                                    sya.argv[1],
                                    sys.argv[2],
                                    sys.argv[3],
                                        ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    results = session.query(State).order_by(State.id).first()
    for result in results:
        print("{}: {}".format(result.id, result.name))
    session.close()
