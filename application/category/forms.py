from flask_wtf import FlaskForm
from wtforms import StringField, validators



class CategoryForm(FlaskForm):

    aihe = StringField("kategoria", [validators.Length(min=2, max=144)])
   
    class Meta:
        csrf = False