from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField


class questionForm(FlaskForm):
    name = StringField("question job", [validators.Length(min=2)])

    class Meta:
        csrf = False
