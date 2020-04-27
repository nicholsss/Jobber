from application import db
from application.models import Base

class Question(Base):

    content = db.Column(db.String(144), nullable=False)
    #answer = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"), nullable=False)
    def __init__(self, account_id, job_id,content):
        self.account_id = account_id
        self.job_id =job_id
        self.content = content
       