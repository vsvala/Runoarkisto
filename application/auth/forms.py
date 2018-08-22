from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
  
from application.auth.models import User 

# Lomake jolla muokataan käyttäjää:
class UppdateForm(FlaskForm):
    name = StringField("nimi")
    username = StringField("käyttäjänimi")
    password = PasswordField("salasana")
    role = StringField("rooli")

# Lomake siäänkirjautumiseen
class LoginForm(FlaskForm):
    username = StringField("käyttäjänimi")
    password = PasswordField("salasana")

# Lomake jolla luodaan uusi käyttäjä
class UserForm(FlaskForm):
    name = StringField("nimi", [validators.Length(min=2, max=144, message= "syötteen täytyy olla 2-144 merkin väliltä" )])
    username = StringField("käyttäjänimi", [validators.Length(min=2, max=144, message= "syötteen täytyy olla 2-144 merkin väliltä")])
    password = PasswordField("salasana", [validators.Length(min=2, max=144, message= "syötteen täytyy olla 2-144 merkin väliltä")])

# Tarkistaa, ettei käyttäjänimi ole jo käytössä
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Käyttäjänimi on jo käytössä")

    class Meta:
        csrf = False