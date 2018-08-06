from application import db

class Runo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False) 
    sisalto = db.Column(db.String(2000), nullable=False) 
    runoilija = db.Column(db.String(100), nullable=False) 

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

def __init__(self, name, sisalto, runoilija): 
       self.name = name
       self.sisalto= sisalto
       self.runoilija = runoilija