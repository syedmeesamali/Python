from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://postgres:admin@localhost/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    __table_name__ = "entry"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template("add_user.html")

@app.route('/post_user', methods=['POST'])
def post_user():
    if(request.method == 'POST'):
        user = User(request.form['username'], request.form['email'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
