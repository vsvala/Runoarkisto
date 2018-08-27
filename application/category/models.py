from application import db
from sqlalchemy.sql import text

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aihe = db.Column(db.String(144), nullable=False)
  
   
    def __init__(self, aihe):
      self.aihe = aihe

    #haetaan runon kategoriat runon nimen perusteella
    @staticmethod
    def find_categories_by(t):
     
        stmt = text("SELECT DISTINCT category.id, category.aihe FROM runo, categories, Category" 
                    " WHERE (Category.id=categories.category_id AND categories.runo_id=runo.id AND runo.name=:nimi)").params(nimi=t.name)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "aihe":row[1]})

        return response