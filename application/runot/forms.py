from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,FileField, validators

class RunoForm(FlaskForm):
    name = StringField("otsikko", [validators.Length(min=2, max=144, message="pituushuono")])
    sisalto = TextAreaField("sisalto", [validators.Length(min=2, max=2000, message="pituushuono")]) 
    runoilija = StringField("runoilija", [validators.Length(min=2,max=144, message="pituushuono" )])

class FindForm(FlaskForm):
    name = StringField("nimi", [validators.Length(min=2, max=144)])
    category = StringField("kategoria", [validators.Length(min=2, max=144)])

class SaveForm(FlaskForm):
    name = StringField("runon nimi", [validators.Length(min=2, max=144)])
    file = StringField("tiedoston nimi", [validators.Length(min=2, max=144)])


class UploadForm(FlaskForm):

    name = StringField("runon nimi", [validators.Length(min=2, max=144)])
    fil = FileField("runon sisältö")
    runoilija = StringField("runoilija", [validators.Length(min=2,max=144 )])

    class Meta:
        csrf = False