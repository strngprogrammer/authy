from wtforms import *
from flask_wtf import FlaskForm 
from wtforms.validators import DataRequired , Length , Email , EqualTo 

class LoginField(FlaskForm):
    username = StringField(label="username",name="username",validators=[Length(5,32),DataRequired(message="username is requierd")])
    password = PasswordField(label="password",name="password",validators=[Length(8,32),DataRequired(message="password is requierd")])
    checkbox = BooleanField("save login")
    submit = SubmitField(label="Login")

class Register(FlaskForm):
    name = StringField(label="name",name="name",validators=[DataRequired(message="name is requierd")])
    email = StringField(label="email",name="email",validators=[Email(message="enter a valid email address"),DataRequired(message="email is requierd")])
    username = StringField(label="username",name="username",validators=[Length(5,32),DataRequired(message="username is requierd")])
    password = PasswordField(label="password",name="password",validators=[Length(8,32),DataRequired(message="password is requierd")])
    password_confirm = PasswordField(label="password_confirm",name="password_confirm",validators=[Length(8,32),DataRequired(message="password is requierd"),EqualTo("password",message="password confirm must be equals to password")])
    submit = SubmitField(label="Sign up")

class NewApp(FlaskForm):
    name = StringField(label="app name",name="name",validators=[DataRequired(message="app name is requierd")])
    password = StringField(label="app password",name="password",validators=[DataRequired(message="app password is requierd")])
    submit = SubmitField(label="Create App")

class NewAuth(FlaskForm):
    name = StringField(label="auth name",name="name",validators=[DataRequired(message="auth name is requierd")])
    auth = StringField(label="auth",name="auth",validators=[DataRequired(message="auth is requierd")])
    days = IntegerField(label="days for expire",name="days",validators=[DataRequired(message="days is requierd")])
    submit = SubmitField(label="Create Auth")
