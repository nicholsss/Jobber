from application import db
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

    #@staticmethod
   # def user_intrested_jobs():
        #stmt =  text("SELECT * FROM Account,job,userJobs"
        ##"LEFT JOIN userJobs ON userJobs.account_id = Account.id AND userJobs.job_id = Job_id")
    
        #stmt = text("SELECT * FROM Account A,Job J,Userjobs UJ CASE WHEN WHERE A.account_id = UJ.account_id AND J.job_id = UJ.job_id"
        #"LEFT JOIN  ")
        # JOTAIN TÄllästä alikyselyillä stmt = text("SELECT *, CASE WHEN account.account_id IN userJobs.account_id AND  job.job_id IN userJobs.job_id THEN TRUE ELSE FALSE END FROM account LEFT JOIN userJobs ON ")



        #response = []
        #for row in res:
           # response.append({"id":row[0], "name":row[1],"question":row[2]})

        #return response