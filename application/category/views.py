from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.category.models import Category
from application.category.forms import  CategoryForm

from application.runot.forms import RunoForm
from application.runot.models import Runo

#yksitttäisen kategorian haku ja näyttö
@app.route("/category/one/<category_id>/", methods=["GET"])
#@login_required
def category_showOne(category_id):
    cate = Category.query.get(category_id)
    print(cate)
    return render_template("category/one.html",  cate=cate)

#kategorioiden listaus
@app.route("/category/", methods=["GET"])
#@login_required
def category_index():
    return render_template("category/list.html", category=Category.query.all())

#kategorian lisäys lomakkeen hakeminen ja kategorioiden lisääminen
@app.route("/category/other/<runo_id>/", methods=["GET","POST"])
@login_required
def category_other(runo_id):

    runo = Runo.query.get(runo_id)

    form = CategoryForm(request.form)

    if request.method == "GET":
        return render_template("category/other.html", form=form, runo=runo)

    form = CategoryForm(request.form)

    runo=Runo.query.get(runo_id)

    category = Category(aihe=form.aihe.data)

    db.session().add(category) #kategoriaolion  luonti ja commitointi tietokantaan
    db.session().commit() 

    runo.categories.append(category)    #liitokset runoon 
    db.session().commit()

    
    return redirect(url_for("runo_modify_page", runo_id=runo.id ))


#kategorian poisto
@app.route("/category/delete/<runo_id>/<category_id>/", methods=["GET", "POST"])
@login_required
def category_delete( runo_id, category_id,):
    
    #etsi id:tä vastaava runo-olio
    runo = Runo.query.get(runo_id)
    #etsi id:tä vastaava kategoriaolio
    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("runo_modify_page", runo_id=runo.id))

    
#kategorian poisto
@app.route("/category/delete/<category_id>/", methods=["GET", "POST"])
@login_required
def category_list_delete(category_id,):
    
    #etsi id:tä vastaava runo-olio
    #etsi id:tä vastaava kategoriaolio
    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("category_index"))
