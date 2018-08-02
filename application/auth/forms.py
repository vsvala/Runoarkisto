from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")


class UserForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    username = StringField("username", [validators.Length(min=2)])
    password = StringField("password", [validators.Length(min=2)])
  
    class Meta:
        csrf = False