from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app_config import app

db = SQLAlchemy(app)
db.create_all()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


class Apartments(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    
    
class Comments(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey(Apartments.id),
                             nullable=False)
    comment = db.Column(db.Text, nullable=False)
