"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """ Class for User """

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(
                db.String,
                nullable=False)
    last_name = db.Column(
                db.String,
                nullable=False)
    # TODO They can have their annonymity,
    # but we want a default image if None
    # https://www.cfdating.com/user_images/default.png
    image_url = db.Column(
        db.String,
        default='https://www.cfdating.com/user_images/default.png')


class Post(db.Model):
    """  Class for Posts made by users"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                primary_key=True,
               autoincrement=True)
    author = db.Column(
        db.Integer,
        # user that wrote the post ref user_id
                )
    title = db.Column(
                db.String,
                nullable=False)
    body = db.Column(
                db.String,
                nullable=False)
