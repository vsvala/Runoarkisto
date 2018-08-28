from application import db
from sqlalchemy.sql import text

class Liked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=False) 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
    runo_id = db.Column(db.Integer, db.ForeignKey('runo.id'),nullable=False)

    def __init__(self, likes):
      self.likes = likes



#haetaan tykätyimmät runot top 10 
    @staticmethod
    def find_poems_with_most_likes():
        stmt = text(" SELECT runo.name AS runo, COUNT(likes) AS total FROM liked, runo"
                    " WHERE runo.id=liked.runo_id"
                    " GROUP BY likes, runo.name"
                    " LIMIT 10")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "total":row[1]})

        return response


#haetaan onko käyttäjä jo likettänyt runoa
    @staticmethod
    def has_poem_liked_by_user(user, runo):
        stmt = text(" SELECT * FROM liked"
                    " WHERE liked.runo_id=:ri AND liked.account_id=:la").params(ri=runo.id, la=user.id)
                   

        res = db.engine.execute(stmt)

        response=res.fetchone()

        if response==None:
            return False
        return True    


#haetaan valitun runon tykkäykset
    @staticmethod
    def find_runo_likes(runo):
        stmt = text(" SELECT SUM(likes) AS total FROM liked"
                    " WHERE liked.runo_id=:ri").params(ri=runo.id)     

        res = db.engine.execute(stmt)

        response = res.fetchone()[0]
      
        return response

# #haetaan valitun runon tykkäysten määrä  
#     @staticmethod
#     def find_poems_likes(runo):
#         stmt = text(" SELECT runo.name AS runo, COUNT(likes) AS total FROM liked, runo"
#                     " WHERE runo.id=:ri"
#                     " GROUP BY likes, runo.name"
#                     ).params(ri=runo.id)

#         res = db.engine.execute(stmt)
  
#         response = []
#         for row in res:
 
#    response.append({"name":row[0], "total":row[1]})

#         return response
