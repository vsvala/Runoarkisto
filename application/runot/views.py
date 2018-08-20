from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User
from application.category.models import Category
from application.runot.models import Runo

from werkzeug import secure_filename
from application.runot.forms import RunoForm, FindForm, SaveForm, UploadForm

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
@login_required(role="USER")
def runot_create(c_id):

    if request.method == "GET":
        return render_template("runot/uusi.html", form=RunoForm(), c_id=c_id)

    form = RunoForm(request.form)
    
    if not form.validate():
        return render_template("runot/uusi.html", form=form, c_id=c_id, name_error="Saman niminen runo on jo arkistossa!")

    runo= Runo.query.filter_by(name=form.name.data).first()
    if runo:
        return redirect(url_for("runot_create", form=RunoForm(),c_id=c_id, name_error="Saman niminen runo on jo arkistossa!"))

    t = Runo(name=form.name.data, sisalto=form.sisalto.data,
             runoilija=form.runoilija.data)

    t.account_id = current_user.id


    category=Category.query.get(c_id)
    t.categories.append(category)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("runot_index"))

#runon muokkaus lomakkeen haku
@app.route("/runot/<runo_id>", methods=["GET"])
@login_required()
def runot_uppdateForm(runo_id):

    t = Runo.query.get(runo_id)
    form = RunoForm(obj=t) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

    return render_template("runot/muokkaa.html", t=t, form=form)

#runon muokkaus
@app.route("/runot/<runo_id>/", methods=["POST"])
@login_required()
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
@login_required()
def runot_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("runot_index"))

#hakee käyttäjät jotka ovat lisänneet runoja
@app.route("/runot/listings/a")
@login_required() #(role="ADMIN")
def users_withPoems():
     return render_template("runot/listings.html", how_many=User.find_users_with_poem())

#hakee kirjautuneen käyttäjä runot
@app.route("/runot/listings/b")
@login_required()
def loggedu_poems():
    return render_template("runot/listings.html", loggedUsers_poems =Runo.find_loggedUsers_poems())

#hakee tietyn kategorian runot
@app.route("/runot/listings/c")
@login_required()
def find_runot_by_category():
    return render_template("runot/listings.html", runot_by_category =Runo.find_runot_by_category())

@app.route("/runot/one/<runo_id>/2",methods=["GET"])
@login_required()
def find_categories(runo_id):
    t = Runo.query.get(runo_id)
    return render_template("runot/one.html", category_by =Category.find_categories_by(), t=t)

#näyttää haku lomakkeen
@app.route("/runot/find/", methods=["GET"])
def find_index():
        return render_template("runot/find.html", form=FindForm())
    
#hakee annetun runon
@app.route("/runot/find/", methods=["POST"])
def find_runo():
    form = FindForm(request.form)
    runo_name=form.name.data
    #runo = Runo.query.filter_by(name=find).first()

    if runo_name: 
        runo= Runo.query.filter_by(name=runo_name).first()
        if not runo:
            return render_template("runot/find.html", form=form, name_error="Nimeämääsi runoa ei löydy arkistosta!")

    form = FindForm(request.form)
    return render_template("runot/find.html", runo=runo, form=form)
 
#näyttää save lomakkeen
@app.route("/runot/save/", methods=["GET"])
@login_required()
def save_index():
        return render_template("runot/save.html", form=SaveForm())

#tallentaa annetun runon nimettyyn tekstitiedotoon
@app.route("/runot/save/", methods=["POST"])
@login_required()
def save_runo():
    form = SaveForm(request.form)
    find=form.name.data
    runo = Runo.query.filter_by(name=find).first()

# Test whether variable is defined to be None
    try:
        runo
    except NameError:
        runo = None
    if runo is None:
        print("Kyseistä runoa ei löydy arkistosta")

    file_name=form.file.data
    tiedosto = open(file_name, "wt")  #avataan ja luodaan tekstitiedosto annetulla nimellä
    for rivi in runo.sisalto: #kirjoitetaan teoslistan tiedot tekstitiedostoon allekkain
        tiedosto.write(str(rivi)) 
        tiedosto.write("\n") 
    tiedosto.close() #suljetaan tiedosto
     
     #Varmistetaan että tiedot tallentuivat tekstitiedostoon tulostamalla luotu tiedosto
    tiedosto = open(file_name, "rt")# avaa tiedosto luettavaksi
    print("Tallensit seuraavan runon: ", runo.name ,"tiedostoon nimeltä: ", file_name)
    for rivi in tiedosto: # tulostaa talletetum tiedoston rivi kerrallaan
        print(rivi[:-1])
    tiedosto.close()#sulje tiedosto

    form = SaveForm(request.form)
    return render_template("runot/save.html", runo=runo, form=form)

#näyttää load lomakkeen
@app.route("/runot/load/", methods=["GET"])
@login_required()
def load_index():
        return render_template("runot/load.html", form=UploadForm())

# #lisää runon tekstitiedostosta
# @app.route("/runot/load/", methods=['GET', 'POST'])
# @login_required
# def load_runo():
#     form = UploadForm(request.form)
#     f=form.fil.data
#     print("TKKKKKKKKKKKKKKKKKKKKK",f)
#     #if form.validate_on_submit():
#     filename = secure_filename(f.filename)
#     #form.file.data.save('runot/load/' + filename)
#     #Varmistetaan että tiedot tallentuivat tekstitiedostoon tulostamalla luotu tiedosto
#     tiedosto = open(filename, "rt")# avaa tiedosto luettavaksi
#     for rivi in tiedosto: # tulostaa talletetum tiedoston rivi kerrallaan
#         print(rivi[:-1])
#     tiedosto.close()#sulje tiedosto

#     #return render_template('runot/load.html', form=form)
#     #return redirect(url_for('load_index'))
#     return render_template("runot/load.html", form=UploadForm(), filename=filename)

     
#      #Varmistetaan että tiedot tallentuivat tekstitiedostoon tulostamalla luotu tiedosto
#     tiedosto = open(filename, "rt")# avaa tiedosto luettavaksi
#     for rivi in tiedosto: # tulostaa talletetum tiedoston rivi kerrallaan
#         print(rivi[:-1])
#     tiedosto.close()#sulje tiedosto

#     form = SaveForm(request.form)

#     return render_template('runot/upload.html', form=form)


#työnalla
#lasketaan montako runoa tietokannasta löytyy
# @app.route("/runot/listings/c")
# @login_required
# def count_runo():
#     return render_template("runot/listings.html", find_poem=User.search_poem())

