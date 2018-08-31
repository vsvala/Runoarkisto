from application import db
from application.models import Base
from application.category import models
from application.like import models
from flask_login import current_user
from sqlalchemy.sql import text

# Määritetään mallit tietokantataululle.

# Kategorian ja runon liitostaulu many to many
categories_c = db.Table('categories',
        db.Column('runo_id', db.Integer, 
        db.ForeignKey('runo.id'), primary_key=True ),
        db.Column('category_id', 
        db.Integer, db.ForeignKey('category.id'), primary_key=True))


# Liken ja runon liitostaulu many to many
liked_l = db.Table('runo_liked',
        db.Column('runo_id', db.Integer,
        db.ForeignKey('runo.id'), primary_key=True ),
        db.Column('liked_id', 
        db.Integer, db.ForeignKey('liked.id'), primary_key=True))


class Runo(Base):

    name = db.Column(db.String(144), nullable=False, unique=True) 
    sisalto = db.Column(db.String(2000), nullable=False) 
    runoilija = db.Column(db.String(100), nullable=False) 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)

    # Määritellään many to many riippuvuussuhde  kategorioiden kanssa. #cascade="all, delete-orphan", single_parent=True
    categories = db.relationship('Category', secondary=categories_c, lazy='subquery', 
        backref=db.backref('runot', lazy=True))   

       # Määritellään many to many riippuvuussuhde  likejen kanssa. 
    runo_liked = db.relationship('Liked', secondary=liked_l, lazy='subquery',cascade="all, delete-orphan", single_parent=True,
        backref=db.backref('runot', lazy=True))   


    def __init__(self, name, sisalto, runoilija): 
       self.name = name
       self.sisalto= sisalto
       self.runoilija = runoilija


  #haetaan kirjautuneen käyttäjän runot
    @staticmethod
    def find_loggedUsers_poems():

        stmt = text("SELECT runo.id, runo.name, runo.sisalto, runo.runoilija FROM runo"
                    " WHERE account_id=:cid"
                    " ORDER BY runo.date_created DESC").params(cid=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "sisalto":row[2], "runoilija":row[3]})

        return response

#haetaan runot annetun kategorian mukaan
    @staticmethod
    def find_runot_by_category(category):
       
        stmt = text("SELECT DISTINCT runo.id, runo.name, runo.sisalto, runo.runoilija FROM category, categories, runo" 
                    " WHERE (runo.id=categories.runo_id AND categories.category_id=category.id AND category.aihe=:categ)").params(categ=category)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "sisalto":row[2], "runoilija":row[3]})

        return response

#haetaan tietyn käyttäjän runot
    @staticmethod
    def find_runot_by(user):
        stmt = text("SELECT DISTINCT runo.id, runo.name FROM runo, account"
                     " WHERE (runo.account_id =:u)").params(u=user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response