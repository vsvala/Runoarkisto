from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application.auth.models import User
from application.auth.forms import LoginForm, UserForm, UppdateForm

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
             password=form.password.data, role="USER")#, role="USER"


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
@app.route("/auth/modify/<auth_id>/", methods=["GET"])
@login_required(role="ADMIN")
def auth_uppdateForm(auth_id):

    user = User.query.get(auth_id)
    form = UppdateForm()
    #form = UppdateForm(obj=user) # Täytetään lomake tietokannasta löytyvillä käyttäjän tiedoilla
    
    return render_template("auth/modify.html", user=user, form=form)

 #käyttäjän muokkaus
@app.route("/auth/modify/<auth_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
def auth_uppdate(auth_id):

    user = User.query.get(auth_id)

    form = UppdateForm(request.form)

    # if not form.validate():
    #      return render_template("auth/modify.html", user=user, form=form)

    user.name=form.name.data
    user.username=form.username.data
    user.password=form.password.data
    user.password=form.password.data
    user.role=form.role.data

    db.session().commit()

    return redirect(url_for("auth_index"))

#käyttäjän poisto???yhteyksien poito tai käyttäjälle nimike poistettu käyttäjä...?
@app.route("/auth/<auth_id>/delete/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def auth_delete(auth_id):

    user = User.query.get(auth_id)
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("auth_index"))

#hakee käyttäjät jotka ovat lisänneet runoja
@app.route("/auth/list/")
@login_required() #(role="ADMIN")
def users_withPoems():
     return render_template("auth/list.html", how_many=User.find_users_with_poem(), users=User.query.all())


