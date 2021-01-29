"""
This file does the basic configuration for the application:
    the secret key,
    the database uri - used by SQLAlchemy,
    the folder for saving images
and other setting may be added here.
"""
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOADED_IMAGES_DEST'] = 'static/images'
