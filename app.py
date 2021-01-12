from flask import Flask, url_for, request, render_template
from flask_login import FlaskLoginClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return 'login'


