from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User
from application.category.models import Category
from application.runot.models import Runo

from werkzeug import secure_filename
from application.runot.forms import RunoForm, FindForm, SaveForm, UploadForm, RunoUpdateForm

#yksitttäisen runon näyttö
@app.route("/runot/one/<runo_id>/", methods=["GET"])
def runot_showOne(runo_id):
    t = Runo.query.get(runo_id)
    print(t)
    return render_template("runot/one.html", t=t)

@app.route("/runot/one/logged/<runo_id>/", methods=["GET"])
def runot_showOne_logged(runo_id):
    runo = Runo.query.get(runo_id)
    return render_template("runot/modifyOne.html", runo=runo, category_by=Category.find_categories_by(runo))


#runojen listaus
@app.route("/runot/", methods=["GET"])
def runot_index():
    return render_template("runot/list.html", runot=Runo.query.all())

#TODOOO.........nää pitäis laittaa vielä uusin ensin järjestykseen
#kirjautuneen käyttäjän runojen listaus
@app.route("/runot/listings/b")
@login_required()
def loggedu_poems():
    return render_template("runot/loggedlist.html", loggedUsers_poems =Runo.find_loggedUsers_poems())



# #uuden runon luomislomakkeen haku 
# @app.route("/runot/uusi/<c_id>/", methods=["GET"]) # @app.route("/runot/uusi")
# # @login_required()
# def runot_form(c_id):
#     form=RunoForm()
#     return render_template("runot/uusi.html", form=RunoForm(), c_id=c_id)


# luomislomakkeen näyttö alkuun ja runon luominen
@app.route("/runot/form/", methods=["GET"])
@login_required()
def runot_createform():

    if request.method == "GET":
         return render_template("runot/uusi.html", form= RunoForm())
    

#kategoria ja runo olion luominen lomaketiedoista, tallennustietokantaan ja liitokset
@app.route("/runot/uusi/create/", methods=["GET","POST"])
@login_required()
def runot_create():

    form = RunoForm(request.form)

    #lomakkeen validointi
    if form.validate_on_submit():
         print(form.aihe.data)
    else:
        print(form.errors)
        return render_template("runot/uusi.html", form=form)

    #kategoria olion luonti ja lisäys kantaan
    category = Category(aihe=form.aihe.data)

    db.session().add(category)
    db.session().commit()

    # runo-olio t:n luonti lomakesyötteestä
    t = Runo(name=form.name.data, sisalto=form.sisalto.data,runoilija=form.runoilija.data)

    #validoidaan samannimiset tietokannasta jos löytyy render lomake uusiks ja error
    runo= Runo.query.filter_by(name=t.name).first()
    if runo:
        return render_template("runot/uusi.html", form=form, name_error= "Samanniminen runo on jo arkistossaaa!")

    # luodaan monesta moneen iitokset runon ja kategorian välilleja talletetaan runo kantaan
    t.account_id = current_user.id
    t.categories.append(category) 

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("loggedu_poems"))


#runon muokkaus lomakkeen haku
@app.route("/runot/<runo_id>", methods=["GET"])
@login_required()
def runot_uppdateForm(runo_id):

    runo = Runo.query.get(runo_id)
    form = RunoUpdateForm(obj=runo) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

    return render_template("runot/muokkaa.html", runo=runo, form=form)

#runon muokkaus 
@app.route("/runot/<runo_id>/", methods=["GET","POST"])
@login_required()
def runot_uppdate(runo_id):

    runo = Runo.query.get(runo_id)
    #print("runooooooooooooooooooooo", runo)

    form = RunoUpdateForm(request.form)

#TOdo VLA*IDO*INTI   ?????????...tässä jotain häikkää...
    # if form.validate_on_submit():
    #     print("ok")
    # else:
    #     print(form.errors)
   
    # if not form.validate():
    #     print("not validateeeeeeeeeeeeeeeeee")
    #     #return redirect(url_for("runot_uppdateForm",runo_id=runo.id))
    #     return render_template("runot/muokkaa.html", runo=runo,form=form)

    runo.name=form.name.data
    runo.sisalto=form.sisalto.data
    runo.runoilija=form.runoilija.data
    runo.account_id = current_user.id 


    db.session().commit()

#TODOOO mieti näyttäisikö tässä yksittäisenä muokatun runon??? niin sopisi kumpaankin muokkaustilanteesen
    #return redirect(url_for("runot_showOne", runo_id=runo.id))
    return render_template("runot/modifyOne.html", runo=runo, category_by=Category.find_categories_by(runo))

#poistaa(admin) listasta
@app.route("/runot/<runo_id>/del/", methods=["GET", "POST"])
@login_required()
def runot_one_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("runot_index"))


#poistaa( runon userin listasta
@app.route("/runot/<runo_id>/delete/", methods=["GET", "POST"])
@login_required()
def runot_delete(runo_id):

    t = Runo.query.get(runo_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("loggedu_poems"))

#näyttää haku lomakkeen
@app.route("/runot/find/", methods=["GET"])
def find_index():
        return render_template("runot/find.html", form=FindForm())
    
#hakee annetun runon
@app.route("/runot/find/", methods=["POST"])
def find_runo():
    form = FindForm(request.form)
    runo_name=form.name.data
    runo_category=form.category.data
    #runo = Runo.query.filter_by(name=find).first()

    if runo_name: 
        runo= Runo.query.filter_by(name=runo_name).first()
        if not runo:
            return render_template("runot/find.html", form=form, name_error="Etsimälläsi nimellä ei löydy runoa arkistosta, etsi toisella nimellä!")
    
    if runo_category:
        return redirect(url_for("find_runot_by_category", runo_category=runo_category))
        #runot= Runo.query.filter_by(category=runo_category).first()
        #print("runooooooooooooooooooooooooooooot",runot))

    #if runo_name and runo_category: 
    #Todo....JOS MOLEMMAT syötett  TIETOKANTAKYSELY? VAI MENEEKÖ QURYLLÄ EHKÄ? Annetun niminen runo annetulla kategorialla
    # SIITÄ ETTÄ NIMI ON NIMI JA KATEGORIA KATEGORI

    form = FindForm(request.form)
    return render_template("runot/find.html", runo=runo, form=form)
 
#hakee tietyn kategorian runot
@app.route("/runot/find/<runo_category>")
def find_runot_by_category(runo_category):
    form = FindForm(request.form)
    category=runo_category
    if not Runo.find_runot_by_category(category):
        print("ei löydyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        return render_template("runot/find.html", form=form, category_error="Etsimälläsi kategorialla ei löydy runoja, yritä toista hakusanaa!")

    return render_template("runot/find.html", runot_by_category = Runo.find_runot_by_category(category), category=category, form=form)

#hakee tietyn runon kategoriat
@app.route("/runot/one/<runo_id>/a",methods=["GET"])
def find_categories(runo_id):
    t = Runo.query.get(runo_id)
    return render_template("runot/one.html", category_by =Category.find_categories_by(t), t=t)

#hakee tietyn käyttäjän runojen kategoriat
@app.route("/runot/listing/<runo_id>/a",methods=["GET"])
def listing_find_categories(runo_id):
    runo = Runo.query.get(runo_id)
    return render_template("runot/listings.html", category_by =Category.find_categories_by(runo), runo=runo)


#Todo..............::::::::::::::::::::::mieti seuraavia näitä ollenkaan

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

