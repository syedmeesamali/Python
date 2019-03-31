from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgres://minhkibb:f8-3TYEbK21CZKJJdDb8EaLob8iSLs4r@balarama.db.elephantsql.com:5432/minhkibb'

db = SQLAlchemy(app)

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('user', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Views
@app.route('/')
@login_required
def home():
    return render_template('add_user.html')

@app.route('/profile/<name>')
def profile(name):
    user = Role.query.filter_by(name = name).first()
    return render_template("profile.html", user = user)

@app.route('/post_user', methods=['POST'])
def post_user():
    if(request.method == 'POST'):
        user1 = Role(name = request.form['name'], description = request.form['desc'])
        db.session.add(user1)
        db.session.commit()
        return render_template("success.html")

if __name__ == '__main__':
    app.run()