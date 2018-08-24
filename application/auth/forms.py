from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
  
from application.auth.models import User


# Lomake siäänkirjautumiseen
class LoginForm(FlaskForm):
    username = StringField("käyttäjänimi")
    password = StringField("salasana")

# Lomake jolla luodaan uusi käyttäjä ja admin muokkaa 
class UserForm(FlaskForm):
    name = StringField("nimi", [validators.Length(min=2, max=20, message= "syötteen täytyy olla 2-20 merkin väliltä" )])
    username = StringField("käyttäjänimi", [validators.Length(min=2, max=20, message= "syötteen täytyy olla 2-20 merkin väliltä")])
    password = StringField("salasana", [validators.Length(min=2, max=10, message= "syötteen täytyy olla 2-10 merkin väliltä")])
    role = StringField("rooli", [validators.Length(max=10, message= "syötteen täytyy olla vähemmän kuin 10 merkkiä ")]) 
    # role vain admin muokkaus käytössä,rekisteröityessä tyhjä

    class Meta:
        csrf = False