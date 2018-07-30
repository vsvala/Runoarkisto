from application import app, db
from flask import render_template, request, redirect, url_for
from application.runot.models import Runo

@app.route("/runot/", methods=["GET"])
def runot_index():
    return render_template("runot/list.html", runot =Runo.query.all())

@app.route("/runot/uusi/")
def runot_form():
    return render_template("runot/uusi.html")

@app.route("/runot/", methods=["POST"])
def runot_create():

  t =Runo(request.form.get("name"))

  db.session().add(t)
  db.session().commit()

  #return "hello world!"
    
  return redirect(url_for("runot_index"))

  