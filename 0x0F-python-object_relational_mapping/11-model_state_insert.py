#!/usr/bin/python3
"""the program inserts
a new row to database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
Session = sessionmaker(bind=engine)
session = Session()
louis = State()
louis.name = "Louisiana"
session.add(louis)
print(louis.id)
session.commit()
