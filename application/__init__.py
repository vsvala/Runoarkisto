# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///runot.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# kirjautuminen part1
from os import urandom
app.config["SECRET_KEY"] = urandom(32)
#app.config["SECRET_KEY"] = 'supersecret'

from flask_login import LoginManager,current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                user_role=current_user.role
                if user_role==role:           
                    unauthorized = False
                     

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# load application content
# oman sovelluksen toiminnallisuudet

from application import views # Luetaan kansiosta application tiedoston views sisältö

from application.runot import models
from application.runot import views

from application.auth import models 
from application.auth import views

from application.category import models 
from application.category import views


# login functionality, part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()
except:
    pass
