from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application import app, db, login_manager, login_required
from application.auth.models import User

from application.runot.models import Runo
from application.like.models import Like


@app.route("/likes/<runo_id>", methods=["GET"])
@login_required()
def runot_create_like(runo_id):

    runo = Runo.query.get(runo_id) 
    user=current_user

   #tarkastus onko nykyinen käyttäjä jo tykännyt runosta  jos ei liken talletus kantaan
    liked=Like.has_poem_liked_by_user(user, runo)

    if not liked:
        l=Like(1) #luo olion liken arvolla 1 
        #l.like=1
        l.runo_id=runo.id
        l.account_id=current_user.id
        print(l)
        print(l.like)
        print(l.runo_id)
        print(l.account_id)
        db.session().add(l)
        db.session().commit()

        return render_template("runot/one.html", runo=runo, l=l) 
    #return redirect(url_for("runot_index"))
    return render_template("runot/one.html", runo=runo, liked_message="Samaa runoa voi tykätä vain kerran!!")
    #TODooo tähän molempiin haku ko. runon liket




#TODOO poista testikäytön juttu kun et tarvi enää TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
@app.route("/likes/", methods=["GET"])
def like_index():
    likes = Like.query.all() 
    print(likes)  
    return render_template("likes/like.html", likes=likes, find_poems=Like.find_poems_with_most_likes())
     