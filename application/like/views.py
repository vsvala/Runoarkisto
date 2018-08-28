from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application import app, db, login_manager, login_required
from application.auth.models import User

from application.runot.models import Runo
from application.like.models import Liked


#top 10 listaus
@app.route("/likes/top/", methods=["GET"])
def top_poems():
    find_poems=Liked.find_poems_with_most_likes()
    return render_template("runot/top.html", find_poems= find_poems )


@app.route("/likes/<runo_id>", methods=["GET"])
@login_required()
def runot_create_like(runo_id):

    runo = Runo.query.get(runo_id) 
    user=current_user

   #tarkastus onko nykyinen käyttäjä jo tykännyt runosta  jos ei liken talletus kantaan
    liked=Liked.has_poem_liked_by_user(user, runo) #true tai false
    print("llllllllllllllllllllllllllllllllll")

    if liked==False:
        l=Liked(1) #luo olion liken arvolla 1 
        l.likes=1
        l.runo_id=runo.id
        l.account_id=current_user.id
        print(l)
        print(l.likes)
        print(l.runo_id)
        print(l.account_id)
        db.session().add(l)
        db.session().commit()

        print("luo likeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeen", l)
        return redirect(url_for('runot_showOne', runo_id=runo.id, l=l))
        #return render_template("runot/one.html", runo=runo, l=l) 
    
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeel") 

    return render_template("runot/one.html", runo=runo, liked_message="Samasta runosta voi tykätä vain kerran!!")
    #TODooo tähän molempiin haku ko. runon liket
