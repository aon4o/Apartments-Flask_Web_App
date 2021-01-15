from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, \
    logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
Bootstrap(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('email',
                        validators=[InputRequired(), Length(max=50)])
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)])


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired()])
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)])
    remember = BooleanField('remember me')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
        db.session.add(new_user)
        db.session.commit()
        login_user(User.query.filter_by(email=form.email.data).first(),
                   remember=False)
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
                return redirect(url_for('index'))
        
        return '<h1>Invalid Email or Password!'
    
    return render_template('auth/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


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
