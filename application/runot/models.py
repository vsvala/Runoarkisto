from application import db
from application.models import Base
from application.category import models
from flask_login import current_user
from sqlalchemy.sql import text

# Määritetään mallit tietokantataululle.

categories_c = db.Table('categories',
        db.Column('runo_id', db.Integer, 
        db.ForeignKey('runo.id'), primary_key=True ),
        db.Column('category_id', 
        db.Integer, db.ForeignKey('category.id'), primary_key=True))

class Runo(Base):

    name = db.Column(db.String(144), nullable=False, unique=True) 
    sisalto = db.Column(db.String(2000), nullable=False) 
    runoilija = db.Column(db.String(100), nullable=False) 

   # Liitetään käytäjälle runo
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)


    # Määritellään many to many riippuvuussuhde  kategorioiden kanssa. 
    categories = db.relationship('Category', secondary=categories_c, lazy='subquery', cascade="all, delete-orphan", single_parent=True,
        backref=db.backref('runot', lazy=True))   


    def __init__(self, name, sisalto, runoilija): 
       self.name = name
       self.sisalto= sisalto
       self.runoilija = runoilija

  
    @staticmethod
    def find_loggedUsers_poems():

        stmt = text("SELECT runo.id, runo.name, runo.sisalto, runo.runoilija FROM Runo"
                    " WHERE account_id=:cid").params(cid=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "sisalto":row[2], "runoilija":row[3]})

        return response


    @staticmethod
    def find_runot_by_category(category):
       
        stmt = text("SELECT DISTINCT runo.id, runo.name, runo.sisalto, runo.runoilija FROM category, categories, Runo" 
                    " WHERE (Runo.id=categories.runo_id AND categories.category_id=category.id AND category.aihe=:categ)").params(categ=category)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "sisalto":row[2], "runoilija":row[3]})

        return response

    # @staticmethod
    # def search_poem():

    #     stmt = text("SELECT runo.name, runo.id FROM Runo"
    #                 " WHERE account_id=:cid").params(cid=current_user.id)

    #     res = db.engine.execute(stmt)
  
    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "name":row[1]})

    #     return response