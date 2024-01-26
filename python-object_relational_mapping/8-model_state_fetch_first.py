"""print the first state"""
import sys 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def print_first_state(session):
    """first state object"""
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}". format(first_state.id, first_state.name))
    else:
        print("Nothing")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} <username> <password> <database>" .format(sys.argv[0]))
        sys.exit(1)
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}' .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    print_first_state(session)