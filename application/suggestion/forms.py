from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.fields.html5 import DateField
  
class SuggestionForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message="Anna vuoron nimi")])
    when = DateField("Milloin")
    location = SelectField("Missä", coerce=int)
  
    class Meta:
        csrf = False
