from flask import Flask, url_for, request, redirect, render_template
from flask_login import FlaskLoginClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/news')
def show_news():
    return render_template('news.html')


@app.route('/contact')
def show_contacts():
    return render_template('contact.html')


@app.route('/about')
def show_about():
    return render_template('about.html')


@app.route('/login')
def login():
    return 'login'
