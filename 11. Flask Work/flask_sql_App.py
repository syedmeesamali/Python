import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine("postgres://postgres:admin@localhost:5432")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flight = db.execute("SELECT * FROM flights2").fetchall()
    return render_template("index.html", flights = flights)

@app.route("/book")
def book():
    name = request.form.get("name")
    try:
        

def main():
    flights = db.execute("SELECT id, origin, destination, duration FROM flights2").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination} of {flight.duration} mins")

    #Prompt user to choose a flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights2 WHERE id = :id",
                        {"id": flight_id}).fetchone()

    if flight is None:
        print("ERROR: No such flight !")
        return
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                        {"flight_id": flight_id}).fetchall()

    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers on this flight")

                         
if __name__ == "__main__":
    main()
