from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.category.models import Category
from application.category.forms import  CategoryForm

#yksitttäisen kategorian haku ja näyttö
@app.route("/category/one/<category_id>/", methods=["GET"])
def category_showOne(category_id):
    cate = Category.query.get(category_id)
    print(cate)
    return render_template("category/one.html",  cate=cate)

#kategorioiden listaus
@app.route("/category/", methods=["GET"])
def category_index():
    return render_template("category/list.html", category=Category.query.all())


#uuden kategorian luominen
@app.route("/category/new", methods=["GET","POST"])
#@login_required
def category_create():

    form = CategoryForm(request.form)

    if form.validate_on_submit():
         print(form.aihe.data)
                          # else:
                          #     print(form.errors)
                         # return render_template("category/addCategory.html", form=form)

    if request.method == "GET":
        return render_template("category/addCategory.html", form=form)

    form = CategoryForm(request.form)
    category = Category(aihe=form.aihe.data)

    db.session().add(category)
    db.session().commit()
    
    #jos kategoriaan j liittyy runo...liitetään uuteen(tee metodi) ja näytetäään runot

    categ = Category.query.filter_by(
    aihe=form.aihe.data).first()
    if not categ :
        return render_template("category/addCategory.html", form=form,
                               error="Ei kategoriaa määriteltynä")
    c_id=categ.id
    print("kääääääääääääääääääääääääääääääääk",c_id)
    
    return redirect(url_for("runot_create", c_id=c_id ))


#kategorian muokkaus lomakkeen haku
@app.route("/category/<category_id>/", methods=["GET"])
@login_required
def category_uppdateForm(category_id):

    c = Category.query.get(category_id)
    form = CategoryForm(request.form) 

    return render_template("category/addCategory.html", c=c, form=form)


#kategorian muokkaaminen
@app.route("/category/<category_id>/", methods=["POST"])
@login_required
def category_uppdate(category_id):

    cate = Category.query.get(category_id)
    form = CategoryForm(request.form)
    
    if form.validate_on_submit():
        print(form.aihe.data)
                          # else:
                          #     print(form.errors)
                         # return render_template("category/addCategory.html", form=form)

    if request.method == "GET":
        return render_template("category/addCategory.html", form=form)

    form = CategoryForm(request.form)
    cate.aihe = form.aihe.data

    db.session().commit()
    

    categ = Category.query.filter_by(
    aihe=form.aihe.data).first()
    if not categ :
        return render_template("category/addCategory.html", form=form,
                               error="Ei kategoriaa määriteltynä")
    c_id=categ.id
    print("kääääääääääääääääääääääääääääääääk",c_id)
    return redirect(url_for("category_create", c_id=c_id ))




#kategorian poisto
@app.route("/category/<category_id>/delete/", methods=["GET", "POST"])
@login_required
def category_delete(category_id):

    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("category_index"))


# #uuden kategorian luominen
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

#     for item in list:
#                              #while len(list)> 0:
#                                      #c.aihe = list.pop(0)     
#         c.aihe = item
#                                 #viite?? c.category.id=runo.id

#         db.session().add(c)
#         db.session().commit()

#         d=Category.query.get(c.id)
#         print('tööt',d)

#     return redirect(url_for("category_index"))
