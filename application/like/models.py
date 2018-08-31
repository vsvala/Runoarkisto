from application import db
from sqlalchemy.sql import text


class Liked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=False) 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)

    def __init__(self, likes, account_id): 
        self.likes = likes
        self.account_id=account_id

#haetaan tykätyimmät runot top 10 
    @staticmethod
    def find_poems_with_most_likes():
        stmt = text(" SELECT runo.id, runo.name, COUNT(likes) AS total FROM liked, runo, runo_liked"
                    " WHERE runo.id=runo_liked.runo_id AND liked.id=runo_liked.liked_id" 
                    " GROUP BY likes, runo.name, runo.id"
                    " ORDER BY total DESC"
                    " LIMIT 10")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({ "id":row[0], "name":row[1], "total":row[2]})

        return response


#haetaan onko käyttäjä jo likettänyt runoa
    @staticmethod
    def has_poem_liked_by_user(user, runo):
        stmt = text(" SELECT * FROM liked, runo_liked"
                    " WHERE  liked.id=runo_liked.liked_id AND runo_liked.runo_id=:ri AND account_id=:la").params(ri=runo.id, la=user.id)                     

        res = db.engine.execute(stmt)

        response=res.fetchone()

        if response==None:
            return False
        return True    


#haetaan valitun runon tykkäykset
    @staticmethod
    def find_runo_likes(runo):
        stmt = text(" SELECT SUM(likes) AS total FROM liked, runo_liked" 
                    " WHERE liked.id=runo_liked.runo_id AND liked.id=:ri").params(ri=runo.id)     

        res = db.engine.execute(stmt)

        response = res.fetchone()[0]
      
        return response
