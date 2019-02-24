#Import dependencies
from flask import Flask, render_template

#Create instance of flask app
app = Flask(__name__)

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
