from application import db

#Tämä liittää monesta moneen ei puuttuu backref.
#works = db.Table('works',
#db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
#db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True)
#)

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    #name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    jobs = db.relationship("Job", backref="account",lazy=True)

    def __init__(self,username, password):
       # self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True