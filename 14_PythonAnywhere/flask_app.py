from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
from flask_security import security, SQLAlchemyUserDatastore, Usermixin, Rolemixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/movie'
db = SQLAlchemy(app)

# class Movie(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(80))
#     email = db.Column(db.String(120))

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<Movie %r>' % self.username

#Define new models for our flask-security database
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), 
                db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, Rolemixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

class User(db.Model, Usermixin):
    id = db.Column(db.Integer(), primary_key = True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', 'lazy = dynamic'))

#Flask-security settings
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
    myUser = Movie.query.all()
    return render_template("add_user.html", myUser = myUser)

@app.route('/profile/<username>')
def profile(username):
    user = Movie.query.filter_by(username = username).first()
    return render_template("profile.html", user = user)

@app.route('/post_user', methods=['POST'])
def post_user():
    if(request.method == 'POST'):
        user1 = Movie(request.form['username'], request.form['email'])
        db.session.add(user1)
        db.session.commit()
        return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)