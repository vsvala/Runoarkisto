from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    #liitetään käyttäjään runo
    runo = db.relationship("Runo", backref='account', lazy=True, cascade="all, delete-orphan")
    
    
    #liitetään käyttäjään like
    liked = db.relationship("Liked", backref='account', lazy=True, cascade="all, delete-orphan")


    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role   
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

#haetaan kaikki käyttäjät jotka ovat lisänneet runoja
    @staticmethod
    def find_users_with_poem():
        stmt = text("SELECT account.id, account.username FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " GROUP BY account.id"
                    " HAVING COUNT(runo.id) > 0")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1]})

        return response

#haetaan  top 10 ketkä ovat lisänneet eniten runoja
    @staticmethod
    def find_users_with_most_poems():
        stmt = text(" SELECT account.id, account.username, COUNT(runo.id) as runocount FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " WHERE (runo.id>0)"
                    " GROUP BY account.id"
                    " ORDER BY runocount DESC"
                    " LIMIT 10")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "runo_count":row[2]})

        return response


#arkiston käyttäjien määrä
    @staticmethod
    def how_many_users():
        stmt = text("SELECT account.id, COUNT(*) AS howmany FROM account"
                    " LEFT JOIN runo ON runo.account_id = account.id"
                    " GROUP BY account.id")               

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"howmany":row[0]})

        return response


