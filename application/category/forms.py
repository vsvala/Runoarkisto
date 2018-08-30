from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField, widgets


class MultiCheckboxField(SelectMultipleField):
    
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()



class CategoryForm(FlaskForm):

   #aihe = StringField("kategoria", [validators.Length(max=144)]) #muokkauksessa tyhjä/ei käytössä
    string_of_files = ['syntymäpäivä\r\ntuparit\r\nkaste\r\nhäät\r\nhautajaiset\r\njoulu\r\nystävä\r\nonnittelu\r\nrakkaus\r\nmuu']
    list_of_files = string_of_files[0].split()
     # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    tokaaihe = MultiCheckboxField('kategoriat:', choices=files)

    aihe = StringField("oma kategoria:", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False