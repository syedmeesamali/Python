#Import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

#Create instance of flask app
app = Flask(__name__)

#Connect to the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost:5432'
db = SQLAlchemy(app)

#Define route and content of page
@app.route("/")
def index():
    return render_template("index.html")

#Define 2nd route and content
@app.route("/success", methods = ['POST'])
def success():
    return render_template("success.html")

#Running and controlling the script
if (__name__ == "__main__"):
    app.run(debug=True)
