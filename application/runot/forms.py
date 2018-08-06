from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class RunoForm(FlaskForm):
    name = StringField("otsikko", [validators.Length(min=2)])
    sisalto = TextAreaField("sisalto", [validators.Length(min=2)]) 
    runoilija = StringField("runoilija", [validators.Length(min=2)])


    class Meta:
        csrf = False