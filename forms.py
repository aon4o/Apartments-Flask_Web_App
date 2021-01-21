from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField,\
    HiddenField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user


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


class ApartmentForm(FlaskForm):
    name = TextAreaField('name',
                         validators=[InputRequired(), Length(min=3, max=255)])
    location = TextAreaField('location',
                             validators=[InputRequired(), Length(min=10)])
    description = TextAreaField('description',
                                validators=[InputRequired(), Length(min=10)])
    
    
class CommentForm(FlaskForm):
    user_id = HiddenField('user_id', validators=[InputRequired()])
    apartment_id = HiddenField('apartment_id', validators=[InputRequired()])
    comment = TextAreaField('comment', validators=[InputRequired()])
