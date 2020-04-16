from flask_wtf import FlaskForm
from wtforms import StringField, validators,IntegerField,TextAreaField

class JobForm(FlaskForm):
    name = StringField("Job name", [validators.Length(min=3,max=12)])
    salary = IntegerField("Salary")
    description = TextAreaField('Job Description', [validators.Length(max=600)])
  
    class Meta:
        csrf = False