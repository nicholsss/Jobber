from flask_wtf import FlaskForm
from wtforms import StringField, validators,IntegerField

class JobForm(FlaskForm):
    name = StringField("Job name", [validators.Length(min=2)])
    salary = IntegerField("Salary")
    description = StringField('Job Description')
  
    class Meta:
        csrf = False