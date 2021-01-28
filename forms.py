from app_config import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, \
    HiddenField, FloatField
from wtforms.validators import InputRequired, Length, NumberRange
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_uploads import configure_uploads, UploadSet, IMAGES

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(), Length(min=3, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField('email',
                        validators=[InputRequired(), Length(max=50)],
                        render_kw={"placeholder": "E-mail"})
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)],
                             render_kw={"placeholder": "Password"})


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired()],
                           render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=8)],
                             render_kw={"placeholder": "Password"})
    remember = BooleanField('remember me')


class ApartmentForm(FlaskForm):
    name = TextAreaField(
        'name',
        validators=[InputRequired(), Length(min=3, max=255)],
        render_kw={"placeholder": "Name for your apartment. (3-255 symbols)"})
    user_id = HiddenField('user_id', validators=[InputRequired()])
    location = TextAreaField(
        'location',
        validators=[InputRequired(), Length(min=10)],
        render_kw={"placeholder": "Where is it located ? (Min. 10 symbols)"})
    description = TextAreaField(
        'description',
        validators=[InputRequired(), Length(min=10)],
        render_kw={"placeholder"
                   : "A description of your apartment. (Min. 10 symbols)"})
    price = FloatField('price',
                       validators=[InputRequired(), NumberRange(min=1)])
    image = FileField('image', validators=[
        FileRequired(), FileAllowed(images, "Images only allowed!")])


class ApartmentEditForm(FlaskForm):
    name = TextAreaField(
        'name',
        validators=[InputRequired(), Length(min=3, max=255)],
        render_kw={"placeholder": "Name for your apartment. (3-255 symbols)"})
    user_id = HiddenField('user_id', validators=[InputRequired()])
    location = TextAreaField(
        'location',
        validators=[InputRequired(), Length(min=10)],
        render_kw={"placeholder": "Where is it located ? (Min. 10 symbols)"})
    description = TextAreaField(
        'description',
        validators=[InputRequired(), Length(min=10)],
        render_kw={"placeholder"
                   : "A description of your apartment. (Min. 10 symbols)"})
    price = FloatField('price',
                       validators=[InputRequired(), NumberRange(min=1)])


class CommentForm(FlaskForm):
    user_id = HiddenField('user_id', validators=[InputRequired()])
    apartment_id = HiddenField('apartment_id', validators=[InputRequired()])
    comment = TextAreaField('comment', validators=[InputRequired()],
                            render_kw={"placeholder": "Your comment here!"})
