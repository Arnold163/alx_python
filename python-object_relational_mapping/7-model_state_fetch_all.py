"""all states via SQLALchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def print_states(session):
    """print from db"""
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} <username> <password> <database>" .format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    session = Session(engine)

    # Print the States
    print_states(session)

    # Close the session
    session.close()

