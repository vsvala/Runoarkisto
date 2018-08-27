from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application import app, db, login_manager, login_required
from application.auth.models import User

from application.runot.models import Runo
from application.like.models import Like


@app.route("/likes/<runo_id>", methods=["GET"])
@login_required()
def runot_create_like(runo_id):

    print("useriiiiiiiiiiiiiiiiiiiii", current_user.id)
    r = Runo.query.get(runo_id)
    print("runooooooooooo", r)
    account_id =current_user.id
    print("tääääääää account id", account_id, "runon id", r.id)

    #li= Like.query.filter_by(account_id=account_id) , Like.query.filter_by(runo_id=r.id).first() )
    
    # user_liked= Like.query.filter_by(account_id=account_id).first() #tarkastetaan onko käyttäjä jo tykännyt runosta 
    # print("ulllllllllllllllllllll",user_liked)  #jos tietokannassa ei vielä ole  runon id:llä oleva tykkäystä talletetaan se sinne
    
    # runo_liked = Like.query.filter_by(runo_id=r.id).first() 
    # print("likeeeeeeeeeeeeeeeeeeeeeeeeeeee",runo_liked)
    # #print("plussaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",runo_liked.like+1)

  
    #if not runo_liked:  # tätä runoa ei tämä käyttäjä ole tykänytt kun käyttäjä ei vielä likennyt tätä runoa talletetaan like tietokantaan ja arvo +1 luo like iden
    #if not user_liked 

    user=current_user

    #tarkastetaan löytyykö tykkäyksiä
    likes=Like.query.all()
    if likes:
        liked=Like.has_poem_liked_by_user(user, r)

    if not liked:
        l=Like(0)
        l.like=1
        l.runo_id=r.id
        l.account_id=account_id
        print(l)
        print(l.like)
        print(l.runo_id)
        print(l.account_id)
        db.session().add(l)
        db.session().commit()

        return render_template("runot/one.html", t=r, l=l)
#tää väis palata takas samaan ja näyttää ko.runon liket..ae ko. runon 
#h.ae ko. runon liket...
    #return render_template("likes/like.html", l=l)
    #return redirect('runot_showOne')
    return render_template("runot/one.html", t=r,)

@app.route("/likes/", methods=["GET"])
def like_index():
    likes = Like.query.all() 
    print(likes)  
    return render_template("likes/like.html", likes=likes, find_poems=Like.find_poems_with_most_likes())