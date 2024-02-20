#!/usr/bin/python3
"""importing relevant modules"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    lstates = session.query(State).order_by(State.id).filter(
                            State.name.like('%a%')).all()
    for stat in lstates:
        print("{}: {}".format(stat.id, stat.name))

    session.close()
