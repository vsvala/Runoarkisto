from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
  
from application.auth.models import User #pitäiskö olla Account

# Lomake siäänkirjautumiseen
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

# Lomake jolla luodaan uusi käyttäjä
class UserForm(FlaskForm):
    name = StringField("name", [validators.Length(min=2)])
    username = StringField("username", [validators.Length(min=2)])
    password = PasswordField("password", [validators.Length(min=2)])

# Tarkistaa, ettei käyttäjänimi ole jo käytössä
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Käyttäjätunnus on jo käytössä")

  
    class Meta:
        csrf = False