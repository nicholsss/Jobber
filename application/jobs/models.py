from application import db
from sqlalchemy.sql import text
from application.models import Base

user_jobs = db.Table('userJobs',
    db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
)


class Job(Base):
    


    name = db.Column(db.String(144), nullable=False)

    salary = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    
    description = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    intrest_user = db.relationship('User', secondary = user_jobs, backref= db.backref('interested'), lazy=True)
    question = db.relationship("Question", backref="job",lazy=True)
    def __init__(self, name,salary,description,account_id):
        self.name = name
        self.salary =salary
        self.description = description
        self.active = False
        self.account_id = account_id

    @staticmethod

    def interested_jobs():
        
    
    @staticmethod
    def jobs_offers():
        stmt = text("SELECT COUNT(job.id) FROM Job")
    
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"count":row[0]})
        
        return response