from application import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    
    salary = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name,salary):
        self.name = name
        self.salary =salary
        self.active = False