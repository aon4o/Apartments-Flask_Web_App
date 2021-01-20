from app_config import app
from flask import url_for, request, redirect, render_template, flash
from database import db, User
from forms import generate_password_hash, check_password_hash, \
    LoginForm, RegistrationForm
from login_manager import login_manager, login_required, login_user, \
    logout_user, current_user
import logging

db.create_all()
logging.basicConfig(filename='logs.log',
                    format='%(levelname)s  %(asctime)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data,
                                            method='sha256')
        )
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already taken!")
        elif User.query.filter_by(email=form.email.data).first():
            flash("Email already taken!")
        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(User.query.filter_by(email=form.email.data).first(),
                       remember=False)
            flash("Registered Successfully!")
            return redirect(url_for('index'))
        
    return render_template('auth/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash("Logged in Successfully!")
                return redirect(url_for('index'))
            else:
                flash("Invalid Password!")
        else:
            flash("Invalid Username!")
    
    return render_template('auth/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/apartments')
def apartments():
    return render_template('apartments.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
