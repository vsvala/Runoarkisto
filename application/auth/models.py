from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    runo = db.relationship("Runo", backref='account', lazy=True)
  

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role=role   
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_poem():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Runo ON Runo.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Runo.id) > 0")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def how_many_users():
        stmt = text("SELECT Account.id, COUNT(*) AS howmany FROM Account"
                    " LEFT JOIN Runo ON Runo.account_id = Account.id"
                    " GROUP BY Account.id")               

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"howmany":row[0]})

        return response

#voisko tässä/initissä luoda tyhjän databasin käynnistäessä automaattisesti ADMiN userin, jos ei ole olemassa

