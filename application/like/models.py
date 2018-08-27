from application import db
from sqlalchemy.sql import text

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, nullable=False) 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    runo_id = db.Column(db.Integer, db.ForeignKey('runo.id'),nullable=False)

    def __init__(self, like):
      self.like = like



#haetaan tykätyimmät runot top 10 
    @staticmethod
    def find_poems_with_most_likes():
        stmt = text(" SELECT runo.name AS runo, SUM(like) AS total FROM like, runo"
                    " WHERE Runo.id=like.runo_id"
                    " GROUP BY like, runo_id"
                    " LIMIT 10")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "total":row[1]})

        return response


#haetaan onko käyttäjä jo likettänyt runoa
    @staticmethod
    def has_poem_liked_by_user(user, runo):
        stmt = text(" SELECT *  FROM like"
                    " WHERE like.runo_id= :ri AND like.account_id= :la").params(ri=runo.id, la=user.id)
                    

        res = db.engine.execute(stmt)

        response=res.fetchone()

        if response==None:
            return False
        return True    

