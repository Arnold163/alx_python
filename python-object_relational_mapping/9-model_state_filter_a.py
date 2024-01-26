"""contains an a lets see"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def print_states_with_a(session):
    """all state objects with letter a"""
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} <username> <password> <database>" .format(sys.argv[0]))
        sys.exit(1)
    
    engine = create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)
    print_states_with_a(session)

    session.close()

