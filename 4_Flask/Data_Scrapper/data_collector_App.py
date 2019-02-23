#Import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy

#Create instance of flask app
app = Flask(__name__)

#Connect to the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost:5432'
db = SQLAlchemy(app)


class Data(db.Model):
    #Create a new table

    __table_name__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sex = db.Column(db.String)

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

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
