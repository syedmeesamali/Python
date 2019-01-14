import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))

db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights2").fetchall()
    for flight in flights:
        printf(f"{flight.origin} to {flights.destination}, {flights.duration}")
        

if __name__ == "__main__":
    main()
