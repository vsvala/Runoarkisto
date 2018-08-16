from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class RunoForm(FlaskForm):
    name = StringField("otsikko", [validators.Length(min=2, max=144)])
    sisalto = TextAreaField("sisalto", [validators.Length(min=2, max=2000)]) 
    runoilija = StringField("runoilija", [validators.Length(min=2,max=144 )])

# class FindForm(FlaskForm):
#     name = StringField("hae runoa", [validators.Length(min=2, max=144)])


    class Meta:
        csrf = False