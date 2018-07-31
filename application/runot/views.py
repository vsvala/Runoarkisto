from application import app, db
from flask import render_template, request, redirect, url_for
from application.runot.models import Runo

# @app.route("/runot/<runo_id>/", methods=["GET"])
# def runot_naytayks(runo_id):
#    # t = Runo.query.get(runo_id)
#     return render_template("runot/yks.html",  t = Runo.query.get(runo_id))


@app.route("/runot/", methods=["GET"])
def runot_index():
    return render_template("runot/list.html", runot = Runo.query.all())


@app.route("/runot/uusi/")
def runot_form():
    return render_template("runot/uusi.html")


@app.route("/runot/<runo_id>/", methods=["GET"])
def runot_uppdateForm(runo_id):

    t = Runo.query.get(runo_id)
    return render_template("runot/muokkaa.html", t=t)
 


@app.route("/runot/<runo_id>/", methods=["POST"])
def runot_uppdate(runo_id):
    t = Runo.query.get(runo_id)
    t.name = request.form.get("name")
    t.sisalto = request.form.get("sisalto")
    t.runoilija = request.form.get("runoilija")

    #Runo(request.form.get("name"), request.form.get("sisalto"), request.form.get("runoilija"))
    db.session().commit()
  
    return redirect(url_for("runot_index"))


@app.route("/runot/<runo_id>/delete/", methods=["POST"])
def runot_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("runot_index"))



@app.route("/runot/", methods=["POST"])
def runot_create():

  t = Runo(request.form.get("name"), request.form.get("sisalto"), request.form.get("runoilija"))
 
  db.session().add(t)
  db.session().commit()

  #return "hello world!"
    
  return redirect(url_for("runot_index"))

  