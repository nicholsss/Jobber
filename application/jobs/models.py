from application import db
from application.models import Base

#user_jobs = db.Table('userJobs',
    #db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
    #db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
#)


class Job(Base):
    


    name = db.Column(db.String(144), nullable=False)

    salary = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    
    description = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    #r = db.relationship('account', secondary = user_jobs, backref= db.backref('jobs'), lazy=True)
    question = db.relationship("Question", backref="job",lazy=True)
    def __init__(self, name,salary,description,account_id):
        self.name = name
        self.salary =salary
        self.description = description
        self.active = False
        self.account_id = account_id