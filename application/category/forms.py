from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, RadioField, SelectMultipleField, validators
from wtforms import Form, widgets, SelectMultipleField

#NÄMÄ TYÖN ALLA
# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()

class CategoryForm(FlaskForm):
    # string_of_files = ['syntymäpäivä\r\ntuparit\r\nkaste\r\nhäät\r\njoulu']
    # list_of_files = string_of_files[0].split()
    #                                                         # create a list of value/description tuples
    # files = [(x, x) for x in list_of_files]
    # aihe = MultiCheckboxField('Kategoriat:', choices=files)

    aihe = StringField("kategoria", [validators.Length(min=2)])
    #aihe=SelectMultipleField(u'kategoria', choices=[('sp', 'syntymäpäivät'), ('tp', 'tuparit'), ('text', 'kaste')], option_widget=None)3#
    #aihe= SelectField(u'kategoria', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    #aihe=RadioField(u'kategoria', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    class Meta:
        csrf = False