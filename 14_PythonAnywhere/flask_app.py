from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://postgres:admin@localhost:5432'
db = SQLAlchemy(app)

class User(db.Model):
    __table_name__ = "entry"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def index():
    return render_template("add_user.html")

@app.route("/success", methods=['POST'])
def success():
    if(request.method == 'POST'):
        username_ = request.form['username']
        email_ = request.form['email']
        entry = User(username_, email_)
        db.session.add(entry)
        db.session.commit()
        return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)