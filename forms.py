from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('email',
                        validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": "E-mail"})
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)], render_kw={"placeholder": "Password"})


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)], render_kw={"placeholder": "Password"})
    remember = BooleanField('remember me')


class ApartmentForm(FlaskForm):
    name = TextAreaField('name',
                         validators=[InputRequired(), Length(min=3, max=255)], render_kw={"placeholder": "Name for your apartment. (3-255 symbols)"})
    location = TextAreaField('location',
                             validators=[InputRequired(), Length(min=10)], render_kw={"placeholder": "Where is it located ? (Min. 10 symbols)"})
    description = TextAreaField('description',
                                validators=[InputRequired(), Length(min=10)], render_kw={"placeholder": "A description of your apartment. (Min. 10 symbols)"})
