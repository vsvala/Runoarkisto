from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application import app, db, login_manager, login_required
from application.auth.models import User

from application.runot.models import Runo
from application.like.models import Liked


#top 10 listaus
@app.route("/likes/top/", methods=["GET"])
def top_poems():
    top=Liked.find_poems_with_most_likes()
    return render_template("runot/top.html", top= top)

#luodaan tykkäyksiä
@app.route("/create/likes/<runo_id>/", methods=["GET", "POST"])
@login_required()
def create_like(runo_id):

    runo = Runo.query.get(runo_id) 
    user=current_user

   #tarkastus onko nykyinen käyttäjä jo tykännyt runosta  jos ei liken talletus kantaan muutoin viesti
    liked=Liked.has_poem_liked_by_user(user, runo) #true tai false   ###ei ielä toimi kunnolla...
    print("llllllllllllllllllllllllllllllllll")
   
    if liked==False:
        like=Liked(1) #luo olion liken arvolla 1 
        db.session().commit()


        #like.id=runo.id
        #like.likes=1
        like.account_id=current_user.id
        db.session().add(like)
        db.session().commit()

        runo.runo_liked.append(like) 
        db.session().add(runo)
        db.session().commit()

        return redirect(url_for('runot_one', runo_id=runo.id, l=like))

    else:
        return render_template("runot/one.html", runo=runo, liked_message="Olet jo tykännyt tästä runosta! Samasta runosta voi tykätä vain kerran!!")


#kaikkien tykkäysten poisto
@app.route("/likes/delete/all/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def delete_likes():

    likes=Liked.query.all()
    for like in likes:
        db.session().delete(like)
    db.session().commit()

    return redirect(url_for("top_poems"))

