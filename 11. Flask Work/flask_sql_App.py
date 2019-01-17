import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine("postgres://postgres:admin@localhost:5432")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/main")
def index():
    flights = db.execute("SELECT * FROM flights2").fetchall()
    return render_template("index.html", flights = flights)
        
if __name__ == "__main__":
    app.run(debug=True)
