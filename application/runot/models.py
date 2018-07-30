from application import db

class Runo(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False) 
    sisalto = db.Column(db.String(2000), nullable=False) 
    runoilija = db.Column(db.String(100), nullable=False) 

    def __init__(self, name, sisalto, runoilija): 
       self.name = name
       self.sisalto= sisalto
       self.runoilija = runoilija