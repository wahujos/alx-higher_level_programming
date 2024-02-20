#!/usr/bin/python3
"""importing the necessary imports"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """create the session"""
    Session = sessionmaker(bind=engine)
    session = Session()
    """creates a new state object"""
    addstate = State(name='Louisiana')
    """add and then commit"""
    session.add(addstate)
    session.commit()
    if addstate:
        print('{}'.format(addstate.id))
    session.close()
