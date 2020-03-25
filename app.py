"""Blogly application."""

from flask import Flask, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def get_index():
    """ Goes to list of Users """
    return redirect("/users")


@app.route('/users')
def show_users():
    """ List of all Users """
    users = User.query.all()
    return render_template(
        'userlisting.html',
        users=users
    )


@app.route('users/new')
def create_new_user();
    """ Takes form info and creates new user """



# @app.route()
# @app.route()
# @app.route()
# @app.route()
# @app.route()