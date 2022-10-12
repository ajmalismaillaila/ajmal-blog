from wsgiref import validate
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from idna import valid_contextj
from sqlalchemy import String
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=  [DataRequired()])
    user_name = StringField("User_name", validators= [DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Create Account")

class LoginForm(FlaskForm):
    username = StringField("Username/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    Submit = SubmitField("Login", validators=[DataRequired()])
    
