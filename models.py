"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    posts = db.relationship("Post", backref="user")

class Post(db.Model):
    """  Class for Posts made by users"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
        # user that wrote the post ref user_id
                )
    title = db.Column(
                db.String,
                nullable=False)
    content = db.Column(
                db.String,
                nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default= datetime.now
    )

    # user = db.relationship("User")