from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application.auth.models import User
from application.auth.forms import LoginForm, UserForm


# Rekisteröitymislomakkeen luonti sekä lähetys
@app.route("/auth/newuser", methods=["GET", "POST"])
def users_create():

    form = UserForm(request.form)

    if request.method == "GET":
        return render_template("auth/newuser.html", form=form)

    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/newuser.html", form=form)

    t = User(name=form.name.data, username=form.username.data,
             password=form.password.data, role="USER")

    # if User.query.filter_by(username=form.username.data): #huom ei toimi jos user on tyhjä...
   
    #     return redirect(url_for("users_create", form=UserForm()))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("auth_login"))


# @app.route("/auth/newuser", methods=["GET"])
# def user_form():
#     return render_template("/auth/newuser.html", form=UserForm())


# Kirjautumislomakkeen haku, sekä lähetys
@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="Tuntematon käyttäjänimi tai salasana")

    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))

# Uloskirjaus
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#yksitttäisen käyttäjän näyttö
@app.route("/auth/one/<auth_id>/", methods=["GET"])
def auth_showOne(auth_id):
    user = User.query.get(auth_id)

    return render_template("auth/one.html", user=user)

#käyttäjien listaus
@app.route("/auth/", methods=["GET"])
def auth_index():
    return render_template("auth/list.html", users=User.query.all())

#käyttäjän muokkaus lomakkeen haku
@app.route("/auth/<auth_id>/", methods=["GET"])
@login_required
def auth_uppdateForm(auth_id):

    user = User.query.get(auth_id)
    form = UserForm(obj=user) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

    return render_template("auth/newuser.html", user=user, form=form)

 #käyttäjän muokkaus
@app.route("/auth/<auth_id>/", methods=["POST"])
@login_required
def auth_uppdate(auth_id):

    user = User.query.get(auth_id)

    form = UserForm(request.form)

    if not form.validate():
         return render_template("auth/newuser.html", user=user, form=form)

    user.name=form.name.data
    user.username=form.usernameo.data
    user.password=form.password.data
    user.password=form.password.data

    db.session().commit()

    return redirect(url_for("auth_index"))

#käyttäjän poisto
@app.route("/auth/<auth_id>/delete/", methods=["GET", "POST"])
@login_required
def auth_delete(auth_id):

    user = User.query.get(auth_id)
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("auth_index"))