from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application.auth.models import User
from application.auth.forms import LoginForm, UserForm
from application.runot.models import Runo


#Haetaan kaikki käyttäjät aakkosjärjestyksessä
@app.route("/user/", methods=["GET"])
@login_required(role="ADMIN")
def auth_index():
    users = User.query.order_by(User.name).all()
    return render_template("auth/list.html", users=users)


# Rekisteröitymislomakkeen luonti sekä lähetys
@app.route("/auth/newuser", methods=["GET", "POST"])
def users_create():
    form = UserForm(request.form)
    if request.method == "GET":
        return render_template("auth/newuser.html", form=form)
    form = UserForm(request.form)
    if not form.validate():
        return render_template("auth/newuser.html", form=form)
#validoidaan samannimiset käyttäjänimet,jos löytyy render lomake uusiks ja error
    if User.query.filter_by(username=form.username.data).first():
        return render_template("auth/newuser.html", form=form, same_error= "Samanniminen käyttäjänimi on jo arkistossa!")
    t = User(name=form.name.data, username=form.username.data,
             password=form.password.data, role="USER")
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("auth_login"))


# Kirjautumislomakkeen haku, sekä lähetys
@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())
    form = LoginForm(request.form)
# validoinnit
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="Tuntematon käyttäjänimi tai salasana")
    login_user(user)
    return redirect(url_for("index"))



# Uloskirjaus
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))



#käyttäjän muokkaus lomakkeen haku
@app.route("/auth/modify/<auth_id>/", methods=["GET"])
@login_required(role="ADMIN")
def auth_uppdateForm(auth_id):
    user = User.query.get(auth_id)
    form = UserForm(obj=user) # Täytetään lomake tietokannasta löytyvillä käyttäjän tiedoilla
    
    return render_template("auth/modify.html", user=user, form=form)


#käyttäjän muokkaus
@app.route("/auth/modify/<auth_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
def auth_uppdate(auth_id):
    user = User.query.get(auth_id)
    form = UserForm(request.form)
#validoinnit
    print(form)
    if not form.validate():
        return render_template("auth/modify.html", user=user, form=form)
    user.name=form.name.data
    user.username=form.username.data
    user.password=form.password.data
    user.role=form.role.data
    db.session().commit()

    return redirect(url_for("auth_index"))



#käyttäjän poisto ja hänen runojen poisto
@app.route("/auth/<auth_id>/delete/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def auth_delete(auth_id):
    user = User.query.get(auth_id)
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("auth_index"))



#yksitttäisen käyttäjän näyttö
@app.route("/auth/one/<auth_id>/", methods=["GET"])
@login_required(role="ADMIN")
def auth_showOne(auth_id):
    user = User.query.get(auth_id)
    
    return render_template("auth/one.html", user=user)



#hakee käyttäjät jotka ovat lisänneet runoja
@app.route("/auth/list/")
@login_required(role="ADMIN")
def users_withPoems():
    how_many=User.find_users_with_poem()
    users = User.query.order_by(User.name).all()
    return render_template("auth/list.html", how_many=how_many, users=users)