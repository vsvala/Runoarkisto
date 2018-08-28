from flask_wtf import FlaskForm
from wtforms import widgets, StringField, TextAreaField, validators, ValidationError, SelectMultipleField

from application.runot.models import Runo

class FindForm(FlaskForm):
    name = StringField("nimi", [validators.Length(min=2, max=144)])
    category = StringField("kategoria", [validators.Length(min=2, max=144)])
 
    class Meta:
        csrf = False

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RunoForm(FlaskForm):
    name = StringField("otsikko", [validators.Length(min=2, max=144)])
    sisalto = TextAreaField("sisalto", [validators.Length(min=2, max=2000)]) 
    runoilija = StringField("runoilija", [validators.Length(min=2,max=144)])
    #aihe = StringField("kategoria", [validators.Length(max=144)]) #muokkauksessa tyhjä/ei käytössä
    string_of_files = ['syntymäpäivä\r\ntuparit\r\nkaste\r\nhäät\r\nhautajaiset\r\njoulu\r\nystävä\r\nonnittelu\r\nrakkaus\r\nmuu']
    list_of_files = string_of_files[0].split()
     # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    aihe = MultiCheckboxField('Kategoriat:', choices=files)

    class Meta:
        csrf = False
