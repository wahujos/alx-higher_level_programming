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
    try:
        letter = session.query(State).filter(State.name.like('%a%')).all()
        for state in letter:
            session.delete(letter)
        session.commit()
        res = session.query(State).all()
        for r in res:
            print('{}: {}'.format(r.id, r.name))
    except Exception as e:
        session.rollback()
    finally:
        session.close()
