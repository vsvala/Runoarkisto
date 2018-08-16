from application import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aihe = db.Column(db.String(144), nullable=False)
  
   
def __init__(self, aihe):
      self.aihe = aihe