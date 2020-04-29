from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False, unique=True)
    password_hash = db.Column(db.String(144), nullable=False)
    roles = db.Column(db.String(144), nullable=False)
    jobs = db.relationship("Job", backref="account",lazy=True)
    question = db.relationship('Question', backref="account")
    
    def __init__(self,username,password, roles):
       # self.name = name
        self.username = username
        self.password_hash = generate_password_hash(password)       
        self.roles = roles

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def most_questions_asked():
        stmt = text("SELECT Account.id, Account.username, COUNT(Question.id) FROM Account"
                " LEFT JOIN Question ON Question.account_id = Account.id"
                " GROUP BY Account.id"
                " HAVING COUNT(Question.id) >0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1],"question":row[2]})

        return response
    #Eniten tienannut

    #Eniten töistä kiinnostunut
