import sqlalchemy
import MySQLdd
from sqlalchemy import create_engine
from model_state import Base, State
import sys
"""connect and view records usib=ng sqlalchemy"""

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[1], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State):
        print("{}: {}". format(state.id, state.name))
    session.close()

