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
    
#kategorioiden lisääminen
@app.route("/category/other/<runo_id>/", methods=["GET","POST"])
@login_required
def category_other(runo_id):

    runo = Runo.query.get(runo_id)

    form = CategoryForm(request.form)

    if form.validate_on_submit():
         print(form.aihe.data)
                          # else:
                          #     print(form.errors)
                         # return render_template("category/addCategory.html", form=form)

    if request.method == "GET":
        return render_template("category/other.html", form=form, runo=runo)

    form = CategoryForm(request.form)
    category = Category(aihe=form.aihe.data)

    db.session().add(category)
    db.session().commit()
    
    runo=Runo.query.get(runo_id)
    runo.categories.append(category)
    db.session().commit()

    #jos kategoriaan j liittyy runo...liitetään uuteen(tee metodi) ja näytetäään runot

    # categ = Category.query.filter_by(aihe=form.aihe.data).first()
    # if not categ :
    #     return render_template("category/other.html", form=form, runo_id=runo.id,
    #                            error="Ei kategoriaa määriteltynä")
    # c_id=categ.id
    # print("kääääääääääääääääääääääääääääääääk",c_id)
    
    return redirect(url_for("runot_showOne_logged", runo_id=runo.id ))

""" #tietyn runon kategorian poisto
@app.route("/category/delete/<category_id>/", methods=["GET", "POST"])
@login_required
def runo_category_delete(category_id, runo):

    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()

    #return redirect(url_for("loggedu_poems"))
    return redirect(url_for("runot_showOne", runo_id=runo.id )) """

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

    return redirect(url_for("runot_showOne_logged", runo_id=runo.id))
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




#TYön
# #uuden kategorian luominen  multiple checkbox
# @app.route("/category/new", methods=["GET","POST"])
# #@login_required
# def category_create():

#     form = CategoryForm(request.form)

#     if form.validate_on_submit():
#          print(form.aihe.data)
#                           # else:
#                           #     print(form.errors)
#                          # return render_template("category/addCategory.html", form=form)

#     if request.method == "GET":
#         return render_template("category/addCategory.html", form=form)

#     form = CategoryForm(request.form)
#     c = Category(aihe=form.aihe.data)
#     print(c)
#                      #t.name=form.name.data
#     list = form.aihe.data
#     print(list)

#     for aihe in list:



#                              #while len(list)> 0:
#                                      #c.aihe = list.pop(0)     
#         c.aihe = item
#                                   #viite?? c.category.id=runo.id
                                    #item.id=runo.id

#         db.session().add(c)
#         db.session().commit()

#         d=Category.query.get(c.id)
#         print('tööt',d)

#     return redirect(url_for("category_index"))



# form = CategoryForm(request.form)
    
#     list = form.aihe.data
#     for aihe in list:
#     category = Category(aihe)

#     db.session().add(category)
#     db.session().commit()
    
#     runo=Runo.query.get(runo_id)
#     runo.categories.append(category)
#     db.session().commit()