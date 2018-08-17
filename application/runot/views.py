from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.auth.models import User

from application.runot.models import Runo
from application.runot.forms import RunoForm

from application.category.models import Category

#yksitttäisen runon näyttö
@app.route("/runot/one/<runo_id>/", methods=["GET"])
def runot_showOne(runo_id):
    t = Runo.query.get(runo_id)
    print(t)
    return render_template("runot/one.html", t=t)

#runojen listaus
@app.route("/runot/", methods=["GET"])
def runot_index():
    return render_template("runot/list.html", runot=Runo.query.all())

# #runon luomislomakkeen haku
# @app.route("/runot/uusi")
# @login_required
# def runot_form(categ):
#     return render_template("runot/uusi.html", form=RunoForm(), categ=categ)


#uuden runon luomislomakkeen haku ja runon luominen
@app.route("/runot/uusi/<c_id>/", methods=["GET","POST"])
@login_required
def runot_create(c_id):

    if request.method == "GET":
        return render_template("runot/uusi.html", form=RunoForm(), c_id=c_id)

    form = RunoForm(request.form)

    if not form.validate():
        return render_template("runot/uusi.html", form=form, c_id=c_id)

    t = Runo(name=form.name.data, sisalto=form.sisalto.data,
             runoilija=form.runoilija.data)

    t.account_id = current_user.id
  
    category=Category.query.get(c_id)
    t.categories.append(category)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("runot_index"))

#runon muokkaus lomakkeen haku
@app.route("/runot/<runo_id>/", methods=["GET"])
@login_required
def runot_uppdateForm(runo_id):

    t = Runo.query.get(runo_id)
    form = RunoForm(obj=t) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

    return render_template("runot/muokkaa.html", t=t, form=form)

#runon muokkaus
@app.route("/runot/<runo_id>/", methods=["POST"])
@login_required
def runot_uppdate(runo_id):

    t = Runo.query.get(runo_id)

    form = RunoForm(request.form)

    if not form.validate():
        return render_template("runot/muokkaa.html", t=t, form=form)

    t.name=form.name.data
    t.sisalto=form.sisalto.data
    t.runoilija=form.runoilija.data
    t.account_id = current_user.id

    db.session().commit()

    return redirect(url_for("runot_index"))

#runon poisto
@app.route("/runot/<runo_id>/delete/", methods=["GET", "POST"])
@login_required
def runot_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("runot_index"))

#hakee käyttäjät jotka ovat lisänneet runoja
@app.route("/runot/listings/a")
@login_required
def users_withPoems():
     return render_template("runot/listings.html", how_many=User.find_users_with_poem())

#hakee kirjautuneen käyttäjä runot
@app.route("/runot/listings/b")
@login_required
def loggedu_poems():
    return render_template("runot/listings.html", loggedUsers_poems =Runo.find_loggedUsers_poems())

@app.route("/runot/listings/c")
@login_required
def find_runot_by_category():
    return render_template("runot/listings.html", runot_by_category =Runo.find_runot_by_category())

@app.route("/runot/one/<runo_id>/2",methods=["GET"])
@login_required
def find_categories(runo_id):
    t = Runo.query.get(runo_id)
    return render_template("runot/one.html", category_by =Category.find_categories_by(), t=t)






#työnalla
#lasketaan montako runoa tietokannasta löytyy
# @app.route("/runot/listings/c")
# @login_required
# def count_runo():
#     return render_template("runot/listings.html", find_poem=User.search_poem())

# #haetaan annettua runoa
# @app.route("/runot/listings/<runo_id>", methods=["GET", "POST"])
# @login_required
# def find_runo(runo_id):

#     t = Runo.query.get(runo_id)
    
#     form = FindForm(request.form) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

#     return render_template("runot/muokkaa.html", t=t, form=form)
    
#     runo = Runo.query.filter_by(name='otsikko').first()
#     print("KÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄK",runo)
  

#     return render_template("runot/listings.html", runo=runo)

