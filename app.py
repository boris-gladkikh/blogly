"""Blogly application."""

from flask import Flask, redirect, render_template, request
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
    return redirect("/users/")


@app.route('/users/')
def show_users():
    """ List of all Users """
    users = User.query.all()
    return render_template(
        'userlisting.html',
        users=users
    )


@app.route('/users/new/')
def create_new_user():
    """ Takes form info and creates new user """
    return render_template('newuserform.html')


@app.route('/users/new/', methods=["POST"])
def post_new_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None


    new_user = User(first_name = first_name,
    last_name = last_name,
    image_url = image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users/")

    
@app.route('/users/<user_id>/')
def info_about_user(user_id):

    current_user = User.query.filter_by(id=user_id).one()
    user_full_name = f"{current_user.first_name} {current_user.last_name}"
    user_image = current_user.image_url

    print("\n\n\n This is our user_image \n\n", user_image)


    return render_template('userdetails.html',
    user = user_full_name,
    image_url = user_image,
    user_id = user_id
    )


@app.route('/users/<user_id>/edit/')
def edit_user(user_id):

    return render_template('useredit.html')
# @app.route()
# @app.route()