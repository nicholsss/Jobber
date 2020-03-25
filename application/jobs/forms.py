from flask_wtf import FlaskForm
from wtforms import StringField, validators,IntegerField

class JobForm(FlaskForm):
    name = StringField("Job name", [validators.Length(min=2)])
    salary = IntegerField("Salary", [validators.Required])
    #Salary pitää vielä katsoa että ottaa vain Integerin vastan.
    class Meta:
        csrf = False