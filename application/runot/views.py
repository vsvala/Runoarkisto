from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.runot.models import Runo
from application.runot.forms import RunoForm

@app.route("/runot/<runo_id>/", methods=["GET"])
def runot_naytayks(runo_id):
    t = Runo.query.get(runo_id)
    print(t)
   
    return render_template("runot/yks.html",  t=t)


@app.route("/runot/", methods=["GET"])
def runot_index():
    return render_template("runot/list.html", runot=Runo.query.all())


@app.route("/runot/uusi/")
@login_required
def runot_form():
    return render_template("runot/uusi.html", form=RunoForm())


@app.route("/runot/<runo_id>/", methods=["GET"])
@login_required
def runot_uppdateForm(runo_id):
    form=RunoForm()
    t = Runo.query.get(runo_id)
    return render_template("runot/muokkaa.html", t=t, form=form)


@app.route("/runot/<runo_id>/", methods=["POST"])
@login_required
def runot_uppdate(runo_id):

    form = RunoForm(request.form)

    t = Runo.query.get(runo_id)

    if not form.validate():
        return render_template("runot/muokkaa.html", t=t, form=form)

    t.name=form.name.data
    t.sisalto=form.sisalto.data
    t.runoilija=form.runoilija.data
    t.account_id = current_user.id

    db.session().commit()

    return redirect(url_for("runot_index"))


@app.route("/runot/<runo_id>/delete/", methods=["POST"])
@login_required
def runot_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("runot_index"))


@app.route("/runot/", methods=["POST"])
@login_required
def runot_create():

    form = RunoForm(request.form)

    if not form.validate():
        return render_template("runot/uusi.html", form=form)

    t = Runo(name=form.name.data, sisalto=form.sisalto.data,
             runoilija=form.runoilija.data)

#    t = Runo(form.name.data)
#    t.sisalto= form.sisalto.data
#    t.runoilija= form.runoilija.data

    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("runot_index"))
