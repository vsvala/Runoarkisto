from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User
from application.category.models import Category
from application.runot.models import Runo
from application.like.models import Liked

#from werkzeug import secure_filename
from application.runot.forms import RunoForm, FindForm

# kaikkien runojen  listaus aakkosittain ja sivuttaminen paginate 20 kerrallaan, ja käyttäjien lkm haku
@app.route("/runot/", defaults={'page': 1})
@app.route("/runot/page/<int:page>/")
def runot_index(page):
    per_page = 10
    runot=Runo.query.order_by(Runo.name).paginate(page, per_page, error_out=False)#Runo.query.all()
    lkm_runot= Runo.query.count()
    return render_template("runot/list.html", runot=runot, lkm_runot = lkm_runot) 

 # Ŕunojen top 10 lista ja tykkäkset
@app.route("/runot/top/<runo_id>/", methods=["GET"])
def show_toplist(runo_id):
    runo = Runo.query.get(runo_id)
    likes=Liked.query.all()
    if likes:
        top=Liked.find_poems_with_most_likes()
        l=Liked.find_runo_likes(runo)
        return render_template("runot/one.html", top=top, l=l, runo=runo)
    return render_template("runot/one.html", runo=runo)


#yksitttäisen runon näyttö ja tykkäyksien haku
@app.route("/runot/one/<runo_id>/", methods=["GET"])
def runot_one(runo_id):
    runo = Runo.query.get(runo_id)
    likes=Liked.query.all()
    if likes:
        l=Liked.find_runo_likes(runo)
        if l:
            return render_template("runot/one.html", runo=runo, l=l)  
    return render_template("runot/one.html", runo=runo, l=l, liked_message="Samasta runosta voi tykätä vain kerran!")

#kirjautuneen käyttäjän runojen listaus viimeksi luotu ensin
@app.route("/runot/loggedlist/")
@login_required()
def loggedu_poems():
    return render_template("runot/loggedlist.html", loggedUsers_poems =Runo.find_loggedUsers_poems())


 #kirjautuneen käyttäjän yksittäisen runon näyttö 
@app.route("/runot/showOne/logged/<runo_id>/", methods=["GET"])
def runot_showOne_logged(runo_id):
    runo = Runo.query.get(runo_id)
    return render_template("runot/one_logged.html", runo=runo, category_by=Category.find_categories_by(runo))


# runon luomislomakkeen haku
@app.route("/runot/new/", methods=["GET"])
@login_required()
def runot_createform():
    if request.method == "GET":
         return render_template("runot/new.html", form= RunoForm())


#kategoria ja runo olion luominen lomaketiedoista, tallennustietokantaan ja liitokset
@app.route("/runot/new/create/", methods=["GET","POST"])
@login_required()
def runot_create():
    form = RunoForm(request.form)

    #validoidaan eka otsikon kirjain isoksi (aakkostamisen takia,,,) 
    n=form.name.data
    bool=n[0].isupper()
    print("booooooooooooooool", bool)
    if bool==False:
        print("faaaaaaaaaaaaaaaaaaaaalssssssssssssssssssssssseeeee")
        return render_template("runot/new.html", form=form, capital_error= "Aloita otsikko isolla kirjaimella!")

    #lomakkeen validointi
    if not form.validate():
        return render_template("runot/new.html", form=form)
 
    #  runo-olion luonti lomakesyötteestä
    runo = Runo(name=form.name.data, sisalto=form.sisalto.data,runoilija=form.runoilija.data)

    #validoidaan samannimiset jos nimi löytyy  kannasta render lomake uusiks ja error
    r= Runo.query.filter_by(name=runo.name).first()
    if r:
        return render_template("runot/new.html", form=form, name_error= "Samanniminen runo on jo arkistossa!")
   
   #lisää  kategoriat  tietokantaan checklistalta, luodaan monesta moneen liitokset runon ja kategorian välille ja talletetaan runo kantaan    
    runo.account_id = current_user.id  #liitetään tili nykyiseen käyttäjään
    
    #tsekataan että kategoria valittuna
    categories_list=form.aihe.data
    if not categories_list:
        return render_template("runot/new.html", form=form, category_error= "Valitse väintään yksi kategorioista!")


    for  aihe in  categories_list:
        category = Category(aihe) #luodaan kategoria olio jokaisetsa listan kategoriasta ja lisätään kantaan
        db.session().add(category)             
        db.session().commit()

        runo.categories.append(category) 
        db.session().add(runo)
        db.session().commit()

    return redirect(url_for("loggedu_poems"))


