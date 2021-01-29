"""
This file creates the DataBase and the tables in it.
Every class in this file is a table in the DB.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app_config import app

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    """
    User is a child of UserMixin so it is easily usable with the login system.
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


class Apartment(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.VARCHAR(255), nullable=False)
    location = db.Column(db.VARCHAR(255), nullable=False, unique=True)
    description = db.Column(db.TEXT, nullable=False)
    price = db.Column(db.FLOAT, nullable=False)
    image = db.Column(db.VARCHAR(255), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey(Apartment.id),
                             nullable=False)
    comment = db.Column(db.Text, nullable=False)
