#!/usr/bin/python3
"""the program changes
a row in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    louis = session.query(State).filter(State.id == 2).first()
    louis.name = "New Mexico"
    session.add(louis)
    session.commit()
  
