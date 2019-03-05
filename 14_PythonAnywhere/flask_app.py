from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMRY_DATABASE_URI'] = 'postgres://postgres:admin@localhost:5432'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<{0} id: {1}>".format(self.__class__.__name__, self.id)

@app.route("/")
def index():
    return render_template("add_user.html")

@app.route("/post_user", methods = ['POST'])
def post_user():
    return "<h1 style='color: red'>Hello, Ali Shah</h1>"


if __name__ == '__main__':
    app.run(debug=True)