#runon muokkaustilaan ohjaus
@app.route("/runot/modifyOne/<runo_id>/", methods=["GET"])
@login_required()
def runo_modify_page(runo_id):

    runo = Runo.query.get(runo_id)
    return render_template("runot/modifyOne.html", runo=runo, category_by=Category.find_categories_by(runo))


#runon muokkaus lomakkeen haku
@app.route("/runot/modify/<runo_id>/", methods=["GET"])
@login_required()
def runot_uppdateForm(runo_id):

    runo = Runo.query.get(runo_id)
    form = RunoForm(obj=runo) # Täytetään lomake tietokannasta löytyvillä runon tiedoilla

    return render_template("runot/muokkaa.html", runo=runo, form=form)


#runon muokkaus 
@app.route("/runot/<runo_id>/", methods=["GET","POST"])
@login_required()
def runot_uppdate(runo_id):

    runo = Runo.query.get(runo_id)

    form = RunoForm(request.form)
   
    if not form.validate():
        print("not validateeeeeeeeeeeeeeeeee")
        return render_template("runot/muokkaa.html", runo=runo,form=form)

    runo.name=form.name.data
    runo.sisalto=form.sisalto.data
    runo.runoilija=form.runoilija.data
    runo.account_id = current_user.id 

    db.session().commit()

    return render_template("runot/modifyOne.html", runo=runo, category_by=Category.find_categories_by(runo))


#poistaa runon poistajan(admin) tai(user)
@app.route("/runot/<runo_id>/del/", methods=["GET", "POST"])
@login_required()
def runot_delete(runo_id):

    runo = Runo.query.get(runo_id)
    db.session().delete(runo)
    db.session().commit()

    if current_user.role=="ADMIN":
        return redirect(url_for("runot_index"))
    if current_user.role=="USER":
        return redirect(url_for("loggedu_poems"))
        #return render_template("runot/modifyOne.html", runo=runo, category_by=Category.find_categories_by(runo))


#näyttää runon haku lomakkeen
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

    
    if not runo_name or runo_category:
        return render_template("runot/find.html", form=form, name_error="Syötä jompikumpi tiedoista!")
    
  
    form = FindForm(request.form)
    return render_template("runot/find.html", runo=runo, form=form)
 

#hakee tietyn kategorian runot
@app.route("/runot/find/<runo_category>")
def find_runot_by_category(runo_category):
    form = FindForm(request.form)
    category=runo_category
    if not Runo.find_runot_by_category(category):
        return render_template("runot/find.html", form=form, category_error="Etsimälläsi kategorialla ei löydy runoja, yritä toista hakusanaa!")

    return render_template("runot/find.html", runot_by_category = Runo.find_runot_by_category(category), category=category, form=form)


#hakee tietyn runon kategoriat
@app.route("/runot/category/<runo_id>/",methods=["GET"])
def find_categories(runo_id):
    runo = Runo.query.get(runo_id)    
    #return render_template("runot/list.html", runot=runot)
    category_by =Category.find_categories_by(runo)
    return redirect(url_for("runot_index_category",category_by=category_by))


#hakee tietyn käyttäjän runot
@app.route("/runot/user/<user_id>/a",methods=["GET"])
def users_poems(user_id):
    user= User.query.get(user_id)
    print(user)
    return render_template("auth/list.html", runot_by =Runo.find_runot_by(user), how_many=User.find_users_with_poem(), users=User.query.all())

# hakee  runojen ja käyttäjien määrät ja ohjaa tialstosivulle
@app.route("/runot/stats/", methods=["GET"])
@login_required(role="ADMIN")
def stats_index():
    lkm_users= User.query.count()
    lkm_runot= Runo.query.count()
    return render_template("runot/stats.html", lkm_users=lkm_users, lkm_runot=lkm_runot,  most_poems=User.find_users_with_most_poems())
